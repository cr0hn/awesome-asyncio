import sys
from datetime import datetime, timedelta, timezone
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "tools"))
import update  # noqa: E402

NOW = datetime(2026, 10, 5, 8, 0, tzinfo=timezone.utc)


def iso(days_ago: float) -> str:
    return (NOW - timedelta(days=days_ago)).isoformat()


def test_status_archived_wins_over_recent_commit():
    assert update.status(True, NOW, NOW) == "archived"


def test_status_inactive_after_a_year_and_active_before():
    assert update.status(False, NOW - timedelta(days=366), NOW) == "inactive"
    assert update.status(False, NOW - timedelta(days=364), NOW) == "active"
    assert update.status(False, None, NOW) == "inactive"


def test_stars_formatting():
    assert update.stars(999) == "999"
    assert update.stars(12_345) == "12.3k"
    assert update.stars(None) == "-"


LIBS = [
    {"name": "fresh", "repo": "o/fresh", "description": "d1", "added": iso(2)},
    {"name": "old", "repo": "o/old", "description": "d2"},
    {"name": "edge", "repo": "o/edge", "description": "d3"},
]
RECORDS = {
    "o/fresh": {"url": "u1", "version": "1.0", "version_date": iso(1)},
    "o/old": {"url": "u2", "version": "0.9", "version_date": iso(40)},
    "o/edge": {"url": "u3", "version": "2.0", "version_date": iso(8)},
}


def test_select_news_uses_a_seven_day_window():
    news = update.select_news(LIBS, RECORDS, NOW)
    assert [r["name"] for r in news["releases"]] == ["fresh"]
    assert [a["name"] for a in news["added"]] == ["fresh"]


def test_history_skips_releases_reported_in_an_earlier_week():
    news = update.select_news(LIBS, RECORDS, NOW)
    first = update.update_history([], news, NOW - timedelta(days=7))
    second = update.update_history(first, news, NOW)
    assert second[0]["week"] == "2026-W41"
    assert second[0]["releases"] == [] and second[0]["added"] == []
    assert len(second) == 2


def test_history_rerun_same_week_replaces_entry():
    news = update.select_news(LIBS, RECORDS, NOW)
    once = update.update_history([], news, NOW)
    twice = update.update_history(once, news, NOW)
    assert len(twice) == 1 and twice[0]["releases"]


def test_render_news_empty():
    assert "Nothing new" in update.render_news({"releases": [], "added": []}, "2026-W41")


def test_build_record_keeps_old_values_when_sources_fail():
    old = {"url": "u", "stars": 5, "version": "1.0"}
    rec = update.build_record({"repo": "o/x"}, None, None, old, NOW)
    assert rec["stars"] == 5 and rec["version"] == "1.0"


def test_pypi_version_beats_github_release():
    gh = {"url": "u", "archived": False, "stars": 1, "last_commit": iso(1),
          "release_tag": "v1", "release_date": iso(3)}
    rec = update.build_record({"repo": "o/x"}, gh, {"version": "1.2", "date": iso(2)}, None, NOW)
    assert rec["version"] == "1.2"


def test_render_llms_skips_libraries_without_a_record():
    cats = [{"id": "web", "title": "Web", "blurb": "b"}]
    libs = [{"name": "x", "repo": "o/x", "category": "web", "description": "d"}]
    out = update.render_llms(cats, libs, {}, datetime(2026, 10, 5, tzinfo=timezone.utc))
    assert "x |" not in out and "1 inactive or archived" in out
