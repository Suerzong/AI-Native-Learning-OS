# DMA 技能地图

## 目标

学习者能理解 DMA 为什么能减少 CPU 搬运数据，并能阅读 ADC + DMA 示例。

## 必会概念

- 源地址
- 目标地址
- 传输长度
- 触发源
- Ping-Pong 缓冲

## 本地示例

| 示例 | 用途 |
|---|---|
| `driverlib/dma_block_transfer` | DMA 块传输 |
| `driverlib/adc12_max_freq_dma` | ADC + DMA |
| `msp_subsystems/adc_dma_ping_pong` | 双缓冲采样 |

## 掌握标准

- 能解释 CPU 搬运和 DMA 搬运的区别。
- 能找到 DMA 传输源、目标和长度。
- 能说明 DMA 适合哪些场景。
