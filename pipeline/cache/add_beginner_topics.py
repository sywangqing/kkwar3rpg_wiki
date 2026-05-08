"""一次性脚本：向 topics.json 批量添加 KK 新人入门主题"""
import json
from datetime import datetime, timezone
from pathlib import Path

TOPICS_PATH = Path(__file__).parent / "topics.json"

topics = json.loads(TOPICS_PATH.read_text(encoding="utf-8"))
existing_ids = {t["topic_id"] for t in topics}
now = datetime.now(timezone.utc).isoformat()

NEW_TOPICS = [
    # ===== 0级：KK平台新人起点 =====
    {"topic_id": "kk-what-is-platform",     "title": "什么是KK平台？新人作者必读指南",            "category": "getting-started", "category_name": "快速入门",   "search_query": "KK卡牌平台 War3地图 新人作者 入门指南",              "output_dir": "docs/getting-started"},
    {"topic_id": "kk-ydwe-vs-worldeditor",  "title": "YDWE vs 原版编辑器：新手该选哪个",          "category": "getting-started", "category_name": "快速入门",   "search_query": "YDWE 魔兽世界编辑器 区别 新手推荐",                   "output_dir": "docs/getting-started"},
    {"topic_id": "kk-first-30-minutes",     "title": "打开编辑器的前30分钟：你应该做什么",         "category": "getting-started", "category_name": "快速入门",   "search_query": "War3 世界编辑器 新手 第一步 入门操作",                 "output_dir": "docs/getting-started"},
    {"topic_id": "kk-map-size-choice",      "title": "新手地图应该多大？地图尺寸选择指南",          "category": "getting-started", "category_name": "快速入门",   "search_query": "War3 地图大小 尺寸选择 新手 推荐",                    "output_dir": "docs/getting-started"},
    {"topic_id": "kk-save-and-backup",      "title": "地图保存与备份：防止丢失作品的方法",          "category": "getting-started", "category_name": "快速入门",   "search_query": "War3 地图保存 备份 防丢失 w3x文件",                   "output_dir": "docs/getting-started"},
    {"topic_id": "kk-learn-roadmap",        "title": "完整学习路线图：从零到发布第一张地图",         "category": "getting-started", "category_name": "快速入门",   "search_query": "War3 地图编辑 学习路线 新手 从零开始 规划",             "output_dir": "docs/getting-started"},

    # ===== 1级：GUI触发器零代码入门 =====
    {"topic_id": "kk-what-is-trigger",      "title": "触发器是什么？用大白话解释游戏逻辑",          "category": "triggers",        "category_name": "触发器系统", "search_query": "War3 触发器 是什么 新手 通俗解释",                     "output_dir": "docs/triggers"},
    {"topic_id": "kk-gui-first-trigger",    "title": "我的第一个触发器：让单位说话",               "category": "triggers",        "category_name": "触发器系统", "search_query": "War3 GUI 触发器 新手教程 单位对话 第一个触发器",        "output_dir": "docs/triggers"},
    {"topic_id": "kk-event-cond-action",    "title": "事件、条件、动作：触发器三要素详解",          "category": "triggers",        "category_name": "触发器系统", "search_query": "War3 触发器 事件 条件 动作 区别 教程 新手",             "output_dir": "docs/triggers"},
    {"topic_id": "kk-trigger-variables",    "title": "变量是什么？触发器变量零基础入门",            "category": "triggers",        "category_name": "触发器系统", "search_query": "War3 触发器变量 新手 什么是变量 使用方法",              "output_dir": "docs/triggers"},
    {"topic_id": "kk-gui-unit-spawn",       "title": "如何刷新单位？触发器实战练习",               "category": "triggers",        "category_name": "触发器系统", "search_query": "War3 触发器 刷新单位 创建单位 GUI 教程 新手",           "output_dir": "docs/triggers"},
    {"topic_id": "kk-gui-timer",            "title": "计时器触发器：制作倒计时和定时事件",          "category": "triggers",        "category_name": "触发器系统", "search_query": "War3 触发器 计时器 倒计时 定时 GUI 新手",              "output_dir": "docs/triggers"},
    {"topic_id": "kk-trigger-debug",        "title": "触发器不生效怎么办？新手调试排错指南",         "category": "triggers",        "category_name": "触发器系统", "search_query": "War3 触发器 不生效 调试 排错 新手问题 解决",            "output_dir": "docs/triggers"},
    {"topic_id": "kk-gui-dialog",           "title": "制作对话框和选项菜单",                       "category": "triggers",        "category_name": "触发器系统", "search_query": "War3 触发器 对话框 Dialog 选项菜单 GUI 教程",           "output_dir": "docs/triggers"},
    {"topic_id": "kk-trigger-memory-leak",  "title": "什么是内存泄漏？为什么地图越玩越卡",          "category": "triggers",        "category_name": "触发器系统", "search_query": "War3 内存泄漏 触发器 卡顿 原因 解决 教程",             "output_dir": "docs/triggers"},

    # ===== 2级：对象编辑器 =====
    {"topic_id": "kk-obj-editor-intro",     "title": "对象编辑器入门：修改单位属性",               "category": "object-editor",   "category_name": "对象编辑器", "search_query": "War3 对象编辑器 入门 新手 单位属性修改",               "output_dir": "docs/object-editor"},
    {"topic_id": "kk-custom-unit",          "title": "从零创建自定义单位：英雄和普通单位",          "category": "object-editor",   "category_name": "对象编辑器", "search_query": "War3 自定义单位 创建 对象编辑器 英雄 新手 教程",        "output_dir": "docs/object-editor"},
    {"topic_id": "kk-custom-ability",       "title": "制作简单技能：给英雄加专属能力",              "category": "object-editor",   "category_name": "对象编辑器", "search_query": "War3 自定义技能 对象编辑器 技能修改 新手 教程",         "output_dir": "docs/object-editor"},
    {"topic_id": "kk-unit-model",           "title": "更换单位外观模型：让单位看起来不一样",         "category": "object-editor",   "category_name": "对象编辑器", "search_query": "War3 单位模型 更换外观 自定义模型 对象编辑器",          "output_dir": "docs/object-editor"},
    {"topic_id": "kk-item-creation",        "title": "制作物品和装备：RPG道具系统入门",             "category": "object-editor",   "category_name": "对象编辑器", "search_query": "War3 物品 装备 创建 对象编辑器 RPG 道具 教程",         "output_dir": "docs/object-editor"},
    {"topic_id": "kk-buff-effect",          "title": "给技能加特效：光环、Buff 和视觉效果",         "category": "object-editor",   "category_name": "对象编辑器", "search_query": "War3 技能特效 Buff 光环 视觉效果 对象编辑器",          "output_dir": "docs/object-editor"},

    # ===== 3级：RPG核心系统 =====
    {"topic_id": "kk-rpg-hero-system",      "title": "RPG英雄系统：经验、升级和属性设计",           "category": "rpg-systems",     "category_name": "RPG系统设计","search_query": "War3 RPG 英雄 升级 经验 属性 系统 设计 教程",          "output_dir": "docs/rpg-systems"},
    {"topic_id": "kk-rpg-inventory",        "title": "背包和物品栏：让玩家能捡装备",                "category": "rpg-systems",     "category_name": "RPG系统设计","search_query": "War3 RPG 背包 物品栏 装备 掉落 系统 触发器",           "output_dir": "docs/rpg-systems"},
    {"topic_id": "kk-rpg-shop",             "title": "制作商店：让玩家用金币买东西",                "category": "rpg-systems",     "category_name": "RPG系统设计","search_query": "War3 商店 金币 购买 RPG 系统 触发器 新手",             "output_dir": "docs/rpg-systems"},
    {"topic_id": "kk-rpg-quest",            "title": "任务系统入门：制作有剧情的任务",              "category": "rpg-systems",     "category_name": "RPG系统设计","search_query": "War3 RPG 任务系统 Quest 剧情 触发器 教程",             "output_dir": "docs/rpg-systems"},
    {"topic_id": "kk-rpg-save-load",        "title": "存档读档系统：让玩家保存游戏进度",            "category": "rpg-systems",     "category_name": "RPG系统设计","search_query": "War3 RPG 存档 读档 保存进度 GameCache 教程",           "output_dir": "docs/rpg-systems"},
    {"topic_id": "kk-rpg-boss",             "title": "设计第一个BOSS：AI技能和挑战性",             "category": "rpg-systems",     "category_name": "RPG系统设计","search_query": "War3 RPG Boss 设计 AI 技能 挑战 教程 新手",            "output_dir": "docs/rpg-systems"},
    {"topic_id": "kk-multiplayer-basics",   "title": "多人地图入门：联机为什么和单机不一样",         "category": "rpg-systems",     "category_name": "RPG系统设计","search_query": "War3 多人地图 联机 同步 新手 注意事项",                "output_dir": "docs/rpg-systems"},

    # ===== 4级：地形美化 =====
    {"topic_id": "kk-terrain-5tips",        "title": "5个让新手地图看起来更好看的地形技巧",          "category": "terrain",         "category_name": "地形编辑",   "search_query": "War3 地形 新手 美化技巧 好看 入门 教程",               "output_dir": "docs/terrain"},
    {"topic_id": "kk-terrain-lighting",     "title": "灯光与氛围：让地图有场景感",                  "category": "terrain",         "category_name": "地形编辑",   "search_query": "War3 地图 灯光 氛围 昼夜 环境光 设置 教程",            "output_dir": "docs/terrain"},
    {"topic_id": "kk-region-usage",         "title": "区域Region的用法：配合触发器实现进入事件",     "category": "terrain",         "category_name": "地形编辑",   "search_query": "War3 Region 区域 触发器 进入 配合 教程 新手",          "output_dir": "docs/terrain"},

    # ===== 5级：发布运营 =====
    {"topic_id": "kk-publish-guide",        "title": "如何把地图发布到KK平台：完整上传步骤",         "category": "publishing",      "category_name": "发布与运营", "search_query": "KK平台 War3地图 发布 上传 步骤 教程 新人",             "output_dir": "docs/publishing"},
    {"topic_id": "kk-map-optimize",         "title": "地图性能优化：解决卡顿掉帧问题",              "category": "publishing",      "category_name": "发布与运营", "search_query": "War3 地图 性能优化 卡顿 FPS 掉帧 解决方法",            "output_dir": "docs/publishing"},
    {"topic_id": "kk-map-protect",          "title": "地图加密保护：防止作品被盗用",                "category": "publishing",      "category_name": "发布与运营", "search_query": "War3 地图加密 保护 防盗 方法 工具 教程",               "output_dir": "docs/publishing"},

    # ===== 6级：FAQ =====
    {"topic_id": "kk-faq-top10-errors",     "title": "新手最常遇到的10个错误和解决方法",             "category": "faq",             "category_name": "常见问题",   "search_query": "War3 编辑器 新手 常见错误 问题 解决方法 汇总",          "output_dir": "docs/faq"},
    {"topic_id": "kk-faq-resources",        "title": "哪里找帮助？新手必收藏的社区和学习资源",        "category": "faq",             "category_name": "常见问题",   "search_query": "War3 地图编辑 社区 论坛 教程资源 新手 帮助 推荐",      "output_dir": "docs/faq"},
]

added = 0
for t in NEW_TOPICS:
    if t["topic_id"] not in existing_ids:
        t.update({
            "status": "pending",
            "retry_count": 0,
            "last_error": None,
            "created_at": now,
            "updated_at": None,
            "article_path": None,
            "discovered_via": "manual",
            "priority": "high",  # 高优先级，优先生成
        })
        topics.insert(0, t)
        existing_ids.add(t["topic_id"])
        added += 1

# 按 priority 排序，high 优先
priority_order = {"high": 0, "normal": 1, None: 2}
topics.sort(key=lambda x: priority_order.get(x.get("priority"), 2))

TOPICS_PATH.write_text(json.dumps(topics, ensure_ascii=False, indent=2), encoding="utf-8")
print(f"✅ 成功添加 {added} 个 KK 入门主题")
print(f"📋 topics.json 现共 {len(topics)} 个主题")
print(f"🔝 前10个（按优先级）:")
for t in topics[:10]:
    print(f"  [{t.get('priority','normal')}] {t['topic_id']} — {t['title']}")
