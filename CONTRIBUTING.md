# Contributing

Add a library by appending an entry to `libraries.yml`:

```yaml
- name: aiofiles
  repo: Tinche/aiofiles
  pypi: aiofiles
  category: files-io
  description: File support for asyncio
  added: 2026-10-05
```

- `repo` is `owner/name` on GitHub. Libraries hosted elsewhere are not supported yet.
- `pypi` is optional. Without it, the version comes from the latest GitHub release.
- `category` must be one of the ids at the top of the file.
- `description` is one factual sentence of at most 110 characters, no trailing period, no marketing words.
- `added` is today's date. It puts the library in "New this week".

What belongs: libraries that are asyncio-native or document asyncio support, and that are on PyPI or have a real user base. Archived or unmaintained projects are welcome if people still run into them. The status column tells readers.

What does not: tutorials, talks, applications, forks, and wrappers with no users.

Do not edit `README.md`, `news/`, `feed.xml` or `data/` by hand. They are generated. Run `uv run tools/update.py` to check your entry, and `uv run --with pytest --with httpx --with pyyaml pytest` before sending the pull request. CI runs the tests, which also validate `libraries.yml`.

Commits follow conventional commits (`feat:`, `fix:`, `docs:`).
