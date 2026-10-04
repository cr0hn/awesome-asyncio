"""Validates the real libraries.yml, so a bad contribution fails CI."""
from collections import Counter
from pathlib import Path

import yaml

SPEC = yaml.safe_load((Path(__file__).resolve().parent.parent / "libraries.yml").read_text())
IDS = {c["id"] for c in SPEC["categories"]}


def test_every_library_has_required_fields_and_a_known_category():
    for lib in SPEC["libraries"]:
        assert {"name", "repo", "category", "description"} <= set(lib), lib
        assert lib["category"] in IDS, lib
        assert lib["repo"].count("/") == 1, lib


def test_repos_are_unique():
    dupes = [r for r, n in Counter(l["repo"].lower() for l in SPEC["libraries"]).items() if n > 1]
    assert not dupes


def test_descriptions_are_short_and_have_no_trailing_period():
    for lib in SPEC["libraries"]:
        assert len(lib["description"]) <= 110, lib["name"]
        assert not lib["description"].endswith("."), lib["name"]


def test_every_category_is_used():
    used = {l["category"] for l in SPEC["libraries"]}
    assert IDS - used == set()
