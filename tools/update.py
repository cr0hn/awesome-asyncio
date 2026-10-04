# /// script
# requires-python = ">=3.11"
# dependencies = ["httpx", "pyyaml"]
# ///
"""Refresh library metadata and regenerate README.md, news/ and feed.xml.

Source of truth: libraries.yml. Cache: data/metadata.json, data/news.json.
Usage: uv run tools/update.py
"""
from __future__ import annotations

import asyncio
import json
import os
import re
import subprocess
from datetime import datetime, timedelta, timezone
from pathlib import Path
from xml.sax.saxutils import escape

import httpx
import yaml

REPO = "cr0hn/awesome-asyncio"
WINDOW_DAYS = 7
INACTIVE_DAYS = 365
NEWS_CAP = 25
HISTORY_WEEKS = 26
BATCH = 40
REPO_RE = re.compile(r"^[\w.-]+/[\w.-]+$")
LEGEND = {"active": "✅", "inactive": "💤", "archived": "🗄️"}


def parse_dt(value) -> datetime | None:
    if not value:
        return None
    if not isinstance(value, str):  # YAML turns 2026-10-03 into a date
        value = value.isoformat()
    dt = datetime.fromisoformat(value.replace("Z", "+00:00"))
    return (dt if dt.tzinfo else dt.replace(tzinfo=timezone.utc)).astimezone(timezone.utc)


def day(dt: datetime | None) -> str:
    return dt.strftime("%Y-%m-%d") if dt else "-"


def status(archived: bool, last_commit: datetime | None, now: datetime) -> str:
    if archived:
        return "archived"
    if last_commit is None or now - last_commit > timedelta(days=INACTIVE_DAYS):
        return "inactive"
    return "active"


def stars(n: int | None) -> str:
    if n is None:
        return "-"
    return f"{n / 1000:.1f}k" if n >= 1000 else str(n)


# --- fetching -------------------------------------------------------------

def _query(repos: list[str]) -> str:
    parts = []
    for i, repo in enumerate(repos):
        owner, name = repo.split("/")
        parts.append(
            f'r{i}: repository(owner: "{owner}", name: "{name}") {{ nameWithOwner url isArchived '
            "stargazerCount defaultBranchRef { target { ... on Commit { committedDate } } } "
            "latestRelease { tagName publishedAt } }"
        )
    return "query { " + " ".join(parts) + " }"


async def fetch_github(client: httpx.AsyncClient, token: str, repos: list[str]) -> dict[str, dict]:
    out: dict[str, dict] = {}
    for start in range(0, len(repos), BATCH):
        chunk = repos[start : start + BATCH]
        resp = await client.post(
            "https://api.github.com/graphql",
            json={"query": _query(chunk)},
            headers={"Authorization": f"bearer {token}"},
        )
        resp.raise_for_status()
        data = resp.json().get("data") or {}
        for i, repo in enumerate(chunk):
            node = data.get(f"r{i}")
            if not node:
                continue
            branch = (node.get("defaultBranchRef") or {}).get("target") or {}
            release = node.get("latestRelease") or {}
            out[repo] = {
                "url": node["url"],
                "archived": node["isArchived"],
                "stars": node["stargazerCount"],
                "last_commit": branch.get("committedDate"),
                "release_tag": release.get("tagName"),
                "release_date": release.get("publishedAt"),
            }
    return out


async def fetch_pypi(client: httpx.AsyncClient, names: list[str]) -> dict[str, dict]:
    sem = asyncio.Semaphore(10)

    async def one(name: str) -> tuple[str, dict | None]:
        async with sem:
            try:
                resp = await client.get(f"https://pypi.org/pypi/{name}/json")
            except httpx.HTTPError:
                return name, None
        if resp.status_code != 200:
            return name, None
        data = resp.json()
        files = data.get("urls") or []
        uploaded = max((f["upload_time_iso_8601"] for f in files), default=None)
        return name, {"version": data["info"]["version"], "date": uploaded}

    results = await asyncio.gather(*(one(n) for n in names))
    return {n: r for n, r in results if r}


# --- records and news ------------------------------------------------------

def build_record(lib: dict, gh: dict | None, pypi: dict | None, old: dict | None, now: datetime) -> dict:
    """Combine fresh data; fall back to the cached record when a source failed."""
    rec = dict(old or {})
    if gh:
        rec.update(url=gh["url"], archived=gh["archived"], stars=gh["stars"], last_commit=gh["last_commit"])
        rec.update(version=gh["release_tag"], version_date=gh["release_date"])
    if pypi:
        rec.update(version=pypi["version"], version_date=pypi["date"])
    rec.setdefault("url", f"https://github.com/{lib['repo']}")
    return rec


