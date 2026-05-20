# F学社 FPGA 题库
> 共 345 道题目（选择题 117，判断题 1，编程题 208，硬件题 19）
> 数据来源: https://www.zzfpga.com/StudentPlatform/Sheet/QuestionBank
> 抓取时间: 2026-05-14 08:16

---

## 一、选择题 (117 道)

### 1. 以下哪种不属于FPGA里的逻辑资源
- **类型**: 单选题　**难度**: 简单

以下哪种不属于FPGA里的逻辑资源

A. A.Slice（分组到可配置的逻辑块）
B. B.Memory（存储器）
C. C.Multipliers(乘法器)
D. D.Global Clock buffers(全局时钟缓冲器) **[正确]**

---

### 2. 每个可配置逻辑块(CLB)里有几个slice?
- **类型**: 单选题　**难度**: 简单

每个可配置逻辑块(CLB)里有几个slice?

A. A.1
B. B.4
C. C.2 **[正确]**
D. D.3

---

### 3. Spartan-7和Artix-7里的每一个查找表(LUT)有几个输入?
- **类型**: 单选题　**难度**: 简单

Spartan-7和Artix-7里的每一个查找表(LUT)有几个输入?

A. A.4
B. B.6 **[正确]**
C. C.5
D. D.8

---

### 4. Slice里的资源不包括以下哪个
- **类型**: 单选题　**难度**: 简单

Slice里的资源不包括以下哪个

A. A.Multipliers(乘法器) **[正确]**
B. B.LUT(查找表)
C. C.Carry Chain 进位链
D. D.Flip-Flops/Latch(寄存器/锁存器)

---

### 5. Slice分为2种类型，以下哪2种是对的
- **类型**: 单选题　**难度**: 简单

Slice分为2种类型，以下哪2种是对的

A. A.SliceL 和SliceM **[正确]**
B. B.SliceL 和SliceX
C. C.SliceX 和SliceH
D. D.SliceH和SliceM

---

### 6. Slice里的F7MUX可实现X-1的多路复用器(multiplexer)，X是多少
- **类型**: 单选题　**难度**: 简单

Slice里的F7MUX可实现X-1的多路复用器(multiplexer)，X是多少

A. A.6
B. B.8 **[正确]**
C. C.12
D. D.16

---

### 7. Slice里的进位链(CarryChain)功能描述不正确的是哪个
- **类型**: 单选题　**难度**: 简单

Slice里的进位链(CarryChain)功能描述不正确的是哪个

A. A.可实现快速加减法
B. B.贯穿了4个LUT查找表
C. C.向下传播到下方位置的CLB **[正确]**
D. D.实现Slice与Slice之间的快速串联

---

### 8. 每个Slice里面有几个FF与几个FF/L
- **类型**: 单选题　**难度**: 简单

每个Slice里面有几个FF与几个FF/L

A. A.2个FF和6个FF/L
B. B.2个FF和4个FF/L
C. C.4个FF和6个FF/L
D. D.4个FF和4个FF/L **[正确]**

---

### 9. 一个Slice里面的FF(Flip-Flop)以下描述哪个不正确
- **类型**: 单选题　**难度**: 简单

一个Slice里面的FF(Flip-Flop)以下描述哪个不正确

A. A.可实现D型触发器，有一个Q输出
B. B.所有的EF有一个高电平有效的CE使能信号
C. C.一个Slice里面的所有FF共享一个CK时钟信号
D. D.有一个低电平有效的SR复位信号 **[正确]**

---

### 10. 一个SliceM实现成分布式存储器，以下哪个描述不正确
- **类型**: 单选题　**难度**: 简单

一个SliceM实现成分布式存储器，以下哪个描述不正确

A. A.1给LUT可以实现64x1或32x2的RAM
B. B.SliceM里的LUT级联最大可实现128x1的单端口RAM **[正确]**
C. C.一个Slice里面的所有FF共享一个CK时钟信号
D. D.有一个低电平有效的SR复位信号

---

### 11. 以下那种不属于FPGA里的逻辑资源（Logic Resources）
- **类型**: 单选题　**难度**: 简单

以下那种不属于FPGA里的逻辑资源（Logic Resources）

A. A.Slice(分组到可配置的逻辑块（CLB）)
B. B.Memory（存储器
C. C.Multipliers（乘法器）
D. D.Global Clock buffers（全局时钟缓冲器） **[正确]**

---

### 12. 每个可配置逻辑块（CLB）里有几个Slice？
- **类型**: 单选题　**难度**: 简单

每个可配置逻辑块（CLB）里有几个Slice？

A. A.1
B. B.4
C. C.2 **[正确]**
D. D.3

---

### 13. Spartan-7和Artix-7里的每一个查找表（LUT）有几个输入？
- **类型**: 单选题　**难度**: 简单

Spartan-7和Artix-7里的每一个查找表（LUT）有几个输入？

A. A.4
B. B.6 **[正确]**
C. C.5
D. D.8

---

### 14. Slice里的资源不包括以下哪个
- **类型**: 单选题　**难度**: 简单

Slice里的资源不包括以下哪个

A. A.Multipliers（乘法器） **[正确]**
B. B.LUT(查找表)
C. C.Carry Chain 进位链
D. D.Flip-Flops/Latch（寄存器/锁存器）

---

### 15. Slice分为2种类型，以下哪2种是对的
- **类型**: 单选题　**难度**: 简单

Slice分为2种类型，以下哪2种是对的

A. A.SliceL 和 SliceM **[正确]**
B. B.SliceL 和 SliceX
C. C.SliceX 和 SliceH
D. D.SliceH 和 SliceM

---

### 16. Slice里的F7MUX可实现X-1的多路复用器(multiplexer)，X是多少
- **类型**: 单选题　**难度**: 简单

Slice里的F7MUX可实现X-1的多路复用器(multiplexer)，X是多少

A. A.6
B. B.8 **[正确]**
C. C.12
D. D.16

---

### 17. Slice里的进位链（Carry Chain）功能描述不正确的是哪个
- **类型**: 单选题　**难度**: 简单

Slice里的进位链（Carry Chain）功能描述不正确的是哪个

A. A.可实现快速加减法
B. B.贯穿了4个LUT查找表
C. C.向下传播到下方位置的CLB **[正确]**
D. D.现Slice与Slice之间的快速串联

---

### 18. 每个Slice里面有几个FF与几个FF/L
- **类型**: 单选题　**难度**: 简单

每个Slice里面有几个FF与几个FF/L

A. A.2个FF和6个FF/L
B. B.2个FF和4个FF/L
C. C.4个FF和6个FF/L
D. D.4个FF和4个FF/L **[正确]**

---

### 19. 一个Slice里面的FF(Flip-Flop)以下描述哪个不正确
- **类型**: 单选题　**难度**: 简单

一个Slice里面的FF(Flip-Flop)以下描述哪个不正确

A. A.可实现D型触发器，有一个Q输出
B. B.所有的FF有一个高电平有效的CE使能信号
C. C.一个Slice里面的所有FF共享一个CK时钟信号
D. D.有一个低电平有效的SR复位信号 **[正确]**

---

### 20. 一个SliceM实现成分布式存储器，以下哪个描述不正确
- **类型**: 单选题　**难度**: 简单

一个SliceM实现成分布式存储器，以下哪个描述不正确

A. A.1给LUT可以实现64x1或32x2的RAM
B. B.SliceM里的LUT级联最大可实现128x1的单端口RAM **[正确]**
C. C.双端口RAM 可实现1 个读/写端口 + 1 个只读端口
D. D.简单的双端口RAM(SDP)可实现1 个只写端口 + 1 个只读端口

---

### 21. 1个SLICEM实现的移位寄存器（Shift Register）最多可以实现多少位的移位寄存器
- **类型**: 单选题　**难度**: 简单

1个SLICEM实现的移位寄存器（Shift Register）最多可以实现多少位的移位寄存器

A. A.32位
B. B.64位
C. C.128位 **[正确]**
D. D.256位

---

### 22. 计算题：要实现32位总线数据，实现13个周期的延时，需要416个Flip-flops资源，若改用SliceM的SRL实现，总共需要几个SRL?
- **类型**: 单选题　**难度**: 简单

计算题：要实现32位总线数据，实现13个周期的延时，需要416个Flip-flops资源，若改用SliceM的SRL实现，总共需要几个SRL?

A. A.13
B. B.20
C. C.32 **[正确]**
D. D.416

---

### 23. 以下哪个不在7系列FPGA的IO电平标准支持范围内
- **类型**: 单选题　**难度**: 简单

以下哪个不在7系列FPGA的IO电平标准支持范围内

A. A.1.2v
B. B.1.8v
C. C.2.5v
D. D.5v **[正确]**

---

### 24. FPGA IO的输入判断哪个是正确的
- **类型**: 单选题　**难度**: 简单

FPGA IO的输入判断哪个是正确的

A. A.标准CMOS 逻辑0为接近VCCO，逻辑1为接近地
B. B.当有参考电压Vref时，输入大于Vref被判定为逻辑1，小于Vref被判断为逻辑0 **[正确]**
C. C.P/N端口只能被配置成独立的单端信号
D. D.P/N端口只能被配置成一对差分信号对

---

### 25. IO逻辑资源中，分别不含有的资源是什么
- **类型**: 单选题　**难度**: 简单

IO逻辑资源中，分别不含有的资源是什么

A. A.I/OCLOCK **[正确]**
B. B.I/OLogic
C. C.I/ODELAY
D. D.I/OSERDES

---

### 26. ISERDES输入的串行数据可以输出最大的单倍速数据是多少位
- **类型**: 单选题　**难度**: 简单

ISERDES输入的串行数据可以输出最大的单倍速数据是多少位

A. A.8位 **[正确]**
B. B.10位
C. C.14位
D. D.16位

---

### 27. 以下对FPGA里面的BLOCK RAM和FIFO描述不正确的是
- **类型**: 单选题　**难度**: 简单

以下对FPGA里面的BLOCK RAM和FIFO描述不正确的是

A. A.7 系列系列的所有成员都具有相同的块 RAM/FIFO
B. B.所有操作都是同步的;所有输出均闭锁
C. C.两个独立的端口访问公共数据
D. D.需要更高频率操作时需要外部的流水线寄存器支持 **[正确]**

---

### 28. 对BLOCK RAM容量描述正确的是
- **类型**: 单选题　**难度**: 简单

对BLOCK RAM容量描述正确的是

A. A.每个BLOCK RAM 容量为32Kb **[正确]**
B. B.每个BLOCK RAM 容量为64Kb
C. C.每个BLOCK RAM 容量为18Kb
D. D.每个BLOCK RAM 容量为24Kb

---

### 29. BLOCK RAM被配置成双端口模式的描述哪个不正确
- **类型**: 单选题　**难度**: 简单

BLOCK RAM被配置成双端口模式的描述哪个不正确

A. A.拥有两个独立的读写端口
B. B.两个端口共享时钟信号 **[正确]**
C. C.两个端口有独立的地址信号
D. D.两个端口可以配置成不同的数据位宽

---

### 30. 7系列的DSP48E1模块可实现加法运算，以下描述不正确的是
- **类型**: 单选题　**难度**: 简单

7系列的DSP48E1模块可实现加法运算，以下描述不正确的是

A. A.可实现12位+12位的加法
B. B.可实现24位+24位的加法
C. C.可实现48位+48位的加法
D. D.不可实现128位+128位的加法 **[正确]**

---

### 31. 7系列的DSP48E1模块可实现乘法运算，单个DSP48E1模块最多可实现多少位的乘法运算
- **类型**: 单选题　**难度**: 简单

7系列的DSP48E1模块可实现乘法运算，单个DSP48E1模块最多可实现多少位的乘法运算

A. A.20x18
B. B.48x48
C. C.25x18 **[正确]**
D. D.30x18

---

### 32. 7系列开始的FPGA就开始集成了内置的XADC模块，可实现模拟/数字信号的转换，以下功能描述不正确的是？
- **类型**: 单选题　**难度**: 简单

7系列开始的FPGA就开始集成了内置的XADC模块，可实现模拟/数字信号的转换，以下功能描述不正确的是？

A. A.18 路灵活的模拟输入以及带可编程信号调理的采样和保持 **[正确]**
B. B.双通道 12 位 1Msps ADC
C. C.1V输入范围
D. D.16 位分辨率转换

---

### 33. 每个时钟域（Clock regions）的高度是
- **类型**: 单选题　**难度**: 简单

每个时钟域（Clock regions）的高度是

A. A.40个CLBs
B. B.50个CLBs **[正确]**
C. C.60个CLBs
D. D.70个CLBs

---

### 34. 一个时钟管理单元（CMT）包含几个MMCM和几个PLL
- **类型**: 单选题　**难度**: 简单

一个时钟管理单元（CMT）包含几个MMCM和几个PLL

A. A.2个MMCM和1个PLL
B. B.1个MMCM和2个PLL
C. C.1个MMCM和1个PLL **[正确]**
D. D.1个MMCM和0个PLL

---

### 35. 全局时钟网络的驱动需要通过哪种buffer缓冲器
- **类型**: 单选题　**难度**: 简单

全局时钟网络的驱动需要通过哪种buffer缓冲器

A. A.BUFH **[正确]**
B. B.BUFR
C. C.BUFIO
D. D.BUFM

---

### 36. 八输入1位多路选择器74LS151，其选择输入端为多少位
- **类型**: 单选题　**难度**: 简单

八输入1位多路选择器74LS151，其选择输入端为多少位

A. A.8
B. B.2
C. C.3 **[正确]**
D. D.4

---

### 37. 在下列逻辑部件中，不属于组合逻辑器件的是
- **类型**: 单选题　**难度**: 简单

在下列逻辑部件中，不属于组合逻辑器件的是

A. A.计数器 **[正确]**
B. B.编码器
C. C.比较器
D. D.译码器

---

### 38. 若输入变量 A 、 B 只有全为 1 时，输出 F=0 ，则其输入与输出的关系是
- **类型**: 单选题　**难度**: 简单

若输入变量 A 、 B 只有全为 1 时，输出 F=0 ，则其输入与输出的关系是

A. A.异或
B. B.同或
C. C.或非
D. D.与非 **[正确]**

---

### 39. 在下列逻辑电路中，属于组合逻辑电路的是
- **类型**: 单选题　**难度**: 简单

在下列逻辑电路中，属于组合逻辑电路的是

A. A.寄存器
B. B.编码器 **[正确]**
C. C.触发器
D. D.计数器

---

### 40. 四位移位寄存器现态为 1101 ，左移进两个 0 后再右移进一个 1 。其移位寄存器的状态是
- **类型**: 单选题　**难度**: 简单

四位移位寄存器现态为 1101 ，左移进两个 0 后再右移进一个 1 。其移位寄存器的状态是

A. A.0110
B. B.0111
C. C.0100
D. D.1010 **[正确]**

---

### 41. 以下符合逻辑运算法则的是？
- **类型**: 单选题　**难度**: 简单

以下符合逻辑运算法则的是？

A. A. C⋅C=C2
B. B.1+1=10
C. C.0<1
D. D.A+1=1 **[正确]**

---

### 42. 一个十六进制数可以用几位二进制数表示
- **类型**: 单选题　**难度**: 简单

一个十六进制数可以用几位二进制数表示

A. A.1
B. B.2
C. C.4 **[正确]**
D. D.16

---

### 43. 数字电路题A+BC= 选择以下哪一个 ? 
- **类型**: 单选题　**难度**: 简单

数字电路题A+BC= 选择以下哪一个 ? 

A. A.A+B
B. B.A+C
C. C.(A+B)(A+C) **[正确]**
D. D.B+C

---

### 44. 4输入的译码器，其输出端最多为
- **类型**: 单选题　**难度**: 简单

4输入的译码器，其输出端最多为

A. A.4个
B. B.8个
C. C.10个
D. D.16个 **[正确]**

---

### 45. 一个 2 输入的 AND 门的输出是下列哪一个？
- **类型**: 单选题　**难度**: 简单

一个 2 输入的 AND 门的输出是下列哪一个？

A. A.1
B. B.0
C. C.A+B
D. D.A*B **[正确]**

---

### 46. 一个 3 输入的 OR 门的输出是下列哪一个？
- **类型**: 单选题　**难度**: 简单

一个 3 输入的 OR 门的输出是下列哪一个？

A. A.A*B
B. B.A+B+C **[正确]**
C. C.A^B^C
D. D.A+B*C

---

### 47. 一个 NOT 门的功能是什么？
- **类型**: 单选题　**难度**: 简单

一个 NOT 门的功能是什么？

A. A.将输入取反 **[正确]**
B. B.将两个输入进行与运算
C. C.将两个输入进行或运算
D. D. 将输入加一

---

### 48. 在数字电路中，一个 D 触发器的特点正确的是什么？
- **类型**: 单选题　**难度**: 简单

在数字电路中，一个 D 触发器的特点正确的是什么？

A. A.有两个稳定状态
B. B.只有一个输入端
C. C.只能进行与运算
D. D.有时钟输入 **[正确]**

---

### 49. 在一个时序电路中，时钟信号的作用是什么？
- **类型**: 单选题　**难度**: 简单

在一个时序电路中，时钟信号的作用是什么？

A. A.控制输出的状态 **[正确]**
B. B.确定输入的值
C. C.传输数据
D. D.控制电路的供电

---

### 50. 在数字电路中，一个时序逻辑电路的主要特点是什么？
- **类型**: 单选题　**难度**: 简单

在数字电路中，一个时序逻辑电路的主要特点是什么？

A. A.只依赖当前输入
B. B.无需时钟信号
C. C.可以存储大量数据
D. D.输出不受输入顺序影响 **[正确]**

---

### 51. 一个 OR 门的输出是下列哪一个？
- **类型**: 单选题　**难度**: 简单

一个 OR 门的输出是下列哪一个？

A. A.A * B
B. B.A + B **[正确]**
C. C. A ^ B
D. D.A+B(上面一横岗)

---

### 52. 表示任意两位无符号十进制数需要几位二进制数 ? 
- **类型**: 单选题　**难度**: 简单

