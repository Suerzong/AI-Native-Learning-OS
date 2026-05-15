# 4.6 Verilog 多路分支语句

### 关键词：case，选择器


case 语句是一种多路条件分支的形式，可以解决 if 语句中有多个条件选项时使用不方便的问题。


### case 语句


case 语句格式如下：

```
case(case_expr)
 condition1 : true_statement1 ;
 condition2 : true_statement2 ;
 &hellip;&hellip;
 default : default_statement ;
endcase
```


case 语句执行时，如果 condition1 为真，则执行 true_statement1 ; 如果 condition1 为假，condition2 为真，则执行 true_statement2；依次类推。如果各个 condition 都不为真，则执行 default_statement 语句。

default 语句是可选的，且在一个 case 语句中不能有多个 default 语句。

条件选项可以有多个，不仅限于 condition1、condition2 等，而且这些条件选项不要求互斥。虽然这些条件选项是并发比较的，但执行效果是谁在前且条件为真谁被执行。

ture_statement1 等执行语句可以是一条语句，也可以是多条。如果是多条执行语句，则需要用 begin 与 end 关键字进行说明。

**case 语句支持嵌套使用。**

下面用 case 语句代替 if 语句实现了一个 4 路选择器的功能。仿真结果与 testbench 可参考[条件语句](https://www.runoob.com/w3cnote/verilog-condition-statement.html)一章，两者完全一致。

## 实例
 
module mux4to1&#40;

 input &#91;1:0&#93; sel ,

 input &#91;1:0&#93; p0 ,

 input &#91;1:0&#93; p1 ,

 input &#91;1:0&#93; p2 ,

 input &#91;1:0&#93; p3 ,

 output &#91;1:0&#93; sout&#41;;

 

 reg &#91;1:0&#93; sout_t ;

 always @&#40;*&#41;

 case&#40;sel&#41;

 2'b00: begin 

 sout_t = p0 ;

 end

 2'b01: sout_t = p1 ;

 2'b10: sout_t = p2 ;

 default: sout_t = p3 ;

 endcase

 assign sout = sout_t ;

 

endmodule