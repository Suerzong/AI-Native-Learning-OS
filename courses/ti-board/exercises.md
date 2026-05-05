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
