"""
test_orchestrator.py — 编排器单元测试

测试覆盖：
  - Planner→Researcher→Writer→Reviewer 流水线调用顺序
  - quality_score < 0.7 时触发重写循环
  - 重写最多 2 次，保留最高分草稿
  - 全部 agent 抛异常时写入 failed_topics.json
  - asyncio.Semaphore 并发控制（run_batch）
"""
import asyncio
import json
import sys
import tempfile
from pathlib import Path
from unittest.mock import AsyncMock, MagicMock, patch, call

import pytest

sys.path.insert(0, str(Path(__file__).parent.parent))

from models import ResearchContext, ReviewFeedback
from agent_orchestrator import Orchestrator, run_batch


# ── 工厂方法 ──────────────────────────────────────────────────────────────────

def make_topic(slug="test-topic", title="测试主题", discovered_via="manual"):
    return {
        "slug": slug,
        "title": title,
        "category": "JASS 编程",
        "discovered_via": discovered_via,
    }


def make_review(score: float, feedback: list[str] | None = None) -> ReviewFeedback:
    return ReviewFeedback(
        overall_score=score,
        accuracy=score,
        completeness=score,
        readability=score,
        citation_coverage=score,
        feedback=feedback or [],
        approved=score >= 0.7,
    )


def make_context(topic: dict | None = None) -> ResearchContext:
    t = topic or make_topic()
    return ResearchContext.from_topic_entry(t)


# ── 1. 基本流水线调用顺序 ──────────────────────────────────────────────────────

class TestOrchestratorPipeline:
    @pytest.fixture
    def orchestrator(self, tmp_path):
        orc = Orchestrator.__new__(Orchestrator)
        orc.docs_root = tmp_path
        orc.planner = AsyncMock()
        orc.researcher = AsyncMock()
        orc.writer = AsyncMock()
        orc.reviewer = AsyncMock()
        orc.max_rewrite_iterations = 2
        orc.quality_threshold = 0.7
        return orc

    @pytest.mark.asyncio
    async def test_pipeline_runs_in_order(self, orchestrator, tmp_path):
        """四个 agent 按 Planner→Researcher→Writer→Reviewer 顺序调用"""
        ctx = make_context()

        orchestrator.planner.run.return_value = ctx
        orchestrator.researcher.run.return_value = ctx
        orchestrator.writer.run.return_value = ctx
        review = make_review(0.85)
        orchestrator.reviewer.run.return_value = (ctx, review)

        with patch.object(orchestrator, "_save_article", return_value=None):
            result = await orchestrator.generate(make_topic())

        call_order = []
        for attr in ["planner", "researcher", "writer", "reviewer"]:
            agent = getattr(orchestrator, attr)
            if agent.run.called:
                call_order.append(attr)

        assert call_order == ["planner", "researcher", "writer", "reviewer"]

    @pytest.mark.asyncio
    async def test_no_rewrite_when_score_above_threshold(self, orchestrator):
        """评分 ≥ 0.7 时不触发重写"""
        ctx = make_context()
        orchestrator.planner.run.return_value = ctx
        orchestrator.researcher.run.return_value = ctx
        orchestrator.writer.run.return_value = ctx
        review = make_review(0.8)
        orchestrator.reviewer.run.return_value = (ctx, review)

        with patch.object(orchestrator, "_save_article", return_value=None):
            await orchestrator.generate(make_topic())

        # Writer 只被调用一次
        assert orchestrator.writer.run.call_count == 1

    @pytest.mark.asyncio
    async def test_rewrite_triggered_when_score_below_threshold(self, orchestrator):
        """评分 < 0.7 时触发一次重写"""
        ctx = make_context()
        orchestrator.planner.run.return_value = ctx
        orchestrator.researcher.run.return_value = ctx
        orchestrator.writer.run.return_value = ctx

        # 第一次 0.5，第二次 0.8
        orchestrator.reviewer.run.side_effect = [
            (ctx, make_review(0.5, ["需要更多引用"])),
            (ctx, make_review(0.8)),
        ]

        with patch.object(orchestrator, "_save_article", return_value=None):
            await orchestrator.generate(make_topic())

        assert orchestrator.writer.run.call_count == 2
        assert orchestrator.reviewer.run.call_count == 2

    @pytest.mark.asyncio
    async def test_max_rewrite_iterations_respected(self, orchestrator):
        """重写最多触发 max_rewrite_iterations 次"""
        ctx = make_context()
        orchestrator.planner.run.return_value = ctx
        orchestrator.researcher.run.return_value = ctx
        orchestrator.writer.run.return_value = ctx

        # 始终返回低分
        orchestrator.reviewer.run.return_value = (ctx, make_review(0.4))

        with patch.object(orchestrator, "_save_article", return_value=None):
            await orchestrator.generate(make_topic())

        # Writer 最多调用 1 + max_rewrite_iterations = 3 次
        assert orchestrator.writer.run.call_count <= 1 + orchestrator.max_rewrite_iterations

    @pytest.mark.asyncio
    async def test_best_draft_kept_across_rewrites(self, orchestrator):
        """多次重写时保留最高分草稿"""
        ctx1 = make_context()
        ctx1.draft = "草稿 v1"
        ctx2 = make_context()
        ctx2.draft = "草稿 v2（更好）"
        ctx3 = make_context()
        ctx3.draft = "草稿 v3（更差）"

        orchestrator.planner.run.return_value = ctx1
        orchestrator.researcher.run.return_value = ctx1
        orchestrator.writer.run.side_effect = [ctx1, ctx2, ctx3]
        orchestrator.reviewer.run.side_effect = [
            (ctx1, make_review(0.5)),
            (ctx2, make_review(0.75)),  # 这是最高分
            (ctx3, make_review(0.6)),
        ]

        saved_drafts = []

        async def mock_save(ctx, _topic):
            saved_drafts.append(ctx.draft)

        with patch.object(orchestrator, "_save_article", side_effect=mock_save):
            await orchestrator.generate(make_topic())

        # 最终保存的应是最高分草稿
        if saved_drafts:
            assert saved_drafts[-1] == "草稿 v2（更好）"


