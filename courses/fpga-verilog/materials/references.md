# 学习资源索引

## 核心题库

| 资源 | 路径/链接 | 说明 |
|------|----------|------|
| F学社题库（Markdown） | `~/Edge-AI/temp/zzfpga-question-bank/fpga-question-bank.md` | 345 道题含答案，按类型分组 |
| F学社题库（原始数据） | `~/Edge-AI/temp/zzfpga-question-bank/raw_data.json` | API 原始 JSON 数据 |
| F学社题库（答案） | `~/Edge-AI/temp/zzfpga-question-bank/answers.json` | 227 道编程题 Verilog 答案 |
| F学社在线平台 | https://www.zzfpga.com/StudentPlatform/Sheet/QuestionBank | 在线练习和提交 |

## 在线学习平台

| 资源 | 链接 | 说明 |
|------|------|------|
| HDLBits | https://hdlbits.01xz.net/wiki/Main_Page | Verilog 在线练习，从基础到高级 |
| FPGA4student | https://www.fpga4student.com/ | FPGA 教程和项目 |
| ASIC World | https://www.asic-world.com/verilog/ | Verilog 语法参考 |
| EDA Playground | https://www.edaplayground.com/ | 在线 Verilog 仿真 |

## 参考教材

| 教材 | 说明 | 对应章节 |
|------|------|---------|
| 《Verilog 数字系统设计教程》夏宇闻 | 经典中文教材 | 全部 |
| 《FPGA 原理与结构》 | FPGA 架构基础 | 第一层 |
| 《数字设计与计算机体系结构》Harris | 从门电路到 CPU | 全部 |
| IEEE 1364 Verilog 标准 | 语法规范参考 | 按需查阅 |

## 工具文档

| 工具 | 说明 | 对应阶段 |
|------|------|---------|
| Vivado Design Suite | Xilinx FPGA 开发工具 | 全部 |
| Quartus Prime | Intel/Altera FPGA 开发工具 | 全部 |
| Icarus Verilog + GTKWave | 开源 Verilog 仿真器 | 学习阶段 |
| ModelSim | 专业仿真工具 | 进阶阶段 |

## Verilog 教程

| 资源 | 说明 | 对应章节 |
|------|------|---------|
| 菜鸟教程 Verilog（本地版） | `~/Edge-AI/temp/runoob-verilog/verilog-tutorial-complete.md` — 35 章节完整版（109KB） | 全部 |
| 菜鸟教程 Verilog（在线） | https://www.runoob.com/w3cnote/verilog-tutorial.html | 全部 |
| HDLBits 练习题 | https://hdlbits.01xz.net/wiki/Main_Page — 按知识点分类的在线练习 | 第一、二层 |

**菜鸟教程章节对照**：
- 1.x 章节 → 课程第一层（组合逻辑基础）：简介、环境搭建、设计方法
- 2.x 章节 → 课程第一层：基础语法、数据类型、数值表示、表达式、编译指令
- 3.x 章节 → 课程第一层：连续赋值、时延
- 4.x 章节 → 课程第二层（时序逻辑）：过程结构、过程赋值、时序控制、语句块、条件语句、循环语句、过程连续赋值
- 5.x 章节 → 课程第一/三层：模块与端口、模块例化、带参数例化
- 6.x 章节 → 课程第二/三层：函数、任务、状态机、竞争与冒险、避免 Latch、仿真激励、流水线
- 7.x 章节 → 课程第四层（系统设计）：除法器、并行/串行 FIR、CIC、FFT、DDS
- 8.x 章节 → 课程第一层：数值转换

## FPGA 架构参考

| 资源 | 说明 |
|------|------|
| Xilinx 7 Series User Guide | CLB、IOB、BRAM、DSP48 结构 |
| Xilinx UG901 Vivado 综合指南 | 综合约束和优化策略 |
| Intel Cyclone V Handbook | Cyclone V FPGA 架构 |

## 接口协议参考

| 协议 | 参考资料 |
|------|---------|
| UART | https://en.wikipedia.org/wiki/Universal_asynchronous_receiver-transmitter |
| SPI | https://en.wikipedia.org/wiki/Serial_Peripheral_Interface |
| I2C | NXP I2C 总线规范 |
| VGA | VGA 时序参数标准 |
| HDMI | HDMI 1.4 规范 |

## 学习路径建议

**快速入门**（4 周）：
1. 第一周：HDLBits 基础练习 + 门电路、MUX、编码器
2. 第二周：F 学社题库第一层 + 触发器、计数器
3. 第三周：F 学社题库第二层 + 状态机
4. 第四周：F 学社题库第三层 + 接口协议

**深入学习**（8 周）：
1-2 周：第一层全部 + 阶段一考试
3-4 周：第二层全部 + 阶段二考试
5-6 周：第三层全部 + 阶段三考试
7-8 周：第四层全部 + 综合项目
