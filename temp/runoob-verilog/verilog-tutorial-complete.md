# 菜鸟教程 - Verilog 教程（完整版）
> 来源: https://www.runoob.com/w3cnote/verilog-tutorial.html
> 共 35 章节

## 目录

1. 1.2 Verilog 简介
2. 1.3 Verilog 环境搭建
3. 2.1 Verilog 基础语法
4. 2.3 Verilog 数据类型
5. 2.2 Verilog 数值表示
6. 8.1 Verilog 数值转换
7. 2.4 Verilog 表达式
8. 5.1 Verilog 模块与端口
9. 3.1 Verilog 连续赋值
10. 4.8 Verilog 过程连续赋值
11. 4.5 Verilog 条件语句
12. 4.6 Verilog 多路分支语句
13. 4.7 Verilog 循环语句
14. 4.4 Verilog 语句块
15. 3.2 Verilog 时延
16. 4.3 Verilog 时序控制
17. 4.2 Verilog 过程赋值
18. 4.1 Verilog 过程结构
19. 6.1 Verilog 函数
20. 6.2 Verilog 任务
21. 2.5 Verilog 编译指令
22. 5.3 Verilog 带参数例化
23. 5.2 Verilog 模块例化
24. 6.6 Verilog 仿真激励
25. 1.4 Verilog 设计方法
26. 6.5 Verilog 避免 Latch
27. 6.4 Verilog 竞争与冒险
28. 6.3 Verilog 状态机
29. 6.7 Verilog 流水线
30. 7.2 Verilog 并行 FIR 滤波器设计
31. 7.3 Verilog 串行 FIR 滤波器设计
32. 7.4 Verilog CIC 滤波器设计
33. 7.6 Verilog DDS 设计
34. 7.5 Verilog FFT 设计
35. 7.1 Verilog 除法器设计

---


---

## 1. 1.2 Verilog 简介

Verilog 具有很强的电路描述与建模能力，能从多个层次对数字系统进行描述和建模。因此，在简化硬件设计任务、提高设计效率与可靠性、语言易读性、层次化和结构化设计等方面展现了强大的生命力与潜力。



### 发展历史


- 
1983 年，Verilog 最初由 Gateway Design Automation 公司（GDA）的 Phil Moorby 创建，作为内部仿真器的语言，主要用于逻辑建模和仿真验证，被广泛使用。
- 
1989 年，GDA 公司被 Cadence 公司收购，Verilog 语言成为 Cadence 公司的私有财产。
- 
1990 年，Cadence 公司成立 OVI（Open Verilog International）组织，公开 Verilog 语言，促进 Verilog 向公众领域发展。
- 
1992 年，OVI 决定致力于将 Verilog OVI 标准推广为 IEEE（The Institute of Electrical and Electronics Engineers）标准。
- 
1995 年，OVI 的努力获得成功，IEEE 制定了 Verilog HDL 的第一个国际标准，即 IEEE Std 1364-1995，也称之为 Verilog 1.0。
- 
2001 年，IEEE 发布 Verilog 第二个标准（Verilog 2.0），即 IEEE Std 1364-2001, 简称为 Verilog-2001 标准。由于 Cadence 在集成电路设计领域的影响力及 Verilog 语言的简洁易用性，Verilog 成为电路设计中最流行的硬件描述语言。


### 主要特性


下面是 Verilog 的主要特性：
- 
可采用 3 种不同的方式进行设计建模：行为级描述——使用过程化结构建模；数据流描述——使用连续赋值语句建模；结构化方式——使用门和模块例化语句描述。

- 两类数据类型：线网（wire）数据类型与寄存器（reg）数据类型，线网表示物理元件之间的连线，寄存器表示抽象的数据存储元件。

- 能够描述层次设计，可使用模块实例化描述任何层次。

- 用户定义原语（UDP）创建十分灵活。原语既可以是组合逻辑，也可以是时序逻辑。

- 可提供显示语言结构指定设计中的指定端口到端口的时延，以及路径时延和时序检查。

- Verilog 支持其他编程语言接口（PLI）进行进一步扩展。PLI 允许外部函数访问 Verilog 模块内部信息，为仿真提供了更加丰富的测试方法。

- 同一语言可用于生成模拟激励和指定测试的约束条件。

- 设计逻辑功能时，设计者可不用关心不影响逻辑功能的因素，例如工艺、温度等。

- ……

### 主要应用


专用集成电路（ASIC），就是具有专门用途和特殊功能的独立集成电路器件。

Verilog 作为硬件描述语言，主要用来生成专用集成电路。

主要通过 3 个途径来完成：

**1、可编程逻辑器件**

FPGA 和 CPLD 是实现这一途径的主流器件。他们直接面向用户，具有极大的灵活性和通用性，实现快捷，测试方便，开发效率高而成本较低。

**2、半定制或全定制 ASIC**


通俗来讲，就是利用 Verilog 来设计具有某种特殊功能的专用芯片。根据基本单元工艺的差异，又可分为门阵列 ASIC，标准单元 ASIC，全定制 ASIC。

**3、混合 ASIC**

主要指既具有面向用户的 FPGA 可编程逻辑功能和逻辑资源，同时也含有可方便调用和配置的硬件标准单元模块，如CPU，RAM，锁相环，乘法器等。

---

## 2. 1.3 Verilog 环境搭建

学习 Verilog 做仿真时，可选择不同仿真环境。FPGA 开发环境有 Xilinx 公司的 ISE（目前已停止更新），VIVADO；因特尔公司的 Quartus II；ASIC 开发环境有 Synopsys 公司的 VCS ；很多人也在用 Icarus Verilog 和 GTKwave 的方法，更加的轻便。


虽然 ISE 或者 Quartus II 都会自带仿真器，但功能还是有欠缺。所以，这里介绍下 Quartus II + Modelsim 联合仿真的测试方法，运行环境为 64bit-win10 系统。

### Quartus II 安装


本次介绍使用的 Quartus 版本为 10.1。



