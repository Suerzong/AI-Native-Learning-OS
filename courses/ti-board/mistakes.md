# 错题与误区记录

本文件只记录会影响后续能力形成的错误，不记录一次性笔误。

## 模板

```md
## YYYY-MM-DD：错误标题

- 所属技能：
- 错误表现：
- 错误原因：
- 正确理解：
- 纠正任务：
- 是否已复测通过：
```

## 常见误区样例

### 把按键按下理解成高电平

- 所属技能：GPIO 输入
- 错误表现：认为 `if (readPins)` 表示按下
- 错误原因：没有结合上拉电阻和按键接地电路
- 正确理解：PB21 内部上拉，松开为高，按下接地为低，所以代码使用 `!DL_GPIO_readPins(...)`
- 纠正任务：画出松开/按下时 PB21 电平，并解释 LED 行为
- 是否已复测通过：否

## 2026-05-03：CCS Debug 流程混淆

- 所属技能：开发环境部署
- 错误表现：多次点击 Debug（虫子图标）启动新调试会话，不知道需要按 F8/Resume 让程序运行；Build 和 Debug 的区别不清楚
- 错误原因：Keil 迁移用户，Keil 的"下载并运行"是单步操作，CCS 是两步（Debug → F8 Resume）。这是所有 Keil 转 CCS 用户的经典障碍
- 正确理解：Debug = Build + Download + 进入调试模式 + 停在 main 第一行。停住后必须按 F8 让程序跑起来。Build 只编译不烧录
- 纠正任务：独立完成一次完整的"导入工程 → Build → Debug → F8 → 观察现象 → Terminate"流程
- 是否已复测通过：否

## 2026-05-03：XDS110 JTAG 连接失败 (Error -1001/-260)

- 所属技能：开发环境部署
- 错误表现：Test Connection 报 SC_ERR_XDS110_OPEN，Error -1001 @ 0x0
- 错误原因：XDS110 固件需要重置。通过 xdsdfu 进入 DFU 模式后重新刷写固件解决。根本原因可能是 USB 插拔过程中调试器状态异常
- 正确理解：XDS110 有两个 COM 口（User UART + Aux Data）和一个 Debug Probe。COM 口正常不代表 Debug Probe 正常。固件卡住时用 xdsdfu -m → xdsdfu -f firmware.bin -r 刷固件
- 纠正任务：遇到 JTAG 错误时，先确认 COM 口在设备管理器可见，再用 xdsdfu -e 检测，最后刷固件
- 是否已复测通过：是（固件重刷后 Test Connection 通过）
