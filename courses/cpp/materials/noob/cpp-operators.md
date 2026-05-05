# C++ 运算符

# C++ 运算符




运算符是一种告诉编译器执行特定的数学或逻辑操作的符号。C++ 内置了丰富的运算符，并提供了以下类型的运算符：


- 算术运算符

- 关系运算符

- 逻辑运算符

- 位运算符

- 赋值运算符

- 杂项运算符


本章将逐一介绍算术运算符、关系运算符、逻辑运算符、位运算符、赋值运算符和其他运算符。



## 算术运算符


下表显示了 C++ 支持的算术运算符。

假设变量 A 的值为 10，变量 B 的值为 20，则：


| 运算符 | 描述 | 实例 

| + | 把两个操作数相加 |  A + B 将得到 30 

| - | 从第一个操作数中减去第二个操作数 |  A - B 将得到 -10 

| * | 把两个操作数相乘 |  A * B 将得到 200 

| / | 分子除以分母 |  B / A 将得到 2 

| % | 取模运算符，整除后的余数 |  B % A 将得到 0 

| ++ | [自增运算符](/cplusplus/cpp-increment-decrement-operators.html)，整数值增加 1 |  A++ 将得到 11 

| -- | [自减运算符](/cplusplus/cpp-increment-decrement-operators.html)，整数值减少 1 |  A-- 将得到 9 


### 实例


请看下面的实例，了解 C++ 中可用的算术运算符。

复制并粘贴下面的 C++ 程序到 test.cpp 文件中，编译并运行程序。


## 实例


#include <iostream>
using namespace std;
 
int main()
{
   int a = 21;
   int b = 10;
   int c;
 
   c = a + b;
   cout << "Line 1 - c 的值是 " << c << endl ;
   c = a - b;
   cout << "Line 2 - c 的值是 " << c << endl ;
   c = a * b;
   cout << "Line 3 - c 的值是 " << c << endl ;
   c = a / b;
   cout << "Line 4 - c 的值是 " << c << endl ;
   c = a % b;
   cout << "Line 5 - c 的值是 " << c << endl ;
 
   int d = 10;   //  测试自增、自减
   c = d++;
   cout << "Line 6 - c 的值是 " << c << endl ;
 
   d = 10;    // 重新赋值
   c = d--;
   cout << "Line 7 - c 的值是 " << c << endl ;
   return 0;
}