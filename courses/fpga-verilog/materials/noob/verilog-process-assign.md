# 4.2 Verilog 过程赋值

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