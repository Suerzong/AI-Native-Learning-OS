# 中断技能地图

## 目标

学习者能理解中断和轮询的区别，能配置并解释基础中断服务流程。

## 必会概念

- 中断源
- NVIC
- ISR
- 中断标志
- 使能与清除
- 轮询 vs 中断

## 本地示例

| 示例 | 用途 |
|---|---|
| `driverlib/gpio_simultaneous_interrupts` | GPIO 中断 |
| `driverlib/nvic_interrupt_disable` | NVIC 控制 |
| `driverlib/timer_*` | 定时中断 |

## 掌握标准

- 能说明为什么中断适合处理外部事件。
- 能找到 ISR 函数。
- 能解释中断标志为什么要清除。
- 能排查中断不触发的常见原因。
