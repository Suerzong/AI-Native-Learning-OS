# 7.3 Verilog 串行 FIR 滤波器设计

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