# 4.3 Verilog 时序控制

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