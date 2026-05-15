# 1.3 Verilog 环境搭建

学习 Verilog 做仿真时，可选择不同仿真环境。FPGA 开发环境有 Xilinx 公司的 ISE（目前已停止更新），VIVADO；因特尔公司的 Quartus II；ASIC 开发环境有 Synopsys 公司的 VCS ；很多人也在用 Icarus Verilog 和 GTKwave 的方法，更加的轻便。


虽然 ISE 或者 Quartus II 都会自带仿真器，但功能还是有欠缺。所以，这里介绍下 Quartus II + Modelsim 联合仿真的测试方法，运行环境为 64bit-win10 系统。

### Quartus II 安装


本次介绍使用的 Quartus 版本为 10.1。



目前 Quartus II 官网已经没有 13.1 以下版本的安装包，大家可以安装 13.1 以上版本的软件。功能都是大同小异，下载地址：[https://fpgasoftware.intel.com/13.1/?edition=subscription&platform=windows](https://fpgasoftware.intel.com/13.1/?edition=subscription&platform=windows)


下载 13.1 以上的 quartus II 时，官网也会推荐相应版本的 Modelsim，一起下载即可。


开始安装，修改安装路径，其他按照默认设置一步步操作即可。

下图是成功安装的截图。

![](https://www.runoob.com/wp-content/uploads/2020/09/vlg-install-1.png)


如果提示需要 License file，如下图所示，则需要指定购买该软件时的 license 文件。

![](https://www.runoob.com/wp-content/uploads/2020/09/vlg-install-2.png)


如果 license 文件需要替换 Host-ID，只需要 license 文件中的 HOSTID 替换为 NIC 选项中随便一个 ID 即可，如下图红色框所示：

![](https://www.runoob.com/wp-content/uploads/2020/09/vlg-install-3.png)


Quartus II 10.1 安装完还需要安装 Device，即安装支持各种可编程逻辑器件型号的库文件，否则 Quartus II 不能正常建立工程。


安装路径需要选择 Quartus II 的安装路径，此时 Device 安装可自动识别 Quartus II。

最新 Quartus II（例如 2016 版本）已经支持一套化安装了。


### Modelsim 安装


Modelsim 选择 modelsim-win64-10.1c-se 版本。


也需要修改下安装路径，然后按照默认设置进行操作即可。


安装完毕后可能提示需要重启电脑，重启即可。

![](https://www.runoob.com/wp-content/uploads/2020/09/vlg-install-4.png)



### 建立 Quartus II 工程


**建立工程**

File->New project Wizard


设置工作路径与工程名字、top module名字。


注意，路径与名字设置时，不能包含中文。

![](https://www.runoob.com/wp-content/uploads/2020/09/vlg-install-5.png)



**选择器件型号**


我们只进行简单的仿真，不进行下载、烧录等，所以我们不用关心具体信号，随便选一种即可。


然后一直点击 Next，直到 Finish。

![](https://www.runoob.com/wp-content/uploads/2020/09/vlg-install-6.png)



**新建 Verilog 源文件**

下面就对 4 位宽 10 进制计数器进行简单的仿真。

点击：File->New->Verilog HDL File->OK


点击：File->Save As


输入 module 名字为：counter10.v

需要注意的是，top module 名字一定要和 project 名字一致，否则会报错（如图中所示）。


把 Verilog 代码复制到文件 counter10.v 中，进行一键编译（实际包含了编译、综合、布局布线等）。


报错时，可通过点击 Error log 来定位错误，进行修改，直至没有 Error。

![](https://www.runoob.com/wp-content/uploads/2020/09/vlg-install-7.png)



### Quartus II 调用 Modelsim 仿真


仿真设置为 Modelsim-altera

点击：Tool->Options->EDA Tool Options

将 Modelsim 后面的地址改为 Modelsim 启动程序的路径。

![](https://www.runoob.com/wp-content/uploads/2020/09/vlg-install-8.png)



**选择仿真器**

点击：Assignments -> Simulation


Tool name 选择 ModelSim，并设置 Format、Time scale 等，如图。。

![](https://www.runoob.com/wp-content/uploads/2020/09/vlg-install-9.png)



**写 testbench 文件**

点击：Processing->start->Start TestBench Template Writer


如果设置正确，会在工程路径 simulation/modelsim 下产生 .vt 文件。

.vt 文件模板已经给出了端口部分的代码、接口变量的声明和例化语句映射等。我们要做的就是将测试代码填入到 testbench 合适的位置。


这里简单的写一下时钟、复位驱动代码，如下图所示。

![](https://www.runoob.com/wp-content/uploads/2020/09/vlg-install-10.png)



**将 testbench 添加到工程中**

点击：Assignments -> Settings -> Simulation

在 Compile test bench 选项中，选择 new，设置 Test bench name，并通过 File name 查找的方式，将上一步生成的 .vt 文件添加到工程中。


需要注意的是，testbench 文件名字需要和 testbench 里的 top module 名字保持一致，否则后续启动 Modelsim 时会报错，不能进行正常的仿真。

![](https://www.runoob.com/wp-content/uploads/2020/09/XFejkqOFS8VYO1jL.png)



**重新一键编译**


此时，你会发现，Tasks 栏编译的状态变成了问号，需要重新进行一键编译。

![](https://www.runoob.com/wp-content/uploads/2020/09/vlg-install-12.png)



**调用 Modelsim 仿真**


点击：Tools->Run simulation Tool->RTL Simulation

这时就会自动启动 Modelsim 软件。

Modelsim 操作这里不做具体介绍。


由仿真图可知，我们的设计完成了 10 进制计数的基本功能。

![](https://www.runoob.com/wp-content/uploads/2020/09/vlg-install-13.png)




## 总结


记忆中，Quartus II + Modelsim 的联合仿真功能既强大，又安装方便。几年后重新进行此过程，发现步骤也有些许繁琐，花费了我一晚上的时间来搞定。很多细节也在上面提出，多多注意就好。不过，大家以后有机会进行大型的数字模块仿真时，就会发现此方法的有效性。


在接下来的教程里，有些简单的仿真可能用其他软件进行，截图界面可能与 Modelsim 不一致。大家看到后不用怀疑仿真的准确性，这里特别说明。


设计模块与 testbench 源码也会全部给出，大家完全可以自己仿真、验证。