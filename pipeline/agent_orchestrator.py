"""
pipeline/agent_orchestrator.py
多 Agent 协作编排器：Planner → Researcher → Writer → Reviewer

主要特性：
- 顺序执行四个 Agent
- 自动重写循环（quality_score < threshold，最多 max_review_loops 次）
- asyncio.Semaphore 控制并发数
- 失败记录到 pipeline/failed_topics.json
- 最终写入 docs/<category>/<slug>.md 带完整 frontmatter
"""
from __future__ import annotations

import asyncio
import json
import logging
import os
import sys
from datetime import datetime, timezone
from pathlib import Path

from dotenv import load_dotenv

load_dotenv()

# 确保 pipeline 目录在 sys.path 中
_PIPELINE_DIR = Path(__file__).parent
if str(_PIPELINE_DIR) not in sys.path:
    sys.path.insert(0, str(_PIPELINE_DIR))

from models import ResearchContext

logger = logging.getLogger(__name__)

# ---------------------------------------------------------------------------
# 配置常量（从环境变量读取）
# ---------------------------------------------------------------------------
QUALITY_THRESHOLD = float(os.getenv("AGENT_QUALITY_THRESHOLD", "0.7"))
MAX_REVIEW_LOOPS = int(os.getenv("AGENT_MAX_REVIEW_LOOPS", "2"))
DEFAULT_CONCURRENCY = int(os.getenv("AGENT_CONCURRENCY", "3"))
AGENT_MODEL = os.getenv("AGENT_LLM_MODEL", "minimax/abab7-chat-preview")
FAILED_TOPICS_PATH = _PIPELINE_DIR / "failed_topics.json"
LOGS_DIR = _PIPELINE_DIR / "logs"


# ---------------------------------------------------------------------------
# 辅助：持久化失败主题
# ---------------------------------------------------------------------------

def _record_failure(topic_id: str, title: str, error: str) -> None:
    FAILED_TOPICS_PATH.parent.mkdir(parents=True, exist_ok=True)
    existing: list[dict] = []
    if FAILED_TOPICS_PATH.exists():
        try:
            existing = json.loads(FAILED_TOPICS_PATH.read_text(encoding="utf-8"))
        except Exception:
            pass
    existing.append({
        "topic_id": topic_id,
        "title": title,
        "error": error,
        "failed_at": datetime.now(timezone.utc).isoformat(),
    })
    FAILED_TOPICS_PATH.write_text(json.dumps(existing, ensure_ascii=False, indent=2), encoding="utf-8")


# ---------------------------------------------------------------------------
# 辅助：写出最终 Markdown 文章
# ---------------------------------------------------------------------------

def _write_article(context: ResearchContext, docs_root: Path) -> Path:
    """生成带 frontmatter 的 Markdown 并写入 docs/<category>/<slug>.md"""
    category_dir = docs_root / context.category
    category_dir.mkdir(parents=True, exist_ok=True)
    output_path = category_dir / f"{context.slug}.md"

    used_urls = [s.url for s in context.get_used_sources()]
    now = datetime.now(timezone.utc).strftime("%Y-%m-%d")

    frontmatter_lines = [
        "---",
        f"title: {context.title}",
        f"category: {context.category}",
        f"updated: {now}",
        f"model: {AGENT_MODEL}",
        f"quality_score: {round(context.quality_score, 2)}",
        f"discovered_via: {context.discovered_via}",
    ]
    if context.quality_warning:
        frontmatter_lines.append("quality_warning: true")
    if used_urls:
        frontmatter_lines.append("sources:")
        for url in used_urls:
            frontmatter_lines.append(f"  - {url}")
    frontmatter_lines.append("---")

    content = "\n".join(frontmatter_lines) + f"\n\n# {context.title}\n\n" + context.draft
    output_path.write_text(content, encoding="utf-8")
    logger.info(f"📄 文章写入: {output_path.relative_to(docs_root.parent)}")
    return output_path


# ---------------------------------------------------------------------------
# 核心：单个主题的生成流水线
# ---------------------------------------------------------------------------

