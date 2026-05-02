# SDK 索引

SDK 路径：

```text
materials/raw-sdk/mspm0_sdk_2_10_00_04/
```

当前已精简保留：

```text
mspm0_sdk_2_10_00_04/
├── docs/
├── examples/
├── source/
└── imports.mak
```

## 关键目录

| 目录 | 用途 | 是否常用 |
|---|---|---|
| `examples/` | 官方示例工程 | 高频 |
| `source/` | DriverLib、CMSIS、设备头文件等源码 | 高频 |
| `docs/` | 官方文档 | 中频 |
| `imports.mak` | Makefile 构建变量 | 低频 |

## 当前重点示例路径

```text
examples/nortos/LP_MSPM0G3507/
├── driverlib/
├── drivers/
├── edgeAI/
├── msp_subsystems/
└── supplemental_examples/
```

## 自定义板模板

```text
examples/nortos/CUSTOM_BOARD/driverlib/empty_mspm0g3507/
```

用途：为 MSPM0G3507 自定义板建立最小空工程模板。