目前 Quartus II 官网已经没有 13.1 以下版本的安装包，大家可以安装 13.1 以上版本的软件。功能都是大同小异，下载地址：[https://fpgasoftware.intel.com/13.1/?edition=subscription&platform=windows](https://fpgasoftware.intel.com/13.1/?edition=subscription&platform=windows)


下载 13.1 以上的 quartus II 时，官网也会推荐相应版本的 Modelsim，一起下载即可。


开始安装，修改安装路径，其他按照默认设置一步步操作即可。

下图是成功安装的截图。

![](https://www.runoob.com/wp-content/uploads/2020/09/vlg-install-1.png)


如果提示需要 License file，如下图所示，则需要指定购买该软件时的 license 文件。

![](https://www.runoob.com/wp-content/uploads/2020/09/vlg-install-2.png)


如果 license 文件需要替换 Host-ID，只需要 license 文件中的 HOSTID 替换为 NIC 选项中随便一个 ID 即可，如下图红色框所示：

![](https://www.runoob.com/wp-content/uploads/2020/09/vlg-install-3.png)


Quartus II 10.1 安装完还需要安装 Device，即安装支持各种可编程逻辑器件型号的库文件，否则 Quartus II 不能正常建立工程。


安装路径需要选择 Quartus II 的安装路径，此时 Device 安装可自动识别 Quartus II。

最新 Quartus II（例如 2016 版本）已经支持一套化安装了。


### Modelsim 安装


Modelsim 选择 modelsim-win64-10.1c-se 版本。


也需要修改下安装路径，然后按照默认设置进行操作即可。


安装完毕后可能提示需要重启电脑，重启即可。

![](https://www.runoob.com/wp-content/uploads/2020/09/vlg-install-4.png)



### 建立 Quartus II 工程


**建立工程**

File->New project Wizard


设置工作路径与工程名字、top module名字。


注意，路径与名字设置时，不能包含中文。

![](https://www.runoob.com/wp-content/uploads/2020/09/vlg-install-5.png)



**选择器件型号**


我们只进行简单的仿真，不进行下载、烧录等，所以我们不用关心具体信号，随便选一种即可。


然后一直点击 Next，直到 Finish。

![](https://www.runoob.com/wp-content/uploads/2020/09/vlg-install-6.png)



**新建 Verilog 源文件**

下面就对 4 位宽 10 进制计数器进行简单的仿真。

点击：File->New->Verilog HDL File->OK


点击：File->Save As


输入 module 名字为：counter10.v

需要注意的是，top module 名字一定要和 project 名字一致，否则会报错（如图中所示）。


把 Verilog 代码复制到文件 counter10.v 中，进行一键编译（实际包含了编译、综合、布局布线等）。


报错时，可通过点击 Error log 来定位错误，进行修改，直至没有 Error。

![](https://www.runoob.com/wp-content/uploads/2020/09/vlg-install-7.png)



### Quartus II 调用 Modelsim 仿真


仿真设置为 Modelsim-altera

点击：Tool->Options->EDA Tool Options

将 Modelsim 后面的地址改为 Modelsim 启动程序的路径。

![](https://www.runoob.com/wp-content/uploads/2020/09/vlg-install-8.png)



**选择仿真器**

点击：Assignments -> Simulation


Tool name 选择 ModelSim，并设置 Format、Time scale 等，如图。。

![](https://www.runoob.com/wp-content/uploads/2020/09/vlg-install-9.png)



**写 testbench 文件**

点击：Processing->start->Start TestBench Template Writer


如果设置正确，会在工程路径 simulation/modelsim 下产生 .vt 文件。

.vt 文件模板已经给出了端口部分的代码、接口变量的声明和例化语句映射等。我们要做的就是将测试代码填入到 testbench 合适的位置。


这里简单的写一下时钟、复位驱动代码，如下图所示。

![](https://www.runoob.com/wp-content/uploads/2020/09/vlg-install-10.png)



**将 testbench 添加到工程中**

点击：Assignments -> Settings -> Simulation

在 Compile test bench 选项中，选择 new，设置 Test bench name，并通过 File name 查找的方式，将上一步生成的 .vt 文件添加到工程中。


需要注意的是，testbench 文件名字需要和 testbench 里的 top module 名字保持一致，否则后续启动 Modelsim 时会报错，不能进行正常的仿真。

![](https://www.runoob.com/wp-content/uploads/2020/09/XFejkqOFS8VYO1jL.png)



**重新一键编译**


此时，你会发现，Tasks 栏编译的状态变成了问号，需要重新进行一键编译。

![](https://www.runoob.com/wp-content/uploads/2020/09/vlg-install-12.png)



**调用 Modelsim 仿真**


点击：Tools->Run simulation Tool->RTL Simulation

这时就会自动启动 Modelsim 软件。

Modelsim 操作这里不做具体介绍。


由仿真图可知，我们的设计完成了 10 进制计数的基本功能。

![](https://www.runoob.com/wp-content/uploads/2020/09/vlg-install-13.png)




## 总结


记忆中，Quartus II + Modelsim 的联合仿真功能既强大，又安装方便。几年后重新进行此过程，发现步骤也有些许繁琐，花费了我一晚上的时间来搞定。很多细节也在上面提出，多多注意就好。不过，大家以后有机会进行大型的数字模块仿真时，就会发现此方法的有效性。


在接下来的教程里，有些简单的仿真可能用其他软件进行，截图界面可能与 Modelsim 不一致。大家看到后不用怀疑仿真的准确性，这里特别说明。


设计模块与 testbench 源码也会全部给出，大家完全可以自己仿真、验证。

---

## 3. 2.1 Verilog 基础语法

### 格式


Verilog 是区分大小写的。

格式自由，可以在一行内编写，也可跨多行编写。


每个语句必须以分号为结束符。空白符（换行、制表、空格）都没有实际的意义，在编译阶段可忽略。例如下面两中编程方式都是等效的。

**不换行（不推荐）**

## 实例
 
wire &#91;1:0&#93; results ;assign results = &#40;a == 1'b0&#41; ? 2'b01 ： &#40;b==1'b0&#41; ? 2'b10 ： 2'b11 ;

---

## 4. 2.3 Verilog 数据类型

Verilog 最常用的 2 种数据类型就是线网（wire）与寄存器（reg），其余类型可以理解为这两种数据类型的扩展或辅助。



### 线网（wire）



wire 类型表示硬件单元之间的物理连线，由其连接的器件输出端连续驱动。如果没有驱动元件连接到 wire 型变量，缺省值一般为 "Z"。举例如下：




## 实例
 
wire interrupt ;

wire flag1, flag2 ;

wire gnd = 1'b0 ;

---

## 5. 2.2 Verilog 数值表示

### 数值种类


Verilog HDL 有下列四种基本的值来表示硬件电路中的电平逻辑：

- 
0：逻辑 0 或 "假"
- 
1：逻辑 1 或 "真"
- 
x 或 X：未知
- 
z 或 Z：高阻
 

x 意味着信号数值的不确定，即在实际电路里，信号可能为 1，也可能为 0。

z 意味着信号处于高阻状态，常见于信号（input, reg）没有驱动时的逻辑结果。例如一个 pad 的 input 呈现高阻状态时，其逻辑值和上下拉的状态有关系。上拉则逻辑值为 1，下拉则为 0 。


### 整数数值表示方法


数字声明时，合法的基数格式有 4 中，包括：十进制('d 或 'D)，十六进制('h 或 'H)，二进制（'b 或 'B），八进制（'o 或 'O）。数值可指明位宽，也可不指明位宽。

**指明位宽：**

## 实例
 
4'b1011 // 4bit 数值

32'h3022_c0de // 32bit 的数值

---

## 6. 8.1 Verilog 数值转换

本节主要对有符号数的十进制与二进制表示以及一些数值变换进行简单的总结。


定义一个宽度为 DW 的二进制补码格式的数据 dbin ，其表示的有符号十进制数字为 ddec 。

```
reg [DW-1:0] dbin ;
```



### 1. 十进制有符号数转二进制补码


正数的补码为原码。


假如十进制数 ddec 为负数，则计算其对应的二进制补码的方法主要有 2 种：


**将ddec 最高位符号位改写为 1，剩余数值部分取反加一**


例如，4bit 数字 -6 的数值部分为 4'b0110，取反加一后为 4'b0010，高位改写后为 4'b1010。

```
dbin = {1'b1, ~3'b110 + 3'b1} ; //4'b1010
```



**将负数 ddec 直接与其代表的最大数值范围数相加（有人称之为模数）**


例如，4bit 数字 -6 与 16（2 的 4 次幂）的和为 10， 即对应 4'b1010。

```
dbin = ddec + (1<<4) ; //4'b1010
```



### 2. 二级制补码转十进制有符号数


当 dbin 最高位为 0 时，其数值大小即为其表示的十进制正数。


当 dbin 最高位为 1 时，计算其表示的十进制有符号数方法主要有 2 种：


**将 dbin 取反加一，并增加符号位**

例如，4bit 数字 -6 的补码为 4'b1010，取反加一后为 4'b0110，增加符号位后为 -6。

```
ddec = -(~4'b1010 + 1'b1) ; //-6
```


**
将 dbin 代表的无符号数值与其代表的最大数值范围数直接相减**


例如，4bit 数字 -6 的补码为 4'b1010，即无符号数值为 10，10 减 16 便可得到 -6 。

```
ddec = dbin - (1<<4) ; //-6
```



### 3. 绝对值


求 dbin 的绝对值逻辑如下：

```
dbin_abs = (dbin[DW-1]? ~dbin : dbin) + 1'b1 ;
```


例如，4bit 数字 -6 的补码为 4'b1010，取反加 1 后的值为 4'b0110（6），即为 -6 的绝对值。


但如果 dbin 为正数，加 1 后的值比其真正的绝对值要大 1，此步操作只是为了让正数部分的绝对值数量与负数部分一致。因为一定位宽下，由于 0 值的存在，有符号数表示的负数数量会比正数多 1 个。

### 4. 有符号数转无符号数


将有符号数扩展成为无符号数的逻辑如下：

```
dbin_unsigned = {!dbin[DW-1], dbin[DW-2:0]) ;
```


例如： 
```
4'b1010 (-6) -> 4'b0010 (2)，4'b0010 (2) -> 4'b1010 (10)
```


其实转换原则是将数据代表的数值范围移动到 0 以上，有符号数转换成无符号数之后，数据相对间的差并没有改变。

### 5. 扩展符号位


计算时有时会根据需要对有符号数位宽进行扩展。假设位宽增量为 W，扩展逻辑如下：

```
dbin_extend = {{(W){dbin[DW-1]}}, dbin} ;
```


扩展原则就是将信号代表符号位的最高位，填充至扩展的高位数据位中。

例如 4'b1010 (-6) 扩展到 8bit 为 8'b11111010，计算其对应的负数仍然是 -6。

---

## 7. 2.4 Verilog 表达式

### 表达式


表达式由操作符和操作数构成，其目的是根据操作符的意义得到一个计算结果。表达式可以在出现数值的任何地方使用。例如：


## 实例
 
a^b ; //a与b进行异或操作

address&#91;9:0&#93; + 10'b1 ; //地址累加

flag1 && flag2 ; //逻辑与操作

---

## 8. 5.1 Verilog 模块与端口

### 关键词：模块，端口，双向端口，PAD


结构建模方式有 3 类描述语句： Gate（门级）例化语句，UDP (用户定义原语)例化语句和 module (模块) 例化语句。本次主要讲述使用最多的模块级例化语句。

### 模块


模块是 Verilog 中基本单元的定义形式，是与外界交互的接口。

模块格式定义如下：

```
module module_name 
#(parameter_list)
(port_list) ;
 Declarations_and_Statements ;
endmodule
```



模块定义必须以关键字 module 开始，以关键字 endmodule 结束。


模块名，端口信号，端口声明和可选的参数声明等，出现在设计使用的 Verilog 语句（图中 Declarations_and_Statements）之前。


模块内部有可选的 5 部分组成，分别是变量声明，数据流语句，行为级语句，低层模块例化及任务和函数，如下图表示。这 5 部分出现顺序、出现位置都是任意的。但是，各种变量都应在使用之前声明。变量具体声明的位置不要求，但必须保证在使用之前的位置。

![](https://www.runoob.com/wp-content/uploads/2020/09/jxRkciGWpiEbvz3D.png)



前面大多数仿真代码都会用到 module 声明，大家可以自行参考，这里不再做具体举例。下面介绍端口时，再做详细的仿真。


### 端口


端口是模块与外界交互的接口。对于外部环境来说，模块内部是不可见的，对模块的调用只能通过端口连接进行。


**端口列表**


模块的定义中包含一个可选的端口列表，一般将不带类型、不带位宽的信号变量罗列在模块声明里。下面是一个 PAD 模型的端口列表：

```
module pad(
 DIN, OEN, PULL,
 DOUT, PAD);
```


一个模块如果和外部环境没有交互，则可以不用声明端口列表。例如之前我们仿真时 test.sv 文件中的 test 模块都没有声明具体端口。

```
module test ; //直接分号结束
 ...... //数据流或行为级描述
endmodule
```



**端口声明**


(1) 端口信号在端口列表中罗列出来以后，就可以在模块实体中进行声明了。


根据端口的方向，端口类型有 3 种： 输入（input），输出（output）和双向端口（inout）。


input、inout 类型不能声明为 reg 数据类型，因为 reg 类型是用于保存数值的，而输入端口只能反映与其相连的外部信号的变化，不能保存这些信号的值。


output 可以声明为 wire 或 reg 数据类型。


上述例子中 pad 模块的端口声明，在 module 实体中就可以表示如下：

## 实例
 
//端口类型声明

input DIN, OEN ;

input &#91;1:0&#93; PULL ; //(00,01-dispull, 11-pullup, 10-pulldown)

inout PAD ; //pad value

output DOUT ; //pad load when pad configured as input

//端口数据类型声明

wire DIN, OEN ;

wire &#91;1:0&#93; PULL ;

wire PAD ;

reg DOUT ;

---

## 9. 3.1 Verilog 连续赋值

### 关键词：assign， 全加器


连续赋值语句是 Verilog 数据流建模的基本语句，用于对 wire 型变量进行赋值。：

格式如下

```
assign LHS_target = RHS_expression ；
```
 

LHS（left hand side） 指赋值操作的左侧，RHS（right hand side）指赋值操作的右侧。


assign 为关键词，任何已经声明 wire 变量的连续赋值语句都是以 assign 开头，例如：

```
wire Cout, A, B ;
assign Cout = A & B ; //实现计算A与B的功能
```


需要说明的是：

- 
LHS_target 必须是一个标量或者线型向量，而不能是寄存器类型。
- 
RHS_expression 的类型没有要求，可以是标量或线型或存器向量，也可以是函数调用。
- 
只要 RHS_expression 表达式的操作数有事件发生（值的变化）时，RHS_expression 就会立刻重新计算，同时赋值给 LHS_target。
 

Verilog 还提供了另一种对 wire 型赋值的简单方法，即在 wire 型变量声明的时候同时对其赋值。wire 型变量只能被赋值一次，因此该种连续赋值方式也只能有一次。例如下面赋值方式和上面的赋值例子的赋值方式，效果都是一致的。

```
wire A, B ;
wire Cout = A & B ;
```


### 全加器


下面采用数据流描述方式，来设计一个 1bit 全加器。


设 Ai，Bi，Ci 分别为被加数、加数和相邻低位的进位数，So, Co 分别为本位和与向相邻高位的进位数。


真值表如下：

| Input | | | Output | | 
| Ci | Ai | Bi | So | Co | 
| 0 | 0 | 0 | 0 | 0 | 
| 0 | 0 | 1 | 1 | 0 | 
| 0 | 1 | 0 | 1 | 0 | 
| 0 | 1 | 1 | 0 | 1 | 
| 1 | 0 | 0 | 1 | 0 | 
| 1 | 0 | 1 | 0 | 1 | 
| 1 | 1 | 0 | 0 | 1 | 
| 1 | 1 | 1 | 1 | 1 | 

全加器的表达式为：

```
So = Ai &oplus; Bi &oplus; Ci ;
Co = AiBi + Ci(Ai+Bi)
```



rtl 代码（full_adder1.v）如下：

## 实例
 
module full_adder1&#40;

 input Ai, Bi, Ci,

 output So, Co&#41;;

 

 assign So = Ai ^ Bi ^ Ci ;

 assign Co = &#40;Ai & Bi&#41; | &#40;Ci & &#40;Ai | Bi&#41;&#41;;

endmodule

---

## 10. 4.8 Verilog 过程连续赋值

### 关键词：deassign，force，release


过程连续赋值是过程赋值的一种。这种赋值语句能够替换其他所有 wire 或 reg 的赋值，改写了 wire 或 reg 型变量的当前值。


与过程赋值不同的是，过程连续赋值的表达式能被连续的驱动到 wire 或 reg 型变量中，即过程连续赋值发生作用时，右端表达式中任意操作数的变化都会引起过程连续赋值语句的重新执行。


过程连续性赋值主要有 2 种，assign-deassign 和 force-release。


### assign, deassign


assign（过程赋值操作）与 deassign （取消过程赋值操作）表示第一类过程连续赋值语句。赋值对象只能是寄存器或寄存器组，而不能是 wire 型变量。


赋值过程中对寄存器连续赋值，寄存器中的值被保留直到被重新赋值。

例如，一个带复位端的 D 触发器可以用下面代码描述：

## 实例
 
module dff_normal&#40;

 input rstn,

 input clk,

 input D,

 output reg Q

 &#41;;

 always @&#40;posedge clk or negedge rstn&#41; begin

 if&#40;!rstn&#41; begin //Q = 0 after reset effective

 Q <= 1'b0 ;

 end

 else begin

 Q <= D ; //Q = D at posedge of clock

 end

 end

endmodule

---

## 11. 4.5 Verilog 条件语句

### 关键词：if，选择器


### 条件语句


条件（if）语句用于控制执行语句要根据条件判断来确定是否执行。

条件语句用关键字 if 和 else 来声明，条件表达式必须在圆括号中。

条件语句使用结构说明如下：


```
if (condition1) true_statement1 ;
else if (condition2) true_statement2 ;
else if (condition3) true_statement3 ;
else default_statement ;
```


- 
if 语句执行时，如果 condition1 为真，则执行 true_statement1 ；如果 condition1 为假，condition2 为真，则执行 true_statement2；依次类推。
- 
else if 与 else 结构可以省略，即可以只有一个 if 条件判断和一组执行语句 ture_statement1 就可以构成一个执行过程。
- 
else if 可以叠加多个，不仅限于 1 或 2 个。
- 
ture_statement1 等执行语句可以是一条语句，也可以是多条。如果是多条执行语句，则需要用 begin 与 end 关键字进行说明。

下面代码实现了一个 4 路选择器的功能。

## 实例
 
module mux4to1&#40;

 input &#91;1:0&#93; sel ,

 input &#91;1:0&#93; p0 ,

 input &#91;1:0&#93; p1 ,

 input &#91;1:0&#93; p2 ,

 input &#91;1:0&#93; p3 ,

 output &#91;1:0&#93; sout&#41;;

 reg &#91;1:0&#93; sout_t ;

 always @&#40;*&#41; begin

 if &#40;sel == 2'b00&#41;

 sout_t = p0 ;

 else if &#40;sel == 2'b01&#41;

 sout_t = p1 ;

 else if &#40;sel == 2'b10&#41;

 sout_t = p2 ;

 else

 sout_t = p3 ;

 end

 assign sout = sout_t ;

 

endmodule

---

## 12. 4.6 Verilog 多路分支语句

### 关键词：case，选择器


case 语句是一种多路条件分支的形式，可以解决 if 语句中有多个条件选项时使用不方便的问题。


### case 语句


case 语句格式如下：

```
case(case_expr)
 condition1 : true_statement1 ;
 condition2 : true_statement2 ;
 &hellip;&hellip;
 default : default_statement ;
endcase
```


case 语句执行时，如果 condition1 为真，则执行 true_statement1 ; 如果 condition1 为假，condition2 为真，则执行 true_statement2；依次类推。如果各个 condition 都不为真，则执行 default_statement 语句。

default 语句是可选的，且在一个 case 语句中不能有多个 default 语句。

条件选项可以有多个，不仅限于 condition1、condition2 等，而且这些条件选项不要求互斥。虽然这些条件选项是并发比较的，但执行效果是谁在前且条件为真谁被执行。

ture_statement1 等执行语句可以是一条语句，也可以是多条。如果是多条执行语句，则需要用 begin 与 end 关键字进行说明。

**case 语句支持嵌套使用。**

下面用 case 语句代替 if 语句实现了一个 4 路选择器的功能。仿真结果与 testbench 可参考[条件语句](https://www.runoob.com/w3cnote/verilog-condition-statement.html)一章，两者完全一致。

## 实例
 
module mux4to1&#40;

 input &#91;1:0&#93; sel ,

 input &#91;1:0&#93; p0 ,

 input &#91;1:0&#93; p1 ,

 input &#91;1:0&#93; p2 ,

 input &#91;1:0&#93; p3 ,

 output &#91;1:0&#93; sout&#41;;

 

 reg &#91;1:0&#93; sout_t ;

 always @&#40;*&#41;

 case&#40;sel&#41;

 2'b00: begin 

 sout_t = p0 ;

 end

 2'b01: sout_t = p1 ;

 2'b10: sout_t = p2 ;

 default: sout_t = p3 ;

 endcase

 assign sout = sout_t ;

 

endmodule

---

## 13. 4.7 Verilog 循环语句

### 关键词：while, for, repeat, forever


Verilog 循环语句有 4 种类型，分别是 while，for，repeat，和 forever 循环。循环语句只能在 always 或 initial 块中使用，但可以包含延迟表达式。


### while 循环


while 循环语法格式如下：

```
while (condition) begin
 &hellip;
end
```



while 循环中止条件为 condition 为假。

如果开始执行到 while 循环时 condition 已经为假，那么循环语句一次也不会执行。

当然，执行语句只有一条时，关键字 begin 与 end 可以省略。

下面代码执行时，counter 执行了 11 次。

## 实例
 
`timescale 1ns/1ns

 

module test ;

 

 reg &#91;3:0&#93; counter ;

 initial begin

 counter = 'b0 ;

 while &#40;counter<=10&#41; begin

 #10 ;

 counter = counter + 1'b1 ;

 end

 end

 

 //stop the simulation

 always begin

 #10 ; if &#40;$time >= 1000&#41; $finish ;

 end

 

endmodule

---

## 14. 4.4 Verilog 语句块

### 关键词：顺序块，并行块，嵌套块，命名块，disable


Verilog 语句块提供了将两条或更多条语句组成语法结构上相当于一条一句的机制。主要包括两种类型：顺序块和并行块。


### 顺序块


顺序块用关键字 begin 和 end 来表示。


顺序块中的语句是一条条执行的。当然，非阻塞赋值除外。


顺序块中每条语句的时延总是与其前面语句执行的时间相关。


在本节之前的仿真中，initial 块中的阻塞赋值，都是顺序块的实例。

### 并行块


并行块有关键字 fork 和 join 来表示。


并行块中的语句是并行执行的，即便是阻塞形式的赋值。


并行块中每条语句的时延都是与块语句开始执行的时间相关。


顺序块与并行块的区别显而易见，下面用仿真说明。

仿真代码如下:

## 实例
 
`timescale 1ns/1ns

 

module test ;

 reg &#91;3:0&#93; ai_sequen, bi_sequen ;

 reg &#91;3:0&#93; ai_paral, bi_paral ;

 reg &#91;3:0&#93; ai_nonblk, bi_nonblk ;

 

 //============================================================//

 //(1)Sequence block

 initial begin

 #5 ai_sequen = 4'd5 ; //at 5ns

 #5 bi_sequen = 4'd8 ; //at 10ns

 end

 //(2)fork block

 initial fork

 #5 ai_paral = 4'd5 ; //at 5ns

 #5 bi_paral = 4'd8 ; //at 5ns

 join

 //(3)non-block block

 initial fork

 #5 ai_nonblk <= 4'd5 ; //at 5ns

 #5 bi_nonblk <= 4'd8 ; //at 5ns

 join

 

endmodule

---

## 15. 3.2 Verilog 时延

### 关键词：时延， 惯性时延



连续赋值延时语句中的延时，用于控制任意操作数发生变化到语句左端赋予新值之间的时间延时。


时延一般是不可综合的。


寄存器的时延也是可以控制的，这部分在时序控制里加以说明。


连续赋值时延一般可分为普通赋值时延、隐式时延、声明时延。


下面 3 个例子实现的功能是等效的，分别对应 3 种不同连续赋值时延的写法。
 
//普通时延，A&B计算结果延时10个时间单位赋值给Z

wire Z, A, B ;

assign #10 Z = A & B ;

---

## 16. 4.3 Verilog 时序控制

### 关键词：时延控制，事件触发，边沿触发，电平触发


Verilog 提供了 2 大类时序控制方法：时延控制和事件控制。事件控制主要分为边沿触发事件控制与电平敏感事件控制。


### 时延控制


基于时延的时序控制出现在表达式中，它指定了语句从开始执行到执行完毕之间的时间间隔。


时延可以是数字、标识符或者表达式。


根据在表达式中的位置差异，时延控制又可以分为常规时延与内嵌时延。

**常规时延**


遇到常规延时时，该语句需要等待一定时间，然后将计算结果赋值给目标信号。


格式为：#delay procedural_statement，例如：

```
reg value_test ;
reg value_general ;
#10 value_general = value_test ;
```


该时延方式的另一种写法是直接将井号 # 独立成一个时延执行语句，例如：
```
#10 ;
value_ single = value_test ;
```


**内嵌时延**


遇到内嵌延时时，该语句先将计算结果保存，然后等待一定的时间后赋值给目标信号。

内嵌时延控制加在赋值号之后。例如：

```
reg value_test ;
reg value_embed ;
value_embed = #10 value_test ;
```


需要说明的是，这 2 种时延控制方式的效果是有所不同的。


当延时语句的赋值符号右端是常量时，2 种时延控制都能达到相同的延时赋值效果。


当延时语句的赋值符号右端是变量时，2 种时延控制可能会产生不同的延时赋值效果。

例如下面仿真代码：

## 实例
 
`timescale 1ns/1ns

 

module test ;

 reg value_test ;

 reg value_general, value_embed, value_single ;

 

 //signal source

 initial begin

 value_test = 0 ;

 #25 ; value_test = 1 ;

 #35 ; value_test = 0 ; //absolute 60ns

 #40 ; value_test = 1 ; //absolute 100ns

 #10 ; value_test = 0 ; //absolute 110ns

 end

 

 //(1)general delay control

 initial begin

 value_general = 1;

 #10 value_general = value_test ; //10ns, value_test=0

 #45 value_general = value_test ; //55ns, value_test=1

 #30 value_general = value_test ; //85ns, value_test=0

 #20 value_general = value_test ; //105ns, value_test=1

 end

 

 //(2)embedded delay control

 initial begin

 value_embed = 1;

 value_embed = #10 value_test ; //0ns, value_test=0

 value_embed = #45 value_test ; //10ns, value_test=0

 value_embed = #30 value_test ; //55ns, value_test=1

 value_embed = #20 value_test ; //85ns, value_test=0

 end

 

 //(3)single delay control

 initial begin

 value_single = 1;

 #10 ;

 value_single = value_test ; //10ns, value_test=0

 #45 ;

 value_single = value_test ; //55ns, value_test=1

 #30 ;

 value_single = value_test ; //85ns, value_test=0

 #20 ;

 value_single = value_test ; //105ns, value_test=1

 end

 

 always begin

 #10;

 if &#40;$time >= 150&#41; begin

 $finish ;

 end

 end

 

endmodule

---

## 17. 4.2 Verilog 过程赋值

### 关键词：阻塞赋值，非阻塞赋值，并行


过程性赋值是在 initial 或 always 语句块里的赋值，赋值对象是寄存器、整数、实数等类型。

这些变量在被赋值后，其值将保持不变，直到重新被赋予新值。

连续性赋值总是处于激活状态，任何操作数的改变都会影响表达式的结果；过程赋值只有在语句执行的时候，才会起作用。这是连续性赋值与过程性赋值的区别。

Verilog 过程赋值包括 2 种语句：阻塞赋值与非阻塞赋值。


### 阻塞赋值


阻塞赋值属于顺序执行，即下一条语句执行前，当前语句一定会执行完毕。

阻塞赋值语句使用等号 = 作为赋值符。

前面的仿真中，initial 里面的赋值语句都是用的阻塞赋值。

### 非阻塞赋值


非阻塞赋值属于并行执行语句，即下一条语句的执行和当前语句的执行是同时进行的，它不会阻塞位于同一个语句块中后面语句的执行。

非阻塞赋值语句使用小于等于号 <= 作为赋值符。

利用下面代码，对阻塞、非阻塞赋值进行仿真，来说明 2 种过程赋值的区别。


## 实例
 
`timescale 1ns/1ns

 

module test ;

 reg &#91;3:0&#93; ai, bi ;

 reg &#91;3:0&#93; ai2, bi2 ;

 reg &#91;3:0&#93; value_blk ;

 reg &#91;3:0&#93; value_non ;

 reg &#91;3:0&#93; value_non2 ;

 

 initial begin

 ai = 4'd1 ; //(1)

 bi = 4'd2 ; //(2)

 ai2 = 4'd7 ; //(3)

 bi2 = 4'd8 ; //(4)

 #20 ; //(5)

 

 //non-block-assigment with block-assignment

 ai = 4'd3 ; //(6)

 bi = 4'd4 ; //(7)

 value_blk = ai + bi ; //(8)

 value_non <= ai + bi ; //(9)

 

 //non-block-assigment itself

 ai2 <= 4'd5 ; //(10)

 bi2 <= 4'd6 ; //(11)

 value_non2 <= ai2 + bi2 ; //(12)

 end

 

 //stop the simulation

 always begin

 #10 ;

 if &#40;$time >= 1000&#41; $finish ;

 end

 

endmodule

---

## 18. 4.1 Verilog 过程结构

### 关键词：initial， always


过程结构语句有 2 种，initial 与 always 语句。它们是行为级建模的 2 种基本语句。


一个模块中可以包含多个 initial 和 always 语句，但 2 种语句不能嵌套使用。


这些语句在模块间并行执行，与其在模块的前后顺序没有关系。


但是 initial 语句或 always 语句内部可以理解为是顺序执行的（非阻塞赋值除外）。


每个 initial 语句或 always 语句都会产生一个独立的控制流，执行时间都是从 0 时刻开始。


### initial语句


initial 语句从 0 时刻开始执行，只执行一次，多个 initial 块之间是相互独立的。


如果 initial 块内包含多个语句，需要使用关键字 begin 和 end 组成一个块语句。


如果 initial 块内只要一条语句，关键字 begin 和 end 可使用也可不使用。


initial 理论上来讲是不可综合的，多用于初始化、信号检测等。


对上一节代码稍作修改，进行仿真，代码如下。

## 实例
 
`timescale 1ns/1ns

 

module test ;

 reg ai, bi ;

 

 initial begin

 ai = 0 ;

 #25 ; ai = 1 ;

 #35 ; ai = 0 ; //absolute 60ns

 #40 ; ai = 1 ; //absolute 100ns

 #10 ; ai = 0 ; //absolute 110ns

 end

 

 initial begin

 bi = 1 ;

 #70 ; bi = 0 ; //absolute 70ns

 #20 ; bi = 1 ; //absolute 90ns

 end

 

 //at proper time stop the simulation

 initial begin

 forever begin

 #100;

 //$display("---gyc---%d", $time);

 if &#40;$time >= 1000&#41; begin

 $finish ;

 end

 end

 end

 

endmodule

---

## 19. 6.1 Verilog 函数

### 关键词：函数，大小端转换，数码管译码


在 Verilog 中，可以利用任务（关键字为 task）或函数（关键字为 function），将重复性的行为级设计进行提取，并在多个地方调用，来避免重复代码的多次编写，使代码更加的简洁、易懂。

### 函数


函数只能在模块中定义，位置任意，并在模块的任何地方引用，作用范围也局限于此模块。函数主要有以下几个特点：

- 
1）不含有任何延迟、时序或时序控制逻辑
- 
2）至少有一个输入变量
- 
3）只有一个返回值，且没有输出
- 
4）不含有非阻塞赋值语句
- 
5）函数可以调用其他函数，但是不能调用任务

Verilog 函数声明格式如下：

```
function [range-1:0] function_id ;
input_declaration ;
 other_declaration ;
procedural_statement ;
endfunction
```

 


函数在声明时，会隐式的声明一个宽度为 range、 名字为 function_id 的寄存器变量，函数的返回值通过这个变量进行传递。当该寄存器变量没有指定位宽时，默认位宽为 1。

 
函数通过指明函数名与输入变量进行调用。函数结束时，返回值被传递到调用处。


函数调用格式如下：

```
function_id(input1, input2, &hellip;);
```

 


下面用函数实现一个数据大小端转换的功能。


当输入为 4'b0011 时，输出可为 4'b1100。例如：

## 实例
 
module endian_rvs

 #&#40;parameter N = 4&#41;

 &#40;

 input en, //enable control

 input &#91;N-1:0&#93; a ,

 output &#91;N-1:0&#93; b

 &#41;;

 

 reg &#91;N-1:0&#93; b_temp ;

 always @&#40;*&#41; begin

 if &#40;en&#41; begin

 b_temp = data_rvs&#40;a&#41;;

 end

 else begin

 b_temp = 0 ;

 end

 end

 assign b = b_temp ;

 

 //function entity

 function &#91;N-1:0&#93; data_rvs ;

 input &#91;N-1:0&#93; data_in ;

 parameter MASK = 32'h3 ; 

 integer k ;

 begin

 for&#40;k=0; k<N; k=k+1&#41; begin

 data_rvs&#91;N-k-1&#93; = data_in&#91;k&#93; ; 

 end

 end

 endfunction

 

endmodule

---

## 20. 6.2 Verilog 任务

### 关键词：任务

### 任务与函数的区别


和函数一样，任务（task）可以用来描述共同的代码段，并在模块内任意位置被调用，让代码更加的直观易读。函数一般用于组合逻辑的各种转换和计算，而任务更像一个过程，不仅能完成函数的功能，还可以包含时序控制逻辑。下面对任务与函数的区别进行概括：

| 比较点 | 函数 | 任务 | 
| 输入 | 函数至少有一个输入，端口声明不能包含 inout 型 | 任务可以没有或者有多个输入，且端口声明可以为 inout 型 | 
| 输出 | 函数没有输出 | 任务可以没有或者有多个输出 | 
| 返回值 | 函数至少有一个返回值 | 任务没有返回值 | 
| 仿真时刻 | 函数总在零时刻就开始执行 | 任务可以在非零时刻执行 | 
| 时序逻辑 | 函数不能包含任何时序控制逻辑 | 任务不能出现 always 语句，但可以包含其他时序控制，如延时语句 | 
| 调用 | 函数只能调用函数，不能调用任务 | 任务可以调用函数和任务 | 
| 书写规范 | 函数不能单独作为一条语句出现，只能放在赋值语言的右端 | 任务可以作为一条单独的语句出现语句块中 | 

### 任务


**任务声明**


任务在模块中任意位置定义，并在模块内任意位置引用，作用范围也局限于此模块。


模块内子程序出现下面任意一个条件时，则必须使用任务而不能使用函数。

- 
1）子程序中包含时序控制逻辑，例如延迟，事件控制等
- 
2）没有输入变量
- 
3）没有输出或输出端的数量大于 1

Verilog 任务声明格式如下：

```
task task_id ;
 port_declaration ;
 procedural_statement ;
endtask
```


任务中使用关键字 input、output 和 inout 对端口进行声明。input 、inout 型端口将变量从任务外部传递到内部，output、inout 型端口将任务执行完毕时的结果传回到外部。


进行任务的逻辑设计时，可以把 input 声明的端口变量看做 wire 型，把 output 声明的端口变量看做 reg 型。但是不需要用 reg 对 output 端口再次说明。


对 output 信号赋值时也不要用关键字 assign。为避免时序错乱，建议 output 信号采用阻塞赋值。


例如，一个带延时的异或功能 task 描述如下：

## 实例
 
task xor_oper_iner;

 input &#91;N-1:0&#93; numa;

 input &#91;N-1:0&#93; numb;

 output &#91;N-1:0&#93; numco ;

 //output reg [N-1:0] numco ; //无需再注明 reg 类型，虽然注明也可能没错

 #3 numco = numa ^ numb ;

 //assign #3 numco = numa ^ numb ; //不用assign，因为输出默认是reg

endtask

---

## 21. 2.5 Verilog 编译指令

以反引号 ` 开始的某些标识符是 Verilog 系统编译指令。

编译指令为 Verilog 代码的撰写、编译、调试等提供了极大的便利。


下面介绍下完整的 8 种编译指令，其中前 4 种使用频率较高。

### `define, `undef


在编译阶段，`define 用于文本替换，类似于 C 语言中的 **#define**。

一旦 `define 指令被编译，其在整个编译过程中都会有效。例如，在一个文件中定义：

```
`define DATA_DW 32
```


则在另一个文件中也可以直接使用 DATA_DW。

```
`define S $stop; 
//用`S来代替系统函数$stop; (包括分号)
`define WORD_DEF reg [31:0] 
//可以用`WORD_DEF来声明32bit寄存器变量
```


`undef 用来取消之前的宏定义，例如：

```
`define DATA_DW 32
&hellip;&hellip;
reg [DATA_DW-1:0] data_in ;
&hellip;&hellip;
`undef DATA_DW

`ifdef, `ifndef, `elsif, `else, `endif
```


这些属于条件编译指令。例如下面的例子中，如果定义了 MCU51，则使用第一种参数说明；如果没有定义 MCU、定义了 WINDOW，则使用第二种参数说明；如果 2 个都没有定义，则使用第三种参数说明。

```
`ifdef MCU51
 parameter DATA_DW = 8 ;
`elsif WINDOW
 parameter DATA_DW = 64 ;
`else
 parameter DATA_DW = 32 ;
`endif
```


`elsif, `else 编译指令对于 `ifdef 指令是可选的，即可以只有 `ifdef 和 `endif 组成一次条件编译指令块。

当然，也可用 `ifndef 来设置条件编译，表示如果没有相关的宏定义，则执行相关语句。

下面例子中，如果定义了 WINDOW，则使用第二种参数说明。如果没有定义 WINDOW，则使用第一种参数说明。

## 实例
 
`ifndef WINDOW

 parameter DATA_DW = 32 ; 

 `else

 parameter DATA_DW = 64 ;

 `endif

---

## 22. 5.3 Verilog 带参数例化

### 关键词： defparam，参数，例化，ram


当一个模块被另一个模块引用例化时，高层模块可以对低层模块的参数值进行改写。这样就允许在编译时将不同的参数传递给多个相同名字的模块，而不用单独为只有参数不同的多个模块再新建文件。


参数覆盖有 2 种方式：1）使用关键字 defparam，2）带参数值模块例化。 

### defparam 语句


可以用关键字 defparam 通过模块层次调用的方法，来改写低层次模块的参数值。

例如对一个单口地址线和数据线都是 4bit 宽度的 ram 模块的 MASK 参数进行改写：

## 实例
 
//instantiation

defparam u_ram_4x4.MASK = 7 ;

ram_4x4 u_ram_4x4

 &#40;

 .CLK &#40;clk&#41;,

 .A &#40;a&#91;4-1:0&#93;&#41;,

 .D &#40;d&#41;,

 .EN &#40;en&#41;,

 .WR &#40;wr&#41;, //1 for write and 0 for read

 .Q &#40;q&#41; &#41;;

---

## 23. 5.2 Verilog 模块例化

### 关键字：例化，generate，全加器，层次访问


在一个模块中引用另一个模块，对其端口进行相关连接，叫做模块例化。模块例化建立了描述的层次。信号端口可以通过位置或名称关联，端口连接也必须遵循一些规则。


### 命名端口连接


这种方法将需要例化的模块端口与外部信号按照其名字进行连接，端口顺序随意，可以与引用 module 的声明端口顺序不一致，只要保证端口名字与外部信号匹配即可。

下面是例化一次 1bit 全加器的例子：

## 实例
 
full_adder1 u_adder0&#40;

 .Ai &#40;a&#91;0&#93;&#41;,

 .Bi &#40;b&#91;0&#93;&#41;,

 .Ci &#40;c==1'b1 ? 1'b0 : 1'b1&#41;,

 .So &#40;so_bit0&#41;,

 .Co &#40;co_temp&#91;0&#93;&#41;&#41;;

---

## 24. 6.6 Verilog 仿真激励

### 关键词：testbench，仿真，文件读写


Verilog 代码设计完成后，还需要进行重要的步骤，即逻辑功能仿真。仿真激励文件称之为 testbench，放在各设计模块的顶层，以便对模块进行系统性的例化调用进行仿真。

毫不夸张的说，对于稍微复杂的 Verilog 设计，如果不进行仿真，即便是经验丰富的老手，99.9999% 以上的设计都不会正常的工作。不能说仿真比设计更加的重要，但是一般来说，仿真花费的时间会比设计花费的时间要多。有时候，考虑到各种应用场景，testbench 的编写也会比 Verilog 设计更加的复杂。所以，数字电路行业会具体划分设计工程师和验证工程师。

下面，对 testbench 做一个简单的学习。

### testbench 结构划分

testbench 一般结构如下:

![](https://www.runoob.com/wp-content/uploads/2020/09/VuJtsmlLrJjDTWDO.png)


其实 testbench 最基本的结构包括信号声明、激励和模块例化。


根据设计的复杂度，需要引入时钟和复位部分。当然更为复杂的设计，激励部分也会更加复杂。根据自己的验证需求，选择是否需要自校验和停止仿真部分。


当然，复位和时钟产生部分，也可以看做激励，所以它们都可以在一个语句块中实现。也可以拿自校验的结果，作为结束仿真的条件。


实际仿真时，可以根据自己的个人习惯来编写 testbench，这里只是做一份个人的总结。

### testbench 仿真举例


前面的章节中，已经写过很多的 testbench。其实它们的结构也都大致相同。

下面，我们举一个数据拼接的简单例子，对 testbench 再做一个具体的分析。

一个 2bit 数据拼接成 8bit 数据的功能模块描述如下:

## 实例
 
module data_consolidation

 &#40;

 input clk ,

 input rstn ,

 input &#91;1:0&#93; din , //data in

 input din_en ,

 output &#91;7:0&#93; dout ,

 output dout_en //data out

 &#41;;

 // data shift and counter

 reg &#91;7:0&#93; data_r ;

 reg &#91;1:0&#93; state_cnt ;

 always @&#40;posedge clk or negedge rstn&#41; begin

 if &#40;!rstn&#41; begin

 state_cnt <= 'b0 ;

 data_r <= 'b0 ;

 end

 else if &#40;din_en&#41; begin

 state_cnt <= state_cnt + 1'b1 ; //数据计数

 data_r <= &#123;data_r&#91;5:0&#93;, din&#125; ; //数据拼接

 end

 else begin

 state_cnt <= 'b0 ;

 end

 end

 assign dout = data_r ;

 // data output en

 reg dout_en_r ;

 always @&#40;posedge clk or negedge rstn&#41; begin

 if &#40;!rstn&#41; begin

 dout_en_r <= 'b0 ;

 end

 //计数为 3 且第 4 个数据输入时，同步输出数据输出使能信号

 else if &#40;state_cnt == 2'd3 & din_en&#41; begin 

 dout_en_r <= 1'b1 ;

 end

 else begin

 dout_en_r <= 1'b0 ;

 end

 end

 //这里不直接声明dout_en为reg变量，而是用相关寄存器对其进行assign赋值

 assign dout_en = dout_en_r;

endmodule

---

## 25. 1.4 Verilog 设计方法

### 设计方法


Verilog 的设计多采用自上而下的设计方法（top-down）。即先定义顶层模块功能，进而分析要构成顶层模块的必要子模块；然后进一步对各个模块进行分解、设计，直到到达无法进一步分解的底层功能块。这样，可以把一个较大的系统，细化成多个小系统，从时间、工作量上分配给更多的人员去设计，从而提高了设计速度，缩短了开发周期。

![](https://www.runoob.com/wp-content/uploads/2020/09/vlg-design-method-1.png)


### 设计流程


![](https://www.runoob.com/wp-content/uploads/2020/09/vlg-design-method-2.png)


Verilog 的设计流程，一般包括以下几个步骤：



**需求分析**


工作人员需要对用户提出的功能要求进行分析理解，做出电路系统的整体规划，形成详细的技术指标，确定初步方案。例如，要设计一个电子屏，需要考虑供电方式、工作频率、产品体积、成本、功耗等，电路实现采用 ASIC 还是选用 FPGA/CPLD 器件等。
 


**功能划分**


正确地分析了用户的电路需求后，就可以进行逻辑功能的总体设计，设计整个电路的功能、接口和总体结构，考虑功能模块的划分和设计思路，各子模块的接口和时序（包括接口时序和内部信号的时序）等，向项目组成员合理分配子模块设计任务。
 


**文本描述**


可以用任意的文本编辑器，也可以用专用的 HDL 编辑环境，对所需求的数字电路进行设计建模，保存为 .v 文件。


**功能仿真（前仿真）**


对建模文件进行编译，对模型电路进行功能上的仿真验证，查找设计的错误并修正。


此时的仿真验证并没有考虑到信号的延迟等一些 timing 因素，只是验证逻辑上的正确性。
 


**逻辑综合**


综合（synthesize），就是在标准单元库和特定的设计约束的基础上，将设计的高层次描述（Verilog 建模）转换为门级网表的过程。逻辑综合的目的是产生物理电路门级结构，并在逻辑、时序上进行一定程度的优化，寻求逻辑、面积、功耗的平衡，增强电路的可测试性。


但不是所有的 Verilog 语句都是可以综合成逻辑单元的，例如时延语句。



**布局布线**


根据逻辑综合出的网表与约束文件，利用厂家提供的各种基本标准单元库，对门级电路进行布局布线。至此，已经将 Verilog 设计的数字电路，设计成由标准单元库组成的数字电路。 


**时序仿真（后仿真）**


布局布线后，电路模型中已经包含了时延信息。利用在布局布线中获得的精确参数，用仿真软件验证电路的时序。单元器件的不同、布局布线方案都会给电路的时序造成影响，严重时会出现错误。出错后可能就需要重新修改 RTL（寄存器传输级描述，即 Verilog 初版描述），重复后面的步骤。这样的过程可能反复多次，直至错误完全排除。


**FPGA/CPLD 下载或 ASIC 制造工艺生产**



完成上面所有步骤后，就可以通过开发工具将设计的数字电路目标文件下载到 FPGA/CPLD 芯片中，然后在电路板上进行调试、验证。


如果要在 ASIC 上实现，则需要制造芯片。一般芯片制造时，也需要先在 FPGA 板卡上进行逻辑功能的验证。

---

## 26. 6.5 Verilog 避免 Latch

### 关键词：触发器，锁存器

### Latch 的含义


锁存器（Latch），是电平触发的存储单元，数据存储的动作取决于输入时钟（或者使能）信号的电平值。仅当锁存器处于使能状态时，输出才会随着数据输入发生变化。


当电平信号无效时，输出信号随输入信号变化，就像通过了缓冲器；当电平有效时，输出信号被锁存。激励信号的任何变化，都将直接引起锁存器输出状态的改变，很有可能会因为瞬态特性不稳定而产生振荡现象。


锁存器示意图如下：

![](https://www.runoob.com/wp-content/uploads/2020/09/UEro1jQtpyTQS4BI.png)


触发器（flip-flop），是边沿敏感的存储单元，数据存储的动作（状态转换）由某一信号的上升沿或者下降沿进行同步的（限制存储单元状态转换在一个很短的时间内）。


触发器示意图如下：

![](https://www.runoob.com/wp-content/uploads/2020/09/DzkHnLYQkX67ZYBO.png)


寄存器（register），在 Verilog 中用来暂时存放参与运算的数据和运算结果的变量。一个变量声明为寄存器时，它既可以被综合成触发器，也可能被综合成 Latch，甚至是 wire 型变量。但是大多数情况下我们希望它被综合成触发器，但是有时候由于代码书写问题，它会被综合成不期望的 Latch 结构。


Latch 的主要危害有：

- 1）输入状态可能多次变化，容易产生毛刺，增加了下一级电路的不确定性；
- 2）在大部分 FPGA 的资源中，可能需要比触发器更多的资源去实现 Latch 结构；
- 3）锁存器的出现使得静态时序分析变得更加复杂。

Latch 多用于门控时钟（clock gating）的控制，一般设计时，我们应当避免 Latch 的产生。

### if 结构不完整


组合逻辑中，不完整的 if - else 结构，会产生 latch。


例如下面的模型，if 语句中缺少 else 结构，系统默认 else 的分支下寄存器 q 的值保持不变，即具有存储数据的功能，所以寄存器 q 会被综合成 latch 结构。

## 实例
 
module module1_latch1&#40;

 input data, 

 input en ,

 output reg q&#41; ;

 

 always @&#40;*&#41; begin

 if &#40;en&#41; q = data ;

 end

endmodule

---

## 27. 6.4 Verilog 竞争与冒险

### 关键字：竞争，冒险，书写规范


### 产生原因


数字电路中，信号传输与状态变换时都会有一定的延时。

- 在组合逻辑电路中，不同路径的输入信号变化传输到同一点门级电路时，在时间上有先有后，这种先后所形成的时间差称为竞争（Competition）。

- 由于竞争的存在，输出信号需要经过一段时间才能达到期望状态，过渡时间内可能产生瞬间的错误输出，例如尖峰脉冲。这种现象被称为冒险（Hazard）。

- 竞争不一定有冒险，但冒险一定会有竞争。F = A & A'，电路如左下图所示。

由于反相器电路的存在，信号 A' 传递到与门输入端的时间相对于信号 A 会滞后，这就可能导致与门最后的输出结果 F 会出现干扰脉冲。如右下图所示。

![](https://www.runoob.com/wp-content/uploads/2020/09/UIYHpuq1MQk1qSRJ.png)




![](https://www.runoob.com/wp-content/uploads/2020/09/1ENpirJR5XTPq4Jt.png)
 


其实实际硬件电路中，只要门电路各个输入端延时不同，就有可能产生竞争与冒险。


例如一个简单的与门，输入信号源不一定是同一个信号变换所来，由于硬件工艺、其他延迟电路的存在，也可能产生竞争与冒险，如下图所示。

![](https://www.runoob.com/wp-content/uploads/2020/09/52NhfykVOdwPDphm.png)


### 判断方法


**代数法**


在逻辑表达式，保持一个变量固定不动，将剩余其他变量用 0 或 1 代替，如果最后逻辑表达式能化简成

```
Y = A + A'
```
 

或 

```
Y = A &middot; A'
```


的形式，则可判定此逻辑存在竞争与冒险。

例如逻辑表达式 Y = AB + A'C，在 B=C=1 的情况下，可化简为 Y = A + A'。显然，A 状态的改变，势必会造成电路存在竞争冒险。


**卡诺图法**


有两个相切的卡诺圈，并且相切处没有其他卡诺圈包围，可能会出现竞争与冒险现象。


例如左下图所存在竞争与冒险，右下图则没有。

![](https://www.runoob.com/wp-content/uploads/2020/09/riZgKcXReVPbPn0Q.png)
 

其实，卡诺图本质上还是对逻辑表达式的一个分析，只是可以进行直观的判断。


例如，左上图逻辑表达式可以简化为 Y = A'B' + AC，当 B=0 且 C=1 时，此逻辑表达式又可以表示为 Y = A' + A。所以肯定会存在竞争与冒险。

右上图逻辑表达式可以简化为 Y = A'B' + AB，显然 **B** 无论等于 **1** 还是 **0**，此式都不会化简成 Y = A' + A。所以此逻辑不存在竞争与冒险。


需要注意的是，卡诺图是首尾相临的。如下图所示，虽然看起来两个卡诺圈并没有相切，但实际上，m6 与 m4 也是相邻的，所以下面卡诺图所代表的数字逻辑也会产生竞争与冒险。

![](https://www.runoob.com/wp-content/uploads/2020/09/jUY4EoeWZhAm5lbT.png)


**
其他较为复杂的情况，可能需要采用 "计算机辅助分析 + 实验" 的方法。**

## 消除方法


对数字电路来说，常见的避免竞争与冒险的方法主要有 4 种。


### 1）增加滤波电容，滤除窄脉冲


此种方法需要在输出端并联一个小电容，将尖峰脉冲的幅度削弱至门电路阈值以下。


此方法虽然简单，但是会增加输出电压的翻转时间，易破坏波形。

### 2）修改逻辑，增加冗余项


利用卡诺图，在两个相切的圆之间，增加一个卡诺圈，并加在逻辑表达式之中。


如下图所示，对数字逻辑 Y = A'B' + AC 增加冗余项 B'C，则此电路逻辑可以表示为 Y = A'B' + AC + B'C。此时电路就不会再存在竞争与冒险。

![](https://www.runoob.com/wp-content/uploads/2020/09/Me1Nfse1Cmcjinur.png)


### 3）使用时钟同步电路，利用触发器进行打拍延迟


同步电路信号的变化都发生在时钟边沿。对于触发器的 D 输入端，只要毛刺不出现在时钟的上升沿并且不满足数据的建立和保持时间，就不会对系统造成危害，因此可认为 D 触发器的 D 输入端对毛刺不敏感。
利用此特性，在时钟边沿驱动下，对一个组合逻辑信号进行延迟打拍，可消除竞争冒险。


延迟一拍时钟时，会一定概率的减少竞争冒险的出现。实验表明，最安全的打拍延迟周期是 3 拍，可有效减少竞争冒险的出现。

当然，最终还是需要根据自己的设计需求，对信号进行合理的打拍延迟。

**为说明对信号进行打拍延迟可以消除竞争冒险，我们建立下面的代码模型。**

## 实例
 
module competition_hazard

 &#40;

 input clk ,

 input rstn ,

 input en ,

 input din_rvs ,

 output reg flag

 &#41;;

 wire condition = din_rvs & en ; //combination logic

 always @&#40;posedge clk or negedge !rstn&#41; begin

 if &#40;!rstn&#41; begin

 flag <= 1'b0 ;

 end

 else begin

 flag <= condition ;

 end

 end 

endmodule

---

## 28. 6.3 Verilog 状态机

### 关键词：状态机，售卖机


有限状态机（Finite-State Machine，FSM），简称状态机，是表示有限个状态以及在这些状态之间的转移和动作等行为的数学模型。状态机不仅是一种电路的描述工具，而且也是一种思想方法，在电路设计的系统级和 RTL 级有着广泛的应用。

### 状态机类型


Verilog 中状态机主要用于同步时序逻辑的设计，能够在有限个状态之间按一定要求和规律切换时序电路的状态。状态的切换方向不但取决于各个输入值，还取决于当前所在状态。
状态机可分为 2 类：Moore 状态机和 Mealy 状态机。


**Moore 型状态机**


Moore 型状态机的输出只与当前状态有关，与当前输入无关。


输出会在一个完整的时钟周期内保持稳定，即使此时输入信号有变化，输出也不会变化。输入对输出的影响要到下一个时钟周期才能反映出来。这也是 Moore 型状态机的一个重要特点：输入与输出是隔离开来的。

![](https://www.runoob.com/wp-content/uploads/2020/09/drIsJ2XFh6mt4t5D.png)


**Mealy 型状态机**


Mealy 型状态机的输出，不仅与当前状态有关，还取决于当前的输入信号。


Mealy 型状态机的输出是在输入信号变化以后立刻发生变化，且输入变化可能出现在任何状态的时钟周期内。因此，同种逻辑下，Mealy 型状态机输出对输入的响应会比 Moore 型状态机早一个时钟周期。

![](https://www.runoob.com/wp-content/uploads/2020/09/4xc5VfpojsJMoZX5.png)


**状态机设计流程**


根据设计需求画出状态转移图，确定使用状态机类型，并标注出各种输入输出信号，更有助于编程。一般使用最多的是 Mealy 型 3 段式状态机，下面用通过设计一个自动售卖机的具体实例来说明状态机的设计过程。

### 自动售卖机


**自动售卖机的功能描述如下：**

饮料单价 2 元，该售卖机只能接受 0.5 元、1 元的硬币。考虑找零和出货。投币和出货过程都是一次一次的进行，不会出现一次性投入多币或一次性出货多瓶饮料的现象。每一轮售卖机接受投币、出货、找零完成后，才能进入到新的自动售卖状态。

**该售卖机的工作状态转移图如下所示，包含了输入、输出信号状态。**

其中，coin = 1 代表投入了 0.5 元硬币，coin = 2 代表投入了 1 元硬币。

![](https://www.runoob.com/wp-content/uploads/2020/09/Uep0FDU5QLlSBjKZ.png)



### 状态机设计：3 段式（推荐）


**状态机设计如下：**

- 
(0) 首先，根据状态机的个数确定状态机编码。利用编码给状态寄存器赋值，代码可读性更好。
- 
(1) 状态机第一段，时序逻辑，非阻塞赋值，传递寄存器的状态。
- 
(2) 状态机第二段，组合逻辑，阻塞赋值，根据当前状态和当前输入，确定下一个状态机的状态。
- 
(3) 状态机第三代，时序逻辑，非阻塞赋值，因为是 Mealy 型状态机，根据当前状态和当前输入，确定输出信号。

## 实例
 
// vending-machine

// 2 yuan for a bottle of drink

// only 2 coins supported: 5 jiao and 1 yuan

// finish the function of selling and changing

module vending_machine_p3 &#40;

 input clk ,

 input rstn ,

 input &#91;1:0&#93; coin , //01 for 0.5 jiao, 10 for 1 yuan

 output &#91;1:0&#93; change ,

 output sell //output the drink

 &#41;;

 //machine state decode

 parameter IDLE = 3'd0 ;

 parameter GET05 = 3'd1 ;

 parameter GET10 = 3'd2 ;

 parameter GET15 = 3'd3 ;

 //machine variable

 reg &#91;2:0&#93; st_next ;

 reg &#91;2:0&#93; st_cur ;

 //(1) state transfer

 always @&#40;posedge clk or negedge rstn&#41; begin

 if &#40;!rstn&#41; begin

 st_cur <= 'b0 ;

 end

 else begin

 st_cur <= st_next ;

 end

 end

 //(2) state switch, using block assignment for combination-logic

 //all case items need to be displayed completely 

 always @&#40;*&#41; begin 

 //st_next = st_cur ;//如果条件选项考虑不全，可以赋初值消除latch

 case&#40;st_cur&#41;

 IDLE:

 case &#40;coin&#41;

 2'b01: st_next = GET05 ;

 2'b10: st_next = GET10 ;

 default: st_next = IDLE ;

 endcase

 GET05:

 case &#40;coin&#41;

 2'b01: st_next = GET10 ;

 2'b10: st_next = GET15 ;

 default: st_next = GET05 ;

 endcase

 GET10:

 case &#40;coin&#41;

 2'b01: st_next = GET15 ;

 2'b10: st_next = IDLE ;

 default: st_next = GET10 ;

 endcase

 GET15:

 case &#40;coin&#41;

 2'b01,2'b10:

 st_next = IDLE ;

 default: st_next = GET15 ;

 endcase

 default: st_next = IDLE ;

 endcase

 end

 //(3) output logic, using non-block assignment

 reg &#91;1:0&#93; change_r ;

 reg sell_r ;

 always @&#40;posedge clk or negedge rstn&#41; begin

 if &#40;!rstn&#41; begin

 change_r <= 2'b0 ;

 sell_r <= 1'b0 ;

 end

 else if &#40;&#40;st_cur == GET15 && coin ==2'h1&#41;

 || &#40;st_cur == GET10 && coin ==2'd2&#41;&#41; begin

 change_r <= 2'b0 ;

 sell_r <= 1'b1 ;

 end

 else if &#40;st_cur == GET15 && coin == 2'h2&#41; begin

 change_r <= 2'b1 ;

 sell_r <= 1'b1 ;

 end

 else begin

 change_r <= 2'b0 ;

 sell_r <= 1'b0 ;

 end

 end

 assign sell = sell_r ;

 assign change = change_r ;

endmodule

---

## 29. 6.7 Verilog 流水线

### 关键词：流水线，乘法器

硬件描述语言的一个突出优点就是指令执行的并行性。多条语句能够在相同时钟周期内并行处理多个信号数据。

但是当数据串行输入时，指令执行的并行性并不能体现出其优势。而且很多时候有些计算并不能在一个或两个时钟周期内执行完毕，如果每次输入的串行数据都需要等待上一次计算执行完毕后才能开启下一次的计算，那效率是相当低的。流水线就是解决多周期下串行数据计算效率低的问题。

### 流水线


流水线的基本思想是：把一个重复的过程分解为若干个子过程，每个子过程由专门的功能部件来实现。将多个处理过程在时间上错开，依次通过各功能段，这样每个子过程就可以与其他子过程并行进行。


假如一个洗衣店内洗衣服的过程分为 4 个阶段：取衣、洗衣、烘干、装柜。每个阶段都需要半小时来完成，则洗一次衣服需要 2 小时。


考虑最差情况，洗衣店内只有一台洗衣机、一台烘干机、一个衣柜。如果每半小时送来一批要洗的衣服，每次等待上一批衣服洗完需要 2 小时，那么洗完 4 批衣服需要的时间就是 8 小时。


图示如下：


[
![](https://www.runoob.com/wp-content/uploads/2020/09/u6XaHdHL1YBgOvq9.png)
](https://www.runoob.com/wp-content/uploads/2020/09/u6XaHdHL1YBgOvq9.png)


对这个洗衣店的装备进行升级，一共引进 4 套洗衣服的装备，工作人员也增加到 4 个，每个人负责一个洗衣阶段。所以每批次的衣服，都能够及时的被相同的人放入到不同的洗衣机内。由于时间上是错开的，每批次的衣服都能被相同的人在不同的设备与时间段（半小时）内洗衣、烘干和装柜。图示如下。


 [
![](https://www.runoob.com/wp-content/uploads/2020/09/S4bJMhLnXd0uIPAf.jpg)
](https://www.runoob.com/wp-content/uploads/2020/09/S4bJMhLnXd0uIPAf.jpg)


可以看出，洗完 4 批衣服只需要 3 个半小时，效率明显提高。


其实，在 2 小时后第一套洗衣装备已经完成洗衣过程而处于空闲状态，如果此时还有第 5 批衣服的送入，那么第一套设备又可以开始工作。依次类推，只要衣服批次不停的输入，4 台洗衣设备即可不间断的完成对所有衣服的清洗过程。且除了第一批次洗衣时间需要 2 小时，后面每半小时都会有一批次衣服清洗完成。


衣服批次越多，节省的时间就越明显。假如有 N 批次衣服，需要的时间为 (4+N) 个半小时。


当然，升级后洗衣流程也有缺点。设备和工作人员的增加导致了投入的成本增加，洗衣店内剩余空间也被缩小，工作状态看起来比较繁忙。

和洗衣服过程类似，数据的处理路径也可以看作是一条生产线，路径上的每个数字处理单元都可以看作是一个阶段，会产生延时。


流水线设计就是将路径系统的分割成一个个数字处理单元（阶段），并在各个处理单元之间插入寄存器来暂存中间阶段的数据。被分割的单元能够按阶段并行的执行，相互间没有影响。所以最后流水线设计能够提高数据的吞吐率，即提高数据的处理速度。


流水线设计的缺点就是，各个处理阶段都需要增加寄存器保存中间计算状态，而且多条指令并行执行，势必会导致功耗增加。


下面，设计一个乘法器，并对是否采用流水线设计进行对比。

### 一般乘法器设计


**前言**


也许有人会问，直接用乘号 * 来完成 2 个数的相乘不是更快更简单吗？


如果你有这个疑问，说明你对硬件描述语言的认知还有所不足。就像之前所说，Verilog 描述的是硬件电路，直接用乘号完成相乘过程，编译器在编译的时候也会把这个乘法表达式映射成默认的乘法器，但其构造不得而知。


例如，在 FPGA 设计中，可以直接调用 IP 核来生成一个高性能的乘法器。在位宽较小的时候，一个周期内就可以输出结果，位宽较大时也可以流水输出。在能满足要求的前提下，可以谨慎的用 * 或直接调用 IP 来完成乘法运算。


但乘法器 IP 也有很多的缺陷，例如位宽的限制，未知的时序等。尤其使用乘号，会为数字设计的不确定性埋下很大的隐瞒。


很多时候，常数的乘法都会用移位相加的形式实现，例如：

## 实例
 
A = A<<1 ; //完成A * 2

A = &#40;A<<1&#41; + A ; //对应A * 3

A = &#40;A<<3&#41; + &#40;A<<2&#41; + &#40;A<<1&#41; + A ; //对应A * 15

---

## 30. 7.2 Verilog 并行 FIR 滤波器设计

FIR（Finite Impulse Response）滤波器是一种有限长单位冲激响应滤波器，又称为非递归型滤波器。

FIR 滤波器具有严格的线性相频特性，同时其单位响应是有限长的，因而是稳定的系统，在数字通信、图像处理等领域都有着广泛的应用。

### FIR 滤波器原理


FIR 滤波器是有限长单位冲击响应滤波器。直接型结构如下：

![](https://www.runoob.com/wp-content/uploads/2020/10/D9lZSuIQcPTnGJfB.png)



FIR 滤波器本质上就是输入信号与单位冲击响应函数的卷积，表达式如下：

![](https://www.runoob.com/wp-content/uploads/2020/10/wa2y7ATjbJV2jmFR.png)


FIR 滤波器有如下几个特性：

- 
(1) 响应是有限长序列。 
- 
(2) 系统函数在 |z| > 0 处收敛，极点全部在 z=0 处，属于因果系统。
- 
(3) 结构上是非递归的，没有输出到输入的反馈。
- 
(4) 输入信号相位响应是线性的，因为响应函数 h(n) 系数是对称的。
- 
(5) 输入信号的各频率之间，相对相位差也是固定不变的。
- 
(6) 时域卷积等于频域相乘，因此该卷积相当于筛选频谱中各频率分量的增益倍数。某些频率分量保留，某些频率分量衰减，从而实现滤波的效果。


### 并行 FIR 滤波器设计


**设计说明**

输入频率为 7.5 MHz 和 250 KHz 的正弦波混合信号，经过 FIR 滤波器后，高频信号 7.5MHz 被滤除，只保留 250KHz 的信号。设计参数如下：


```
输入频率： 7.5MHz 和 250KHz
采样频率： 50MHz
阻带： 1MHz ~ 6MHz
阶数： 15（N-1=15）
```



由 FIR 滤波器结构可知，阶数为 15 时，FIR 的实现需要 16 个乘法器，15 个加法器和 15 组延时寄存器。为了稳定第一拍的数据，可以再多用一组延时寄存器，即共用 16 组延时寄存器。由于 FIR 滤波器系数的对称性，乘法器可以少用一半，即共使用 8 个乘法器。


并行设计，就是在一个时钟周期内对 16 个延时数据同时进行乘法、加法运算，然后在时钟驱动下输出滤波值。这种方法的优点是滤波延时短，但是对时序要求比较高。

**并行设计**


设计中使用到的乘法器模块代码，可参考之前流水线式设计的乘法器。


为方便快速仿真，也可以直接使用乘号 * 完成乘法运算，设计中加入宏定义 SAFE_DESIGN 来选择使用哪种乘法器。

FIR 滤波器系数可由 matlab 生成，具体见附录。

## 实例
 
/***********************************************************

>> V201001 : Fs：50Mhz, fstop：1Mhz-6Mhz, order： 15

************************************************************/

`define SAFE_DESIGN

 

module fir_guide &#40;

 input rstn, //复位，低有效

 input clk, //工作频率，即采样频率

 input en, //输入数据有效信号

 input &#91;11:0&#93; xin, //输入混合频率的信号数据

 output valid, //输出数据有效信号

 output &#91;28:0&#93; yout //输出数据，低频信号，即250KHz

 &#41;;

 

 //data en delay 

 reg &#91;3:0&#93; en_r ;

 always @&#40;posedge clk or negedge rstn&#41; begin

 if &#40;!rstn&#41; begin

 en_r&#91;3:0&#93; <= 'b0 ;

 end

 else begin

 en_r&#91;3:0&#93; <= &#123;en_r&#91;2:0&#93;, en&#125; ;

 end

 end

 

 //(1) 16 组移位寄存器

 reg &#91;11:0&#93; xin_reg&#91;15:0&#93;;

 reg &#91;3:0&#93; i, j ;

 always @&#40;posedge clk or negedge rstn&#41; begin

 if &#40;!rstn&#41; begin

 for &#40;i=0; i<15; i=i+1&#41; begin

 xin_reg&#91;i&#93; <= 12'b0;

 end

 end

 else if &#40;en&#41; begin

 xin_reg&#91;0&#93; <= xin ;

 for &#40;j=0; j<15; j=j+1&#41; begin

 xin_reg&#91;j+1&#93; <= xin_reg&#91;j&#93; ; //周期性移位操作

 end

 end

 end

 

 //Only 8 multipliers needed because of the symmetry of FIR filter coefficient

 //(2) 系数对称，16个移位寄存器数据进行首位相加

 reg &#91;12:0&#93; add_reg&#91;7:0&#93;;

 always @&#40;posedge clk or negedge rstn&#41; begin

 if &#40;!rstn&#41; begin

 for &#40;i=0; i<8; i=i+1&#41; begin

 add_reg&#91;i&#93; <= 13'd0 ;

 end

 end

 else if &#40;en_r&#91;0&#93;&#41; begin

 for &#40;i=0; i<8; i=i+1&#41; begin

 add_reg&#91;i&#93; <= xin_reg&#91;i&#93; + xin_reg&#91;15-i&#93; ;

 end

 end

 end

 

 //(3) 8个乘法器

 // 滤波器系数，已经过一定倍数的放大

 wire &#91;11:0&#93; coe&#91;7:0&#93; ;

 assign coe&#91;0&#93; = 12'd11 ;

 assign coe&#91;1&#93; = 12'd31 ;

 assign coe&#91;2&#93; = 12'd63 ;

 assign coe&#91;3&#93; = 12'd104 ;

 assign coe&#91;4&#93; = 12'd152 ;

 assign coe&#91;5&#93; = 12'd198 ;

 assign coe&#91;6&#93; = 12'd235 ;

 assign coe&#91;7&#93; = 12'd255 ;

 reg &#91;24:0&#93; mout&#91;7:0&#93;; 

 

`ifdef SAFE_DESIGN

 //流水线式乘法器

 wire &#91;7:0&#93; valid_mult ;

 genvar k ;

 generate

 for &#40;k=0; k<8; k=k+1&#41; begin

 mult_man #&#40;13, 12&#41;

 u_mult_paral &#40;

 .clk &#40;clk&#41;,

 .rstn &#40;rstn&#41;,

 .data_rdy &#40;en_r&#91;1&#93;&#41;,

 .mult1 &#40;add_reg&#91;k&#93;&#41;,

 .mult2 &#40;coe&#91;k&#93;&#41;,

 .res_rdy &#40;valid_mult&#91;k&#93;&#41;, //所有输出使能完全一致 

 .res &#40;mout&#91;k&#93;&#41;

 &#41;;

 end

 endgenerate

 wire valid_mult7 = valid_mult&#91;7&#93; ;

 

`else

 //如果对时序要求不高，可以直接用乘号

 always @&#40;posedge clk or negedge rstn&#41; begin

 if &#40;!rstn&#41; begin

 for &#40;i=0 ; i<8; i=i+1&#41; begin

 mout&#91;i&#93; <= 25'b0 ;

 end

 end

 else if &#40;en_r&#91;1&#93;&#41; begin

 for &#40;i=0 ; i<8; i=i+1&#41; begin

 mout&#91;i&#93; <= coe&#91;i&#93; * add_reg&#91;i&#93; ;

 end

 end

 end

 wire valid_mult7 = en_r&#91;2&#93;;

`endif

 

 //(4) 积分累加，8组25bit数据 -> 1组 29bit 数据

 //数据有效延时

 reg &#91;3:0&#93; valid_mult_r ;

 always @&#40;posedge clk or negedge rstn&#41; begin

 if &#40;!rstn&#41; begin

 valid_mult_r&#91;3:0&#93; <= 'b0 ;

 end

 else begin

 valid_mult_r&#91;3:0&#93; <= &#123;valid_mult_r&#91;2:0&#93;, valid_mult7&#125; ;

 end

 end

`ifdef SAFE_DESIGN

 //加法运算时，分多个周期进行流水，优化时序

 reg &#91;28:0&#93; sum1 ;

 reg &#91;28:0&#93; sum2 ;

 reg &#91;28:0&#93; yout_t ;

 always @&#40;posedge clk or negedge rstn&#41; begin

 if &#40;!rstn&#41; begin

 sum1 <= 29'd0 ;

 sum2 <= 29'd0 ;

 yout_t <= 29'd0 ;

 end

 else if&#40;valid_mult7&#41; begin

 sum1 <= mout&#91;0&#93; + mout&#91;1&#93; + mout&#91;2&#93; + mout&#91;3&#93; ;

 sum2 <= mout&#91;4&#93; + mout&#91;5&#93; + mout&#91;6&#93; + mout&#91;7&#93; ;

 yout_t <= sum1 + sum2 ;

 end

 end

 

`else 

 //一步计算累加结果，但是实际中时序非常危险

 reg signed &#91;28:0&#93; sum ;

 reg signed &#91;28:0&#93; yout_t ;

 always @&#40;posedge clk or negedge rstn&#41; begin

 if &#40;!rstn&#41; begin

 sum <= 29'd0 ;

 yout_t <= 29'd0 ;

 end

 else if &#40;valid_mult7&#41; begin

 sum <= mout&#91;0&#93; + mout&#91;1&#93; + mout&#91;2&#93; + mout&#91;3&#93; + mout&#91;4&#93; + mout&#91;5&#93; + mout&#91;6&#93; + mout&#91;7&#93;;

 yout_t <= sum ;

 end

 end 

`endif

 assign yout = yout_t ;

 assign valid = valid_mult_r&#91;0&#93;;

endmodule

---

## 31. 7.3 Verilog 串行 FIR 滤波器设计

### 串行 FIR 滤波器设计


**设计说明**


设计参数不变，与并行 FIR 滤波器参数一致。即，输入频率为 7.5 MHz 和 250 KHz 的正弦波混合信号，经过 FIR 滤波器后，高频信号 7.5MHz 被滤除，只保留 250KMHz 的信号。


```
输入频率： 7.5MHz 和 250KHz
采样频率： 50MHz
阻带： 1MHz-6MHz
阶数： 15 （N=15）
```

 

串行设计，就是在 16 个时钟周期内对 16 个延时数据分时依次进行乘法、加法运算，然后在时钟驱动下输出滤波值。考虑到 FIR 滤波器系数的对称性，计算一个滤波输出值的周期可以减少到 8 个。串行设计时每个周期只进行一次乘法运算，所以设计中只需一个乘法器即可。此时数据需要每 8 个时钟周期有效输入一次，但是为了保证输出信号频率的正确性，工作时钟需要为采样频率的 8 倍，即 400MHz。这种方法的优点是资源耗费少，但是工作频率要求高，数据不能持续输出。

**串行设计**


设计中使用到的乘法器模块代码，可参考之前流水线式设计的乘法器。

为方便快速仿真，也可以直接使用乘号 * 完成乘法运算，设计中加入宏定义 SAFE_DESIGN 来选择使用哪种乘法器。


FIR 滤波器系数可由 matlab 生成，具体见附录。 

## 实例
 
/**********************************************************

>> Description : fir study with serial tech

>> V190403 : Fs:50Mhz, fstop:1-6Mhz, order:16, sys clk:400MHz

***********************************************************/

`define SAFE_DESIGN

 

module fir_serial_low&#40;

 input rstn,

 input clk, // 系统工作时钟，400MHz

 input en , // 输入数据有效信号

 input &#91;11:0&#93; xin, // 输入混合频率的信号数据

 output valid, // 输出数据有效信号

 output &#91;28:0&#93; yout // 输出数据

 &#41;;

 

 //delay of input data enable

 reg &#91;11:0&#93; en_r ;

 always @&#40;posedge clk or negedge rstn&#41; begin

 if &#40;!rstn&#41; begin

 en_r&#91;11:0&#93; <= 'b0 ;

 end

 else begin

 en_r&#91;11:0&#93; <= &#123;en_r&#91;10:0&#93;, en&#125; ;

 end

 end

 

 //fir coeficient

 wire &#91;11:0&#93; coe&#91;7:0&#93; ;

 assign coe&#91;0&#93; = 12'd11 ;

 assign coe&#91;1&#93; = 12'd31 ;

 assign coe&#91;2&#93; = 12'd63 ;

 assign coe&#91;3&#93; = 12'd104 ;

 assign coe&#91;4&#93; = 12'd152 ;

 assign coe&#91;5&#93; = 12'd198 ;

 assign coe&#91;6&#93; = 12'd235 ;

 assign coe&#91;7&#93; = 12'd255 ;

 

 //(1) 输入数据移位部分 

 reg &#91;2:0&#93; cnt ;

 integer i, j ;

 always @&#40;posedge clk or negedge rstn&#41; begin

 if &#40;!rstn&#41; begin

 cnt <= 3'b0 ;

 end

 else if &#40;en || cnt != 0&#41; begin

 cnt <= cnt + 1'b1 ; //8个周期计数

 end

 end

 

 reg &#91;11:0&#93; xin_reg&#91;15:0&#93;;

 always @&#40;posedge clk or negedge rstn&#41; begin

 if &#40;!rstn&#41; begin

 for &#40;i=0; i<16; i=i+1&#41; begin

 xin_reg&#91;i&#93; <= 12'b0;

 end

 end

 else if &#40;cnt == 3'd0 && en&#41; begin //每8个周期读入一次有效数据

 xin_reg&#91;0&#93; <= xin ;

 for &#40;j=0; j<15; j=j+1&#41; begin

 xin_reg&#91;j+1&#93; <= xin_reg&#91;j&#93; ; // 数据移位

 end

 end

 end

 

 //(2) 系数对称，16个移位寄存器数据进行首位相加

 reg &#91;11:0&#93; add_a, add_b ;

 reg &#91;11:0&#93; coe_s ;

 wire &#91;12:0&#93; add_s ;

 wire &#91;2:0&#93; xin_index = cnt>=1 ? cnt-1 : 3'd7 ;

 always @&#40;posedge clk or negedge rstn&#41; begin

 if &#40;!rstn&#41; begin

 add_a <= 13'b0 ;

 add_b <= 13'b0 ;

 coe_s <= 12'b0 ;

 end

 else if &#40;en_r&#91;xin_index&#93;&#41; begin //from en_r[1]

 add_a <= xin_reg&#91;xin_index&#93; ;

 add_b <= xin_reg&#91;15-xin_index&#93; ;

 coe_s <= coe&#91;xin_index&#93; ;

 end

 end

 assign add_s = &#123;add_a&#125; + &#123;add_b&#125; ; 

 

 //(3) 乘法运算，只用一个乘法

 reg &#91;24:0&#93; mout ;

`ifdef SAFE_DESIGN

 wire en_mult ;

 wire &#91;3:0&#93; index_mult = cnt>=2 ? cnt-1 : 4'd7 + cnt&#91;0&#93; ;

 mult_man #&#40;13, 12&#41; u_mult_single //例化自己设计的流水线乘法器

 &#40;.clk &#40;clk&#41;,

 .rstn &#40;rstn&#41;,

 .data_rdy &#40;en_r&#91;index_mult&#93;&#41;, //注意数据时序对应

 .mult1 &#40;add_s&#41;,

 .mult2 &#40;coe_s&#41;,

 .res_rdy &#40;en_mult&#41;, 

 .res &#40;mout&#41;

 &#41;;

 

`else

 always @&#40;posedge clk or negedge rstn&#41; begin

 if &#40;!rstn&#41; begin

 mout <= 25'b0 ;

 end

 else if &#40;|en_r&#91;8:1&#93;&#41; begin

 mout <= coe_s * add_s ; //直接乘

 end

 end

 wire en_mult = en_r&#91;2&#93;;

`endif

 

 //(4) 积分累加，8组25bit数据 -> 1组 29bit 数据

 reg &#91;28:0&#93; sum ;

 reg valid_r ;

 //mult output en counter

 reg &#91;4:0&#93; cnt_acc_r ;

 always @&#40;posedge clk or negedge rstn&#41; begin

 if &#40;!rstn&#41; begin

 cnt_acc_r <= 'b0 ;

 end

 else if &#40;cnt_acc_r == 5'd7&#41; begin //计时8个周期

 cnt_acc_r <= 'b0 ;

 end

 else if &#40;en_mult || cnt_acc_r != 0&#41; begin //只要en有效，计时不停

 cnt_acc_r <= cnt_acc_r + 1'b1 ;

 end

 end

 

 always @&#40;posedge clk or negedge rstn&#41; begin

 if &#40;!rstn&#41; begin

 sum <= 29'd0 ;

 valid_r <= 1'b0 ;

 end

 else if &#40;cnt_acc_r == 5'd7&#41; begin //在第8个累加周期输出滤波值

 sum <= sum + mout;

 valid_r <= 1'b1 ;

 end

 else if &#40;en_mult && cnt_acc_r == 0&#41; begin //初始化

 sum <= mout ;

 valid_r <= 1'b0 ;

 end

 else if &#40;cnt_acc_r != 0&#41; begin //acculating between cycles

 sum <= sum + mout ;

 valid_r <= 1'b0 ;

 end

 end

 

 //时钟锁存有效的输出数据，为了让输出信号不是那么频繁的变化

 reg &#91;28:0&#93; yout_r ;

 always @&#40;posedge clk or negedge rstn&#41; begin

 if &#40;!rstn&#41; begin

 yout_r <= 'b0 ;

 end

 else if &#40;valid_r&#41; begin

 yout_r <= sum ;

 end

 end

 assign yout = yout_r ;

 

 //(5) 输出数据有效延迟，即滤波数据丢掉前15个滤波值

 reg &#91;4:0&#93; cnt_valid ;

 always @&#40;posedge clk or negedge rstn&#41; begin

 if &#40;!rstn&#41; begin

 cnt_valid <= 'b0 ;

 end

 else if &#40;valid_r && cnt_valid != 5'd16&#41; begin

 cnt_valid <= cnt_valid + 1'b1 ;

 end

 end

 assign valid = &#40;cnt_valid == 5'd16&#41; & valid_r ;

endmodule

---

## 32. 7.4 Verilog CIC 滤波器设计

积分梳状滤波器（CIC，Cascaded Integrator Comb），一般用于数字下变频（DDC）和数字上变频（DUC）系统。CIC 滤波器结构简单，没有乘法器，只有加法器、积分器和寄存器，资源消耗少，运算速率高，可实现高速滤波，常用在输入采样率最高的第一级，在多速率信号处理系统中具有着广泛应用。


### DDC 原理


**DDC 工作原理**

DDC 主要由本地振荡器（NCO） 、混频器、滤波器等组成，如下图所示。

![](https://www.runoob.com/wp-content/uploads/2020/10/2m4NPzvfZ6t05QJR.png)


DDC 将中频信号与振荡器产生的载波信号进行混频，信号中心频率被搬移，再经过抽取滤波，恢复原始信号，实现了下变频功能。


中频数据采样时，需要很高的采样频率来确保 ADC（模数转换器）采集到信号的信噪比。经过数字下变频后，得到的基带信号采样频率仍然是 ADC 采样频率，所以数据率很高。此时基带信号的有效带宽往往已经远小于采样频率，所以利用抽取、滤波进行数据速率的转换，使采样率降低，避免资源的浪费和设计的困难，就成为 DDC 不可缺少的一部分。


而采用 CIC 滤波器进行数据处理，是 DDC 抽取滤波部分最常用的方法。

**带通采样定理**

在 DDC 系统中，输入的中频载波信号会根据载波频率进行频移，得到一个带通信号。如果此时仍然采用奈奎斯特采样定理，即采样频率为带通信号最高频率的两倍，那么此时所需的采样频率将会很高，设计会变的复杂。此时可按照带通采样定理来确定抽样频率。


带通采样定理：一个频带限制在
![](https://www.runoob.com/wp-content/uploads/2020/10/CB3Gz6OG3lRqyVeU.png)
的连续带通信号，带宽为
![](https://www.runoob.com/wp-content/uploads/2020/10/jWnH9TDjFfjOqy98.png)
。令
![](https://www.runoob.com/wp-content/uploads/2020/10/sekAtl6NmQKRoyEH.png)
 ，其中 N 为不大于
 
![](https://www.runoob.com/wp-content/uploads/2020/10/9NIJyfr2X4H3ers2.png)
的最大正整数，如果采样频率满足条件：

![](https://www.runoob.com/wp-content/uploads/2020/10/C9desSSp3KHHparq.png)


则该信号完全可以由其采样值无失真的重建。


当 m=1 时，带通采样定理便是奈奎斯特采样定理。


带通采样定理的另一种描述方式为：若信号最高频率为信号带宽的整数倍，采样频率只需大于信号带宽的两倍即可，此时不会发生频谱混叠。


所以，可以认为采样频率的一半是 CIC 滤波器的截止频率。

**DDC 频谱搬移**


例如一个带宽信号中心频率为 60MHz，带宽为 8MHz, 则频率范围为 56MHz ~ 64MHz，m 的可取值范围为 0 ~ 7。取 m=1, 则采样频率范围为 64MHz ~ 112MHz。


取采样频率为 80MHz，设 NCO 中心频率为 20 MHz，下面讨论复信号频谱搬移示意图。


（1）考虑频谱的对称性，输入复信号的频谱示意图如下：

![](https://www.runoob.com/wp-content/uploads/2020/10/GjRsFhR9juwnNAQI.png)


（2）80MHz 采样频率采样后，56~64MHz 的频带被搬移到了 -24~ -16MHz 与 136 ~ 144MHz（高于采样频率被滤除）的频带处，-64~ -56MHz 的频带被搬移到 -144~ -136MHz（高于采样频率被滤除）与 16~24MHz 的频带处。


采样后频带分布如下：

![](https://www.runoob.com/wp-content/uploads/2020/10/kPZgwGWzUVoiUHAn.png)


（3）信号经过 20MHz NCO 的正交电路后， -24~ -16MHz 的频带被搬移到 -4~4MHz 与 -44~ -36MHz 的频带处，16~24MHz 的频带被搬移到 -4~4MHz 与 36~44MHz 的频带处，如下所示。

![](https://www.runoob.com/wp-content/uploads/2020/10/ssJHBTZboUUiAUVl.png)


（4）此时中频输入的信号已经被搬移到零中频基带处。

-44~ -36MHz 和 36~44MHz 的带宽信号是不需要的，可以滤除；-4~4MHz 的零中频信号数据速率仍然是 80MHz，可以进行抽取降低数据速率。而 CIC 滤波，就是要完成这个过程。


上述复习了很多数字信号处理的内容，权当抛 DDC 的砖，引 CIC 的玉。


### CIC 滤波器原理


**单级 CIC 滤波器**


设滤波器抽取倍数为 D，则单级滤波器的冲激响应为：

![](https://www.runoob.com/wp-content/uploads/2020/10/g6tPam4PJNf6JCYG.png)


对其进行 z 变换，可得单级 CIC 滤波器的系统函数为：

![](https://www.runoob.com/wp-content/uploads/2020/10/UmSSUeYZTs5MRaYz.png)


令

![](https://www.runoob.com/wp-content/uploads/2020/10/QU2gINl3LaIfRItM.png)


可以看出，单级 CIC 滤波器包括两个基本组成部分：积分部分和梳状部分，结构图如下：

![](https://www.runoob.com/wp-content/uploads/2020/10/oiOOZjhrW4cYhcGq.png)



**积分器**


积分器是一个单级点的 IIR（Infinite Impulse Response，无限长脉冲冲激响应）滤波器，且反馈系数为 1，其状态方程和系统函数分别为：

![](https://www.runoob.com/wp-content/uploads/2020/10/qL6qNZcXBKWxZ4ul.png)


![](https://www.runoob.com/wp-content/uploads/2020/10/EFBW6lL9mBQoxQNO.png)


**梳状器**

梳状器是一个 FIR 滤波器，其状态方程和系统函数分别为：



![](https://www.runoob.com/wp-content/uploads/2020/10/v1GMYTF5Mrb55Z84.png)



![](https://www.runoob.com/wp-content/uploads/2020/10/LLqkUraVGcQdoYDZ.png)


**抽取器**


在积分器之后，还有一个抽取器，抽取倍数与梳状器的延时参数是一致的。利用 z 变换的性质进行恒等变换，将抽取器移动到积分器与梳状器之间，可得到单级 CIC 滤波器结构，如下所示。



![](https://www.runoob.com/wp-content/uploads/2020/10/Qfte9w0ahwOmo2o3.png)



**参数说明**


CIC 滤波器结构变换之前的参数 D 可以理解为梳状滤波器的延时或阶数；变换之后，D 的含义 变为抽取倍数，而此时梳状滤波器的延时为 1，即阶数为 1。


很多学者会引入一个变量 M，表示梳状器每一级的延时，此时梳妆部分的延时就不为 1 了。那么梳状器的系统函数就变为：

![](https://www.runoob.com/wp-content/uploads/2020/10/yHsYHzAeVvbB8A6j.png)


其实把 DM 整体理解为单级滤波器延时，或者抽取倍数，也都是可以的。可能实现的方式或结构不同，但是最后的结果都是一样的。本次设计中，单级滤波器延时都为 M=1，即抽取倍数与滤波延时相同。

**多级 CIC 滤波器**


单级 CIC 滤波器的阻带衰减较差，为了提高滤波效果，抽取滤波时往往会采用多级 CIC 滤波器级联的结构。


实现多级直接级联的 CIC 滤波器在设计和资源上并不是最优的方式，需要对其结构进行调整。如下所示，将积分器和梳状滤波器分别移至一组，并将抽取器移到梳状滤波器之前。先抽取再进行滤波，可以减少数据处理的长度，节约硬件资源。

![](https://www.runoob.com/wp-content/uploads/2020/10/Vvzxwfm3XATUytdT.jpg)



当然，级联数越大，旁瓣抑制越好，但是通带内的平坦度也会变差。所以级联数不宜过多，一般最多 5 级。

### CIC 滤波器设计


**设计说明**


CIC 滤波器本质上就是一个简单的低通滤波器，截止频率为采样频率除以抽取倍数后的一半。输入数据信号仍然是 7.5MHz 和 250KHz，采样频率 50MHz。抽取倍数设置为 5，则截止频率为 5MHz，小于 7.5MHz，可以滤除 7.5MHz 的频率成分。设计参数如下：


```
输入频率： 7.5MHz 和 250KHz
采样频率： 50MHz
阻带： 5MHz 
阶数： 1（M=1）
级数： 3（N=3）
```



关于积分时中间数据信号的位宽，很多地方给出了不同的计算方式，计算结果也大相径庭。这里总结一下使用最多的计算方式：

![](https://www.runoob.com/wp-content/uploads/2020/10/X5JtffBUWSt61xBG.png)


其中，D 为抽取倍数，M 为滤波器阶数，N 为滤波器级数。抽取倍数为 5，滤波器阶数为 1，滤波器级联数为 3，取输入信号数据位宽为 12bit，对数部分向上取整，则积分后数据不溢出的中间信号位宽为 21bit。


为了更加宽裕的设计，滤波器阶数如果理解为未变换结构前的多级 CIC 滤波器直接型结构，则滤波器阶数可以认为是 5，此时中间信号最大位宽为 27bit。

**积分器设计**


根据输入数据的有效信号的控制，积分器做一个简单的累加即可，注意数据位宽。

## 实例
 
//3 stages integrator

module integrator

 #&#40;parameter NIN = 12,

 parameter NOUT = 21&#41;

 &#40;

 input clk ,

 input rstn ,

 input en ,

 input &#91;NIN-1:0&#93; din ,

 output valid ,

 output &#91;NOUT-1:0&#93; dout&#41; ;

 reg &#91;NOUT-1:0&#93; int_d0 ;

 reg &#91;NOUT-1:0&#93; int_d1 ;

 reg &#91;NOUT-1:0&#93; int_d2 ;

 wire &#91;NOUT-1:0&#93; sxtx = &#123;&#123;&#40;NOUT-NIN&#41;&#123;1'b0&#125;&#125;, din&#125; ;

 //data input enable delay

 reg &#91;2:0&#93; en_r ;

 always @&#40;posedge clk or negedge rstn&#41; begin

 if &#40;!rstn&#41; begin

 en_r <= 'b0 ;

 end

 else begin

 en_r <= &#123;en_r&#91;1:0&#93;, en&#125;;

 end

 end

 //integrator

 //stage1

 always @&#40;posedge clk or negedge rstn&#41; begin

 if &#40;!rstn&#41; begin

 int_d0 <= 'b0 ;

 end

 else if &#40;en&#41; begin

 int_d0 <= int_d0 + sxtx ;

 end

 end

 //stage2

 always @&#40;posedge clk or negedge rstn&#41; begin

 if &#40;!rstn&#41; begin

 int_d1 <= 'b0 ;

 end

 else if &#40;en_r&#91;0&#93;&#41; begin

 int_d1 <= int_d1 + int_d0 ;

 end

 end

 //stage3

 always @&#40;posedge clk or negedge rstn&#41; begin

 if &#40;!rstn&#41; begin

 int_d2 <= 'b0 ;

 end

 else if &#40;en_r&#91;1&#93;&#41; begin

 int_d2 <= int_d2 + int_d1 ;

 end

 end

 assign dout = int_d2 ;

 assign valid = en_r&#91;2&#93;;

endmodule

---

## 33. 7.6 Verilog DDS 设计

### DDS 原理


DDS（直接频率合成）技术是根据奈奎斯特抽样定理及数字处理技术，把一系列的模拟信号进行不失真的抽样，将得到的数字信号存储在存储器中，并在时钟的控制下，通过数模转换，将数字量变成模拟信号的方法。


DDS 模块主要由相位累加器、查找表、DAC 转换器和低通滤波器组成，基本结构如下。

![](https://www.runoob.com/wp-content/uploads/2020/10/KogSsjzSTCoDbr9S.png)


相位累加器，是 DDS 的核心组成部分，用于实现相位的累加，并输出相应的幅值。相位累加器由 ***M*** 位宽加法器和 ***M*** 位宽寄存器组成，通过时钟控制，将上一次累加结果反馈到加法器输入端实现累加功能，从而使每个时钟周期内的相位递增数为 ***K***，并取相位累加结果作为地址输出给 ROM 查找表部分。

幅值查找表，存储着每个相位对应的二进制数字幅度。在每个时钟周期内，查找表对相位累加器输出的相位地址信息进行寻址，然后输出对应的二进制幅度数字离散值。假设查找表地址为 ***M*** 位，输出数据为 ***N*** 位，则查找表的容量大小为 
![](https://www.runoob.com/wp-content/uploads/2020/10/mHuZv2REp4ZSscYO.png)
。不难看出，输出信号的相位分辨率为：

![](https://www.runoob.com/wp-content/uploads/2020/10/u6VUBptgAYsnEfsz.png)


DAC 转换器，将数字信号转换为模拟信号。实际上，DAC 输出的信号并不是连续的，而是根据每位代码的权重，将每一位输入的数字量进行求和，然后以其分辨率为单位进行模拟的输出。实际输出的信号是阶梯状的模拟线型信号，所以要对其进行平滑处理，一般使用滤波器滤波。


低通滤波器，由于 DAC 转换器输出的模拟信号存在阶梯状的缺陷，所以要对其进行平滑处理，滤除掉大部分的杂散信号，使输出信号变为比较理想的模拟信号。


DDS 工作时，频率控制字 ***K*** 与 ***M*** 比特位的相位累加器相加，得到的结果作为相位值。在每一个时钟周期内以二进制数的形式送给 ROM 查找表，将相位信息转化为数字化的正弦幅度值，再经过数模转换转化为阶梯形状的模拟信号。待信号经过系统滤波滤除大部分的杂散信号后，就可以得到一个比较纯正的正弦波。

从频率分解的角度讲，ROM 查找表将输入频率
![](https://www.runoob.com/wp-content/uploads/2020/10/HFSJHPLQNTYMq9FG.png)
分解成了
![](https://www.runoob.com/wp-content/uploads/2020/10/VvqaxosD86lXSV2Y.png)
份，输出频率
![](https://www.runoob.com/wp-content/uploads/2020/10/RfEC3ntul1mqenQj.png)
占用的份数正是步进频率控制字 ***K***。 所以 DDS 输出频率可以表示为：

![](https://www.runoob.com/wp-content/uploads/2020/10/ixFOiN3Ey7H1EaJh.png)


从相位角度讲，在时间
![](https://www.runoob.com/wp-content/uploads/2020/10/EdPLOV7Iu42Q3JlK.png)
内由频率控制字 ***K*** 控制输出的相位增量为：

![](https://www.runoob.com/wp-content/uploads/2020/10/aIwftzwEvHgksl5J.png)


考虑此时输出频率的角速度
![](https://www.runoob.com/wp-content/uploads/2020/10/1Xm1rQpV0y9b7IbK.png)
，时间
![](https://www.runoob.com/wp-content/uploads/2020/10/EdPLOV7Iu42Q3JlK-1.png)
内输出频率的相位增量还可以表示为：

![](https://www.runoob.com/wp-content/uploads/2020/10/Q1XTz6YsiNB3lwch.png)


由上述两式也可以推导出 DDS 输出频率与输入频率之间的关系。


### DDS 设计


**设计说明**


下面只对 DAC 之前的 DDS 电路进行设计。


设计的 DDS 特性有：

- 
1）频率可控；
- 
2）起始相位可控；
- 
3）幅值可控；
- 
4）正弦波、三角波和方波可选择输出；
- 
5）资源优化：波形存储文件只采用了四分之一的正弦波数据。

**生成 ROM**


ROM 模块最好使用定制的 ip 核，时序和面积都会有更好的优化。定制的 ROM 还需要指定数据文件，例如 ISE 的 ROM 数据文件后缀为 .coe，Quartus II 的 ROM 数据文件后缀为 .mif。

为了方便仿真，这里用代码编写 ROM 模块，地址宽度为 8bit，数据宽度 10bit。


为了节省空间，只存四分之一的正弦波形，然后根据对称性进行平移，即可得到一个完整周期正弦波数据波形。


为实现 DDS 模式多样化，还加入了三角波、方波的 ROM 程序。


实现代码如下（全都包含在文件 mem.v 中）。

## 实例
 
module mem&#40;

 input clk, //reference clock

 input rstn , //resetn, low effective

 input en , //start to generating waves

 input &#91;1:0&#93; sel , //waves selection

 input &#91;7:0&#93; addr ,

 output dout_en ,

 output &#91;9:0&#93; dout&#41;; //data out, 10bit width

 //data out fROM ROMs

 wire &#91;9:0&#93; q_tri ;

 wire &#91;9:0&#93; q_square ;

 wire &#91;9:0&#93; q_cos ;

 //ROM addr

 reg &#91;1:0&#93; en_r ;

 always @&#40;posedge clk or negedge rstn&#41; begin

 if &#40;!rstn&#41; begin

 en_r <= 2'b0 ;

 end

 else begin

 en_r <= &#123;en_r&#91;0&#93;, en&#125; ; //delay one cycle for en

 end

 end

 assign dout = en_r&#91;1&#93; ? &#40;q_tri | q_square | q_cos&#41; : 10'b0 ;

 assign dout_en = en_r&#91;1&#93; ;

 //ROM instiation

 cos_ROM u_cos_ROM &#40;

 .clk &#40;clk&#41;,

 .en &#40;en_r&#91;0&#93; & &#40;sel == 2'b0&#41;&#41;, //sel = 0, cos wave

 .addr &#40;addr&#91;7:0&#93;&#41;,

 .q &#40;q_cos&#91;9:0&#93;&#41;&#41;;

 square_ROM u_square_ROM &#40;

 .clk &#40;clk&#41;,

 .en &#40;en_r&#91;0&#93; & sel == 2'b01&#41;, //sel = 1, square wave

 .addr &#40;addr&#91;7:0&#93;&#41;,

 .q &#40;q_square&#91;9:0&#93;&#41;&#41;;

 tri_ROM u_tri_ROM &#40;

 .clk &#40;clk&#41;,

 .en &#40;en_r&#91;0&#93; & sel == 2'b10&#41;, //sel = 2, triangle wave

 .addr &#40;addr&#91;7:0&#93;&#41;,

 .q &#40;q_tri&#91;9:0&#93;&#41;&#41;;

endmodule

//square waves ROM

module square_ROM &#40;

 input clk,

 input en,

 input &#91;7:0&#93; addr,

 output reg &#91;9:0&#93; q&#41;;

 

 //1 in first half cycle, and 0 in second half cycle

 always @&#40;posedge clk&#41; begin

 if &#40;en&#41; begin

 q <= &#123; 10&#123;&#40;addr < 128&#41;&#125; &#125;; 

 end

 else begin

 q <= 'b0 ;

 end

 end

endmodule

 //triangle waves ROM

module tri_ROM &#40;

 input clk,

 input en,

 input &#91;7:0&#93; addr,

 output reg &#91;9:0&#93; q&#41;;

 //rising edge, addr -> 0x0, 0x3f

 always @&#40;posedge clk&#41; begin

 if &#40;en&#41; begin

 if &#40;addr < 128&#41; begin

 q <= &#123;addr&#91;6:0&#93;, 3'b0&#125;; //rising edge 

 end

 else begin //falling edge

 q <= 10'h3ff - &#123;addr&#91;6:0&#93;, 3'b0&#125; ;

 end

 end

 else begin

 q <= 'b0 ;

 end

 end

endmodule

//Better use mem ip.

//This format is easy for simulation

module cos_ROM &#40;

 input clk,

 input en,

 input &#91;7:0&#93; addr,

 output reg &#91;9:0&#93; q&#41;;

 wire &#91;8:0&#93; ROM_t &#91;0 : 64&#93; ;

 //as the symmetry of cos function, just store 1/4 data of one cycle

 assign ROM_t&#91;0:64&#93; = &#123;

 511, 510, 510, 509, 508, 507, 505, 503,

 501, 498, 495, 492, 488, 485, 481, 476,

 472, 467, 461, 456, 450, 444, 438, 431,

 424, 417, 410, 402, 395, 386, 378, 370,

 361, 352, 343, 333, 324, 314, 304, 294,

 283, 273, 262, 251, 240, 229, 218, 207,

 195, 183, 172, 160, 148, 136, 124, 111,

 99 , 87 , 74 , 62 , 50 , 37 , 25 , 12 ,

 0 &#125; ;

 always @&#40;posedge clk&#41; begin

 if &#40;en&#41; begin

 if &#40;addr&#91;7:6&#93; == 2'b00 &#41; begin //quadrant 1, addr[0, 63]

 q <= ROM_t&#91;addr&#91;5:0&#93;&#93; + 10'd512 ; //上移

 end

 else if &#40;addr&#91;7:6&#93; == 2'b01 &#41; begin //2nd, addr[64, 127]

 q <= 10'd512 - ROM_t&#91;64-addr&#91;5:0&#93;&#93; ; //两次翻转

 end

 else if &#40;addr&#91;7:6&#93; == 2'b10 &#41; begin //3rd, addr[128, 192]

 q <= 10'd512 - ROM_t&#91;addr&#91;5:0&#93;&#93;; //翻转右移

 end

 else begin //4th quadrant, addr [193, 256]

 q <= 10'd512 + ROM_t&#91;64-addr&#91;5:0&#93;&#93;; //翻转上移

 end

 end

 else begin

 q <= 'b0 ;

 end

 end

endmodule

---

## 34. 7.5 Verilog FFT 设计

FFT（Fast Fourier Transform），快速傅立叶变换，是一种 DFT（离散傅里叶变换）的高效算法。在以时频变换分析为基础的数字处理方法中，有着不可替代的作用。


### FFT 原理


**公式推导**

DFT 的运算公式为：

![](https://www.runoob.com/wp-content/uploads/2020/10/H9juUU8XwrsEd0yc.png)


其中，

![](https://www.runoob.com/wp-content/uploads/2020/10/EhjmOcWZm03RwY9o-1.png)


将离散傅里叶变换公式拆分成奇偶项，则前 N/2 个点可以表示为：

![](https://www.runoob.com/wp-content/uploads/2020/10/ShPtKMa3r27MshcX.png)


同理，后 N/2 个点可以表示为：

![](https://www.runoob.com/wp-content/uploads/2020/10/MMmgQxwSMAEcLjjl.png)


由此可知，后 N/2 个点的值完全可以通过计算前 N/2 个点时的中间过程值确定。对 A[k] 与 B[k] 继续进行奇偶分解，直至变成 2 点的 DFT，这样就可以避免很多的重复计算，实现了快速离散傅里叶变换（FFT）的过程。

**算法结构**


8 点 FFT 计算的结构示意图如下。


由图可知，只需要简单的计算几次乘法和加法，便可完成离散傅里叶变换过程，而不是对每个数据进行繁琐的相乘和累加。

![](https://static.jyshare.com/images/mix/uuE5FKpYLflJt5EF.jpg)


**重要特性**

(1) 级的概念

每分割一次，称为一级运算。


设 FFT 运算点数为 N，共有 M 级运算，则它们满足：

![](https://www.runoob.com/wp-content/uploads/2020/10/oBL12HrkSCYT6wby.png)


每一级运算的标识为 m = 0, 1, 2, ..., M-1。


为了便于分割计算，FFT 点数 N 的取值经常为 2 的整数次幂。


(2) 蝶形单元


FFT 计算结构由若干个蝶形运算单元组成，每个运算单元示意图如下：

![](https://www.runoob.com/wp-content/uploads/2020/10/VexKYoVwuj6hn1rE.gif)


蝶形单元的输入输出满足：

![](https://www.runoob.com/wp-content/uploads/2020/10/9sP3eefIuDNwQHXP.jpg)


其中， 
![](https://www.runoob.com/wp-content/uploads/2020/10/uWayxKitgWrBaOoc.png)


每一个蝶形单元运算时，进行了一次乘法和两次加法。


每一级中，均有 N/2 个蝶形单元。


故完成一次 FFT 所需要的乘法次数和加法次数分别为：

![](https://www.runoob.com/wp-content/uploads/2020/10/CRxV0zepPlkuX52I.png)



(3) 组的概念

每一级 N/2 个蝶形单元可分为若干组，每一组有着相同的结构与
![](https://www.runoob.com/wp-content/uploads/2020/10/rEc1ZdxQpj2YT1lg.png)
因子分布。


例如 m=0 时，可以分为 N/2=4 组。

m=1 时，可以分为 N/4=2 组。

m=M-1 时，此时只能分为 1 组。


(4) 
![](https://www.runoob.com/wp-content/uploads/2020/10/rEc1ZdxQpj2YT1lg.png)
因子分布

![](https://www.runoob.com/wp-content/uploads/2020/10/pSLdneHbbRSopxSr.png)
因子存在于 m 级，其中 
![](https://www.runoob.com/wp-content/uploads/2020/10/4SUEFQHUCuPswYnR.png)
。

在 8 点 FFT 第二级运算中，即 m=1 ，蝶形运算因子可以化简为：

![](https://www.runoob.com/wp-content/uploads/2020/10/c1RNmtc0hUnyRWbY.png)



(5) 码位倒置


对于 N=8 点的 FFT 计算，X(0) ~ X(7) 位置对应的 2 进制码为：

```
X(000), X(001), X(010), X(011), X(100), X(101), X(110), X(111)
```


将其位置的 2 进制码进行翻转：

```
X(000), X(100), X(010), X(110), X(001), X(101), X(011), X(111)
```


此时位置对应的 10 进制为：

```
X(0), X(4), X(2), X(6), X(1), X(5), X(3), X(7)
```


恰好对应 FFT 第一级输入数据的顺序。

该特性有利于 FFT 的编程实现。


### FFT 设计


**设计说明**


为了利用仿真简单的说明 FFT 的变换过程，数据点数取较小的值 8。


如果数据是串行输入，需要先进行缓存，所以设计时数据输入方式为并行。


数据输入分为实部和虚部共 2 部分，所以计算结果也分为实部和虚部。


设计采用流水结构，暂不考虑资源消耗的问题。


为了使设计结构更加简单，这里做一步妥协，乘法计算直接使用乘号。如果 FFT 设计应用于实际，一定要将乘法结构换成可以流水的乘法器，或使用官方提供的效率较高的乘法器 IP。

**蝶形单元设计**


蝶形单元为定点运算，需要对旋转因子进行定点量化。


借助 matlab 将旋转因子扩大 8192 倍（左移 13 位），可参考附录。


为了防止蝶形运算中的乘法和加法导致位宽逐级增大，每一级运算完成后，要对输出数据进行固定位宽的截位，也可去掉旋转因子倍数增大而带来的影响。
代码如下：

## 实例
 
`timescale 1ns/100ps

/**************** butter unit *************************

Xm(p) ------------------------> Xm+1(p)

 - ->

 - -

 -

 - -

 - ->

Xm(q) ------------------------> Xm+1(q)

 Wn -1

*//////////////////////////////////////////////////////

module butterfly

 &#40;

 input clk,

 input rstn,

 input en,

 input signed &#91;23:0&#93; xp_real, // Xm(p)

 input signed &#91;23:0&#93; xp_imag,

 input signed &#91;23:0&#93; xq_real, // Xm(q)

 input signed &#91;23:0&#93; xq_imag,

 input signed &#91;15:0&#93; factor_real, // Wnr

 input signed &#91;15:0&#93; factor_imag,

 output valid,

 output signed &#91;23:0&#93; yp_real, //Xm+1(p)

 output signed &#91;23:0&#93; yp_imag,

 output signed &#91;23:0&#93; yq_real, //Xm+1(q)

 output signed &#91;23:0&#93; yq_imag&#41;;

 reg &#91;4:0&#93; en_r ;

 always @&#40;posedge clk or negedge rstn&#41; begin

 if &#40;!rstn&#41; begin

 en_r <= 'b0 ;

 end

 else begin

 en_r <= &#123;en_r&#91;3:0&#93;, en&#125; ;

 end

 end

 //=====================================================//

 //(1.0) Xm(q) mutiply and Xm(p) delay

 reg signed &#91;39:0&#93; xq_wnr_real0;

 reg signed &#91;39:0&#93; xq_wnr_real1;

 reg signed &#91;39:0&#93; xq_wnr_imag0;

 reg signed &#91;39:0&#93; xq_wnr_imag1;

 reg signed &#91;39:0&#93; xp_real_d;

 reg signed &#91;39:0&#93; xp_imag_d;

 always @&#40;posedge clk or negedge rstn&#41; begin

 if &#40;!rstn&#41; begin

 xp_real_d <= 'b0;

 xp_imag_d <= 'b0;

 xq_wnr_real0 <= 'b0;

 xq_wnr_real1 <= 'b0;

 xq_wnr_imag0 <= 'b0;

 xq_wnr_imag1 <= 'b0;

 end

 else if &#40;en&#41; begin

 xq_wnr_real0 <= xq_real * factor_real;

 xq_wnr_real1 <= xq_imag * factor_imag;

 xq_wnr_imag0 <= xq_real * factor_imag;

 xq_wnr_imag1 <= xq_imag * factor_real;

 //expanding 8192 times as Wnr

 xp_real_d <= &#123;&#123;4&#123;xp_real&#91;23&#93;&#125;&#125;, xp_real&#91;22:0&#93;, 13'b0&#125;; 

 xp_imag_d <= &#123;&#123;4&#123;xp_imag&#91;23&#93;&#125;&#125;, xp_imag&#91;22:0&#93;, 13'b0&#125;;

 end

 end

 //(1.1) get Xm(q) mutiplied-results and Xm(p) delay again

 reg signed &#91;39:0&#93; xp_real_d1;

 reg signed &#91;39:0&#93; xp_imag_d1;

 reg signed &#91;39:0&#93; xq_wnr_real;

 reg signed &#91;39:0&#93; xq_wnr_imag;

 always @&#40;posedge clk or negedge rstn&#41; begin

 if &#40;!rstn&#41; begin

 xp_real_d1 <= 'b0;

 xp_imag_d1 <= 'b0;

 xq_wnr_real <= 'b0 ;

 xq_wnr_imag <= 'b0 ;

 end

 else if &#40;en_r&#91;0&#93;&#41; begin

 xp_real_d1 <= xp_real_d;

 xp_imag_d1 <= xp_imag_d;

 //提前设置好位宽余量，防止数据溢出

 xq_wnr_real <= xq_wnr_real0 - xq_wnr_real1 ; 

 xq_wnr_imag <= xq_wnr_imag0 + xq_wnr_imag1 ;

 end

 end

 //======================================================//

 //(2.0) butter results

 reg signed &#91;39:0&#93; yp_real_r;

 reg signed &#91;39:0&#93; yp_imag_r;

 reg signed &#91;39:0&#93; yq_real_r;

 reg signed &#91;39:0&#93; yq_imag_r;

 always @&#40;posedge clk or negedge rstn&#41; begin

 if &#40;!rstn&#41; begin

 yp_real_r <= 'b0;

 yp_imag_r <= 'b0;

 yq_real_r <= 'b0;

 yq_imag_r <= 'b0;

 end

 else if &#40;en_r&#91;1&#93;&#41; begin

 yp_real_r <= xp_real_d1 + xq_wnr_real;

 yp_imag_r <= xp_imag_d1 + xq_wnr_imag;

 yq_real_r <= xp_real_d1 - xq_wnr_real;

 yq_imag_r <= xp_imag_d1 - xq_wnr_imag;

 end

 end

 //(3) discard the low 13bits because of Wnr

 assign yp_real = &#123;yp_real_r&#91;39&#93;, yp_real_r&#91;13+23:13&#93;&#125;;

 assign yp_imag = &#123;yp_imag_r&#91;39&#93;, yp_imag_r&#91;13+23:13&#93;&#125;;

 assign yq_real = &#123;yq_real_r&#91;39&#93;, yq_real_r&#91;13+23:13&#93;&#125;;

 assign yq_imag = &#123;yq_imag_r&#91;39&#93;, yq_imag_r&#91;13+23:13&#93;&#125;;

 assign valid = en_r&#91;2&#93;;

endmodule

---

## 35. 7.1 Verilog 除法器设计

### 除法器原理（定点）


和十进制除法类似，计算 27 除以 5 的过程如下所示：

![](https://www.runoob.com/wp-content/uploads/2020/09/KGUCofhbNPJRkGv3.png)



除法运算过程如下：

- 
(1) 取被除数的高几位数据，位宽和除数相同（实例中是 3bit 数据）。
- 
(2) 将被除数高位数据与除数作比较，如果前者不小于后者，则可得到对应位的商为 1，两者做差得到第一步的余数；否则得到对应的商为 0，将前者直接作为余数。
- 
(3) 将上一步中的余数与被除数剩余最高位 1bit 数据拼接成新的数据，然后再和除数做比较。可以得到新的商和余数。
- 
(4) 重复过程 (3)，直到被除数最低位数据也参与计算。


需要说明的是，商的位宽应该与被除数保持一致，因为除数有可能为1。**所以上述手动计算除法的实例中，第一步做比较时，应该取数字 27 最高位 1 (3'b001) 与 3'b101 做比较。**
根据此计算过程，设计位宽可配置的流水线式除法器，流水延迟周期个数与被除数位宽一致。


### 除法器设计


**单步运算设计**


单步除法计算时，单步被除数位宽（信号 dividend）需比原始除数（信号 divisor）位宽多 1bit 才不至于溢出。


为了便于流水，输出端需要有寄存器来存储原始的除数（信号 divisor 和 divisor_kp）和被除数信息（信号 dividend_ci 和 dividend_kp）。


单步的运算结果就是得到新的 1bit 商数据（信号 merchant）和余数（信号 remainder）。


为了得到最后的除法结果，新的 1bit 商数据（信号 merchant）还需要与上一周期的商结果（merchant_ci）进行移位累加。


单步运算单元设计如下（文件名 divider_cell.v）：

## 实例
 
// parameter M means the actual width of divisor

module divider_cell

 #&#40;parameter N=5,

 parameter M=3&#41;

 &#40;

 input clk,

 input rstn,

 input en,

 input &#91;M:0&#93; dividend,

 input &#91;M-1:0&#93; divisor,

 input &#91;N-M:0&#93; merchant_ci , //上一级输出的商

 input &#91;N-M-1:0&#93; dividend_ci , //原始除数

 output reg &#91;N-M-1:0&#93; dividend_kp, //原始被除数信息

 output reg &#91;M-1:0&#93; divisor_kp, //原始除数信息

 output reg rdy ,

 output reg &#91;N-M:0&#93; merchant , //运算单元输出商

 output reg &#91;M-1:0&#93; remainder //运算单元输出余数

 &#41;;

 always @&#40;posedge clk or negedge rstn&#41; begin

 if &#40;!rstn&#41; begin

 rdy <= 'b0 ;

 merchant <= 'b0 ;

 remainder <= 'b0 ;

 divisor_kp <= 'b0 ;

 dividend_kp <= 'b0 ;

 end

 else if &#40;en&#41; begin

 rdy <= 1'b1 ;

 divisor_kp <= divisor ; //原始除数保持不变

 dividend_kp <= dividend_ci ; //原始被除数传递

 if &#40;dividend >= &#123;1'b0, divisor&#125;&#41; begin

 merchant <= &#40;merchant_ci<<1&#41; + 1'b1 ; //商为1

 remainder <= dividend - &#123;1'b0, divisor&#125; ; //求余

 end

 else begin

 merchant <= merchant_ci<<1 ; //商为0

 remainder <= dividend ; //余数不变

 end

 end // if (en)

 else begin

 rdy <= 'b0 ;

 merchant <= 'b0 ;

 remainder <= 'b0 ;

 divisor_kp <= 'b0 ;

 dividend_kp <= 'b0 ;

 end

 end 

endmodule

---
