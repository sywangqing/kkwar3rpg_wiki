"""
gap_finder.py — AI 知识缺口识别器

分析已生成文章，发现分类体系中缺失的主题，自动追加到 topics.json。

用法:
  python pipeline/gap_finder.py
"""
import json
import os
from datetime import datetime, timezone
from pathlib import Path

import yaml
from dotenv import load_dotenv
from litellm import completion

load_dotenv()

TAXONOMY_PATH = Path(__file__).parent / "config" / "taxonomy.yaml"
CACHE_DIR = Path(__file__).parent / "cache"
TOPICS_PATH = CACHE_DIR / "topics.json"


def load_existing_topics() -> list:
    if TOPICS_PATH.exists():
        with open(TOPICS_PATH, "r", encoding="utf-8") as f:
            return json.load(f)
    return []


def save_topics(topics: list) -> None:
    with open(TOPICS_PATH, "w", encoding="utf-8") as f:
        json.dump(topics, f, ensure_ascii=False, indent=2)


def get_done_titles(topics: list) -> list[str]:
    return [t["title"] for t in topics if t["status"] == "done"]


def find_gaps(done_titles: list[str], category_context: str) -> list[dict]:
    """调用 LLM 分析缺失主题"""
    model_name = os.getenv("OUTLINE_GEN_MODEL", "gpt-4o")
    api_key = os.getenv("OPENAI_API_KEY")
    base_url = os.getenv("OPENAI_BASE_URL")

    # 支持自定义 base_url（MiniMax / 其他 OpenAI 兼容服务）
    if base_url and "/" not in model_name:
        model = f"openai/{model_name}"
    else:
        model = model_name

    prompt = f"""你是 War3 地图编辑器知识库的专家编辑。

当前知识库分类体系：
{category_context}

已有文章主题：
{chr(10).join(f'- {t}' for t in done_titles) if done_titles else '（暂无已完成文章）'}

请分析上述知识库，找出 **5~10 个** 重要的缺失主题，这些主题：
1. 对 War3 地图开发者有实际价值
2. 在已有文章中尚未覆盖
3. 适合写成独立的 Wiki 文章

以 JSON 数组格式输出，每个元素包含：
- id: kebab-case 标识符（英文，如 "hero-attribute-system"）
- title: 中文标题
- category: 所属分类 id（从分类体系中选择）
- search_query: 搜索查询词（中文，用于搜索引擎）

只输出 JSON 数组，不要其他文字。"""

    completion_kwargs = dict(
        model=model,
        messages=[{"role": "user", "content": prompt}],
        api_key=api_key,
        max_tokens=1000,
    )
    if base_url:
        completion_kwargs["api_base"] = base_url

    response = completion(**completion_kwargs)

    raw = response.choices[0].message.content.strip()
    # 提取 JSON 数组
    if "```" in raw:
        raw = raw.split("```")[1]
        if raw.startswith("json"):
            raw = raw[4:]
    return json.loads(raw.strip())


def build_gap_record(gap: dict, taxonomy: dict) -> dict:
    """构建缺口主题记录"""
    # 找到对应分类
    category = next(
        (c for c in taxonomy["categories"] if c["id"] == gap.get("category", "advanced")),
        taxonomy["categories"][-1]
    )
    return {
        "topic_id": gap["id"],
        "title": gap["title"],
        "category": category["id"],
        "category_name": category["name"],
        "search_query": gap.get("search_query", gap["title"]),
        "output_dir": category.get("output_dir", f"docs/{category['id']}"),
        "status": "pending",
        "retry_count": 0,
        "last_error": None,
        "created_at": datetime.now(timezone.utc).isoformat(),
        "updated_at": None,
        "article_path": None,
        "source": "gap_finder",  # 标记来源
    }


def run():
    print("🔍 启动知识缺口分析...")

    taxonomy = yaml.safe_load(open(TAXONOMY_PATH, encoding="utf-8"))
    existing_topics = load_existing_topics()
    existing_ids = {t["topic_id"] for t in existing_topics}
    done_titles = get_done_titles(existing_topics)

    # 构建分类上下文
    category_context = "\n".join(
        f"- {c['id']}: {c['name']} — {c['description']}"
        for c in taxonomy["categories"]
    )

    print(f"   已有主题: {len(existing_topics)} 个，已完成: {len(done_titles)} 个")

    gaps = find_gaps(done_titles, category_context)
    print(f"   LLM 识别到 {len(gaps)} 个候选缺口主题")

    new_records = []
    for gap in gaps:
        if gap["id"] not in existing_ids:
            record = build_gap_record(gap, taxonomy)
            new_records.append(record)
            print(f"   ➕ [{record['category']}] {record['title']}")
        else:
            print(f"   ⏩ 跳过（已存在）: {gap['id']}")

    if new_records:
        all_topics = existing_topics + new_records
        save_topics(all_topics)
        print(f"\n✅ 成功追加 {len(new_records)} 个新主题到 topics.json")
    else:
        print("\n✅ 无新缺口主题需要追加")


if __name__ == "__main__":
    run()
