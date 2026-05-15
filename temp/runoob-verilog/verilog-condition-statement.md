# 4.5 Verilog 条件语句

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