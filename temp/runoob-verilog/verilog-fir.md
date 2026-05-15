# 7.2 Verilog 并行 FIR 滤波器设计

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