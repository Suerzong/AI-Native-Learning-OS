# 6.3 Verilog 状态机

### 关键词：状态机，售卖机


有限状态机（Finite-State Machine，FSM），简称状态机，是表示有限个状态以及在这些状态之间的转移和动作等行为的数学模型。状态机不仅是一种电路的描述工具，而且也是一种思想方法，在电路设计的系统级和 RTL 级有着广泛的应用。

### 状态机类型


Verilog 中状态机主要用于同步时序逻辑的设计，能够在有限个状态之间按一定要求和规律切换时序电路的状态。状态的切换方向不但取决于各个输入值，还取决于当前所在状态。
状态机可分为 2 类：Moore 状态机和 Mealy 状态机。


**Moore 型状态机**


Moore 型状态机的输出只与当前状态有关，与当前输入无关。


输出会在一个完整的时钟周期内保持稳定，即使此时输入信号有变化，输出也不会变化。输入对输出的影响要到下一个时钟周期才能反映出来。这也是 Moore 型状态机的一个重要特点：输入与输出是隔离开来的。

![](https://www.runoob.com/wp-content/uploads/2020/09/drIsJ2XFh6mt4t5D.png)


**Mealy 型状态机**


Mealy 型状态机的输出，不仅与当前状态有关，还取决于当前的输入信号。


Mealy 型状态机的输出是在输入信号变化以后立刻发生变化，且输入变化可能出现在任何状态的时钟周期内。因此，同种逻辑下，Mealy 型状态机输出对输入的响应会比 Moore 型状态机早一个时钟周期。

![](https://www.runoob.com/wp-content/uploads/2020/09/4xc5VfpojsJMoZX5.png)


**状态机设计流程**


根据设计需求画出状态转移图，确定使用状态机类型，并标注出各种输入输出信号，更有助于编程。一般使用最多的是 Mealy 型 3 段式状态机，下面用通过设计一个自动售卖机的具体实例来说明状态机的设计过程。

### 自动售卖机


**自动售卖机的功能描述如下：**

饮料单价 2 元，该售卖机只能接受 0.5 元、1 元的硬币。考虑找零和出货。投币和出货过程都是一次一次的进行，不会出现一次性投入多币或一次性出货多瓶饮料的现象。每一轮售卖机接受投币、出货、找零完成后，才能进入到新的自动售卖状态。

**该售卖机的工作状态转移图如下所示，包含了输入、输出信号状态。**

其中，coin = 1 代表投入了 0.5 元硬币，coin = 2 代表投入了 1 元硬币。

![](https://www.runoob.com/wp-content/uploads/2020/09/Uep0FDU5QLlSBjKZ.png)



### 状态机设计：3 段式（推荐）


**状态机设计如下：**

- 
(0) 首先，根据状态机的个数确定状态机编码。利用编码给状态寄存器赋值，代码可读性更好。
- 
(1) 状态机第一段，时序逻辑，非阻塞赋值，传递寄存器的状态。
- 
(2) 状态机第二段，组合逻辑，阻塞赋值，根据当前状态和当前输入，确定下一个状态机的状态。
- 
(3) 状态机第三代，时序逻辑，非阻塞赋值，因为是 Mealy 型状态机，根据当前状态和当前输入，确定输出信号。

## 实例
 
// vending-machine

// 2 yuan for a bottle of drink

// only 2 coins supported: 5 jiao and 1 yuan

// finish the function of selling and changing

module vending_machine_p3 &#40;

 input clk ,

 input rstn ,

 input &#91;1:0&#93; coin , //01 for 0.5 jiao, 10 for 1 yuan

 output &#91;1:0&#93; change ,

 output sell //output the drink

 &#41;;

 //machine state decode

 parameter IDLE = 3'd0 ;

 parameter GET05 = 3'd1 ;

 parameter GET10 = 3'd2 ;

 parameter GET15 = 3'd3 ;

 //machine variable

 reg &#91;2:0&#93; st_next ;

 reg &#91;2:0&#93; st_cur ;

 //(1) state transfer

 always @&#40;posedge clk or negedge rstn&#41; begin

 if &#40;!rstn&#41; begin

 st_cur <= 'b0 ;

 end

 else begin

 st_cur <= st_next ;

 end

 end

 //(2) state switch, using block assignment for combination-logic

 //all case items need to be displayed completely 

 always @&#40;*&#41; begin 

 //st_next = st_cur ;//如果条件选项考虑不全，可以赋初值消除latch

 case&#40;st_cur&#41;

 IDLE:

 case &#40;coin&#41;

 2'b01: st_next = GET05 ;

 2'b10: st_next = GET10 ;

 default: st_next = IDLE ;

 endcase

 GET05:

 case &#40;coin&#41;

 2'b01: st_next = GET10 ;

 2'b10: st_next = GET15 ;

 default: st_next = GET05 ;

 endcase

 GET10:

 case &#40;coin&#41;

 2'b01: st_next = GET15 ;

 2'b10: st_next = IDLE ;

 default: st_next = GET10 ;

 endcase

 GET15:

 case &#40;coin&#41;

 2'b01,2'b10:

 st_next = IDLE ;

 default: st_next = GET15 ;

 endcase

 default: st_next = IDLE ;

 endcase

 end

 //(3) output logic, using non-block assignment

 reg &#91;1:0&#93; change_r ;

 reg sell_r ;

 always @&#40;posedge clk or negedge rstn&#41; begin

 if &#40;!rstn&#41; begin

 change_r <= 2'b0 ;

 sell_r <= 1'b0 ;

 end

 else if &#40;&#40;st_cur == GET15 && coin ==2'h1&#41;

 || &#40;st_cur == GET10 && coin ==2'd2&#41;&#41; begin

 change_r <= 2'b0 ;

 sell_r <= 1'b1 ;

 end

 else if &#40;st_cur == GET15 && coin == 2'h2&#41; begin

 change_r <= 2'b1 ;

 sell_r <= 1'b1 ;

 end

 else begin

 change_r <= 2'b0 ;

 sell_r <= 1'b0 ;

 end

 end

 assign sell = sell_r ;

 assign change = change_r ;

endmodule