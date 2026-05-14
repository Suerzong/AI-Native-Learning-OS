# 时序逻辑技能图

## 目标

掌握 Verilog 时序逻辑的描述方法，能用 always @(posedge clk) 实现触发器、寄存器、计数器、分频器和移位寄存器。

## 必知概念

- 时钟边沿触发（posedge / negedge）
- 非阻塞赋值（<=）的必要性
- 同步复位与异步复位
- 寄存器（register）与锁存器（latch）的区别
- 建立时间、保持时间概念

## 核心代码模式

### D 触发器

```verilog
module dff(input clk, d, output reg q);
    always @(posedge clk)
        q <= d;
endmodule
```

### 带异步复位的寄存器

```verilog
module dff_rst(input clk, rst, input [7:0] d, output reg [7:0] q);
    always @(posedge clk or posedge rst) begin
        if (rst) q <= 8'b0;
        else     q <= d;
    end
endmodule
```

### 带同步复位的寄存器

```verilog
module dff_sync(input clk, rst, input [7:0] d, output reg [7:0] q);
    always @(posedge clk) begin
        if (rst) q <= 8'b0;
        else     q <= d;
    end
endmodule
```

### 计数器

```verilog
module counter(input clk, rst, output reg [3:0] cnt);
    always @(posedge clk) begin
        if (rst) cnt <= 4'd0;
        else     cnt <= cnt + 1'b1;
    end
endmodule
```

### 分频器

```verilog
// 偶数分频（2 分频）
module div2(input clk, rst, output reg clk_out);
    always @(posedge clk) begin
        if (rst) clk_out <= 0;
        else     clk_out <= ~clk_out;
    end
endmodule
```

### 移位寄存器

```verilog
module shift_reg(input clk, rst, d, output reg [3:0] q);
    always @(posedge clk) begin
        if (rst) q <= 4'b0;
        else     q <= {q[2:0], d};
    end
endmodule
```

## 常见错误

| 错误 | 原因 | 纠正 |
|------|------|------|
| 用 `=` 而非 `<=` | 不理解非阻塞赋值 | 时序逻辑永远用 <= |
| 同步/异步复位混用 | 不理解两者的区别 | 选定一种，统一使用 |
| 复位缺初始值 | 寄存器上电状态不确定 | if (rst) q <= 初始值 |
| 计数器模值判断错 | 终值 = N-1 而非 N | 10 进制数到 9 |
| 分频计数器位宽不够 | 位宽不满足计数范围 | 位宽 >= log2(分频系数) |

## 训练阶梯

1. 理解时钟和复位 → 完成 D 触发器题
2. 掌握非阻塞赋值 → 完成 8 位寄存器题
3. 理解同步/异步复位 → 完成带复位寄存器题
4. 掌握计数器 → 完成二进制/十进制计数器题
5. 理解分频 → 完成偶数/奇数分频器题
6. 掌握移位 → 完成移位寄存器题
7. 综合应用 → 完成时序逻辑综合题

## 掌握标准

- 能解释阻塞和非阻塞赋值的仿真行为差异
- 能不看参考写出带复位的计数器
- 能设计任意模值的分频器
- 能解释同步和异步复位的综合结果差异

## 题库对应

Q129-Q131：触发器和寄存器
Q135-Q136：计数器
Q96、Q147：分频器
Q139、Q141：移位寄存器
Q112、Q291：格雷码计数器
