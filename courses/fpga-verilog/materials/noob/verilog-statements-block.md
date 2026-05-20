# 4.4 Verilog 语句块

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