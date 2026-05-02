# I2C 技能地图

## 目标

学习者能理解 I2C 控制器/目标设备通信，并能阅读基础收发示例。

## 必会概念

- SDA / SCL
- 地址
- 控制器 / 目标设备
- 读写方向
- ACK / NACK

## 本地示例

| 示例 | 用途 |
|---|---|
| `driverlib/i2c_controller_rw_multibyte_fifo_poll` | I2C 控制器轮询 |
| `driverlib/i2c_target_rw_multibyte_fifo_poll` | I2C 目标设备 |
| `msp_subsystems/uart_to_i2c_bridge` | UART 到 I2C 桥 |

## 掌握标准

- 能说明 I2C 地址的作用。
- 能区分控制器和目标设备。
- 能解释一次读写过程的大致顺序。
