# 系统设计技能图

## 目标

掌握 FPGA 系统级设计方法，包括流水线、仲裁器、校验编码、数字信号处理和 CPU 设计。

## 必知概念

- 流水线的吞吐量和延迟
- 仲裁策略（固定优先级、轮询调度）
- CRC 校验原理
- RISC-V 指令集基础

## 核心设计模式

### 流水线

```verilog
// 二级流水线乘法器
module pipe_mult(input clk, input [3:0] a, b, output reg [7:0] prod);
    reg [7:0] stage1;
    always @(posedge clk) begin
        stage1 <= a * b;      // 第一级：计算
        prod   <= stage1;     // 第二级：输出
    end
endmodule
```

### 固定优先级仲裁器

```verilog
module arbiter(input [3:0] req, output reg [3:0] grant);
    always @(*) begin
        casex (req)
            4'bxxx1: grant = 4'b0001;
            4'bxx10: grant = 4'b0010;
            4'bx100: grant = 4'b0100;
            4'b1000: grant = 4'b1000;
            default: grant = 4'b0000;
        endcase
    end
endmodule
```

### CRC8 计算器

```verilog
module crc8(input clk, rst, din, valid, output reg [7:0] crc);
    always @(posedge clk) begin
        if (rst) crc <= 8'hFF;
        else if (valid) begin
            crc[0] <= crc[7] ^ din;
            crc[1] <= crc[0];
            crc[2] <= crc[1] ^ crc[7] ^ din;
            crc[3] <= crc[2];
            crc[4] <= crc[3];
            crc[5] <= crc[4];
            crc[6] <= crc[5];
            crc[7] <= crc[6];
        end
    end
endmodule
```

## 设计层次

```
算法描述 → 架构选择 → 模块划分 → 接口定义 → 模块实现 → 集成仿真 → 时序约束 → 上板验证
```

## 掌握标准

- 能设计二级流水线，理解吞吐量和延迟
- 能实现固定优先级和轮询仲裁器
- 能实现 CRC8 校验模块
- 能实现简单的 RISC-V 单周期 CPU
- 能完成包含多个模块的综合项目

## 题库对应

Q171：流水线乘法器
Q211-Q214：仲裁器
Q159：CRC8 计算器
Q160：奇偶校验
Q196：8b/10b 编码
Q298：并行 FIR 滤波器
Q345-Q346：RISC-V CPU
