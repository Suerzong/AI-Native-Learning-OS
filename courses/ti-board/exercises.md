# 训练任务库

训练任务用于 10-30 分钟内完成一个明确技能点。

## 任务模板

```md
## 任务名称

- 目标技能：
- 起始文件：
- 任务要求：
- 限制条件：
- 成功标准：
- 常见错误：
- 反馈重点：
```

## GPIO-01：解释按键轮询

- 目标技能：理解 GPIO 输入轮询
- 起始文件：`materials/raw-sdk/.../gpio_software_poll/gpio_software_poll.c`
- 任务要求：逐行解释 `while (1)` 内部逻辑
- 限制条件：必须说明 PA0、PB21、上拉、低有效
- 成功标准：能解释按下和松开时 LED 为什么变化
- 常见错误：把按下理解成高电平
- 反馈重点：按键电路与代码条件判断的对应关系

## GPIO-02：反转 LED 行为

- 目标技能：修改 GPIO 输出逻辑
- 起始文件：`gpio_software_poll.c`
- 任务要求：让松开 S2 时 LED 亮，按下 S2 时 LED 灭
- 限制条件：只改主循环逻辑
- 成功标准：能说明改动前后的行为差异
- 常见错误：只改注释，没有改 `setPins/clearPins`
- 反馈重点：行为描述、代码条件、硬件电平三者一致

## GPIO-03：API 函数编写——GPIO 初始化和控制

- 目标技能：不看示例写出 GPIO 初始化 API 调用
- 起始文件：无（从零写）
- 任务要求：写出以下代码片段（只需关键代码，不用完整工程）：
  1. 初始化 PA0 为数字输出（宏名 `MY_LED`）
  2. 初始化 PB21 为数字输入，上拉
  3. 在循环中读取 PB21，按下（读到 0）时让 PA0 翻转，延时 200ms
- 限制条件：不参考 SDK 示例，只参考 DriverLib 头文件或 skill-map
- 成功标准：所有 API 函数名正确、参数位置和宏名正确、逻辑正确
- 常见错误：
  - `DL_GPIO_initDigitalOutput()` 忘记传 `IOMUX_PINCM()` 参数
  - `DL_GPIO_readPins()` 返回值直接用 `== 0` 还是 `== 1` 搞反
  - `DL_GPIO_togglePins()` 参数写成引脚名而不是 `_PIN` 宏
- 反馈重点：每个 API 的参数含义解释

## GPIO-04：SysConfig 实操——添加并重命名 GPIO

- 目标技能：在 SysConfig 中独立添加和配置 GPIO 引脚
- 起始文件：任意有 `.syscfg` 的 GPIO 示例工程
- 任务要求：
  1. 打开 `.syscfg`，把现有 LED 引脚名改为 `MY_LED1`
  2. 新增一个 GPIO 输出引脚，选 PB0，命名为 `MY_LED2`，方向 Output，初始低电平
  3. 保存 `.syscfg`，检查 `ti_msp_dl_config.h` 中是否生成了 `MY_LED1_PIN` 和 `MY_LED2_PIN` 宏
  4. 修改主程序，让两个 LED 交替闪烁（MY_LED1 亮时 MY_LED2 灭，反之亦然）
- 限制条件：必须用 SysConfig 图形界面操作，不直接改代码
- 成功标准：生成的宏名正确、主程序引用新宏名、板卡上两个 LED 交替闪烁
- 常见错误：
  - 改 SysConfig 后没保存，代码引用的宏未生成
  - 引脚名改了但主程序宏引用没同步改
  - 新增引脚选错了 PORT（应选 GPIO Port B 而非 A）
- 反馈重点：`.syscfg` 操作 → 生成代码 → 主程序引用的完整链路

## GPIO-05：API 函数速认——GPIO 函数全家桶

- 目标技能：区分 GPIO DriverLib 的 5 个写函数
- 起始文件：无
- 任务要求：不参考资料，解释以下函数的区别和应用场景：
  - `DL_GPIO_writePins()`
  - `DL_GPIO_setPins()`
  - `DL_GPIO_clearPins()`
  - `DL_GPIO_togglePins()`
  - `DL_GPIO_readPins()`