class Orchestrator:
    """多 Agent 协作编排器"""

    def __init__(
        self,
        docs_root: Path,
        quality_threshold: float = QUALITY_THRESHOLD,
        max_review_loops: int = MAX_REVIEW_LOOPS,
        model: str = AGENT_MODEL,
    ):
        self.docs_root = docs_root
        self.quality_threshold = quality_threshold
        self.max_review_loops = max_review_loops
        self.model = model
        LOGS_DIR.mkdir(parents=True, exist_ok=True)

        # 懒加载 agents（避免在导入时就拉起 litellm）
        self._planner = None
        self._researcher = None
        self._writer = None
        self._reviewer = None

    def _get_agents(self):
        if self._planner is None:
            from agents.planner.agent import PlannerAgent
            from agents.researcher.agent import ResearcherAgent
            from agents.writer.agent import WriterAgent
            from agents.reviewer.agent import ReviewerAgent
            self._planner = PlannerAgent(model=self.model)
            self._researcher = ResearcherAgent(model=self.model)
            self._writer = WriterAgent(model=self.model)
            self._reviewer = ReviewerAgent(model=self.model)
        return self._planner, self._researcher, self._writer, self._reviewer

    def _setup_topic_logger(self, slug: str) -> logging.FileHandler:
        log_path = LOGS_DIR / f"{slug}.log"
        handler = logging.FileHandler(log_path, encoding="utf-8")
        handler.setFormatter(logging.Formatter("%(asctime)s [%(levelname)s] %(message)s"))
        logging.getLogger().addHandler(handler)
        return handler

    async def generate(self, topic: dict) -> Path | None:
        """
        为单个主题执行完整的 Planner→Researcher→Writer→Reviewer 流水线。
        返回生成的文章路径，失败返回 None。
        """
        context = ResearchContext.from_topic_entry(topic)
        log_handler = self._setup_topic_logger(context.slug)

        try:
            planner, researcher, writer, reviewer = self._get_agents()

            # ---- Stage 1: Planner ----
            context = await planner.run(context)

            # ---- Stage 2: Researcher ----
            context = await researcher.run(context)

            # ---- Stage 3+4: Writer → Reviewer → (rewrite loop) ----
            best_draft = ""
            best_score = 0.0
            feedback_text = ""

            for loop in range(self.max_review_loops + 1):
                context.review_loop_count = loop
                context = await writer.run(context, reviewer_feedback=feedback_text)
                context = await reviewer.run(context)

                score = context.quality_score
                if score > best_score:
                    best_score = score
                    best_draft = context.draft

                if context.review_result and context.review_result.passed:
                    logger.info(f"✅ 质量通过 (loop {loop}): score={score:.2f}")
                    break

                if loop < self.max_review_loops:
                    # 准备下一轮重写的反馈文本
                    if context.review_result:
                        feedback_items = "\n".join(
                            f"- [{fb.category}] {fb.excerpt[:100]}... → {fb.suggestion}"
                            for fb in context.review_result.feedback
                        )
                        feedback_text = f"上一轮评分: {score:.2f}\n需要改进:\n{feedback_items}"
                    logger.info(f"⚠️  质量未通过 (loop {loop})，score={score:.2f}，开始重写...")

            # 使用最佳草稿
            if best_draft and best_score > context.quality_score:
                context.draft = best_draft
                context.quality_score = best_score

            if best_score < self.quality_threshold:
                context.quality_warning = True
                logger.warning(f"⚠️  最终质量仍低于阈值: {best_score:.2f} < {self.quality_threshold}")

            # ---- 写文章 ----
            output_path = _write_article(context, self.docs_root)
            return output_path

        except Exception as e:
            error_msg = f"{type(e).__name__}: {e}"
            logger.error(f"❌ 生成失败: {context.title} — {error_msg}", exc_info=True)
            _record_failure(context.topic_id, context.title, error_msg)
            return None
        finally:
            logging.getLogger().removeHandler(log_handler)
            log_handler.close()


# ---------------------------------------------------------------------------
# 批量异步运行器
# ---------------------------------------------------------------------------

async def run_batch(
    topics: list[dict],
    docs_root: Path,
    concurrency: int = DEFAULT_CONCURRENCY,
    force_rewrite: bool = False,
    skip_manual_existing: bool = True,
) -> dict:
    """
    并发处理多个主题（asyncio.Semaphore 控制并发数）。
    返回统计字典 {success, skipped, failed}。
    """
    orchestrator = Orchestrator(docs_root=docs_root)
    sem = asyncio.Semaphore(concurrency)

    stats = {"success": 0, "skipped": 0, "failed": 0}

    async def _process(topic: dict):
        # 跳过逻辑：非 force_rewrite 时，manual 主题且文章已存在则跳过
        if not force_rewrite and skip_manual_existing:
            is_manual = topic.get("source", "manual") == "manual"
            slug = topic.get("slug", "")
            category = topic.get("category", "general")
            existing = docs_root / category / f"{slug}.md"
            if is_manual and existing.exists():
                logger.info(f"⏩ 跳过（已存在）: {topic.get('title', slug)}")
                stats["skipped"] += 1
                return

        async with sem:
            result = await orchestrator.generate(topic)
            if result:
                stats["success"] += 1
            else:
                stats["failed"] += 1

    await asyncio.gather(*[_process(t) for t in topics])
    return stats
