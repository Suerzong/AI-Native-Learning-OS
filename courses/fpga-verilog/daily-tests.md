# 每日诊断短测

每日短测用于判断今天应该训练什么，而不是为了打分。

## 模板

```md
## YYYY-MM-DD

### 诊断题

1. 概念题：
2. 代码题：
3. 分析题：
4. 调试题：

### 结果

- 正确率：
- 主要错误：
- 今日训练目标：
- 是否允许推进：
```

---

## 组合逻辑样例

1. `assign out = ~a;` 和 `assign out = !a;` 有什么区别？当 a = 4'b1010 时，结果分别是什么？
2. 写出 2 选 1 MUX 的 Verilog 代码（用三元运算符）。
3. 以下代码综合后会生成什么电路？会产生锁存器吗？
   ```verilog
   always @(*) begin
       if (sel) out = a;
   end
   ```
4. 以下代码有什么问题？
   ```verilog
   assign out = a & b;
   assign out = c | d;
   ```

## 时序逻辑样例

1. 阻塞赋值（`=`）和非阻塞赋值（`<=`）的区别是什么？各自用在什么场景？
2. 写出带异步复位的 8 位 D 触发器代码。
3. 以下代码会产生什么问题？
   ```verilog
   always @(posedge clk) begin
       if (rst) q = 0;
       else q = d;
   end
   ```
4. 一个 10 进制计数器，计数终值应该是多少？为什么？

## 状态机样例

1. 三段式状态机的三段分别负责什么？
2. Moore 型和 Mealy 型状态机的输出有什么区别？
3. 以下状态机代码缺少了什么？会产生什么问题？
   ```verilog
   always @(*) begin
       case (state)
           S0: next = din ? S1 : S0;
           S1: next = din ? S2 : S0;
       endcase
   end
   ```
4. 序列检测器检测 1011（不重叠），需要几个状态？
