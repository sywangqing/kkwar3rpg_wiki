---
title: 神墓 2.7C — 🔥 08 最终战斗
category: kk-triggers
slug: shenmu/08-final
description: 最终 BOSS / 邪神相关
updated: 2026-06-01
---

# 🏆 神墓 2.7C — 🔥 08 最终战斗

> 最终 BOSS / 邪神相关

**共 1 个触发器**

## 📑 触发器目录

- [MyGod 复制](#trigger-08_000_MyGod 复制)

---

## 📜 触发器代码（中文 GUI 格式）

> 💡 提示：点击展开查看。代码可直接复制到 KKWE 编辑器。

<details id="trigger-08_000_MyGod 复制">
<summary><strong>📌 MyGod 复制</strong> <code>08_000_MyGod 复制</code></summary>

```text
触发器: MyGod 复制 (其他) [✗]
───────────────────────────────────────────────────────
事件
  └─ (无)
条件
  └─ 命令ID比较(单位当前命令(触发单位()), OperatorEqualENE, 字符串转命令ID("monsoon"))
动作
  ├─ 运行计时器 tHB50 (循环, 0.10s)
  ├─ 设置 uTemp = 最后创建的单位()
  ├─ 设置 uTemp = uPlayerHeros[循环整数A]
  └─ 伤害: uTemp→选取单位(): 10.00 (AttackTypeNormal/DamageTypeNormal)
```

</details>