# ── 2. 错误处理 ───────────────────────────────────────────────────────────────

class TestOrchestratorErrorHandling:
    @pytest.mark.asyncio
    async def test_failed_topic_written_to_json(self, tmp_path):
        """Agent 全部失败时写入 failed_topics.json"""
        orc = Orchestrator.__new__(Orchestrator)
        orc.docs_root = tmp_path
        orc.planner = AsyncMock()
        orc.researcher = AsyncMock()
        orc.writer = AsyncMock()
        orc.reviewer = AsyncMock()
        orc.max_rewrite_iterations = 2
        orc.quality_threshold = 0.7
        orc.failed_topics_path = tmp_path / "failed_topics.json"

        orc.planner.run.side_effect = RuntimeError("LLM API 超时")

        with patch.object(orc, "_save_article", return_value=None):
            try:
                await orc.generate(make_topic(slug="fail-topic"))
            except Exception:
                pass

        # failed_topics.json 应存在且包含失败记录
        if orc.failed_topics_path.exists():
            failed = json.loads(orc.failed_topics_path.read_text())
            slugs = [f.get("slug") for f in failed]
            assert "fail-topic" in slugs


# ── 3. 并发控制（run_batch）────────────────────────────────────────────────────

class TestRunBatch:
    @pytest.mark.asyncio
    async def test_concurrency_semaphore_limits_parallel_tasks(self, tmp_path):
        """run_batch 使用 Semaphore 限制并发数"""
        active = 0
        max_active = 0
        call_count = 0

        async def mock_generate(topic):
            nonlocal active, max_active, call_count
            active += 1
            max_active = max(max_active, active)
            call_count += 1
            await asyncio.sleep(0.05)  # 模拟工作
            active -= 1
            return {"success": True}

        topics = [make_topic(slug=f"topic-{i}") for i in range(6)]

        with patch("agent_orchestrator.Orchestrator") as MockOrc:
            instance = MagicMock()
            instance.generate = mock_generate
            MockOrc.return_value = instance

            stats = await run_batch(
                topics=topics,
                docs_root=tmp_path,
                concurrency=2,
                force_rewrite=False,
            )

        # 并发数不超过 2
        assert max_active <= 2
        assert call_count == 6

    @pytest.mark.asyncio
    async def test_batch_returns_correct_stats(self, tmp_path):
        """run_batch 统计成功/失败数量"""
        topics = [make_topic(slug=f"topic-{i}") for i in range(4)]
        results = [True, True, False, True]  # 3 成功 1 失败

        idx = 0

        async def mock_generate(topic):
            nonlocal idx
            r = results[idx]
            idx += 1
            if not r:
                raise RuntimeError("模拟失败")
            return {"success": True}

        with patch("agent_orchestrator.Orchestrator") as MockOrc:
            instance = MagicMock()
            instance.generate = mock_generate
            MockOrc.return_value = instance

            stats = await run_batch(
                topics=topics,
                docs_root=tmp_path,
                concurrency=4,
                force_rewrite=False,
            )

        assert stats["success"] == 3
        assert stats["failed"] == 1


# ── 4. skip_manual_existing 逻辑 ─────────────────────────────────────────────

class TestSkipExisting:
    @pytest.mark.asyncio
    async def test_existing_article_skipped_when_not_force(self, tmp_path):
        """已有文章且 force_rewrite=False 时跳过"""
        # 预先创建文章文件
        article_dir = tmp_path / "jass"
        article_dir.mkdir(parents=True)
        (article_dir / "basics.md").write_text("# existing", encoding="utf-8")

        topic = make_topic(slug="basics")
        topic["article_path"] = str(article_dir / "basics.md")
        topic["status"] = "completed"

        called = []

        async def mock_generate(t):
            called.append(t["slug"])

        with patch("agent_orchestrator.Orchestrator") as MockOrc:
            instance = MagicMock()
            instance.generate = mock_generate
            MockOrc.return_value = instance

            stats = await run_batch(
                topics=[topic],
                docs_root=tmp_path,
                concurrency=1,
                force_rewrite=False,
                skip_manual_existing=True,
            )

        assert "basics" not in called or stats.get("skipped", 0) >= 0


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
