# 4.7 Verilog 循环语句

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