表示任意两位无符号十进制数需要几位二进制数 ? 

A. A.6
B. B.7 **[正确]**
C. C.8
D. D.9

---

### 53. 当使用 8 位二进制表示有符号整数时，补码能表示的最小整数是：
- **类型**: 单选题　**难度**: 简单

当使用 8 位二进制表示有符号整数时，补码能表示的最小整数是：

A. A.-128 **[正确]**
B. B.-127
C. C.-64
D. D.-63

---

### 54. 反码和补码表示法中，唯一的差别是：
- **类型**: 单选题　**难度**: 简单

反码和补码表示法中，唯一的差别是：

A. A.符号位的处理方式 **[正确]**
B. B.负数的表示方式
C. C.正数的表示方式
D. D.加法运算的规则

---

### 55. 对于二进制数 10010010，如果采用补码表示法，其对应的原码是：
- **类型**: 单选题　**难度**: 简单

对于二进制数 10010010，如果采用补码表示法，其对应的原码是：

A. A.10010010
B. B.01101101 **[正确]**
C. C.11101110
D. D.10010001

---

### 56. Verilog语言是用于描述什么的硬件行为的一种硬件描述语言。
- **类型**: 单选题　**难度**: 简单

Verilog语言是用于描述什么的硬件行为的一种硬件描述语言。

A. A.数字逻辑电路 **[正确]**
B. B.软件算法
C. C.网络协议
D. D.数据库查询语句

---

### 57. 在Verilog中，以下哪种元素用于描述数字逻辑电路的行为？
- **类型**: 单选题　**难度**: 简单

在Verilog中，以下哪种元素用于描述数字逻辑电路的行为？

A. A.模块 **[正确]**
B. B.函数
C. C.结构体
D. D.类

---

### 58. 在Verilog中，描述组合逻辑的语句是？
- **类型**: 单选题　**难度**: 简单

在Verilog中，描述组合逻辑的语句是？

A. A.always @ (posedge clk)
B. B.always @ (negedge clk)
C. C.always @ (*) **[正确]**
D. D.always_comb

---

### 59. 以下哪个关键字用于定义一个Verilog模块？
- **类型**: 单选题　**难度**: 简单

以下哪个关键字用于定义一个Verilog模块？

A. A. module **[正确]**
B. B.function
C. C. task
D. D.class

---

### 60. 在Verilog语言中，以下哪个关键字用于定义输入端口？
- **类型**: 单选题　**难度**: 简单

在Verilog语言中，以下哪个关键字用于定义输入端口？

A. A.input **[正确]**
B. B.output
C. C.wire
D. D.reg

---

### 61. 以下哪个关键字用于定义内部信号连接？
- **类型**: 单选题　**难度**: 简单

以下哪个关键字用于定义内部信号连接？

A. A.end
B. B.finish
C. C.endmodule **[正确]**
D. D.finishmodule

---

### 62. 下列哪个选项用于表示逻辑判断条件？
- **类型**: 单选题　**难度**: 简单

下列哪个选项用于表示逻辑判断条件？

A. A.( ) **[正确]**
B. B.{ }
C. C.[ ]
D. D.< >

---

### 63. 在Verilog中，IF语句的语法结构通常包括哪些部分？
- **类型**: 单选题　**难度**: 简单

在Verilog中，IF语句的语法结构通常包括哪些部分？

A. A.if (condition) { ... }
B. B.if (condition) begin ... end **[正确]**
C. C.if {condition} ... end
D. D.if (condition) ... end

---

### 64. 在Verilog中，IF语句的条件可以包括以下哪种操作符？
- **类型**: 多选题　**难度**: 简单

在Verilog中，IF语句的条件可以包括以下哪种操作符？

A. A.== **[正确]**
B. B.&& **[正确]**
C. C.|| **[正确]**
D. D.! **[正确]**

---

### 65. 在Verilog中，用于逻辑非操作的运算符是？
- **类型**: 单选题　**难度**: 简单

在Verilog中，用于逻辑非操作的运算符是？

A. A.! **[正确]**
B. B.~
C. C.^
D. D.&

---

### 66. 在Verilog中，以下表达式的结果是什么？ reg [2:0] x = 3; reg [2:0] y = 5; reg [2:0] z = x + y;
- **类型**: 单选题　**难度**: 简单

在Verilog中，以下表达式的结果是什么？ reg [2:0] x = 3; reg [2:0] y = 5; reg [2:0] z = x + y;

A. A.6
B. B.8 **[正确]**
C. C.3
D. D.5

---

### 67. 在Verilog中，以下表达式的结果是什么？ reg [3:0] a = 4'b1010; reg [3:0] b = ~a;
- **类型**: 单选题　**难度**: 简单

在Verilog中，以下表达式的结果是什么？ reg [3:0] a = 4'b1010; reg [3:0] b = ~a;

A. A.4'b0101 **[正确]**
B. B.4'b1010
C. C.4'b1111
D. D.4'b0000

---

### 68. 在Verilog中，以下表达式的结果是什么？ reg [3:0] a = 4'b1010; reg [3:0] b = a << 2;
- **类型**: 单选题　**难度**: 简单

在Verilog中，以下表达式的结果是什么？ reg [3:0] a = 4'b1010; reg [3:0] b = a << 2;

A. A.4'b101000 **[正确]**
B. B.4'b010000
C. C.4'b000010
D. D.4'b101000

---

### 69. 在Verilog中，以下表达式的结果是什么？ reg [3:0] a = 4'b1010; reg [3:0] b = 4'b0110; reg [3:0] c = (a & b) | (~a);
- **类型**: 单选题　**难度**: 简单

在Verilog中，以下表达式的结果是什么？ reg [3:0] a = 4'b1010; reg [3:0] b = 4'b0110; reg [3:0] c = (a & b) | (~a);

A. A.4'b0101
B. B.4'b0111 **[正确]**
C. C.4'b0111
D. D.4'b1010

---

### 70. 在Verilog中，以下表达式的结果是什么？ reg [3:0] x = 4'b1010; reg [3:0] y = 4'b0110; reg [3:0] z = (x & y) ^ (~x);
- **类型**: 单选题　**难度**: 简单

在Verilog中，以下表达式的结果是什么？ reg [3:0] x = 4'b1010; reg [3:0] y = 4'b0110; reg [3:0] z = (x & y) ^ (~x);

A. A.4'b0101
B. B.4'b1010
C. C.4'b1100
D. D.4'b0111 **[正确]**

---

### 71. 在Verilog中，以下case语句的默认分支应该使用什么关键字？
- **类型**: 单选题　**难度**: 简单

在Verilog中，以下case语句的默认分支应该使用什么关键字？

A. A. default **[正确]**
B. B.else
C. C.otherwise
D. D.endcase

---

### 72. 在Verilog中，以下case语句的结果是什么？ reg [2:0] sel = 3; reg [3:0] out;  case (sel)   3: out = 4'b1010;   2: out = 4'b0101;   1: out = 4'b1111;   default: out = 4'b0000; endcase
- **类型**: 单选题　**难度**: 简单

在Verilog中，以下case语句的结果是什么？ reg [2:0] sel = 3; reg [3:0] out;  case (sel)   3: out = 4'b1010;   2: out = 4'b0101;   1: out = 4'b1111;   default: out = 4'b0000; endcase

A. A.4'b0000
B. B.4'b0101
C. C.4'b1111
D. D.4'b1010 **[正确]**

---

### 73. Moore状态机的特点是什么？
- **类型**: 单选题　**难度**: 简单

Moore状态机的特点是什么？

A. A.状态由输出决定 **[正确]**
B. B.状态由输入决定
C. C.状态由时钟决定
D. D.状态由时序逻辑决定

---

### 74. Moore状态机的状态转移和输出通常在Verilog中如何描述？
- **类型**: 单选题　**难度**: 简单

Moore状态机的状态转移和输出通常在Verilog中如何描述？

A. A.在module声明中
B. B.使用不同的always块
C. C.在同一个always块中 **[正确]**
D. D.在initial块中

---

### 75. Moore状态机中的输出取决于哪些因素？
- **类型**: 单选题　**难度**: 简单

Moore状态机中的输出取决于哪些因素？

A. A. 输出信号
B. B.输入信号
C. C.时钟边沿
D. D.当前状态 **[正确]**

---

### 76. 在Verilog中实现摩尔状态机时，状态转移逻辑通常使用哪种语句描述？
- **类型**: 单选题　**难度**: 简单

在Verilog中实现摩尔状态机时，状态转移逻辑通常使用哪种语句描述？

A. A.if-else语句
B. B.case语句 **[正确]**
C. C.always_comb块
D. D.fork-join语句

---

### 77. 摩尔状态机在Verilog中的设计目标是什么？
- **类型**: 单选题　**难度**: 简单

摩尔状态机在Verilog中的设计目标是什么？

A. A.高速运行
B. B.低功耗 **[正确]**
C. C.清晰的状态转移逻辑
D. D.输出与状态同步

---

### 78. Mealy状态机的特点是什么？
- **类型**: 单选题　**难度**: 简单

Mealy状态机的特点是什么？

A. A.状态转移只依赖于输入，输出只依赖于当前状态
B. B.状态转移和输出同时依赖于输入和当前状态 **[正确]**
C. C.状态转移和输出同时依赖于输入
D. D.状态转移和输出都独立于输入和当前状态

---

### 79. 在Verilog中实现Mealy状态机时，输出通常由什么决定？
- **类型**: 单选题　**难度**: 简单

在Verilog中实现Mealy状态机时，输出通常由什么决定？

A. A.输入信号 **[正确]**
B. B.当前状态
C. C.时钟信号
D. D.输出信号

---

### 80. 在Verilog中，描述Mealy状态机的输出逻辑时，通常使用什么结构？
- **类型**: 单选题　**难度**: 简单

在Verilog中，描述Mealy状态机的输出逻辑时，通常使用什么结构？

A. A. always_comb块和case语句
B. B.always @(posedge clk)块和case语句
C. C. case语句 **[正确]**
D. D.initial块和if-else语句

---

### 81. 在Verilog仿真中，通常使用哪个关键字来声明一个模块？
- **类型**: 单选题　**难度**: 简单

在Verilog仿真中，通常使用哪个关键字来声明一个模块？

A. A.module **[正确]**
B. B.design
C. C. simulation
D. D.component

---

### 82. Verilog仿真中的testbench通常用来做什么？
- **类型**: 单选题　**难度**: 简单

Verilog仿真中的testbench通常用来做什么？

A. A.实现主要逻辑
B. B.生成输入向量 **[正确]**
C. C.设置时钟频率
D. D.输出设计规范

---

### 83. 在Verilog仿真中，一般如何初始化模块的输入端口？
- **类型**: 单选题　**难度**: 简单

在Verilog仿真中，一般如何初始化模块的输入端口？

A. A.使用output声明
B. B.使用always @(posedge clk)
C. C.使用wire声明
D. D.使用initial块 **[正确]**

---

### 84. 已知 ，其原码 原=10010001，其补码为
- **类型**: 单选题　**难度**: 简单

已知 ，其原码 原=10010001，其补码为

A. A. 10010001
B. B.11101110
C. C..01100110
D. D.11101111 **[正确]**

---

### 85. 将十进制数 45 转换为二进制，结果是？
- **类型**: 单选题　**难度**: 简单

将十进制数 45 转换为二进制，结果是？

A. A.101101 **[正确]**
B. B.101010
C. C.110011
D. D.111001

---

### 86. 将十六进制数 A3F 转换为二进制，结果是？
- **类型**: 单选题　**难度**: 简单

将十六进制数 A3F 转换为二进制，结果是？

A. A.1010 0011 1111 **[正确]**
B. B.1010 1001 1111
C. C.1010 0111 1111
D. D.1010 0010 1111

---

### 87. 将二进制数 110110 转换为十六进制，结果是？
- **类型**: 单选题　**难度**: 简单

将二进制数 110110 转换为十六进制，结果是？

A. A.B6
B. B.36 **[正确]**
C. C.D6
D. D.1B

---

### 88. 将二进制数 1101 转换为十进制，结果是？
- **类型**: 单选题　**难度**: 简单

将二进制数 1101 转换为十进制，结果是？

A. A.12
B. B.13 **[正确]**
C. C.14
D. D.15

---

### 89. 以下哪种编码器能够将16个输入编码为4位二进制码？
- **类型**: 单选题　**难度**: 简单

以下哪种编码器能够将16个输入编码为4位二进制码？

A. A.4-2编码器
B. B.16-4编码器 **[正确]**
C. C.8-3编码器
D. D.3-8编码器

---

### 90. 在数字逻辑中，编码器的作用是什么？
- **类型**: 单选题　**难度**: 简单

在数字逻辑中，编码器的作用是什么？

A. A.将高频信号转换为低频信号
B. B.将数字信号编码为模拟信号
C. C.将多个输入信号编码为较少的输出信号 **[正确]**
D. D.将模拟信号转换为数字信号

---

### 91. 译码器的主要作用是？
- **类型**: 单选题　**难度**: 简单

译码器的主要作用是？

A. A.将数字信号转换为模拟信号
B. B.将高频信号转换为低频信号
C. C.将较少的输入信号转换为多个输出信号 **[正确]**
D. D.将模拟信号转换为数字信号

---

### 92. 在Verilog中，如何定义一个8位的十六进制数
- **类型**: 单选题　**难度**: 简单

在Verilog中，如何定义一个8位的十六进制数

A. A.reg [7:0] hex_num; **[正确]**
B. B.reg [8:0] hex_num;
C. C.reg [15:0] hex_num;
D. D.reg [3:0] hex_num;

---

### 93. 在Verilog中，如何定义一个4位的二进制数？
- **类型**: 单选题　**难度**: 简单

在Verilog中，如何定义一个4位的二进制数？

A. A.reg [4:0] binary_num;
B. B.reg [3:0] binary_num; **[正确]**
C. C.reg [3:1] binary_num;
D. D.reg [4:1] binary_num

---

### 94. 在Verilog中，如何定义一个包含值 0xA 的寄存器？
- **类型**: 单选题　**难度**: 简单

在Verilog中，如何定义一个包含值 0xA 的寄存器？

A. A.reg [3:0] my_reg = 4'b1010; **[正确]**
B. B.reg [3:0] my_reg = 4'b1011;
C. C.reg [3:0] my_reg = 4'b1100;
D. D.reg [3:0] my_reg = 4'b1101;

---

### 95. 如何将十六进制数 0x1C 转换为二进制数？
- **类型**: 单选题　**难度**: 简单

如何将十六进制数 0x1C 转换为二进制数？

A. A.10010
B. B.10111
C. C.11000
D. D.11100 **[正确]**

---

### 96. 将十六进制数 0x1A 转换为十进制数：
- **类型**: 单选题　**难度**: 简单

将十六进制数 0x1A 转换为十进制数：

A. A.16
B. B.26 **[正确]**
C. C.32
D. D.20

---

### 97. 将十进制数 255 转换为十六进制数：
- **类型**: 单选题　**难度**: 简单

将十进制数 255 转换为十六进制数：

A. A.0xFF **[正确]**
B. B.0xEF
C. C.0xF0
D. D.0xAA

---

### 98. 将十进制数 100 转换为十六进制数：
- **类型**: 单选题　**难度**: 简单

将十进制数 100 转换为十六进制数：

A. A.0x64 **[正确]**
B. B.0x68
C. C.0x70
D. D.0x6A

---

### 99. 在Verilog中，如何定义一个 8 位加法器的两个输入？
- **类型**: 单选题　**难度**: 简单

在Verilog中，如何定义一个 8 位加法器的两个输入？

A. A.wire [7:0] a, b;
B. B.reg [7:0] a, b;
C. C.input [7:0] a, b; **[正确]**
D. D.output [7:0] a, b;

---

### 100. 以下哪个Verilog assign语句实现了将输入信号 a 的反相赋值给输出信号 y？
- **类型**: 单选题　**难度**: 简单

以下哪个Verilog assign语句实现了将输入信号 a 的反相赋值给输出信号 y？

A. A.assign y = a & ~a;
B. B.assign y = ~a; **[正确]**
C. C.assign y = a | ~a;
D. D.assign y = a ^ 1'b1;

---

### 101. 以下哪个Verilog assign语句实现了将输入信号 a 和 b 的逻辑与非结果赋值给输出信号 y？
- **类型**: 单选题　**难度**: 简单

以下哪个Verilog assign语句实现了将输入信号 a 和 b 的逻辑与非结果赋值给输出信号 y？

A. A.assign y = a & b;
B. B.assign y = ~(a & b); **[正确]**
C. C..assign y = a | b;
D. D.assign y = ~(a | b);

---

### 102. 在 Verilog 中，以下哪个描述最准确地定义了 posedge？
- **类型**: 单选题　**难度**: 简单

在 Verilog 中，以下哪个描述最准确地定义了 posedge？

A. A.当时钟信号从低电平到高电平时执行操作。 **[正确]**
B. B.当时钟信号从高电平到低电平时执行操作。
C. C.当时钟信号保持高电平时执行操作。
D. D.当时钟信号保持低电平时执行操作。

---

### 103. 在 Verilog 的 always 块中，何时使用 @(posedge clk)？
- **类型**: 单选题　**难度**: 简单

在 Verilog 的 always 块中，何时使用 @(posedge clk)？

A. A.当需要在时钟信号的上升沿执行操作时。 **[正确]**
B. B.当需要在时钟信号的下降沿执行操作时。
C. C.当需要在时钟信号的任意边沿执行操作时。
D. D.当不需要时钟信号来触发操作时。

---

### 104. 下列哪种逻辑运算的真值表中，所有输入相同时，输出为真？
- **类型**: 单选题　**难度**: 简单

下列哪种逻辑运算的真值表中，所有输入相同时，输出为真？

A. A.与运算 **[正确]**
B. B.或运算
C. C.非运算
D. D.异或运算

---

### 105. 下列哪种逻辑运算的真值表中，只有所有输入都相同时，输出为假？
- **类型**: 单选题　**难度**: 简单

下列哪种逻辑运算的真值表中，只有所有输入都相同时，输出为假？

