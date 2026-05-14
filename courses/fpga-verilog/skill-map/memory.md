# 存储器设计技能图

## 目标

掌握 FPGA 内部存储器（RAM、ROM、FIFO）的设计方法，理解同步和异步存储器的区别。

## 必知概念

- 寄存器堆（Register File）vs 块 RAM（BRAM）
- 同步读写 vs 异步读写
- FIFO 的满/空判断
- 跨时钟域问题与格雷码

## 核心代码模式

### 同步 RAM

```verilog
module ram(input clk, wr_en, input [7:0] addr, din, output reg [7:0] dout);
    reg [7:0] mem [0:255];
    always @(posedge clk) begin
        if (wr_en) mem[addr] <= din;
        dout <= mem[addr];
    end
endmodule
```

### ROM

```verilog
module rom(input [7:0] addr, output [7:0] data);
    reg [7:0] mem [0:255];
    initial $readmemh("rom_init.hex", mem);
    assign data = mem[addr];
endmodule
```

### 同步 FIFO

```verilog
module sync_fifo(input clk, rst, wr_en, rd_en,
                 input [7:0] wr_data,
                 output [7:0] rd_data,
                 output full, empty);
    reg [7:0] mem [0:15];
    reg [4:0] wr_ptr, rd_ptr;

    always @(posedge clk) begin
        if (rst) begin wr_ptr <= 0; rd_ptr <= 0; end
        else begin
            if (wr_en && !full) begin
                mem[wr_ptr[3:0]] <= wr_data;
                wr_ptr <= wr_ptr + 1;
            end
            if (rd_en && !empty) rd_ptr <= rd_ptr + 1;
        end
    end

    assign rd_data = mem[rd_ptr[3:0]];
    assign full  = (wr_ptr == {~rd_ptr[4], rd_ptr[3:0]});
    assign empty = (wr_ptr == rd_ptr);
endmodule
```

## 常见错误

| 错误 | 原因 | 纠正 |
|------|------|------|
| 满/空判断条件错 | 指针位宽和比较逻辑 | 多一位指针区分满和空 |
| 异步读写混乱 | 跨时钟域 | 用格雷码同步指针 |
| 读写冲突 | 同一地址同时读写 | 定义冲突行为（读旧值/新值） |

## 掌握标准

- 能实现同步 RAM 和 ROM
- 能实现带满/空信号的同步 FIFO
- 理解异步 FIFO 的格雷码同步原理

## 题库对应

Q156：同步 FIFO
Q157：异步 FIFO
Q218：ROM 简单实现
Q308-Q309：RAM/ROM 设计
