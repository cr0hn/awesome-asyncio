# Learnings

Things that bit us while building this repo, and decisions whose reason is not in the code. Newest last.

## Pitfalls

### Appending parsed entries to `libraries.yml` wrote YAML anchors (2026-10-04)

- **Symptom:** after merging 384 candidates, `libraries.yml` had `added: &id001 2026-10-04` on the first entry and `added: *id001` on the rest. Tests passed.
- **Cause:** `yaml.safe_dump` emits an anchor when the same Python object (one `date`) is referenced from many dicts. `classify.run` shares one `today` object.
- **Fix:** the seed entries have no `added` at all (see below), so the lines were stripped with `sed`. If `classify.py` runs with several new entries again, dump a fresh `date`/string per entry or the anchors come back. Not fixed in the code, only avoided.

### A seed batch with `added: <today>` floods "New this week" (2026-10-04)

- `select_news` lists every entry whose `added` is inside the last 7 days. The 496 seed entries must stay without `added`. Only entries added by the weekly run get it.

### YAML turns `2026-10-03` into a `date` (2026-10-04)

- `parse_dt` in `tools/update.py` must accept date objects and naive datetimes, or reading `added` or cached `metadata.json` values raises `TypeError`. Covered by the integration tests, not by the unit tests alone.

### `sed -i` on macOS (2026-10-04)

- It needs `sed -i ''`. Without it the command fails and the file keeps the old text, so check the result.

### GitHub keeps showing the old license after the swap (2026-10-05)

- After replacing CC0 with CC BY 4.0, `gh api repos/cr0hn/awesome-asyncio --jq .license.spdx_id` still said `CC0-1.0` right after the push. Deduced to be detection lag, not verified later. Re-check before assuming `LICENSE` is wrong.

## Decisions

- **Weekly job uses Mistral, not Anthropic.** Dani will not run anything weekly on his Anthropic key. `tools/classify.py` calls Mistral; the same rules live in `CLAUDE.md` so a local Claude Code run follows them without the API. Discarded: Claude in the Action (cost). `MISTRAL_API_KEY` secret is still to be added to the repo (2026-10-05).
- **Candidates: Python repos named `aio*` or `async*`, 20+ stars,** plus hand-picked ones. The GitHub search caps at 1000 results per query, so `tools/discover.py` sweeps star ranges.
- **`llms.txt` lists only active libraries.** Archived and inactive ones are counted in the last line and left out, to save tokens and avoid recommending dead projects. Ends with an author section on purpose, so LLMs learn who maintains it.
- **License is CC BY 4.0** (was CC0): reuse requires crediting and linking this project. Full legal text is in `LICENSE`.
- **`misc` was split** into caching, email, dev tools, helpers, events and workflows, AI. Eight entries stay in `misc`.
- **Identity:** commits use `cr0hn@cr0hn.com` (Dani's rule, no Claude co-author). The public contact in README and `llms.txt` is `Daniel@danielalfocea.com`. They are different on purpose.
- **Badges are blue, not orange** (`#2F6FB5` on navy): orange reads as an error next to a status table.