- 限制条件：必须说明每个函数的参数和典型用法
- 成功标准：5 个函数全部正确区分
- 常见错误：`writePins` 和 `setPins` 混淆；不知道 `togglePins` 内部是读-取反-写
- 反馈重点：`setPins` 只置高不关心之前状态，`writePins` 直接写目标值

---

## Printf-01：重定向 printf 到 UART

- 目标技能：Printf 调试输出（技能 2.1）
- 起始文件：`code/layer-2-advanced/printf/`
- 任务要求：阅读 `empty.c` 中 printf 重定向的实现（`fputc`），修改代码让 printf 每 500ms 输出一次系统运行时间
- 限制条件：不能使用 `delay_ms()` 阻塞，用定时器中断驱动
- 成功标准：串口助手中看到定时输出，格式为 `[t=XXXX ms] ADC=YYYY`
- 常见错误：`fputc` 实现用轮询而非中断；浮点格式 `%f` 需要链接时启用
- 反馈重点：printf 在嵌入式中的开销分析

## DMA-01：DMA 基础传输

- 目标技能：DMA 基础（技能 2.4）
- 起始文件：`code/layer-2-advanced/DMA_1/`
- 任务要求：阅读 `empty.c` 和 SysConfig 配置，画出数据从源到目标的流向图。然后修改：把 DMA 目标从 UART TX 改成另一个内存数组
- 限制条件：必须能说出 DMA 触发源是什么、每次传多少字节
- 成功标准：能解释 DMA 通道配置的四个关键参数（源地址、目标地址、传输长度、触发源）
- 常见错误：DMA 触发源选错；地址自增模式未配置；传输完成没有通知
- 反馈重点：DMA vs 轮询 vs 中断的效率对比

## DMA-02：DMA FIFO 与多通道

- 目标技能：DMA 进阶（技能 2.5）
- 起始文件：`code/layer-2-advanced/DMA_FIFO/`、`code/layer-2-advanced/DMAs_FIFO/`
- 任务要求：对比 `DMA_FIFO` 和 `DMAs_FIFO` 两个工程的 SysConfig 配置差异，说明 FIFO 阈值的作用。尝试在两个 DMA 通道中分别传输不同的数据
- 限制条件：必须能解释什么情况下用 FIFO、什么情况下不用
- 成功标准：能独立配置一个新的 DMA 通道用于不同的外设
- 常见错误：FIFO 阈值设太大导致数据延迟；多通道同时触发时数据混乱
- 反馈重点：DMA FIFO 在电赛中的实际应用场景（ADC 高速采样、LCD 刷屏）

## ADC-ADV-01：定时器触发 ADC

- 目标技能：ADC 进阶（技能 2.6）
- 起始文件：`code/layer-1-basics/ADC_Timer_Trigger/`
- 任务要求：阅读定时器触发 ADC 序列转换的代码。修改定时器周期使采样率变为 1kHz，验证采样数据的时间间隔
- 限制条件：必须理解定时器触发和软件触发的区别
- 成功标准：能解释为什么电赛中推荐用定时器触发 ADC 而不是在循环里读
- 常见错误：定时器周期计算错误；ADC 转换时间和定时器周期的关系没考虑
- 反馈重点：定时器触发 ADC 在巡线传感器采样中的应用

## Encoder-01：编码器读取与速度计算

- 目标技能：编码器（技能 3.3 配套）
- 起始文件：`code/layer-3-application/Encoder_LP_MSPM0G3507_nortos_ticlang/`
- 任务要求：阅读编码器读取代码，理解编码器模式和计数方向。添加速度计算逻辑（每 100ms 计算一次转速）
- 限制条件：必须用定时器中断周期读取编码器计数值
- 成功标准：能输出编码器原始计数和换算后的速度值
- 常见错误：编码器模式（x1/x2/x4）配置错误；计数溢出未处理；速度计算忘记清零
- 反馈重点：编码器在巡线小车电机闭环控制中的作用

