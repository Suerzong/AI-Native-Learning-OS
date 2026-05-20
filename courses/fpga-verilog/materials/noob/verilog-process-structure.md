# 4.1 Verilog 过程结构

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