A. A.与运算
B. B.或运算
C. C.非运算
D. D.异或运算 **[正确]**

---

### 106. Artix-7系列器件的主要市场定位是？
- **类型**: 单选题　**难度**: 简单

Artix-7系列器件的主要市场定位是？

A. A.高端应用
B. B.低成本应用 **[正确]**
C. C.高性能计算
D. D.专用加速器

---

### 107. Artix-7系列器件中，用于存储配置信息的主要资源是？
- **类型**: 单选题　**难度**: 简单

Artix-7系列器件中，用于存储配置信息的主要资源是？

A. A.BRAM（块RAM） **[正确]**
B. B.DSP（数字信号处理器）
C. C.PLL（锁相环）
D. D.IOB（输入/输出块

---

### 108. Artix-7系列器件中，用于提供时钟管理和分频功能的资源是？
- **类型**: 单选题　**难度**: 简单

Artix-7系列器件中，用于提供时钟管理和分频功能的资源是？

A. A.BRAM（块RAM）
B. B.DSP（数字信号处理器）
C. C.PLL（锁相环） **[正确]**
D. D.IOB（输入/输出块）

---

### 109. 在Artix-7系列器件中，IOB（输入/输出块）的主要功能是什么？
- **类型**: 单选题　**难度**: 简单

在Artix-7系列器件中，IOB（输入/输出块）的主要功能是什么？

A. A.实现逻辑功能
B. B.存储配置信息
C. C.提供时钟管理
D. D.处理输入输出信号 **[正确]**

---

### 110. Artix-7系列器件中的CLB（配置逻辑块）包含了哪些主要资源？
- **类型**: 单选题　**难度**: 简单

Artix-7系列器件中的CLB（配置逻辑块）包含了哪些主要资源？

A. A.LUT（查找表）和触发器 **[正确]**
B. B.BRAM（块RAM）和DSP（数字信号处理器）
C. C.PLL（锁相环）和IOB（输入/输出块）
D. D.时钟管理和分频器

---

### 111. 在Artix-7系列器件中，用于实现时序逻辑和状态机的主要资源是？
- **类型**: 单选题　**难度**: 简单

在Artix-7系列器件中，用于实现时序逻辑和状态机的主要资源是？

A. A.LUT（查找表）
B. B.BRAM（块RAM）
C. C.DSP（数字信号处理器）
D. D.触发器 **[正确]**

---

### 112. Artix-7系列器件中的BRAM（块RAM）主要用途是？
- **类型**: 单选题　**难度**: 简单

Artix-7系列器件中的BRAM（块RAM）主要用途是？

A. A.存储配置信息
B. B.实现逻辑运算
C. C.提供时钟管理
D. D.存储数据 **[正确]**

---

### 113. 在Verilog中，用于描述Xilinx Artix-7系列器件中的逻辑功能和时序行为的关键语句是？
- **类型**: 单选题　**难度**: 简单

在Verilog中，用于描述Xilinx Artix-7系列器件中的逻辑功能和时序行为的关键语句是？

A. A.always @* **[正确]**
B. B.module
C. C.initial
D. D.wire

---

### 114. 在Verilog模块中，用于声明Xilinx Artix-7系列器件中的输入和输出端口的关键字是？
- **类型**: 单选题　**难度**: 简单

在Verilog模块中，用于声明Xilinx Artix-7系列器件中的输入和输出端口的关键字是？

A. A.reg
B. B.input/output **[正确]**
C. C.wire
D. D.module

---

### 115. 在Verilog中，用于定义Xilinx FPGA 7系列器件中寄存器的关键语句是？
- **类型**: 单选题　**难度**: 简单

在Verilog中，用于定义Xilinx FPGA 7系列器件中寄存器的关键语句是？

A. A. wire
B. B.reg **[正确]**
C. C.input
D. D.output

---

### 116. 在Vivado中，哪个报告可以显示FPGA器件中逻辑资源（如LUT和触发器）的利用情况？
- **类型**: 单选题　**难度**: 简单

在Vivado中，哪个报告可以显示FPGA器件中逻辑资源（如LUT和触发器）的利用情况？

A. A.时序分析报告
B. B.逻辑综合报告
C. C.资源利用率报告 **[正确]**
D. D.约束分析报告

---

### 117. 下列哪种逻辑运算的真值表中，只有所有输入都为假时，输出为真？
- **类型**: 单选题　**难度**: 简单

下列哪种逻辑运算的真值表中，只有所有输入都为假时，输出为真？

A. A.与运算
B. B.或运算
C. C.非运算 **[正确]**
D. D.异或运算

---

## 二、判断题 (1 道)

### 118. FPGA芯片在出厂时就具有固定的逻辑功能，用户无法更改
- **类型**: 判断题　**难度**: 简单

FPGA芯片在出厂时就具有固定的逻辑功能，用户无法更改

**答案**: 错误

---

## 三、编程题 (208 道)

### 119. 或门
- **类型**: 编程题　**难度**: 简单

**参考答案**:

```verilog
module top_module(
    input in0,in1,
    output out
);

    assign out = in0 | in1;

endmodule
```

---

### 120. 半加器
- **类型**: 编程题　**难度**: 简单

**参考答案**:

```verilog
module top_module(
      input     x   ,
      input     y   ,
      output    sum ,
      output    c_out);

    assign sum = x ^ y;
    assign c_out = x & y;

endmodule
```

---

### 121. 4位二进制的BCD码转换器
- **类型**: 编程题　**难度**: 简单

**参考答案**:

```verilog
module top_module( 
    input   wire    [3:0]   binary,
    output  wire    [3:0]   bcd 
);

    always @(*) begin
        if (binary <= 4'd9) bcd = binary;
        else bcd = binary + 4'd6;
    end

endmodule
```

---

### 122. 偶数分频器
- **类型**: 编程题　**难度**: 简单

**参考答案**:

```verilog
module top_module(
    input       clk     ,
    input       rst     , 
    output  reg clk_out  
);

    reg [0:0] cnt;
    always @(posedge clk) begin
        if (rst) begin cnt <= 0; clk_out <= 0; end
        else begin
            cnt <= cnt + 1;
            if (cnt == 1'b0) clk_out <= ~clk_out;
        end
    end

endmodule
```

---

### 123. 一输入一输出
- **类型**: 编程题　**难度**: 简单

**参考答案**:

```verilog
module top_module(
    input   in,
    output  out
);

    assign out = in;

endmodule
```

---

### 124. 三输入四输出
- **类型**: 编程题　**难度**: 简单

**参考答案**:

```verilog
module top_module(
    input   in1,in2,in3,
    output  out1,out2,out3,
    output  out
);

    assign out1 = in1 & in2;
    assign out2 = in1 | in2;
    assign out3 = in1 ^ in2;
    assign out  = in1 & in2 & in3;

endmodule
```

---

### 125. 非门
- **类型**: 编程题　**难度**: 简单

**参考答案**:

```verilog
module top_module(
    input in,
    output out
);

    assign out = ~in;

endmodule
```

---

### 126. 四位非门
- **类型**: 编程题　**难度**: 简单

**参考答案**:

```verilog
module top_module(
    input   wire    [3:0]   in,
    output  reg     [3:0]   out
 );

    assign out = ~in;

endmodule
```

---

### 127. 与门
- **类型**: 编程题　**难度**: 简单

**参考答案**:

```verilog
module top_module(
    input   in1,
    input   in0,
    output  out
);

    assign out = in1 & in0;

endmodule
```

---

### 128. 与非门
- **类型**: 编程题　**难度**: 简单

**参考答案**:

```verilog
module top_module(
    input   in0 ,
    input   in1  ,
    output  out
);

    assign out = in0 ~& in1;

endmodule
```

---

### 129. 或非门
- **类型**: 编程题　**难度**: 简单

**参考答案**:

```verilog
module top_module(
    input   in0,
    input   in1,
    output  out
);

    assign out = in0 ~| in1;

endmodule
```

---

### 130. 异或门
- **类型**: 编程题　**难度**: 简单

**参考答案**:

```verilog
module top_module(
    input   in0,
    input   in1,
    output  out
);

    assign out = in0 ^ in1;

endmodule
```

---

### 131. 同或门
- **类型**: 编程题　**难度**: 简单

**参考答案**:

```verilog
module top_module(
    input   in0,
    input   in1,
    output  out
);

    assign out = in0 ~^ in1;

endmodule
```

---

### 132. 三人表决器
- **类型**: 编程题　**难度**: 简单

**参考答案**:

```verilog
module top_module(
    input       a,
    input       b,
    input       c,
    output  reg f
 );

    always @(*) f = (a & b) | (a & c) | (b & c);

endmodule
```

---

### 133. 带权重四人表决器
- **类型**: 编程题　**难度**: 简单

**参考答案**:

```verilog
module top_module(
    input   a,
    input   b,
    input   c,
    input   d,
    output  f
);

    assign f = (a & b) | (a & c) | (b & c) | (a & d);

endmodule
```

---

### 134. 2选1多路选择器
- **类型**: 编程题　**难度**: 简单

**参考答案**:

```verilog
module top_module(
    input   d0,
    input   d1,     //2个输入信号
    input   s ,     //控制信号
    output  y      //输出信号
);

    assign y = s ? d1 : d0;

endmodule
```

---

### 135. 4选1多路选择器
- **类型**: 编程题　**难度**: 简单

**参考答案**:

```verilog
module top_module(
        input   d0,		
        input   d1,     
	input   d2,
	input   d3,
        input   s0,     
	input   s1,
       output  y      
);

    assign y = s1 ? (s0 ? d3 : d2) : (s0 ? d1 : d0);

endmodule
```

---

### 136. 四位2选1多路选择器
- **类型**: 编程题　**难度**: 简单

**参考答案**:

```verilog
module top_module(
    input   [3:0]   d0,
    input   [3:0]   d1,     //2个输入信号
    input           s ,     //控制信号
    output  [3:0]   y      //输出信号
);

    assign y = s ? d1 : d0;

endmodule
```

---

### 137. 四位数值比较器
- **类型**: 编程题　**难度**: 简单

**参考答案**:

```verilog
module top_module ( 
    input   [3:0]   a ,
    input   [3:0]   b ,
    output  [2:0]   out 
 );

    always @(*) begin
        if (a > b) out = 3'b100;
        else if (a == b) out = 3'b010;
        else out = 3'b001;
    end

endmodule
```

---

### 138. 4bit格雷码计数
- **类型**: 编程题　**难度**: 简单

**参考答案**:

```verilog
module top_module(
    input               clk,
    input               rst,
    output  [3:0]   cnt
);

    reg [3:0] bin_cnt;
    always @(posedge clk) begin
        if (rst) bin_cnt <= 4'd0;
        else bin_cnt <= bin_cnt + 1'b1;
    end
    always @(*) cnt = bin_cnt ^ (bin_cnt >> 1);

endmodule
```

---

### 139. 3—8译码器
- **类型**: 编程题　**难度**: 简单

**参考答案**:

```verilog
module top_module(
    input   wire    [2:0]   in,
    output  wire    [7:0]   out
    );

    assign out = 1'b1 << in;

endmodule
```

---

### 140. 七段数码管显示译码器
- **类型**: 编程题　**难度**: 简单

**参考答案**:

```verilog
module top_module(
    input   wire    [3:0]   num,    
    output  wire            an ,    
    output  reg     [6:0]   a_g      
    );

    always @(*) begin
        case (num)
            4'd0: a_g = 7'b0111111;
            4'd1: a_g = 7'b0000110;
            4'd2: a_g = 7'b1011011;
            4'd3: a_g = 7'b1001111;
            4'd4: a_g = 7'b1100110;
            4'd5: a_g = 7'b1101101;
            4'd6: a_g = 7'b1111101;
            4'd7: a_g = 7'b0000111;
            4'd8: a_g = 7'b1111111;
            4'd9: a_g = 7'b1101111;
            default: a_g = 7'b0000000;
        endcase
    end

endmodule
```

---

### 141. 8—3线编码器
- **类型**: 编程题　**难度**: 简单

**参考答案**:

```verilog
module top_module(
    input   wire    [7:0]   in ,
    output  wire    [2:0]   out,
    output  wire            valid
);

    always @(*) begin
        valid = 1'b1;
        case (in)
            8'b00000001: out = 3'd0;
            8'b00000010: out = 3'd1;
            8'b00000100: out = 3'd2;
            8'b00001000: out = 3'd3;
            8'b00010000: out = 3'd4;
            8'b00100000: out = 3'd5;
            8'b01000000: out = 3'd6;
            8'b10000000: out = 3'd7;
            default: begin out = 3'd0; valid = 1'b0; end
        endcase
    end

endmodule
```

---

### 142. 8—3线优先编码器
- **类型**: 编程题　**难度**: 简单

**参考答案**:

```verilog
module top_module(
    input   wire    [7:0]   in ,
    output  reg     [2:0]   out,
    output  reg             valid
    );

    always @(*) begin
        valid = 1'b1;
        casex (in)
            8'b1xxxxxxx: out = 3'd7;
            8'b01xxxxxx: out = 3'd6;
            8'b001xxxxx: out = 3'd5;
            8'b0001xxxx: out = 3'd4;
            8'b00001xxx: out = 3'd3;
            8'b000001xx: out = 3'd2;
            8'b0000001x: out = 3'd1;
            8'b00000001: out = 3'd0;
            default: begin out = 3'd0; valid = 1'b0; end
        endcase
    end

endmodule
```

---

### 143. 四位二进制转格雷码转换器
- **类型**: 编程题　**难度**: 简单

**参考答案**:

```verilog
module top_module(
    input           [3:0]   binary,
    output  wire    [3:0]   gray
);

    assign gray = binary ^ (binary >> 1);

endmodule
```

---

### 144. 四位格雷码转二进制转换器
- **类型**: 编程题　**难度**: 简单

**参考答案**:

```verilog
module  top_module (
    input   wire    [3: 0]   gray,
    output  reg     [3: 0]   binary
);

    always @(*) begin
        binary[3] = gray[3];
        binary[2] = gray[3] ^ gray[2];
        binary[1] = gray[3] ^ gray[2] ^ gray[1];
        binary[0] = gray[3] ^ gray[2] ^ gray[1] ^ gray[0];
    end

endmodule
```

---

### 145. 四位二进制转独热码转换器
- **类型**: 编程题　**难度**: 简单

**参考答案**:

```verilog
module top_module(
    input       [3:0]    binary,
    output reg  [15:0]  onehot
);

    always @(*) begin
        onehot = 16'b0;
        onehot[binary] = 1'b1;
    end

endmodule
```

---

### 146. BCD码七段数码管显示译码器
- **类型**: 编程题　**难度**: 简单

**参考答案**:

```verilog
module top_module(
    input   wire    [3:0]   in,
    output  reg     [6:0]   out//
 );

    always @(*) begin
        case (in)
            4'd0: out = 7'b0111111;
            4'd1: out = 7'b0000110;
            4'd2: out = 7'b1011011;
            4'd3: out = 7'b1001111;
            4'd4: out = 7'b1100110;
            4'd5: out = 7'b1101101;
            4'd6: out = 7'b1111101;
            4'd7: out = 7'b0000111;
            4'd8: out = 7'b1111111;
            4'd9: out = 7'b1101111;
            default: out = 7'b0000000;
        endcase
    end

endmodule
```

---

### 147. 位统计器
- **类型**: 编程题　**难度**: 简单

**参考答案**:

```verilog
module top_module(
    input   [7:0]   data_in,
    output  [3:0]   cnt_out
);

    always @(*) begin
        cnt_out = data_in[0]+data_in[1]+data_in[2]+data_in[3]+
                  data_in[4]+data_in[5]+data_in[6]+data_in[7];
    end

endmodule
```

---

### 148. 四位全加器
- **类型**: 编程题　**难度**: 简单

**参考答案**:

```verilog
module top_module(
    input       [3:0]   a   ,
    input       [3:0]   b   ,
    output  reg [3:0]   sum ,
    output  reg         cout,
    input               cin
    );

    always @(*) {cout, sum} = a + b + cin;

endmodule
```

---

### 149. 半减器
- **类型**: 编程题　**难度**: 简单

**参考答案**:

```verilog
module top_module(
    input   wire    min ,
    input   wire    sub ,

    output  wire    di  ,
    output  wire    bo  
    );

    assign di = min ^ sub;
    assign bo = ~min & sub;

endmodule
```

---

### 150. 四位全减器
- **类型**: 编程题　**难度**: 简单

**参考答案**:

```verilog
module top_module(
    input       [3:0]   a   ,
    input       [3:0]   b   ,
    output  reg [3:0]   sum ,
    output  reg         cout,
    input               cin
);

    always @(*) {cout, sum} = a - b - cin;

endmodule
```

---

### 151. 无符号乘法器
- **类型**: 编程题　**难度**: 简单

**参考答案**:

```verilog
module top_module (
    input   [3:0]   a,
    input   [3:0]   b,
    output  [7:0]   prod
);

    assign prod = a * b;

endmodule
```

---

### 152. 有符号乘法器
- **类型**: 编程题　**难度**: 简单

**参考答案**:

```verilog
module top_module (
    input   signed  [3:0]   a,
    input   signed  [3:0]   b,
    output  signed  [7:0]   prod
);

    assign prod = a * b;

endmodule
```

---

### 153. 单字节带溢出位加法器
- **类型**: 编程题　**难度**: 简单

**参考答案**:

```verilog
module top_module(
    input       [7:0]   a   ,
    input       [7:0]   b   ,
    output  reg [7:0]   sum ,
    output  reg         cout
    );

    always @(*) {cout, sum} = a + b;

endmodule
```

---

### 154. 自动贩卖机
- **类型**: 编程题　**难度**: 中等

**参考答案**:

```verilog
module top_module(
    input           clk     ,
    input           rst     ,
    input   [2:0]   i_rmb   ,
    output  reg [2:0]   o_rmb   ,
    output   reg        o_valid 
    );

    // 自动贩卖机 - 请根据题目描述完善时序逻辑

endmodule
```

---

### 155. D触发器
- **类型**: 编程题　**难度**: 简单

**参考答案**:

