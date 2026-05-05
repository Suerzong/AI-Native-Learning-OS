# SysConfig 技能地图

## 目标

学习者能独立使用 SysConfig 图形化工具配置 MSPM0 外设和引脚，理解 `.syscfg` 如何生成 `ti_msp_dl_config.c/.h`，并能把图形化配置、生成代码和主程序调用联系起来。

## 必会概念

- `.syscfg` 文件的作用和结构
- 生成代码流程：保存 `.syscfg` → 自动生成 `ti_msp_dl_config.c/.h`
- PinMux / IOMUX：引脚复用配置
- `SYSCFG_DL_init()`：外设初始化总入口
- `ti_msp_dl_config.h`：生成的宏定义（引脚名、外设句柄等）
- `ti_msp_dl_config.c`：生成的初始化代码

## 必会操作（实操）

1. 打开 `.syscfg` 文件，认识左侧外设列表、右侧属性面板、中间引脚视图
2. 在 SysConfig 中添加一个 GPIO 输出引脚，修改名称（如 `MY_LED`）、方向（Output）、初始电平
3. 在 SysConfig 中添加一个 GPIO 输入引脚，配置上拉/下拉
4. 在 SysConfig 中添加 Timer/PWM/ADC/UART 外设
5. 理解 `SYSCFG_DL_init()` 内部调用了哪些初始化函数
6. 修改 SysConfig 后，对比 `ti_msp_dl_config.h` 的变化

## 本地示例

| 示例 | 用途 |
|---|---|
| `driverlib/gpio_software_poll` | GPIO 配置生成 |
| `driverlib/gpio_toggle_output` | 基础 GPIO 输出配置 |
| `driverlib/adc12_single_conversion` | ADC 配置生成 |
| `driverlib/uart_*` | 串口配置生成 |
| `driverlib/timer_periodic_toggle` | Timer 配置生成 |

## 训练阶梯（必须包含实操）

1. **识别**：打开 `gpio_toggle_output.syscfg`，指出 LED 引脚叫什么名字、方向是什么。
2. **解释**：找出 `ti_msp_dl_config.h` 中由 SysConfig 生成的宏，说明哪些宏是主程序用到的。
3. **跟做修改**：在 SysConfig 中把 LED 引脚名改为 `MY_LED1`，保存后观察 `ti_msp_dl_config.h` 的宏名变化，同步修改主程序中的宏引用。
4. **独立添加**：不参考已有工程，新建一个空 `.syscfg`，添加一个 GPIO 输出引脚（选任意空闲引脚如 PB0），命名为 `TEST_OUT`，方向 Output，初始高电平。
5. **添加外设**：在 SysConfig 中添加一个 Timer，配置为周期模式，周期 1ms，使能中断。验证生成的 `ti_msp_dl_config.c` 中包含了 Timer 初始化代码。
6. **综合配置**：同时添加 2 个 GPIO 输出 + 1 个 GPIO 输入 + 1 个 Timer，检查无冲突。

## 掌握标准

- 能独立新建 `.syscfg` 并添加 GPIO 输出/输入引脚。
- 能独立添加 Timer/PWM/ADC 等外设。
- 能解释 `.syscfg` 中每个配置项在生成的代码中对应什么。
- 能说出 `SYSCFG_DL_init()` 的执行顺序。
- 修改 SysConfig 后能同步更新主程序中的宏引用。
