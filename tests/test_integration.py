"""Runs the whole pipeline against fake GitHub and PyPI servers."""
import asyncio
import json
import re
import sys
from datetime import datetime, timedelta, timezone
from pathlib import Path

import httpx

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "tools"))
import update  # noqa: E402

NOW = datetime(2026, 10, 5, 8, 0, tzinfo=timezone.utc)


def iso(days_ago):
    return (NOW - timedelta(days=days_ago)).strftime("%Y-%m-%dT%H:%M:%SZ")


SPEC = """
categories:
  - {id: web, title: Web frameworks, blurb: Build web apps.}
  - {id: files, title: Files and I/O, blurb: Async files.}
libraries:
  - {name: alpha, repo: o/alpha, pypi: alpha, category: web, description: Alpha does web}
  - {name: beta, repo: o/beta, category: files, description: Beta does files, added: 2026-10-03}
  - {name: gone, repo: o/gone, category: files, description: Deleted upstream}
"""

GITHUB = {
    "o/alpha": {"nameWithOwner": "o/alpha", "url": "https://github.com/o/alpha", "isArchived": False,
                "stargazerCount": 1500, "defaultBranchRef": {"target": {"committedDate": iso(3)}},
                "latestRelease": None},
    "o/beta": {"nameWithOwner": "o/beta", "url": "https://github.com/o/beta", "isArchived": True,
               "stargazerCount": 20, "defaultBranchRef": {"target": {"committedDate": iso(900)}},
               "latestRelease": {"tagName": "v0.3", "publishedAt": iso(2)}},
}


def handler(request: httpx.Request) -> httpx.Response:
    if request.url.host == "api.github.com":
        query = json.loads(request.content)["query"]
        data = {}
        for alias, owner, name in re.findall(r'(r\d+): repository\(owner: "([^"]+)", name: "([^"]+)"', query):
            data[alias] = GITHUB.get(f"{owner}/{name}")
        return httpx.Response(200, json={"data": data})
    if request.url.path == "/pypi/alpha/json":
        return httpx.Response(200, json={"info": {"version": "2.1.0"},
                                         "urls": [{"upload_time_iso_8601": iso(1)}]})
    return httpx.Response(404)


def make_root(tmp_path):
    (tmp_path / "templates").mkdir()
    (tmp_path / "templates/README.md.tmpl").write_text((ROOT / "templates/README.md.tmpl").read_text())
    (tmp_path / "libraries.yml").write_text(SPEC)
    return tmp_path


def run(root):
    async def go():
        async with httpx.AsyncClient(transport=httpx.MockTransport(handler)) as client:
            return await update.run(root, client, "token", NOW)
    return asyncio.run(go())


def test_pipeline_writes_readme_news_and_feed(tmp_path):
    root = make_root(tmp_path)
    report = run(root)
    readme = (root / "README.md").read_text()

    assert report["stale"] == ["o/gone"]
    assert "{{" not in readme
    # New this week comes before the libraries and lists both the release and the added library
    news_pos, libs_pos = readme.index("## New this week"), readme.index("## Libraries")
    assert news_pos < libs_pos
    news_block = readme[news_pos:libs_pos]
    assert "| [alpha](https://github.com/o/alpha) | 2.1.0 |" in news_block
    assert "[beta](https://github.com/o/beta): Beta does files" in news_block
    # Table rows: active shows commit date and PyPI version, archived shows the marker
    assert "| [alpha](https://github.com/o/alpha) | Alpha does web | ✅ |" in readme
    assert "1.5k" in readme
    assert "| [beta](https://github.com/o/beta) | Beta does files | 🗄️ |" in readme
    # A repo missing upstream still renders, with placeholders
    assert "| [gone](https://github.com/o/gone) | Deleted upstream | 💤 | - | - | - |" in readme

    assert (root / "news/2026-W41.md").exists()
    feed = (root / "feed.xml").read_text()
    assert "alpha 2.1.0" in feed and "<feed" in feed


def test_second_run_keeps_cached_values_when_github_fails(tmp_path):
    root = make_root(tmp_path)
    run(root)
    GITHUB_BACKUP = dict(GITHUB)
    GITHUB.clear()
    try:
        report = run(root)
    finally:
        GITHUB.update(GITHUB_BACKUP)
    assert set(report["stale"]) == {"o/alpha", "o/beta", "o/gone"}
    assert "| [beta](https://github.com/o/beta) | Beta does files | 🗄️ |" in (root / "README.md").read_text()


def test_invalid_repo_name_is_rejected_before_any_request(tmp_path):
    root = make_root(tmp_path)
    (root / "libraries.yml").write_text(SPEC.replace("o/alpha", "o/al pha"))
    try:
        run(root)
    except ValueError as exc:
        assert "invalid repo names" in str(exc)
    else:
        raise AssertionError("expected ValueError")