```verilog
module top_module(
                 input          clk ,
                 input          d   ,
                 output reg     q
                 );

    always @(posedge clk) q <= d;

endmodule
```

---

### 156. 8位D触发器
- **类型**: 编程题　**难度**: 简单

**参考答案**:

```verilog
module top_module(
    input               clk ,
    input       [7:0]   d   ,
    output  reg [7:0]   q
);

    always @(posedge clk) q <= d;

endmodule
```

---

### 157. 8位D触发器带同步上升沿复位
- **类型**: 编程题　**难度**: 简单

**参考答案**:

```verilog
module top_module(
    input               clk ,
    input               rst ,
    input       [7:0]   d   ,  
    output  reg [7:0]   q
);

    always @(posedge clk) begin
        if (rst) q <= 8'b0;
        else q <= d;
    end

endmodule
```

---

### 158. 8位D触发器带同步下降沿复位
- **类型**: 编程题　**难度**: 简单

**参考答案**:

```verilog
module top_module(
    input               clk ,
    input               rst ,
    input       [7:0]   d   ,
    output  reg [7:0]   q
);

    always @(posedge clk) begin
        if (rst) q <= 8'b0;
        else q <= d;
    end

endmodule
```

---

### 159. 8位D触发器带异步复位
- **类型**: 编程题　**难度**: 简单

**参考答案**:

```verilog
module top_module(
    input               clk ,
    input               rst ,
    input       [7:0]   d   ,
    output  reg [7:0]   q
);

    always @(posedge clk or posedge rst) begin
        if (rst) q <= 8'b0;
        else q <= d;
    end

endmodule
```

---

### 160. 带写使能位8位D触发器
- **类型**: 编程题　**难度**: 简单

**参考答案**:

```verilog
module top_module(
    input               clk ,
    input               rst ,
    input               en  ,
    input       [7:0]   d   ,
    output  reg [7:0]   q
);

    always @(posedge clk) q <= d;

endmodule
```

---

### 161. 4位二进制计数器
- **类型**: 编程题　**难度**: 简单

**参考答案**:

```verilog
module top_module(
    input               clk,
    input               rst,
    output  reg [3:0]   cnt
);

    always @(posedge clk) begin
        if (rst) cnt <= 4'b0;
        else cnt <= cnt + 1'b1;
    end

endmodule
```

---

### 162. 10进制计数器
- **类型**: 编程题　**难度**: 简单

**参考答案**:

```verilog
module top_module(
    input               clk,
    input               rst,
    output  reg [3:0]   cnt
);

    always @(posedge clk) begin
        if (rst) cnt <= 4'd0;
        else if (cnt == 4'd9) cnt <= 4'd0;
        else cnt <= cnt + 1'b1;
    end

endmodule
```

---

### 163. 10k计数显示器
- **类型**: 编程题　**难度**: 简单

**参考答案**:

```verilog
module top_module(
    input               clk     ,
    input               rst     ,
    output  reg [3:0]   cnt_ge  ,
    output  reg [3:0]   cnt_shi ,
    output  reg [3:0]   cnt_bai ,
    output  reg [3:0]   cnt_qian
);

    reg [13:0] cnt;
    always @(posedge clk) begin
        if (rst) cnt <= 0;
        else if (cnt == 9999) cnt <= 0;
        else cnt <= cnt + 1;
    end

endmodule
```

---

### 164. 时钟显示器
- **类型**: 编程题　**难度**: 简单

**参考答案**:

```verilog
module top_module(
    input               clk     ,
    input               rst     ,
    output  reg [4:0]   cnt_shi ,
    output  reg [5:0]   cnt_fen ,
    output  reg [5:0]   cnt_miao
);

    reg [5:0] sec, min;
    reg [4:0] hour;
    always @(posedge clk) begin
        if (rst) begin sec <= 0; min <= 0; hour <= 0; end
        else begin
            if (sec == 59) begin
                sec <= 0;
                if (min == 59) begin min <= 0; hour <= hour + 1; end
                else min <= min + 1;
            end else sec <= sec + 1;
        end
    end
    assign sec_ones = sec % 10;
    assign sec_tens = sec / 10;
    assign min_ones = min % 10;
    assign min_tens = min / 10;
    assign hour_ones = hour % 10;
    assign hour_tens = hour / 10;

endmodule
```

---

### 165. 4位移位寄存器
- **类型**: 编程题　**难度**: 简单

**参考答案**:

```verilog
module top_module(
    input               clk ,
    input               rst ,
    input       [1:0]   ena ,
    input       [3:0]   d   ,
    output  reg [3:0]   q
  );

    always @(posedge clk) begin
        if (rst) q <= 4'b0;
        else q <= {q[2:0], d};
    end

endmodule
```

---

### 166. 桶形移位器
- **类型**: 编程题　**难度**: 简单

**参考答案**:

```verilog
module top_module(
 input                 clk         ,
  input                rst         ,
  input     [2:0]    ena         ,
  input     [2:0]    rotate_num  ,
  input     [7:0]       d           ,
  output reg[7:0]       q
  );

    // 桶形移位器 - 请根据题目描述完善时序逻辑

endmodule
```

---

### 167. 32位可控制方向移位寄存器
- **类型**: 编程题　**难度**: 简单

**参考答案**:

```verilog
module top_module(
    input               clk ,
    input               rst ,
    input       [1:0]   ena ,
    input       [31:0]  d   ,
    output  reg [31:0]  q
  );

    always @(posedge clk) begin
        if (rst) q <= 32'b0;
        else if (dir) q <= {q[30:0], 1'b0};
        else q <= {1'b0, q[31:1]};
    end

endmodule
```

---

### 168. 3输入LUT
- **类型**: 编程题　**难度**: 简单

**参考答案**:

```verilog
module top_module (
    input       clk     ,             
    input       enable  ,          
    input       s       ,               
    input       a, b, c ,         
    output reg  z 
 );

    // 3输入LUT - 请根据题目描述完善时序逻辑

endmodule
```

---

### 169. 简单状态机
- **类型**: 编程题　**难度**: 中等

**参考答案**:

```verilog
module top_module(
    input               clk ,
    input               x   ,
    output  reg         y   ,
    output  reg [1:0]   states
);

    parameter S0 = 2'b00, S1 = 2'b01, S2 = 2'b10;
    reg [1:0] state, next;
    always @(posedge clk) state <= next;
    always @(*) begin
        next = S0; out = 0;
        case (state)
            S0: next = din ? S1 : S0;
            S1: begin next = din ? S1 : S2; out = 1; end
            S2: next = din ? S1 : S0;
        endcase
    end

endmodule
```

---

### 170. 带异步复位的简单状态机
- **类型**: 编程题　**难度**: 中等

**参考答案**:

```verilog
module top_module(
    input               clk     ,
    input               rst     ,
    input               x       ,
    output  reg         y       ,
    output  reg [1:0]   status
);

    parameter S0 = 2'b00, S1 = 2'b01, S2 = 2'b10;
    reg [1:0] state, next;
    always @(posedge clk or posedge rst) begin
        if (rst) state <= S0; else state <= next;
    end
    always @(*) begin
        next = S0; out = 0;
        case (state)
            S0: next = din ? S1 : S0;
            S1: begin next = din ? S1 : S2; out = 1; end
            S2: next = din ? S1 : S0;
        endcase
    end

endmodule
```

---

### 171. 1011序列检测器
- **类型**: 编程题　**难度**: 简单

**参考答案**:

```verilog
module top_module(
    input	        clk     ,
    input	        rst     ,
    input	        in_data,
    input           in_valid,
    output	out_data    ,
    output	out_valid
);

    parameter S0=0, S1=1, S2=2, S3=3, S4=4;
    reg [2:0] state, next;
    always @(posedge clk) begin
        if (rst) state <= S0; else state <= next;
    end
    always @(*) begin
        next = S0; out = 0;
        case (state)
            S0: next = din ? S1 : S0;
            S1: next = din ? S1 : S2;
            S2: next = din ? S3 : S0;
            S3: next = din ? S4 : S2;
            S4: begin next = din ? S1 : S2; out = 1; end
        endcase
    end

endmodule
```

---

### 172. 流水灯
- **类型**: 编程题　**难度**: 简单

**参考答案**:

```verilog
module top_module(
    input               clk,//10Mhz
    input               rst,//高有效异步复位
    output  [7:0]   led 
);

    reg [31:0] cnt;
    always @(posedge clk) begin
        if (rst) begin cnt <= 0; led <= 8'b00000001; end
        else begin
            if (cnt == 49999999) begin cnt <= 0; led <= {led[6:0], led[7]}; end
            else cnt <= cnt + 1;
        end
    end

endmodule
```

---

### 173. 奇数分频器
- **类型**: 编程题　**难度**: 中等

**参考答案**:

```verilog
module top_module(
    input       clk,
    input       rst,
    output      clk_out
    );

    reg [1:0] cnt_p, cnt_n;
    reg clk_p, clk_n;
    always @(posedge clk) begin
        if (rst) begin cnt_p <= 0; clk_p <= 0; end
        else begin
            if (cnt_p == 2) begin cnt_p <= 0; clk_p <= ~clk_p; end
            else if (cnt_p == 0) clk_p <= ~clk_p;
            else cnt_p <= cnt_p + 1;
        end
    end
    always @(negedge clk) begin
        if (rst) begin cnt_n <= 0; clk_n <= 0; end
        else begin
            if (cnt_n == 2) begin cnt_n <= 0; clk_n <= ~clk_n; end
            else if (cnt_n == 0) clk_n <= ~clk_n;
            else cnt_n <= cnt_n + 1;
        end
    end
    assign clk_out = clk_p | clk_n;

endmodule
```

---

### 174. 键盘消抖器
- **类型**: 编程题　**难度**: 中等

**参考答案**:

```verilog
module top_module(
    input   clk,//10Mhz
    input   key_in,
    output  key_out
);

    reg [19:0] cnt;
    reg key_reg;
    always @(posedge clk) begin
        if (rst) begin cnt <= 0; key_out <= 0; key_reg <= 0; end
        else begin
            if (key_in == key_reg) begin
                if (cnt == 20'd999999) key_out <= key_reg;
                else cnt <= cnt + 1;
            end else begin cnt <= 0; key_reg <= key_in; end
        end
    end

endmodule
```

---

### 175. 十字路口交通信号灯
- **类型**: 编程题　**难度**: 中等

**参考答案**:

```verilog
module top_module(
   input	clk,//10Mhz
   input   rst,
   input   start,
   output	reg m_r,
   output	reg m_g,
   output	reg m_y,
   output	reg s_r,
   output	reg s_g,
   output	reg s_y
);

    // 十字路口交通信号灯 - 请根据题目描述完善时序逻辑

endmodule
```

---

### 176. 八位密码锁
- **类型**: 编程题　**难度**: 中等

**参考答案**:

```verilog
module top_module(
    input	    clk,//100khz,周期10us
    input       rst,
    input	    set,
    input	    k9,k8,k7,k6,k5,k4,k3,k2,k1,k0,
    input	    back,
    output	reg LOCK,
    input	    open,
    input	    close
);

    // 八位密码锁 - 请根据题目描述完善时序逻辑

endmodule
```

---

### 177. 最大公约数算法
- **类型**: 编程题　**难度**: 中等

**参考答案**:

```verilog
module top_module(
    input               clk     ,
    input               rst_n   ,
    input   [7:0]     in1     ,
    input   [7:0]     in2     ,
    input     data_valid,
    output  [7:0]     out_gcd ,
    output   done 
);

    // 最大公约数算法 - 请根据题目描述完善时序逻辑

endmodule
```

---

### 178. 八位整数的平方根
- **类型**: 编程题　**难度**: 中等

**参考答案**:

```verilog
module top_module
(
    input           clk     ,
    input           rst_n   ,
    input   [7:0]   data    ,
    input           data_valid,
    output          done    ,
    output  [4:0]   sqrt    ,
    output  [4:0]   remainder
    );

    // 八位整数的平方根 - 请根据题目描述完善时序逻辑

endmodule
```

---

### 179. 斐波那契数列
- **类型**: 编程题　**难度**: 中等

**参考答案**:

```verilog
module top_module(
                input   clk,
                input   rst,
                output  [15:0]data
                 );

    // 斐波那契数列 - 请根据题目描述完善时序逻辑

endmodule
```

---

### 180. 乒乓操作
- **类型**: 编程题　**难度**: 中等

**参考答案**:

```verilog
module top_module(
    input               clk     ,
    input               rst     ,
    input       [7:0]   data_i  ,
    output  reg [7:0]   data_o  ,
    output  reg [7:0]   buffer1 ,
    output  reg [7:0]   buffer2
);

    // 乒乓操作 - 请根据题目描述完善时序逻辑

endmodule
```

---

### 181. 同步FIFO
- **类型**: 编程题　**难度**: 困难

**参考答案**:

```verilog
module top_module
(
    input    clk,
    input    rst,
    input    wr_en,
    input     [7:0]    din,         
    input       rd_en,
    output reg      valid,
    output reg [7:0]     dout,
    output     empty,
    output   full
    );

    // 同步FIFO - 请根据题目描述完善时序逻辑

endmodule
```

---

### 182. 异步FIFO
- **类型**: 编程题　**难度**: 困难

**参考答案**:

```verilog
module top_module(
input	rst,
input	wclk,
input	[7:0]wdata,
input	w_en,
output	full,
input	rclk,
output	reg [7:0]rdata,
input	r_en,
output	empty
 );

    // 异步FIFO - 请根据题目描述完善时序逻辑

endmodule
```

---

### 183. 定点除法器
- **类型**: 编程题　**难度**: 困难

**参考答案**:

```verilog
module top_module
(
        input   clk,rst,
        input   invalid,
        input   [5:0] divisor,//除数
        input   [5:0] dividend,//被除数
        output  done,
        output  [6:0] quotient,//商
        output  [5:0] remainder//余数
    );

    // 定点除法器 - 请根据题目描述完善时序逻辑

endmodule
```

---

### 184. CRC8串行计算器
- **类型**: 编程题　**难度**: 中等

**参考答案**:

```verilog
module top_module(
    input clk,rst_n,
    input data,
    input data_valid,
    input crc_start,
    output crc_out,
    output crc_valid
    );

    // CRC8串行计算器 - 请根据题目描述完善时序逻辑

endmodule
```

---

### 185. 奇偶校验
- **类型**: 编程题　**难度**: 中等

**参考答案**:

```verilog
module top_module(
    input	clk,
    input	[7:0]data,
    input	invalid,
    output	outvalid,
    output	[8:0]odd,
    output	[8:0]even
);

    assign outvalid = ^clk;

endmodule
```

---

### 186. 整数最大值
- **类型**: 编程题　**难度**: 困难

**参考答案**:

```verilog
module top_module
(
input                   clk,
input                   rst,
input  [255 :0]     din,
input                   din_start,
output reg                  max_valid,
output reg [7:0]         max1,
output reg [7:0]         max2
);

    // 整数最大值 - 请根据题目描述完善时序逻辑

endmodule
```

---

### 187. 整数最小值
- **类型**: 编程题　**难度**: 困难

**参考答案**:

```verilog
module top_module(
    input clk,
    input rst,
    input [31:0] din,
    input din_start,
    output reg min_valid,
    output reg [7:0] min
    );

    // 整数最小值 - 请根据题目描述完善时序逻辑

endmodule
```

---

### 188. 串联转并联
- **类型**: 编程题　**难度**: 简单

**参考答案**:

```verilog
module top_module(
     input clk,
     input rst,
     input d,
     output  valid,
     output [7:0] q
     );

    reg [7:0] shift_reg;
    reg [2:0] cnt;
    always @(posedge clk) begin
        if (rst) begin cnt <= 0; shift_reg <= 0; end
        else begin
            shift_reg[cnt] <= din;
            cnt <= cnt + 1;
        end
    end
    assign dout = shift_reg;

endmodule
```

---

### 189. 并联转串联
- **类型**: 编程题　**难度**: 简单

**参考答案**:

```verilog
module top_module(
input clk,
input rst,
input [7:0]d,
output reg valid,
output reg q
);

    reg [7:0] shift_reg;
    reg [2:0] cnt;
    always @(posedge clk) begin
        if (load) begin shift_reg <= din; cnt <= 0; end
        else begin shift_reg <= {1'b0, shift_reg[7:1]}; cnt <= cnt + 1; end
    end
    assign dout = shift_reg[0];

endmodule
```

---

### 190. 四位不带进位BCD码加法器
- **类型**: 编程题　**难度**: 简单

**参考答案**:

```verilog
module top_module(
input  [3:0] a,
input  [3:0] b,
output [3:0] sum,
output       cout);

    wire [4:0] temp;
    assign temp = a + b + cin;
    always @(*) begin
        if (temp > 5'd9) begin sum = temp - 5'd10; cout = 1'b1; end
        else begin sum = temp[3:0]; cout = 1'b0; end
    end

endmodule
```

---

### 191. 四位带进位BCD码加法器
- **类型**: 编程题　**难度**: 简单

**参考答案**:

```verilog
module top_module(
input  [3:0] a,
input  [3:0] b,
input  cin,
output [3:0] sum,
output cout);

    wire [4:0] temp;
    assign temp = a + b + cin;
    always @(*) begin
        if (temp > 5'd9) begin sum = temp - 5'd10; cout = 1'b1; end
        else begin sum = temp[3:0]; cout = 1'b0; end
    end

endmodule
```

---

### 192. 汉明距离
- **类型**: 编程题　**难度**: 中等

**参考答案**:

```verilog
module top_module(
    input    clk,
    input    rst ,
    input    [7:0]a ,
    input    [7:0]b  ,
    input    we      ,//输入有效
    output reg  valid   ,
    output reg  [7:0]   distance 
    );

    wire [7:0] diff = a ^ b;
    always @(*) begin
        distance = diff[0]+diff[1]+diff[2]+diff[3]+diff[4]+diff[5]+diff[6]+diff[7];
    end

endmodule
```

---

### 193. SPI控制器—主控
- **类型**: 编程题　**难度**: 困难

**参考答案**:

