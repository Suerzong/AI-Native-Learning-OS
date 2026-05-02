# SDK 示例地图

本文件帮助 agent 快速把“要训练的技能”映射到“应该看的本地示例”。

基础路径：

```text
materials/raw-sdk/mspm0_sdk_2_10_00_04/examples/nortos/LP_MSPM0G3507/
```

## GPIO

| 技能 | 示例路径 | 用途 |
|---|---|---|
| GPIO 输出 | `driverlib/gpio_toggle_output` | LED 输出/翻转 |
| GPIO 输入轮询 | `driverlib/gpio_software_poll` | S2 按键控制 LED |
| GPIO 中断 | `driverlib/gpio_simultaneous_interrupts` | 外部事件触发 |
| GPIO 输入捕获 | `driverlib/gpio_input_capture` | 输入事件观察 |

## SysConfig

| 技能 | 示例路径 | 用途 |
|---|---|---|
| 生成配置 | `driverlib/gpio_software_poll` | `.syscfg` 到 `ti_msp_dl_config.*` |
| 空工程 | `driverlib/empty` | 最小工程结构 |
| 自定义板空工程 | `../CUSTOM_BOARD/driverlib/empty_mspm0g3507` | 自定义板起点 |

## ADC / DMA

| 技能 | 示例路径 | 用途 |
|---|---|---|
| ADC 单次采样 | `driverlib/adc12_single_conversion` | 基础采样 |
| ADC 序列采样 | `driverlib/adc12_sequence_conversion` | 多通道/序列 |
| ADC + DMA | `driverlib/adc12_max_freq_dma` | 高频采样 |
| ADC 到 UART | `msp_subsystems/adc_to_uart` | 采样结果输出 |

## 通信

| 技能 | 示例路径 | 用途 |
|---|---|---|
| UART 回显 | `drivers/uart_echo` | 串口输入输出 |
| I2C 控制器 | `driverlib/i2c_controller_rw_multibyte_fifo_poll` | I2C 主机读写 |
| I2C 目标设备 | `driverlib/i2c_target_rw_multibyte_fifo_poll` | I2C 从机读写 |
| CAN | `driverlib/mcan_loopback` | CAN 基础闭环 |

## 系统级训练

| 技能 | 示例路径 | 用途 |
|---|---|---|
| ADC + UART | `msp_subsystems/adc_to_uart` | 采样后输出 |
| PWM 控制 | `msp_subsystems/pushbutton_change_pwm` | 按键改变 PWM |
| 任务调度 | `msp_subsystems/task_scheduler` | 简单调度结构 |
| FIR 滤波 | `msp_subsystems/fir_low_pass_filter` | 信号处理 |

## Edge AI

| 技能 | 示例路径 | 用途 |
|---|---|---|
| AI 入门 | `edgeAI/hello_world_ai` | 推理流程入门 |
| 波形分类 | `edgeAI/waveform_classifier_ai` | 时序分类 |
| 字符识别 | `edgeAI/character_recognition` | 图像/字符任务 |
| 数据采集 | `edgeAI/*_data_capture` | 采集训练/测试数据 |
