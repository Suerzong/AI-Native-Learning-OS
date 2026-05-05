# C++ 预处理器

# C++ 预处理器



预处理器是一些指令，指示编译器在实际编译之前所需完成的预处理。

所有的预处理器指令都是以井号（#）开头，只有空格字符可以出现在预处理指令之前。预处理指令不是 C++ 语句，所以它们不会以分号（;）结尾。

我们已经看到，之前所有的实例中都有 **#include** 指令。这个宏用于把头文件包含到源文件中。

C++ 还支持很多预处理指令，比如 #include、#define、#if、#else、#line 等，让我们一起看看这些重要指令。


## #define 预处理


#define 预处理指令用于创建符号常量。该符号常量通常称为**宏**，指令的一般形式是：

```cpp
#define macro-name replacement-text
```


当这一行代码出现在一个文件中时，在该文件中后续出现的所有宏都将会在程序编译之前被替换为 replacement-text。例如：
 

#include <iostream>
using namespace std;
 
#define PI 3.14159
 
int main ()
{
 
    cout << "Value of PI :" << PI << endl; 
 
    return 0;
}