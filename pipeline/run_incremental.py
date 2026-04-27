"""
run_incremental.py — 每日增量更新主入口

流程：读取 pending/failed 主题 → 哈希比对 → STORM 生成 → 更新缓存 → git commit & push
"""
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

# 配置
MAX_TOPICS_PER_RUN = int(os.getenv("MAX_TOPICS_PER_RUN", "10"))
MAX_RETRY_COUNT = int(os.getenv("MAX_RETRY_COUNT", "3"))
RETRY_WAIT_SECONDS = int(os.getenv("RETRY_WAIT_SECONDS", "60"))


def load_pending_topics() -> list:
    """加载需要处理的主题（pending + failed 且未超过重试上限）"""
    if not TOPICS_PATH.exists():
        logger.error("topics.json 不存在，请先运行 python pipeline/taxonomy.py --init")
        sys.exit(1)
    with open(TOPICS_PATH, encoding="utf-8") as f:
        all_topics = json.load(f)
    return [
        t for t in all_topics
        if t["status"] == "pending"
        or (t["status"] == "failed" and t.get("retry_count", 0) < MAX_RETRY_COUNT)
    ]


def append_changelog(updated_topics: list) -> None:
    """在 docs/changelog.md 顶部插入本次更新条目"""
    DOCS_ROOT.mkdir(parents=True, exist_ok=True)
    now = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC")
    new_entry_lines = [
        f"\n## {now}\n\n",
        f"本次更新 **{len(updated_topics)}** 篇文章：\n\n",
    ]
    for t in updated_topics:
        new_entry_lines.append(f"- [{t['title']}]({t.get('article_path', '#')})\n")
    new_entry_lines.append("\n")

    if CHANGELOG_PATH.exists():
        existing = CHANGELOG_PATH.read_text(encoding="utf-8")
        # 在第一个 ## 之前插入（保留文件头部标题）
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
    commit_msg = f"[bot] Auto-update: {count} topics updated at {timestamp}"

    try:
        subprocess.run(["git", "config", "user.name", "war3-wiki-bot"], cwd=REPO_ROOT, check=True)
        subprocess.run(["git", "config", "user.email", "bot@war3-wiki.auto"], cwd=REPO_ROOT, check=True)
        subprocess.run(["git", "add", "."], cwd=REPO_ROOT, check=True)

        # 检查是否有变更
        result = subprocess.run(
            ["git", "diff", "--cached", "--quiet"], cwd=REPO_ROOT
        )
        if result.returncode == 0:
            logger.info("git: 暂存区无变更，跳过 commit")
            return

        subprocess.run(["git", "commit", "-m", commit_msg], cwd=REPO_ROOT, check=True)
        subprocess.run(["git", "push"], cwd=REPO_ROOT, check=True)
        logger.info(f"✅ git commit & push 成功: {commit_msg}")
    except subprocess.CalledProcessError as e:
        logger.error(f"git 操作失败: {e}")


def write_job_summary(stats: dict) -> None:
    """将统计结果写入 GitHub Actions Job Summary"""
    summary_path = os.getenv("GITHUB_STEP_SUMMARY")
    if not summary_path:
        return
    elapsed = stats.get("elapsed", 0)
    content = f"""## 🌪️ War3 Wiki 自动更新报告

| 指标 | 数值 |
|---|---|
| 处理主题总数 | {stats['total_processed']} |
| ✅ 成功生成 | {stats['success_count']} |
| ⏩ 缓存命中跳过 | {stats['skipped_count']} |
| ❌ 失败 | {stats['failed_count']} |
| ⏱️ 总耗时 | {elapsed:.1f}s ({elapsed/60:.1f}min) |
| 🕐 执行时间 | {datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M UTC')} |
"""
    with open(summary_path, "w", encoding="utf-8") as f:
        f.write(content)


def main(force_rewrite: bool = False):
    import asyncio
    start_time = time.time()
    logger.info("🚀 War3 Wiki 增量更新管道启动 (Agent Orchestrator)")

    from agent_orchestrator import run_batch

    topics = load_pending_topics()

    if not topics:
        logger.info("✅ 所有主题均已完成，无需更新")
        write_job_summary({"total_processed": 0, "success_count": 0, "skipped_count": 0, "failed_count": 0, "elapsed": 0})
        return

    if MAX_TOPICS_PER_RUN > 0:
        topics = topics[:MAX_TOPICS_PER_RUN]

    logger.info(f"📋 本次待处理主题: {len(topics)} 个")

    concurrency = int(os.getenv("AGENT_CONCURRENCY", "3"))
    stats = asyncio.run(run_batch(
        topics=topics,
        docs_root=DOCS_ROOT,
        concurrency=concurrency,
        force_rewrite=force_rewrite,
        skip_manual_existing=not force_rewrite,
    ))

    success_count = stats["success"]
    skipped_count = stats["skipped"]
    failed_count = stats["failed"]
    elapsed = time.time() - start_time

    # 更新 changelog
    completed_topics = [t for t in topics if t.get("article_path")]
    if completed_topics:
        append_changelog(completed_topics)

    git_commit_and_push(success_count)

    job_stats = {
        "total_processed": len(topics),
        "success_count": success_count,
        "skipped_count": skipped_count,
        "failed_count": failed_count,
        "elapsed": elapsed,
    }
    write_job_summary(job_stats)

    logger.info(f"\n📊 执行摘要:")
    logger.info(f"   处理: {len(topics)} | 成功: {success_count} | 跳过: {skipped_count} | 失败: {failed_count}")
    logger.info(f"   总耗时: {elapsed:.1f}s ({elapsed/60:.1f}min)")

    if failed_count > 0:
        sys.exit(1)


if __name__ == "__main__":
    import argparse
    sys.path.insert(0, str(Path(__file__).parent))
    parser = argparse.ArgumentParser(description="War3 Wiki 增量更新")
    parser.add_argument("--force-rewrite", action="store_true", help="强制重新生成所有主题（包括已有文章）")
    args = parser.parse_args()
    main(force_rewrite=args.force_rewrite)
