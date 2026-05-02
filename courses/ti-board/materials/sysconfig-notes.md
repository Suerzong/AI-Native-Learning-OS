# SysConfig Notes

# SysConfig Notes

## SysConfig 是什么

SysConfig 是 TI 提供的图形化配置工具，用于配置外设、引脚、时钟、中断和驱动参数，并生成初始化代码。

## 为什么重要

对于 LP_MSPM0G3507 学习，SysConfig 会影响：

- GPIO 配置
- UART 配置
- I2C / SPI 配置
- ADC 配置
- Timer / PWM 配置
- 中断配置
- 引脚复用

## 学习目标

1. 能打开 SysConfig；
2. 能添加外设；
3. 能配置引脚；
4. 能生成代码；
5. 能理解生成代码和 DriverLib 调用之间的关系；
6. 能修改配置并验证硬件现象。

## 常见问题记录

### 问题 1：修改引脚后代码没有生效

可能原因：

- 没有重新生成 SysConfig；
- 工程没有重新编译；
- 引脚复用冲突；
- 板卡实际引脚与配置不一致。

解决方法：

……