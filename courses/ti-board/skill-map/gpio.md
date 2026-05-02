# GPIO 技能地图

## 目标

学习者能使用 DriverLib 和 SysConfig 控制 LP-MSPM0G3507 上的数字输入输出，并能解释代码、引脚和硬件现象之间的关系。

## 必会概念

- GPIO 输入
- GPIO 输出
- 上拉电阻
- 低有效按键
- IOMUX
- 轮询
- 中断

## 本地示例

| 示例 | 用途 |
|---|---|
| `driverlib/gpio_toggle_output` | 基础输出 |
| `driverlib/gpio_software_poll` | 按键轮询 |
| `driverlib/gpio_simultaneous_interrupts` | GPIO 中断 |
| `driverlib/gpio_input_capture` | 输入捕获 |

## 训练阶梯

1. 找到 LED 和按键引脚。
2. 解释 `gpio_software_poll.c`。
3. 修改 LED 行为。
4. 解释 `.syscfg` 和 `ti_msp_dl_config.*` 的关系。
5. 做一个调试题：按键不生效时怎么查。
6. 迁移到 GPIO 中断示例。

## 掌握标准

- 能解释 PA0、PB21、LED1、S2 的对应关系。
- 能解释按键为什么低有效。
- 能独立修改 GPIO 输出行为。
- 能指出 GPIO 初始化代码在哪里。
- 能提出至少 3 步排查方法。
