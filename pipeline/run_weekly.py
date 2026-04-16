"""
run_weekly.py — 每周全量扫描主入口

执行顺序：
1. gap_finder - AI 识别知识缺口
2. taxonomy --update - 同步新主题
3. run_incremental - 执行增量更新
"""
import logging
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
)
logger = logging.getLogger(__name__)


def main():
    logger.info("� War3 Wiki 每周全量扫描启动")

    # Step 1: AI 识别知识缺口
    logger.info("\n� Step 1: 知识缺口识别...")
    try:
        import gap_finder
        gap_finder.run()
    except Exception as e:
        logger.warning(f"gap_finder 执行异常（非致命，继续）: {e}")

    # Step 2: 同步 taxonomy.yaml 新增主题
    logger.info("\n� Step 2: 同步分类体系...")
    try:
        import taxonomy
        taxonomy.cmd_update()
    except Exception as e:
        logger.warning(f"taxonomy update 执行异常（非致命，继续）: {e}")

    # Step 3: 执行增量更新
    logger.info("\n🌪️  Step 3: 执行增量更新...")
    import run_incremental
    run_incremental.main()

    logger.info("\n✅ 每周全量扫描完成")


if __name__ == "__main__":
    main()