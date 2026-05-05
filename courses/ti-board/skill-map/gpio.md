# GPIO 技能地图

## 目标

学习者能使用 DriverLib API 和 SysConfig 控制 LP-MSPM0G3507 上的数字输入输出，能不看示例写出 GPIO 初始化和控制的完整代码，并能解释代码、引脚和硬件现象之间的关系。

## 必会概念

- GPIO 输入 / GPIO 输出
- 上拉电阻 / 下拉电阻
- 低有效按键（按下为低电平）
- IOMUX（引脚复用）
- 轮询 vs 中断

## 必会 DriverLib API（必须能不看示例写出调用）

| 函数 | 头文件 | 用途 | 关键参数 |
|------|--------|------|---------|
| `DL_GPIO_initDigitalOutput()` | `ti/driverlib/dl_gpio.h` | 初始化 GPIO 为数字输出 | `GPIO_Output_Pin_0_MASK`, `IOMUX_PINCM(引脚号)` |
| `DL_GPIO_initDigitalInput()` | `ti/driverlib/dl_gpio.h` | 初始化 GPIO 为数字输入 | `GPIO_InternalResistor_Pull_UP` |
| `DL_GPIO_writePins()` | `ti/driverlib/dl_gpio.h` | 写指定引脚（高/低） | `GPIO_OUT_PIN`, `value` |
| `DL_GPIO_setPins()` | `ti/driverlib/dl_gpio.h` | 将指定引脚置高 | `GPIO_OUT_PIN` |
| `DL_GPIO_clearPins()` | `ti/driverlib/dl_gpio.h` | 将指定引脚置低 | `GPIO_OUT_PIN` |
| `DL_GPIO_togglePins()` | `ti/driverlib/dl_gpio.h` | 翻转指定引脚电平 | `GPIO_OUT_PIN` |
| `DL_GPIO_readPins()` | `ti/driverlib/dl_gpio.h` | 读取指定引脚电平 | `GPIO_IN_PIN` |
| `DL_GPIO_initDigitalInputFeatures()` | `ti/driverlib/dl_gpio.h` | 初始化 GPIO 输入（带中断功能） | `DL_GPIO_INVERSION_DISABLE`, `DL_GPIO_RESISTOR_PULL_UP` |

## 必会 SysConfig 操作

- 添加 GPIO Output 引脚，设置名称、方向、初始电平
- 添加 GPIO Input 引脚，设置上拉/下拉
- 理解 SysConfig 生成的宏：`引脚名_PIN`、`引脚名_PORT`

## 本地示例

| 示例 | 用途 |
|---|---|
| `driverlib/gpio_toggle_output` | 基础输出翻转 |
| `driverlib/gpio_software_poll` | 按键轮询控制 LED |
| `driverlib/gpio_simultaneous_interrupts` | GPIO 中断 |
| `driverlib/gpio_input_capture` | 输入捕获 |

## 训练阶梯（优先 API 函数 + SysConfig 实操）

1. **SysConfig 识别**：打开 `gpio_toggle_output.syscfg`，找到 LED 引脚名、方向、初始电平。
2. **API 识别**：在 `gpio_toggle_output.c` 中找到 `DL_GPIO_initDigitalOutput()` 调用，说出每个参数的含义。
3. **API 解释**：解释 `DL_GPIO_setPins()` 和 `DL_GPIO_clearPins()` 的区别，解释 `DL_GPIO_togglePins()` 的内部行为。
4. **SysConfig 跟做**：把 LED 引脚名从默认值改为 `MY_LED`，同步修改主程序的宏引用。添加第二个 LED 引脚 `MY_LED2`。
5. **API 编写**：不参考示例，写出初始化 PA0 为输出、PB21 为上拉输入、读取 PB21 并翻转 PA0 的完整代码片段。
6. **代码修改**：修改 LED 闪烁频率和占空比（用延时控制）。
7. **迁移编写**：从轮询示例迁移——不看 `gpio_toggle_output.c`，写出用另一个引脚控制另一个 LED 的完整代码。
8. **调试**：按键按下 LED 不变化时，列出排查顺序（先查硬件接线 → 查 SysConfig 上拉配置 → 查代码条件判断 → 查生成的宏名）。

## 掌握标准

- 能独立在 SysConfig 中添加 GPIO 输出和输入引脚。
- 能不参考示例写出 GPIO 初始化、读写、翻转的 DriverLib API 调用。
- 能解释 PA0、PB21、LED1、S2 的对应关系。
- 能解释按键为什么低有效。
- 能提出至少 3 步排查方法。
