"""
cache_manager.py — 增量更新缓存系统

基于 SHA256 哈希避免重复生成未变更主题，节省 AI API 成本。
支持：内容哈希比对、缓存持久化、失败任务重试、错误日志。
"""
import hashlib
import json
import logging
import time
from datetime import datetime, timezone
from pathlib import Path
from typing import Optional

logger = logging.getLogger(__name__)

CACHE_DIR = Path(__file__).parent / "cache"
HASHES_PATH = CACHE_DIR / "topic_hashes.json"
ERROR_LOG_PATH = CACHE_DIR / "error_log.json"
TOPICS_PATH = CACHE_DIR / "topics.json"


class CacheManager:
    def __init__(self):
        CACHE_DIR.mkdir(parents=True, exist_ok=True)
        self._hashes = self._load_hashes()
        self._errors = self._load_errors()

    # --------------------------------------------------------
    # 哈希计算
    # --------------------------------------------------------

    def compute_topic_hash(self, topic: dict, search_results: Optional[str] = None) -> str:
        """
        计算主题内容哈希（基于搜索结果原文 + 主题标题）。
        如未提供 search_results，则仅基于主题元数据（用于无网络场景）。
        """
        content = f"{topic['title']}::{topic.get('search_query', '')}::{search_results or ''}"
        return hashlib.sha256(content.encode("utf-8")).hexdigest()

    # --------------------------------------------------------
    # 缓存比对
    # --------------------------------------------------------

    def is_cached(self, topic_id: str, new_hash: str) -> bool:
        """比对哈希，内容未变更返回 True（应跳过生成）"""
        cached = self._hashes.get(topic_id)
        if not cached:
            return False
        return cached.get("hash") == new_hash

    # --------------------------------------------------------
    # 缓存更新
    # --------------------------------------------------------

    def update(self, topic_id: str, hash_value: str, article_path: str) -> None:
        """文章成功生成后立即更新缓存（原子写入）"""
        self._hashes[topic_id] = {
            "hash": hash_value,
            "generated_at": datetime.now(timezone.utc).isoformat(),
            "article_path": article_path,
        }
        self._save_hashes()
        logger.debug(f"缓存已更新: {topic_id}")

    # --------------------------------------------------------
    # Topic 状态管理
    # --------------------------------------------------------

    def mark_done(self, topic_id: str, article_path: str) -> None:
        """将主题标记为已完成"""
        self._update_topic_status(topic_id, "done", article_path=article_path)

    def mark_failed(self, topic_id: str, error: str) -> None:
        """将主题标记为失败，记录错误原因"""
        self._update_topic_status(topic_id, "failed", error=error)
        self._append_error_log(topic_id, error)

    def increment_retry(self, topic_id: str) -> int:
        """重试计数 +1，返回当前重试次数"""
        topics = self._load_topics()
        for t in topics:
            if t["topic_id"] == topic_id:
                t["retry_count"] = t.get("retry_count", 0) + 1
                self._save_topics(topics)
                return t["retry_count"]
        return 0

    def get_retry_count(self, topic_id: str) -> int:
        topics = self._load_topics()
        for t in topics:
            if t["topic_id"] == topic_id:
                return t.get("retry_count", 0)
        return 0

    # --------------------------------------------------------
    # 重试执行器
    # --------------------------------------------------------

    def run_with_retry(
        self,
        topic: dict,
        fn,
        max_retries: int = 3,
        wait_seconds: int = 60,
    ) -> Optional[str]:
        """
        带重试逻辑的执行器。

        Args:
            topic: 主题记录
            fn: 生成函数，签名 fn(topic) -> article_path
            max_retries: 最大重试次数
            wait_seconds: 每次重试前等待秒数

        Returns:
            article_path (str) or None（失败时）
        """
        topic_id = topic["topic_id"]
        attempt = 0

        while attempt <= max_retries:
            try:
                article_path = fn(topic)
                return article_path
            except Exception as e:
                attempt += 1
                retry_count = self.increment_retry(topic_id)
                error_msg = str(e)
                logger.warning(f"⚠️  主题 '{topic['title']}' 第 {attempt} 次失败: {error_msg}")

                if attempt > max_retries:
                    logger.error(f"❌ 主题 '{topic['title']}' 超过最大重试次数 ({max_retries})")
                    self.mark_failed(topic_id, error_msg)
                    return None
                else:
                    logger.info(f"🔄 等待 {wait_seconds}s 后重试...")
                    time.sleep(wait_seconds)

        return None

    # --------------------------------------------------------
    # 私有：JSON 读写
    # --------------------------------------------------------

    def _load_hashes(self) -> dict:
        if HASHES_PATH.exists():
            with open(HASHES_PATH, "r", encoding="utf-8") as f:
                return json.load(f)
        return {}

    def _save_hashes(self) -> None:
        with open(HASHES_PATH, "w", encoding="utf-8") as f:
            json.dump(self._hashes, f, ensure_ascii=False, indent=2)

    def _load_errors(self) -> list:
        if ERROR_LOG_PATH.exists():
            with open(ERROR_LOG_PATH, "r", encoding="utf-8") as f:
                return json.load(f)
        return []

    def _append_error_log(self, topic_id: str, error: str) -> None:
        self._errors.append({
            "topic_id": topic_id,
            "error": error,
            "timestamp": datetime.now(timezone.utc).isoformat(),
        })
        with open(ERROR_LOG_PATH, "w", encoding="utf-8") as f:
            json.dump(self._errors, f, ensure_ascii=False, indent=2)

    def _load_topics(self) -> list:
        if TOPICS_PATH.exists():
            with open(TOPICS_PATH, "r", encoding="utf-8") as f:
                return json.load(f)
        return []

    def _save_topics(self, topics: list) -> None:
        with open(TOPICS_PATH, "w", encoding="utf-8") as f:
            json.dump(topics, f, ensure_ascii=False, indent=2)

    def _update_topic_status(
        self,
        topic_id: str,
        status: str,
        article_path: Optional[str] = None,
        error: Optional[str] = None,
    ) -> None:
        topics = self._load_topics()
        for t in topics:
            if t["topic_id"] == topic_id:
                t["status"] = status
                t["updated_at"] = datetime.now(timezone.utc).isoformat()
                if article_path:
                    t["article_path"] = article_path
                if error:
                    t["last_error"] = error
                break
        self._save_topics(topics)
