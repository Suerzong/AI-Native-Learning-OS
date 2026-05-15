# 5.1 Verilog 模块与端口

### 关键词：模块，端口，双向端口，PAD


结构建模方式有 3 类描述语句： Gate（门级）例化语句，UDP (用户定义原语)例化语句和 module (模块) 例化语句。本次主要讲述使用最多的模块级例化语句。

### 模块


模块是 Verilog 中基本单元的定义形式，是与外界交互的接口。

模块格式定义如下：

```
module module_name 
#(parameter_list)
(port_list) ;
 Declarations_and_Statements ;
endmodule
```



模块定义必须以关键字 module 开始，以关键字 endmodule 结束。


模块名，端口信号，端口声明和可选的参数声明等，出现在设计使用的 Verilog 语句（图中 Declarations_and_Statements）之前。


模块内部有可选的 5 部分组成，分别是变量声明，数据流语句，行为级语句，低层模块例化及任务和函数，如下图表示。这 5 部分出现顺序、出现位置都是任意的。但是，各种变量都应在使用之前声明。变量具体声明的位置不要求，但必须保证在使用之前的位置。

![](https://www.runoob.com/wp-content/uploads/2020/09/jxRkciGWpiEbvz3D.png)



前面大多数仿真代码都会用到 module 声明，大家可以自行参考，这里不再做具体举例。下面介绍端口时，再做详细的仿真。


### 端口


端口是模块与外界交互的接口。对于外部环境来说，模块内部是不可见的，对模块的调用只能通过端口连接进行。


**端口列表**


模块的定义中包含一个可选的端口列表，一般将不带类型、不带位宽的信号变量罗列在模块声明里。下面是一个 PAD 模型的端口列表：

```
module pad(
 DIN, OEN, PULL,
 DOUT, PAD);
```


一个模块如果和外部环境没有交互，则可以不用声明端口列表。例如之前我们仿真时 test.sv 文件中的 test 模块都没有声明具体端口。

```
module test ; //直接分号结束
 ...... //数据流或行为级描述
endmodule
```



**端口声明**


(1) 端口信号在端口列表中罗列出来以后，就可以在模块实体中进行声明了。


根据端口的方向，端口类型有 3 种： 输入（input），输出（output）和双向端口（inout）。


input、inout 类型不能声明为 reg 数据类型，因为 reg 类型是用于保存数值的，而输入端口只能反映与其相连的外部信号的变化，不能保存这些信号的值。


output 可以声明为 wire 或 reg 数据类型。


上述例子中 pad 模块的端口声明，在 module 实体中就可以表示如下：

## 实例
 
//端口类型声明

input DIN, OEN ;

input &#91;1:0&#93; PULL ; //(00,01-dispull, 11-pullup, 10-pulldown)

inout PAD ; //pad value

output DOUT ; //pad load when pad configured as input

//端口数据类型声明

wire DIN, OEN ;

wire &#91;1:0&#93; PULL ;

wire PAD ;

reg DOUT ;