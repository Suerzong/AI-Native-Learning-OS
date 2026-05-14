# 组合逻辑技能图

## 目标

掌握 Verilog 组合逻辑的描述方法，能用 assign 和 always @(*) 实现门电路、选择器、编码器、加法器等基本组合逻辑模块。

## 必知概念

- wire（线网）与 reg（寄存器变量）的区别
- assign 连续赋值语句
- always @(*) 过程块
- 阻塞赋值（=）在组合逻辑中的使用
- 位宽声明 `[MSB:LSB]`
- 拼接运算符 `{}`

## 核心代码模式

### 基本门电路（assign）

```verilog
module gates(input a, b,
             output and_out, or_out, not_out, xor_out);
    assign and_out = a & b;   // 与门
    assign or_out  = a | b;   // 或门
    assign not_out = ~a;      // 非门（按位取反）
    assign xor_out = a ^ b;   // 异或门
endmodule
```

### 多路选择器（条件运算符）

```verilog
module mux2(input d0, d1, s, output y);
    assign y = s ? d1 : d0;   // 2选1 MUX
endmodule

module mux4(input [3:0] d, input [1:0] s, output y);
    assign y = d[s];          // 4选1 MUX（用索引）
endmodule
```

### 译码器（移位操作）

```verilog
module decoder38(input [2:0] in, output [7:0] out);
    assign out = 8'b1 << in;  // 3-8译码器
endmodule
```

### 加法器（算术运算）

```verilog
module adder(input [3:0] a, b, input cin,
             output [3:0] sum, output cout);
    assign {cout, sum} = a + b + cin;
endmodule
```

### always @(*) 组合逻辑

```verilog
module comparator(input [3:0] a, b, output reg [2:0] out);
    always @(*) begin
        if (a > b)       out = 3'b100;
        else if (a == b) out = 3'b010;
        else             out = 3'b001;
    end
endmodule
```

## 常见错误

| 错误 | 原因 | 纠正 |
|------|------|------|
| `~a` vs `!a` | 混淆按位和逻辑取反 | `~` 按位（每位取反），`!` 逻辑（结果 1 位） |
| if 缺 else | 组合逻辑不完整 | 每个 if 都写 else |
| case 缺 default | 未覆盖所有情况 | 加 default 分支 |
| assign 目标用 reg | assign 只能驱动 wire | assign 目标必须是 wire |
| 位宽不匹配 | 隐式截断 | 运算前检查位宽 |

## 训练阶梯

1. 认识 assign 语句的语法 → 完成门电路题
2. 理解条件运算符 → 完成 MUX 题
3. 掌握 case 语句 → 完成译码器/编码器题
4. 理解 always @(*) → 完成比较器、投票器题
5. 掌握算术运算 → 完成加法器、乘法器题
6. 理解位宽和拼接 → 完成多位运算题
7. 独立设计 → 完成组合逻辑综合题
8. 迁移应用 → 将组合逻辑应用到新场景

## 掌握标准

- 能画出每种组合逻辑模块的门电路图
- 能不看参考写出 assign 和 always @(*) 代码
- 能预判代码综合后的电路结构
- 能发现并修复锁存器推断问题

## 题库对应

Q93-Q131：选择题（数字逻辑基础）
Q93-Q128：编程题（组合逻辑模块）
