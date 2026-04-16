"""
taxonomy.py — 知识分类体系管理器

用法:
  python pipeline/taxonomy.py --init          # 从 taxonomy.yaml 初始化 topics.json
  python pipeline/taxonomy.py --update        # 追加 taxonomy.yaml 中的新主题
  python pipeline/taxonomy.py --list          # 列出所有主题及状态
  python pipeline/taxonomy.py --stats         # 显示统计信息
"""
import argparse
import json
import os
from datetime import datetime, timezone
from pathlib import Path

import yaml

TAXONOMY_PATH = Path(__file__).parent / "config" / "taxonomy.yaml"
CACHE_DIR = Path(__file__).parent / "cache"
TOPICS_PATH = CACHE_DIR / "topics.json"


def load_taxonomy() -> dict:
    with open(TAXONOMY_PATH, "r", encoding="utf-8") as f:
        return yaml.safe_load(f)


def load_topics() -> list:
    if TOPICS_PATH.exists():
        with open(TOPICS_PATH, "r", encoding="utf-8") as f:
            return json.load(f)
    return []


def save_topics(topics: list) -> None:
    CACHE_DIR.mkdir(parents=True, exist_ok=True)
    with open(TOPICS_PATH, "w", encoding="utf-8") as f:
        json.dump(topics, f, ensure_ascii=False, indent=2)
    print(f"✅ topics.json 已保存 ({len(topics)} 个主题)")


def build_topic_record(category: dict, topic: dict) -> dict:
    """构建单个主题记录（符合 spec 2.3 字段要求）"""
    return {
        "topic_id": topic["id"],
        "title": topic["title"],
        "category": category["id"],
        "category_name": category["name"],
        "search_query": topic.get("search_query", topic["title"]),
        "output_dir": category.get("output_dir", f"docs/{category['id']}"),
        "status": "pending",       # pending / done / failed
        "retry_count": 0,
        "last_error": None,
        "created_at": datetime.now(timezone.utc).isoformat(),
        "updated_at": None,
        "article_path": None,
    }


def cmd_init(force: bool = False) -> None:
    """从 taxonomy.yaml 全量初始化 topics.json"""
    if TOPICS_PATH.exists() and not force:
        print(f"⚠️  topics.json 已存在。使用 --force 强制重新初始化，或使用 --update 追加新主题。")
        return

    taxonomy = load_taxonomy()
    topics = []
    for category in taxonomy["categories"]:
        for topic in category["topics"]:
            topics.append(build_topic_record(category, topic))

    save_topics(topics)
    print(f"🚀 初始化完成：{len(topics)} 个主题（{len(taxonomy['categories'])} 个分类）")


def cmd_update() -> None:
    """追加 taxonomy.yaml 中新增的主题，不重置已有状态"""
    taxonomy = load_taxonomy()
    existing_topics = load_topics()
    existing_ids = {t["topic_id"] for t in existing_topics}

    new_topics = []
    for category in taxonomy["categories"]:
        for topic in category["topics"]:
            if topic["id"] not in existing_ids:
                new_topics.append(build_topic_record(category, topic))

    if not new_topics:
        print("✅ 无新主题需要追加，taxonomy.yaml 与 topics.json 已同步。")
        return

    all_topics = existing_topics + new_topics
    save_topics(all_topics)
    print(f"➕ 追加 {len(new_topics)} 个新主题：")
    for t in new_topics:
        print(f"   - [{t['category']}] {t['title']}")


def cmd_list() -> None:
    """列出所有主题及状态"""
    topics = load_topics()
    if not topics:
        print("❌ topics.json 不存在或为空，请先运行 --init")
        return

    status_icon = {"pending": "⏳", "done": "✅", "failed": "❌"}
    current_cat = None
    for t in topics:
        if t["category"] != current_cat:
            current_cat = t["category"]
            cat_name = t.get("category_name", current_cat)
            print(f"\n📂 {cat_name} ({current_cat})")
        icon = status_icon.get(t["status"], "❓")
        retry = f" (重试:{t['retry_count']})" if t["retry_count"] > 0 else ""
        print(f"  {icon} {t['title']}{retry}")


def cmd_stats() -> None:
    """显示统计信息"""
    topics = load_topics()
    if not topics:
        print("❌ topics.json 不存在，请先运行 --init")
        return

    total = len(topics)
    done = sum(1 for t in topics if t["status"] == "done")
    pending = sum(1 for t in topics if t["status"] == "pending")
    failed = sum(1 for t in topics if t["status"] == "failed")

    print(f"\n📊 知识库主题统计")
    print(f"   总计:  {total}")
    print(f"   ✅ 已完成: {done} ({done/total*100:.1f}%)")
    print(f"   ⏳ 待处理: {pending}")
    print(f"   ❌ 失败:   {failed}")


def main():
    parser = argparse.ArgumentParser(description="War3 Wiki 知识分类体系管理器")
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("--init", action="store_true", help="从 taxonomy.yaml 初始化 topics.json")
    group.add_argument("--update", action="store_true", help="追加 taxonomy.yaml 中的新主题")
    group.add_argument("--list", action="store_true", help="列出所有主题及状态")
    group.add_argument("--stats", action="store_true", help="显示统计信息")
    parser.add_argument("--force", action="store_true", help="配合 --init 强制重新初始化")
    args = parser.parse_args()

    if args.init:
        cmd_init(force=args.force)
    elif args.update:
        cmd_update()
    elif args.list:
        cmd_list()
    elif args.stats:
        cmd_stats()


if __name__ == "__main__":
    main()
