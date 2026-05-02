# LP-MSPM0G3507 板卡信息

## 基本信息

- 板卡：LP-MSPM0G3507 LaunchPad
- 主芯片：MSPM0G3507
- 官方用户指南：`datasheets/MSPM0G3507 LaunchPad Development Kit User's Guide.pdf`

## 当前已知资源

| 资源 | 引脚 | 说明 | 参考示例 |
|---|---|---|---|
| LED1 | PA0 | 可由 GPIO 控制 | `gpio_software_poll` |
| S2 按键 | PB21 | 内部上拉，按下接地，低有效 | `gpio_software_poll` |
| SWCLK | PA20 | 调试时钟 | 板卡用户指南 |
| SWDIO | PA19 | 调试数据 | 板卡用户指南 |

## Agent 使用方式

当学习者遇到“代码和板子现象对不上”时，优先查本文件和板卡用户指南。

## 个性化补充

把实际接线、跳帽设置、外接模块记录在这里。

```md
## YYYY-MM-DD 接线记录

- 外设/模块：
- 连接引脚：
- 电源：
- 注意事项：
```
