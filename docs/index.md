---
layout: page
title: KK 作者中心 · 跳转中
sidebar: false
aside: false
head:
  - - meta
    - http-equiv: refresh
      content: '0; url=/author/'
---

<script setup>
import { onMounted } from 'vue'
import { useRouter, withBase } from 'vitepress'
const router = useRouter()
onMounted(() => {
  router.go(withBase('/author/'))
})
</script>

<div style="text-align:center;padding:6rem 1rem;color:var(--vp-c-text-2)">
  <p style="font-size:1.125rem">正在跳转到 <a :href="'/author/'" style="color:var(--vp-c-brand-1)">KK 作者中心</a>……</p>
  <p style="font-size:.875rem;margin-top:1rem">如未自动跳转，请<a href="/author/">点击这里</a></p>
  <p style="font-size:.75rem;margin-top:2rem;color:var(--vp-c-text-3)">想看旧版首页？<a href="/legacy">查看 legacy</a></p>
</div>
