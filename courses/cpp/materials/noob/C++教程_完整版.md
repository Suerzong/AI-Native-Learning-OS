# C++ 教程 —— 菜鸟教程整理版

> 本文档整理自 [菜鸟教程 C++](https://www.runoob.com/cplusplus/cpp-tutorial.html)，便于离线学习阅读。

## 目录


**前言**

- C++ 教程
- C++ 简介
- C++ 环境设置

**C++ 基础**

- C++ 基本语法
- C++ 注释
- C++ 数据类型
- C++ 变量类型
- C++ 变量作用域
- C++ 常量
- C++ 修饰符类型
- C++ 存储类
- C++ 运算符

**C++ 流程控制**

- C++ 循环
- C++ 判断

**C++ 函数与数据结构**

- C++ 函数
- C++ 数字
- C++ 数组
- C++ 字符串
- C++ 指针
- C++ 引用
- C++ 日期 & 时间
- C++ 基本的输入输出
- C++ 结构体(struct)

**C++ 面向对象**

- C++ 类 & 对象
- C++ 继承
- C++ 重载运算符和重载函数
- C++ 多态
- C++ 数据抽象
- C++ 数据封装
- C++ 接口（抽象类）

**C++ 高级教程**

- C++ 文件和流
- C++ 异常处理
- C++ 动态内存
- C++ 命名空间
- C++ 模板
- C++ 预处理器


---


---

# 前言


## C++ 教程

C++ 是一种高级语言，它是由 Bjarne Stroustrup 于 1979 年在贝尔实验室开始设计开发的。C++ 进一步扩充和完善了 C 语言，是一种面向对象的程序设计语言。C++ 可运行于多种平台上，如 Windows、MAC 操作系统以及 UNIX 的各种版本。


本教程通过通俗易懂的语言来讲解 C++ 编程语言。

**[现在开始学习 C++ 编程！](/cplusplus/cpp-intro.html)**

C++ 在线工具


谁适合阅读本教程？

本教程是专门为初学者打造的，帮助他们理解与 C++ 编程语言相关的基础到高级的概念。

阅读本教程前，您需要了解的知识：

在您开始练习本教程中所给出的各种实例之前，您需要对计算机程序和计算机程序设计语言有基本的了解。

编译/执行 C++ 程序


### 实例



```cpp
#include
using namespace std;
int main()
{
    cout
using namespace std;
int main()
{
    cout << "Hello, world!" << "\n";
    return 0;
}
```


## C++ 简介

C++ 是一种静态类型的、编译式的、通用的、大小写敏感的、不规则的编程语言，支持过程化编程、面向对象编程和泛型编程。

C++ 被认为是一种**中级**语言，它综合了高级语言和低级语言的特点。

C++ 是由 Bjarne Stroustrup 于 1979 年在新泽西州美利山贝尔实验室开始设计开发的。C++ 进一步扩充和完善了 C 语言，最初命名为带类的C，后来在 1983 年更名为 C++。

C++ 是 C 的一个超集，事实上，任何合法的 C 程序都是合法的 C++ 程序。

**注意：**使用静态类型的编程语言是在编译时执行类型检查，而不是在运行时执行类型检查。


面向对象程序设计

C++ 完全支持面向对象的程序设计，包括面向对象开发的四大特性：


-

**封装（Encapsulation）**：封装是将数据和方法组合在一起，对外部隐藏实现细节，只公开对外提供的接口。这样可以提高安全性、可靠性和灵活性。
-

**继承（Inheritance）**：继承是从已有类中派生出新类，新类具有已有类的属性和方法，并且可以扩展或修改这些属性和方法。这样可以提高代码的复用性和可扩展性。
-

**多态（Polymorphism）**：多态是指同一种操作作用于不同的对象，可以有不同的解释和实现。它可以通过接口或继承实现，可以提高代码的灵活性和可读性。
-

**抽象（Abstraction）**：抽象是从具体的实例中提取共同的特征，形成抽象类或接口，以便于代码的复用和扩展。抽象类和接口可以让程序员专注于高层次的设计和业务逻辑，而不必关注底层的实现细节。


标准库

标准的 C++ 由三个重要部分组成：


- 核心语言，提供了所有构件块，包括变量、数据类型和常量，等等。

- C++ 标准库，提供了大量的函数，用于操作文件、字符串等。

- 标准模板库（STL），提供了大量的方法，用于操作数据结构等。


ANSI 标准

ANSI 标准是为了确保 C++ 的便携性 —— 您所编写的代码在 Mac、UNIX、Windows、Alpha 计算机上都能通过编译。

由于 ANSI 标准已稳定使用了很长的时间，所有主要的 C++ 编译器的制造商都支持 ANSI 标准。

学习 C++

学习 C++，关键是要理解概念，而不应过于深究语言的技术细节。

学习程序设计语言的目的是为了成为一个更好的程序员，也就是说，是为了能更有效率地设计和实现新系统，以及维护旧系统。

C++ 支持多种编程风格。您可以使用 Fortran、C、Smalltalk 等任意一种语言的编程风格来编写代码。每种风格都能有效地保证运行时间效率和空间效率。

C++ 的使用

C++ 语言在许多行业和领域都有广泛应用，包括：

-

游戏开发：C++ 是游戏开发领域中最常用的编程语言之一，因为它具有高效的性能和直接控制硬件的能力。许多主要的游戏引擎，如 Unreal Engine 和 Unity，都使用 C++ 编写。
-

嵌入式系统开发：C++ 可以在嵌入式系统中发挥重要作用，如智能手机、汽车、机器人和家电等领域。由于嵌入式系统通常具有严格的资源限制和实时要求，因此 C++ 的高效性能和内存控制功能非常有用。
-

金融领域：C++ 在金融领域中被广泛应用，如高频交易、算法交易和风险管理等领域。由于这些应用程序需要高效的性能和对硬件的直接控制，C++ 语言是一个合适的选择。
-

图形图像处理：C++ 可以用于开发图形和图像处理应用程序，如计算机视觉、计算机图形学和人工智能领域。由于这些应用程序需要高效的计算能力和对硬件的控制，因此 C++ 是一个很好的选择。
-

科学计算和数值分析：C++ 可以用于开发科学计算和数值分析应用程序，如数值模拟和高性能计算等领域。由于这些应用程序需要高效的计算能力和对硬件的直接控制，C++ 语言是一个很好的选择。

标准化

| 发布时间 | 通称 | 备注 |
| --- | --- | --- |
| 2020 | C++20, C++2a | ISO/IEC 14882:2020 |
| 2017 | C++17 | 第五个C++标准 |
| 2017 | coroutines TS | 协程库扩展 |
| 2017 | ranges TS | 提供范围机制 |
| 2017 | library fundamentals TS | 标准库扩展 |
| 2016 | concurrency TS | 用于并发计算的扩展 |
| 2015 | concepts TS | 概念库，用于优化编译期信息 |
| 2015 | TM TS | 事务性内存操作 |
| 2015 | parallelism TS | 用于并行计算的扩展 |
| 2015 | filesystem TS | 文件系统 |
| 2014 | C++14 | 第四个C++标准 |
| 2011 | - | 十进制浮点数扩展 |
| 2011 | C++11 | 第三个C++标准 |
| 2010 | - | 数学函数扩展 |
| 2007 | C++TR1 | C++技术报告：库扩展 |
| 2006 | - | C++性能技术报告 |
| 2003 | C++03 | 第二个C++标准 |
| 1998 | C++98 | 第一个C++标准 |


## C++ 环境设置

如果您想要设置 C++ 语言环境，您需要确保电脑上有以下两款可用的软件，文本编辑器和 C++ 编译器。

文本编辑器


通过编辑器创建的文件通常称为源文件，源文件包含程序源代码。

C++ 程序的源文件通常使用扩展名 .cpp、.cp 或 .c。

在开始编程之前，请确保您有一个文本编辑器，且有足够的经验来编写一个计算机程序，然后把它保存在一个文件中，编译并执行它。



-

**Visual Studio Code**：虽然它是一个通用的文本编辑器，但它有很多插件支持 C/C++ 开发，使其成为一个流行的选择，通过安装 C/C++ 插件和调整设置，你可以使其成为一个很好的 C 语言开发环境。

安装教程：https://www.runoob.com/w3cnote/vscode-tutorial.html

下载地址：[https://code.visualstudio.com/](https://code.visualstudio.com/)



-

Visual Studio： 面向 .NET 和 C++ 开发人员的综合性 Windows 版 IDE，可用于构建 Web、云、桌面、移动应用、服务和游戏。

下载地址：[https://visualstudio.microsoft.com/zh-hans/downloads/](https://visualstudio.microsoft.com/zh-hans/downloads/)。



-

**Vim** 和 **Emacs**：这两个是传统的文本编辑器，它们有着强大的编辑功能和高度的可定制性，对于熟练的用户来说非常强大，有很多插件和配置可以支持C语言的开发。
-

**Eclipse**：Eclipse 是另一个功能强大的集成开发环境，虽然它最初是为 Java 开发设计的，但通过安装 C/C++ 插件，可以使其支持 C 语言开发。



C++ 编译器 

写在源文件中的源代码是人类可读的源。它需要"编译"，转为机器语言，这样 CPU 可以按给定指令执行程序。

C++ 编译器用于把源代码编译成最终的可执行程序。

大多数的 C++ 编译器并不在乎源文件的扩展名，但是如果您未指定扩展名，则默认使用 .cpp。

最常用的免费可用的编译器是 GNU 的 C/C++ 编译器，如果您使用的是 HP 或 Solaris，则可以使用各自操作系统上的编译器。

以下部分将指导您如何在不同的操作系统上安装 GNU 的 C/C++ 编译器。这里同时提到 C/C++，主要是因为 GNU 的 gcc 编译器适合于 C 和 C++ 编程语言。


UNIX/Linux 上的安装

如果您使用的是 **Linux 或 UNIX**，请在命令行使用下面的命令来检查您的系统上是否安装了 GCC：

```cpp
$ g++ -v
```



如果您的计算机上已经安装了 GNU 编译器，则会显示如下消息：

```cpp
Using built-in specs.
Target: i386-redhat-linux
Configured with: ../configure --prefix=/usr .......
Thread model: posix
gcc version 4.1.2 20080704 (Red Hat 4.1.2-46)
```



如果未安装 GCC，那么请按照 [https://gcc.gnu.org/install/](https://gcc.gnu.org/install/) 上的详细说明安装 GCC。

Mac OS X 上的安装

如果您使用的是 Mac OS X，最快捷的获取 GCC 的方法是从苹果的网站上下载 Xcode 开发环境，并按照安装说明进行安装。一旦安装上 Xcode，您就能使用 GNU 编译器。

Xcode 目前可从 [https://developer.apple.com/download](https://developer.apple.com/download) 上下载，需要使用 apple ID 登录 。


Windows 上的安装
Cygwin


Cygwin 是一个在 Windows 操作系统上模拟 Unix/Linux 环境的软件包，它允许用户在 Windows 上使用类 Unix 工具和应用程序。

Cygwin 通过提供一组 DLL（动态链接库），这些 DLL 充当 Unix 系统调用层和 Windows 内核之间的桥梁，使得 Unix 程序能够在 Windows 系统上运行。


**Cygwin 官网：https://www.cygwin.com/**。

在官网下载安装包：



下载完成后，双击下载的文件：


接下来可以一直点击下一步(Next):




这里我们可以添加网易开源镜像阿里云镜像 https://mirrors.aliyun.com/cygwin/：




安装完成后，就会在桌面生成一个图标：





双击图标，进入命令行界面，输入 cygcheck -c cygwin命令可以查看当前的 cygwin 的版本信息：



 


接下来我们安装 gcc/g++ 的编译环境，在命令行进入 setup-x86_64.exe 目录下，执行：


```cpp
setup-x86_64.exe -q -P wget -P gcc-g++ -P make -P diffutils -P libmpfr-devel -P libgmp-devel -P libmpc-devel
```



安装完成后，进入 Cygwin64 终端， 输入 gcc --version 命令就可以查看版本信息了。

MinGW-w64

为了在 Windows 上安装 GCC，您需要安装 MinGW-w64。

MinGW-w64 是一个开源项目，它为 Windows 系统提供了一个完整的 GCC 工具链，支持编译生成 32 位和 64 位的 Windows 应用程序。

访问 MinGW-w64 的主页 [mingw-w64.org](https://www.mingw-w64.org/)，进入 MinGW 下载页面 [https://www.mingw-w64.org/downloads/](https://www.mingw-w64.org/downloads/)，下载最新版本的 MinGW-w64 安装程序。




也可以在 Github 上下载：[https://github.com/niXman/mingw-builds-binaries/releases](https://github.com/niXman/mingw-builds-binaries/releases)



MinGW-w64 的下载详情页面包含了很多 MinGW-w64 及特定工具的整合包：





我们只安装 MinGW-w64 ，所以只需下载 MinGW-w64 即可，点击红框中的"SourceForge"超链接，就会进入 SourceForge 中的 MinGW-w64 下载页面。


在 SourceForge 上下载 MinGW-w64 ：[https://sourceforge.net/projects/mingw-w64/files/](https://sourceforge.net/projects/mingw-w64/files/)



页面往下滑，下载安装程序：


这种安装，会碰到网络连接错误问题，所以我们可以直接下载 sjlj （稳定的，64 位和 32 位都支持）：


下载完成后，解压，在 bin 目录里面就可以找到 g++.exe 或者 gcc.exe：



当安装 MinGW 时，您至少要安装 gcc-core、gcc-g++、binutils 和 MinGW runtime，但是一般情况下都会安装更多其他的项。

添加您安装的 MinGW 的 bin 子目录到您的 **PATH** 环境变量中，这样您就可以在命令行中通过简单的名称来指定这些工具。



当完成安装时，您可以从 Windows 命令行上运行 gcc、g++、ar、ranlib、dlltool 和其他一些 GNU 工具。


使用 Visual Studio (Graphical Interface) 编译

1、下载及安装 [Visual Studio 下载](https://visualstudio.microsoft.com/zh-hans/downloads/)。





2、打开 Visual Studio Community


3、点击 File -> New -> Project 





4、左侧列表选择 Templates -> Visual C++ -> Win32 Console Application，并设置项目名为 MyFirstProgram。






5、点击 OK。



6、在以下窗口中点击 Next 





7、在弹出的窗口中选择 Empty project 选项后，点击 Finish 按钮：



8、右击文件夹 Source File 并点击 Add --> New Item... : 





9、选择  C++ File 然后设置文件名为 main.cpp，然后点击 Add：





10、拷贝以下代码到 main.cpp 中：

```cpp
#include 

int main()
{
    std::cout  Start Without Debugging (或按下 ctrl + F5) :






12、完成以上操作后，你可以看到以下输出：



g++ 应用说明

程序 g++ 是将 gcc 默认语言设为 C++ 的一个特殊的版本，链接时它自动使用 C++ 标准库而不用 C 标准库。通过遵循源码的命名规范并指定对应库的名字，用 gcc 来编译链接 C++ 程序是可行的，如下例所示：

```cpp
$ gcc main.cpp -lstdc++ -o main
```





下面是一个保存在文件 helloworld.cpp 中一个简单的 C++ 程序的代码：

```cpp
#include 
using namespace std;
int main()
{
    cout g++ 常用命令选项 

| 选项 | 解释 | -ansi | 只支持 ANSI 标准的 C 语法。这一选项将禁止 GNU C 的某些特色， 
例如 asm 或 typeof 关键词。 |
| --- | --- | --- | --- |
| -c | 只编译并生成目标文件。 |
| -DMACRO | 以字符串"1"定义 MACRO 宏。 |
| -DMACRO=DEFN | 以字符串"DEFN"定义 MACRO 宏。 |
| -E | 只运行 C 预编译器。 |
| -g | 生成调试信息。GNU 调试器可利用该信息。 |
| -IDIRECTORY | 指定额外的头文件搜索路径DIRECTORY。 |
| -LDIRECTORY | 指定额外的函数库搜索路径DIRECTORY。 |
| -lLIBRARY | 连接时搜索指定的函数库LIBRARY。 |
| -m486 | 针对 486 进行代码优化。 |
| -o | FILE 生成指定的输出文件。用在生成可执行文件时。 |
| -O0 | 不进行优化处理。 |
| -O | 或 -O1 优化生成代码。 |
| -O2 | 进一步优化。 |
| -O3 | 比 -O2 更进一步优化，包括 inline 函数。 |
| -shared | 生成共享目标文件。通常用在建立共享库时。 |
| -static | 禁止使用共享连接。 |
| -UMACRO | 取消对 MACRO 宏的定义。 |
| -w | 不生成任何警告信息。 |
| -Wall | 生成所有警告信息。 |


---

# C++ 基础


## C++ 基本语法

C++ 程序可以定义为对象的集合，这些对象通过调用彼此的方法进行交互。现在让我们简要地看一下什么是类、对象，方法、即时变量。


- **对象 -** 对象具有状态和行为。例如：一只狗的状态 - 颜色、名称、品种，行为 - 摇动、叫唤、吃。对象是类的实例。

- **类 -** 类可以定义为描述对象行为/状态的模板/蓝图。

- **方法 -** 从基本上说，一个方法表示一种行为。一个类可以包含多个方法。可以在方法中写入逻辑、操作数据以及执行所有的动作。

- **即时变量 -** 每个对象都有其独特的即时变量。对象的状态是由这些即时变量的值创建的。



C++ 程序结构

让我们看一段简单的代码，可以输出单词 *Hello World*。


### 实例



```cpp
#include
using namespace std;

// main() 是程序开始执行的地方

int main()
{
   cout 编译 & 执行 C++ 程序

接下来让我们看看如何把源代码保存在一个文件中，以及如何编译并运行它。下面是简单的步骤：


- 打开一个文本编辑器，添加上述代码。

- 保存文件为 hello.cpp。

- 打开命令提示符，进入到保存文件所在的目录。

- 键入 'g++ hello.cpp '，输入回车，编译代码。如果代码中没有错误，命令提示符会跳到下一行，并生成 a.out 可执行文件。

- 现在，键入 ' a.out' 来运行程序。	

- 您可以看到屏幕上显示 ' Hello World '。


```cpp
$ g++ hello.cpp
$ ./a.out
Hello World
```



请确保您的路径中已包含 g++ 编译器，并确保在包含源文件 hello.cpp 的目录中运行它。

您也可以使用 makefile 来编译 C/C++ 程序。

C++ 中的分号 & 语句块

在 C++ 中，分号是语句结束符。也就是说，每个语句必须以分号结束。它表明一个逻辑实体的结束。

例如，下面是三个不同的语句：
 

```cpp
x = y;
y = y+1;
add(x, y);
```



语句块是一组使用大括号括起来的按逻辑连接的语句。例如：
 

```cpp
{
   cout C++ 标识符

C++ 标识符是用来标识变量、函数、类、模块，或任何其他用户自定义项目的名称。一个标识符以字母 A-Z 或 a-z 或下划线 _ 开始，后跟零个或多个字母、下划线和数字（0-9）。

C++ 标识符内不允许出现标点字符，比如 @、& 和 %。C++ 是区分大小写的编程语言。因此，在 C++ 中，**Manpower** 和 **manpower** 是两个不同的标识符。

下面列出几个有效的标识符：

```cpp
mohd       zara    abc   move_name  a_123
myname50   _temp   j     a23b9      retVal
```



C++ 关键字

下表列出了 C++ 中的保留字。这些保留字不能作为常量名、变量名或其他标识符名称。

| asm | else | new | this |
| --- | --- | --- | --- |
| auto | enum | operator | throw |
| bool | explicit | private | true |
| break | export | protected | try |
| case | extern | public | typedef |
| catch | false | register | typeid |
| char | float | reinterpret_cast | typename |
| class | for | return | union |
| const | friend | short | unsigned |
| const_cast | goto | signed | using |
| continue | if | sizeof | virtual |
| default | inline | static | void |
| delete | int | static_cast | volatile |
| do | long | struct | wchar_t |
| double | mutable | switch | while |
| dynamic_cast | namespace | template |   |



完整关键字介绍可查阅：C++ 的关键字（保留字）完整介绍



三字符组

三字符组就是用于表示另一个字符的三个字符序列，又称为三字符序列。三字符序列总是以两个问号开头。

三字符序列不太常见，但 C++ 标准允许把某些字符指定为三字符序列。以前为了表示键盘上没有的字符，这是必不可少的一种方法。

三字符序列可以出现在任何地方，包括字符串、字符序列、注释和预处理指令。

下面列出了最常用的三字符序列：

| 三字符组 | 替换 |
| --- | --- |
| ??= | # |
| ??/ | \ |
| ??' | ^ |
| ??( | [ |
| ??) | ] |
| ??! | | |
| ?? | } |
| ??- | ~ |



如果希望在源程序中有两个连续的问号，且不希望被预处理器替换，这种情况出现在字符常量、字符串字面值或者是程序注释中，可选办法是用字符串的自动连接："...?""?..."或者转义序列："...?\?..."。


从Microsoft Visual C++ 2010版开始，该编译器默认不再自动替换三字符组。如果需要使用三字符组替换（如为了兼容古老的软件代码），需要设置编译器命令行选项/Zc:trigraphs


g++仍默认支持三字符组，但会给出编译警告。

C++ 中的空格

只包含空格的行，被称为空白行，可能带有注释，C++ 编译器会完全忽略它。

在 C++ 中，空格用于描述空白符、制表符、换行符和注释。空格分隔语句的各个部分，让编译器能识别语句中的某个元素（比如 int）在哪里结束，下一个元素在哪里开始。因此，在下面的语句中：

```cpp
int age;
```



在这里，int 和 age 之间必须至少有一个空格字符（通常是一个空白符），这样编译器才能够区分它们。另一方面，在下面的语句中：

```cpp
fruit = apples + oranges;   // 获取水果的总数
```



fruit 和 =，或者 = 和 apples 之间的空格字符不是必需的，但是为了增强可读性，您可以根据需要适当增加一些空格。


## C++ 注释

程序的注释是解释性语句，您可以在 C++ 代码中包含注释，这将提高源代码的可读性。所有的编程语言都允许某种形式的注释。

C++ 支持单行注释和多行注释。注释中的所有字符会被 C++ 编译器忽略。

C++ 注释一般有两种：

- 

// - 一般用于单行注释。
- 

/* ... */ - 一般用于多行注释。

注释以 // 开始，直到行末为止。例如：
 

### 实例



```cpp
#include
using namespace std;

int main() {
  // 这是一个注释
  cout
using namespace std;

int main()
{
   cout
using namespace std;

int main() {
    /* 这是注释 */

    /* C++ 注释也可以
     * 跨行
     */
    cout << "Hello World!";
    return 0;
}
```




在 /* 和 */ 注释内部，// 字符没有特殊的含义。在 // 注释内，/* 和 */ 字符也没有特殊的含义。因此，您可以在一种注释内嵌套另一种注释。例如：
 

```cpp
/* 用于输出 Hello World 的注释

cout << "Hello World"; // 输出 Hello World

*/
```


## C++ 数据类型

使用编程语言进行编程时，需要用到各种变量来存储各种信息。变量保留的是它所存储的值的内存位置。这意味着，当您创建一个变量时，就会在内存中保留一些空间。

您可能需要存储各种数据类型（比如字符型、宽字符型、整型、浮点型、双浮点型、布尔型等）的信息，操作系统会根据变量的数据类型，来分配内存和决定在保留内存中存储什么。


基本的内置类型

C++ 为程序员提供了种类丰富的内置数据类型和用户自定义的数据类型。下表列出了七种基本的 C++ 数据类型：

| 类型 | 关键字 |
| --- | --- |
| 布尔型 | bool |
| 字符型 | char |
| 整型 | int |
| 浮点型 | float |
| 双浮点型 | double |
| 无类型 | void |
| 宽字符型 | wchar_t |



其实 wchar_t 是这样来的：


```cpp
typedef short int wchar_t;
```



所以 wchar_t 实际上的空间是和 short int 一样。

一些基本类型可以使用一个或多个类型修饰符进行修饰：

| 修饰符 | 描述 | 示例 |
| --- | --- | --- |
| signed | 表示有符号类型（默认） | signed int x = -10; |
| unsigned | 表示无符号类型 | unsigned int y = 10; |
| short | 表示短整型 | short int z = 100; |
| long | 表示长整型 | long int a = 100000; |
| const | 表示常量，值不可修改 | const int b = 5; |
| volatile | 表示变量可能被意外修改，禁止编译器优化 | volatile int c = 10; |
| mutable | 表示类成员可以在 const 对象中修改 | mutable int counter; |




下表显示了各种变量类型在内存中存储值时需要占用的内存，以及该类型的变量所能存储的最大值和最小值。

**注意：**不同系统会有所差异，一字节为 8 位。

**注意：**默认情况下，int、short、long都是带符号的，即 signed。

**注意：**long int 8 个字节，int 都是 4 个字节，早期的 C 编译器定义了 long int 占用 4 个字节，int 占用 2 个字节，新版的 C/C++ 标准兼容了早期的这一设定。

| 数据类型 | 描述 | 大小（字节） | 范围/取值示例 |
| --- | --- | --- | --- |
| bool | 布尔类型，表示真或假 | 1 | true 或 false |
| char | 字符类型，通常用于存储 ASCII 字符 | 1 | -128 到 127 或 0 到 255 |
| signed char | 有符号字符类型 | 1 | -128 到 127 |
| unsigned char | 无符号字符类型 | 1 | 0 到 255 |
| wchar_t | 宽字符类型，用于存储 Unicode 字符 | 2 或 4 | 取决于平台 |
| char16_t | 16 位 Unicode 字符类型（C++11 引入） | 2 | 0 到 65,535 |
| char32_t | 32 位 Unicode 字符类型（C++11 引入） | 4 | 0 到 4,294,967,295 |
| short | 短整型 | 2 | -32,768 到 32,767 |
| unsigned short | 无符号短整型 | 2 | 0 到 65,535 |
| int | 整型 | 4 | -2,147,483,648 到 2,147,483,647 |
| unsigned int | 无符号整型 | 4 | 0 到 4,294,967,295 |
| long | 长整型 | 4 或 8 | 取决于平台 |
| unsigned long | 无符号长整型 | 4 或 8 | 取决于平台 |
| long long | 长长整型（C++11 引入） | 8 | -9,223,372,036,854,775,808 到 9,223,372,036,854,775,807 |
| unsigned long long | 无符号长长整型（C++11 引入） | 8 | 0 到 18,446,744,073,709,551,615 |
| float | 单精度浮点数 | 4 | 约 ±3.4e±38（6-7 位有效数字） |
| double | 双精度浮点数 | 8 | 约 ±1.7e±308（15 位有效数字） |
| long double | 扩展精度浮点数 | 8、12 或 16 | 取决于平台 |



C++11 新增类型

| 数据类型 | 描述 | 示例 |
| --- | --- | --- |
| auto | 自动类型推断 | auto x = 10; |
| decltype | 获取表达式的类型 | decltype(x) y = 20; |
| nullptr | 空指针常量 | int* ptr = nullptr; |
| std::initializer_list | 初始化列表类型 | std::initializer_list list = {1, 2, 3}; |
| std::tuple | 元组类型，可以存储多个不同类型的值 | std::tuple t(1, 2.0, 'a'); |



注意，各种类型的存储大小与系统位数有关，但目前通用的以64位系统为主。

以下列出了32位系统与64位系统的存储大小的差别（windows 相同）：



从上表可得知，变量的大小会根据编译器和所使用的电脑而有所不同。

下面实例会输出您电脑上各种数据类型的大小。
 

### 实例



```cpp
#include
#include
-

using namespace std;

int main()
{
    cout ::max)();
    cout ::min)() ::max)();
    cout ::min)() ::max)();
    cout ::min)() ::max)();
    cout ::min)() ::max)();
    cout ::min)() ::max)();
    cout ::min)() ::max)();
    cout ::min)() ::max)();
    cout ::min)() ::max)();
    cout ::min)() ::max)();
    cout ::min)() ::max)();
    cout ::min)() ::max)();
    cout ::min)() ::max)();
    cout ::min)() ::max)();
    cout ::min)() ::max)() ::min)() 派生数据类型

| 数据类型 | 描述 | 示例 |
| --- | --- | --- |
| 数组 | 相同类型元素的集合 | int arr[5] = {1, 2, 3, 4, 5}; |
| 指针 | 存储变量内存地址的类型 | int* ptr = &x; |
| 引用 | 变量的别名 | int& ref = x; |
| 函数 | 函数类型，表示函数的签名 | int func(int a, int b); |
| 结构体 | 用户定义的数据类型，可以包含多个不同类型的成员 | struct Point { int x; int y; }; |
| 类 | 用户定义的数据类型，支持封装、继承和多态 | class MyClass { ... }; |
| 联合体 | 多个成员共享同一块内存 | union Data { int i; float f; }; |
| 枚举 | 用户定义的整数常量集合 | enum Color { RED, GREEN, BLUE }; |

类型别名

| 别名 | 描述 | 示例 |
| --- | --- | --- |
| typedef | 为现有类型定义别名 | typedef int MyInt; |
| using | 为现有类型定义别名（C++11 引入） | using MyInt = int; |



标准库类型

| 数据类型 | 描述 | 示例 |
| --- | --- | --- |
| std::string | 字符串类型 | std::string s = "Hello"; |
| std::vector | 动态数组 | std::vector v = {1, 2, 3}; |
| std::array | 固定大小数组（C++11 引入） | std::array a = {1, 2, 3}; |
| std::pair | 存储两个值的容器 | std::pair p(1, 2.0); |
| std::map | 键值对容器 | std::map m; |
| std::set | 唯一值集合 | std::set s = {1, 2, 3}; |


typedef 声明

您可以使用 **typedef** 为一个已有的类型取一个新的名字。下面是使用 typedef 定义一个新类型的语法：

```cpp
typedef type newname;
```



例如，下面的语句会告诉编译器，feet 是 int 的另一个名称：

```cpp
typedef int feet;
```



现在，下面的声明是完全合法的，它创建了一个整型变量 distance：

```cpp
feet distance;
```



枚举类型


枚举类型(enumeration)是C++中的一种派生数据类型，它是由用户定义的若干枚举常量的集合。

如果一个变量只有几种可能的值，可以定义为枚举(enumeration)类型。所谓"枚举"是指将变量的值一一列举出来，变量的值只能在列举出来的值的范围内。

创建枚举，需要使用关键字 **enum**。枚举类型的一般形式为：

```cpp
enum 枚举名{ 
     标识符[=整型常数], 
     标识符[=整型常数], 
... 
    标识符[=整型常数]
} 枚举变量;
```



如果枚举没有初始化, 即省掉"=整型常数"时, 则从第一个标识符开始。

例如，下面的代码定义了一个颜色枚举，变量 c 的类型为 color。最后，c 被赋值为 "blue"。

```cpp
enum color { red, green, blue } c;
c = blue;
```



默认情况下，第一个名称的值为 0，第二个名称的值为 1，第三个名称的值为 2，以此类推。但是，您也可以给名称赋予一个特殊的值，只需要添加一个初始值即可。例如，在下面的枚举中，**green** 的值为 5。

```cpp
enum color { red, green=5, blue };
```



在这里，**blue** 的值为 6，因为默认情况下，每个名称都会比它前面一个名称大 1，但 red 的值依然为 0。



类型转换

类型转换是将一个数据类型的值转换为另一种数据类型的值。

C++ 中有四种类型转换：静态转换、动态转换、常量转换和重新解释转换。

静态转换（Static Cast）

静态转换是将一种数据类型的值强制转换为另一种数据类型的值。


静态转换通常用于比较类型相似的对象之间的转换，例如将 int 类型转换为 float 类型。


静态转换不进行任何运行时类型检查，因此可能会导致运行时错误。


### 实例


```cpp
int i = 10;
float f = static_cast(i); // 静态将int类型转换为float类型
```


动态转换（Dynamic Cast）


动态转换（dynamic_cast）是 C++ 中用于在继承层次结构中进行向下转换（downcasting）的一种机制。


动态转换通常用于将一个基类指针或引用转换为派生类指针或引用。

动态转换在运行时进行类型检查。如果转换失败，对于指针类型会返回 nullptr，对于引用类型则会抛出 std::bad_cast 异常。


**语法：**

```cpp
dynamic_cast(表达式)
```

-

**目标类型**：必须是指针或引用类型。
-

**表达式**：需要转换的基类指针或引用。



### 实例：指针类型的动态转换


```cpp
#include

class Base {
public:
    virtual ~Base() = default; // 基类必须具有虚函数
};

class Derived : public Base {
public:
    void show() {
        std::cout (ptr_base);

    if (ptr_derived) {
        ptr_derived->show(); // 成功转换，调用派生类方法
    } else {
        std::cout

#include

class Base {

public:

    virtual ~Base() = default; // 基类必须具有虚函数

};

class Derived : public Base {

public:

    void show() {

        std::cout (ref_base);

        ref_derived.show(); // 成功转换，调用派生类方法

    } catch (const std::bad_cast& e) {

        std::cout 常量转换（Const Cast）

常量转换用于将 const 类型的对象转换为非 const 类型的对象。

常量转换只能用于转换掉 const 属性，不能改变对象的类型。

### 实例


```cpp
const int i = 10;
int& r = const_cast(i); // 常量转换，将const int转换为int
```


重新解释转换（Reinterpret Cast）

重新解释转换将一个数据类型的值重新解释为另一个数据类型的值，通常用于在不同的数据类型之间进行转换。

重新解释转换不进行任何类型检查，因此可能会导致未定义的行为。


### 实例


```cpp
int i = 10;
float f = reinterpret_cast(i); // 重新解释将int类型转换为float类型
```


## C++ 变量类型

变量其实只不过是程序可操作的存储区的名称。


在 C++ 中，有多种变量类型可用于存储不同种类的数据。


C++ 中每个变量都有指定的类型，类型决定了变量存储的大小和布局，该范围内的值都可以存储在内存中，运算符可应用于变量上。

变量的名称可以由字母、数字和下划线字符组成。它必须以字母或下划线开头。

大写字母和小写字母是不同的，因为 C++ 是大小写敏感的。

基于前一章讲解的基本类型，有以下几种基本的变量类型，将在下一章中进行讲解：

| 类型 | 描述 |
| --- | --- |
| bool | 布尔类型，存储值 true 或 false，占用 1 个字节。 |
| char | 字符类型，用于存储 ASCII 字符，通常占用 1 个字节。 |
| int | 整数类型，通常用于存储普通整数，通常占用 4 个字节。 |
| float | 单精度浮点值，用于存储单精度浮点数。单精度是这样的格式，1 位符号，8 位指数，23 位小数，通常占用4个字节。 |
| double | 双精度浮点值，用于存储双精度浮点数。双精度是 1 位符号，11 位指数，52 位小数，通常占用 8 个字节。 |
| void | 表示类型的缺失。 |
| wchar_t | 宽字符类型，用于存储更大范围的字符，通常占用 2 个或 4 个字节。 |



C++ 也允许定义各种其他类型的变量，比如**枚举、指针、数组、引用、数据结构、类**等等，这将会在后续的章节中进行讲解。

-

整数类型（Integer Types）：
- `int`：用于表示整数，通常占用4个字节。
- `short`：用于表示短整数，通常占用2个字节。
- `long`：用于表示长整数，通常占用4个字节。
- `long long`：用于表示更长的整数，通常占用8个字节。
-

浮点类型（Floating-Point Types）：
- `float`：用于表示单精度浮点数，通常占用4个字节。
- `double`：用于表示双精度浮点数，通常占用8个字节。
- `long double`：用于表示更高精度的浮点数，占用字节数可以根据实现而变化。
-

字符类型（Character Types）：
- `char`：用于表示字符，通常占用1个字节。
- `wchar_t`：用于表示宽字符，通常占用2或4个字节。
- `char16_t`：用于表示16位Unicode字符，占用2个字节。
- `char32_t`：用于表示32位Unicode字符，占用4个字节。
-

布尔类型（Boolean Type）：
- `bool`：用于表示布尔值，只能取`true`或`false`。
-

枚举类型（Enumeration Types）：
- `enum`：用于定义一组命名的整数常量。
-

指针类型（Pointer Types）：
- `type*`：用于表示指向类型为`type`的对象的指针。
-

数组类型（Array Types）：
- `type[]`或`type[size]`：用于表示具有相同类型的元素组成的数组。
-

结构体类型（Structure Types）：
- `struct`：用于定义包含多个不同类型成员的结构。
-

类类型（Class Types）：
- `class`：用于定义具有属性和方法的自定义类型。
-

共用体类型（Union Types）：
- `union`：用于定义一种特殊的数据类型，它可以在相同的内存位置存储不同的数据类型。



在 C++ 中，类型的长度（即占用的字节数）取决于编译器和计算机架构，然而，C++ 标准规定了不同整数类型的最小范围，而不是具体的字节数，这是为了确保代码在不同的系统上都能正确运行。

请注意，以上类型的范围只是 C++ 标准规定的最小要求，实际上，许多系统上这些类型可能占用更多的字节，例如，很多现代计算机上 int 通常占用 4 字节，而 long 可能占用 8 字节。



下面我们将讲解如何定义、声明和使用各种类型的变量。

C++ 中的变量定义

变量定义就是告诉编译器在何处创建变量的存储，以及如何创建变量的存储。




变量定义指定一个数据类型，并包含了该类型的一个或多个变量的列表，如下所示：

```cpp
type variable_list;
```




在这里，**type** 必须是一个有效的 C++ 数据类型，可以是 char、wchar_t、int、float、double、bool 或任何用户自定义的对象，**variable_list** 可以由一个或多个标识符名称组成，多个标识符之间用逗号分隔。下面列出几个有效的声明：
 

```cpp
int    i, j, k;
char   c, ch;
float  f, salary;
double d;
```



行 **int i, j, k;** 声明并定义了变量 i、j 和 k，这指示编译器创建类型为 int 的名为 i、j、k 的变量。

变量可以在声明的时候被初始化（指定一个初始值）。初始化器由一个等号，后跟一个常量表达式组成，如下所示：
 

```cpp
type variable_name = value;
```



下面列举几个实例：
 

```cpp
extern int d = 3, f = 5;    // d 和 f 的声明
int d = 3, f = 5;           // 定义并初始化 d 和 f
byte z = 22;                // 定义并初始化 z
char x = 'x';               // 变量 x 的值为 'x'
```



不带初始化的定义：带有静态存储持续时间的变量会被隐式初始化为 NULL（所有字节的值都是 0），其他所有变量的初始值是未定义的。

C++ 中的变量声明

变量声明向编译器保证变量以给定的类型和名称存在，这样编译器在不需要知道变量完整细节的情况下也能继续进一步的编译。变量声明只在编译时有它的意义，在程序连接时编译器需要实际的变量声明。

当您使用多个文件且只在其中一个文件中定义变量时（定义变量的文件在程序连接时是可用的），变量声明就显得非常有用。您可以使用 **extern** 关键字在任何地方声明一个变量。虽然您可以在 C++ 程序中多次声明一个变量，但变量只能在某个文件、函数或代码块中被定义一次。

实例

尝试下面的实例，其中，变量在头部就已经被声明，但它们是在主函数内被定义和初始化的：

 

### 实例



```cpp
#include
using namespace std;

// 变量声明
extern int a, b;
extern int c;
extern float f;

int main ()
{
  // 变量定义
  int a, b;
  int c;
  float f;

  // 实际初始化
  a = 10;
  b = 20;
  c = a + b;

  cout C++ 中的左值（Lvalues）和右值（Rvalues）

C++ 中有两种类型的表达式：


- **左值（lvalue）：**指向内存位置的表达式被称为左值（lvalue）表达式。左值可以出现在赋值号的左边或右边。

- **右值（rvalue）：**术语右值（rvalue）指的是存储在内存中某些地址的数值。右值是不能对其进行赋值的表达式，也就是说，右值可以出现在赋值号的右边，但不能出现在赋值号的左边。


变量是左值，因此可以出现在赋值号的左边。数值型的字面值是右值，因此不能被赋值，不能出现在赋值号的左边。下面是一个有效的语句：

```cpp
int g = 20;
```



但是下面这个就不是一个有效的语句，会生成编译时错误：

```cpp
10 = 20;
```


## C++ 变量作用域

一般来说有三个地方可以定义变量：


-

在函数或一个代码块内部声明的变量，称为**局部变量**。

-

在函数参数的定义中声明的变量，称为**形式参数**。

-

在所有函数外部声明的变量，称为**全局变量**。



作用域是程序的一个区域，变量的作用域可以分为以下几种：


-

**局部作用域**：在函数内部声明的变量具有局部作用域，它们只能在函数内部访问。局部变量在函数每次被调用时被创建，在函数执行完后被销毁。

-

**全局作用域**：在所有函数和代码块之外声明的变量具有全局作用域，它们可以被程序中的任何函数访问。全局变量在程序开始时被创建，在程序结束时被销毁。

-

**块作用域**：在代码块内部声明的变量具有块作用域，它们只能在代码块内部访问。块作用域变量在代码块每次被执行时被创建，在代码块执行完后被销毁。
-

**类作用域**：在类内部声明的变量具有类作用域，它们可以被类的所有成员函数访问。类作用域变量的生命周期与类的生命周期相同。


**注意：**如果在内部作用域中声明的变量与外部作用域中的变量同名，则内部作用域中的变量将覆盖外部作用域中的变量。
局部变量

在函数或一个代码块内部声明的变量，称为局部变量。它们只能被函数内部或者代码块内部的语句使用。下面的实例使用了局部变量：

 

### 实例



```cpp
#include
using namespace std;

int main ()
{
  // 局部变量声明
  int a, b;
  int c;

  // 实际初始化
  a = 10;
  b = 20;
  c = a + b;

  cout 全局变量

在所有函数外部定义的变量（通常是在程序的头部），称为全局变量。全局变量的值在程序的整个生命周期内都是有效的。

全局变量可以被任何函数访问。也就是说，全局变量一旦声明，在整个程序中都是可用的。下面的实例使用了全局变量和局部变量：
 

### 实例



```cpp
#include
using namespace std;

// 全局变量声明
int g;

int main ()
{
  // 局部变量声明
  int a, b;

  // 实际初始化
  a = 10;
  b = 20;
  g = a + b;

  cout
using namespace std;

// 全局变量声明
int g = 20;

int main ()
{
  // 局部变量声明
  int g = 10;

  cout 初始化局部变量和全局变量

当局部变量被定义时，系统不会对其初始化，您必须自行对其初始化。定义全局变量时，系统会自动初始化为下列值：

| 数据类型 | 初始化默认值 |
| --- | --- |
| int | 0 |
| char | '\0' |
| float | 0 |
| double | 0 |
| pointer | NULL |



正确地初始化变量是一个良好的编程习惯，否则有时候程序可能会产生意想不到的结果。



块作用域指的是在代码块内部声明的变量：


### 实例


```cpp
#include

int main() {

    int a = 10;

    {

        int a = 20;  // 块作用域变量

        std::cout 类作用域


类作用域指的是在类内部声明的变量：


### 实例


```cpp
#include

class MyClass {

public:

    static int class_var;  // 类作用域变量

};

int MyClass::class_var = 30;

int main() {

    std::cout << "类变量: " << MyClass::class_var << std::endl;

    return 0;

}
```

以上实例中，MyClass 类中声明了一个名为 class_var 的类作用域变量。可以使用类名和作用域解析运算符 :: 来访问这个变量。在 main() 函数中访问 class_var 时输出的是 30。

```cpp
类变量: 30
```


## C++ 常量

常量是固定值，在程序执行期间不会改变。这些固定的值，又叫做**字面量**。

常量可以是任何的基本数据类型，可分为整型数字、浮点数字、字符、字符串和布尔值。

常量就像是常规的变量，只不过常量的值在定义后不能进行修改。


整数常量

整数常量可以是十进制、八进制或十六进制的常量。前缀指定基数：0x 或 0X 表示十六进制，0 表示八进制，不带前缀则默认表示十进制。

整数常量也可以带一个后缀，后缀是 U 和 L 的组合，U 表示无符号整数（unsigned），L 表示长整数（long）。后缀可以是大写，也可以是小写，U 和 L 的顺序任意。

下面列举几个整数常量的实例：
 

```cpp
212         // 合法的
215u        // 合法的
0xFeeL      // 合法的
078         // 非法的：8 不是八进制的数字
032UU       // 非法的：不能重复后缀
```



以下是各种类型的整数常量的实例：
 

```cpp
85         // 十进制
0213       // 八进制
0x4b       // 十六进制
30         // 整数
30u        // 无符号整数
30l        // 长整数
30ul       // 无符号长整数
```



浮点常量

浮点常量由整数部分、小数点、小数部分和指数部分组成。您可以使用小数形式或者指数形式来表示浮点常量。

当使用小数形式表示时，必须包含整数部分、小数部分，或同时包含两者。当使用指数形式表示时， 必须包含小数点、指数，或同时包含两者。带符号的指数是用 e 或 E 引入的。

下面列举几个浮点常量的实例：
 

```cpp
3.14159       // 合法的
314159E-5L    // 合法的
510E          // 非法的：不完整的指数
210f          // 非法的：没有小数或指数
.e55          // 非法的：缺少整数或分数
```



布尔常量

布尔常量共有两个，它们都是标准的 C++ 关键字：


- **true** 值代表真。

- **false** 值代表假。


我们不应把 true 的值看成 1，把 false 的值看成 0。

字符常量

字符常量是括在单引号中。如果常量以 L（仅当大写时）开头，则表示它是一个宽字符常量（例如 L'x'），此时它必须存储在 **wchar_t** 类型的变量中。否则，它就是一个窄字符常量（例如 'x'），此时它可以存储在 **char** 类型的简单变量中。

字符常量可以是一个普通的字符（例如 'x'）、一个转义序列（例如 '\t'），或一个通用的字符（例如 '\u02C0'）。

在 C++ 中，有一些特定的字符，当它们前面有反斜杠时，它们就具有特殊的含义，被用来表示如换行符（\n）或制表符（\t）等。下表列出了一些这样的转义序列码：

| 转义序列 | 含义 |
| --- | --- |
| \\ | \ 字符 |
| \' | ' 字符 |
| \" | " 字符 |
| \? | ? 字符 |
| \a | 警报铃声 |
| \b | 退格键 |
| \f | 换页符 |
| \n | 换行符 |
| \r | 回车 |
| \t | 水平制表符 |
| \v | 垂直制表符 |
| \ooo | 一到三位的八进制数 |
| \xhh . . . | 一个或多个数字的十六进制数 |



下面的实例显示了一些转义序列字符：
 

### 实例



```cpp
#include
using namespace std;

int main()
{
   cout 字符串常量

字符串字面值或常量是括在双引号 "" 中的。一个字符串包含类似于字符常量的字符：普通的字符、转义序列和通用的字符。

您可以使用 \ 做分隔符，把一个很长的字符串常量进行分行。

下面的实例显示了一些字符串常量：


### 实例


```cpp
#include

#include

using namespace std;

int main() {

    string greeting = "hello, runoob";

    cout 定义常量

在 C++ 中，有两种简单的定义常量的方式：


- 使用 **#define** 预处理器。

- 使用 **const** 关键字。

#define 预处理器

下面是使用 #define 预处理器定义常量的形式：

```cpp
#define identifier value
```



具体请看下面的实例：
 

### 实例



```cpp
#include
using namespace std;

#define LENGTH 10
#define WIDTH  5
#define NEWLINE '\n'

int main()
{

   int area;

   area = LENGTH * WIDTH;
   cout const 关键字

您可以使用 **const** 前缀声明指定类型的常量，如下所示：

```cpp
const type variable = value;
```



具体请看下面的实例：
 

### 实例



```cpp
#include
using namespace std;

int main()
{
   const int  LENGTH = 10;
   const int  WIDTH  = 5;
   const char NEWLINE = '\n';
   int area;

   area = LENGTH * WIDTH;
   cout << area;
   cout << NEWLINE;
   return 0;
}
```



当上面的代码被编译和执行时，它会产生下列结果：

```cpp
50
```



请注意，把常量定义为大写字母形式，是一个很好的编程实践。


## C++ 修饰符类型

C++ 允许在 **char、int 和 double** 数据类型前放置修饰符。


修饰符是用于改变变量类型的行为的关键字，它更能满足各种情境的需求。

下面列出了数据类型修饰符：

-

signed：表示变量可以存储负数。对于整型变量来说，signed 可以省略，因为整型变量默认为有符号类型。
-

unsigned：表示变量不能存储负数。对于整型变量来说，unsigned 可以将变量范围扩大一倍。
-

short：表示变量的范围比 int 更小。short int 可以缩写为 short。
-

long：表示变量的范围比 int 更大。long int 可以缩写为 long。
-

long long：表示变量的范围比 long 更大。C++11 中新增的数据类型修饰符。
-

float：表示单精度浮点数。
-

double：表示双精度浮点数。
-

bool：表示布尔类型，只有 true 和 false 两个值。
-

char：表示字符类型。
-

wchar_t：表示宽字符类型，可以存储 Unicode 字符。

修饰符 **signed、unsigned、long 和 short** 可应用于整型，**signed** 和 **unsigned** 可应用于字符型，**long** 可应用于双精度型。

这些修饰符也可以组合使用，修饰符 **signed** 和 **unsigned** 也可以作为 **long** 或 **short** 修饰符的前缀。例如：**unsigned long int**。

C++ 允许使用速记符号来声明**无符号短整数**或**无符号长整数**。您可以不写 int，只写单词 **unsigned、short** 或 **long**，**int** 是隐含的。例如，下面的两个语句都声明了无符号整型变量。

```cpp
signed int num1 = -10; // 定义有符号整型变量 num1，初始值为 -10
unsigned int num2 = 20; // 定义无符号整型变量 num2，初始值为 20

short int num1 = 10; // 定义短整型变量 num1，初始值为 10
long int num2 = 100000; // 定义长整型变量 num2，初始值为 100000

long long int num1 = 10000000000; // 定义长长整型变量 num1，初始值为 10000000000

float num1 = 3.14f; // 定义单精度浮点数变量 num1，初始值为 3.14
double num2 = 2.71828; // 定义双精度浮点数变量 num2，初始值为 2.71828

bool flag = true; // 定义布尔类型变量 flag，初始值为 true

char ch1 = 'a'; // 定义字符类型变量 ch1，初始值为 'a'
wchar_t ch2 = L'你'; // 定义宽字符类型变量 ch2，初始值为 '你'
```



为了理解 C++ 解释有符号整数和无符号整数修饰符之间的差别，我们来运行一下下面这个短程序：
 

### 实例



```cpp
#include
using namespace std;

/*
 * 这个程序演示了有符号整数和无符号整数之间的差别
*/
int main()
{
   short int i;           // 有符号短整数
   short unsigned int j;  // 无符号短整数

   j = 50000;

   i = j;
   cout C++ 中的类型限定符

类型限定符提供了变量的额外信息，用于在定义变量或函数时改变它们的默认行为的关键字。

| 限定符 | 含义 |
| --- | --- |
| const | const 定义常量，表示该变量的值不能被修改。 |
| volatile | 修饰符 volatile 告诉该变量的值可能会被程序以外的因素改变，如硬件或其他线程。。 |
| restrict | 由 restrict 修饰的指针是唯一一种访问它所指向的对象的方式。只有 C99 增加了新的类型限定符 restrict。 |
| mutable | mutable 用于修饰类的成员变量。被 mutable 修饰的成员变量可以被修改，即使它们所在的对象是 const 的。 |
| static | 用于定义静态变量，表示该变量的作用域仅限于当前文件或当前函数内，不会被其他文件或函数访问。 |
| register | 用于定义寄存器变量，表示该变量被频繁使用，可以存储在CPU的寄存器中，以提高程序的运行效率。在 C++11 中被标记为弃用(deprecated)
在 C++17 中被正式移除。 |



const 实例


```cpp
const int NUM = 10; // 定义常量 NUM，其值不可修改
const int* ptr = &NUM; // 定义指向常量的指针，指针所指的值不可修改
int const* ptr2 = &NUM; // 和上面一行等价
```


volatile 实例


```cpp
volatile int num = 20; // 定义变量 num，其值可能会在未知的时间被改变
```


mutable 实例

```cpp
class Example {
public:
    int get_value() const {
        return value_; // const 关键字表示该成员函数不会修改对象中的数据成员
    }
    void set_value(int value) const {
        value_ = value; // mutable 关键字允许在 const 成员函数中修改成员变量
    }
private:
    mutable int value_;
};
```


static 实例

```cpp
void example_function() {
    static int count = 0; // static 关键字使变量 count 存储在程序生命周期内都存在
    count++;
}
```


register 实例

```cpp
void example_function(register int num) {
    // register 关键字建议编译器将变量 num 存储在寄存器中
    // 以提高程序执行速度
    // 但是实际上是否会存储在寄存器中由编译器决定
}
```

C++11 后 register 的变化：


- 
在 C++11 中被标记为弃用(deprecated)


- 
在 C++17 中被正式移除


- 
保留为关键字（可能用于兼容或未来用途）


## C++ 存储类

存储类定义 C++ 程序中变量/函数的范围（可见性）和生命周期。这些说明符放置在它们所修饰的类型之前。下面列出 C++ 程序中可用的存储类：


-

**auto**：这是默认的存储类说明符，通常可以省略不写。auto 指定的变量具有自动存储期，即它们的生命周期仅限于定义它们的块（block）。auto 变量通常在栈上分配。

-

**register**：用于建议编译器将变量存储在CPU寄存器中以提高访问速度。在 C++11 及以后的版本中，register 已经是一个废弃的特性，不再具有实际作用。

-

**static**：用于定义具有静态存储期的变量或函数，它们的生命周期贯穿整个程序的运行期。在函数内部，static变量的值在函数调用之间保持不变。在文件内部或全局作用域，static变量具有内部链接，只能在定义它们的文件中访问。

-

**extern**：用于声明具有外部链接的变量或函数，它们可以在多个文件之间共享。默认情况下，全局变量和函数具有 extern 存储类。在一个文件中使用extern声明另一个文件中定义的全局变量或函数，可以实现跨文件共享。

-

**mutable (C++11)**：用于修饰类中的成员变量，允许在const成员函数中修改这些变量的值。通常用于缓存或计数器等需要在const上下文中修改的数据。

-

**thread_local (C++11)**：用于定义具有线程局部存储期的变量，每个线程都有自己的独立副本。线程局部变量的生命周期与线程的生命周期相同。



从 C++ 17 开始，auto 关键字不再是 C++ 存储类说明符，且 register 关键字被弃用。


中的存储类说明符为程序员提供了控制变量和函数生命周期及可见性的手段。

合理使用存储类说明符可以提高程序的可维护性和性能。


从 C++11 开始，register 已经失去了原有的作用，而 mutable 和 thread_local 则是新引入的特性，用于解决特定的编程问题。

下面是一个展示不同存储类说明符的实例：

### 实例


```cpp
#include

// 全局变量，具有外部链接，默认存储类为extern

int globalVar;

void function() {

    // 局部变量，具有自动存储期，默认存储类为auto

    auto int localVar = 10;

    // 静态变量，具有静态存储期，生命周期贯穿整个程序

    static int staticVar = 20;

    const int constVar = 30; // const变量默认具有static存储期

    // 尝试修改const变量，编译错误

    // constVar = 40;

    // mutable成员变量，可以在const成员函数中修改

    class MyClass {

    public:

        mutable int mutableVar;

        void constMemberFunc() const {

            mutableVar = 50; // 允许修改mutable成员变量

        }

    };

    // 线程局部变量，每个线程有自己的独立副本

    thread_local int threadVar = 60;

}

int main() {

    extern int externalVar; // 声明具有外部链接的变量

    function();

    return 0;

}
```

auto 存储类

自 C++ 11 以来，**auto** 关键字用于两种情况：声明变量时根据初始化表达式自动推断该变量的类型、声明函数时函数返回值的占位符。

C++98 标准中 auto 关键字用于自动变量的声明，但由于使用极少且多余，在 C++17 中已删除这一用法。

根据初始化表达式自动推断被声明的变量的类型，如：


```cpp
auto f=3.14;      //double
auto s("hello");  //const char*
auto z = new auto(9); // int*
auto x1 = 5, x2 = 5.0, x3='r';//错误，必须是初始化为同一类型
```




register 存储类


register 是一种存储类（storage class），用于声明变量，并提示编译器将这些变量存储在寄存器中，以便快速访问。

使用 register 关键字可以提高程序的执行速度，因为它减少了对内存的访问次数。


然而，需要注意的是，register 存储类只是一种提示，编译器可以忽略它，因为现代的编译器通常会自动优化代码，选择合适的存储位置。

**语法格式：**

```cpp
register data_type variable_name;
```



- `register` 是存储类的关键字，用于提示编译器将变量存储在寄存器中。
- `data_type` 是变量的数据类型，可以是任何合法的 C++ 数据类型。
- `variable_name` 是变量的名称。



```cpp
void loop() {
    register int i;
    for (i = 0; i static 存储类

**static** 存储类指示编译器在程序的生命周期内保持局部变量的存在，而不需要在每次它进入和离开作用域时进行创建和销毁。因此，使用 static 修饰局部变量可以在函数调用之间保持局部变量的值。

static 修饰符也可以应用于全局变量。当 static 修饰全局变量时，会使变量的作用域限制在声明它的文件内。

在 C++ 中，当 static 用在类数据成员上时，会导致仅有一个该成员的副本被类的所有对象共享。


### 实例



```cpp
#include

// 函数声明
void func(void);

static int count = 10; /* 全局变量 */

int main()
{
    while(count--)
    {
       func();
    }
    return 0;
}
// 函数定义
void func( void )
{
    static int i = 5; // 局部静态变量
    i++;
    std::cout extern 存储类

**extern** 存储类用于提供一个全局变量的引用，全局变量对所有的程序文件都是可见的。当您使用 'extern' 时，对于无法初始化的变量，会把变量名指向一个之前定义过的存储位置。

当您有多个文件且定义了一个可以在其他文件中使用的全局变量或函数时，可以在其他文件中使用 *extern* 来得到已定义的变量或函数的引用。可以这么理解，*extern* 是用来在另一个文件中声明一个全局变量或函数。

extern 修饰符通常用于当有两个或多个文件共享相同的全局变量或函数的时候，如下所示：

第一个文件：main.cpp


### 实例



```cpp
#include

int count ;
extern void write_extern();

int main()
{
   count = 5;
   write_extern();
}
```



第二个文件：support.cpp


### 实例



```cpp
#include

extern int count;

void write_extern(void)
{
   std::cout mutable 存储类

mutable 是一个关键字，用于修饰类的成员变量，使其能够在 const 成员函数中被修改。通常情况下，const 成员函数不能修改对象的状态，但如果某个成员变量被声明为 mutable，则可以在 const 函数中对其进行修改。

**特点：**

- **允许修改**：`mutable` 成员变量可以在 `const` 成员函数内被改变。
- **设计目的**：通常用于需要在不改变对象外部状态的情况下进行状态管理的场景，比如缓存、延迟计算等。


### 实例


```cpp
#include

class Example {

public:

    Example() : value(0), cachedValue(0) {}

    // 常量成员函数

    int getValue() const {

        return value; // 读取常量成员

    }

    // 修改 mutable 成员

    void increment() {

        ++value;

        cachedValue = value * 2; // 修改 mutable 成员

    }

    int getCachedValue() const {

        return cachedValue; // 读取 mutable 成员

    }

private:

    int value;                 // 常规成员，不能在 const 函数中修改

    mutable int cachedValue;   // 可修改成员，可以在 const 函数中修改

};

int main() {

    const Example ex;

    // ex.increment(); // 错误：无法在 const 对象上调用非 const 函数

    // ex.value = 10;  // 错误：无法修改 const 对象的成员

    std::cout thread_local 存储类


thread_local 是 C++11 引入的一种存储类，用于在多线程环境中管理线程特有的变量。

使用 thread_local 修饰的变量在每个线程中都有独立的实例，因此每个线程对该变量的操作不会影响其他线程。

- **独立性**：每个线程都有自己独立的变量副本，不同线程之间的读写操作互不干扰。
- **生命周期**：`thread_local` 变量在其线程结束时自动销毁。
- **初始化**：`thread_local` 变量可以进行静态初始化或动态初始化，支持在声明时初始化。

thread_local 适合用于需要存储线程状态、缓存或者避免数据竞争的场景，如线程池、请求上下文等。

以下演示了可以被声明为 thread_local 的变量：


```cpp
#include
#include

thread_local int threadSpecificVar = 0; // 每个线程都有自己的 threadSpecificVar

void threadFunction(int id) {
    threadSpecificVar = id; // 设置线程特有的变量
    std::cout << "Thread " << id << ": threadSpecificVar = " << threadSpecificVar << std::endl;
}

int main() {
    std::thread t1(threadFunction, 1);
    std::thread t2(threadFunction, 2);

    t1.join();
    t2.join();

    return 0;
}
```

**注意事项：**

- **性能**：由于每个线程都有独立的副本，`thread_local` 变量的访问速度可能比全局或静态变量稍慢。
- **静态存储**：`thread_local` 变量的存储类型为静态存储持续时间，因此在程序整个运行期间会一直存在。


## C++ 运算符

运算符是一种告诉编译器执行特定的数学或逻辑操作的符号。C++ 内置了丰富的运算符，并提供了以下类型的运算符：


- 算术运算符

- 关系运算符

- 逻辑运算符

- 位运算符

- 赋值运算符

- 杂项运算符


本章将逐一介绍算术运算符、关系运算符、逻辑运算符、位运算符、赋值运算符和其他运算符。


算术运算符

下表显示了 C++ 支持的算术运算符。

假设变量 A 的值为 10，变量 B 的值为 20，则：

| 运算符 | 描述 | 实例 |
| --- | --- | --- |
| + | 把两个操作数相加 | A + B 将得到 30 |
| - | 从第一个操作数中减去第二个操作数 | A - B 将得到 -10 |
| * | 把两个操作数相乘 | A * B 将得到 200 |
| / | 分子除以分母 | B / A 将得到 2 |
| % | 取模运算符，整除后的余数 | B % A 将得到 0 |
| ++ | 自增运算符，整数值增加 1 | A++ 将得到 11 |
| -- | 自减运算符，整数值减少 1 | A-- 将得到 9 |


实例

请看下面的实例，了解 C++ 中可用的算术运算符。

复制并粘贴下面的 C++ 程序到 test.cpp 文件中，编译并运行程序。


### 实例



```cpp
#include
using namespace std;

int main()
{
   int a = 21;
   int b = 10;
   int c;

   c = a + b;
   cout 关系运算符

下表显示了 C++ 支持的关系运算符。

假设变量 A 的值为 10，变量 B 的值为 20，则：

| 运算符 | 描述 | 实例 |
| --- | --- | --- |
| == | 检查两个操作数的值是否相等，如果相等则条件为真。 | (A == B) 不为真。 |
| != | 检查两个操作数的值是否相等，如果不相等则条件为真。 | (A != B) 为真。 |
| > | 检查左操作数的值是否大于右操作数的值，如果是则条件为真。 | (A > B) 不为真。 |
| = | 检查左操作数的值是否大于或等于右操作数的值，如果是则条件为真。 | (A >= B) 不为真。 |
| 实例

请看下面的实例，了解 C++ 中可用的关系运算符。

复制并黏贴下面的 C++ 程序到 test.cpp 文件中，编译并运行程序。


### 实例



```cpp
#include
using namespace std;

int main()
{
   int a = 21;
   int b = 10;
   int c ;

   if( a == b )
   {
      cout  b )
   {
      cout = a )
   {
      cout 逻辑运算符

下表显示了 C++ 支持的关系逻辑运算符。

假设变量 A 的值为 1，变量 B 的值为 0，则：

| 运算符 | 描述 | 实例 |
| --- | --- | --- |
| && | 称为逻辑与运算符。如果两个操作数都 true，则条件为 true。 | (A && B) 为 false。 |
| || | 称为逻辑或运算符。如果两个操作数中有任意一个 true，则条件为 true。 | (A || B) 为 true。 |
| ! | 称为逻辑非运算符。用来逆转操作数的逻辑状态，如果条件为 true 则逻辑非运算符将使其为 false。 | !(A && B) 为 true。 |


实例

请看下面的实例，了解 C++ 中可用的逻辑运算符。

复制并黏贴下面的 C++ 程序到 test.cpp 文件中，编译并运行程序。


### 实例



```cpp
#include
using namespace std;

int main()
{
   int a = 5;
   int b = 20;
   int c ;

   if ( a && b )
   {
      cout 位运算符

位运算符作用于位，并逐位执行操作。&、 | 和 ^ 的真值表如下所示：

| p | q | p & q | p | q | p ^ q |
| --- | --- | --- | --- | --- |
| 0 | 0 | 0 | 0 | 0 |
| 0 | 1 | 0 | 1 | 1 |
| 1 | 1 | 1 | 1 | 0 |
| 1 | 0 | 0 | 1 | 1 |



假设如果 A = 60，且 B = 13，现在以二进制格式表示，它们如下所示：

A = 0011 1100

B = 0000 1101

-----------------

A&B = 0000 1100

A|B = 0011 1101

A^B = 0011 0001

~A  = 1100 0011

下表显示了 C++ 支持的位运算符。假设变量 A 的值为 60，变量 B 的值为 13，则：

| 运算符 | 描述 | 实例 |
| --- | --- | --- |
| & | 按位与操作，按二进制位进行"与"运算。运算规则：

```cpp
0&0=0;   
0&1=0;    
1&0=0;     
1&1=1;
``` | (A & B) 将得到 12，即为 0000 1100 |
| | | 按位或运算符，按二进制位进行"或"运算。运算规则：

```cpp
0|0=0;   
0|1=1;   
1|0=1;    
1|1=1;
``` | (A | B) 将得到 61，即为 0011 1101 |
| ^ | 异或运算符，按二进制位进行"异或"运算。运算规则：

```cpp
0^0=0;   
0^1=1;   
1^0=1;  
1^1=0;
``` | (A ^ B) 将得到 49，即为 0011 0001 |
| ~ | 取反运算符，按二进制位进行"取反"运算。运算规则：

```cpp
~1=-2;   
~0=-1;
``` | (~A ) 将得到 -61，即为 1100 0011，一个有符号二进制数的补码形式。 |
| > | 二进制右移运算符。将一个数的各二进制位全部右移若干位，正数左补0，负数左补1，右边丢弃。 | A >> 2 将得到 15，即为 0000 1111 |

实例

请看下面的实例，了解 C++ 中可用的位运算符。

复制并黏贴下面的 C++ 程序到 test.cpp 文件中，编译并运行程序。


### 实例



```cpp
#include
using namespace std;

int main()
{
   unsigned int a = 60;      // 60 = 0011 1100
   unsigned int b = 13;      // 13 = 0000 1101
   int c = 0;

   c = a & b;             // 12 = 0000 1100
   cout > 2;            // 15 = 0000 1111
   cout 赋值运算符

下表列出了 C++ 支持的赋值运算符：

| 运算符 | 描述 | 实例 |
| --- | --- | --- |
| = | 简单的赋值运算符，把右边操作数的值赋给左边操作数 | C = A + B 将把 A + B 的值赋给 C |
| += | 加且赋值运算符，把右边操作数加上左边操作数的结果赋值给左边操作数 | C += A 相当于 C = C + A |
| -= | 减且赋值运算符，把左边操作数减去右边操作数的结果赋值给左边操作数 | C -= A 相当于 C = C - A |
| *= | 乘且赋值运算符，把右边操作数乘以左边操作数的结果赋值给左边操作数 | C *= A 相当于 C = C * A |
| /= | 除且赋值运算符，把左边操作数除以右边操作数的结果赋值给左边操作数 | C /= A 相当于 C = C / A |
| %= | 求模且赋值运算符，求两个操作数的模赋值给左边操作数 | C %= A 相当于 C = C % A |
| >= | 右移且赋值运算符 | C >>= 2 等同于  C = C >> 2 |
| &= | 按位与且赋值运算符 | C &= 2 等同于  C = C & 2 |
| ^= | 按位异或且赋值运算符 | C ^= 2 等同于  C = C ^ 2 |
| |= | 按位或且赋值运算符 | C |= 2 等同于  C = C | 2 |


实例

请看下面的实例，了解 C++ 中可用的赋值运算符。

复制并黏贴下面的 C++ 程序到 test.cpp 文件中，编译并运行程序。


### 实例



```cpp
#include
using namespace std;

int main()
{
   int a = 21;
   int c ;

   c =  a;
   cout >=  2;
   cout >= 运算符实例，c 的值 = : " >= 运算符实例，c 的值 = 11
Line 9 - &= 运算符实例，c 的值 = 2
Line 10 - ^= 运算符实例，c 的值 = 0
Line 11 - |= 运算符实例，c 的值 = 2
```



杂项运算符

下表列出了 C++ 支持的其他一些重要的运算符。

| 运算符 | 描述 |
| --- | --- |
| sizeof | sizeof 运算符返回变量的大小。例如，sizeof(a) 将返回 4，其中 a 是整数。 |
| Condition ? X : Y | 条件运算符。如果 Condition 为真 ? 则值为 X : 否则值为 Y。 |
| , | 逗号运算符会顺序执行一系列运算。整个逗号表达式的值是以逗号分隔的列表中的最后一个表达式的值。 |
| .（点）和  ->（箭头） | 成员运算符用于引用类、结构和共用体的成员。 |
| Cast | 强制转换运算符把一种数据类型转换为另一种数据类型。例如，int(2.2000) 将返回 2。 |
| & | 指针运算符 & 返回变量的地址。例如 &a; 将给出变量的实际地址。 |
| * | 指针运算符 * 指向一个变量。例如，*var; 将指向变量 var。 |



C++ 中的运算符优先级

运算符的优先级确定表达式中项的组合。这会影响到一个表达式如何计算。某些运算符比其他运算符有更高的优先级，例如，乘除运算符具有比加减运算符更高的优先级。

例如 x = 7 + 3 * 2，在这里，x 被赋值为 13，而不是 20，因为运算符 * 具有比 + 更高的优先级，所以首先计算乘法 3*2，然后再加上 7。


下表将按运算符优先级从高到低列出各个运算符，具有较高优先级的运算符出现在表格的上面，具有较低优先级的运算符出现在表格的下面。在表达式中，较高优先级的运算符会优先被计算。

| 类别  | 运算符  | 结合性  |
| --- | --- | --- |
| 后缀  | () [] -> .  ++   - -   | 从左到右  |
| 一元  | +  -   !  ~  ++  - -   (type)*  &  sizeof  | 从右到左  |
| 乘除  | *  /  %  | 从左到右  |
| 加减  | +  -  | 从左到右  |
| 移位  | >  | 从左到右  |
| 关系  |  >=  | 从左到右  |
| 相等  | ==  !=  | 从左到右  |
| 位与 AND  | &  | 从左到右  |
| 位异或 XOR  | ^  | 从左到右  |
| 位或 OR  | |  | 从左到右  |
| 逻辑与 AND  | &&  | 从左到右  |
| 逻辑或 OR  | ||  | 从左到右  |
| 条件  | ?:  | 从右到左  |
| 赋值  | =  +=  -=  *=  /=  %=>>=  实例

请看下面的实例，了解 C++ 中运算符的优先级。

复制并黏贴下面的 C++ 程序到 test.cpp 文件中，编译并运行程序。

对比有括号和没有括号时的区别，这将产生不同的结果。因为 ()、 /、 * 和 + 有不同的优先级，高优先级的操作符将优先计算。


### 实例



```cpp
#include
using namespace std;

int main()
{
   int a = 20;
   int b = 10;
   int c = 15;
   int d = 5;
   int e;

   e = (a + b) * c / d;      // ( 30 * 15 ) / 5
   cout << "(a + b) * c / d 的值是 " << e << endl ;

   e = ((a + b) * c) / d;    // (30 * 15 ) / 5
   cout << "((a + b) * c) / d 的值是 " << e << endl ;

   e = (a + b) * (c / d);   // (30) * (15/5)
   cout << "(a + b) * (c / d) 的值是 " << e << endl ;

   e = a + (b * c) / d;     //  20 + (150/5)
   cout << "a + (b * c) / d 的值是 " << e << endl ;

   return 0;
}
```



当上面的代码被编译和执行时，它会产生以下结果：

```cpp
(a + b) * c / d 的值是 90
((a + b) * c) / d 的值是 90
(a + b) * (c / d) 的值是 90
a + (b * c) / d 的值是 50
```


---

# C++ 流程控制


## C++ 循环

有的时候，可能需要多次执行同一块代码。一般情况下，语句是顺序执行的：函数中的第一个语句先执行，接着是第二个语句，依此类推。

编程语言提供了允许更为复杂的执行路径的多种控制结构。

循环语句允许我们多次执行一个语句或语句组，下面是大多数编程语言中循环语句的一般形式：



循环类型

C++ 编程语言提供了以下几种循环类型。点击链接查看每个类型的细节。

| 循环类型 | 描述 |
| --- | --- |
| while 循环 | 当给定条件为真时，重复语句或语句组。它会在执行循环主体之前测试条件。 |
| for 循环 | 多次执行一个语句序列，简化管理循环变量的代码。 |
| do...while 循环 | 除了它是在循环主体结尾测试条件外，其他与 while 语句类似。 |
| 嵌套循环 | 您可以在 while、for 或 do..while 循环内使用一个或多个循环。 |




循环控制语句

循环控制语句更改执行的正常序列。当执行离开一个范围时，所有在该范围中创建的自动对象都会被销毁。

C++ 提供了下列的控制语句。点击链接查看每个语句的细节。

| 控制语句 | 描述 |
| --- | --- |
| break 语句 | 终止 loop 或 switch 语句，程序流将继续执行紧接着 loop 或 switch 的下一条语句。 |
| continue 语句 | 引起循环跳过主体的剩余部分，立即重新开始测试条件。 |
| goto 语句 | 将控制转移到被标记的语句。但是不建议在程序中使用 goto 语句。 |




无限循环

如果条件永远不为假，则循环将变成无限循环。**for** 循环在传统意义上可用于实现无限循环。由于构成循环的三个表达式中任何一个都不是必需的，您可以将某些条件表达式留空来构成一个无限循环。
 

### 实例



```cpp
#include
using namespace std;

int main ()
{

   for( ; ; )
   {
      printf("This loop will run forever.\n");
   }

   return 0;
}
```



当条件表达式不存在时，它被假设为真。您也可以设置一个初始值和增量表达式，但是一般情况下，C++ 程序员偏向于使用 for(;;) 结构来表示一个无限循环。

**注意：**您可以按 Ctrl + C 键终止一个无限循环。


## C++ 判断

判断结构要求程序员指定一个或多个要评估或测试的条件，以及条件为真时要执行的语句（必需的）和条件为假时要执行的语句（可选的）。

下面是大多数编程语言中典型的判断结构的一般形式：



判断语句

C++ 编程语言提供了以下类型的判断语句。点击链接查看每个语句的细节。

| 语句 | 描述 |
| --- | --- |
| if 语句 | 一个 if 语句 由一个布尔表达式后跟一个或多个语句组成。 |
| if...else 语句 | 一个 if 语句 后可跟一个可选的 else 语句，else 语句在布尔表达式为假时执行。 |
| 嵌套 if 语句 | 您可以在一个 if 或 else if 语句内使用另一个 if 或 else if 语句。 |
| switch 语句 | 一个 switch 语句允许测试一个变量等于多个值时的情况。 |
| 嵌套 switch 语句 | 您可以在一个 switch 语句内使用另一个 switch  语句。 |




? : 运算符

我们已经在前面的章节中讲解了 [**条件运算符 ? :**](/cplusplus/cpp-conditional-operator.html)，可以用来替代 **if...else** 语句。它的一般形式如下：

```cpp
Exp1 ? Exp2 : Exp3;
```



其中，Exp1、Exp2 和 Exp3 是表达式。请注意，冒号的使用和位置。

? 表达式的值是由 Exp1 决定的。如果 Exp1 为真，则计算 Exp2 的值，结果即为整个 ? 表达式的值。如果 Exp1 为假，则计算 Exp3 的值，结果即为整个 ? 表达式的值。


---

# C++ 函数与数据结构


## C++ 函数

函数是一组一起执行一个任务的语句。每个 C++ 程序都至少有一个函数，即主函数 **main()** ，所有简单的程序都可以定义其他额外的函数。

您可以把代码划分到不同的函数中。如何划分代码到不同的函数中是由您来决定的，但在逻辑上，划分通常是根据每个函数执行一个特定的任务来进行的。

函数**声明**告诉编译器函数的名称、返回类型和参数。函数**定义**提供了函数的实际主体。

C++ 标准库提供了大量的程序可以调用的内置函数。例如，函数 **strcat()** 用来连接两个字符串，函数 **memcpy()** 用来复制内存到另一个位置。

函数还有很多叫法，比如方法、子例程或程序，等等。


定义函数

C++ 中的函数定义的一般形式如下：
 

```cpp
return_type function_name( parameter list )
{
   body of the function
}
```



在 C++ 中，函数由一个函数头和一个函数主体组成。下面列出一个函数的所有组成部分：


- **返回类型：**一个函数可以返回一个值。**return_type** 是函数返回的值的数据类型。有些函数执行所需的操作而不返回值，在这种情况下，return_type 是关键字 **void**。

- **函数名称：**这是函数的实际名称。函数名和参数列表一起构成了函数签名。

- **参数：**参数就像是占位符。当函数被调用时，您向参数传递一个值，这个值被称为实际参数。参数列表包括函数参数的类型、顺序、数量。参数是可选的，也就是说，函数可能不包含参数。

- **函数主体：**函数主体包含一组定义函数执行任务的语句。


实例

以下是 **max()** 函数的源代码。该函数有两个参数 num1 和 num2，会返回这两个数中较大的那个数：
 

```cpp
// 函数返回两个数中较大的那个数

int max(int num1, int num2)
{
   // 局部变量声明
   int result;

   if (num1 > num2)
      result = num1;
   else
      result = num2;

   return result;
}
```



函数声明

函数**声明**会告诉编译器函数名称及如何调用函数。函数的实际主体可以单独定义。

函数声明包括以下几个部分：

```cpp
return_type function_name( parameter list );
```



针对上面定义的函数 max()，以下是函数声明：

```cpp
int max(int num1, int num2);
```



在函数声明中，参数的名称并不重要，只有参数的类型是必需的，因此下面也是有效的声明：

```cpp
int max(int, int);
```



当您在一个源文件中定义函数且在另一个文件中调用函数时，函数声明是必需的。在这种情况下，您应该在调用函数的文件顶部声明函数。

调用函数

创建 C++ 函数时，会定义函数做什么，然后通过调用函数来完成已定义的任务。

当程序调用函数时，程序控制权会转移给被调用的函数。被调用的函数执行已定义的任务，当函数的返回语句被执行时，或到达函数的结束括号时，会把程序控制权交还给主程序。

调用函数时，传递所需参数，如果函数返回一个值，则可以存储返回值。例如：
 

### 实例



```cpp
#include
using namespace std;

// 函数声明
int max(int num1, int num2);

int main ()
{
   // 局部变量声明
   int a = 100;
   int b = 200;
   int ret;

   // 调用函数来获取最大值
   ret = max(a, b);

   cout  num2)
      result = num1;
   else
      result = num2;

   return result;
}
```



把 max() 函数和 main() 函数放一块，编译源代码。当运行最后的可执行文件时，会产生下列结果：

```cpp
Max value is : 200
```



函数参数

如果函数要使用参数，则必须声明接受参数值的变量。这些变量称为函数的**形式参数**。

形式参数就像函数内的其他局部变量，在进入函数时被创建，退出函数时被销毁。

当调用函数时，有三种向函数传递参数的方式：

| 调用类型 | 描述 |
| --- | --- |
| 传值调用 | 该方法把参数的实际值赋值给函数的形式参数。在这种情况下，修改函数内的形式参数对实际参数没有影响。 |
| 指针调用 | 该方法把参数的地址赋值给形式参数。在函数内，该地址用于访问调用中要用到的实际参数。这意味着，修改形式参数会影响实际参数。 |
| 引用调用 | 该方法把参数的引用赋值给形式参数。在函数内，该引用用于访问调用中要用到的实际参数。这意味着，修改形式参数会影响实际参数。 |



默认情况下，C++ 使用**传值调用**来传递参数。一般来说，这意味着函数内的代码不能改变用于调用函数的参数。之前提到的实例，调用 max() 函数时，使用了相同的方法。

参数的默认值

当您定义一个函数，您可以为参数列表中后边的每一个参数指定默认值。当调用函数时，如果实际参数的值留空，则使用这个默认值。

这是通过在函数定义中使用赋值运算符来为参数赋值的。调用函数时，如果未传递参数的值，则会使用默认值，如果指定了值，则会忽略默认值，使用传递的值。请看下面的实例：
 

### 实例



```cpp
#include
using namespace std;

int sum(int a, int b=20)
{
  int result;

  result = a + b;

  return (result);
}

int main ()
{
   // 局部变量声明
   int a = 100;
   int b = 200;
   int result;

   // 调用函数来添加值
   result = sum(a, b);
   cout 
Lambda 函数与表达式

C++11 提供了对匿名函数的支持,称为 Lambda 函数(也叫 Lambda 表达式)。 

Lambda 表达式把函数看作对象。Lambda 表达式可以像对象一样使用，比如可以将它们赋给变量和作为参数传递，还可以像函数一样对其求值。

Lambda 表达式本质上与函数声明非常类似。Lambda 表达式具体形式如下:

```cpp
[capture](parameters)->return-type{body}
```




例如：

```cpp
[](int x, int y){ return x  int { int z = x + y; return z + x; }
```



本例中，一个临时的参数 z 被创建用来存储中间结果。如同一般的函数，z 的值不会保留到下一次该不具名函数再次被调用时。


如果 lambda 函数没有传回值（例如 void），其返回类型可被完全忽略。



在Lambda表达式内可以访问当前作用域的变量，这是Lambda表达式的闭包（Closure）行为。 与JavaScript闭包不同，C++变量传递有传值和传引用的区别。可以通过前面的[]来指定：

```cpp
[]      // 沒有定义任何变量。使用未定义变量会引发错误。
[x, &y] // x以传值方式传入（默认），y以引用方式传入。
[&]     // 任何被使用到的外部变量都隐式地以引用方式加以引用。
[=]     // 任何被使用到的外部变量都隐式地以传值方式加以引用。
[&, x]  // x显式地以传值方式加以引用。其余变量以引用方式加以引用。
[=, &z] // z显式地以引用方式加以引用。其余变量以传值方式加以引用。
```



另外有一点需要注意。对于[=]或[&]的形式，lambda 表达式可以直接使用 this 指针。但是，对于[]的形式，如果要使用 this 指针，必须显式传入：

```cpp
[this]() { this->someFunc(); }();
```


## C++ 数字

通常，当我们需要用到数字时，我们会使用原始的数据类型，如 int、short、long、float 和 double 等等。这些用于数字的数据类型，其可能的值和数值范围，我们已经在 C++ 数据类型一章中讨论过。

C++ 定义数字

我们已经在之前章节的各种实例中定义过数字。下面是一个 C++ 中定义各种类型数字的综合实例：
 

### 实例



```cpp
#include
using namespace std;

int main ()
{
   // 数字定义
   short  s;
   int    i;
   long   l;
   float  f;
   double d;

   // 数字赋值
   s = 10;
   i = 1000;
   l = 1000000;
   f = 230.47;
   d = 30949.374;

   // 数字输出
   cout C++ 数学运算

在 C++ 中，除了可以创建各种函数，还包含了各种有用的函数供您使用。这些函数写在标准 C 和 C++ 库中，叫做**内置**函数。您可以在程序中引用这些函数。

C++ 内置了丰富的数学函数，可对各种数字进行运算。下表列出了 C++ 中一些有用的内置的数学函数。

为了利用这些函数，您需要引用数学头文件 **<cmath>**。

| 序号 | 函数 & 描述 |
| --- | --- |
| 1 | double cos(double);该函数返回弧度角（double 型）的余弦。 |
| 2 | double sin(double);该函数返回弧度角（double 型）的正弦。 |
| 3 | double tan(double);该函数返回弧度角（double 型）的正切。 |
| 4 | double log(double);该函数返回参数的自然对数。 |
| 5 | double pow(double, double);假设第一个参数为 x，第二个参数为 y，则该函数返回 x 的 y 次方。 |
| 6 | double hypot(double, double);该函数返回两个参数的平方总和的平方根，也就是说，参数为一个直角三角形的两个直角边，函数会返回斜边的长度。 |
| 7 | double sqrt(double);该函数返回参数的平方根。 |
| 8 | int abs(int);该函数返回整数的绝对值。 |
| 9 | double fabs(double);该函数返回任意一个浮点数的绝对值。 |
| 10 | double floor(double);该函数返回一个小于或等于传入参数的最大整数。 |



下面是一个关于数学运算的简单实例：
 

### 实例



```cpp
#include
#include
using namespace std;

int main ()
{
   // 数字定义
   short  s = 10;
   int    i = -1000;
   long   l = 100000;
   float  f = 230.47;
   double d = 200.374;

   // 数学运算
   cout C++ 随机数

在许多情况下，需要生成随机数。关于随机数生成器，有两个相关的函数。一个是 **rand()**，该函数只返回一个伪随机数。生成随机数之前必须先调用 **srand()** 函数。

下面是一个关于生成随机数的简单实例。实例中使用了 **time()** 函数来获取系统时间的秒数，通过调用 rand() 函数来生成随机数：
 

### 实例



```cpp
#include
#include
#include

using namespace std;

int main ()
{
   int i,j;

   // 设置种子
   srand( (unsigned)time( NULL ) );

   /* 生成 10 个随机数 */
   for( i = 0; i 
 C++ 数学常数

在 C++ 中，数学常数（如 π、e、黄金比例等）是许多算法和应用中不可或缺的部分，虽然早期版本的 C++ 中没有直接提供这些常数，但从 C++20 开始，标准库引入了几个常用的数学常数，并提供了更高效和统一的方式来访问它们。


更多内容参考：C++ 标准库 。

π
- 常量：`std::numbers::pi`
- 类型：`std::float32_t`（32位浮动）、`std::float64_t`（64位浮动）


### 实例


```cpp
#include

#include

int main() {

    std::cout 自然对数的底数 e (Euler's Number)
- 常量：`std::numbers::e`
- 类型：`std::float32_t`、`std::float64_t`

```cpp
std::cout 黄金比例 φ (Golden Ratio)

- 常量：`std::numbers::phi`
- 类型：`std::float32_t`、`std::float64_t`


```cpp
std::cout

#include

#include

int main() {

    std::cout << "pi: " << std::numbers::pi << std::endl;

    std::cout << "e: " << std::numbers::e << std::endl;

    std::cout << "phi: " << std::numbers::phi << std::endl;

    return 0;

}
```


输出结果为：

```cpp
pi: 3.14159
e: 2.71828
phi: 1.61803
```


## C++ 数组

C++ 支持**数组**数据结构，它可以存储一个固定大小的相同类型元素的顺序集合。数组是用来存储一系列数据，但它往往被认为是一系列相同类型的变量。

数组的声明并不是声明一个个单独的变量，比如 number0、number1、...、number99，而是声明一个数组变量，比如 numbers，然后使用 numbers[0]、numbers[1]、...、numbers[99] 来代表一个个单独的变量。数组中的特定元素可以通过索引访问。

所有的数组都是由连续的内存位置组成。最低的地址对应第一个元素，最高的地址对应最后一个元素。


声明数组

在 C++ 中要声明一个数组，需要指定元素的类型和元素的数量，如下所示：

```cpp
type arrayName [ arraySize ];
```



这叫做一维数组。**arraySize** 必须是一个大于零的整数常量，**type** 可以是任意有效的 C++ 数据类型。例如，要声明一个类型为 double 的包含 10 个元素的数组 **balance**，声明语句如下：

```cpp
double balance[10];
```



现在 *balance* 是一个可用的数组，可以容纳 10 个类型为 double 的数字。

初始化数组

在 C++ 中，您可以逐个初始化数组，也可以使用一个初始化语句，如下所示：

```cpp
double balance[5] = {1000.0, 2.0, 3.4, 7.0, 50.0};
```



大括号 { } 之间的值的数目不能大于我们在数组声明时在方括号 [ ] 中指定的元素数目。

如果您省略掉了数组的大小，数组的大小则为初始化时元素的个数。因此，如果：

```cpp
double balance[] = {1000.0, 2.0, 3.4, 7.0, 50.0};
```



您将创建一个数组，它与前一个实例中所创建的数组是完全相同的。下面是一个为数组中某个元素赋值的实例：

```cpp
balance[4] = 50.0;
```



上述的语句把数组中第五个元素的值赋为 50.0。所有的数组都是以 0 作为它们第一个元素的索引，也被称为基索引，数组的最后一个索引是数组的总大小减去 1。以下是上面所讨论的数组的的图形表示：




访问数组元素

数组元素可以通过数组名称加索引进行访问。元素的索引是放在方括号内，跟在数组名称的后边。例如：

```cpp
double salary = balance[9];
```



上面的语句将把数组中第 10 个元素的值赋给 salary 变量。下面的实例使用了上述的三个概念，即，声明数组、数组赋值、访问数组：

 

### 实例



```cpp
#include
using namespace std;

#include
using std::setw;

int main ()
{
   int n[ 10 ]; // n 是一个包含 10 个整数的数组

   // 初始化数组元素
   for ( int i = 0; i C++ 中数组详解

在 C++ 中，数组是非常重要的，我们需要了解更多有关数组的细节。下面列出了 C++ 程序员必须清楚的一些与数组相关的重要概念：

| 概念 | 描述 |
| --- | --- |
| 多维数组 | C++ 支持多维数组。多维数组最简单的形式是二维数组。 |
| 指向数组的指针 | 您可以通过指定不带索引的数组名称来生成一个指向数组中第一个元素的指针。 |
| 传递数组给函数 | 您可以通过指定不带索引的数组名称来给函数传递一个指向数组的指针。 |
| 从函数返回数组 | C++ 允许从函数返回数组。 |


## C++ 字符串

C++ 提供了以下两种类型的字符串表示形式：


- C 风格字符串

- C++ 引入的 string 类类型



C 风格字符串

C 风格的字符串起源于 C 语言，并在 C++ 中继续得到支持。字符串实际上是使用 **null** 字符  \0  终止的一维字符数组。因此，一个以 null 结尾的字符串，包含了组成字符串的字符。

下面的声明和初始化创建了一个 **RUNOOB** 字符串。由于在数组的末尾存储了空字符，所以字符数组的大小比单词 **RUNOOB** 的字符数多一个。

```cpp
char site[7] = {'R', 'U', 'N', 'O', 'O', 'B', '\0'};
```



依据数组初始化规则，您可以把上面的语句写成以下语句：

```cpp
char site[] = "RUNOOB";
```



以下是 C/C++ 中定义的字符串的内存表示：


其实，您不需要把 **null** 字符放在字符串常量的末尾。C++ 编译器会在初始化数组时，自动把 \0 放在字符串的末尾。让我们尝试输出上面的字符串：



### 实例



```cpp
#include

using namespace std;

int main ()
{
   char site[7] = {'R', 'U', 'N', 'O', 'O', 'B', '\0'};

   cout s2 则返回值大于 0。 |
| 5 | strchr(s1, ch);返回一个指针，指向字符串 s1 中字符 ch 的第一次出现的位置。 |
| 6 | strstr(s1, s2);返回一个指针，指向字符串 s1 中字符串 s2 的第一次出现的位置。 |



下面的实例使用了上述的一些函数：



### 实例



```cpp
#include
#include

using namespace std;

int main ()
{
   char str1[13] = "runoob";
   char str2[13] = "google";
   char str3[13];
   int  len ;

   // 复制 str1 到 str3
   strcpy( str3, str1);
   cout C++ 中的 String 类

C++ 标准库提供了 **string** 类类型，支持上述所有的操作，另外还增加了其他更多的功能。我们将学习 C++ 标准库中的这个类，现在让我们先来看看下面这个实例：

现在您可能还无法透彻地理解这个实例，因为到目前为止我们还没有讨论类和对象。所以现在您可以只是粗略地看下这个实例，等理解了面向对象的概念之后再回头来理解这个实例。 


### 实例



```cpp
#include
#include

using namespace std;

int main ()
{
   string str1 = "runoob";
   string str2 = "google";
   string str3;
   int  len ;

   // 复制 str1 到 str3
   str3 = str1;
   cout << "str3 : " << str3 << endl;

   // 连接 str1 和 str2
   str3 = str1 + str2;
   cout << "str1 + str2 : " << str3 << endl;

   // 连接后，str3 的总长度
   len = str3.size();
   cout << "str3.size() :  " << len << endl;

   return 0;
}
```



当上面的代码被编译和执行时，它会产生下列结果：

```cpp
str3 : runoob
str1 + str2 : runoobgoogle
str3.size() :  12
```


## C++ 指针

学习 C++ 的指针既简单又有趣。通过指针，可以简化一些 C++ 编程任务的执行，还有一些任务，如动态内存分配，没有指针是无法执行的。所以，想要成为一名优秀的 C++ 程序员，学习指针是很有必要的。

正如您所知道的，每一个变量都有一个内存位置，每一个内存位置都定义了可使用连字号（&）运算符访问的地址，它表示了在内存中的一个地址。请看下面的实例，它将输出定义的变量地址：
 

### 实例



```cpp
#include

using namespace std;

int main ()
{
   int  var1;
   char var2[10];

   cout 什么是指针？

**指针**是一个变量，其值为另一个变量的地址，即，内存位置的直接地址。就像其他变量或常量一样，您必须在使用指针存储其他变量地址之前，对其进行声明。指针变量声明的一般形式为：

```cpp
type *var-name;
```



在这里，**type** 是指针的基类型，它必须是一个有效的 C++ 数据类型，**var-name** 是指针变量的名称。用来声明指针的星号 * 与乘法中使用的星号是相同的。但是，在这个语句中，星号是用来指定一个变量是指针。以下是有效的指针声明：

```cpp
int    *ip;    /* 一个整型的指针 */
double *dp;    /* 一个 double 型的指针 */
float  *fp;    /* 一个浮点型的指针 */
char   *ch;    /* 一个字符型的指针 */
```



所有指针的值的实际数据类型，不管是整型、浮点型、字符型，还是其他的数据类型，都是一样的，都是一个代表内存地址的长的十六进制数。不同数据类型的指针之间唯一的不同是，指针所指向的变量或常量的数据类型不同。

C++ 中使用指针

使用指针时会频繁进行以下几个操作：定义一个指针变量、把变量地址赋值给指针、访问指针变量中可用地址的值。这些是通过使用一元运算符 ***** 来返回位于操作数所指定地址的变量的值。下面的实例涉及到了这些操作：
 

### 实例



```cpp
#include

using namespace std;

int main ()
{
   int  var = 20;   // 实际变量的声明
   int  *ip;        // 指针变量的声明

   ip = &var;       // 在指针变量中存储 var 的地址

   cout C++ 指针详解

在 C++ 中，有很多指针相关的概念，这些概念都很简单，但是都很重要。下面列出了 C++ 程序员必须清楚的一些与指针相关的重要概念：

| 概念 | 描述 |
| --- | --- |
| C++ Null 指针 | C++ 支持空指针。NULL 指针是一个定义在标准库中的值为零的常量。 |
| C++ 指针的算术运算 | 可以对指针进行四种算术运算：++、--、+、- |
| C++ 指针 vs 数组 | 指针和数组之间有着密切的关系。 |
| C++ 指针数组 | 可以定义用来存储指针的数组。 |
| C++ 指向指针的指针 | C++ 允许指向指针的指针。 |
| C++ 传递指针给函数 | 通过引用或地址传递参数，使传递的参数在调用函数中被改变。 |
| C++ 从函数返回指针 | C++ 允许函数返回指针到局部变量、静态变量和动态内存分配。 |


## C++ 引用

引用变量是一个别名，也就是说，它是某个已存在变量的另一个名字。

一旦把引用初始化为某个变量，就可以使用该引用名称或变量名称来指向变量。

引用必须在定义时初始化，并且一旦绑定到一个变量后，就不能再绑定到其他变量。

引用的语法如下：


```cpp
int a = 10;
int &ref = a;  // ref 是 a 的引用
```



-

`int &ref` 表示 `ref` 是一个 `int` 类型的引用。
-

`ref` 是 `a` 的别名，对 `ref` 的操作会直接作用于 `a`。
C++ 引用 vs 指针

引用很容易与指针混淆，它们之间有三个主要的不同：


- 不存在空引用，引用必须连接到一块合法的内存。

- 一旦引用被初始化为一个对象，就不能被指向到另一个对象。指针可以在任何时候指向到另一个对象。

- 引用必须在创建时被初始化。指针可以在任何时间被初始化。

- 引用的对象必须是一个变量，而指针必须是一个地址。


| 特性 | 引用 | 指针 |
| --- | --- | --- |
| 定义与初始化 | 必须初始化，且不能为 null。 | 可以不初始化，可以在后续代码中指向其他对象，可以为 null。 |
| 语法 | 使用 & 声明，例如：int &ref = a; | 使用 * 声明，例如：int *ptr = &a; |
| 重新绑定 | 不能重新绑定，一旦初始化后始终引用同一个对象。 | 可以重新指向其他对象，例如：ptr = &b; |
| 空值（Nullability） | 不能为 null，必须绑定到有效的对象。 | 可以为 null，表示不指向任何对象。 |
| 内存占用 | 不占用额外内存（编译器通常将其优化为直接操作所引用的对象）。 | 占用额外内存（存储地址，通常是一个机器字长，如4字节或8字节）。 |
| 访问方式 | 直接使用，无需解引用操作符，例如：ref = 10; | 需要使用 * 解引用操作符访问或修改所指向的对象，例如：*ptr = 10; |
| 多级间接访问 | 不支持多级间接访问（不能有引用的引用）。 | 支持多级间接访问（如指针的指针：int **pptr;）。 |
| 函数参数传递 | 常用于函数参数传递，语法简洁，例如：void func(int &x) { x = 10; } | 也可以用于函数参数传递，但需要使用解引用操作符，例如：void func(int *x) { *x = 10; } |
| 数组与引用 | 不能直接创建引用数组，但可以创建数组的引用，例如：int (&ref)[10] = arr; | 可以创建指针数组，也可以创建指向数组的指针，例如：int *ptrArr[10]; |
| 安全性 | 更安全，不能为 null，且语法更直观。 | 更灵活，但容易出错（如空指针、野指针等）。 |
| 底层实现 | 通常通过指针实现，但编译器会优化为直接操作所引用的对象。 | 直接存储目标对象的内存地址。 |


C++ 中创建引用

试想变量名称是变量附属在内存位置中的标签，您可以把引用当成是变量附属在内存位置中的第二个标签。因此，您可以通过原始变量名称或引用来访问变量的内容。例如：

```cpp
int i = 17;
```



我们可以为 i 声明引用变量，如下所示：

```cpp
int&  r = i;
double& s = d;
```



在这些声明中，& 读作**引用**。


因此，第一个声明可以读作 **"r 是一个初始化为 i 的整型引用"**，第二个声明可以读作 **"s 是一个初始化为 d 的 double 型引用"**。

下面的实例使用了 int 和 double 引用：
 

### 实例



```cpp
#include

using namespace std;

int main ()
{
   // 声明简单的变量
   int    i;
   double d;

   // 声明引用变量
   int&    r = i;
   double& s = d;

   i = 5;
   cout << "Value of i : " << i << endl;
   cout << "Value of i reference : " << r  << endl;

   d = 11.7;
   cout << "Value of d : " << d << endl;
   cout << "Value of d reference : " << s  << endl;

   return 0;
}
```



当上面的代码被编译和执行时，它会产生下列结果：

```cpp
Value of i : 5
Value of i reference : 5
Value of d : 11.7
Value of d reference : 11.7
```



引用通常用于函数参数列表和函数返回值。下面列出了 C++ 程序员必须清楚的两个与 C++ 引用相关的重要概念：

| 概念 | 描述 |
| --- | --- |
| 把引用作为参数 | C++ 支持把引用作为参数传给函数，这比传一般的参数更安全。 |
| 把引用作为返回值 | 可以从 C++ 函数中返回引用，就像返回其他数据类型一样。 |


## C++ 日期 & 时间

C++ 标准库没有提供所谓的日期类型。C++ 继承了 C 语言用于日期和时间操作的结构和函数。为了使用日期和时间相关的函数和结构，需要在 C++ 程序中引用 <ctime> 头文件。

有四个与时间相关的类型：**clock_t、time_t、size_t** 和 **tm**。类型 clock_t、size_t 和 time_t 能够把系统时间和日期表示为某种整数。

结构类型 **tm** 把日期和时间以 C 结构的形式保存，tm 结构的定义如下：
 

```cpp
struct tm {
  int tm_sec;   // 秒，正常范围从 0 到 59，但允许至 61
  int tm_min;   // 分，范围从 0 到 59
  int tm_hour;  // 小时，范围从 0 到 23
  int tm_mday;  // 一月中的第几天，范围从 1 到 31
  int tm_mon;   // 月，范围从 0 到 11
  int tm_year;  // 自 1900 年起的年数
  int tm_wday;  // 一周中的第几天，范围从 0 到 6，从星期日算起
  int tm_yday;  // 一年中的第几天，范围从 0 到 365，从 1 月 1 日算起
  int tm_isdst; // 夏令时
};
```




下面是 C/C++ 中关于日期和时间的重要函数。所有这些函数都是 C/C++ 标准库的组成部分，您可以在 C++ 标准库中查看一下各个函数的细节。

| 序号 | 函数 & 描述 |
| --- | --- |
| 1 | time_t time(time_t *time);该函数返回系统的当前日历时间，自 1970 年 1 月 1 日以来经过的秒数。如果系统没有时间，则返回 -1。 |
| 2 | char *ctime(const time_t *time);返回一个指向字符串的指针，字符串内容表示本地时间，格式为：


```cpp
Www Mmm dd hh:mm:ss yyyy\n\0
```


其中：

    Www：星期（如 Tue）
    Mmm：月份（如 Jul）
    dd：日（如 29）
    hh:mm:ss：时间（24 小时制）
    yyyy：年份（如 2025）
    最后包含换行符 \n 和结束符 \0

示例返回值：

```cpp
"Tue Jul 29 19:12:15 2025\n\0"
``` |
| 3 | struct tm *localtime(const time_t *time);该函数返回一个指向表示本地时间的 tm 结构的指针。 |
| 4 | clock_t clock(void);该函数返回程序执行起（一般为程序的开头），处理器时钟所使用的时间。如果时间不可用，则返回 -1。 |
| 5 | char * asctime ( const struct tm * time );该函数返回一个指向字符串的指针，字符串包含了 time 所指向结构中存储的信息，返回形式为：day month date hours:minutes:seconds year\n\0。 |
| 6 | struct tm *gmtime(const time_t *time);该函数返回一个指向 time 的指针，time 为 tm 结构，用协调世界时（UTC）也被称为格林尼治标准时间（GMT）表示。 |
| 7 | time_t mktime(struct tm *time);该函数返回日历时间，相当于 time 所指向结构中存储的时间。 |
| 8 | double difftime ( time_t time2, time_t time1 );该函数返回 time1 和 time2 之间相差的秒数。 |
| 9 | size_t strftime();该函数可用于格式化日期和时间为指定的格式。 |



当前日期和时间

下面的实例获取当前系统的日期和时间，包括本地时间和协调世界时（UTC）。
 

### 实例



```cpp
#include
#include

using namespace std;

int main( )
{
   // 基于当前系统的当前日期/时间
   time_t now = time(0);

   // 把 now 转换为字符串形式
   char* dt = ctime(&now);

   cout 使用结构 tm 格式化时间

**tm** 结构在 C/C++ 中处理日期和时间相关的操作时，显得尤为重要。tm 结构以 C 结构的形式保存日期和时间。大多数与时间相关的函数都使用了 tm 结构。下面的实例使用了 tm 结构和各种与日期和时间相关的函数。

在练习使用结构之前，需要对 C 结构有基本的了解，并懂得如何使用箭头 -> 运算符来访问结构成员。
 

### 实例



```cpp
#include
#include

using namespace std;

int main( )
{
   // 基于当前系统的当前日期/时间
   time_t now = time(0);

   cout tm_year tm_montm_mday tm_hour tm_min tm_sec << endl;
}
```



当上面的代码被编译和执行时，它会产生下列结果：

```cpp
1970 到目前时间:1503564157
年: 2017
月: 8
日: 24
时间: 16:42:37
```


## C++ 基本的输入输出

C++ 标准库提供了一组丰富的输入/输出功能，我们将在后续的章节进行介绍。本章将讨论 C++ 编程中最基本和最常见的 I/O 操作。

C++ 的 I/O 发生在流中，流是字节序列。如果字节流是从设备（如键盘、磁盘驱动器、网络连接等）流向内存，这叫做**输入操作**。如果字节流是从内存流向设备（如显示屏、打印机、磁盘驱动器、网络连接等），这叫做**输出操作**。


I/O 库头文件

下列的头文件在 C++ 编程中很重要。

| 头文件 | 函数和描述 |
| --- | --- |
|  | 该文件定义了 cin、cout、cerr 和 clog 对象，分别对应于标准输入流、标准输出流、非缓冲标准错误流和缓冲标准错误流。 |
|  | 该文件通过所谓的参数化的流操纵器（比如 setw 和 setprecision），来声明对执行标准化 I/O 有用的服务。 |
|  | 该文件为用户控制的文件处理声明服务。我们将在文件和流的相关章节讨论它的细节。 |



标准输出流（cout）

预定义的对象 **cout** 是 **iostream** 类的一个实例。cout 对象"连接"到标准输出设备，通常是显示屏。**cout** 是与流插入运算符 << 结合使用的，如下所示：
 

### 实例



```cpp
#include

using namespace std;

int main( )
{
   char str[] = "Hello C++";

   cout 标准输入流（cin）

预定义的对象 **cin** 是 **iostream** 类的一个实例。cin 对象附属到标准输入设备，通常是键盘。**cin** 是与流提取运算符 >> 结合使用的，如下所示：
 

### 实例



```cpp
#include

using namespace std;

int main( )
{
   char name[50];

   cout > name;
   cout > name >> age;
```



这相当于下面两个语句：

```cpp
cin >> name;
cin >> age;
```



标准错误流（cerr）

预定义的对象 **cerr** 是 **iostream** 类的一个实例。cerr 对象附属到标准输出设备，通常也是显示屏，但是 **cerr** 对象是非缓冲的，且每个流插入到 cerr 都会立即输出。

**cerr** 也是与流插入运算符 << 结合使用的，如下所示：
 

### 实例



```cpp
#include

using namespace std;

int main( )
{
   char str[] = "Unable to read....";

   cerr 标准日志流（clog）

预定义的对象 **clog** 是 **iostream** 类的一个实例。clog 对象附属到标准输出设备，通常也是显示屏，但是 **clog** 对象是缓冲的。这意味着每个流插入到 clog 都会先存储在缓冲区，直到缓冲填满或者缓冲区刷新时才会输出。

**clog** 也是与流插入运算符 << 结合使用的，如下所示：
 

### 实例



```cpp
#include

using namespace std;

int main( )
{
   char str[] = "Unable to read....";

   clog << "Error message : " << str << endl;
}
```



当上面的代码被编译和执行时，它会产生下列结果：

```cpp
Error message : Unable to read....
```



通过这些小实例，我们无法区分 cout、cerr 和 clog 的差异，但在编写和执行大型程序时，它们之间的差异就变得非常明显。所以良好的编程实践告诉我们，使用 cerr 流来显示错误消息，而其他的日志消息则使用 clog 流来输出。


## C++ 结构体(struct)

C/C++ 数组允许定义可存储相同类型数据项的变量，但是**结构**是 C++ 中另一种用户自定义的可用的数据类型，它允许您存储不同类型的数据项。

结构用于表示一条记录，假设您想要跟踪图书馆中书本的动态，您可能需要跟踪每本书的下列属性：


- Title ：标题

- Author ：作者 

- Subject ：类目 

- Book ID ：书的 ID



定义结构

在 C++ 中，struct 语句用于定义结构体（structure）。

结构体是一种用户自定义的数据类型，用于将不同类型的数据组合在一起。与类（class）类似，结构体允许你定义成员变量和成员函数。

为了定义结构，您必须使用 **struct** 语句。struct 语句定义了一个包含多个成员的新的数据类型，struct 语句的格式如下：


```cpp
struct type_name {
member_type1 member_name1;
member_type2 member_name2;
member_type3 member_name3;
.
.
} object_names;
```



**type_name** 是结构体类型的名称，**member_type1 member_name1** 是标准的变量定义，比如 **int i;** 或者 **float f;** 或者其他有效的变量定义。在结构定义的末尾，最后一个分号之前，您可以指定一个或多个结构变量，这是可选的。下面是声明一个结构体类型 **Books**，变量为 **book**：


```cpp
struct Books
{
   char  title[50];
   char  author[50];
   char  subject[100];
   int   book_id;
} book;
```

**结构体优点：**

- **简单数据封装**：适合封装多种类型的简单数据，通常用于数据的存储。
- **轻量级**：相比 `class`，结构体语法更简洁，适合小型数据对象。
- **面向对象支持**：支持构造函数、成员函数和访问权限控制，可以实现面向对象的设计。
访问结构成员

为了访问结构的成员，我们使用**成员访问运算符（.）**。成员访问运算符是结构变量名称和我们要访问的结构成员之间的一个句号。

下面的实例演示了结构的用法：


### 实例



```cpp
#include
#include

using namespace std;

// 声明一个结构体类型 Books
struct Books
{
   char  title[50];
   char  author[50];
   char  subject[100];
   int   book_id;
};

int main( )
{
   Books Book1;        // 定义结构体类型 Books 的变量 Book1
   Books Book2;        // 定义结构体类型 Books 的变量 Book2

   // Book1 详述
   strcpy( Book1.title, "C++ 教程");
   strcpy( Book1.author, "Runoob");
   strcpy( Book1.subject, "编程语言");
   Book1.book_id = 12345;

   // Book2 详述
   strcpy( Book2.title, "CSS 教程");
   strcpy( Book2.author, "Runoob");
   strcpy( Book2.subject, "前端技术");
   Book2.book_id = 12346;

   // 输出 Book1 信息
   cout 结构作为函数参数

您可以把结构作为函数参数，传参方式与其他类型的变量或指针类似。您可以使用上面实例中的方式来访问结构变量：


### 实例



```cpp
#include
#include

using namespace std;
void printBook( struct Books book );

// 声明一个结构体类型 Books
struct Books
{
   char  title[50];
   char  author[50];
   char  subject[100];
   int   book_id;
};

int main( )
{
   Books Book1;        // 定义结构体类型 Books 的变量 Book1
   Books Book2;        // 定义结构体类型 Books 的变量 Book2

    // Book1 详述
   strcpy( Book1.title, "C++ 教程");
   strcpy( Book1.author, "Runoob");
   strcpy( Book1.subject, "编程语言");
   Book1.book_id = 12345;

   // Book2 详述
   strcpy( Book2.title, "CSS 教程");
   strcpy( Book2.author, "Runoob");
   strcpy( Book2.subject, "前端技术");
   Book2.book_id = 12346;

   // 输出 Book1 信息
   printBook( Book1 );

   // 输出 Book2 信息
   printBook( Book2 );

   return 0;
}
void printBook( struct Books book )
{
   cout 结构体的各个部分详细介绍
	

-

**struct 关键字：**用于定义结构体，它告诉编译器后面要定义的是一个自定义类型。


-

**成员变量：**成员变量是结构体中定义的数据项，它们可以是任何基本类型或其他自定义类型。在 struct 中，这些成员默认是 public，可以直接访问。

- 


**成员函数：**结构体中也可以包含成员函数，这使得结构体在功能上类似于类。成员函数可以操作结构体的成员变量，提供对数据的封装和操作。

- 

**访问权限：**与 class 类似，你可以在 struct 中使用 public、private 和 protected 来定义成员的访问权限。在 struct 中，默认所有成员都是 public，而 class 中默认是 private。




指向结构的指针

您可以定义指向结构的指针，方式与定义指向其他类型变量的指针相似，如下所示：

```cpp
struct Books *struct_pointer;
```


以上代码定义了一个指向 Books 结构体的指针 struct_pointer。

现在，您可以在上述定义的指针变量中存储结构变量的地址。为了查找结构变量的地址，请把 & 运算符放在结构名称的前面，如下所示：

```cpp
struct_pointer = &Book1;
```


以上代码将 Book1 结构体变量的地址赋值给 struct_pointer。


为了使用指向该结构的指针访问结构的成员，您必须使用 -> 运算符，如下所示：

```cpp
struct_pointer->title;
```

以上代码通过 struct_pointer 访问 Book1 结构体的 title 成员。

让我们使用结构指针来重写上面的实例，这将有助于您理解结构指针的概念：


### 实例



```cpp
#include
#include

using namespace std;

// 声明一个结构体类型 Books
struct Books
{
    string title;
    string author;
    string subject;
    int book_id;

    // 构造函数
    Books(string t, string a, string s, int id)
        : title(t), author(a), subject(s), book_id(id) {}
};

// 打印书籍信息的函数，接受一个指向 Books 结构体的指针
void printBookInfo(const Books* book) {
    cout title author subject book_id ` 操作符来访问结构体指针所指向的成员变量。
-

**`main` 函数**：
-

创建了两个 `Books` 类型的对象 `Book1` 和 `Book2`。
-

使用 `&` 操作符获取这两个对象的地址，并将它们赋值给指针 `ptrBook1` 和 `ptrBook2`。
-

调用 `printBookInfo` 函数时，传递的是指向 `Books` 对象的指针。

当上面的代码被编译和执行时，它会产生下列结果：

```cpp
书籍标题: C++ 教程
书籍作者: Runoob
书籍类目: 编程语言
书籍 ID: 12345
书籍标题: CSS 教程
书籍作者: Runoob
书籍类目: 前端技术
书籍 ID: 12346
```



typedef 关键字

下面是一种更简单的定义结构的方式，您可以为创建的类型取一个"别名"。例如：

```cpp
typedef struct Books
{
   char  title[50];
   char  author[50];
   char  subject[100];
   int   book_id;
}Books;
```



现在，您可以直接使用 *Books* 来定义 *Books* 类型的变量，而不需要使用 struct 关键字。下面是实例：

```cpp
Books Book1, Book2;
```



您可以使用 **typedef** 关键字来定义非结构类型，如下所示：

```cpp
typedef long int *pint32;
 
pint32 x, y, z;
```



x, y 和 z 都是指向长整型 long int 的指针。

结构体与类的区别

在 C++ 中，struct 和 class 本质上非常相似，唯一的区别在于默认的访问权限：
- `struct` 默认的成员和继承是 `public`。
- `class` 默认的成员和继承是 `private`。

你可以将 `struct` 当作一种简化形式的 `class`，适合用于没有太多复杂功能的简单数据封装。结构体与函数的结合

你可以通过构造函数初始化结构体，还可以通过引用传递结构体来避免不必要的拷贝。


### 实例


```cpp
struct Books {

    string title;

    string author;

    string subject;

    int book_id;

    // 构造函数

    Books(string t, string a, string s, int id)

        : title(t), author(a), subject(s), book_id(id) {}

    void printInfo() const {

        cout << "书籍标题: " << title << endl;

        cout << "书籍作者: " << author << endl;

        cout << "书籍类目: " << subject << endl;

        cout << "书籍 ID: " << book_id << endl;

    }

};

void printBookByRef(const Books& book) {

    book.printInfo();

}
```


---

# C++ 面向对象


## C++ 类 & 对象

C++ 在 C 语言的基础上增加了面向对象编程，C++ 支持面向对象程序设计。类是 C++ 的核心特性，通常被称为用户定义的类型。

类用于指定对象的形式，是一种用户自定义的数据类型，它是一种封装了数据和函数的组合。类中的数据称为成员变量，函数称为成员函数。类可以被看作是一种模板，可以用来创建具有相同属性和行为的多个对象。


C++ 类定义

定义一个类需要使用关键字 class，然后指定类的名称，并类的主体是包含在一对花括号中，主体包含类的成员变量和成员函数。

定义一个类，本质上是定义一个数据类型的蓝图，它定义了类的对象包括了什么，以及可以在这个对象上执行哪些操作。



以下实例我们使用关键字 **class** 定义 Box 数据类型，包含了三个成员变量 length、breadth 和 height：

 

```cpp
class Box
{
   public:
      double length;   // 盒子的长度
      double breadth;  // 盒子的宽度
      double height;   // 盒子的高度
};
```



关键字 **public** 确定了类成员的访问属性。在类对象作用域内，公共成员在类的外部是可访问的。您也可以指定类的成员为 **private** 或 **protected**，这个我们稍后会进行讲解。

定义 C++ 对象

类提供了对象的蓝图，所以基本上，对象是根据类来创建的。声明类的对象，就像声明基本类型的变量一样。下面的语句声明了类 Box 的两个对象：
 

```cpp
Box Box1;          // 声明 Box1，类型为 Box
Box Box2;          // 声明 Box2，类型为 Box
```



对象 Box1 和 Box2 都有它们各自的数据成员。

访问数据成员

类的对象的公共数据成员可以使用直接成员访问运算符 . 来访问。




为了更好地理解这些概念，让我们尝试一下下面的实例：
 

### 实例



```cpp
#include

using namespace std;

class Box
{
   public:
      double length;   // 长度
      double breadth;  // 宽度
      double height;   // 高度
      // 成员函数声明
      double get(void);
      void set( double len, double bre, double hei );
};
// 成员函数定义
double Box::get(void)
{
    return length * breadth * height;
}

void Box::set( double len, double bre, double hei)
{
    length = len;
    breadth = bre;
    height = hei;
}
int main( )
{
   Box Box1;        // 声明 Box1，类型为 Box
   Box Box2;        // 声明 Box2，类型为 Box
   Box Box3;        // 声明 Box3，类型为 Box
   double volume = 0.0;     // 用于存储体积

   // box 1 详述
   Box1.height = 5.0;
   Box1.length = 6.0;
   Box1.breadth = 7.0;

   // box 2 详述
   Box2.height = 10.0;
   Box2.length = 12.0;
   Box2.breadth = 13.0;

   // box 1 的体积
   volume = Box1.height * Box1.length * Box1.breadth;
   cout 类 & 对象详解

到目前为止，我们已经对 C++ 的类和对象有了基本的了解。下面的列表中还列出了其他一些 C++ 类和对象相关的概念，可以点击相应的链接进行学习。

| 概念 | 描述 |
| --- | --- |
| 类成员函数 | 类的成员函数是指那些把定义和原型写在类定义内部的函数，就像类定义中的其他变量一样。 |
| 类访问修饰符 | 类成员可以被定义为 public、private 或 protected。默认情况下是定义为 private。 |
| 构造函数 & 析构函数 | 类的构造函数是一种特殊的函数，在创建一个新的对象时调用。类的析构函数也是一种特殊的函数，在删除所创建的对象时调用。 |
| C++ 拷贝构造函数 | 拷贝构造函数，是一种特殊的构造函数，它在创建对象时，是使用同一类中之前创建的对象来初始化新创建的对象。 |
| C++ 友元函数 | 友元函数可以访问类的 private 和 protected 成员。 |
| C++ 内联函数 | 通过内联函数，编译器试图在调用函数的地方扩展函数体中的代码。 |
| C++ 中的 this 指针 | 每个对象都有一个特殊的指针 this，它指向对象本身。 |
| C++ 中指向类的指针 | 指向类的指针方式如同指向结构的指针。实际上，类可以看成是一个带有函数的结构。 |
| C++ 类的静态成员 | 类的数据成员和函数成员都可以被声明为静态的。 |


## C++ 继承

面向对象程序设计中最重要的一个概念是继承。继承允许我们依据另一个类来定义一个类，这使得创建和维护一个应用程序变得更容易。这样做，也达到了重用代码功能和提高执行效率的效果。

当创建一个类时，您不需要重新编写新的数据成员和成员函数，只需指定新建的类继承了一个已有的类的成员即可。这个已有的类称为**基类**，新建的类称为**派生类**。

继承代表了 **is a** 关系。例如，哺乳动物是动物，狗是哺乳动物，因此，狗是动物，等等。



代码如下：

```cpp
// 基类

class Animal {

    // eat() 函数

    // sleep() 函数

};

//派生类

class Dog : public Animal {

    // bark() 函数

};
```

基类 & 派生类

一个类可以派生自多个类，这意味着，它可以从多个基类继承数据和函数。定义一个派生类，我们使用一个类派生列表来指定基类。类派生列表以一个或多个基类命名，形式如下：

```cpp
class derived-class: access-specifier base-class
```



其中，访问修饰符 access-specifier 是 **public、protected** 或 **private** 其中的一个，base-class 是之前定义过的某个类的名称。如果未使用访问修饰符 access-specifier，则默认为 private。

假设有一个基类 **Shape**，**Rectangle** 是它的派生类，如下所示：
 

### 实例



```cpp
#include

using namespace std;

// 基类
class Shape
{
   public:
      void setWidth(int w)
      {
         width = w;
      }
      void setHeight(int h)
      {
         height = h;
      }
   protected:
      int width;
      int height;
};

// 派生类
class Rectangle: public Shape
{
   public:
      int getArea()
      {
         return (width * height);
      }
};

int main(void)
{
   Rectangle Rect;

   Rect.setWidth(5);
   Rect.setHeight(7);

   // 输出对象的面积
   cout 访问控制和继承

派生类可以访问基类中所有的非私有成员。因此基类成员如果不想被派生类的成员函数访问，则应在基类中声明为 private。

我们可以根据访问权限总结出不同的访问类型，如下所示：

| 访问 | public | protected | private |
| --- | --- | --- | --- |
| 同一个类 | yes | yes | yes |
| 派生类 | yes | yes | no |
| 外部的类 | yes | no | no |



一个派生类继承了所有的基类方法，但下列情况除外：


- 基类的构造函数、析构函数和拷贝构造函数。

- 基类的重载运算符。

- 基类的友元函数。


继承类型

当一个类派生自基类，该基类可以被继承为 **public、protected** 或 ** private** 几种类型。继承类型是通过上面讲解的访问修饰符 access-specifier 来指定的。

我们几乎不使用 **protected** 或 ** private** 继承，通常使用 **public** 继承。当使用不同类型的继承时，遵循以下几个规则：


- **公有继承（public）：**当一个类派生自**公有**基类时，基类的**公有**成员也是派生类的**公有**成员，基类的**保护**成员也是派生类的**保护**成员，基类的**私有**成员不能直接被派生类访问，但是可以通过调用基类的**公有**和**保护**成员来访问。

- **保护继承（protected）：** 当一个类派生自**保护**基类时，基类的**公有**和**保护**成员将成为派生类的**保护**成员。

- **私有继承（private）：**当一个类派生自**私有**基类时，基类的**公有**和**保护**成员将成为派生类的**私有**成员。


多继承

多继承即一个子类可以有多个父类，它继承了多个父类的特性。

C++ 类可以从多个类继承成员，语法如下：

```cpp
class :,,…
{

};
```



其中，访问修饰符继承方式是 **public、protected** 或 **private** 其中的一个，用来修饰每个基类，各个基类之间用逗号分隔，如上所示。现在让我们一起看看下面的实例：
 

### 实例



```cpp
#include

using namespace std;

// 基类 Shape
class Shape
{
   public:
      void setWidth(int w)
      {
         width = w;
      }
      void setHeight(int h)
      {
         height = h;
      }
   protected:
      int width;
      int height;
};

// 基类 PaintCost
class PaintCost
{
   public:
      int getCost(int area)
      {
         return area * 70;
      }
};

// 派生类
class Rectangle: public Shape, public PaintCost
{
   public:
      int getArea()
      {
         return (width * height);
      }
};

int main(void)
{
   Rectangle Rect;
   int area;

   Rect.setWidth(5);
   Rect.setHeight(7);

   area = Rect.getArea();

   // 输出对象的面积
   cout << "Total area: " << Rect.getArea() << endl;

   // 输出总花费
   cout << "Total paint cost: $" << Rect.getCost(area) << endl;

   return 0;
}
```



当上面的代码被编译和执行时，它会产生下列结果：

```cpp
Total area: 35
Total paint cost: $2450
```


## C++ 重载运算符和重载函数

C++ 允许在同一作用域中的某个**函数**和**运算符**指定多个定义，分别称为**函数重载**和**运算符重载**。

重载声明是指一个与之前已经在该作用域内声明过的函数或方法具有相同名称的声明，但是它们的参数列表和定义（实现）不相同。

当您调用一个**重载函数**或**重载运算符**时，编译器通过把您所使用的参数类型与定义中的参数类型进行比较，决定选用最合适的定义。选择最合适的重载函数或重载运算符的过程，称为**重载决策**。


C++ 中的函数重载

在同一个作用域内，可以声明几个功能类似的同名函数，但是这些同名函数的形式参数（指参数的个数、类型或者顺序）必须不同。您不能仅通过返回类型的不同来重载函数。

下面的实例中，同名函数 **print()** 被用于输出不同的数据类型：
 

### 实例



```cpp
#include
using namespace std;

class printData
{
   public:
      void print(int i) {
        cout C++ 中的运算符重载

您可以重定义或重载大部分 C++ 内置的运算符。这样，您就能使用自定义类型的运算符。

重载的运算符是带有特殊名称的函数，函数名是由关键字 operator 和其后要重载的运算符符号构成的。与其他函数一样，重载运算符有一个返回类型和一个参数列表。

```cpp
Box operator+(const Box&);
```



声明加法运算符用于把两个 Box 对象相加，返回最终的 Box 对象。大多数的重载运算符可被定义为普通的非成员函数或者被定义为类成员函数。如果我们定义上面的函数为类的非成员函数，那么我们需要为每次操作传递两个参数，如下所示：

```cpp
Box operator+(const Box&, const Box&);
```



下面的实例使用成员函数演示了运算符重载的概念。在这里，对象作为参数进行传递，对象的属性使用 **this** 运算符进行访问，如下所示：
 

### 实例



```cpp
#include
using namespace std;

class Box
{
   public:

      double getVolume(void)
      {
         return length * breadth * height;
      }
      void setLength( double len )
      {
          length = len;
      }

      void setBreadth( double bre )
      {
          breadth = bre;
      }

      void setHeight( double hei )
      {
          height = hei;
      }
      // 重载 + 运算符，用于把两个 Box 对象相加
      Box operator+(const Box& b)
      {
         Box box;
         box.length = this->length + b.length;
         box.breadth = this->breadth + b.breadth;
         box.height = this->height + b.height;
         return box;
      }
   private:
      double length;      // 长度
      double breadth;     // 宽度
      double height;      // 高度
};
// 程序的主函数
int main( )
{
   Box Box1;                // 声明 Box1，类型为 Box
   Box Box2;                // 声明 Box2，类型为 Box
   Box Box3;                // 声明 Box3，类型为 Box
   double volume = 0.0;     // 把体积存储在该变量中

   // Box1 详述
   Box1.setLength(6.0);
   Box1.setBreadth(7.0);
   Box1.setHeight(5.0);

   // Box2 详述
   Box2.setLength(12.0);
   Box2.setBreadth(13.0);
   Box2.setHeight(10.0);

   // Box1 的体积
   volume = Box1.getVolume();
   cout 可重载运算符/不可重载运算符

下面是可重载的运算符列表：

| 双目算术运算符 | + (加)，-(减)，*(乘)，/(除)，% (取模) |
| --- | --- |
| 关系运算符 | ==(等于)，!= (不等于)， (大于)，=(大于等于) |
| 逻辑运算符 | ||(逻辑或)，&&(逻辑与)，!(逻辑非) |
| 单目运算符 | + (正)，-(负)，*(指针)，&(取地址) |
| 自增自减运算符 | ++(自增)，--(自减) |
| 位运算符 | | (按位或)，& (按位与)，~(按位取反)，^(按位异或),，>(右移) |
| 赋值运算符 | =, +=, -=, *=, /= , % = , &=, |=, ^=, >= |
| 空间申请与释放 | new, delete, new[ ] , delete[] |
| 其他运算符 | ()(函数调用)，->(成员访问)，,(逗号)，[](下标) |



下面是不可重载的运算符列表：

- 
.：成员访问运算符
- 
.*, ->*：成员指针访问运算符
- 
::：域运算符
- 
sizeof：长度运算符
- 
?:：条件运算符
- 
#： 预处理符号



运算符重载实例

下面提供了各种运算符重载的实例，帮助您更好地理解重载的概念。

| 序号 | 运算符和实例 |
| --- | --- |
| 1 | 一元运算符重载 |
| 2 | 二元运算符重载 |
| 3 | 关系运算符重载 |
| 4 | 输入/输出运算符重载 |
| 5 | ++ 和 -- 运算符重载 |
| 6 | 赋值运算符重载 |
| 7 | 函数调用运算符 () 重载 |
| 8 | 下标运算符 [] 重载 |


## C++ 多态

**多态**按字面的意思就是多种形态。

当类之间存在层次结构，并且类之间是通过继承关联时，就会用到多态。

在 C++ 中，多态（Polymorphism）是面向对象编程的重要特性之一。


C++ 多态允许使用基类指针或引用来调用子类的重写方法，从而使得同一接口可以表现不同的行为。

多态使得代码更加灵活和通用，程序可以通过基类指针或引用来操作不同类型的对象，而不需要显式区分对象类型。这样可以使代码更具扩展性，在增加新的形状类时不需要修改主程序。

以下是多态的几个关键点：



**虚函数（Virtual Functions）**：
            

- 在基类中声明一个函数为虚函数，使用关键字virtual。

- 派生类可以重写（override）这个虚函数。

- 调用虚函数时，会根据对象的实际类型来决定调用哪个版本的函数。
            
     


**动态绑定（Dynamic Binding）**：
            

- 也称为晚期绑定（Late Binding），在运行时确定函数调用的具体实现。

- 需要使用指向基类的指针或引用来调用虚函数，编译器在运行时根据对象的实际类型来决定调用哪个函数。
            
      


**纯虚函数（Pure Virtual Functions）**：
            

- 一个包含纯虚函数的类被称为抽象类（Abstract Class），它不能被直接实例化。

- 纯虚函数没有函数体，声明时使用= 0。

- 它强制派生类提供具体的实现。
            
    


**多态的实现机制**：
            

- 虚函数表（V-Table）：C++运行时使用虚函数表来实现多态。每个包含虚函数的类都有一个虚函数表，表中存储了指向类中所有虚函数的指针。

- 虚函数指针（V-Ptr）：对象中包含一个指向该类虚函数表的指针。
            
     


**使用多态的优势**：
            

- **代码复用**：通过基类指针或引用，可以操作不同类型的派生类对象，实现代码的复用。

- **扩展性**：新增派生类时，不需要修改依赖于基类的代码，只需要确保新类正确重写了虚函数。

- **解耦**：多态允许程序设计更加模块化，降低类之间的耦合度。
            
      


**注意事项**：
            

- 只有通过基类的指针或引用调用虚函数时，才会发生多态。

- 如果直接使用派生类的对象调用函数，那么调用的是派生类中的版本，而不是基类中的版本。

- 多态性需要运行时类型信息（RTTI），这可能会增加程序的开销。
            
实例 1     

我们通过一个简单的实例来了解多态的应用：

### 实例 1


```cpp
#include

using namespace std;

// 基类 Animal

class Animal {

public:

    // 虚函数 sound，为不同的动物发声提供接口

    virtual void sound() const {

        cout sound();  // 调用 Dog 的 sound 方法

    delete animalPtr;    // 释放内存，调用 Dog 和 Animal 的析构函数

    // 创建 Cat 对象，并指向 Animal 指针

    animalPtr = new Cat();

    animalPtr->sound();  // 调用 Cat 的 sound 方法

    delete animalPtr;    // 释放内存，调用 Cat 和 Animal 的析构函数

    return 0;

}
```

程序执行输出为：

```cpp
Dog barks
Dog destroyed
Animal destroyed
Cat meows
Cat destroyed
Animal destroyed
```




代码解释


**基类 `Animal`**：
        

- `Animal` 类定义了一个虚函数 `sound()`，这是一个虚函数（`virtual`），用于表示动物发声的行为。

- `~Animal()` 为虚析构函数，确保在释放基类指针指向的派生类对象时能够正确调用派生类的析构函数，防止内存泄漏。
        
  


**派生类 `Dog` 和 `Cat`**：
        

- `Dog` 和 `Cat` 类都从 `Animal` 类派生，并各自实现了 `sound()` 方法。

- `Dog` 的 `sound()` 输出"Dog barks"；`Cat` 的 `sound()` 输出"Cat meows"。这使得同一个方法（`sound()`）在不同的类中表现不同的行为。
        
  


**主函数 `main()`**：
        

- 创建一个基类指针 `animalPtr`。

- 使用 `new Dog()` 创建 `Dog` 对象，将其地址赋给 `animalPtr`。此时，调用 `animalPtr->sound()` 会输出"Dog barks"，因为 `animalPtr` 实际指向的是 `Dog` 对象。

- 释放 `Dog` 对象时，先调用 `Dog` 的析构函数，再调用 `Animal` 的析构函数。

- 使用 `new Cat()` 创建 `Cat` 对象并赋给 `animalPtr`，再调用 `animalPtr->sound()`，输出"Cat meows"，显示多态行为。
        关键概念

-

**虚函数**：通过在基类中使用 `virtual` 关键字声明虚函数，派生类可以重写这个函数，从而使得在运行时根据对象类型调用正确的函数。
-

**动态绑定**：C++ 的多态通过动态绑定实现。在运行时，基类指针 `animalPtr` 会根据它实际指向的对象类型（`Dog` 或 `Cat`）调用对应的 `sound()` 方法。
-

**虚析构函数**：在具有多态行为的基类中，析构函数应该声明为 `virtual`，以确保在删除派生类对象时调用派生类的析构函数，防止资源泄漏。
实例 2

下面的实例中，我们通过多态实现了一个通用的 Shape 基类和两个派生类 Rectangle 和 Triangle。

通过基类指针调用不同的派生类方法，展示了多态的动态绑定特性。
 

### 实例 2



```cpp
#include
using namespace std;

// 基类 Shape，表示形状
class Shape {
   protected:
      int width, height; // 宽度和高度

   public:
      // 构造函数，带有默认参数
      Shape(int a = 0, int b = 0) : width(a), height(b) { }

      // 虚函数 area，用于计算面积
      // 使用 virtual 关键字，实现多态
      virtual int area() {
         cout area() area() 代码分析


**Shape 类的定义：**
- `Shape` 是一个抽象基类，定义了一个虚函数 `area()`。`area()` 是用来计算面积的虚函数，并使用了 `virtual` 关键字，这样在派生类中可以重写该函数，进而实现多态。
- `width` 和 `height` 是 `protected` 属性，只能在 `Shape` 类及其派生类中访问。


```cpp
// 基类 Shape，表示形状
class Shape {
   protected:
      int width, height; // 宽度和高度

   public:
      // 构造函数，带有默认参数
      Shape(int a = 0, int b = 0) : width(a), height(b) { }

      // 虚函数 area，用于计算面积
      virtual int area() {
         cout area()`。由于 `area()` 是虚函数，此时会动态绑定到 `Rectangle::area()`，输出矩形的面积。
- 接着，将 `shape` 指针指向 `Triangle` 对象 `tri`，调用 `shape->area()` 时会动态绑定到 `Triangle::area()`，输出三角形的面积。

```cpp
// 主函数
int main() {
   Shape *shape;           // 基类指针
   Rectangle rec(10, 7);   // 矩形对象
   Triangle tri(10, 5);    // 三角形对象

   // 将基类指针指向矩形对象，并调用 area 函数
   shape = &rec;
   cout area() area() 关键概念
-

**虚函数**：在基类 `Shape` 中定义了虚函数 `area()`。虚函数的作用是让派生类可以重写此函数，并在运行时根据指针的实际对象类型调用适当的函数实现。
-

**动态绑定**：因为 `area()` 是虚函数，`shape->area()` 调用时会在运行时根据 `shape` 实际指向的对象类型（`Rectangle` 或 `Triangle`）来调用相应的 `area()` 实现。这种在运行时决定调用哪个函数的机制称为动态绑定，是多态的核心。
-

**基类指针的多态性**：基类指针 `shape` 可以指向任何派生自 `Shape` 的对象。当 `shape` 指向不同的派生类对象时，调用 `shape->area()` 会产生不同的行为，这体现了多态的特性。

虚函数

**虚函数**是在基类中使用关键字 **virtual** 声明的函数。

**虚函数**允许子类重写它，从而在运行时通过基类指针或引用调用子类的重写版本，实现动态绑定。

我们想要的是在程序中任意点可以根据所调用的对象类型来选择调用的函数，这种操作被称为**动态链接**，或**后期绑定。**

 **特点：**

- **在基类中可以有实现**。通常虚函数在基类中提供默认实现，但子类可以选择重写。
- **动态绑定**：在运行时根据对象的实际类型调用相应的函数版本。
- **可选重写**：派生类可以选择性地重写虚函数，但不是必须。

### 实例


```cpp
#include

using namespace std;

class Animal {

public:

    virtual void sound() {  // 虚函数

        cout sound();  // 输出: Dog barks

    delete animal;

}
```


以上代码中，sound 是 Animal 类的虚函数。通过 Animal* 指针 animal 调用 sound() 时，程序会根据实际对象类型（Dog）来选择调用 Dog::sound()。
纯虚函数

您可能想要在基类中定义虚函数，以便在派生类中重新定义该函数更好地适用于对象，但是您在基类中又不能对虚函数给出有意义的实现，这个时候就会用到纯虚函数。

纯虚函数是没有实现的虚函数，在基类中用 = 0 来声明。


纯虚函数表示基类定义了一个接口，但具体实现由派生类负责。

纯虚函数使得基类变为抽象类（abstract class），无法实例化。

**特点：**

- **必须在基类中声明为 `= 0`**，表示没有实现，子类必须重写。
- **抽象类**：包含纯虚函数的类不能直接实例化，必须通过派生类实现所有纯虚函数才能创建对象。
- **接口定义**：纯虚函数通常用于定义接口，让派生类实现具体行为。


我们可以把基类中的虚函数 area() 改写如下：
 

```cpp
#include
using namespace std;

class Shape {
public:
    virtual int area() = 0;  // 纯虚函数，强制子类实现此方法
};

class Rectangle : public Shape {
private:
    int width, height;
public:
    Rectangle(int w, int h) : width(w), height(h) { }

    int area() override {  // 实现纯虚函数
        return width * height;
    }
};

int main() {
    Shape *shape = new Rectangle(10, 5);
    cout area() 虚函数与纯虚函数的对比

| 特性 | 虚函数（Virtual Function） | 纯虚函数（Pure Virtual Function） |
| --- | --- | --- |
| 定义 | 基类中使用 virtual 声明，有实现 | 基类中使用 = 0 声明，无实现 |
| 子类重写 | 子类可以选择重写 | 子类必须实现 |
| 抽象性 | 可以实例化类 | 使类变为抽象类，无法实例化 |
| 用途 | 提供默认行为，允许子类重写 | 定义接口，强制子类实现具体行为 |


## C++ 数据抽象

数据抽象是指，只向外界提供关键信息，并隐藏其后台的实现细节，即只表现必要的信息而不呈现细节。

数据抽象是一种依赖于接口和实现分离的编程（设计）技术。

让我们举一个现实生活中的真实例子，比如一台电视机，您可以打开和关闭、切换频道、调整音量、添加外部组件（如喇叭、录像机、DVD 播放器），但是您不知道它的内部实现细节，也就是说，您并不知道它是如何通过缆线接收信号，如何转换信号，并最终显示在屏幕上。

因此，我们可以说电视把它的内部实现和外部接口分离开了，您无需知道它的内部实现原理，直接通过它的外部接口（比如电源按钮、遥控器、声量控制器）就可以操控电视。

现在，让我们言归正传，就 C++ 编程而言，C++ 类为**数据抽象**提供了可能。它们向外界提供了大量用于操作对象数据的公共方法，也就是说，外界实际上并不清楚类的内部实现。

例如，您的程序可以调用 **sort()** 函数，而不需要知道函数中排序数据所用到的算法。实际上，函数排序的底层实现会因库的版本不同而有所差异，只要接口不变，函数调用就可以照常工作。

在 C++ 中，我们使用**类**来定义我们自己的抽象数据类型（ADT）。您可以使用类 **iostream** 的 **cout** 对象来输出数据到标准输出，如下所示：
 

### 实例



```cpp
#include
using namespace std;

int main( )
{
   cout 访问标签强制抽象

在 C++ 中，我们使用访问标签来定义类的抽象接口。一个类可以包含零个或多个访问标签：


- 使用公共标签定义的成员都可以访问该程序的所有部分。一个类型的数据抽象视图是由它的公共成员来定义的。

- 使用私有标签定义的成员无法访问到使用类的代码。私有部分对使用类型的代码隐藏了实现细节。


访问标签出现的频率没有限制。每个访问标签指定了紧随其后的成员定义的访问级别。指定的访问级别会一直有效，直到遇到下一个访问标签或者遇到类主体的关闭右括号为止。

数据抽象的好处

数据抽象有两个重要的优势：


- 类的内部受到保护，不会因无意的用户级错误导致对象状态受损。

- 类实现可能随着时间的推移而发生变化，以便应对不断变化的需求，或者应对那些要求不改变用户级代码的错误报告。


如果只在类的私有部分定义数据成员，编写该类的作者就可以随意更改数据。如果实现发生改变，则只需要检查类的代码，看看这个改变会导致哪些影响。如果数据是公有的，则任何直接访问旧表示形式的数据成员的函数都可能受到影响。

数据抽象的实例

C++ 程序中，任何带有公有和私有成员的类都可以作为数据抽象的实例。请看下面的实例：
 

### 实例



```cpp
#include
using namespace std;

class Adder{
   public:
      // 构造函数
      Adder(int i = 0)
      {
        total = i;
      }
      // 对外的接口
      void addNum(int number)
      {
          total += number;
      }
      // 对外的接口
      int getTotal()
      {
          return total;
      };
   private:
      // 对外隐藏的数据
      int total;
};
int main( )
{
   Adder a;

   a.addNum(10);
   a.addNum(20);
   a.addNum(30);

   cout 设计策略

抽象把代码分离为接口和实现。所以在设计组件时，必须保持接口独立于实现，这样，如果改变底层实现，接口也将保持不变。

在这种情况下，不管任何程序使用接口，接口都不会受到影响，只需要将最新的实现重新编译即可。


## C++ 数据封装

数据封装（Data Encapsulation）是面向对象编程（OOP）的一个基本概念，它通过将数据和操作数据的函数封装在一个类中来实现。这种封装确保了数据的私有性和完整性，防止了外部代码对其直接访问和修改。

所有的 C++ 程序都有以下两个基本要素： 


- **程序语句（代码）：**这是程序中执行动作的部分，它们被称为函数。

- **程序数据：**数据是程序的信息，会受到程序函数的影响。


封装是面向对象编程中的把数据和操作数据的函数绑定在一起的一个概念，这样能避免受到外界的干扰和误用，从而确保了安全。数据封装引申出了另一个重要的 OOP 概念，即**数据隐藏**。

**数据封装**是一种把数据和操作数据的函数捆绑在一起的机制，**数据抽象**是一种仅向用户暴露接口而把具体的实现细节隐藏起来的机制。

C++ 通过创建**类**来支持封装和数据隐藏（public、protected、private）。我们已经知道，类包含私有成员（private）、保护成员（protected）和公有成员（public）成员。默认情况下，在类中定义的所有项目都是私有的。例如：
 

```cpp
class Box
{
   public:
      double getVolume(void)
      {
         return length * breadth * height;
      }
   private:
      double length;      // 长度
      double breadth;     // 宽度
      double height;      // 高度
};
```



变量 length、breadth 和 height 都是私有的（private）。这意味着它们只能被 Box 类中的其他成员访问，而不能被程序中其他部分访问。这是实现封装的一种方式。

为了使类中的成员变成公有的（即，程序中的其他部分也能访问），必须在这些成员前使用 **public** 关键字进行声明。所有定义在 public 标识符后边的变量或函数可以被程序中所有其他的函数访问。

把一个类定义为另一个类的友元类，会暴露实现细节，从而降低了封装性。理想的做法是尽可能地对外隐藏每个类的实现细节。

**访问修饰符：**

- **private**: 私有成员只能在类的内部访问，不能被类的外部代码直接访问。
- **public**: 公有成员可以被类的外部代码直接访问。
- **protected**: 受保护成员可以被类和其派生类访问。
数据封装的实例

C++ 程序中，任何带有公有和私有成员的类都可以作为数据封装和数据抽象的实例。请看下面的实例：
 

### 实例



```cpp
#include
using namespace std;

class Adder{
   public:
      // 构造函数
      Adder(int i = 0)
      {
        total = i;
      }
      // 对外的接口
      void addNum(int number)
      {
          total += number;
      }
      // 对外的接口
      int getTotal()
      {
          return total;
      };
   private:
      // 对外隐藏的数据
      int total;
};
int main( )
{
   Adder a;

   a.addNum(10);
   a.addNum(20);
   a.addNum(30);

   cout

using namespace std;

class Student {

private:

    string name;

    int age;

public:

    // 构造函数

    Student(string studentName, int studentAge) {

        name = studentName;

        age = studentAge;

    }

    // 访问器函数（getter）

    string getName() {

        return name;

    }

    int getAge() {

        return age;

    }

    // 修改器函数（setter）

    void setName(string studentName) {

        name = studentName;

    }

    void setAge(int studentAge) {

        if (studentAge > 0) {

            age = studentAge;

        } else {

            cout 设计策略

通常情况下，我们都会设置类成员状态为私有（private），除非我们真的需要将其暴露，这样才能保证良好的**封装性**。

这通常应用于数据成员，但它同样适用于所有成员，包括虚函数。
数据封装的优点

- **数据隐藏**: 通过将数据成员声明为私有，防止外部代码直接访问这些数据。
- **提高代码可维护性**: 提供公共方法来访问和修改数据，这使得可以在不影响外部代码的情况下修改类的内部实现。
- **增强安全性**: 防止不合法的数据输入和不当的修改操作。
- **实现抽象**: 提供了一种机制，使得用户不需要了解类的内部实现细节，只需要了解如何使用类的公共接口即可。


## C++ 接口（抽象类）

接口描述了类的行为和功能，而不需要完成类的特定实现。

C++ 接口是使用**抽象类**来实现的，抽象类与数据抽象互不混淆，数据抽象是一个把实现细节与相关的数据分离开的概念。

如果类中至少有一个函数被声明为纯虚函数，则这个类就是抽象类。纯虚函数是通过在声明中使用 "= 0" 来指定的，如下所示：
 

```cpp
class Box
{
   public:
      // 纯虚函数
      virtual double getVolume() = 0;
   private:
      double length;      // 长度
      double breadth;     // 宽度
      double height;      // 高度
};
```



设计**抽象类**（通常称为 ABC）的目的，是为了给其他类提供一个可以继承的适当的基类。抽象类不能被用于实例化对象，它只能作为**接口**使用。如果试图实例化一个抽象类的对象，会导致编译错误。

因此，如果一个 ABC 的子类需要被实例化，则必须实现每个纯虚函数，这也意味着 C++ 支持使用 ABC 声明接口。如果没有在派生类中重写纯虚函数，就尝试实例化该类的对象，会导致编译错误。

可用于实例化对象的类被称为**具体类**。

抽象类的实例

请看下面的实例，基类 Shape 提供了一个接口 **getArea()**，在两个派生类 Rectangle 和 Triangle 中分别实现了 **getArea()**：
 

### 实例



```cpp
#include

using namespace std;

// 基类
class Shape
{
public:
   // 提供接口框架的纯虚函数
   virtual int getArea() = 0;
   void setWidth(int w)
   {
      width = w;
   }
   void setHeight(int h)
   {
      height = h;
   }
protected:
   int width;
   int height;
};

// 派生类
class Rectangle: public Shape
{
public:
   int getArea()
   {
      return (width * height);
   }
};
class Triangle: public Shape
{
public:
   int getArea()
   {
      return (width * height)/2;
   }
};

int main(void)
{
   Rectangle Rect;
   Triangle  Tri;

   Rect.setWidth(5);
   Rect.setHeight(7);
   // 输出对象的面积
   cout 设计策略

面向对象的系统可能会使用一个抽象基类为所有的外部应用程序提供一个适当的、通用的、标准化的接口。然后，派生类通过继承抽象基类，就把所有类似的操作都继承下来。

外部应用程序提供的功能（即公有函数）在抽象基类中是以纯虚函数的形式存在的。这些纯虚函数在相应的派生类中被实现。

这个架构也使得新的应用程序可以很容易地被添加到系统中，即使是在系统被定义之后依然可以如此。


---

# C++ 高级教程


## C++ 文件和流

到目前为止，我们已经使用了 **iostream** 标准库，它提供了 **cin** 和 **cout** 方法分别用于从标准输入读取流和向标准输出写入流。

本教程介绍如何从文件读取流和向文件写入流。这就需要用到 C++ 中另一个标准库 **fstream**，它定义了三个新的数据类型：

| 数据类型 | 描述 |
| --- | --- |
| ofstream | 该数据类型表示输出文件流，用于创建文件并向文件写入信息。 |
| ifstream | 该数据类型表示输入文件流，用于从文件读取信息。 |
| fstream | 该数据类型通常表示文件流，且同时具有 ofstream 和 ifstream 两种功能，这意味着它可以创建文件，向文件写入信息，从文件读取信息。 |



要在 C++ 中进行文件处理，必须在 C++ 源代码文件中包含头文件 <iostream> 和 <fstream>。

打开文件

在从文件读取信息或者向文件写入信息之前，必须先打开文件。**ofstream** 和 **fstream** 对象都可以用来打开文件进行写操作，如果只需要打开文件进行读操作，则使用 **ifstream** 对象。

下面是 open() 函数的标准语法，open() 函数是 fstream、ifstream 和 ofstream 对象的一个成员。

```cpp
void open(const char *filename, ios::openmode mode);
```



在这里，**open()** 成员函数的第一参数指定要打开的文件的名称和位置，第二个参数定义文件被打开的模式。

| 模式标志 | 描述 |
| --- | --- |
| ios::app | 追加模式。所有写入都追加到文件末尾。 |
| ios::ate | 文件打开后定位到文件末尾。 |
| ios::in | 打开文件用于读取。 |
| ios::out | 打开文件用于写入。 |
| ios::trunc | 如果该文件已经存在，其内容将在打开文件之前被截断，即把文件长度设为 0。 |



您可以把以上两种或两种以上的模式结合使用。例如，如果您想要以写入模式打开文件，并希望截断文件，以防文件已存在，那么您可以使用下面的语法：

```cpp
ofstream outfile;
outfile.open("file.dat", ios::out | ios::trunc );
```



类似地，您如果想要打开一个文件用于读写，可以使用下面的语法：

```cpp
ifstream  afile;
afile.open("file.dat", ios::out | ios::in );
```



关闭文件

当 C++ 程序终止时，它会自动关闭刷新所有流，释放所有分配的内存，并关闭所有打开的文件。但程序员应该养成一个好习惯，在程序终止前关闭所有打开的文件。

下面是 close() 函数的标准语法，close() 函数是 fstream、ifstream 和 ofstream 对象的一个成员。

```cpp
void close();
```



写入文件

在 C++ 编程中，我们使用流插入运算符（ << ）向文件写入信息，就像使用该运算符输出信息到屏幕上一样。唯一不同的是，在这里您使用的是 **ofstream** 或 **fstream** 对象，而不是 **cout** 对象。

读取文件

在 C++ 编程中，我们使用流提取运算符（ >> ）从文件读取信息，就像使用该运算符从键盘输入信息一样。唯一不同的是，在这里您使用的是 **ifstream** 或 **fstream** 对象，而不是 **cin** 对象。

读取 & 写入实例

下面的 C++ 程序以读写模式打开一个文件。在向文件 afile.dat 写入用户输入的信息之后，程序从文件读取信息，并将其输出到屏幕上：
 

### 实例



```cpp
#include
#include
using namespace std;

int main() {

   char data[100];

   // 以写模式打开文件
   ofstream outfile;
   outfile.open("afile.dat");

   cout > data;
   cin.ignore();

   // 再次向文件写入用户输入的数据
   outfile > data;

   // 在屏幕上写入数据
   cout > data;
   cout 文件位置指针

**istream** 和 **ostream** 都提供了用于重新定位文件位置指针的成员函数。这些成员函数包括关于 istream 的 **seekg**（"seek get"）和关于 ostream 的 **seekp**（"seek put"）。

seekg 和 seekp 的参数通常是一个长整型。第二个参数可以用于指定查找方向。查找方向可以是 **ios::beg**（默认的，从流的开头开始定位），也可以是 **ios::cur**（从流的当前位置开始定位），也可以是 **ios::end**（从流的末尾开始定位）。

文件位置指针是一个整数值，指定了从文件的起始位置到指针所在位置的字节数。下面是关于定位 "get" 文件位置指针的实例：
 

```cpp
// 定位到 fileObject 的第 n 个字节（假设是 ios::beg）
fileObject.seekg( n );

// 把文件的读指针从 fileObject 当前位置向后移 n 个字节
fileObject.seekg( n, ios::cur );

// 把文件的读指针从 fileObject 末尾往回移 n 个字节
fileObject.seekg( n, ios::end );

// 定位到 fileObject 的末尾
fileObject.seekg( 0, ios::end );
```


## C++ 异常处理

异常是程序在执行期间产生的问题。C++ 异常是指在程序运行时发生的特殊情况，比如尝试除以零的操作。

异常提供了一种转移程序控制权的方式。C++ 异常处理涉及到三个关键字：**try、catch、throw**。


- **throw:** 当问题出现时，程序会抛出一个异常。这是通过使用 **throw** 关键字来完成的。

- **catch:** 在您想要处理问题的地方，通过异常处理程序捕获异常。**catch** 关键字用于捕获异常。

- **try:** **try** 块中的代码标识将被激活的特定异常。它后面通常跟着一个或多个 catch 块。


如果有一个块抛出一个异常，捕获异常的方法会使用 **try** 和 **catch** 关键字。try 块中放置可能抛出异常的代码，try 块中的代码被称为保护代码。使用 try/catch 语句的语法如下所示：
 

```cpp
try
{
   // 保护代码
}catch( ExceptionName e1 )
{
   // catch 块
}catch( ExceptionName e2 )
{
   // catch 块
}catch( ExceptionName eN )
{
   // catch 块
}
```



如果 **try** 块在不同的情境下会抛出不同的异常，这个时候可以尝试罗列多个 **catch** 语句，用于捕获不同类型的异常。

抛出异常

您可以使用 **throw** 语句在代码块中的任何地方抛出异常。throw 语句的操作数可以是任意的表达式，表达式的结果的类型决定了抛出的异常的类型。

以下是尝试除以零时抛出异常的实例：
 

```cpp
double division(int a, int b)
{
   if( b == 0 )
   {
      throw "Division by zero condition!";
   }
   return (a/b);
}
```




捕获异常

**catch** 块跟在 **try** 块后面，用于捕获异常。您可以指定想要捕捉的异常类型，这是由 catch 关键字后的括号内的异常声明决定的。 
 

```cpp
try
{
   // 保护代码
}catch( ExceptionName e )
{
  // 处理 ExceptionName 异常的代码
}
```



上面的代码会捕获一个类型为 **ExceptionName** 的异常。如果您想让 catch 块能够处理 try 块抛出的任何类型的异常，则必须在异常声明的括号内使用省略号 ...，如下所示：
 

```cpp
try
{
   // 保护代码
}catch(...)
{
  // 能处理任何异常的代码
}
```




下面是一个实例，抛出一个除以零的异常，并在 catch 块中捕获该异常。
 

### 实例



```cpp
#include
using namespace std;

double division(int a, int b)
{
   if( b == 0 )
   {
      throw "Division by zero condition!";
   }
   return (a/b);
}

int main ()
{
   int x = 50;
   int y = 0;
   double z = 0;

   try {
     z = division(x, y);
     cout C++ 标准的异常

C++ 提供了一系列标准的异常，定义在 **<exception>** 中，我们可以在程序中使用这些标准的异常。它们是以父子类层次结构组织起来的，如下所示：





下表是对上面层次结构中出现的每个异常的说明：

| 异常 | 描述 |
| --- | --- |
| std::exception | 该异常是所有标准 C++ 异常的父类。 |
| std::bad_alloc | 该异常可以通过 new 抛出。 |
| std::bad_cast | 该异常可以通过 dynamic_cast 抛出。 |
| std::bad_typeid | 该异常可以通过 typeid 抛出。 |
| std::bad_exception | 这在处理 C++ 程序中无法预期的异常时非常有用。 |
| std::logic_error | 理论上可以通过读取代码来检测到的异常。 |
| std::domain_error | 当使用了一个无效的数学域时，会抛出该异常。 |
| std::invalid_argument | 当使用了无效的参数时，会抛出该异常。 |
| std::length_error | 当创建了太长的 std::string 时，会抛出该异常。 |
| std::out_of_range | 该异常可以通过方法抛出，例如 std::vector 和 std::bitset<>::operator[]()。 |
| std::runtime_error | 理论上不可以通过读取代码来检测到的异常。 |
| std::overflow_error | 当发生数学上溢时，会抛出该异常。 |
| std::range_error | 当尝试存储超出范围的值时，会抛出该异常。 |
| std::underflow_error | 当发生数学下溢时，会抛出该异常。 |



定义新的异常

您可以通过继承和重载 **exception** 类来定义新的异常。下面的实例演示了如何使用 std::exception 类来实现自己的异常：
 

### 实例



```cpp
#include
#include
using namespace std;

struct MyException : public exception
{
  const char * what () const throw ()
  {
    return "C++ Exception";
  }
};

int main()
{
  try
  {
    throw MyException();
  }
  catch(MyException& e)
  {
    std::cout << "MyException caught" << std::endl;
    std::cout << e.what() << std::endl;
  }
  catch(std::exception& e)
  {
    //其他的错误
  }
}
```



这将产生以下结果：

```cpp
MyException caught
C++ Exception
```



在这里，**what()** 是异常类提供的一个公共方法，它已被所有子异常类重载。这将返回异常产生的原因。


## C++ 动态内存

了解动态内存在 C++ 中是如何工作的是成为一名合格的 C++ 程序员必不可少的。C++ 程序中的内存分为两个部分：


- **栈：**在函数内部声明的所有变量都将占用栈内存。

- **堆：**这是程序中未使用的内存，在程序运行时可用于动态分配内存。


很多时候，您无法提前预知需要多少内存来存储某个定义变量中的特定信息，所需内存的大小需要在运行时才能确定。

在 C++ 中，您可以使用特殊的运算符为给定类型的变量在运行时分配堆内的内存，这会返回所分配的空间地址。这种运算符即 **new** 运算符。

如果您不再需要动态分配的内存空间，可以使用 **delete** 运算符，删除之前由 new 运算符分配的内存。

new 和 delete 运算符

下面是使用 new 运算符来为任意的数据类型动态分配内存的通用语法：

```cpp
new data-type;
```



在这里，**data-type** 可以是包括数组在内的任意内置的数据类型，也可以是包括类或结构在内的用户自定义的任何数据类型。让我们先来看下内置的数据类型。例如，我们可以定义一个指向 double 类型的指针，然后请求内存，该内存在执行时被分配。我们可以按照下面的语句使用 **new** 运算符来完成这点：
 

```cpp
double* pvalue  = NULL; // 初始化为 null 的指针
pvalue  = new double;   // 为变量请求内存
```



如果自由存储区已被用完，可能无法成功分配内存。所以建议检查 new 运算符是否返回 NULL 指针，并采取以下适当的操作：
 

```cpp
double* pvalue  = NULL;
if( !(pvalue  = new double ))
{
   cout
using namespace std;

int main ()
{
   double* pvalue  = NULL; // 初始化为 null 的指针
   pvalue  = new double;   // 为变量请求内存

   *pvalue = 29494.99;     // 在分配的地址存储值
   cout 数组的动态内存分配

假设我们要为一个字符数组（一个有 20 个字符的字符串）分配内存，我们可以使用上面实例中的语法来为数组动态地分配内存，如下所示：

```cpp
char* pvalue  = NULL;   // 初始化为 null 的指针
pvalue  = new char[20]; // 为变量请求内存
```



要删除我们刚才创建的数组，语句如下：

```cpp
delete [] pvalue;        // 删除 pvalue 所指向的数组
```



下面是 new 操作符的通用语法，可以为多维数组分配内存，如下所示：



### 一维数组



```cpp
// 动态分配,数组长度为 m
int *array=new int [m];

//释放内存
delete [] array;
```







### 二维数组



```cpp
int **array;
// 假定数组第一维长度为 m， 第二维长度为 n
// 动态分配空间
array = new int *[m];
for( int i=0; i
using namespace std;

int main()
{
    int **p;
    int i,j;   //p[4][8]
    //开始分配4行8列的二维数据
    p = new int *[4];
    for(i=0;i
using namespace std;

int main()
{
    int i,j,k;   // p[2][3][4]

    int ***p;
    p = new int **[2];
    for(i=0; i对象的动态内存分配

对象与简单的数据类型没有什么不同。例如，请看下面的代码，我们将使用一个对象数组来理清这一概念：
 

### 实例



```cpp
#include
using namespace std;

class Box
{
   public:
      Box() {
         cout << "调用构造函数！" <<endl;
      }
      ~Box() {
         cout << "调用析构函数！" <<endl;
      }
};

int main( )
{
   Box* myBoxArray = new Box[4];

   delete [] myBoxArray; // 删除数组
   return 0;
}
```



如果要为一个包含四个 Box 对象的数组分配内存，构造函数将被调用 4 次，同样地，当删除这些对象时，析构函数也将被调用相同的次数（4次）。

当上面的代码被编译和执行时，它会产生下列结果：

```cpp
调用构造函数！
调用构造函数！
调用构造函数！
调用构造函数！
调用析构函数！
调用析构函数！
调用析构函数！
调用析构函数！
```


## C++ 命名空间

假设这样一种情况，当一个班上有两个名叫 Zara 的学生时，为了明确区分它们，我们在使用名字之外，不得不使用一些额外的信息，比如他们的家庭住址，或者他们父母的名字等等。

同样的情况也出现在 C++ 应用程序中。例如，您可能会写一个名为 xyz() 的函数，在另一个可用的库中也存在一个相同的函数 xyz()。这样，编译器就无法判断您所使用的是哪一个 xyz() 函数。

因此，引入了**命名空间**这个概念，专门用于解决上面的问题，它可作为附加信息来区分不同库中相同名称的函数、类、变量等。使用了命名空间即定义了上下文。本质上，命名空间就是定义了一个范围。

我们举一个计算机系统中的例子，一个文件夹(目录)中可以包含多个文件夹，每个文件夹中不能有相同的文件名，但不同文件夹中的文件可以重名。


定义命名空间

命名空间的定义使用关键字 **namespace**，后跟命名空间的名称，如下所示：
 

```cpp
namespace namespace_name {
   // 代码声明
}
```

为了调用带有命名空间的函数或变量，需要在前面加上命名空间的名称，如下所示：

 

```cpp
name::code;  // code 可以是变量或函数
```



让我们来看看命名空间如何为变量或函数等实体定义范围：
 

### 实例



```cpp
#include
using namespace std;

// 第一个命名空间
namespace first_space{
   void func(){
      cout using 指令

您可以使用 **using namespace** 指令，这样在使用命名空间时就可以不用在前面加上命名空间的名称。这个指令会告诉编译器，后续的代码将使用指定的命名空间中的名称。
 

### 实例



```cpp
#include
using namespace std;

// 第一个命名空间
namespace first_space{
   void func(){
      cout
using std::cout;

int main ()
{

   cout 不连续的命名空间

命名空间可以定义在几个不同的部分中，因此命名空间是由几个单独定义的部分组成的。一个命名空间的各个组成部分可以分散在多个文件中。

所以，如果命名空间中的某个组成部分需要请求定义在另一个文件中的名称，则仍然需要声明该名称。下面的命名空间定义可以是定义一个新的命名空间，也可以是为已有的命名空间增加新的元素：
 

```cpp
namespace namespace_name {
   // 代码声明
}
```



嵌套的命名空间

命名空间可以嵌套，您可以在一个命名空间中定义另一个命名空间，如下所示：
 

```cpp
namespace namespace_name1 {
   // 代码声明
   namespace namespace_name2 {
      // 代码声明
   }
}
```



您可以通过使用 :: 运算符来访问嵌套的命名空间中的成员：
 

```cpp
// 访问 namespace_name2 中的成员
using namespace namespace_name1::namespace_name2;

// 访问 namespace_name1 中的成员
using namespace namespace_name1;
```



在上面的语句中，如果使用的是 namespace_name1，那么在该范围内 namespace_name2 中的元素也是可用的，如下所示：
 

### 实例



```cpp
#include
using namespace std;

// 第一个命名空间
namespace first_space{
   void func(){
      cout << "Inside first_space" << endl;
   }
   // 第二个命名空间
   namespace second_space{
      void func(){
         cout << "Inside second_space" << endl;
      }
   }
}
using namespace first_space::second_space;
int main ()
{

   // 调用第二个命名空间中的函数
   func();

   return 0;
}
```



当上面的代码被编译和执行时，它会产生下列结果：

```cpp
Inside second_space
```


## C++ 模板

模板是泛型编程的基础，泛型编程即以一种独立于任何特定类型的方式编写代码。

模板是创建泛型类或函数的蓝图或公式。库容器，比如迭代器和算法，都是泛型编程的例子，它们都使用了模板的概念。

每个容器都有一个单一的定义，比如 **向量**，我们可以定义许多不同类型的向量，比如 **vector <int>**  或 **vector <string>**。

您可以使用模板来定义函数和类，接下来让我们一起来看看如何使用。

函数模板

模板函数定义的一般形式如下所示：
 

```cpp
template  ret-type func-name(parameter list)
{
   // 函数的主体
}
```



在这里，type 是函数所使用的数据类型的占位符名称。这个名称可以在函数定义中使用。

下面是函数模板的实例，返回两个数中的最大值：
 

### 实例



```cpp
#include
#include

using namespace std;

template
inline T const& Max (T const& a, T const& b)
{
    return a 类模板

正如我们定义函数模板一样，我们也可以定义类模板。泛型类声明的一般形式如下所示：

```cpp
template  class class-name {
.
.
.
}
```



在这里，**type** 是占位符类型名称，可以在类被实例化的时候进行指定。您可以使用一个逗号分隔的列表来定义多个泛型数据类型。

下面的实例定义了类 Stack<>，并实现了泛型方法来对元素进行入栈出栈操作：
 

### 实例



```cpp
#include
#include
#include
#include
#include

using namespace std;

template
class Stack {
  private:
    vector elems;     // 元素

  public:
    void push(T const&);  // 入栈
    void pop();               // 出栈
    T top() const;            // 返回栈顶元素
    bool empty() const{       // 如果为空则返回真。
        return elems.empty();
    }
};

template
void Stack::push (T const& elem)
{
    // 追加传入元素的副本
    elems.push_back(elem);
}

template
void Stack::pop ()
{
    if (elems.empty()) {
        throw out_of_range("Stack<>::pop(): empty stack");
    }
    // 删除最后一个元素
    elems.pop_back();
}

template
T Stack::top () const
{
    if (elems.empty()) {
        throw out_of_range("Stack<>::top(): empty stack");
    }
    // 返回最后一个元素的副本
    return elems.back();
}

int main()
{
    try {
        Stack         intStack;  // int 类型的栈
        Stack stringStack;    // string 类型的栈

        // 操作 int 类型的栈
        intStack.push(7);
        cout ::pop(): empty stack
```


## C++ 预处理器

预处理器是一些指令，指示编译器在实际编译之前所需完成的预处理。

所有的预处理器指令都是以井号（#）开头，只有空格字符可以出现在预处理指令之前。预处理指令不是 C++ 语句，所以它们不会以分号（;）结尾。

我们已经看到，之前所有的实例中都有 **#include** 指令。这个宏用于把头文件包含到源文件中。

C++ 还支持很多预处理指令，比如 #include、#define、#if、#else、#line 等，让我们一起看看这些重要指令。

#define 预处理

#define 预处理指令用于创建符号常量。该符号常量通常称为**宏**，指令的一般形式是：

```cpp
#define macro-name replacement-text
```



当这一行代码出现在一个文件中时，在该文件中后续出现的所有宏都将会在程序编译之前被替换为 replacement-text。例如：
 

```cpp
#include
using namespace std;

#define PI 3.14159

int main ()
{

    cout  test.p

...
int main ()
{
 
    cout 参数宏

您可以使用 #define 来定义一个带有参数的宏，如下所示：
 

```cpp
#include
using namespace std;

#define MIN(a,b) (a条件编译

有几个指令可以用来有选择地对部分程序源代码进行编译。这个过程被称为条件编译。

条件预处理器的结构与 if 选择结构很像。请看下面这段预处理器的代码：

```cpp
#ifdef NULL
   #define NULL 0
#endif
```



您可以只在调试时进行编译，调试开关可以使用一个宏来实现，如下所示：

```cpp
#ifdef DEBUG
   cerr
using namespace std;
#define DEBUG

#define MIN(a,b) (((a)# 和 ## 运算符

# 和 ## 预处理运算符在 C++ 和 ANSI/ISO C 中都是可用的。# 运算符会把 replacement-text 令牌转换为用引号引起来的字符串。

请看下面的宏定义：
 

### 实例



```cpp
#include
using namespace std;

#define MKSTR( x ) #x

int main ()
{
    cout
using namespace std;

#define concat(a, b) a ## b
int main()
{
   int xy = 100;

   cout C++ 中的预定义宏

C++ 提供了下表所示的一些预定义宏：

| 宏 | 描述 |
| --- | --- |
| __LINE__ | 这会在程序编译时包含当前行号。 |
| __FILE__ | 这会在程序编译时包含当前文件名。 |
| __DATE__ | 这会包含一个形式为 month/day/year 的字符串，它表示把源文件转换为目标代码的日期。 |
| __TIME__ | 这会包含一个形式为 hour:minute:second 的字符串，它表示程序被编译的时间。 |



让我们看看上述这些宏的实例：
 

### 实例



```cpp
#include
using namespace std;

int main ()
{
    cout << "Value of __LINE__ : " << __LINE__ << endl;
    cout << "Value of __FILE__ : " << __FILE__ << endl;
    cout << "Value of __DATE__ : " << __DATE__ << endl;
    cout << "Value of __TIME__ : " << __TIME__ << endl;

    return 0;
}
```



当上面的代码被编译和执行时，它会产生下列结果：

```cpp
Value of __LINE__ : 6
Value of __FILE__ : test.cpp
Value of __DATE__ : Feb 28 2011
Value of __TIME__ : 18:52:48
```
