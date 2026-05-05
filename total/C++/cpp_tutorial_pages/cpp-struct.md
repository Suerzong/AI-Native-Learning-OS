# C++ 结构体(struct)

# C++ 结构体(struct)




C/C++ 数组允许定义可存储相同类型数据项的变量，但是**结构**是 C++ 中另一种用户自定义的可用的数据类型，它允许您存储不同类型的数据项。

结构用于表示一条记录，假设您想要跟踪图书馆中书本的动态，您可能需要跟踪每本书的下列属性：


- Title ：标题

- Author ：作者 

- Subject ：类目 

- Book ID ：书的 ID




## 定义结构

在 C++ 中，struct 语句用于定义结构体（structure）。

结构体是一种用户自定义的数据类型，用于将不同类型的数据组合在一起。与类（class）类似，结构体允许你定义成员变量和成员函数。

为了定义结构，您必须使用 **struct** 语句。struct 语句定义了一个包含多个成员的新的数据类型，struct 语句的格式如下：


struct type_name {
member_type1 member_name1;
member_type2 member_name2;
member_type3 member_name3;
.
.
} object_names;