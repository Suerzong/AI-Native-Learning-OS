# 4.8 Verilog 过程连续赋值

### 关键词：deassign，force，release


过程连续赋值是过程赋值的一种。这种赋值语句能够替换其他所有 wire 或 reg 的赋值，改写了 wire 或 reg 型变量的当前值。


与过程赋值不同的是，过程连续赋值的表达式能被连续的驱动到 wire 或 reg 型变量中，即过程连续赋值发生作用时，右端表达式中任意操作数的变化都会引起过程连续赋值语句的重新执行。


过程连续性赋值主要有 2 种，assign-deassign 和 force-release。


### assign, deassign


assign（过程赋值操作）与 deassign （取消过程赋值操作）表示第一类过程连续赋值语句。赋值对象只能是寄存器或寄存器组，而不能是 wire 型变量。


赋值过程中对寄存器连续赋值，寄存器中的值被保留直到被重新赋值。

例如，一个带复位端的 D 触发器可以用下面代码描述：

## 实例
 
module dff_normal&#40;

 input rstn,

 input clk,

 input D,

 output reg Q

 &#41;;

 always @&#40;posedge clk or negedge rstn&#41; begin

 if&#40;!rstn&#41; begin //Q = 0 after reset effective

 Q <= 1'b0 ;

 end

 else begin

 Q <= D ; //Q = D at posedge of clock

 end

 end

endmodule