# 2.3 Verilog 数据类型

Verilog 最常用的 2 种数据类型就是线网（wire）与寄存器（reg），其余类型可以理解为这两种数据类型的扩展或辅助。



### 线网（wire）



wire 类型表示硬件单元之间的物理连线，由其连接的器件输出端连续驱动。如果没有驱动元件连接到 wire 型变量，缺省值一般为 "Z"。举例如下：




## 实例
 
wire interrupt ;

wire flag1, flag2 ;

wire gnd = 1'b0 ;