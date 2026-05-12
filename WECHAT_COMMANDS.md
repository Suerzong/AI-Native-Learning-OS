# 微信可用命令速查

本文件整理 Edge-AI 工作区通过微信可用的常用命令。默认运行环境是云端或本地已连接的 cc-connect 会话；不要在微信里发送 token、私钥、密码或其他凭据。

## 使用方式

- 在微信里直接发送命令，例如：`/start-day`
- 命令后可以补充自然语言参数，例如：`/topic-study 接下来 7 天学习 C 语言指针`
- 不带命令也可以闲聊；闲聊会按 `plan/life-companion-policy.md` 处理，默认轻松回应，并将有日记价值的内容摘要记录到私密区 `personal/`

## 每日计划与复盘

| 命令 | 用途 | 示例 | 读写文件 | 适合什么时候用 |
|---|---|---|---|---|
| `/start-day` | 启动新一天，生成今日学习计划 | `/start-day 今天上午有课，下午想学神经网络` | 读 `profile.md`、`learning-progress.md`、`plan/*`、`course-index.md`；写 `plan/daily-plan.md`、`plan/record/daily/YYYY-MM-DD.md` | 早上开始学习前 |
| `/end-day` | 每日结束复盘，记录完成情况和后续调整 | `/end-day 今天完成池化层和 LeNet-5，栈没做完` | 读写 `plan/daily-plan.md`、`plan/record/daily/YYYY-MM-DD.md`；必要且有证据时才写 `learning-progress.md` | 晚上复盘时 |
| `/update-event` | 记录突发事件并调整今日计划 | `/update-event 下午临时开会，占用 2 小时` | 读写 `plan/daily-plan.md`；通常不写 `learning-progress.md` | 有临时事务、调课、身体状态变化时 |
| `/plan-next-step` | 根据当前能力画像规划未来 2-4 周 | `/plan-next-step 期末前怎么安排数据结构和神经网络？` | 读 `learning-progress.md`、`plan/roadmap.md`、`plan/timetable.md` 等；默认只输出建议 | 需要阶段规划时 |

## 掌握学习与课程辅导

| 命令 | 用途 | 示例 | 读写文件 | 适合什么时候用 |
|---|---|---|---|---|
| `/mastery-learn <课程名>` | 进入 2 Sigma 掌握学习教学循环 | `/mastery-learn neural-networks`、`/mastery-learn data-structures` | 读 `.github/agents/mastery-learn.agent.md`、`plan/spaced-review-policy.md`、课程 `course-config.md`、`mastery-tracker.md`、`mistakes.md`；会更新课程掌握度和错题 | 想正式学一小节并做练习时 |
| `/end-mastery-learn` | 结束当前掌握学习会话并收尾记录 | `/end-mastery-learn 今天先到这里` | 写当前课程 `mastery-tracker.md`、`mistakes.md`；必要时写 daily 记录；谨慎更新 `learning-progress.md` | 学完一轮、需要保存状态时 |
| `/teach-course` | 按课程资料讲解指定知识点 | `/teach-course 讲一下 LeNet-5 的结构` | 读 `learning-progress.md`、`course-index.md`、课程资料；默认不写学习进度 | 想先听讲解、不一定进入完整训练时 |
| `/topic-study` | 生成阶段性主题学习计划 | `/topic-study 接下来 14 天主攻 STM32 串口通信` | 读 `learning-progress.md`、`plan/*`、`course-index.md`；可更新 `plan/daily-plan.md` | 想围绕一个主题持续推进时 |

## 学习进度与课程信息

| 命令 | 用途 | 示例 | 读写文件 | 适合什么时候用 |
|---|---|---|---|---|
| `/update-progress` | 将明确完成的学习成果合并进能力画像 | `/update-progress 我完成了 NumPy 池化层实现和测试` | 读写 `learning-progress.md`，必须保持 12 模块完整结构 | 确实完成学习/实验/代码/复测后 |
| `/get-course-info` | 查询课程、校历、节次或时间安排 | `/get-course-info 今天第 6 节是什么时间？` | 读 `plan/school-calendar.md`、`plan/timetable.md` | 查课表、节次、假期、周次时 |

## 科技情报

| 命令 | 用途 | 示例 | 读写文件 | 适合什么时候用 |
|---|---|---|---|---|
| `/tech-intel` | 生成 Edge AI / AI 工程每日科技情报 | `/tech-intel 今天帮我抓一版 AI 晨报` | 读 `learning-progress.md`、`plan/daily-plan.md`、`tech-intel/sources.yaml`；写 `tech-intel/YYYY-MM-DD/` | 想看今日技术趋势或晨报时 |

## 微信闲聊与生活记录

| 命令 | 用途 | 示例 | 读写文件 | 适合什么时候用 |
|---|---|---|---|---|
| `/life-chat` | 轻松闲聊，并把有日记价值的内容摘要记录到私密区 | `/life-chat 今天有点累，但 LeNet-5 终于看懂了` | 读 `plan/life-companion-policy.md`；写 `personal/chat/YYYY-MM-DD.md` | 想聊天、记录心情、留下生活素材时 |
| `/chat` | `/life-chat` 的短别名 | `/chat 今天晚上心情还不错` | 同 `/life-chat` | 手机上快速输入 |
| 无命令自然闲聊 | 默认轻松回应；如果内容有日记价值，按规则摘要记录 | `今天学完以后突然感觉踏实了一点` | 写 `personal/chat/YYYY-MM-DD.md`，除非你说“别记” | 日常碎碎念、想法、心情、生活片段 |

## 隐私与记录边界

- 说“这句别记”“这段私聊别存”“不要写进日记”时，当次内容不记录。
- 说“这段适合写进日记”时，会标记为高价值日记素材。
- 闲聊记录默认只保存摘要、标签和少量代表性原话，不保存完整逐字稿。
- `personal/` 是私密区，已在 `.gitignore` 中忽略，不应提交到 Git。
- 闲聊、情绪和生活想法不代表学习能力，不写入 `learning-progress.md`。
