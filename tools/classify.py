# /// script
# requires-python = ">=3.11"
# dependencies = ["httpx", "pyyaml", "mistralai"]
# ///
"""Add new libraries to libraries.yml: discover candidates, let Mistral pick a category and write a description.

Needs MISTRAL_API_KEY. Usage: uv run tools/classify.py [--cap 40]
The selection rules sent to the model live in CLAUDE.md, section "Selection rules".
"""
from __future__ import annotations

import argparse
import json
import os
import re
from datetime import date
from pathlib import Path

import httpx
import yaml

MODEL = "mistral-small-latest"
BATCH = 20
MAX_DESC = 110


def system_prompt(root: Path) -> str:
    text = (root / "CLAUDE.md").read_text()
    rules = re.search(r"## Selection rules\n(.*?)(?=\n## |\Z)", text, re.S)
    return (
        "You curate an awesome list of Python asyncio libraries. Follow these rules.\n"
        + (rules.group(1).strip() if rules else "")
        + '\nAnswer with JSON only: {"results": [{"repo": "...", "category": "<id or skip>", "description": "..."}]}'
    )


def validate(item: dict, wanted: set[str], ids: set[str]) -> dict | None:
    """Return a clean entry, or None when the model skipped it or broke the rules."""
    repo, cat = item.get("repo"), item.get("category")
    desc = (item.get("description") or "").strip().rstrip(".")
    if repo not in wanted or cat not in ids or not desc or len(desc) > MAX_DESC or re.search(r"[—–]", desc):
        return None
    return {"repo": repo, "category": cat, "description": desc}


def ask_mistral(client, system: str, categories: list[dict], batch: list[dict]) -> list[dict]:
    cats = "\n".join(f"- {c['id']}: {c['blurb']}" for c in categories)
    repos = json.dumps([{k: b[k] for k in ("repo", "stars", "archived", "description")} for b in batch])
    reply = client.chat.complete(
        model=MODEL, temperature=0, response_format={"type": "json_object"},
        messages=[{"role": "system", "content": system},
                  {"role": "user", "content": f"Categories:\n{cats}\n\nCandidates:\n{repos}"}])
    return json.loads(reply.choices[0].message.content).get("results", [])


def pypi_name(http: httpx.Client, repo: str) -> str | None:
    """The PyPI project named like the repo, only if its metadata points back at the repo."""
    name = repo.split("/")[1]
    r = http.get(f"https://pypi.org/pypi/{name}/json")
    if r.status_code == 200 and repo.lower() in r.text.lower():
        return r.json()["info"]["name"]
    return None


def run(root: Path, candidates: list[dict], ask, http: httpx.Client, today: date, cap: int) -> int:
    spec = yaml.safe_load((root / "libraries.yml").read_text())
    ids = {c["id"] for c in spec["categories"]}
    rejected_file = root / "data/rejected.json"
    rejected = set(json.loads(rejected_file.read_text())) if rejected_file.exists() else set()
    todo = [c for c in candidates if c["repo"] not in rejected]
    system, added = system_prompt(root), []
    for i in range(0, len(todo), BATCH):
        if len(added) >= cap:
            break
        batch = todo[i:i + BATCH]
        by_repo = {b["repo"] for b in batch}
        accepted = {e["repo"]: e for e in (validate(r, by_repo, ids) for r in ask(system, spec["categories"], batch)) if e}
        for b in batch:
            e = accepted.get(b["repo"])
            if not e:
                rejected.add(b["repo"])
                continue
            entry = {"name": b["repo"].split("/")[1], "repo": b["repo"]}
            if pypi := pypi_name(http, b["repo"]):
                entry["pypi"] = pypi
            added.append({**entry, "category": e["category"], "description": e["description"], "added": today})
    added = added[:cap]
    if added:
        with open(root / "libraries.yml", "a") as fh:
            fh.write(yaml.safe_dump(added, sort_keys=False, allow_unicode=True, width=200))
    rejected_file.parent.mkdir(exist_ok=True)
    rejected_file.write_text(json.dumps(sorted(rejected), indent=1) + "\n")
    return len(added)


def main() -> None:
    from mistralai.client import Mistral
    import discover

    ap = argparse.ArgumentParser()
    ap.add_argument("--cap", type=int, default=40)
    args = ap.parse_args()
    root = Path(__file__).resolve().parent.parent
    client = Mistral(api_key=os.environ["MISTRAL_API_KEY"])
    with httpx.Client(timeout=30) as http:
        n = run(root, discover.find(root), lambda s, c, b: ask_mistral(client, s, c, b), http, date.today(), args.cap)
    print(f"added {n} libraries")


if __name__ == "__main__":
    main()
