# SysConfig 技能地图

## 目标

学习者能理解 `.syscfg` 文件如何生成 `ti_msp_dl_config.c/.h`，并能把图形化配置、生成代码和主程序调用联系起来。

## 必会概念

- `.syscfg`
- 生成代码
- PinMux / IOMUX
- `SYSCFG_DL_init()`
- `ti_msp_dl_config.h`
- `ti_msp_dl_config.c`

## 本地示例

| 示例 | 用途 |
|---|---|
| `driverlib/gpio_software_poll` | GPIO 配置生成 |
| `driverlib/adc12_single_conversion` | ADC 配置生成 |
| `driverlib/uart_*` | 串口配置生成 |

## 训练任务

1. 找出 `.syscfg` 中声明的设备型号。
2. 找出 `ti_msp_dl_config.h` 中生成的宏。
3. 解释 `SYSCFG_DL_init()` 调用了哪些初始化函数。
4. 判断主程序依赖哪些生成的宏。