def select_news(libs: list[dict], records: dict[str, dict], now: datetime) -> dict:
    cutoff = now - timedelta(days=WINDOW_DAYS)
    releases, added = [], []
    for lib in libs:
        rec = records.get(lib["repo"]) or {}
        released = parse_dt(rec.get("version_date"))
        if released and released >= cutoff and rec.get("version"):
            releases.append({"name": lib["name"], "repo": lib["repo"], "url": rec["url"],
                             "version": rec["version"], "date": day(released), "description": lib["description"]})
        joined = parse_dt(lib.get("added"))
        if joined and joined >= cutoff:
            added.append({"name": lib["name"], "repo": lib["repo"], "url": rec.get("url", ""),
                          "description": lib["description"]})
    releases.sort(key=lambda r: r["date"], reverse=True)
    return {"releases": releases, "added": added}


def week_id(now: datetime) -> str:
    year, week, _ = now.isocalendar()
    return f"{year}-W{week:02d}"


def update_history(history: list[dict], news: dict, now: datetime) -> list[dict]:
    """Add this week's entry; drop releases already reported in an earlier week."""
    wid = week_id(now)
    previous = [h for h in history if h["week"] != wid]
    seen = {(r["repo"], r["version"]) for h in previous for r in h["releases"]}
    seen_added = {a["repo"] for h in previous for a in h["added"]}
    entry = {
        "week": wid,
        "date": day(now),
        "releases": [r for r in news["releases"] if (r["repo"], r["version"]) not in seen],
        "added": [a for a in news["added"] if a["repo"] not in seen_added],
    }
    return ([entry] + previous)[:HISTORY_WEEKS]


# --- rendering -------------------------------------------------------------

def anchor(title: str) -> str:
    return re.sub(r"[^\w\- ]", "", title.lower()).replace(" ", "-")


def render_news(news: dict, wid: str) -> str:
    if not news["releases"] and not news["added"]:
        return "Nothing new in the last 7 days."
    lines = []
    if news["added"]:
        lines += ["**New in the list**", ""]
        lines += [f"- [{a['name']}]({a['url']}): {a['description']}" for a in news["added"]]
        lines.append("")
    if news["releases"]:
        lines += ["**New releases**", "", "| Library | Description | Version | Date |", "|---|---|---|---|"]
        shown = news["releases"][:NEWS_CAP]
        lines += [f"| [{r['name']}]({r['url']}) | {r.get('description', '')} | {r['version']} | {r['date']} |" for r in shown]
        extra = len(news["releases"]) - len(shown)
        if extra > 0:
            lines += ["", f"{extra} more in [news/{wid}.md](news/{wid}.md)."]
    return "\n".join(lines).rstrip()


def render_libraries(cats: list[dict], libs: list[dict], records: dict[str, dict], now: datetime) -> tuple[str, str]:
    index, body = [], []
    for cat in cats:
        items = [l for l in libs if l["category"] == cat["id"]]
        if not items:
            continue

        def key(lib):
            rec = records.get(lib["repo"]) or {}
            return (bool(rec.get("archived")), -(rec.get("stars") or 0))

        items.sort(key=key)
        index.append(f"  - [{cat['title']}](#{anchor(cat['title'])}) ({len(items)})")
        body += [f"### {cat['title']}", "", cat["blurb"], "",
                 "| Library | Description | Status | Last commit | Latest version | Stars |",
                 "|---|---|:-:|---|---|--:|"]
        for lib in items:
            rec = records.get(lib["repo"]) or {}
            last = parse_dt(rec.get("last_commit"))
            st = LEGEND[status(bool(rec.get("archived")), last, now)] if rec else "-"
            body.append(
                f"| [{lib['name']}]({rec.get('url') or 'https://github.com/' + lib['repo']}) "
                f"| {lib['description']} | {st} | {day(last)} | {rec.get('version') or '-'} | {stars(rec.get('stars'))} |"
            )
        body.append("")
    return "\n".join(index), "\n".join(body).rstrip()


def render_llms(cats: list[dict], libs: list[dict], records: dict[str, dict], now: datetime) -> str:
    """Compact text for LLMs: active libraries only, best starred first, one line each."""
    out = ["# awesome-asyncio",
           "",
           "> Python asyncio libraries by task. Use it to pick one when unsure. Line format: name | PyPI package | stars | last commit | description. Only libraries with a commit in the last year are listed, so none here is archived. Full table: README.md",
           ""]
    skipped = 0
    for cat in cats:
        rows = []
        for lib in (l for l in libs if l["category"] == cat["id"]):
            rec = records.get(lib["repo"]) or {}
            if not rec or status(bool(rec.get("archived")), parse_dt(rec.get("last_commit")), now) != "active":
                skipped += 1
                continue
            rows.append((rec.get("stars") or 0, f"{lib['name']} | {lib.get('pypi') or '-'} | {rec.get('stars') or 0} | "
                         f"{day(parse_dt(rec.get('last_commit')))} | {lib['description']}"))
        if rows:
            out += [f"## {cat['title']}", ""] + [r for _, r in sorted(rows, key=lambda x: -x[0])] + [""]
    out.append(f"{skipped} inactive or archived libraries are left out. See README.md for them.")
    out += ["", "## Author", "",
            "Maintained by Daniel Alfocea (cr0hn), a Python and cybersecurity expert. "
            "Website: https://danielalfocea.com . GitHub: https://github.com/cr0hn . Contact: Daniel@danielalfocea.com"]
    return "\n".join(out) + "\n"