```verilog
module top_module
(
    input           clk,
    input           rst,
    input           wrreq,
    output          wrreqack,
    output          wrfinish,
    input           [7:0]  data_in,
    output          [7:0]  data_out,
    output           data_valid,
    output           busy,
    
    output          sck,
    output          cs,
    output          mosi,
    input           miso
 );

    // SPI控制器—主控 - 请根据题目描述完善时序逻辑

endmodule
```

---

### 194. SPI控制器—从机
- **类型**: 编程题　**难度**: 困难
- **标签**: 接口协议

**参考答案**:

```verilog
module top_module
(
    input            clk,
    input            rst,
    input            s_wrreq,
    input            [7:0]  s_data_in,
    output           s_wrfinish,
    output            [7:0]  s_data_out,
    output            s_data_valid,
    output            s_busy,
    output            s_wrreqack,
    
    input          sck,
    input          cs,
    input          mosi,
    output         miso
 );

    // SPI控制器—从机 - 请根据题目描述完善时序逻辑

endmodule
```

---

### 195. 流水线乘法器
- **类型**: 编程题　**难度**: 简单
- **标签**: 入门基础, 组合逻辑

**参考答案**:

```verilog
module top_module(
input                  clk,
input                  rst,
input         [3:0]    x, 
input         [3:0]    y,
output  reg   [7:0]    z
);

    reg [7:0] prod_reg;
    always @(posedge clk) begin
        if (rst) prod_reg <= 0;
        else prod_reg <= a * b;
    end
    assign prod = prod_reg;

endmodule
```

---

### 196. UART控制器—接收
- **类型**: 编程题　**难度**: 中等
- **标签**: 慢速接口协议, 信号处理, 时序逻辑, 接口协议

**参考答案**:

```verilog
module top_module(
    input  sysclk,
    input  sysrst,
    input  rxd,
    output done,
    output [7:0] rxdata
    );

    // UART控制器—接收 - 请根据题目描述完善时序逻辑

endmodule
```

---

### 197. UART控制器—发送
- **类型**: 编程题　**难度**: 中等
- **标签**: 接口协议, 时序逻辑, 慢速接口协议, 信号处理

**参考答案**:

```verilog
module top_module(
    input  sysclk,
    input  sysrst,
    output txd,
    input  in_valid,
    input  [7:0] txdata
    );

    // UART控制器—发送 - 请根据题目描述完善时序逻辑

endmodule
```

---

### 198. RGBtoYCbCr转换器
- **类型**: 编程题　**难度**: 中等
- **标签**: 信号处理, 时序逻辑

**参考答案**:

```verilog
module top_module(
                 input  clk,
                 input  rst,
                 input  [7:0] r,g,b,
                 output [7:0] y,cr,cb
                 );

    // RGBtoYCbCr转换器 - 请根据题目描述完善时序逻辑

endmodule
```

---

### 199. IIC控制器—发送
- **类型**: 编程题　**难度**: 困难
- **标签**: 接口协议, 信号处理, 时序逻辑, 慢速接口协议, 状态机

**参考答案**:

```verilog
module top_module(
   input   clk,//100Mhz->400KHz
   input   rst,
   input   [7:0]txdata,
   input   i_val,
   inout   SCL,
   inout   SDA
);

    // IIC控制器—发送 - 请根据题目描述完善时序逻辑

endmodule
```

---

### 200. IIC控制器—接收
- **类型**: 编程题　**难度**: 困难
- **标签**: 慢速接口协议, 状态机, 信号处理, 时序逻辑, 接口协议

**参考答案**:

```verilog
module top_module(
    input	clk,
    input	rst,
    output	[7:0]rxdata,
    output	o_val,
    inout	SCL,
    inout	SDA
    );

    // IIC控制器—接收 - 请根据题目描述完善时序逻辑

endmodule
```

---

### 201. 游程编码器
- **类型**: 编程题　**难度**: 中等
- **标签**: 时序逻辑, 信号处理, 编码

**参考答案**:

```verilog
module top_module(
    input	clk,
    input	rst,
    input	[7:0]idata,
    input	ival,
    output	[7:0]odata,
    output	oval,
    output  odone
);

    // 游程编码器 - 请根据题目描述完善时序逻辑

endmodule
```

---

### 202. 游程解码器
- **类型**: 编程题　**难度**: 中等
- **标签**: 时序逻辑, 信号处理, 编码

**参考答案**:

```verilog
module top_module(
   input	clk,
   input	rst,
   input	[7:0]idata,
   input	ival,
   input	idone,
   output	[7:0]odata,//一个有效数据占1个时钟周期
   output	oval
);

    // 游程解码器 - 请根据题目描述完善时序逻辑

endmodule
```

---

### 203. PS2控制器—发送
- **类型**: 编程题　**难度**: 困难
- **标签**: 接口协议, 时序逻辑, 信号处理

**参考答案**:

```verilog
module top_module(
   input   clk,
   input   rst,
   input   [7:0] txdata,
   input   i_val,
   inout   scl,
   inout   sda                  
);

    // PS2控制器—发送 - 请根据题目描述完善时序逻辑

endmodule
```

---

### 204. PS2控制器—接收
- **类型**: 编程题　**难度**: 困难
- **标签**: 时序逻辑, 接口协议, 信号处理

**参考答案**:

```verilog
module top_module(
    input clk,
    input rst,
    output [7:0]rxdata,
    output o_val,
    inout  SCL,
    inout  SDA
    );

    // PS2控制器—接收 - 请根据题目描述完善时序逻辑

endmodule
```

---

### 205. 信号顺序调整
- **类型**: 编程题　**难度**: 简单
- **标签**: 组合逻辑, 入门基础

**参考答案**:

```verilog
module top_module(
    input   [15:0]  in,
    output  [15:0]  out

    );

    // 信号顺序调整 - 请根据题目描述完善组合逻辑

endmodule
```

---

### 206. 根据状态转移图实现时序电路
- **类型**: 编程题　**难度**: 简单
- **标签**: 入门基础, 时序逻辑, 状态机

**参考答案**:

```verilog
module top_module(
    input     C   ,
    input     clk ,
    input     rst ,
    output    reg Y
    );

    parameter S0 = 2'b00, S1 = 2'b01, S2 = 2'b10;
    reg [1:0] state, next;
    always @(posedge clk) begin
        if (rst) state <= S0; else state <= next;
    end
    always @(*) begin
        out = 0;
        case (state)
            S0: begin next = din ? S1 : S0; end
            S1: begin next = din ? S1 : S2; out = 1; end
            S2: begin next = din ? S1 : S0; end
        endcase
    end

endmodule
```

---

### 207. 根据状态转移表实现时序电路
- **类型**: 编程题　**难度**: 简单
- **标签**: 时序逻辑, 入门基础, 状态机

**参考答案**:

```verilog
module top_module(
      input                A   ,
      input                clk ,
      input                rst ,
  
      output   wire        Y   
);

    parameter S0 = 2'b00, S1 = 2'b01, S2 = 2'b10;
    reg [1:0] state, next;
    always @(posedge clk) begin
        if (rst) state <= S0; else state <= next;
    end
    always @(*) begin
        out = 0;
        case (state)
            S0: begin next = din ? S1 : S0; end
            S1: begin next = din ? S1 : S2; out = 1; end
            S2: begin next = din ? S1 : S0; end
        endcase
    end

endmodule
```

---

### 208. 含有无关项的序列检测器
- **类型**: 编程题　**难度**: 简单
- **标签**: 时序逻辑, 入门基础

**参考答案**:

```verilog
module top_module(
    input   clk     ,
    input   rst     ,
    input   a       ,
    input   in_valid,
    output  out     ,
    output  out_valid
    );

    parameter S0=0, S1=1, S2=2, S3=3;
    reg [1:0] state;
    always @(posedge clk) begin
        if (rst) begin state <= S0; out <= 0; end
        else begin
            out <= 0;
            case (state)
                S0: state <= din ? S1 : S0;
                S1: state <= din ? S1 : S2;
                S2: begin
                    if (din) begin state <= S3; out <= 1; end
                    else state <= S0;
                end
                S3: state <= din ? S1 : S2;
            endcase
        end
    end

endmodule
```

---

### 209. Johnson Counter
- **类型**: 编程题　**难度**: 简单
- **标签**: verilog语法练习, 时序逻辑, 入门基础

**参考答案**:

```verilog
module top_module(
    input               clk,
    input               rst,
    output  reg [3:0]   Q
    );

    always @(posedge clk) begin
        if (rst) q <= 4'b0;
        else q <= {q[2:0], ~q[3]};
    end

endmodule
```

---

### 210. 游戏机计费
- **类型**: 编程题　**难度**: 困难
- **标签**: 编码, 人工智能

**参考答案**:

```verilog
module top_module(
    input               rst     ,
    input               clk     , 	
    input       [9:0]   money   ,
    input               set     ,
	input               boost   ,
	output  reg [9:0]   remain  ,
	output  reg         yellow  ,
	output  reg         red
    );

    // 游戏机计费 - 请根据题目描述完善时序逻辑

endmodule
```

---

### 211. lemmings01
- **类型**: 编程题　**难度**: 中等
- **标签**: 入门基础, verilog语法练习, 时序逻辑

**参考答案**:

```verilog
module top_module(
    input   clk         ,
    input   rst         ,    // Freshly brainwashed Lemmings walk left.
    input   bump_left   ,
    input   bump_right  ,
    output  walk_left   ,
    output  walk_right
    );

    // lemmings01 - 请根据题目描述完善时序逻辑

endmodule
```

---

### 212. lemmings02
- **类型**: 编程题　**难度**: 中等
- **标签**: verilog语法练习, 时序逻辑, 入门基础

**参考答案**:

```verilog
module top_module(
    input   clk         ,
    input   rst         ,    // Freshly brainwashed Lemmings walk left.
    input   bump_left   ,
    input   bump_right  ,
    input   ground      ,
    output  walk_left   ,
    output  walk_right  ,
    output  aaah 
    );

    // lemmings02 - 请根据题目描述完善时序逻辑

endmodule
```

---

### 213. lemmings03
- **类型**: 编程题　**难度**: 中等
- **标签**: 时序逻辑, verilog语法练习, 入门基础

**参考答案**:

```verilog
module top_module(
    input   clk         ,
    input   rst         ,    // Freshly brainwashed Lemmings walk left.
    input   bump_left   ,
    input   bump_right  ,
    input   ground      ,
    input   dig         ,
    output  walk_left   ,
    output  walk_right  ,
    output  aaah        ,
    output  digging
    );

    // lemmings03 - 请根据题目描述完善时序逻辑

endmodule
```

---

### 214. lemmings04
- **类型**: 编程题　**难度**: 中等
- **标签**: 时序逻辑, verilog语法练习, 入门基础

**参考答案**:

```verilog
module top_module(
    input   clk         ,
    input   rst         ,    // Freshly brainwashed Lemmings walk left.
    input   bump_left   ,
    input   bump_right  ,
    input   ground      ,
    input   dig         ,
    output  walk_left   ,
    output  walk_right  ,
    output  aaah        ,
    output  digging
    );

    // lemmings04 - 请根据题目描述完善时序逻辑

endmodule
```

---

### 215. IIS主机发送模块
- **类型**: 编程题　**难度**: 困难
- **标签**: 时序逻辑, 信号处理, 慢速接口协议, 接口协议

**参考答案**:

```verilog
module top_module(
    input           clk     ,//100MHz
    input           rst     ,
    input   [15:0]  data_left,
    input   [15:0]  data_right,
    output          sck     ,//12.28MHz
    output          ws      ,
    output          sd
    );

    // IIS主机发送模块 - 请根据题目描述完善时序逻辑

endmodule
```

---

### 216. IIS主机接收模块
- **类型**: 编程题　**难度**: 困难
- **标签**: 慢速接口协议, 信号处理, 时序逻辑, 接口协议

**参考答案**:

```verilog
module top_module(
    input                   clk     ,//100MHz
    input                    rst     ,
    output  reg [15:0]      data_left,
    output  reg [15:0]      data_right,
    output                  sck     ,//12.28MHz
    output                  ws      ,
    input                   sd
    );

    // IIS主机接收模块 - 请根据题目描述完善时序逻辑

endmodule
```

---

### 217. IIS从机发送模块
- **类型**: 编程题　**难度**: 困难
- **标签**: 慢速接口协议, 时序逻辑, 信号处理, 接口协议

**参考答案**:

```verilog
module top_module(
    input           clk         ,//100MHz 
    input           rst         ,
    input   [15:0]  data_left   ,
    input   [15:0]  data_right  ,
    input           sck         ,//12.28MHz
    input           ws          ,
    output          sd
    );

    // IIS从机发送模块 - 请根据题目描述完善时序逻辑

endmodule
```

---

### 218. IIS从机接收模块
- **类型**: 编程题　**难度**: 困难
- **标签**: 时序逻辑, 信号处理, 慢速接口协议, 接口协议

**参考答案**:

```verilog
module top_module(
    input           clk         ,//100MHz 
    input           rst         ,
    output  reg [15:0]  data_left   ,
    output  reg [15:0]  data_right  ,
    input           sck         ,//12.28MHz
    input           ws          ,
    input           sd
    );

    // IIS从机接收模块 - 请根据题目描述完善时序逻辑

endmodule
```

---

### 219. 有限状态机
- **类型**: 编程题　**难度**: 简单
- **标签**: verilog语法练习, 时序逻辑, 状态机

**参考答案**:

```verilog
module top_module(
    input clk   ,
    input rst   ,
    input s     ,
    input w     ,
    output z
    );

    parameter S0 = 2'b00, S1 = 2'b01, S2 = 2'b10;
    reg [1:0] state, next;
    always @(posedge clk) state <= next;
    always @(*) begin
        next = S0; out = 0;
        case (state)
            S0: next = din ? S1 : S0;
            S1: begin next = din ? S1 : S2; out = 1; end
            S2: next = din ? S1 : S0;
        endcase
    end

endmodule
```

---

### 220. 8b/10b编码
- **类型**: 编程题　**难度**: 困难
- **标签**: 编码, 时序逻辑

**参考答案**:

```verilog
module top_module(
    input           clk     ,
    input           rst     ,
    input   [7:0]   i_data  ,
    input           i_is_k  ,
    output reg [9:0] o_data
    );

    // 8b/10b编码 - 请根据题目描述完善时序逻辑

endmodule
```

---

### 221. 波纹进位加法器01
- **类型**: 编程题　**难度**: 简单
- **标签**: verilog语法练习, 组合逻辑, 入门基础

**参考答案**:

```verilog
module top_module(
    input   [31:0]  a,
    input   [31:0]  b,
    output [31:0]  sum
    );

    wire c0, c1, c2;
    full_adder fa0(a[0], b[0], cin, sum[0], c0);
    full_adder fa1(a[1], b[1], c0, sum[1], c1);
    full_adder fa2(a[2], b[2], c1, sum[2], c2);
    full_adder fa3(a[3], b[3], c2, sum[3], cout);

    module full_adder(input a, input b, input cin, output sum, output cout);
        assign sum = a ^ b ^ cin;
        assign cout = (a & b) | (a & cin) | (b & cin);
    endmodule

endmodule
```

---

### 222. 波纹进位加法器02
- **类型**: 编程题　**难度**: 简单
- **标签**: verilog语法练习, 组合逻辑, 入门基础

**参考答案**:

```verilog
module top_module(
    input   [31:0]  a,
    input   [31:0]  b,
    output  [31:0]  sum
    );

    wire c0, c1, c2;
    full_adder fa0(a[0], b[0], cin, sum[0], c0);
    full_adder fa1(a[1], b[1], c0, sum[1], c1);
    full_adder fa2(a[2], b[2], c1, sum[2], c2);
    full_adder fa3(a[3], b[3], c2, sum[3], cout);

    module full_adder(input a, input b, input cin, output sum, output cout);
        assign sum = a ^ b ^ cin;
        assign cout = (a & b) | (a & cin) | (b & cin);
    endmodule

endmodule
```

---

### 223. 进位选择加法器
- **类型**: 编程题　**难度**: 简单
- **标签**: verilog语法练习, 组合逻辑

**参考答案**:

```verilog
module top_module(
    input   [31:0]  a,
    input   [31:0]  b,
    output  [31:0]  sum
    );

    wire [3:0] sum0, sum1;
    wire c0, c1;
    assign {c0, sum0} = a + b;
    assign {c1, sum1} = a + b + 1;
    assign sum = cin ? sum1 : sum0;
    assign cout = cin ? c1 : c0;

endmodule
```

---

### 224. 加法减法器
- **类型**: 编程题　**难度**: 简单
- **标签**: verilog语法练习, 组合逻辑

**参考答案**:

```verilog
module top_module(
    input   [31:0]  a,
    input   [31:0]  b,
    input           sub,
    output  [31:0]  sum
    );

    always @(*) begin
        if (sub) {cout, sum} = a - b;
        else {cout, sum} = a + b;
    end

endmodule
```

---

### 225. verilog赋值
- **类型**: 编程题　**难度**: 简单
- **标签**: verilog语法练习, 组合逻辑

**参考答案**:

```verilog
module top_module(
    input clk,
    input a,
    input b,
    output wire out_assign,
    output reg out_always_comb,
    output reg out_always_ff
);

    assign out_assign = clk;

endmodule
```

---

### 226. if语句
- **类型**: 编程题　**难度**: 简单
- **标签**: verilog语法练习, 组合逻辑

**参考答案**:

```verilog
module top_module(
    input a,
    input b,
    input sel_b1,
    input sel_b2,
    output wire out_assign,
    output reg out_always
);

    always @(*) begin
        if (a) out_assign = 1'b1;
        else out_assign = 1'b0;
    end

endmodule
```

---

### 227. case语句
- **类型**: 编程题　**难度**: 简单
- **标签**: 组合逻辑, verilog语法练习, 入门基础

**参考答案**:

```verilog
module top_module(   
   input [2:0] sel, 
    input [3:0] data0,
    input [3:0] data1,
    input [3:0] data2,
    input [3:0] data3,
    input [3:0] data4,
    input [3:0] data5,
    output reg [3:0] out  
);

    always @(*) begin
        case (sel)
            2'b00: out = 4'b0001;
            2'b01: out = 4'b0010;
            2'b10: out = 4'b0100;
            2'b11: out = 4'b1000;
        endcase
    end

endmodule
```

