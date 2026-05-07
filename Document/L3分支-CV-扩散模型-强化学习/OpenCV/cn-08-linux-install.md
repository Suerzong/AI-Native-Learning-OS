![Logo](../../opencv-logo-small.png) |  OpenCV 4.14.0-pre 开源计算机视觉库
---|---

  * [OpenCV 教程](../../d9/df8/tutorial_root.html)
  * [OpenCV 简介](../../df/d65/tutorial_table_of_content_introduction.html)

Linux 下的安装

### 目录

  * 快速开始
    * 构建核心模块
    * 使用 opencv_contrib 构建
  * 详细流程
    * 安装编译器和构建工具
    * 下载源码
    * 配置和构建
    * 检查构建结果
    * 安装

**上一篇教程：** [OpenCV 环境变量参考](../../d6/dea/tutorial_env_reference.html)
**下一篇教程：** [使用 oneAPI 构建 OpenCV](../../d9/d08/tutorial_oneapi_install.html)

|
---|---
原始作者 | Ana Huamán
兼容性 | OpenCV >= 3.0

# 快速开始

## 构建核心模块

# 安装最低前提依赖（以 Ubuntu 18.04 为例）

sudo apt update && sudo apt install -y cmake g++ wget unzip

# 下载并解压源码

wget -O opencv.zip https://github.com/opencv/opencv/archive/4.x.zip

unzip opencv.zip

# 创建构建目录

mkdir -p build && cd build

# 配置

cmake ../opencv-4.x

# 构建

cmake --build .

## 使用 opencv_contrib 构建

# 安装最低前提依赖（以 Ubuntu 18.04 为例）

sudo apt update && sudo apt install -y cmake g++ wget unzip

# 下载并解压源码

wget -O opencv.zip https://github.com/opencv/opencv/archive/4.x.zip

wget -O opencv_contrib.zip https://github.com/opencv/opencv_contrib/archive/4.x.zip

unzip opencv.zip

unzip opencv_contrib.zip

# 创建构建目录并进入

mkdir -p build && cd build

# 配置

cmake -DOPENCV_EXTRA_MODULES_PATH=../opencv_contrib-4.x/modules ../opencv-4.x

# 构建

cmake --build .

# 详细流程

本节提供构建过程的更多细节，并描述了替代方法和工具。请参阅 [OpenCV 安装概述](../../d0/d3d/tutorial_general_install.html) 教程了解通用安装详情，参阅 [OpenCV 配置选项参考](../../db/d05/tutorial_config_reference.html) 了解配置选项文档。

## 安装编译器和构建工具

  * 编译 OpenCV 需要 C++ 编译器。通常使用 G++/GCC 或 Clang/LLVM：
    * 安装 GCC...

sudo apt install -y g++

    * ...或 Clang：

sudo apt install -y clang

  * OpenCV 使用 CMake 构建配置工具：

sudo apt install -y cmake

  * CMake 可以为不同的构建系统生成脚本，例如 _make_、_ninja_：
    * 安装 Make...

sudo apt install -y make

    * ...或 Ninja：

sudo apt install -y ninja-build

  * 安装获取和解压源码的工具：
    * _wget_ 和 _unzip_...

sudo apt install -y wget unzip

    * ...或 _git_：

sudo apt install -y git

## 下载源码

获取 OpenCV 源码有两种方法：

  * 使用浏览器或任何下载工具下载仓库快照（约 80-90MB）并解压...

wget -O opencv.zip https://github.com/opencv/opencv/archive/4.x.zip

unzip opencv.zip

mv opencv-4.x opencv

  * ...或使用 _git_ 将仓库克隆到本地以获取完整变更历史（>470MB）：

git clone https://github.com/opencv/opencv.git

git -C opencv checkout 4.x

> 注意：其他分支、发布版本或提交的快照可以在 [GitHub](https://github.com/opencv/opencv) 和 [官方下载页面](https://opencv.org/releases) 上找到。

## 配置和构建

  * 创建构建目录：

mkdir -p build && cd build

  * 配置——为首选构建系统生成构建脚本：
    * 使用 _make_...

cmake ../opencv

    * ...或使用 _ninja_：

cmake -GNinja ../opencv

  * 构建——运行实际编译过程：
    * 使用 _make_...

make -j4

    * ...或 _ninja_：

ninja

> 注意：_配置_ 过程可能会从互联网下载一些文件以满足库依赖，连接失败可能导致某些模块或功能被关闭或行为不同。详情请参阅 [OpenCV 安装概述](../../d0/d3d/tutorial_general_install.html) 和 [OpenCV 配置选项参考](../../db/d05/tutorial_config_reference.html) 教程。
> 如果构建过程遇到问题，请尝试清理或重建构建目录。禁用依赖项、修改构建脚本或将源码切换到其他分支等配置更改无法很好地处理，可能导致工作区损坏。
> _Make_ 可以并行运行多个编译进程，`-j<NUM>` 选项表示"同时运行 <NUM> 个任务"。_Ninja_ 会自动检测可用处理器核心数量，不需要 `-j` 选项。

## 检查构建结果

构建成功后，你将在 `build/lib` 目录中找到库文件，在 `build/bin` 目录中找到可执行文件（测试、示例、应用程序）：

ls bin

ls lib

CMake 包文件将位于构建根目录：

ls OpenCVConfig*.cmake

ls OpenCVModules.cmake

## 安装

> 警告：安装过程仅将文件复制到预定义位置并进行少量修补。使用此方法安装不会将 OpenCV 集成到系统包注册表中，因此例如无法自动卸载 OpenCV。由于可能与系统包发生冲突，我们不建议普通用户进行系统级安装。

默认情况下，OpenCV 将安装到 `/usr/local` 目录，所有文件将被复制到以下位置：

  * `/usr/local/bin` \- 可执行文件
  * `/usr/local/lib` \- 库文件（.so）
  * `/usr/local/cmake/opencv4` \- CMake 包
  * `/usr/local/include/opencv4` \- 头文件
  * `/usr/local/share/opencv4` \- 其他文件（如 XML 格式的训练级联分类器）

由于 `/usr/local` 由 root 用户拥有，安装需要使用提升权限（`sudo`）执行：

sudo make install

或

sudo ninja install

安装根目录可以通过 `CMAKE_INSTALL_PREFIX` 配置参数更改，例如 `-DCMAKE_INSTALL_PREFIX=$HOME/.local` 以安装到当前用户的本地目录。安装布局可以通过 `OPENCV_*_INSTALL_PATH` 参数更改。详情请参阅 [OpenCV 配置选项参考](../../db/d05/tutorial_config_reference.html)。

* * *
