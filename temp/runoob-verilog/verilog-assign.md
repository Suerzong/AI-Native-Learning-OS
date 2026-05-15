# 3.1 Verilog 连续赋值

### 关键词：assign， 全加器


连续赋值语句是 Verilog 数据流建模的基本语句，用于对 wire 型变量进行赋值。：

格式如下

```
assign LHS_target = RHS_expression ；
```
 

LHS（left hand side） 指赋值操作的左侧，RHS（right hand side）指赋值操作的右侧。


assign 为关键词，任何已经声明 wire 变量的连续赋值语句都是以 assign 开头，例如：

```
wire Cout, A, B ;
assign Cout = A & B ; //实现计算A与B的功能
```


需要说明的是：

- 
LHS_target 必须是一个标量或者线型向量，而不能是寄存器类型。
- 
RHS_expression 的类型没有要求，可以是标量或线型或存器向量，也可以是函数调用。
- 
只要 RHS_expression 表达式的操作数有事件发生（值的变化）时，RHS_expression 就会立刻重新计算，同时赋值给 LHS_target。
 

Verilog 还提供了另一种对 wire 型赋值的简单方法，即在 wire 型变量声明的时候同时对其赋值。wire 型变量只能被赋值一次，因此该种连续赋值方式也只能有一次。例如下面赋值方式和上面的赋值例子的赋值方式，效果都是一致的。

```
wire A, B ;
wire Cout = A & B ;
```


### 全加器


下面采用数据流描述方式，来设计一个 1bit 全加器。


设 Ai，Bi，Ci 分别为被加数、加数和相邻低位的进位数，So, Co 分别为本位和与向相邻高位的进位数。


真值表如下：

| Input | | | Output | | 
| Ci | Ai | Bi | So | Co | 
| 0 | 0 | 0 | 0 | 0 | 
| 0 | 0 | 1 | 1 | 0 | 
| 0 | 1 | 0 | 1 | 0 | 
| 0 | 1 | 1 | 0 | 1 | 
| 1 | 0 | 0 | 1 | 0 | 
| 1 | 0 | 1 | 0 | 1 | 
| 1 | 1 | 0 | 0 | 1 | 
| 1 | 1 | 1 | 1 | 1 | 

全加器的表达式为：

```
So = Ai &oplus; Bi &oplus; Ci ;
Co = AiBi + Ci(Ai+Bi)
```



rtl 代码（full_adder1.v）如下：

## 实例
 
module full_adder1&#40;

 input Ai, Bi, Ci,

 output So, Co&#41;;

 

 assign So = Ai ^ Bi ^ Ci ;

 assign Co = &#40;Ai & Bi&#41; | &#40;Ci & &#40;Ai | Bi&#41;&#41;;

endmodule