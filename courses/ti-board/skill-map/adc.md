# ADC 技能地图

## 目标

学习者能完成基础模拟采样，并理解采样通道、参考电压、采样率和结果转换。

## 必会概念

- 模拟输入
- ADC 分辨率
- 参考电压
- 单次采样
- 序列采样
- DMA 采样

## 本地示例

| 示例 | 用途 |
|---|---|
| `driverlib/adc12_single_conversion` | 单次采样 |
| `driverlib/adc12_sequence_conversion` | 多通道/序列采样 |
| `driverlib/adc12_max_freq_dma` | ADC + DMA |
| `msp_subsystems/adc_to_uart` | 采样结果串口输出 |

## 掌握标准

- 能找到 ADC 输入引脚。
- 能解释采样结果代表的电压。
- 能把采样结果通过 UART 或变量观察输出。
- 能说明采样异常时的排查路径。