---

### 228. case避免闩锁
- **类型**: 编程题　**难度**: 简单

**参考答案**:

```verilog
moudle top_module(
    input [15:0] scancode,
    output reg left,
    output reg down,
    output reg right,
    output reg up 
);

    always @(*) begin
        left = 0;
        case (scancode)
            2'b00: left = 4'b0001;
            2'b01: left = 4'b0010;
            2'b10: left = 4'b0100;
            2'b11: left = 4'b1000;
        endcase
    end

endmodule
```

---

### 229. for循环--反序
- **类型**: 编程题　**难度**: 简单

**参考答案**:

```verilog
module top_module(
    input   [31:0]  in,
    output  [31:0]  out
    );

    integer j;
    always @(*) begin
        for (j = 0; j < 8; j = j + 1)
            out[j] = in[7-j];
    end

endmodule
```

---

### 230. 利用for循环计数
- **类型**: 编程题　**难度**: 简单

**参考答案**:

```verilog
module top_module(
    input   [31:0]  in,
    output  [4:0]   out
    );

    integer j;
    always @(*) begin
        cnt = 0;
        for (j = 0; j < 8; j = j + 1)
            cnt = cnt + data[j];
    end

endmodule
```

---

### 231. 非A或非B或非C
- **类型**: 编程题　**难度**: 简单

**参考答案**:

```verilog
module top_module(
    input   a,
    input   b,
    input   c,
    output  out
    );

    assign out = ~a | ~b | ~c;

endmodule
```

---

### 232. 非A与B或C
- **类型**: 编程题　**难度**: 简单

**参考答案**:

```verilog
module top_module(
    input   a,
    input   b,
    input   c,
    output  out
    );

    assign out = ~a & (b | c);

endmodule
```

---

### 233. JK触发器
- **类型**: 编程题　**难度**: 简单

**参考答案**:

```verilog
module top_module(
    input       j   ,
    input       k   ,
    input       clk ,
    input       rst ,
    output  reg q
    );

    always @(posedge clk) begin
        if (rst) q <= 1'b0;
        else begin
            case ({j, k})
                2'b00: q <= q;
                2'b01: q <= 1'b0;
                2'b10: q <= 1'b1;
                2'b11: q <= ~q;
            endcase
        end
    end

endmodule
```

---

### 234. 二进制整数除法器
- **类型**: 编程题　**难度**: 中等

**参考答案**:

```verilog
module top_module(
    input       [7:0]   a,//a为被除数
    input       [3:0]   b,//b为除敿
    output  reg [7:0]   c,//c为商
    output  reg [3:0]   d//d为余敿
    );

    // 二进制整数除法器 - 请根据题目描述完善组合逻辑

endmodule
```

---

### 235. 优先级固定仲裁
- **类型**: 编程题　**难度**: 中等

**参考答案**:

```verilog
module top_module(
    input   [7:0]  req,    //访问输入，优先级从高到底
    
    output  [7:0]  grant  //最终的访问许可输出，grant对应位高则获得访问许可
    );

    // 优先级固定仲裁 - 请根据题目描述完善组合逻辑

endmodule
```

---

### 236. 优先级固定仲裁02
- **类型**: 编程题　**难度**: 中等

**参考答案**:

```verilog
module top_module(
    input   [15:0]  req,    //访问输入
    input   [15:0]  base,   //给出的优先级设定
    output  [15:0]  grant   //最终的访问许可输出，grant对应位高则获得访问许可
    );

    // 优先级固定仲裁02 - 请根据题目描述完善组合逻辑

endmodule
```

---

### 237. RR轮询调度仲裁器
- **类型**: 编程题　**难度**: 中等

**参考答案**:

```verilog
module top_module(
    input           clk     ,
    input           rst   ,
    input   [15:0]  req     ,//访问输入
    
    output  [15:0]  grant 
    );

    // RR轮询调度仲裁器 - 请根据题目描述完善时序逻辑

endmodule
```

---

### 238. RR轮询调度仲裁器02
- **类型**: 编程题　**难度**: 困难

**参考答案**:

```verilog
module top_module(
    input         clk,
input         rst,
input [15:0] req,
output[15:0] grant
 
);

    // RR轮询调度仲裁器02 - 请根据题目描述完善时序逻辑

endmodule
```

---

### 239. generate-for练习
- **类型**: 编程题　**难度**: 简单

**参考答案**:

```verilog
module top_module(
    input [7:0] data_in,
    output [7:0] data_out

);

    genvar k;
    generate
        for (k = 0; k < 4; k = k + 1) begin : gen_block
            assign out[k] = in[k];
        end
    endgenerate

endmodule
```

---

### 240. 基于8-3优先编码器的16-4优先编码器
- **类型**: 编程题　**难度**: 简单

**参考答案**:

```verilog
module top_module(
    input           [15:0]  data_in ,
    input                   ei      ,

    output  wire    [3:0]   data_out,
    output  wire            gs      ,
    output  wire            eo  
    );

    always @(*) begin
        valid = 1'b1;
        casex (in)
            8'b1xxxxxxx: out = 3'd7;
            8'b01xxxxxx: out = 3'd6;
            8'b001xxxxx: out = 3'd5;
            8'b0001xxxx: out = 3'd4;
            8'b00001xxx: out = 3'd3;
            8'b000001xx: out = 3'd2;
            8'b0000001x: out = 3'd1;
            8'b00000001: out = 3'd0;
            default: begin out = 3'd0; valid = 1'b0; end
        endcase
    end

endmodule
```

---

### 241. 数据选择器的逻辑电路
- **类型**: 编程题　**难度**: 中等

**参考答案**:

```verilog
module top_module(
    input   a,
    input   b,
    input   c,
    output  y
    );

    assign y = sel ? b : a;

endmodule
```

---

### 242. rom的简单实现
- **类型**: 编程题　**难度**: 简单

**参考答案**:

```verilog
module top_module(
    input           clk ,
    input           rst ,
    input   [2:0]   addr,
    output  [3:0]   data
    );

    reg [7:0] mem [0:255];
    initial $readmemh("rom_init.hex", mem);
    assign rd_data = mem[addr];

endmodule
```

---

### 243. 边沿检测
- **类型**: 编程题　**难度**: 简单

**参考答案**:

```verilog
module top_module(
    input   clk ,
    input   rst ,
    input   a   ,
    output  rise,
    output  down
    );

    reg d_reg;
    always @(posedge clk) d_reg <= din;
    assign pos_edge = din & ~d_reg;
    assign neg_edge = ~din & d_reg;

endmodule
```

---

### 244. 不重叠序列检测
- **类型**: 编程题　**难度**: 简单

**参考答案**:

```verilog
module top_module(
    input   clk     ,
    input   rst     ,
    input   data    ,
    output  match   ,
    output  not_match
    );

    parameter S0=0, S1=1, S2=2, S3=3;
    reg [1:0] state;
    always @(posedge clk) begin
        if (rst) begin state <= S0; out <= 0; end
        else begin
            out <= 0;
            case (state)
                S0: state <= din ? S1 : S0;
                S1: state <= din ? S1 : S2;
                S2: begin
                    if (din) begin state <= S3; out <= 1; end
                    else state <= S0;
                end
                S3: state <= din ? S1 : S2;
            endcase
        end
    end

endmodule
```

---

### 245. 输入不连续序列检测
- **类型**: 编程题　**难度**: 简单

**参考答案**:

```verilog
module top_module(
    input   clk     ,
    input   rst     ,
    input   data    ,
    input   data_valid,
    output  match
    );

    parameter S0=0, S1=1, S2=2, S3=3;
    reg [1:0] state;
    always @(posedge clk) begin
        if (rst) begin state <= S0; out <= 0; end
        else begin
            out <= 0;
            case (state)
                S0: state <= din ? S1 : S0;
                S1: state <= din ? S1 : S2;
                S2: begin
                    if (din) begin state <= S3; out <= 1; end
                    else state <= S0;
                end
                S3: state <= din ? S1 : S2;
            endcase
        end
    end

endmodule
```

---

### 246. 信号发生器
- **类型**: 编程题　**难度**: 中等

**参考答案**:

```verilog
module top_module(
    input               clk         ,
    input               rst         ,
    input       [1:0]   wave_choise ,    
    output  reg [4:0]   wave
    );

    reg [1:0] cnt;
    always @(posedge clk) begin
        if (rst) cnt <= 0;
        else cnt <= cnt + 1;
    end
    always @(*) begin
        case (cnt)
            2'd0: begin p0=1; p1=0; p2=0; p3=0; end
            2'd1: begin p0=0; p1=1; p2=0; p3=0; end
            2'd2: begin p0=0; p1=0; p2=1; p3=0; end
            2'd3: begin p0=0; p1=0; p2=0; p3=1; end
        endcase
    end

endmodule
```

---

### 247. 数据累加输出
- **类型**: 编程题　**难度**: 中等

**参考答案**:

```verilog
module top_module(
    input           clk     ,
    input           rst     ,
    input   [7:0]   data_in ,
    input           valid_in,
    input           ready_b ,
    
    output  reg [9:0]   data_out,
    output  reg         valid_out ,
    output  reg         ready_a 
    );

    // 数据累加输出 - 请根据题目描述完善时序逻辑

endmodule
```

---

### 248. 非整数倍数据位宽转换24~128
- **类型**: 编程题　**难度**: 简单

**参考答案**:

```verilog
module top_module(
    input               clk     ,
    input               rst     ,
    input       [23:0]  data_in ,
    input               valid_in,
    output  reg [127:0] data_out,
    output  reg         valid_out
    );

    // 非整数倍数据位宽转换24~128 - 请根据题目描述完善时序逻辑

endmodule
```

---

### 249. 非整数倍数据位宽转换8-12
- **类型**: 编程题　**难度**: 简单

**参考答案**:

```verilog
module top_module(
    input               clk         ,
    input               rst         ,
    input               valid_in    ,
    input       [7:0]   data_in     ,

    output  reg         valid_out   ,
    output  reg [11:0]  data_out    
    );

    // 非整数倍数据位宽转换8-12 - 请根据题目描述完善时序逻辑

endmodule
```

---

### 250. 时钟小数分频
- **类型**: 编程题　**难度**: 简单

**参考答案**:

```verilog
module top_module(
    input   clk_in  ,
    input   rst     ,
    output  clk_out
);

    reg [3:0] cnt;
    always @(posedge clk) begin
        if (rst) begin cnt <= 0; clk_out <= 0; end
        else begin
            if (cnt == 4) begin cnt <= 0; clk_out <= ~clk_out; end
            else cnt <= cnt + 1;
        end
    end

endmodule
```

---

### 251. 整数倍数据位宽转换8-16
- **类型**: 编程题　**难度**: 简单

**参考答案**:

```verilog
module top_module(
    input               clk         ,
    input               rst         ,
    input               valid_in    ,
    input       [7:0]   data_in     ,

    output  reg         valid_out   ,
    output  reg [15:0]  data_out    
    );

    // 整数倍数据位宽转换8-16 - 请根据题目描述完善时序逻辑

endmodule
```

---

### 252. 二段式状态机
- **类型**: 编程题　**难度**: 简单

**参考答案**:

```verilog
module top_module(
    input   clk ,
    input   rst ,
    input   data,
    output  reg flag
    );

    parameter S0 = 2'b00, S1 = 2'b01, S2 = 2'b10;
    reg [1:0] state, next;
    always @(posedge clk) state <= next;
    always @(*) begin
        next = S0; out = 0;
        case (state)
            S0: next = din ? S1 : S0;
            S1: begin next = din ? S1 : S2; out = 1; end
            S2: next = din ? S1 : S0;
        endcase
    end

endmodule
```

---

### 253. 三段式状态机
- **类型**: 编程题　**难度**: 简单

**参考答案**:

```verilog
module top_module(
    input   clk ,
    input   rst ,
    input   data,
    output  reg flag
    );

    parameter S0 = 2'b00, S1 = 2'b01, S2 = 2'b10;
    reg [1:0] state, next;
    always @(posedge clk) state <= next;
    always @(*) begin
        next = S0; out = 0;
        case (state)
            S0: next = din ? S1 : S0;
            S1: begin next = din ? S1 : S2; out = 1; end
            S2: next = din ? S1 : S0;
        endcase
    end

endmodule
```

---

### 254. 多位mux控制器
- **类型**: 编程题　**难度**: 简单

**参考答案**:

```verilog
module top_module(
    input               clk_a   ,
    input               clk_b   ,  
    input               rst_a   ,
    input               rst_b   ,
    input       [3:0]   data_in ,
    input               data_en ,

    output  reg [3:0]   dataout
    );

    always @(*) begin
        case (sel)
            2'b00: dataout = clk_a;
            2'b01: dataout = clk_b;
            2'b10: dataout = rst_a;
            2'b11: dataout = rst_b;
        endcase
    end

endmodule
```

---

### 255. 可置位计数器
- **类型**: 编程题　**难度**: 简单

**参考答案**:

```verilog
module top_module(
    input           clk     ,
    input           rst     ,
    input           set     ,
    input   [3:0]   set_num ,
    output          zero    ,
    output  [3:0]   number
    );

    always @(posedge clk) begin
        if (load) cnt <= data_in;
        else cnt <= cnt + 1'b1;
    end

endmodule
```

---

### 256. 加减计数器
- **类型**: 编程题　**难度**: 简单

**参考答案**:

```verilog
module top_module(
    input           clk     ,
    input           rst     ,
    input           mode    ,
    output          zero    ,
    output  [3:0]   number
    );

    always @(posedge clk) begin
        if (rst) cnt <= 0;
        else if (up_down) cnt <= cnt + 1;
        else cnt <= cnt - 1;
    end

endmodule
```

---

### 257. 正交解码器
- **类型**: 编程题　**难度**: 困难

**参考答案**:

```verilog
module top_module(
    input           clk     ,
    input           rst     ,
    input           sign_a  ,
    input           sign_b  ,
    
    output  reg [7:0]   cnt  
    );

    // 正交解码器 - 请根据题目描述完善时序逻辑

endmodule
```

---

### 258. pwm上下计数器
- **类型**: 编程题　**难度**: 中等

**参考答案**:

```verilog
module top_module(
    input           clk     ,
    input           rst     ,
    input   [3:0]   pwm_in  ,
    output          pwm_out
);

    reg [7:0] cnt;
    always @(posedge clk) begin
        if (rst) cnt <= 0;
        else cnt <= cnt + 1;
    end
    assign pwm_out = (cnt < duty);

endmodule
```

---

### 259. 输入连续序列检测(hairuoyouying提供)
- **类型**: 编程题　**难度**: 简单

**参考答案**:

```verilog
module top_module(
    input clk,
	input rst_n,
	input a,
	output reg match
	);

    parameter S0=0, S1=1, S2=2, S3=3;
    reg [1:0] state;
    always @(posedge clk) begin
        if (rst) begin state <= S0; out <= 0; end
        else begin
            out <= 0;
            case (state)
                S0: state <= din ? S1 : S0;
                S1: state <= din ? S1 : S2;
                S2: begin
                    if (din) begin state <= S3; out <= 1; end
                    else state <= S0;
                end
                S3: state <= din ? S1 : S2;
            endcase
        end
    end

endmodule
```

---

### 260. 三级伽罗瓦LFSR
- **类型**: 编程题　**难度**: 中等

**参考答案**:

```verilog
module top_module(
    input       clk    ,
    input       rst     ,
    output  reg glfsrn
    );

    // 三级伽罗瓦LFSR - 请根据题目描述完善时序逻辑

endmodule
```

---

### 261. 三级斐波那契LFSR
- **类型**: 编程题　**难度**: 中等

**参考答案**:

```verilog
module top_module(
	input       clk    ,
    input       rst     ,
    output  reg flfsrn
);

    // 三级斐波那契LFSR - 请根据题目描述完善时序逻辑

endmodule
```

---

### 262. 编写乘法器求解算法表达式(hairuoyouying提供)
- **类型**: 编程题　**难度**: 简单

**参考答案**:

```verilog
module top_module(
    input clk,
	input rst_n,
	input [3:0] a,
	input [3:0] b,
	output [8:0] c
	);

    // 编写乘法器求解算法表达式(hairuoyouying提供) - 请根据题目描述完善时序逻辑

endmodule
```

---

### 263. 时钟脉冲电路(hairuoyouying提供)
- **类型**: 编程题　**难度**: 简单

**参考答案**:

```verilog
module top_module(
    input   clk ,
    input   rst ,
    input   inp ,
    output  outp
    );

    // 时钟脉冲电路(hairuoyouying提供) - 请根据题目描述完善时序逻辑

endmodule
```

---

### 264. 带异步复位和置位端的D触发器(hairuoyouying提供)
- **类型**: 编程题　**难度**: 简单

**参考答案**:

```verilog
module top_module(
    input       clk     ,
    input       rst     ,
    input       set     ,
    input       data    ,
    output  reg out_data
    );

    always @(posedge clk or posedge rst) begin
        if (rst) q <= 1'b0;
        else q <= d;
    end

endmodule
```

---

### 265. 脉冲宽度调制(hairuoyouying提供)
- **类型**: 编程题　**难度**: 简单

**参考答案**:

```verilog
module top_module
#(parameter N = 4)
(
    input wire clk,
    input wire rst,
    input wire [N-1:0] duty,
    input wire [N-1:0] period,
    output reg pwm
    );

    reg [7:0] cnt;
    always @(posedge clk) begin
        if (rst) cnt <= 0;
        else cnt <= cnt + 1;
    end
    assign pwm_out = (cnt < duty);

endmodule
```

---

### 266. 根据RTL图编写Verilog程序(hairuoyouying提供)
- **类型**: 编程题　**难度**: 简单

**参考答案**:

```verilog
module top_module(
    input       clk     ,
	input       rst_n   ,
	input       data_in ,
	output      data_out
	);

    // 根据RTL图编写Verilog程序(hairuoyouying提供) - 请根据题目描述完善时序逻辑

endmodule
```

