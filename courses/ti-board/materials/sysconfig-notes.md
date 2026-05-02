# SysConfig 笔记

## 它解决什么问题

SysConfig 用来配置芯片型号、引脚复用、外设参数，并生成 `ti_msp_dl_config.c` 和 `ti_msp_dl_config.h`。

## 典型文件关系

```text
example.syscfg
    ↓ 生成
ti_msp_dl_config.h
ti_msp_dl_config.c
    ↓ 被包含和调用
main.c / example.c
```

## 学习者必须会解释

- `.syscfg` 不是主程序，而是配置源。
- `ti_msp_dl_config.h` 里通常有端口、引脚、外设宏定义。
- `ti_msp_dl_config.c` 里通常有初始化函数。
- 主程序常用 `SYSCFG_DL_init()` 完成初始化。

## 示例观察任务

以 `gpio_software_poll` 为例：

1. 打开 `.syscfg`，找到芯片型号。
2. 打开 `ti_msp_dl_config.h`，找到 `GPIO_LEDS_USER_LED_1_PIN`。
3. 打开 `ti_msp_dl_config.c`，找到 `SYSCFG_DL_GPIO_init()`。
4. 打开 `gpio_software_poll.c`，找到主循环如何使用这些宏。
