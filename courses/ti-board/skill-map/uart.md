# UART 技能地图

## 目标

学习者能使用 UART 完成串口收发、回显和基础调试输出。

## 必会概念

- 波特率
- TX / RX
- 轮询发送
- 中断接收
- 串口调试

## 本地示例

| 示例 | 用途 |
|---|---|
| `drivers/uart_echo` | 串口回显 |
| `driverlib/uart_*` | DriverLib UART 示例 |
| `msp_subsystems/adc_to_uart` | ADC 数据串口输出 |

## 掌握标准

- 能解释 TX/RX 连接关系。
- 能修改波特率相关配置。
- 能发送调试文本或数据。
- 能排查串口无输出的常见原因。
