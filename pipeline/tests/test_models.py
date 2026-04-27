"""pipeline/tests/test_models.py — 验证数据模型序列化与必填字段"""
import sys
from pathlib import Path

# 加入 pipeline 目录到路径
sys.path.insert(0, str(Path(__file__).parent.parent))

from models import (
    ResearchContext,
    ReviewFeedback,
    ReviewResult,
    SearchResult,
    Source,
)


def test_search_result_roundtrip():
    sr = SearchResult(title="Test", url="https://example.com", snippet="foo", score=0.9, source_engine="tavily")
    data = sr.model_dump()
    sr2 = SearchResult(**data)
    assert sr2.url == sr.url
    assert sr2.score == 0.9


def test_source_footnote_def():
    s = Source(id=3, url="https://hive.com/thread/1", title="JASS Tutorial", accessed_at="2026-04-15T10:00:00+00:00")
    assert s.footnote_def == "[^3]: [JASS Tutorial](https://hive.com/thread/1) — accessed 2026-04-15"


def test_source_dedup_in_context():
    ctx = ResearchContext(topic_id="1", title="Test Topic", category="general", slug="test-topic")
    s1 = ctx.add_source("https://example.com", "Example")
    s2 = ctx.add_source("https://example.com", "Example again")
    assert s1.id == s2.id  # same URL → same source returned
    assert len(ctx.sources) == 1


def test_review_result_overall_score_computed():
    rr = ReviewResult(accuracy=0.8, completeness=0.9, readability=0.7, citation_coverage=0.6, overall_score=0.0)
    expected = round(0.8 * 0.35 + 0.9 * 0.30 + 0.7 * 0.20 + 0.6 * 0.15, 2)
    assert rr.overall_score == expected
    assert rr.passed == (expected >= 0.7)


def test_review_result_passed_flag():
    passing = ReviewResult(accuracy=0.9, completeness=0.9, readability=0.9, citation_coverage=0.9, overall_score=0.9)
    assert passing.passed is True
    failing = ReviewResult(accuracy=0.4, completeness=0.5, readability=0.5, citation_coverage=0.4, overall_score=0.46)
    assert failing.passed is False


def test_research_context_from_topic_entry():
    topic = {"topic_id": "t001", "title": "JASS 触发器入门", "category": "scripting"}
    ctx = ResearchContext.from_topic_entry(topic)
    assert ctx.topic_id == "t001"
    assert ctx.title == "JASS 触发器入门"
    assert ctx.discovered_via == "manual"
    assert ctx.slug  # not empty


def test_research_context_from_topic_with_source():
    topic = {
        "topic_id": "t002",
        "title": "Custom Map Triggers",
        "category": "modding",
        "slug": "custom-map-triggers",
        "source": "reddit",
        "source_urls": ["https://reddit.com/r/WC3/abc"],
    }
    ctx = ResearchContext.from_topic_entry(topic)
    assert ctx.discovered_via == "reddit"
    assert ctx.slug == "custom-map-triggers"
    assert "https://reddit.com/r/WC3/abc" in ctx.source_urls


def test_context_log_error():
    ctx = ResearchContext(topic_id="e1", title="Error Test", category="test", slug="error-test")
    ctx.log_error("PlannerAgent", "LLM timeout")
    assert len(ctx.errors) == 1
    assert ctx.errors[0]["agent"] == "PlannerAgent"


def test_context_get_used_sources():
    ctx = ResearchContext(topic_id="u1", title="Used Sources", category="test", slug="used-sources")
    s1 = ctx.add_source("https://a.com", "A")
    s2 = ctx.add_source("https://b.com", "B")
    s1.used = True
    used = ctx.get_used_sources()
    assert len(used) == 1
    assert used[0].url == "https://a.com"


if __name__ == "__main__":
    test_search_result_roundtrip()
    test_source_footnote_def()
    test_source_dedup_in_context()
    test_review_result_overall_score_computed()
    test_review_result_passed_flag()
    test_research_context_from_topic_entry()
    test_research_context_from_topic_with_source()
    test_context_log_error()
    test_context_get_used_sources()
    print("✅ All model tests passed.")
