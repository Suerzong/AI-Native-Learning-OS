# C++ 基本的输入输出

# C++ 基本的输入输出




C++ 标准库提供了一组丰富的输入/输出功能，我们将在后续的章节进行介绍。本章将讨论 C++ 编程中最基本和最常见的 I/O 操作。

C++ 的 I/O 发生在流中，流是字节序列。如果字节流是从设备（如键盘、磁盘驱动器、网络连接等）流向内存，这叫做**输入操作**。如果字节流是从内存流向设备（如显示屏、打印机、磁盘驱动器、网络连接等），这叫做**输出操作**。



## I/O 库头文件


下列的头文件在 C++ 编程中很重要。


| 头文件 | 函数和描述 

| [<iostream>](https://www.runoob.com/cplusplus/cpp-libs-iostream.html) | 该文件定义了 **cin、cout、cerr** 和 **clog** 对象，分别对应于标准输入流、标准输出流、非缓冲标准错误流和缓冲标准错误流。  

| [<iomanip>](https://www.runoob.com/cplusplus/cpp-libs-iomanip.html) | 该文件通过所谓的参数化的流操纵器（比如 **setw** 和 **setprecision**），来声明对执行标准化 I/O 有用的服务。  

| [<fstream>](https://www.runoob.com/cplusplus/cpp-libs-fstream.html) | 该文件为用户控制的文件处理声明服务。我们将在文件和流的相关章节讨论它的细节。  



## 标准输出流（cout）


预定义的对象 **cout** 是 **iostream** 类的一个实例。cout 对象"连接"到标准输出设备，通常是显示屏。**cout** 是与流插入运算符 << 结合使用的，如下所示：
 

## 实例


#include <iostream>
 
using namespace std;
 
int main( )
{
   char str[] = "Hello C++";
 
   cout << "Value of str is : " << str << endl;
}