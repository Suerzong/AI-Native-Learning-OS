# 有限状态机技能图

## 目标

掌握有限状态机（FSM）的设计方法，能用一段式、二段式、三段式实现状态机，能设计序列检测器。

## 必知概念

- 状态（State）、转移条件（Transition）、输出（Output）
- Moore 型（输出只依赖状态）vs Mealy 型（输出依赖状态和输入）
- 状态编码：二进制、格雷码、独热码（One-Hot）
- 一段式/二段式/三段式状态机的区别

## 核心代码模式

### 三段式状态机（推荐）

```verilog
module fsm(input clk, rst, din, output reg out);
    parameter S0 = 2'b00, S1 = 2'b01, S2 = 2'b10;
    reg [1:0] state, next;

    // 第一段：状态转移（时序逻辑）
    always @(posedge clk) begin
        if (rst) state <= S0;
        else     state <= next;
    end

    // 第二段：次态逻辑（组合逻辑）
    always @(*) begin
        case (state)
            S0: next = din ? S1 : S0;
            S1: next = din ? S1 : S2;
            S2: next = din ? S1 : S0;
            default: next = S0;
        endcase
    end

    // 第三段：输出逻辑（组合或时序）
    always @(*) begin
        out = (state == S2);
    end
endmodule
```

### 序列检测器（检测 1011）

```verilog
module seq_detect(input clk, rst, din, output reg out);
    parameter S0=0, S1=1, S2=2, S3=3, S4=4;
    reg [2:0] state, next;

    always @(posedge clk) begin
        if (rst) state <= S0;
        else     state <= next;
    end

    always @(*) begin
        next = S0; out = 0;
        case (state)
            S0: next = din ? S1 : S0;
            S1: next = din ? S1 : S2;
            S2: next = din ? S3 : S0;
            S3: next = din ? S4 : S2;
            S4: begin next = din ? S1 : S2; out = 1; end
            default: next = S0;
        endcase
    end
endmodule
```

## 常见错误

| 错误 | 原因 | 纠正 |
|------|------|------|
| 三段混在一起 | 不理解分离的好处 | 状态转移、次态、输出分开写 |
| 缺 default 分支 | 未处理非法状态 | case 加 default: next = S0 |
| Moore/Mealy 搞混 | 输出时序不同 | Moore 只看 state，Mealy 还看 input |
| 状态编码选择不当 | 影响资源和速度 | 少状态用 binary，多状态用 one-hot |
| 输出信号延迟一拍 | 三段式的输出时序 | 时序输出延迟一拍，组合输出不延迟 |

## 训练阶梯

1. 理解状态转移图 → 画出简单 FSM 的状态图
2. 掌握状态编码 → 对比 binary vs one-hot
3. 一段式实现 → 完成简单 FSM
4. 三段式实现 → 完成标准 FSM
5. 序列检测器 → 完成 1011 检测
6. 不重叠 vs 可重叠 → 理解状态回退差异
7. Mealy 型 → 实现 Mealy 型检测器
8. 复杂 FSM → 完成交通灯、密码锁等

## 掌握标准

- 能从需求画出完整的状态转移图
- 能用三段式实现任意 FSM
- 能区分 Moore 和 Mealy 的输出时序
- 能设计不重叠和可重叠序列检测器

## 题库对应

Q143-Q144：简单状态机
Q145：1011 序列检测器
Q195：有限状态机
Q220-Q221：序列检测变体
Q230-Q231：二段式/三段式状态机
Q302：Mealy 型状态机
