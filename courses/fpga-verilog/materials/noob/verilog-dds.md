# 7.6 Verilog DDS 设计

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