## Car-01：巡线控制逻辑分析

- 目标技能：基本巡线（技能 3.3）
- 起始文件：`code/layer-3-application/line-following-car/`
- 任务要求：先运行 `car_single_line.py` 和 `car_dual_lines.py` 仿真，理解单线和双线巡线的控制策略差异。然后阅读 MCU 端 `empty.c` 和 `motor.c`，找到 PWM 控制电机的代码
- 限制条件：必须能解释 bang-bang 控制和 PID 控制的区别
- 成功标准：能在仿真中调整参数观察小车行为变化，说出各参数的含义
- 常见错误：P 系数太大导致震荡；传感器死区太大导致反应迟钝
- 反馈重点：巡线控制参数整定的工程方法

## US-01：超声波测距

- 目标技能：测距与避障（技能 3.4）
- 起始文件：`code/layer-3-application/ultrasonic-obstacle/`
- 任务要求：阅读 `ultrasonic.c/h` 的 Trig/Echo 实现，测量不同距离的物体，验证距离公式 `d = t * 340 / 2`。添加 OLED 显示距离值
- 限制条件：必须处理 Echo 超时（无回波）的情况
- 成功标准：OLED 上实时显示距离（cm），误差不超过 ±1cm
- 常见错误：忘记除以 2（声波来回）；Trig 脉冲宽度不够；Echo 超时未处理导致卡死
- 反馈重点：超声波盲区和串扰问题

## Sign-01：Edge Impulse 图像分类

- 目标技能：标识识别（技能 3.5）
- 起始文件：`code/layer-3-application/sign-recognition/`
- 任务要求：阅读 `ei_image_classification.py`，理解 Edge Impulse 模型的输入格式（图像预处理、归一化）。在 MCU 端阅读 OLED 显示和标识识别的主逻辑
- 限制条件：必须能说出从图像采集到分类结果输出的完整数据流
- 成功标准：能解释 Edge Impulse 模型如何部署到 MCU 端
- 常见错误：输入图像尺寸和模型要求不匹配；归一化参数错误
- 反馈重点：Edge AI 在 MCU 上的推理流程（采集→预处理→推理→输出）

## IMU-01：ATK-MS901M 姿态读取

- 目标技能：陀螺仪/IMU 系列（技能 4.5）
- 起始文件：`code/layer-4-integration/IMU/`、`code/layer-4-integration/IMU901/`
- 任务要求：阅读 `atk_ms901m_uart.c/h` 的 UART 协议解析代码，理解 IMU 数据帧格式。对比两个工程的差异（IMU901 多了 ADC_DMA 组合）
- 限制条件：必须能解析出加速度、角速度、角度三个数据
- 成功标准：在 OLED 上实时显示 IMU 的俯仰角和横滚角
- 常见错误：UART 波特率不匹配；数据帧解析偏移；字节序搞反
- 反馈重点：IMU 数据融合（加速度+陀螺仪→姿态角）的基本原理

## TFT-01：SPI 驱动 TFT LCD

- 目标技能：OLED/TFT LCD 显示（技能 4.1）
- 起始文件：`code/layer-4-integration/TFTlcd_spi_Hardware/`、`code/layer-4-integration/TFTlcd_spi_dma_Hardware/`
- 任务要求：先跑通硬件 SPI 版本，理解 `lcd.c/h` 的初始化序列和画点函数。再对比 SPI+DMA 版本，说出 DMA 带来的性能提升
- 限制条件：必须理解 SPI 的 CPOL/CPHA 配置对 LCD 的影响
- 成功标准：能在 LCD 上显示字符和图形，说清楚 SPI+DMA 相比纯 SPI 快在哪里
- 常见错误：SPI 模式（CPOL/CPHA）配置错误导致花屏；DMA 缓冲区大小和 LCD 分辨率不匹配
- 反馈重点：LCD 驱动移植的通用方法（看初始化序列→移植画点→封装图形函数）
