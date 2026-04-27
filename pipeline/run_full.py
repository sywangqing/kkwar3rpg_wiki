"""
run_full.py — 全量重新生成所有主题

与 run_incremental.py 的区别：
  - 遍历 topics.json 中 *所有* 主题（包括已完成的）
  - 支持 --concurrency 控制并发数
  - 支持 --limit 限制本次运行主题数（调试用）
  - 支持 --category 过滤分类
  - 使用异步批量 runner (asyncio.Semaphore)

用法:
  python pipeline/run_full.py
  python pipeline/run_full.py --concurrency 5
  python pipeline/run_full.py --limit 20 --category "JASS 编程"
  python pipeline/run_full.py --force-rewrite
"""
import argparse
import asyncio
import json
import logging
import os
import subprocess
import sys
import time
from datetime import datetime, timezone
from pathlib import Path

from dotenv import load_dotenv

load_dotenv()

# 配置日志
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
)
logger = logging.getLogger(__name__)

# 路径常量
REPO_ROOT = Path(__file__).parent.parent
DOCS_ROOT = REPO_ROOT / "docs"
PIPELINE_DIR = Path(__file__).parent
CACHE_DIR = PIPELINE_DIR / "cache"
TOPICS_PATH = CACHE_DIR / "topics.json"
CHANGELOG_PATH = DOCS_ROOT / "changelog.md"


def load_all_topics(category: str | None = None) -> list:
    """加载所有主题，可选按分类过滤"""
    if not TOPICS_PATH.exists():
        logger.error("topics.json 不存在，请先运行: python pipeline/taxonomy.py --init")
        sys.exit(1)
    with open(TOPICS_PATH, encoding="utf-8") as f:
        all_topics = json.load(f)
    if category:
        all_topics = [t for t in all_topics if t.get("category") == category]
    return all_topics


def append_changelog(updated_topics: list) -> None:
    """在 docs/changelog.md 顶部插入本次更新条目"""
    DOCS_ROOT.mkdir(parents=True, exist_ok=True)
    now = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC")
    new_entry_lines = [
        f"\n## {now}\n\n",
        f"本次全量重建 **{len(updated_topics)}** 篇文章：\n\n",
    ]
    for t in updated_topics:
        new_entry_lines.append(f"- [{t['title']}]({t.get('article_path', '#')})\n")
    new_entry_lines.append("\n")

    if CHANGELOG_PATH.exists():
        existing = CHANGELOG_PATH.read_text(encoding="utf-8")
        if "# 更新日志" in existing:
            insert_pos = existing.index("# 更新日志") + len("# 更新日志")
            new_content = existing[:insert_pos] + "\n" + "".join(new_entry_lines) + existing[insert_pos:]
        else:
            new_content = "# 更新日志\n\n" + "".join(new_entry_lines) + existing
    else:
        new_content = "# 更新日志\n\n" + "".join(new_entry_lines)

    CHANGELOG_PATH.write_text(new_content, encoding="utf-8")
    logger.info(f"✅ 更新日志已追加: {len(updated_topics)} 条记录")


def git_commit_and_push(count: int) -> None:
    """有更新时自动 git commit & push"""
    if count == 0:
        logger.info("无内容变更，跳过 git commit")
        return
    timestamp = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC")
    commit_msg = f"[bot] Full rebuild: {count} topics regenerated at {timestamp}"
    try:
        subprocess.run(["git", "config", "user.name", "war3-wiki-bot"], cwd=REPO_ROOT, check=True)
        subprocess.run(["git", "config", "user.email", "bot@war3-wiki.auto"], cwd=REPO_ROOT, check=True)
        subprocess.run(["git", "add", "."], cwd=REPO_ROOT, check=True)
        result = subprocess.run(["git", "diff", "--cached", "--quiet"], cwd=REPO_ROOT)
        if result.returncode == 0:
            logger.info("git: 暂存区无变更，跳过 commit")
            return
        subprocess.run(["git", "commit", "-m", commit_msg], cwd=REPO_ROOT, check=True)
        subprocess.run(["git", "push"], cwd=REPO_ROOT, check=True)
        logger.info(f"✅ git commit & push 成功")
    except subprocess.CalledProcessError as e:
        logger.error(f"git 操作失败: {e}")


