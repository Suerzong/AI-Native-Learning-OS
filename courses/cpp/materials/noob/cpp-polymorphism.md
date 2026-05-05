# C++ 多态

# C++ 多态



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
            

## 实例 1
     

我们通过一个简单的实例来了解多态的应用：

## 实例 1
 
#include <iostream>

using namespace std;

// 基类 Animal

class Animal &#123;

public:

    // 虚函数 sound，为不同的动物发声提供接口

    virtual void sound&#40;&#41; const &#123;

        cout << "Animal makes a sound" << endl;

    &#125;

    

    // 虚析构函数确保子类对象被正确析构

    virtual ~Animal&#40;&#41; &#123; 

        cout << "Animal destroyed" << endl; 

    &#125;

&#125;;

// 派生类 Dog，继承自 Animal

class Dog : public Animal &#123;

public:

    // 重写 sound 方法

    void sound&#40;&#41; const override &#123;

        cout << "Dog barks" << endl;

    &#125;

    

    ~Dog&#40;&#41; &#123;

        cout << "Dog destroyed" << endl;

    &#125;

&#125;;

// 派生类 Cat，继承自 Animal

class Cat : public Animal &#123;

public:

    // 重写 sound 方法

    void sound&#40;&#41; const override &#123;

        cout << "Cat meows" << endl;

    &#125;

    

    ~Cat&#40;&#41; &#123;

        cout << "Cat destroyed" << endl;

    &#125;

&#125;;

// 测试多态

int main&#40;&#41; &#123;

    Animal* animalPtr;  // 基类指针

    // 创建 Dog 对象，并指向 Animal 指针

    animalPtr = new Dog&#40;&#41;;

    animalPtr->sound&#40;&#41;;  // 调用 Dog 的 sound 方法

    delete animalPtr;    // 释放内存，调用 Dog 和 Animal 的析构函数

    // 创建 Cat 对象，并指向 Animal 指针

    animalPtr = new Cat&#40;&#41;;

    animalPtr->sound&#40;&#41;;  // 调用 Cat 的 sound 方法

    delete animalPtr;    // 释放内存，调用 Cat 和 Animal 的析构函数

    return 0;

&#125;

   

程序执行输出为：

```cpp
Dog barks
Dog destroyed
Animal destroyed
Cat meows
Cat destroyed
Animal destroyed
```




### 代码解释

        

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
        

### 关键概念

 
- 

**虚函数**：通过在基类中使用 `virtual` 关键字声明虚函数，派生类可以重写这个函数，从而使得在运行时根据对象类型调用正确的函数。
- 

**动态绑定**：C++ 的多态通过动态绑定实现。在运行时，基类指针 `animalPtr` 会根据它实际指向的对象类型（`Dog` 或 `Cat`）调用对应的 `sound()` 方法。
- 

**虚析构函数**：在具有多态行为的基类中，析构函数应该声明为 `virtual`，以确保在删除派生类对象时调用派生类的析构函数，防止资源泄漏。

## 实例 2


下面的实例中，我们通过多态实现了一个通用的 Shape 基类和两个派生类 Rectangle 和 Triangle。

通过基类指针调用不同的派生类方法，展示了多态的动态绑定特性。
 

## 实例 2


#include <iostream>
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
         cout << "Shape class area: " << endl;
         return 0;
      }
};
 
// 派生类 Rectangle，表示矩形
class Rectangle : public Shape {
   public:
      // 构造函数，使用基类构造函数初始化 width 和 height
      Rectangle(int a = 0, int b = 0) : Shape(a, b) { }
 
      // 重写 area 函数，计算矩形面积
      int area() override { 
         cout << "Rectangle class area: " << endl;
         return width * height;
      }
};
 
// 派生类 Triangle，表示三角形
class Triangle : public Shape {
   public:
      // 构造函数，使用基类构造函数初始化 width 和 height
      Triangle(int a = 0, int b = 0) : Shape(a, b) { }
 
      // 重写 area 函数，计算三角形面积
      int area() override { 
         cout << "Triangle class area: " << endl;
         return (width * height / 2); 
      }
};
 
// 主函数
int main() {
   Shape *shape;           // 基类指针
   Rectangle rec(10, 7);   // 矩形对象
   Triangle tri(10, 5);    // 三角形对象
 
   // 将基类指针指向矩形对象，并调用 area 函数
   shape = &rec;
   cout << "Rectangle Area: " << shape->area() << endl;
 
   // 将基类指针指向三角形对象，并调用 area 函数
   shape = &tri;
   cout << "Triangle Area: " << shape->area() << endl;
 
   return 0;
}