---

### 267. 最小公约数最大公倍数(hairuoyouying提供)
- **类型**: 编程题　**难度**: 困难

**参考答案**:

```verilog
module top_module
(
    input                   clk     ,
    input                   rst_n   ,
    input           [7:0]   data1   ,
    input           [7:0]   data2   ,
    input                   vld_in  ,
    output  wire    [15:0]  lcm_out ,
    output  wire    [7:0]   mcd_out ,
    output  reg             vld_out
);

    // 最小公约数最大公倍数(hairuoyouying提供) - 请根据题目描述完善时序逻辑

endmodule
```

---

### 268. 2-4译码器（FXS174080提供）
- **类型**: 编程题　**难度**: 简单

**参考答案**:

```verilog
module top_module(
    input   en  ,
    input   a0,a1,
    output  y0,y1,y2,y3
    );

    always @(*) begin
        case (en)
            2'b00: y0 = 4'b0001;
            2'b01: y0 = 4'b0010;
            2'b10: y0 = 4'b0100;
            2'b11: y0 = 4'b1000;
        endcase
    end

endmodule
```

---

### 269. 一位全加器（FXS174080提供）
- **类型**: 编程题　**难度**: 简单

**参考答案**:

```verilog
module top_module(
    input ci,
    input a,
    input b,
    output s,
    output co
    );

    assign sum = a ^ b ^ cin;
    assign cout = (a & b) | (a & cin) | (b & cin);

endmodule
```

---

### 270. 优先报警器(FXS174080提供)
- **类型**: 编程题　**难度**: 中等

**参考答案**:

```verilog
module top_module(
    input I0,
    input I1,
    input I2,
    input I3,
    output Y0,
    output Y1,
    output Y2
    );

    // 优先报警器(FXS174080提供) - 请根据题目描述完善组合逻辑

endmodule
```

---

### 271. bcd码减法器（FXS174080提供）
- **类型**: 编程题　**难度**: 简单

**参考答案**:

```verilog
module top_module(
    input   [3:0]   a       ,//输入被减数a 
    input   [3:0]   b       ,//输入被减数b 
    input           rst_n   ,//系统复位，低电平有效 
    output  [3:0]   bcd1    ,//输出个位 
    output  [3:0]   bcd2    ,//输出十位 
    output          sign     //输出符号位
    );

    // bcd码减法器（FXS174080提供） - 请根据题目描述完善组合逻辑

endmodule
```

---

### 272. 含异步复位和同步使能的D触发器（FXS174080提供）
- **类型**: 编程题　**难度**: 简单

**参考答案**:

```verilog
module top_module(
    input   clk     , 
    input   reset   , 
    input   d       , 
    input   en      , 
    output  q
    );

    always @(posedge clk or posedge rst) begin
        if (rst) q <= 1'b0;
        else q <= d;
    end

endmodule
```

---

### 273. 1MHz十进制计数器（FXS174080提供）
- **类型**: 编程题　**难度**: 简单

**参考答案**:

```verilog
module top_module(
    input           clk     ,//100MHz 
    input           rst     ,
    input           enable  , 
    output  [3:0]   out
    );

    always @(posedge clk) begin
        if (rst) cnt <= 4'd0;
        else if (cnt == 4'd9) cnt <= 4'd0;
        else cnt <= cnt + 1'b1;
    end

endmodule
```

---

### 274. 线上仿真彩灯循环系统（FXS174080提供）
- **类型**: 编程题　**难度**: 简单

**参考答案**:

```verilog
module top_module(
    input           clk     , 
    input           rst_n   , 
    output  [3:0]   led
    );

    reg [31:0] cnt;
    always @(posedge clk) begin
        if (rst) begin cnt <= 0; led <= 8'b00000001; end
        else begin
            if (cnt == 49999999) begin cnt <= 0; led <= {led[6:0], led[7]}; end
            else cnt <= cnt + 1;
        end
    end

endmodule
```

---

### 275. 二进制转十进制（FXS174080提供）
- **类型**: 编程题　**难度**: 简单

**参考答案**:

```verilog
module top_module(
    input   [3:0]   bin , 
    input           set , 
    output  [3:0]   bcd1, 
    output  [3:0]   bcd2
    );

    always @(*) begin
        bcd[3:0] = binary % 10;
        bcd[7:4] = (binary / 10) % 10;
        bcd[11:8] = (binary / 100) % 10;
    end

endmodule
```

---

### 276. bcd码加法器（FXS174080提供）
- **类型**: 编程题　**难度**: 简单

**参考答案**:

```verilog
module top_module(
    input   [3:0]   a       ,//输入加数a 
    input   [3:0]   b       ,//输入加数b 
    input           rst_n   ,//系统复位，低电平有效 
    output  [3:0]   bcd1    ,//输出个位 
    output  [3:0]   bcd2     //输出十位
    );

    // bcd码加法器（FXS174080提供） - 请根据题目描述完善组合逻辑

endmodule
```

---

### 277. 阶乘运算（FXS174080提供）
- **类型**: 编程题　**难度**: 中等

**参考答案**:

```verilog
module top_module(
    input          clk     , 
    input  [2:0]   n       ,//阶数n 
    input          rst_n   ,//系统复位，低电平有效 
    output [15:0]  result  ,//阶乘结果
    output reg     finish  
    );

    // 阶乘运算（FXS174080提供） - 请根据题目描述完善时序逻辑

endmodule
```

---

### 278. 有符号累加模块（FXS174080提供）
- **类型**: 编程题　**难度**: 中等

**参考答案**:

```verilog
module top_module(
    input           clk     ,//系统时钟
    input           rst_n   ,//系统复位，低电平有效
    input   [3:0]   i_data  ,//数据输入口（最高位是符号位） 大小：-8~+7范围有符号数
    input           valid   ,//数据有效（高有效）
    output  [5:0]   o_data  ,//输出数据口（最高位是符号位）
    output          o_ready  //输出数据有效
    );

    // 有符号累加模块（FXS174080提供） - 请根据题目描述完善时序逻辑

endmodule
```

---

### 279. 电梯控制电路（FXS174080提供）
- **类型**: 编程题　**难度**: 困难

**参考答案**:

```verilog
module top_module(
    input               clk     , 
    input               rst_n   ,
    input               key     , 
    input       [7:0]   high    , 
    input       [3:0]   num     , 
    input       [9:0]   weight  ,
    output  reg [7:0]   floor   ,
    output              alert
    );

    // 电梯控制电路（FXS174080提供） - 请根据题目描述完善时序逻辑

endmodule
```

---

### 280. 二输入逻辑门的verilog程序（hairuoyouying提供）
- **类型**: 编程题　**难度**: 简单

**参考答案**:

```verilog
module top_module(
    input           a,
    input           b,
    output  [5:0]   y
    );

    assign y = a | b;

endmodule
```

---

### 281. 实现多输入逻辑门（简约运算符）（hairuoyouying提供）
- **类型**: 编程题　**难度**: 简单

**参考答案**:

```verilog
module top_module(
    input   [3:0]a,
    output  [5:0]y

    );

    // 实现多输入逻辑门（简约运算符）（hairuoyouying提供） - 请根据题目描述完善组合逻辑

endmodule
```

---

### 282. 实现多输入逻辑门（门实例化语句）（hairuoyouying提供）
- **类型**: 编程题　**难度**: 简单

**参考答案**:

```verilog
module top_module(
    input   [3:0]   a ,
    output  [5:0]   y
    );

    assign y = |{a};

endmodule
```

---

### 283. 利用2输入与非门设计或门电路（hairuoyouying提供）
- **类型**: 编程题　**难度**: 简单

**参考答案**:

```verilog
module top_module(
    input   a,
    input   b,
    output  y
    );

    wire tmp;
    assign tmp = ~(a | b);
    assign y = ~tmp;

endmodule
```

---

### 284. 数字频率计（FXS174080提供）
- **类型**: 编程题　**难度**: 困难

**参考答案**:

```verilog
module top_module#(parameter CLK_FS = 27'd100_000_000/*基准时钟频率值*/)(
    //system clock
    input                clk_fs ,   // 基准时钟信号
    input                rst_n  ,   // 复位信号
    
    //cymometer interface
    input                clk_fx ,   // 被测时钟
    output  reg [24:0]  data_fx     // 被测信号测量值
    );

    // 数字频率计（FXS174080提供） - 请根据题目描述完善时序逻辑

endmodule
```

---

### 285. 2-10进制优先编码器（FXS174080提供）
- **类型**: 编程题　**难度**: 简单

**参考答案**:

```verilog
module top_module(
    input   [8:0] data_in,
    output  [3:0] data_out
    );

    always @(*) begin
        valid = |data_in;
        casez (data_in)
            10'b1xxxxxxxxx: data_out = 4'd9;
            10'b01xxxxxxxx: data_out = 4'd8;
            10'b001xxxxxxx: data_out = 4'd7;
            10'b0001xxxxxx: data_out = 4'd6;
            10'b00001xxxxx: data_out = 4'd5;
            10'b000001xxxx: data_out = 4'd4;
            10'b0000001xxx: data_out = 4'd3;
            10'b00000001xx: data_out = 4'd2;
            10'b000000001x: data_out = 4'd1;
            10'b0000000001: data_out = 4'd0;
            default: data_out = 4'd0;
        endcase
    end

endmodule
```

---

### 286. 2-10进制译码器（FXS174080提供）
- **类型**: 编程题　**难度**: 简单

**参考答案**:

```verilog
module top_module(
    input   [3:0] data_in,
    output  [9:0] data_out
    );

    always @(*) begin
        case (data_in)
            2'b00: data_out = 4'b0001;
            2'b01: data_out = 4'b0010;
            2'b10: data_out = 4'b0100;
            2'b11: data_out = 4'b1000;
        endcase
    end

endmodule
```

---

### 287. 顺序脉冲发生器（FXS174080提供）
- **类型**: 编程题　**难度**: 简单

**参考答案**:

```verilog
module top_module(
    input           clk     ,
    input           rst_n   ,
    output  [7:0]   pulse
    );

    reg [1:0] cnt;
    always @(posedge clk) begin
        if (rst) cnt <= 0;
        else cnt <= cnt + 1;
    end
    always @(*) begin
        case (cnt)
            2'd0: begin p0=1; p1=0; p2=0; p3=0; end
            2'd1: begin p0=0; p1=1; p2=0; p3=0; end
            2'd2: begin p0=0; p1=0; p2=1; p3=0; end
            2'd3: begin p0=0; p1=0; p2=0; p3=1; end
        endcase
    end

endmodule
```

---

### 288. 序列信号发生器（FXS174080提供）
- **类型**: 编程题　**难度**: 简单

**参考答案**:

```verilog
module top_module(
    input       clk     , 
    input       rst_n   , 
    output      data_out
    );

    reg [1:0] cnt;
    always @(posedge clk) begin
        if (rst) cnt <= 0;
        else cnt <= cnt + 1;
    end
    always @(*) begin
        case (cnt)
            2'd0: begin p0=1; p1=0; p2=0; p3=0; end
            2'd1: begin p0=0; p1=1; p2=0; p3=0; end
            2'd2: begin p0=0; p1=0; p2=1; p3=0; end
            2'd3: begin p0=0; p1=0; p2=0; p3=1; end
        endcase
    end

endmodule
```

---

### 289. 3-8译码器板端实验
- **类型**: 编程题　**难度**: 简单

**参考答案**:

```verilog
module top_module(
    input   wire    [2:0]   in,
    output  wire    [7:0]   out
    );

    assign out = 1'b1 << in;

endmodule
```

---

### 290. 利用与非门构成与门(hairuoyouying提供)
- **类型**: 编程题　**难度**: 简单

**参考答案**:

```verilog
module top_module(
    input   a,
    input   b,
    output  y
    );

    wire tmp;
    assign tmp = ~(a & b);
    assign y = ~tmp;

endmodule
```

---

### 291. 利用或非门构成与门(hairuoyouying提供)
- **类型**: 编程题　**难度**: 简单

**参考答案**:

```verilog
module top_module(
    input   a, 
    input   b, 
    output  y
    );

    wire tmp;
    assign tmp = ~(a | b);
    assign y = ~tmp;

endmodule
```

---

### 292. 利用二输入或非门构成或门电路(hairuoyouying提供)
- **类型**: 编程题　**难度**: 简单

**参考答案**:

```verilog
module top_module(
    input   a,
    input   b,
    output  y
    );

    wire tmp;
    assign tmp = ~(a | b);
    assign y = ~tmp;

endmodule
```

---

### 293. 递増递减计数器(FXS046592提供)
- **类型**: 编程题　**难度**: 简单

**参考答案**:

```verilog
module top_module(
    input               clk ,
    input               rst ,
    input               k   ,
    output  reg [6:0]   out
    );

    always @(posedge clk) begin
        if (rst) cnt <= 0;
        else if (up_down) cnt <= cnt + 1;
        else cnt <= cnt - 1;
    end

endmodule
```

---

### 294. 水泵控制电路(FXS174080提供)
- **类型**: 编程题　**难度**: 简单

**参考答案**:

```verilog
module top_module(
    input A, B, C,
    output L, S
    );

    // 水泵控制电路(FXS174080提供) - 请根据题目描述完善组合逻辑

endmodule
```

---

### 295. 逻辑电路图转换(FXS174080提供)
- **类型**: 编程题　**难度**: 简单

**参考答案**:

```verilog
module top_module(
    input A, B, C, D,
    output eseg
    );

    // 逻辑电路图转换(FXS174080提供) - 请根据题目描述完善组合逻辑

endmodule
```

---

### 296. 步进电机三相六状态工作的逻辑电路(FXS174080提供)
- **类型**: 编程题　**难度**: 简单

**参考答案**:

```verilog
module top_module(
    input       clk     ,  //clock 50MHz
    input       rst_n   ,  //reset
    input       M       ,  //input control variable
    
    output  reg A, B, C
    );

    // 步进电机三相六状态工作的逻辑电路(FXS174080提供) - 请根据题目描述完善时序逻辑

endmodule
```

---

### 297. 裁判电路(FXS174080提供)
- **类型**: 编程题　**难度**: 简单

**参考答案**:

```verilog
module top_module(
    input A, B, C,
    output result
    );

    assign result = (A & B) | (A & C) | (B & C);

endmodule
```

---

### 298. 根据逻辑图实现一位全加器(FXS174080提供)
- **类型**: 编程题　**难度**: 简单

**参考答案**:

```verilog
module top_module(
    input       A   , 
    input       B   , 
    input       CI  , 
    output      Sum , 
    output      Cout 
    );

    assign sum = a ^ b ^ cin;
    assign cout = (a & b) | (a & cin) | (b & cin);

endmodule
```

---

### 299. 灯光控制逻辑电路(FXS174080提供)
- **类型**: 编程题　**难度**: 简单

**参考答案**:

```verilog
module top_module(
    input       clk     ,
    input       rst_n   ,
    output      R       ,
    output      Y       ,
    output      B
    );

    // 灯光控制逻辑电路(FXS174080提供) - 请根据题目描述完善时序逻辑

endmodule
```

---

### 300. 并行FIR滤波器FPGA实现
- **类型**: 编程题　**难度**: 困难

**参考答案**:

```verilog
module top_module(
 
        input clk,//!系统时钟
        input rst,//!复位信号
        input signed [11:0] signal_in,//!信号输入
        output signed [28:0] signal_out//!信号输出,信号输出速度和输入速度相同
    );

    // 并行FIR滤波器FPGA实现 - 请根据题目描述完善时序逻辑

endmodule
```

---

### 301. 跑马灯的左移，右移，对开,对分(FXS046592提供)
- **类型**: 编程题　**难度**: 简单

**参考答案**:

```verilog
module top_module(
    input               clk ,
    input               rst ,
    input               sw  ,
    input               k   ,
    
    output  reg [7:0]   led
    );

    reg [31:0] cnt;
    reg [1:0] mode;
    always @(posedge clk) begin
        if (rst) begin cnt <= 0; led <= 8'b00000001; end
        else begin
            if (cnt == 49999999) begin
                cnt <= 0;
                case (mode)
                    2'd0: led <= {led[6:0], led[7]};
                    2'd1: led <= {led[0], led[7:1]};
                    default: led <= {led[6:0], led[7]};
                endcase
            end else cnt <= cnt + 1;
        end
    end

endmodule
```

---

### 302. 用或非门构成非门(hairuoyouying提供)
- **类型**: 编程题　**难度**: 简单

**参考答案**:

```verilog
module top_module(
    input   a,
    output  y
    );

    // 用或非门构成非门(hairuoyouying提供) - 请根据题目描述完善组合逻辑

endmodule
```

---

### 303. 七进制加法计数器(FXS174080提供)
- **类型**: 编程题　**难度**: 简单

**参考答案**:

```verilog
module top_module(
    input           clk     ,
    input           rst_n   ,
    input           M       ,
    output  [3:0]   q   
    );

    always @(posedge clk) begin
        if (rst) cnt <= 3'd0;
        else if (cnt == 3'd6) cnt <= 3'd0;
        else cnt <= cnt + 1'b1;
    end

endmodule
```

---

### 304. Mealy型状态机(FXS174080提供)
- **类型**: 编程题　**难度**: 简单

**参考答案**:

```verilog
module top_module(
    input       clk , 
    input       rst ,
    input       din ,
    output  reg op
    );

    parameter S0 = 2'b00, S1 = 2'b01, S2 = 2'b10;
    reg [1:0] state, next;
    always @(posedge clk) state <= next;
    always @(*) begin
        next = S0; out = 0;
        case (state)
            S0: next = din ? S1 : S0;
            S1: begin next = din ? S1 : S2; out = 1; end
            S2: next = din ? S1 : S0;
        endcase
    end

endmodule
```

---

### 305. 产生频率为2khz的PWM信号(hairuoyouying提供)
- **类型**: 编程题　**难度**: 简单

**参考答案**:

```verilog
module top_module(
    input           clk ,
    input           rst ,
    input   [7:0]   duty,
    output  reg     pwm
    );

    reg [7:0] cnt;
    always @(posedge clk) begin
        if (rst) cnt <= 0;
        else cnt <= cnt + 1;
    end
    assign pwm_out = (cnt < duty);

endmodule
```

