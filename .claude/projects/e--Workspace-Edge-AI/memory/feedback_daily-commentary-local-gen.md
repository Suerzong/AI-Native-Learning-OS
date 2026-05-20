---
name: 每日时评禁止本地生成
description: 每日时评原创命题只能在云端服务器生成，禁止本地生成
type: feedback
---

每日时评（daily-commentary）原创命题只能在云端服务器（tx）生成，禁止在本地生成。

**Why:** 本地和云端各自运行命题生成流程会产生竞态条件（race condition），导致同一日期出现两套不同题目。云端是用户正常学习流程（start-day → daily-commentary → score-commentary 一体化），本地生成的题目无法接入这个流程。

**How to apply:** 当用户在本地触发 `/sync` 后再提到"生成题目""每日时评"等，不要生成。如果 `daily-commentary/YYYY-MM-DD/` 在本地不存在，先 sync pull 拉取云端版本，而不是本地补生成。
