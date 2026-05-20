# 7.1 Verilog 除法器设计

### 除法器原理（定点）


和十进制除法类似，计算 27 除以 5 的过程如下所示：

![](https://www.runoob.com/wp-content/uploads/2020/09/KGUCofhbNPJRkGv3.png)



除法运算过程如下：

- 
(1) 取被除数的高几位数据，位宽和除数相同（实例中是 3bit 数据）。
- 
(2) 将被除数高位数据与除数作比较，如果前者不小于后者，则可得到对应位的商为 1，两者做差得到第一步的余数；否则得到对应的商为 0，将前者直接作为余数。
- 
(3) 将上一步中的余数与被除数剩余最高位 1bit 数据拼接成新的数据，然后再和除数做比较。可以得到新的商和余数。
- 
(4) 重复过程 (3)，直到被除数最低位数据也参与计算。


需要说明的是，商的位宽应该与被除数保持一致，因为除数有可能为1。**所以上述手动计算除法的实例中，第一步做比较时，应该取数字 27 最高位 1 (3'b001) 与 3'b101 做比较。**
根据此计算过程，设计位宽可配置的流水线式除法器，流水延迟周期个数与被除数位宽一致。


### 除法器设计


**单步运算设计**


单步除法计算时，单步被除数位宽（信号 dividend）需比原始除数（信号 divisor）位宽多 1bit 才不至于溢出。


为了便于流水，输出端需要有寄存器来存储原始的除数（信号 divisor 和 divisor_kp）和被除数信息（信号 dividend_ci 和 dividend_kp）。


单步的运算结果就是得到新的 1bit 商数据（信号 merchant）和余数（信号 remainder）。


为了得到最后的除法结果，新的 1bit 商数据（信号 merchant）还需要与上一周期的商结果（merchant_ci）进行移位累加。


单步运算单元设计如下（文件名 divider_cell.v）：

## 实例
 
// parameter M means the actual width of divisor

module divider_cell

 #&#40;parameter N=5,

 parameter M=3&#41;

 &#40;

 input clk,

 input rstn,

 input en,

 input &#91;M:0&#93; dividend,

 input &#91;M-1:0&#93; divisor,

 input &#91;N-M:0&#93; merchant_ci , //上一级输出的商

 input &#91;N-M-1:0&#93; dividend_ci , //原始除数

 output reg &#91;N-M-1:0&#93; dividend_kp, //原始被除数信息

 output reg &#91;M-1:0&#93; divisor_kp, //原始除数信息

 output reg rdy ,

 output reg &#91;N-M:0&#93; merchant , //运算单元输出商

 output reg &#91;M-1:0&#93; remainder //运算单元输出余数

 &#41;;

 always @&#40;posedge clk or negedge rstn&#41; begin

 if &#40;!rstn&#41; begin

 rdy <= 'b0 ;

 merchant <= 'b0 ;

 remainder <= 'b0 ;

 divisor_kp <= 'b0 ;

 dividend_kp <= 'b0 ;

 end

 else if &#40;en&#41; begin

 rdy <= 1'b1 ;

 divisor_kp <= divisor ; //原始除数保持不变

 dividend_kp <= dividend_ci ; //原始被除数传递

 if &#40;dividend >= &#123;1'b0, divisor&#125;&#41; begin

 merchant <= &#40;merchant_ci<<1&#41; + 1'b1 ; //商为1

 remainder <= dividend - &#123;1'b0, divisor&#125; ; //求余

 end

 else begin

 merchant <= merchant_ci<<1 ; //商为0

 remainder <= dividend ; //余数不变

 end

 end // if (en)

 else begin

 rdy <= 'b0 ;

 merchant <= 'b0 ;

 remainder <= 'b0 ;

 divisor_kp <= 'b0 ;

 dividend_kp <= 'b0 ;

 end

 end 

endmodule