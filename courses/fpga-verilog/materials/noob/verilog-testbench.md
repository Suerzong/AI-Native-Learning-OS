# 6.6 Verilog 仿真激励

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