import json
import sys
from datetime import date
from pathlib import Path

import httpx
import yaml

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "tools"))
import classify  # noqa: E402

IDS = {"web", "files"}


def test_validate_accepts_a_clean_entry_and_strips_the_period():
    got = classify.validate({"repo": "o/a", "category": "web", "description": "Async web thing."}, {"o/a"}, IDS)
    assert got == {"repo": "o/a", "category": "web", "description": "Async web thing"}


def test_validate_rejects_each_broken_rule():
    ok = {"repo": "o/a", "category": "web", "description": "Async web thing"}
    bad = [
        {**ok, "category": "skip"},
        {**ok, "category": "made-up"},
        {**ok, "repo": "o/other"},
        {**ok, "description": ""},
        {**ok, "description": "x" * 111},
        {**ok, "description": "Fast — and async"},
    ]
    for item in bad:
        assert classify.validate(item, {"o/a"}, IDS) is None, item


def test_system_prompt_carries_the_rules_from_claude_md():
    prompt = classify.system_prompt(ROOT)
    assert "at least 20 stars" in prompt and "110 characters" in prompt


# --- integration: real run() with a fake model and a fake PyPI -------------

SPEC = """
categories:
  - {id: web, title: Web, blurb: Web apps}
  - {id: files, title: Files, blurb: Files}
libraries:
- {name: old, repo: o/old, category: web, description: Already here}
"""
CANDIDATES = [
    {"repo": "o/aioweb", "stars": 90, "archived": False, "pushed": "2026-09-01", "description": "x"},
    {"repo": "o/asyncdemo", "stars": 50, "archived": False, "pushed": "2026-09-01", "description": "demo"},
    {"repo": "o/aiofiles2", "stars": 30, "archived": False, "pushed": "2026-09-01", "description": "x"},
]


def pypi(request: httpx.Request) -> httpx.Response:
    if request.url.path == "/pypi/aioweb/json":
        return httpx.Response(200, json={"info": {"name": "aioweb", "project_urls": {"Source": "https://github.com/o/aioweb"}}})
    if request.url.path == "/pypi/aiofiles2/json":  # same name, different project
        return httpx.Response(200, json={"info": {"name": "aiofiles2", "project_urls": {"Source": "https://github.com/someone/else"}}})
    return httpx.Response(404)


def make_root(tmp_path):
    (tmp_path / "libraries.yml").write_text(SPEC)
    (tmp_path / "CLAUDE.md").write_text((ROOT / "CLAUDE.md").read_text())
    return tmp_path


def fake_model(system, categories, batch):
    answers = {"o/aioweb": ("web", "Async web framework"), "o/asyncdemo": ("skip", ""), "o/aiofiles2": ("files", "Async file helpers")}
    return [{"repo": b["repo"], "category": answers[b["repo"]][0], "description": answers[b["repo"]][1]} for b in batch]


def run(root, cap=40):
    with httpx.Client(transport=httpx.MockTransport(pypi)) as http:
        return classify.run(root, CANDIDATES, fake_model, http, date(2026, 10, 5), cap)


def test_run_appends_accepted_libraries_and_remembers_rejections(tmp_path):
    root = make_root(tmp_path)
    assert run(root) == 2
    libs = {l["repo"]: l for l in yaml.safe_load((root / "libraries.yml").read_text())["libraries"]}
    assert libs["o/aioweb"]["pypi"] == "aioweb" and libs["o/aioweb"]["added"] == date(2026, 10, 5)
    assert "pypi" not in libs["o/aiofiles2"]  # PyPI project does not point back at the repo
    assert libs["o/old"]["description"] == "Already here"
    assert json.loads((root / "data/rejected.json").read_text()) == ["o/asyncdemo"]


def test_second_run_does_not_ask_about_rejected_repos(tmp_path):
    root = make_root(tmp_path)
    run(root)
    asked = []
    def spy(system, categories, batch):
        asked.extend(b["repo"] for b in batch)
        return fake_model(system, categories, batch)
    with httpx.Client(transport=httpx.MockTransport(pypi)) as http:
        classify.run(root, CANDIDATES, spy, http, date(2026, 10, 12), 40)
    assert "o/asyncdemo" not in asked


def test_cap_limits_how_many_are_added(tmp_path):
    root = make_root(tmp_path)
    assert run(root, cap=1) == 1
    assert len(yaml.safe_load((root / "libraries.yml").read_text())["libraries"]) == 2