def write_job_summary(stats: dict) -> None:
    """写入 GitHub Actions Job Summary"""
    summary_path = os.getenv("GITHUB_STEP_SUMMARY")
    if not summary_path:
        return
    elapsed = stats.get("elapsed", 0)
    content = f"""## 🌪️ War3 Wiki 全量重建报告

| 指标 | 数值 |
|---|---|
| 处理主题总数 | {stats['total_processed']} |
| ✅ 成功生成 | {stats['success_count']} |
| ⏩ 缓存跳过 | {stats['skipped_count']} |
| ❌ 失败 | {stats['failed_count']} |
| ⏱️ 总耗时 | {elapsed:.1f}s ({elapsed/60:.1f}min) |
| 🕐 执行时间 | {datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M UTC')} |
"""
    with open(summary_path, "w", encoding="utf-8") as f:
        f.write(content)


def main():
    parser = argparse.ArgumentParser(
        description="War3 Wiki 全量重建 — 重新生成所有主题文章",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
示例:
  # 默认并发3，全量重建
  python pipeline/run_full.py

  # 并发5，仅重建 "JASS 编程" 分类
  python pipeline/run_full.py --concurrency 5 --category "JASS 编程"

  # 调试：只处理前5个主题
  python pipeline/run_full.py --limit 5 --dry-run
        """,
    )
    parser.add_argument(
        "--concurrency", type=int, default=int(os.getenv("AGENT_CONCURRENCY", "3")),
        help="并发处理主题数 (default: 3, env: AGENT_CONCURRENCY)"
    )
    parser.add_argument(
        "--limit", type=int, default=0,
        help="限制处理主题数（0 = 不限制，调试用）"
    )
    parser.add_argument(
        "--category", type=str, default=None,
        help="仅处理指定分类的主题"
    )
    parser.add_argument(
        "--force-rewrite", action="store_true",
        help="即使文章已存在也强制重新生成"
    )
    parser.add_argument(
        "--no-git", action="store_true",
        help="跳过 git commit & push"
    )
    parser.add_argument(
        "--dry-run", action="store_true",
        help="仅打印将要处理的主题，不实际生成"
    )
    args = parser.parse_args()

    sys.path.insert(0, str(PIPELINE_DIR))

    start_time = time.time()
    logger.info("🚀 War3 Wiki 全量重建管道启动")
    logger.info(f"   并发数: {args.concurrency} | 强制重写: {args.force_rewrite}")

    topics = load_all_topics(category=args.category)

    if not topics:
        logger.info("✅ 未找到任何主题（请检查 topics.json 或 --category 参数）")
        return

    if args.limit > 0:
        topics = topics[:args.limit]
        logger.info(f"🔍 --limit 生效，只处理前 {args.limit} 个主题")

    logger.info(f"📋 本次待处理主题: {len(topics)} 个")

    if args.dry_run:
        logger.info("🏃 --dry-run 模式，列出主题后退出：")
        for i, t in enumerate(topics, 1):
            logger.info(f"  {i:3d}. [{t.get('category', '?')}] {t['title']}")
        return

    from agent_orchestrator import run_batch

    stats = asyncio.run(run_batch(
        topics=topics,
        docs_root=DOCS_ROOT,
        concurrency=args.concurrency,
        force_rewrite=args.force_rewrite,
        skip_manual_existing=False,  # 全量模式不跳过 manual 主题
    ))

    success_count = stats["success"]
    skipped_count = stats["skipped"]
    failed_count = stats["failed"]
    elapsed = time.time() - start_time

    # 更新 changelog
    completed_topics = [t for t in topics if t.get("article_path")]
    if completed_topics and not args.no_git:
        append_changelog(completed_topics)

    if not args.no_git:
        git_commit_and_push(success_count)

    job_stats = {
        "total_processed": len(topics),
        "success_count": success_count,
        "skipped_count": skipped_count,
        "failed_count": failed_count,
        "elapsed": elapsed,
    }
    write_job_summary(job_stats)

    logger.info(f"\n📊 全量重建摘要:")
    logger.info(f"   总计: {len(topics)} | 成功: {success_count} | 跳过: {skipped_count} | 失败: {failed_count}")
    logger.info(f"   总耗时: {elapsed:.1f}s ({elapsed/60:.1f}min)")

    if failed_count > 0:
        sys.exit(1)


if __name__ == "__main__":
    main()
