# 2.5 Verilog 编译指令

以反引号 ` 开始的某些标识符是 Verilog 系统编译指令。

编译指令为 Verilog 代码的撰写、编译、调试等提供了极大的便利。


下面介绍下完整的 8 种编译指令，其中前 4 种使用频率较高。

### `define, `undef


在编译阶段，`define 用于文本替换，类似于 C 语言中的 **#define**。

一旦 `define 指令被编译，其在整个编译过程中都会有效。例如，在一个文件中定义：

```
`define DATA_DW 32
```


则在另一个文件中也可以直接使用 DATA_DW。

```
`define S $stop; 
//用`S来代替系统函数$stop; (包括分号)
`define WORD_DEF reg [31:0] 
//可以用`WORD_DEF来声明32bit寄存器变量
```


`undef 用来取消之前的宏定义，例如：

```
`define DATA_DW 32
&hellip;&hellip;
reg [DATA_DW-1:0] data_in ;
&hellip;&hellip;
`undef DATA_DW

`ifdef, `ifndef, `elsif, `else, `endif
```


这些属于条件编译指令。例如下面的例子中，如果定义了 MCU51，则使用第一种参数说明；如果没有定义 MCU、定义了 WINDOW，则使用第二种参数说明；如果 2 个都没有定义，则使用第三种参数说明。

```
`ifdef MCU51
 parameter DATA_DW = 8 ;
`elsif WINDOW
 parameter DATA_DW = 64 ;
`else
 parameter DATA_DW = 32 ;
`endif
```


`elsif, `else 编译指令对于 `ifdef 指令是可选的，即可以只有 `ifdef 和 `endif 组成一次条件编译指令块。

当然，也可用 `ifndef 来设置条件编译，表示如果没有相关的宏定义，则执行相关语句。

下面例子中，如果定义了 WINDOW，则使用第二种参数说明。如果没有定义 WINDOW，则使用第一种参数说明。

## 实例
 
`ifndef WINDOW

 parameter DATA_DW = 32 ; 

 `else

 parameter DATA_DW = 64 ;

 `endif