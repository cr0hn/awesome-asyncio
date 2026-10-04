# /// script
# requires-python = ">=3.11"
# dependencies = ["httpx", "pyyaml"]
# ///
"""List Python repos named aio*/async* with 20+ stars that are not in libraries.yml.

Usage: uv run tools/discover.py > candidates.yml
Claude then picks a category and writes a description for each one.
"""
from __future__ import annotations

import os
import re
import subprocess
import sys
import time
from pathlib import Path

import httpx
import yaml

MIN_STARS = 20
PREFIX = re.compile(r"^(aio|async)", re.I)
# GitHub search returns at most 1000 results per query, so split by star range.
RANGES = ["20..24", "25..29", "30..39", "40..49", "50..74", "75..99", "100..199", "200..499", "500..999", ">=1000"]


def token() -> str:
    return os.environ.get("GITHUB_TOKEN") or subprocess.check_output(["gh", "auth", "token"], text=True).strip()


def search(client: httpx.Client, word: str, stars: str) -> list[dict]:
    items = []
    for page in range(1, 11):
        for attempt in range(3):
            r = client.get("/search/repositories", params={
                "q": f"{word} in:name language:python stars:{stars} fork:false",
                "sort": "stars", "per_page": 100, "page": page})
            if r.status_code in (403, 429):  # search API allows 30 requests a minute
                time.sleep(30)
                continue
            r.raise_for_status()
            break
        batch = r.json()["items"]
        items += batch
        if len(batch) < 100:
            break
        time.sleep(2)
    if len(items) >= 1000:
        print(f"warning: {word} stars:{stars} hit the 1000 result cap", file=sys.stderr)
    return items


def find(root: Path) -> list[dict]:
    have = {l["repo"].lower() for l in yaml.safe_load((root / "libraries.yml").read_text())["libraries"]}
    found: dict[str, dict] = {}
    with httpx.Client(base_url="https://api.github.com", timeout=30,
                      headers={"Authorization": f"Bearer {token()}", "Accept": "application/vnd.github+json"}) as client:
        for word in ("aio", "async"):
            for stars in RANGES:
                for it in search(client, word, stars):
                    full = it["full_name"]
                    if PREFIX.match(it["name"]) and it["stargazers_count"] >= MIN_STARS and full.lower() not in have:
                        found[full] = {"repo": full, "stars": it["stargazers_count"], "archived": it["archived"],
                                       "pushed": it["pushed_at"][:10], "description": (it["description"] or "").strip()}
    return sorted(found.values(), key=lambda r: -r["stars"])


def main() -> None:
    rows = find(Path(__file__).resolve().parent.parent)
    print(yaml.safe_dump(rows, sort_keys=False, allow_unicode=True, width=200))
    print(f"{len(rows)} candidates", file=sys.stderr)


if __name__ == "__main__":
    main()