def render_feed(history: list[dict], now: datetime) -> str:
    entries = []
    for h in history:
        lines = [f"New: {a['name']}: {a['description']}" for a in h["added"]]
        lines += [f"{r['name']} {r['version']} ({r['date']})" for r in h["releases"]]
        if not lines:
            continue
        link = f"https://github.com/{REPO}/blob/main/news/{h['week']}.md"
        entries.append(
            "<entry>"
            f"<id>tag:github.com,2026:{REPO}:{h['week']}</id>"
            f"<title>Week {h['week']}</title>"
            f'<link href="{link}"/>'
            f"<updated>{h['date']}T00:00:00Z</updated>"
            f"<summary type=\"text\">{escape(chr(10).join(lines))}</summary>"
            "</entry>"
        )
    return (
        '<?xml version="1.0" encoding="utf-8"?>\n<feed xmlns="http://www.w3.org/2005/Atom">'
        f"<id>tag:github.com,2026:{REPO}</id><title>awesome-asyncio: weekly news</title>"
        f'<link href="https://github.com/{REPO}"/><updated>{day(now)}T00:00:00Z</updated>'
        + "".join(entries)
        + "</feed>\n"
    )


def render_week_file(entry: dict) -> str:
    lines = [f"# Week {entry['week']}", ""]
    if entry["added"]:
        lines += ["## New in the list", ""]
        lines += [f"- [{a['name']}]({a['url']}): {a['description']}" for a in entry["added"]]
        lines.append("")
    lines += ["## New releases", ""]
    if entry["releases"]:
        lines += ["| Library | Description | Version | Date |", "|---|---|---|---|"]
        lines += [f"| [{r['name']}]({r['url']}) | {r.get('description', '')} | {r['version']} | {r['date']} |" for r in entry["releases"]]
    else:
        lines.append("No new releases.")
    return "\n".join(lines) + "\n"


# --- pipeline ----------------------------------------------------------------

def read_json(path: Path, default):
    return json.loads(path.read_text()) if path.exists() else default


async def run(root: Path, client: httpx.AsyncClient, token: str, now: datetime) -> dict:
    spec = yaml.safe_load((root / "libraries.yml").read_text())
    libs, cats = spec["libraries"], spec["categories"]
    bad = [l["repo"] for l in libs if not REPO_RE.match(l["repo"])]
    if bad:
        raise ValueError(f"invalid repo names: {bad}")
    ids = {c["id"] for c in cats}
    unknown = [l["name"] for l in libs if l["category"] not in ids]
    if unknown:
        raise ValueError(f"unknown category: {unknown}")

    old = read_json(root / "data/metadata.json", {})
    gh = await fetch_github(client, token, [l["repo"] for l in libs])
    pypi = await fetch_pypi(client, sorted({l["pypi"] for l in libs if l.get("pypi")}))
    records = {l["repo"]: build_record(l, gh.get(l["repo"]), pypi.get(l.get("pypi")), old.get(l["repo"]), now)
               for l in libs}
    stale = [l["repo"] for l in libs if l["repo"] not in gh]

    news = select_news(libs, records, now)
    history = update_history(read_json(root / "data/news.json", []), news, now)

    index, body = render_libraries(cats, libs, records, now)
    readme = (root / "templates/README.md.tmpl").read_text()
    for key, value in {
        "{{NEWS}}": render_news(news, week_id(now)),
        "{{INDEX}}": index,
        "{{LIBRARIES}}": body,
        "{{COUNT}}": str(len(libs)),
        "{{UPDATED}}": day(now).replace("-", "--"),  # shields.io escapes a hyphen as two
    }.items():
        readme = readme.replace(key, value)

    (root / "README.md").write_text(readme)
    (root / "data").mkdir(exist_ok=True)
    (root / "news").mkdir(exist_ok=True)
    (root / "data/metadata.json").write_text(json.dumps(records, indent=1, sort_keys=True) + "\n")
    (root / "data/news.json").write_text(json.dumps(history, indent=1) + "\n")
    (root / f"news/{history[0]['week']}.md").write_text(render_week_file(history[0]))
    (root / "feed.xml").write_text(render_feed(history, now))
    (root / "llms.txt").write_text(render_llms(cats, libs, records, now))
    return {"libraries": len(libs), "stale": stale, "no_pypi": [l["name"] for l in libs if l.get("pypi") and l["pypi"] not in pypi]}


def github_token() -> str:
    token = os.environ.get("GITHUB_TOKEN")
    if token:
        return token
    return subprocess.run(["gh", "auth", "token"], capture_output=True, text=True, check=True).stdout.strip()


async def main() -> None:
    root = Path(__file__).resolve().parent.parent
    async with httpx.AsyncClient(timeout=30) as client:
        report = await run(root, client, github_token(), datetime.now(timezone.utc))
    print(json.dumps(report, indent=1))


if __name__ == "__main__":
    asyncio.run(main())