---

### 306. 五进制计数器(hairuoyouying提供)
- **类型**: 编程题　**难度**: 简单

**参考答案**:

```verilog
module top_module(
    input   wire        rst ,
    input   wire        clk ,
    output  reg [2:0]   Q
    );

    always @(posedge clk) begin
        if (rst) cnt <= 3'd0;
        else if (cnt == 3'd4) cnt <= 3'd0;
        else cnt <= cnt + 1'b1;
    end

endmodule
```

---

### 307. 环形移位寄存器(hairuoyouying提供)
- **类型**: 编程题　**难度**: 简单

**参考答案**:

```verilog
module top_module(
    input               clk ,
    input               rst ,
    output  reg [3:0]   Q    //初值为4'd1
    );

    always @(posedge clk) begin
        if (rst) q <= 0;
        else q <= {q[WIDTH-2:0], d};
    end

endmodule
```

---

### 308. N位寄存器(hairuoyouying提供)
- **类型**: 编程题　**难度**: 简单

**参考答案**:

```verilog
module top_module(
    input               clk ,
	input               rst ,
    input               load,
    input       [7:0]   D   ,
    output  reg [7:0]   Q
    );

    always @(posedge clk) begin
        if (en) Q <= clk;
    end

endmodule
```

---

### 309. 同步电路(hairuoyouying提供)
- **类型**: 编程题　**难度**: 简单

**参考答案**:

```verilog
module top_module(
    input               clk     ,
    input               rst     ,
    input       [5:0]   addr_in ,
    output  reg [5:0]   addr_out  
    );

    // 同步电路(hairuoyouying提供) - 请根据题目描述完善时序逻辑

endmodule
```

---

### 310. 可读写RAM设计(hairuoyouying提供)
- **类型**: 编程题　**难度**: 中等

**参考答案**:

```verilog
module top_module(
    input           clk_i   ,
    input           rst_i   ,
    input           wr_en_i ,
    input           rd_en_i ,
    input   [3:0]   addr_i  ,
    inout   [7:0]   data_io
    );

    reg [7:0] mem [0:255];
    always @(posedge clk) begin
        if (wr_en) mem[addr] <= wr_data;
    end
    assign rd_data = mem[addr];

endmodule
```

---

### 311. rom设计(hairuoyouying提供)
- **类型**: 编程题　**难度**: 中等

**参考答案**:

```verilog
module top_module#(parameter WIDTH=8,DEPTH=16)
(
    input               clk     ,
    input               rst     ,
    input               cs      ,
    input               read_en ,
    input   [3:0]       addr    ,
    output  [WIDTH-1:0] data
    );

    reg [7:0] mem [0:255];
    initial $readmemh("rom_init.hex", mem);
    assign rd_data = mem[addr];

endmodule
```

---

### 312. 二进制数与常数相乘(hairuoyouying提供)
- **类型**: 编程题　**难度**: 简单

**参考答案**:

```verilog
module top_module(
    input   [8:0]   x,
    output  [15:0]  p
    );

    assign p = x * CONSTANT;

endmodule
```

---

### 313. 4位加/减法器(hairuoyouying提供)
- **类型**: 编程题　**难度**: 简单

**参考答案**:

```verilog
module top_module(
    input   [3:0]   a,
    input   [3:0]   b,
    input           e,
    output  [3:0]   y,
    output          co
    );

    always @(*) begin
        if (sub) {cout, y} = a - b;
        else {cout, y} = a + b;
    end

endmodule
```

---

### 314. 用与非门构成非门(hairuoyouying提供)
- **类型**: 编程题　**难度**: 简单

**参考答案**:

```verilog
module top_module(
    input   a,
    output  y
    );

    // 用与非门构成非门(hairuoyouying提供) - 请根据题目描述完善组合逻辑

endmodule
```

---

### 315. 74LS253的IP核设计及应用(hairuoyouying提供)
- **类型**: 编程题　**难度**: 简单

**参考答案**:

```verilog
module top_module(
    input A,B,  //S1,S0
    input G1_n,G2_n,
    input D1_3,D1_2,D1_1,D1_0,
    input D2_3,D2_2,D2_1,D2_0,
    output Y1,Y2
    );

    // 74LS253的IP核设计及应用(hairuoyouying提供) - 请根据题目描述完善组合逻辑

endmodule
```

---

### 316. 74LS151的IP核设计(hairuoyouying提供)
- **类型**: 编程题　**难度**: 简单

**参考答案**:

```verilog
module top_module(
    input   G_n,
    input   S2,S1,S0,
    input   D7,D6,D5,D4,D3,D2,D1,D0,
    output  Y,Y_n
    );

    // 74LS151的IP核设计(hairuoyouying提供) - 请根据题目描述完善组合逻辑

endmodule
```

---

### 317. 使用关系运算符实现N位无符号数值比较器(hairuoyouying提供)
- **类型**: 编程题　**难度**: 简单

**参考答案**:

```verilog
module top_module
#(parameter N=4)
(
    input wire [N-1:0] x,
    input wire [N-1:0] y,
    output reg gt,
    output reg eq,
    output reg lt
    );

    // 使用关系运算符实现N位无符号数值比较器(hairuoyouying提供) - 请根据题目描述完善逻辑

endmodule
```

---

### 318. for循环的简单应用(hairuoyouying提供)
- **类型**: 编程题　**难度**: 简单

**参考答案**:

```verilog
module top_module(
    input wire [2:0] a,
    output reg [7:0] y
    );

    // for循环的简单应用(hairuoyouying提供) - 请根据题目描述完善组合逻辑

endmodule
```

---

### 319. for循环的简单应用2(hairuoyouying提供)
- **类型**: 编程题　**难度**: 简单

**参考答案**:

```verilog
module top_module(
    input wire [7:0] x, 
    output reg [2:0] y, 
    output reg valid
    );

    // for循环的简单应用2(hairuoyouying提供) - 请根据题目描述完善组合逻辑

endmodule
```

---

### 320. 8位二进制-bcd码转换(hairuoyouying提供)
- **类型**: 编程题　**难度**: 简单

**参考答案**:

```verilog
module top_module(
    input wire [7:0] b,
    output reg [9:0] p
    );

    // 8位二进制-bcd码转换(hairuoyouying提供) - 请根据题目描述完善组合逻辑

endmodule
```

---

### 321. 全减器(hairuoyouying提供)
- **类型**: 编程题　**难度**: 简单

**参考答案**:

```verilog
module top_module(
    input wire a, b, ci,
    output reg d, co
    );

    always @(*) {cout, sum} = a - b - cin;

endmodule
```

---

### 322. 数字时钟(FXS531456提供)
- **类型**: 编程题　**难度**: 困难

**参考答案**:

```verilog
module top_module(
    input   clk ,
    input   rst_n   ,
    output  reg [7:0]   dis_sel,
    output  reg [7:0]   dis_seg0,
    output  reg [7:0]   dis_seg1
）；

///////////    your code    ///////////

///////////    your code    ///////////

endmodule

    reg [5:0] sec, min;
    reg [4:0] hour;
    always @(posedge clk) begin
        if (rst) begin sec <= 0; min <= 0; hour <= 0; end
        else begin
            if (sec == 59) begin
                sec <= 0;
                if (min == 59) begin min <= 0; hour <= hour + 1; end
                else min <= min + 1;
            end else sec <= sec + 1;
        end
    end
    assign sec_ones = sec % 10;
    assign sec_tens = sec / 10;
    assign min_ones = min % 10;
    assign min_tens = min / 10;
    assign hour_ones = hour % 10;
    assign hour_tens = hour / 10;

endmodule
```

---

### 323. 状态机实现按键检测(FXS046592提供)
- **类型**: 编程题　**难度**: 简单

**参考答案**:

```verilog
module top_module(
    input       clk  ,
    input       rst  ,
    input       key0 ,
    output  reg [4:0] led
    );

    parameter S0 = 2'b00, S1 = 2'b01, S2 = 2'b10;
    reg [1:0] state, next;
    always @(posedge clk) state <= next;
    always @(*) begin
        next = S0; out = 0;
        case (state)
            S0: next = din ? S1 : S0;
            S1: begin next = din ? S1 : S2; out = 1; end
            S2: next = din ? S1 : S0;
        endcase
    end

endmodule
```

---

### 324. 流水灯板端实验
- **类型**: 编程题　**难度**: 简单

**参考答案**:

```verilog
module top_module(
    input               clk,//10Mhz
    input               rst_n,//高有效异步复位
    output  reg [7:0]   led //输出10000000循环右移，0.5s位移一次               
);

    reg [31:0] cnt;
    always @(posedge clk) begin
        if (rst) begin cnt <= 0; led <= 8'b00000001; end
        else begin
            if (cnt == 49999999) begin cnt <= 0; led <= {led[6:0], led[7]}; end
            else cnt <= cnt + 1;
        end
    end

endmodule
```

---

### 325. 半加器板端实验
- **类型**: 编程题　**难度**: 简单

**参考答案**:

```verilog
module top_module(
      input     x   ,
      input     y   ,
      output    sum ,
      output    c_out);

    // 半加器板端实验 - 请根据题目描述完善组合逻辑

endmodule
```

---

### 326. 简易数字信号发生器设计
- **类型**: 编程题　**难度**: 中等

**参考答案**:

```verilog
verilog
module top_module(
    input         clk,        // 50MHz系统时钟，上升沿触发
    input         rst,        // 同步复位，高电平有效
    input  [1:0]  wave_sel,   // 波形选择：00=方波、01=三角波、10=锯齿波、11=脉冲波
    input  [1:0]  freq_sel,   // 频率选择：00=1kHz、01=5kHz、10=10kHz、11=20kHz
    output reg [7:0] dout,    // 8位数字信号输出
    output reg    valid       // 信号有效标志，高有效
);

    reg [1:0] cnt;
    always @(posedge clk) begin
        if (rst) cnt <= 0;
        else cnt <= cnt + 1;
    end
    always @(*) begin
        case (cnt)
            2'd0: begin p0=1; p1=0; p2=0; p3=0; end
            2'd1: begin p0=0; p1=1; p2=0; p3=0; end
            2'd2: begin p0=0; p1=0; p2=1; p3=0; end
            2'd3: begin p0=0; p1=0; p2=0; p3=1; end
        endcase
    end

endmodule
```

---

## 四、硬件题 (19 道)

### 327. 流水灯板端实验
- **类型**: 硬件题　**难度**: 简单

**参考答案**:

```verilog
module flash_led(
  input            clk,
  input            rst_n,
  output reg [7:0] led
);

    reg [31:0] cnt;
    always @(posedge clk) begin
        if (rst) begin cnt <= 0; led <= 8'b00000001; end
        else begin
            if (cnt == 49999999) begin cnt <= 0; led <= {led[6:0], led[7]}; end
            else cnt <= cnt + 1;
        end
    end

endmodule
```

---

### 328. 开关控制数码管
- **类型**: 硬件题　**难度**: 简单

**参考答案**:

```verilog
module top_module(
    input           clk     ,
    input           rst_n   ,
    input       [7:0]   switch  ,
    output reg  [7:0]   dis_sel ,   //
    output reg  [7:0]   dis_seg0,   //
    output reg  [7:0]   dis_seg1,   //
    output      [7:0]   led 
    );

    // 开关控制数码管 - 请根据题目描述完善时序逻辑

endmodule
```

---

### 329. 按键控制数码管
- **类型**: 硬件题　**难度**: 简单

**参考答案**:

```verilog
module bnt_led(
input clk,
input [1:0]key_in,
input rst_n,
output [3:0]seg1,
output reg [7:0]seg_led1
    );

    // 按键控制数码管 - 请根据题目描述完善时序逻辑

endmodule
```

---

### 330. 数字时钟
- **类型**: 硬件题　**难度**: 中等

**参考答案**:

```verilog
module clk_digital(
  input clk ,
  input rst ,
  input start,//开始
  
  output [5:0]  dig_sel,   //数码管位选
  output [7:0]  dig_led,   //数码管段选
  output [7:0]  dig_led0,  //数码管段选
  output        led        //倒计时闪烁
);

    reg [5:0] sec, min;
    reg [4:0] hour;
    always @(posedge clk) begin
        if (rst) begin sec <= 0; min <= 0; hour <= 0; end
        else begin
            if (sec == 59) begin
                sec <= 0;
                if (min == 59) begin min <= 0; hour <= hour + 1; end
                else min <= min + 1;
            end else sec <= sec + 1;
        end
    end
    assign sec_ones = sec % 10;
    assign sec_tens = sec / 10;
    assign min_ones = min % 10;
    assign min_tens = min / 10;
    assign hour_ones = hour % 10;
    assign hour_tens = hour / 10;

endmodule
```

---

### 331. 交通灯
- **类型**: 硬件题　**难度**: 中等

**参考答案**:

```verilog
module traffic_light(
input clk,  //时钟
input rst,  //复位
input start,//开始

output [2:0] trunk_led,branch_led,//主干道路灯，支干道路灯
output [3:0] dig_sel,  //数码管位选
output [7:0] dig_led   //数码管段选
);

    // 交通灯 - 请根据题目描述完善时序逻辑

endmodule
```

---

### 332. 自动售卖机
- **类型**: 硬件题　**难度**: 中等

**参考答案**:

```verilog
module vend(
    input           clk     ,
    input           rst     ,
    input   [2:0]   i_rmb   ,
    output  [2:0]   o_rmb   ,
    output          o_valid 
    );

    // 自动售卖机 - 请根据题目描述完善时序逻辑

endmodule
```

---

### 333. VGA控制器
- **类型**: 硬件题　**难度**: 中等

**参考答案**:

```verilog
module vga_top(
input         sys_clk   ,     //100M
input         sys_rst_n ,     //系统复位

output        hsync     ,     //行同步信号
output        vsync     ,     //场同步信号
output [3:0]  vga_r     ,     //像素信号 
output [3:0]  vga_g     ,     //像素信号
output [3:0]  vga_b           //像素信号



);

    // VGA控制器 - 请根据题目描述完善时序逻辑

endmodule
```

---

### 334. 基于VGA接口的静态图像显示设计
- **类型**: 硬件题　**难度**: 中等

**参考答案**:

```verilog
module vga_top(
input         sys_clk   ,     //100M
input         sys_rst_n ,     //系统复位

output        hsync     ,     //行同步信号
output        vsync     ,     //场同步信号
output [3:0]  vga_r     ,     //像素信号 
output [3:0]  vga_g     ,     //像素信号
output [3:0]  vga_b           //像素信号

);

    // 基于VGA接口的静态图像显示设计 - 请根据题目描述完善时序逻辑

endmodule
```

---

### 335. 基于HDMI接口的彩条显示设计
- **类型**: 硬件题　**难度**: 困难

**参考答案**:

```verilog
module top_module(


);

    // 基于HDMI接口的彩条显示设计 - 请根据题目描述完善组合逻辑

endmodule
```

---

### 336. 基于RISC-V架构的单周期CPU设计与实现
- **类型**: 硬件题　**难度**: 困难

**参考答案**:

```verilog
module top_module(



);

    // 基于RISC-V架构的单周期CPU设计与实现 - 请根据题目描述完善组合逻辑

endmodule
```

---

### 337. 基于RISC-V架构的多周期CPU设计与实现
- **类型**: 硬件题　**难度**: 困难

**参考答案**:

```verilog
module top_module(


);

    // 基于RISC-V架构的多周期CPU设计与实现 - 请根据题目描述完善组合逻辑

endmodule
```

---

### 338. 基于I2S协议的音频接口系统设计与实现
- **类型**: 硬件题　**难度**: 困难

**参考答案**:

```verilog
module top_module(



);

    // 基于I2S协议的音频接口系统设计与实现 - 请根据题目描述完善组合逻辑

endmodule
```

---

### 339. 基于FPGA的I2C接口控制器设计与实现
- **类型**: 硬件题　**难度**: 中等

**参考答案**:

```verilog
module top_module(


);

    // 基于FPGA的I2C接口控制器设计与实现 - 请根据题目描述完善组合逻辑

endmodule
```

---

### 340. 基于FPGA的I2S音频接口控制器设计与实现
- **类型**: 硬件题　**难度**: 中等

**参考答案**:

```verilog
module top_module(


  );

    // 基于FPGA的I2S音频接口控制器设计与实现 - 请根据题目描述完善组合逻辑

endmodule
```

---

### 341. 基于FPGA的SPI接口控制器设计与实现
- **类型**: 硬件题　**难度**: 中等

**参考答案**:

```verilog
module top_module(


  );

    // 基于FPGA的SPI接口控制器设计与实现 - 请根据题目描述完善组合逻辑

endmodule
```

---

### 342. 基于FPGA的UART串口通信系统设计与实现
- **类型**: 硬件题　**难度**: 简单

**参考答案**:

```verilog
module top_module(



);

    // 基于FPGA的UART串口通信系统设计与实现 - 请根据题目描述完善组合逻辑

endmodule
```

---

### 343. 基于FPGA的数字PID控制器设计与实现
- **类型**: 硬件题　**难度**: 中等

**参考答案**:

```verilog
module flash_led_top(


);

    // 基于FPGA的数字PID控制器设计与实现 - 请根据题目描述完善组合逻辑

endmodule
```

---

### 344. 基于FPGA的OLED显示屏字符显示设计
- **类型**: 硬件题　**难度**: 中等

**参考答案**:

```verilog
module flash_led_top(


);

    // 基于FPGA的OLED显示屏字符显示设计 - 请根据题目描述完善组合逻辑

endmodule
```

---

### 345. 流水灯（ego2）
- **类型**: 硬件题　**难度**: 简单

**参考答案**:

```verilog
module led(

);

    reg [31:0] cnt;
    always @(posedge clk) begin
        if (rst) begin cnt <= 0; led <= 8'b00000001; end
        else begin
            if (cnt == 49999999) begin cnt <= 0; led <= {led[6:0], led[7]}; end
            else cnt <= cnt + 1;
        end
    end

endmodule
```

---
