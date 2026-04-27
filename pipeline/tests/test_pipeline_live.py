"""
pipeline/tests/test_pipeline_live.py — 端到端冒烟测试
测试单个主题走完完整 Planner→Researcher→Writer→Reviewer 流水线。

用法（在 pipeline/ 目录下）：
    python tests/test_pipeline_live.py
    python tests/test_pipeline_live.py --stage search   # 只测试搜索层
    python tests/test_pipeline_live.py --stage planner  # 只测试 Planner
    python tests/test_pipeline_live.py --stage full     # 完整端到端
"""
from __future__ import annotations

import argparse
import asyncio
import json
import logging
import sys
from pathlib import Path

# 确保 pipeline 在 sys.path
_PIPELINE = Path(__file__).parent.parent
sys.path.insert(0, str(_PIPELINE))

from dotenv import load_dotenv
load_dotenv(str(_PIPELINE.parent / ".env"))

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(name)s — %(message)s",
    datefmt="%H:%M:%S",
)
logger = logging.getLogger("smoke_test")

# 测试用主题（小而有代表性）
TEST_TOPIC = {
    "topic_id": "test-jass-basics",
    "title": "JASS 触发器基础语法",
    "category": "scripting",
    "slug": "jass-basics",
    "status": "pending",
    "source": "manual",
    "source_urls": [],
}


# ─────────────────────────────────────────────
# 阶段 1：搜索层测试
# ─────────────────────────────────────────────
async def test_search():
    print("\n" + "="*50)
    print("🔍 阶段 1：搜索层测试")
    print("="*50)

    from search.orchestrator import MultiSourceSearch

    searcher = MultiSourceSearch()
    results = await searcher.search("Warcraft III JASS trigger basics", max_results=3)

    print(f"\n✅ 搜索结果 ({len(results)} 条):")
    for r in results:
        print(f"  [{r.source_engine}] {r.title[:60]}")
        print(f"    URL: {r.url[:70]}")
        print(f"    Score: {r.score:.2f}")
    return len(results) > 0


# ─────────────────────────────────────────────
# 阶段 2：Planner 测试
# ─────────────────────────────────────────────
async def test_planner():
    print("\n" + "="*50)
    print("📐 阶段 2：Planner Agent 测试")
    print("="*50)

    from models import ResearchContext
    from agents.planner.agent import PlannerAgent

    ctx = ResearchContext.from_topic_entry(TEST_TOPIC)
    planner = PlannerAgent()
    ctx = await planner.run(ctx)

    print(f"\n✅ 大纲生成 ({len(ctx.outline)} 节):")
    for node in ctx.outline:
        print(f"  {'#'*node.level} {node.title}")
        for q in node.search_queries:
            print(f"    🔎 {q}")

    print(f"\n📋 总搜索查询: {len(ctx.search_queries)} 条")
    return len(ctx.outline) > 0


# ─────────────────────────────────────────────
# 阶段 3：完整流水线测试
# ─────────────────────────────────────────────
async def test_full_pipeline():
    print("\n" + "="*50)
    print("🚀 阶段 3：完整端到端流水线测试")
    print("="*50)
    print(f"主题: {TEST_TOPIC['title']}")

    import tempfile
    from pathlib import Path
    from agent_orchestrator import Orchestrator

    # 使用临时目录避免污染真实 docs
    with tempfile.TemporaryDirectory() as tmpdir:
        docs_root = Path(tmpdir)
        orchestrator = Orchestrator(
            docs_root=docs_root,
            quality_threshold=0.5,   # 测试时放宽阈值
            max_review_loops=1,
        )

        result_path = await orchestrator.generate(TEST_TOPIC)

        if result_path and result_path.exists():
            content = result_path.read_text(encoding="utf-8")
            lines = content.split("\n")

            print(f"\n✅ 文章生成成功!")
            print(f"   路径: {result_path.name}")
            print(f"   大小: {len(content)} 字符 / {len(lines)} 行")

            # 检查 frontmatter
            has_fm = content.startswith("---")
            has_quality = "quality_score:" in content
            has_refs = "## 参考来源" in content or "参考" in content
            has_citations = "[^" in content

            print(f"\n📋 质量检查:")
            print(f"   {'✅' if has_fm else '❌'} 包含 YAML frontmatter")
            print(f"   {'✅' if has_quality else '❌'} 包含 quality_score")
            print(f"   {'✅' if has_refs else '⚠️ '} 包含参考来源区块")
            print(f"   {'✅' if has_citations else '⚠️ '} 包含引用标记 [^N]")

            # 打印文章前 30 行预览
            print(f"\n📄 文章预览 (前30行):")
            print("-" * 50)
            for line in lines[:30]:
                print(line)
            print("...")

            return True
        else:
            print("\n❌ 文章生成失败！")
            # 检查错误日志
            log_path = _PIPELINE / "logs" / f"{TEST_TOPIC['slug']}.log"
            if log_path.exists():
                print("\n📋 错误日志:")
                print(log_path.read_text(encoding="utf-8")[-1000:])
            return False


# ─────────────────────────────────────────────
# 主函数
# ─────────────────────────────────────────────
async def main(stage: str):
    print("🧪 War3 Wiki Agent 系统冒烟测试")
    print(f"   时间: {__import__('datetime').datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")

    results = {}

    if stage in ("search", "all"):
        results["search"] = await test_search()

    if stage in ("planner", "all"):
        results["planner"] = await test_planner()

    if stage in ("full", "all"):
        results["full_pipeline"] = await test_full_pipeline()

    print("\n" + "="*50)
    print("📊 测试结果汇总")
    print("="*50)
    all_passed = True
    for name, passed in results.items():
        status = "✅ PASS" if passed else "❌ FAIL"
        print(f"  {status}  {name}")
        if not passed:
            all_passed = False

    print()
    if all_passed:
        print("🎉 所有测试通过！系统运行正常。")
    else:
        print("⚠️  有测试失败，请检查上方日志。")
        sys.exit(1)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--stage",
        choices=["search", "planner", "full", "all"],
        default="full",
        help="要测试的阶段（默认: full）"
    )
    args = parser.parse_args()
    asyncio.run(main(args.stage))
