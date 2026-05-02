# 核心概念索引

本文件记录学习者需要掌握的关键概念。每个概念都应能回答三个问题：它是什么、为什么需要它、在本板卡代码里哪里出现。

| 概念 | 简要说明 | 对应资料 |
|---|---|---|
| GPIO | 数字输入输出引脚控制 | `skill-map/gpio.md` |
| 上拉电阻 | 让未按下的按键输入保持稳定高电平 | `gpio_software_poll` |
| 低有效 | 按下后读到 0，而不是 1 | `gpio_software_poll` |
| SysConfig | TI 的外设和引脚配置工具 | `skill-map/sysconfig.md` |
| DriverLib | TI 提供的外设驱动库 | `materials/raw-sdk/.../source/ti/driverlib` |
| 中断 | 外设事件触发 CPU 响应 | `skill-map/interrupt.md` |
| PWM | 用占空比控制平均输出 | `skill-map/pwm.md` |
| ADC | 把模拟电压转换成数字值 | `skill-map/adc.md` |
| UART | 异步串口通信 | `skill-map/uart.md` |
| I2C | 双线总线通信 | `skill-map/i2c.md` |
| SPI | 同步串行通信 | `skill-map/spi.md` |
| DMA | 外设和内存间自动搬运数据 | `skill-map/dma.md` |
