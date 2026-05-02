# TI 板卡训练路径

本路径采用“先单点技能，再组合系统，再迁移项目”的顺序。

## 阶段 0：诊断与环境

目标：确认学习者能打开资料、定位 SDK 示例、理解板卡资源。

通过标准：

- 能说出当前板卡和芯片型号
- 能找到 `LP_MSPM0G3507/driverlib` 示例
- 能解释 `README.md`、`.c`、`.syscfg`、`ti_msp_dl_config.*` 的作用

## 阶段 1：GPIO 与板卡输入输出

目标：掌握数字输入输出、按键、LED、上拉、轮询和中断。

推荐示例：

- `gpio_toggle_output`
- `gpio_software_poll`
- `gpio_simultaneous_interrupts`

## 阶段 2：时钟、定时器、PWM 与中断

目标：理解周期事件、占空比、定时中断和基础实时控制。

推荐示例：

- `timer_*`
- `pwm_*`
- `nvic_*`

## 阶段 3：ADC、DMA 与信号采集

目标：掌握模拟采样、采样率、数据搬运和基础滤波。

推荐示例：

- `adc12_single_conversion`
- `adc12_sequence_conversion`
- `adc12_max_freq_dma`
- `msp_subsystems/adc_to_uart`

## 阶段 4：通信接口

目标：掌握 UART、I2C、SPI、CAN 的基本通信模型和调试方式。

推荐示例：

- `drivers/uart_echo`
- `i2c_controller_rw_multibyte_fifo_poll`
- `spi_*`
- `mcan_*`

## 阶段 5：系统级小项目

目标：组合多个外设完成可观察、可调试的小系统。

推荐示例：

- `msp_subsystems/adc_to_uart`
- `msp_subsystems/pushbutton_change_pwm`
- `msp_subsystems/task_scheduler`
- `msp_subsystems/fir_low_pass_filter`

## 阶段 6：Edge AI 示例

目标：理解 MCU 端数据采集、特征处理、模型推理和结果输出。

推荐示例：

- `edgeAI/hello_world_ai`
- `edgeAI/waveform_classifier_ai`
- `edgeAI/character_recognition`
- `edgeAI/*_data_capture`
