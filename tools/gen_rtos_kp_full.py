#!/usr/bin/env python3
"""Generate complete kp_rtos.json for Mastering the FreeRTOS Real-Time Kernel."""
import json

S = {}

# ==================== Chapter 1 ====================

S["1.1"] = {
    "core": [
        "多任务系统让MCU单核交替执行多个任务,营造同时运行的假象",
        "实时系统对外部事件的响应具有时间确定性,必须在截止期限内完成",
        "硬实时(Hard Real-Time)错过截止期限=系统失败;软实时(Soft Real-Time)允许偶尔超时",
        "裸机while(1)大循环不是多任务——所有任务共享同一个栈,没有独立上下文",
        "RTOS内核是一个管理多任务执行顺序和资源的系统软件层",
        "Context Switch(上下文切换)是RTOS核心开销——保存/恢复任务寄存器"
    ],
    "background": [
        "你已有STM32裸机经验,理解中断响应和定时器——RTOS在此基础上增加任务调度层",
        "STM32的SysTick硬件定时器为FreeRTOS提供Tick心跳时钟源,驱动任务调度"
    ],
    "understand": [
        "FreeRTOS是市场占有率最高的嵌入式RTOS之一,MIT开源许可",
        "多任务系统的任务数理论上只受RAM限制(每个任务需要独立栈空间)"
    ]
}

S["1.1.1"] = {
    "core": [
        "FreeRTOS Kernel是轻量级实时内核,提供任务调度/IPC/内存管理等核心功能",
        "FreeRTOS由Richard Barry主导开发,现由Amazon FreeRTOS团队维护",
        "FreeRTOS内核最小ROM占用约4-9KB,适合ROM/RAM受限的MCU",
        "FreeRTOS源代码用C编写,可移植到40+处理器架构"
    ],
    "background": ["与裸机开发相比,FreeRTOS提供标准化的多任务API,避免每次从头设计任务调度逻辑"],
    "understand": ["Amazon FreeRTOS在FreeRTOS内核基础上增加了云连接库(MQTT/HTTPS)"]
}

S["1.1.2"] = {
    "core": [
        "FreeRTOS价值:缩短嵌入式多任务系统开发周期",
        "提供标准化的任务间通信和同步机制(Queue/Semaphore/Mutex)",
        "抢占式调度确保高优先级任务在可控延迟内得到CPU",
        "任务隔离防止单任务崩溃拖垮整个系统(与裸机共用栈不同)",
        "代码可移植性强——应用代码在不同MCU间迁移时只需重编移植层"
    ],
    "background": [
        "裸机中新增外设功能往往需要重构主循环——RTOS中只需创建新任务",
        "裸机中断响应延迟取决于最长关中断时间;RTOS中取决于ISR函数的最长执行时间"
    ],
    "understand": ["FreeRTOS广泛应用于消费电子、工业控制、汽车电子和IoT设备"]
}

S["1.1.3"] = {
    "core": [
        "Task(任务):独立无限循环程序片段,拥有自己的栈和TCB",
        "TCB(Task Control Block):内核维护每个任务的状态/优先级/栈指针等元数据",
        "Scheduler(调度器):决定哪个就绪任务获得CPU的内核组件",
        "Tick:RTOS的心跳中断,每个Tick触发调度器评估是否需要切换任务",
        "Critical Section(临界区):需要互斥访问的代码段,通常通过关中断保护"
    ],
    "background": [
        "裸机中上下文只有一个——main函数执行流;RTOS中每个任务有独立上下文"
    ],
    "understand": ["PendSV异常在ARM Cortex-M上用于触发上下文切换——利用其可悬起特性"]
}

S["1.1.4"] = {
    "core": [
        "裸机while(1)大循环三大痛点:实时性难以保证、代码难以复用、功能难以扩展",
        "RTOS将复杂系统拆分为多个独立任务,降低代码耦合度",
        "任务隔离——一个任务栈溢出不影响其他任务正常运行",
        "RTOS提供标准化同步原语避免竞态条件(Race Condition)",
        "RTOS让开发者从'什么时候执行什么'中解放,专注'每个任务做什么'"
    ],
    "background": [
        "裸机中所有模块共享同一个栈——局部变量过多会导致全局栈溢出",
        "裸机新增功能需仔细插入主循环时间片——RTOS中只需创建新任务并设置优先级"
    ],
    "understand": ["RTOS不是银弹——简单系统(单功能LED/按键)用RTOS反而增加复杂度和开销"]
}

S["1.1.5"] = {
    "core": [
        "抢占式调度:高优先级任务就绪时立即抢占低优先级任务",
        "协作式调度:任务主动让出CPU才发生切换",
        "队列(Queue):任务间线程安全的数据传递机制(FIFO,按值拷贝)",
        "信号量(Semaphore):任务间/ISR与任务间的事件通知机制",
        "互斥锁(Mutex):带优先级继承的二进制信号量,用于保护共享资源",
        "软件定时器(Software Timer):基于Tick计数实现的可配置定时回调",
        "事件组(Event Group):任务等待多个事件位的AND/OR组合",
        "任务通知(Task Notification):轻量级一对一同步机制"
    ],
    "background": [
        "这些特性在裸机中需开发者从头实现——RTOS提供标准化API",
        "FreeRTOS所有特性设计目标:最小RAM占用、确定行为、可配置裁剪"
    ],
    "understand": [
        "FreeRTOS还支持Stream Buffer、Message Buffer等较新IPC机制",
        "每个特性通过FreeRTOSConfig.h中的宏裁剪,节省ROM"
    ]
}

S["1.1.6"] = {
    "core": [
        "FreeRTOS使用MIT开源许可证,允许免费用于商业闭源产品",
        "开源意味着可查看和修改内核源码,理解每个API底层实现",
        "FreeRTOS内核代码有严格编码规范和统一代码风格",
        "许可证要求:在软件文档中保留FreeRTOS版权声明"
    ],
    "background": [
        "与GPL不同,MIT许可不要求衍生作品开源——适合商业嵌入式产品"
    ],
    "understand": ["Amazon FreeRTOS增加了OTA/AWS IoT集成等额外组件"]
}

S["1.2"] = {
    "core": [
        "FreeRTOS源码发布包含:内核核心源文件、移植层(Port Layer)、示例工程",
        "FreeRTOS/Source/目录是内核核心代码,包含task.c/queue.c/timers.c等",
        "移植层(portable/)包含与特定编译器/MCU相关的适配代码",
        "每个官方发行版附带多个MCU平台的Demo项目供快速上手"
    ],
    "background": [
        "从裸机到RTOS需理解移植层概念——裸机直接操作硬件寄存器,RTOS移植层封装硬件差异",
        "获取示例工程比从零搭建项目更高效——官方Demo已配置好FreeRTOSConfig.h和启动文件"
    ],
    "understand": ["FreeRTOS官网(www.freertos.org)提供完整API文档和示例"]
}

S["1.2.1"] = {
    "core": [
        "示例项目可在多种开发板上直接编译运行(STM32 Discovery/LPCXpresso等)",
        "示例项目展示了FreeRTOS最小系统所需的所有文件配置",
        "从官方示例复制FreeRTOSConfig.h作为项目起点是最佳实践",
        "示例工程通常包含多个任务的简单演示(LED闪烁/串口打印等)"
    ],
    "background": [
        "运行示例工程是验证开发环境搭建正确的最快方式",
        "STM32平台的Demo使用HAL或标准外设库,与已有STM32经验一致"
    ],
    "understand": ["FreeRTOS也提供Windows模拟器版本,可在PC上调试RTOS应用"]
}

# ==================== Chapter 2 ====================

S["2.1"] = {
    "core": [
        "FreeRTOS内核源码通过解压官方ZIP包获得",
        "理解分布结构是正确搭建FreeRTOS项目的前提",
        "每个Demo项目已完成FreeRTOSConfig.h配置、启动代码和链接脚本集成",
        "从Demo入手能避免从零搭建时的文件遗漏和配置错误"
    ],
    "background": ["STM32裸机项目需自行配置启动文件和链接脚本——RTOS项目在此基础上增加内核源码引用"],
    "understand": ["FreeRTOS Ziplib/目录已被弃用,不再需要引入"]
}

S["2.2"] = {
    "core": [
        "FreeRTOS发行版包含:Source/(内核源码)、Demo/(示例项目)、License/(许可证文件)",
        "Source/目录是所有FreeRTOS项目的核心,必须包含",
        "Demo/目录提供各平台参考实现,用于学习和快速启动",
        "FreeRTOSConfig.h是内核配置唯一入口,裁剪功能以节省ROM/RAM"
    ],
    "background": ["与STM32裸机中stm32xxxx.h类似,FreeRTOSConfig.h是内核配置头文件"],
    "understand": ["FreeRTOS发行版每个大版本下包含多子目录对应不同MCU系列"]
}

S["2.2.1"] = {
    "core": [
        "Port(移植层)是连接FreeRTOS内核与特定MCU/编译器的桥梁",
        "移植层负责三件核心工作:上下文切换、Tick中断管理、临界区进出",
        "每个硬件平台需要特定的移植层文件(port.c/portmacro.h)",
        "ARM Cortex-M3/M4移植层位于portable/GCC/ARM_CM3/或ARM_CM4F/"
    ],
    "background": [
        "裸机直接操作SCB/NVIC等寄存器——FreeRTOS移植层封装这些操作",
        "不同编译器(GCC/IAR/KEIL)需不同移植层文件,因为内联汇编语法不同"
    ],
    "understand": ["Cortex-M系列利用SVC启动第一个任务,PendSV执行后续上下文切换"]
}

S["2.2.2"] = {
    "core": [
        "构建FreeRTOS需将Source/下所有.c文件加入工程(排除非目标平台的portable/)",
        "只需包含目标平台的移植层文件:port.c + portmacro.h",
        "heap_x.c根据项目需求选择一种(heap_1~heap_5)加入工程",
        "FreeRTOSConfig.h必须放在编译器的include path中"
    ],
    "background": ["STM32裸机项目需包含startup和外设库文件——RTOS额外增加约10个内核文件"],
    "understand": ["heap_x.c文件位于portable/MemMang/,同一时间只能有一个heap实现"]
}

S["2.2.3"] = {
    "core": [
        "FreeRTOSConfig.h是FreeRTOS配置核心,所有功能裁剪通过宏定义控制",
        "关键配置:configTICK_RATE_HZ(Tick频率)、configUSE_PREEMPTION(是否抢占)",
        "内存相关:configTOTAL_HEAP_SIZE(heap总量)、configMINIMAL_STACK_SIZE(最小栈)",
        "功能开关:configUSE_QUEUE_SETS/configUSE_TIMERS/configUSE_MUTEXES等",
        "configMAX_PRIORITIES定义优先级数量(非最大值),影响RAM使用",
        "configSUPPORT_STATIC_ALLOCATION启用静态分配,不依赖heap"
    ],
    "background": [
        "STM32裸机用SystemCoreClock和SysTick_Config()配置时钟——configTICK_RATE_HZ对应SysTick频率",
        "错误的configTOTAL_HEAP_SIZE导致运行时内存分配失败——需用xPortGetFreeHeapSize()调试"
    ],
    "understand": ["configASSERT()宏在调试阶段应启用——帮助捕获API参数错误"]
}

S["2.2.4"] = {
    "core": [
        "FreeRTOS官方发行版定期发布(LTS和标准版本),包含经过测试的稳定代码",
        "每个发行版包含Release Notes说明新特性/Bug修复/已知问题",
        "官方发行版包含已验证的Demo工程,与对应MCU开发板配套",
        "长期支持版(LTS)提供更长时间的安全更新和Bug修复"
    ],
    "background": ["裸机代码通常固定使用某个HAL库版本——FreeRTOS也依赖版本匹配的移植层"],
    "understand": ["FreeRTOSv202604.00-LTS是当前使用版本,基于FreeRTOS Kernel V10.x"]
}

S["2.2.6"] = {
    "core": [
        "所有FreeRTOS项目必须包含的通用源文件:task.c/list.c/queue.c",
        "task.c:任务创建/删除/调度/延时等核心功能",
        "list.c:内核链表实现,用于就绪列表/延迟列表等内部数据结构",
        "queue.c:队列和信号量(信号量基于队列实现)",
        "按需包含:timers.c/event_groups.c/stream_buffer.c"
    ],
    "background": ["裸机不需要这些基础设施——RTOS内核本身就是精心设计的软件架构"],
    "understand": ["croutine.c(协程)是FreeRTOS轻量级替代方案,已不推荐新项目使用"]
}

S["2.2.7"] = {
    "core": [
        "移植层文件分两大类:port.c(C/汇编实现)和portmacro.h(类型定义和宏)",
        "port.c包含:启动第一个任务(prvStartFirstTask)/上下文切换(xPortPendSVHandler)",
        "portmacro.h定义:TickType_t/BaseType_t/临界区宏(portENTER_CRITICAL等)",
        "ARM Cortex-M使用PendSV+SVC;M4F相比M3增加浮点寄存器保存/恢复(FPU上下文)"
    ],
    "background": [
        "裸机CPU寄存器保存/恢复仅在中断进出时发生——RTOS在每次任务切换时发生",
        "Cortex-M4F的FPU上下文切换增加约200字节栈开销——任务栈设计时必须考虑"
    ],
    "understand": ["Lazy Stacking是Cortex-M3/M4硬件特性,减少中断响应时的寄存器压栈开销"]
}

S["2.2.8"] = {
    "core": [
        "FreeRTOSConfig.h必须位于编译器Include Path中",
        "Source/include/目录包含所有公共头文件(FreeRTOS.h/task.h/queue.h等)",
        "移植层的portmacro.h通过FreeRTOS.h中的路径包含",
        "应用代码只需包含FreeRTOS.h和具体功能头文件(如task.h/queue.h)"
    ],
    "background": ["STM32裸机工程需包含stm32f4xx.h等外设头文件——RTOS额外增加FreeRTOS头文件路径"],
    "understand": ["FreeRTOSConfig.h中的#ifdef __ICCARM__等预编译指令兼容多编译器"]
}

S["2.2.9"] = {
    "core": [
        "应用代码包含头文件的规范顺序:FreeRTOS.h → 功能模块头文件(task.h/queue.h等)",
        "FreeRTOS.h自动包含portmacro.h",
        "功能头文件主要提供API函数声明和常量定义",
        "FreeRTOS.h中通过FreeRTOSConfig.h的配置宏决定哪些功能模块被编译"
    ],
    "background": ["裸机包含stm32f4xx.h后可操作所有外设寄存器——FreeRTOS头文件分层更精细"],
    "understand": ["projdefs.h定义了pdTRUE/pdFALSE/pdPASS/pdFAIL等常用常量"]
}

S["2.3"] = {
    "core": [
        "FreeRTOS官方Demo是验证移植和配置正确性的最快途径",
        "Demo工程展示完整RTOS项目结构:main.c/FreeRTOSConfig.h/启动文件/链接脚本",
        "运行Demo可确认:Tick中断正常、任务切换发生、空闲任务运行",
        "Demo工程也是学习FreeRTOS API用法的参考代码"
    ],
    "background": ["从裸机到RTOS第一步不是写应用代码——而是跑通Demo确认环境配置正确"],
    "understand": ["FreeRTOS Demo中通常包含多个标准测试任务用于验证内核功能完整性"]
}

S["2.4"] = {
    "core": [
        "创建FreeRTOS项目有两种方法:基于Demo修改、从零手动配置",
        "基于Demo修改:复制Demo目录,修改FreeRTOSConfig.h和任务代码(推荐方式)",
        "从零配置:手动添加所有源文件路径/Include Path/链接脚本修改",
        "必须为Idle Task和Timer Task预留栈空间(在FreeRTOSConfig.h中配置)"
    ],
    "background": ["STM32CubeMX可集成FreeRTOS——但理解手动配置有助于排查问题"],
    "understand": ["FreeRTOS BSP帮助文件在Demo/Common/目录中供参考"]
}

S["2.4.1"] = {
    "core": [
        "根据目标MCU选择最接近的Demo作为起点(如STM32F4选Cortex-M4 Demo)",
        "修改FreeRTOSConfig.h匹配目标板资源(时钟频率/内存大小/外设)",
        "替换Demo中外设初始化代码为目标板的外设初始化",
        "逐步替换Demo任务为应用任务,每次替换后验证功能"
    ],
    "background": ["STM32不同系列(F1/F4/F7/H7)移植层文件相同,差异在外设驱动"],
    "understand": ["中断优先级分组必须与FreeRTOS要求一致——通常4位抢占优先级"]
}

S["2.4.2"] = {
    "core": [
        "从零创建需准备:FreeRTOSConfig.h/main.c/链接脚本/启动文件",
        "需添加的源文件:所有内核通用文件+目标移植层+一种heap实现",
        "configCPU_CLOCK_HZ必须匹配MCU实际时钟频率",
        "SysTick中断优先级必须设为FreeRTOS允许的最低优先级(configKERNEL_INTERRUPT_PRIORITY)"
    ],
    "background": ["SysTick优先级设置错误是RTOS系统不工作的首要原因——Cortex-M上数值越小优先级越高"],
    "understand": ["FreeRTOS的portable/目录含常见编译器和MCU的预配置启动文件参考"]
}

S["2.5"] = {
    "core": [
        "FreeRTOS定义独特命名规范:变量前缀表示类型(x=结构体,u=unsigned,p=pointer)",
        "函数返回值类型通过前缀标注(pdPASS/pdFAIL)",
        "TickType_t根据配置决定16位或32位——影响延时最大值和精度",
        "BaseType_t对应MCU最自然的整数宽度(Cortex-M上为32位)"
    ],
    "background": ["裸机代码通常无严格命名规范——FreeRTOS命名规范有助于一眼看出变量类型"],
    "understand": ["FreeRTOS命名规范源于嵌入式系统需精确控制数据类型大小的需求"]
}

S["2.5.1"] = {
    "core": [
        "FreeRTOS重定义基本数据类型(TickType_t/BaseType_t),不直接使用C标准类型",
        "目的:保证跨平台移植时数据类型大小一致性",
        "portmacro.h中定义这些类型到编译器类型的映射",
        "应用代码应尽量使用FreeRTOS定义的类型而非标准C类型"
    ],
    "background": ["移植到新平台时只需修改portmacro.h中的类型定义,应用代码无需改动"],
    "understand": ["portCHAR/portSHORT/portLONG等基础类型别名也定义在portmacro.h中"]
}

S["2.5.2"] = {
    "core": [
        "TickType_t是FreeRTOS的Tick计数值类型——用于延时和超时参数",
        "configTICK_TYPE_WIDTH_IN_BITS决定TickType_t是16位还是32位",
        "16位TickType_t的portMAX_DELAY约65535个Tick;32位约4.29e9个Tick",
        "RAM受限的8位MCU应使用16位TickType_t以节省TCB成员空间"
    ],
    "background": ["STM32F4是32位MCU——TickType_t默认32位,portMAX_DELAY接近无限期阻塞"],
    "understand": ["configUSE_16_BIT_TICKS在8位和16位MCU上启用减小RAM占用"]
}

S["2.5.3"] = {
    "core": [
        "BaseType_t定义为MCU架构最高效的整数类型(Cortex-M上为long,32位)",
        "BaseType_t用于布尔值/错误码/计数等频繁使用场景",
        "返回值为pdTRUE/pdFALSE的API使用BaseType_t",
        "UBaseType_t是BaseType_t的无符号版本"
    ],
    "background": ["STM32(ARM Cortex-M)上是32位——BaseType_t和int等效"],
    "understand": ["BaseType_t也是configSTACK_DEPTH_TYPE的基础类型"]
}

S["2.5.4"] = {
    "core": [
        "大多数返回BaseType_t的API用pdPASS(0)表示成功,pdFAIL表示失败",
        "pdTRUE(1)和pdFALSE(0)用于条件判断型API",
        "检查返回值是嵌入式开发基本习惯——FreeRTOS API调用后应始终检查返回值",
        "内存分配失败(errCOULD_NOT_ALLOCATE_REQUIRED_MEMORY)是常见返回值错误"
    ],
    "background": ["裸机函数通常返回void或int——FreeRTOS统一使用pdPASS/pdFAIL便于错误链检查"],
    "understand": ["部分API(如xQueueReceive)超时特性使其在portMAX_DELAY时永不返回错误"]
}

S["2.5.5"] = {
    "core": [
        "变量命名前缀:x=结构体/u=unsigned/p=pointer/c=char/s=string(pc=char*,px=结构体指针)",
        "pv=void指针;v=void;uc=unsigned char;ux=unsigned BaseType_t",
        "命名规范帮助代码阅读者从变量名直接推断类型"
    ],
    "background": ["裸机代码变量名通常只反映业务含义——FreeRTOS通过前缀暴露变量类型"],
    "understand": ["prv前缀表示私有(private)函数,应用代码不应直接调用"]
}

S["2.5.6"] = {
    "core": [
        "函数名前缀规则:vTaskFunction(返回值类型+所属模块+功能名)",
        "API函数名使用PascalCase(如xQueueCreate/xTaskCreate)",
        "私有函数(static)以prv开头(如prvIdleTask)",
        "FromISR后缀表示ISR安全版本(如xQueueSendToBackFromISR)"
    ],
    "background": ["裸机函数命名自定——FreeRTOS统一命名规范有助于一眼区分Task/Queue/ISR API"],
    "understand": ["API函数名x前缀表示返回BaseType_t或非标准类型"]
}

# ==================== Chapter 3 ====================

S["3.1"] = {
    "core": [
        "RTOS需要在运行时动态创建内核对象(任务/队列/信号量)——需要内存分配机制",
        "标准C库malloc()在嵌入式MCU中不一定可用(线程安全/碎片不确定)",
        "FreeRTOS提供多个heap实现方案(heap_1~heap_5),各有不同性能和碎片特性",
        "所有heap实现位于portable/MemMang/目录,同一时间只能选择一个",
        "FreeRTOS不提供动态内存释放后的碎片整理——设计时需考虑内存预算"
    ],
    "background": [
        "裸机开发中内存分配通常是静态的(全局变量/固定数组)——不需要动态分配",
        "裸机的全局变量分配在BSS段,大小编译时确定——RTOS动态对象分配在heap区域"
    ],
    "understand": [
        "heap区域在启动时从主RAM中划出一块连续区域作为FreeRTOS堆空间",
        "configTOTAL_HEAP_SIZE决定heap总大小——过小导致分配失败,过大浪费RAM"
    ]
}

S["3.2"] = {
    "core": [
        "五种heap方案核心区别:是否支持释放/是否合并碎片/是否支持多RAM区域",
        "选择指南:简单系统用heap_1,通用场景用heap_4,多RAM区域用heap_5",
        "heap_2已被heap_4取代(heap_4包含heap_2功能并增加碎片合并)",
        "heap_3封装编译器自带的malloc/free——线程安全取决于编译器实现"
    ],
    "background": ["STM32项目总RAM有限——heap大小需与全局变量/栈空间统筹分配"],
    "understand": ["heap实现选择不影响应用API——所有API使用同样的pvPortMalloc/vPortFree接口"]
}

S["3.2.1"] = {
    "core": [
        "heap_1:最简单的分配器——只能分配,不能释放",
        "内部维护nextFreeByte地址指针,每次分配指针后移——O(1)确定时间",
        "适用场景:项目不需要动态删除任务(任务数固定)",
        "最适合安全关键系统——确定行为+最小化代码复杂度"
    ],
    "background": ["裸机静态全局数组分配与heap_1行为类似——所有资源初始化时确定"],
    "understand": ["heap_1实现代码约80行C代码,是理解FreeRTOS内存管理的起点"]
}

S["3.2.2"] = {
    "core": [
        "heap_2:可释放但不合并相邻空闲块——已被heap_4取代",
        "使用Best-Fit算法:寻找大小最匹配的空闲块",
        "碎片问题:多次分配释放后产生不可合并碎片(即使相邻)",
        "不推荐新项目使用——直接使用功能等同但更好的heap_4"
    ],
    "background": ["heap_2不能合并相邻空闲块的缺陷在长时间运行系统中尤为致命"],
    "understand": ["heap_2代码在FreeRTOS 10.x版本后标记为过时"]
}

S["3.2.3"] = {
    "core": [
        "heap_3:简单封装标准C库malloc()/free(),通过挂起调度器保证线程安全",
        "依赖编译器提供的标准库实现(newlib/musl等)——行为因编译器而异",
        "heap_3的堆空间来自链接脚本中的Heap_Size设置——而非configTOTAL_HEAP_SIZE",
        "适用场景:项目已在使用标准malloc,或需要realloc等功能"
    ],
    "background": ["STM32裸机设置Heap_Size=0——RTOS中使用heap_3时需确保Heap_Size足够"],
    "understand": ["newlib(GCC嵌入式工具链常用)的malloc在heap_3中线程安全由挂起调度器保证"]
}

S["3.2.4"] = {
    "core": [
        "heap_4:最推荐的通用方案——支持释放并合并相邻空闲块",
        "使用Best-Fit算法从空闲列表查找合适块",
        "插入排序维护空闲列表(按地址升序)——释放时与前/后块合并",
        "所有FreeRTOS官方Demo中heap_4是默认选择",
        "适用场景:绝大多数需要动态分配/释放的FreeRTOS项目"
    ],
    "background": [
        "heap_4中合并是释放时关键操作——连续释放相邻地址后合并为更大空闲块",
        "即使使用heap_4,长期运行系统仍可能有碎片——监控xPortGetMinimumEverFreeHeapSize()"
    ],
    "understand": ["heap_4使用end指针标记heap区域结束边界"]
}

S["3.2.5"] = {
    "core": [
        "heap_5:在heap_4基础上支持跨多个非连续RAM区域分配",
        "需在使用任何动态分配API前调用vPortDefineHeapRegions()初始化各区域",
        "每个区域由起始地址和大小定义,按地址升序排列,以{NULL,0}结尾",
        "适用场景:MCU有多个不连续RAM块(如DTCM+SRAM+SDRAM)"
    ],
    "background": [
        "STM32F7/H7有多个RAM区域——heap_5可统一管理",
        "vPortDefineHeapRegions()必须在vTaskStartScheduler()之前调用且只调用一次"
    ],
    "understand": ["heap_5无法合并不同区域的空闲块——跨区域碎片无法处理"]
}

S["3.3"] = {
    "core": [
        "xPortGetFreeHeapSize():返回当前未分配heap字节数",
        "xPortGetMinimumEverFreeHeapSize():返回启动以来最少空闲heap字节数",
        "pvPortMalloc()和vPortFree()是FreeRTOS内部使用的内存分配/释放接口",
        "空闲heap监控是嵌入式系统长时间运行测试的必要部分"
    ],
    "background": ["裸机通过查看全局变量数组使用情况估算内存——RTOS提供标准化接口"],
    "understand": ["Malloc Failed Hook可在分配失败时触发调试断点"]
}

S["3.4"] = {
    "core": [
        "静态内存分配在编译时确定所有资源——不使用heap_1~heap_5",
        "启用方法:FreeRTOSConfig.h中设置configSUPPORT_STATIC_ALLOCATION为1",
        "使用静态分配时,对象创建API改为xTaskCreateStatic()/xQueueCreateStatic()等",
        "需为Idle Task和Timer Daemon Task提供静态TCB和栈",
        "适合航空/汽车/医疗等安全关键领域——避免运行时分配失败风险"
    ],
    "background": [
        "裸机天然使用静态分配——RTOS静态分配是回归裸机思维",
        "安全标准(如MISRA C/IEC 61508)倾向静态分配,避免动态内存不可预测行为"
    ],
    "understand": ["静态分配不意味不使用heap——只是内核对象内存由用户提供而非从heap分配"]
}

# ==================== Chapter 4 ====================

S["4.1"] = {
    "core": [
        "任务是FreeRTOS中可被调度的独立执行单元——每个任务有独立栈空间和TCB",
        "任务函数标准原型:void vTaskFunction(void *pvParameters)",
        "任务函数通常是无限循环(for(;;)或while(1))——返回意味着任务被自动删除",
        "TCB存储任务完整上下文:寄存器状态、栈指针、优先级等",
        "裸机的main()函数是单任务——所有代码共享一个栈"
    ],
    "background": [
        "裸机while(1)独占CPU——RTOS中每个任务while(1)在调用阻塞API时自动让出CPU",
        "多任务代价:每个任务需独立栈空间——RAM大小决定可创建任务数量"
    ],
    "understand": ["TCB占用RAM约40-80字节(取决于配置)——创建大量任务时需计入TCB内存开销"]
}

S["4.2"] = {
    "core": [
        "任务函数必须永不返回的无限循环——或调用vTaskDelete(NULL)自我终止",
        "任务函数不接受参数时参数应设为NULL——pvParameters是void*类型",
        "任务函数内部局部变量存储在任务栈上(不是全局栈)",
        "如果任务函数return,必须调用vTaskDelete(NULL)——否则触发configASSERT"
    ],
    "background": ["裸机函数return返回调用者——RTOS任务return触发prvDeleteTask是正常清理流程"],
    "understand": ["进入任务函数前,调度器已通过prvPortStartFirstTask()恢复任务初始寄存器状态"]
}

S["4.3"] = {
    "core": [
        "RTOS任务四种主要状态:Running、Ready、Blocked、Suspended",
        "Running:当前正在执行的任务——每个CPU核任意时刻只有一个Running任务",
        "Ready:已就绪可被调度但尚未获得CPU的任务",
        "Blocked:等待事件(延时到期/队列非空/信号量可用)而不可执行的任务",
        "Suspended:通过vTaskSuspend()显式挂起,只能vTaskResume()恢复",
        "裸机的等待就是while(flag==0)空转——RTOS的Blocked不消耗CPU"
    ],
    "background": [
        "裸机中delay_ms(100)通过SysTick忙等——RTOS的vTaskDelay(100)让任务进入Blocked,CPU执行其他任务",
        "理解任务状态转换是所有FreeRTOS开发的基础——必须能手画状态转换图"
    ],
    "understand": ["状态转换:延时到期→Blocked→Ready→调度→Running;信号量Give→Blocked→Ready"]
}

S["4.4"] = {
    "core": [
        "xTaskCreate()是创建任务的标准动态API,返回pdPASS/pdFAIL",
        "参数:任务函数指针/task name(调试用)/栈深度(字,非字节)/pvParameters/优先级/TaskHandle指针",
        "栈深度以字(word)为单位,非字节——栈大小=栈深度×sizeof(StackType_t)",
        "TaskHandle用于后续引用该任务(删除/挂起/通知等),不需要时传NULL",
        "任务创建成功后立即进入Ready状态,等待调度器分配CPU"
    ],
    "background": [
        "裸机中不需要创建任务——RTOS中xTaskCreate()是最常用的API之一",
        "不检查xTaskCreate返回值是初学者常见错误——任务未创建但后续代码仍向其发数据"
    ],
    "understand": ["任务名仅用于调试(如vTaskList()),长度受configMAX_TASK_NAME_LEN限制"]
}

S["4.4.1"] = {
    "core": [
        "xTaskCreate()参数详解:pcName仅用于调试,pvParameters传递给任务函数的void*参数",
        "uxPriority必须小于configMAX_PRIORITIES(有效值0~configMAX_PRIORITIES-1)",
        "pxCreatedTask是输出参数——保存新创建任务的句柄",
        "栈深度估算:任务内所有局部变量+函数调用深度+可能的ISR嵌套,建议至少configMINIMAL_STACK_SIZE"
    ],
    "background": [
        "栈大小估算技巧:先用较大值(如256字),运行后用uxTaskGetStackHighWaterMark()获取实际峰值",
        "STM32F4上configMINIMAL_STACK_SIZE通常设为128字(Cortex-M4F需更大因FPU上下文)"
    ],
    "understand": ["返回errCOULD_NOT_ALLOCATE_REQUIRED_MEMORY表示heap空间不足"]
}

S["4.5"] = {
    "core": [
        "任务优先级范围:0(最低)~configMAX_PRIORITIES-1(最高)",
        "数字越大优先级越高——抢占式调度器总是运行最高优先级的Ready任务",
        "空闲任务优先级为0(最低优先级)",
        "configMAX_PRIORITIES越大,RAM占用越多(每个优先级需维护就绪列表)"
    ],
    "background": [
        "裸机中优先级只在中断控制器(NVIC)中存在——RTOS将优先级概念扩展到任务层",
        "不建议设置过多优先级——通常5-10个足以应对大多数嵌入式场景"
    ],
    "understand": ["相同优先级任务间通过时间片轮转(time slicing)共享CPU"]
}

S["4.6"] = {
    "core": [
        "Tick是RTOS的心跳中断,由硬件定时器(通常SysTick)周期性触发",
        "configTICK_RATE_HZ定义Tick频率(如1000Hz=每1ms一次Tick)",
        "Tick中断中调度器做:更新系统Tick计数、检查延时到期任务、必要时触发上下文切换",
        "Tick频率选择权衡:高频提高时间精度但增加中断开销;低频减少开销但时间粒度粗"
    ],
    "background": [
        "STM32裸机中SysTick用作HAL_Delay()的时基——RTOS同样使用SysTick但用于驱动调度器",
        "configTICK_RATE_HZ=1000时,vTaskDelay(100)延时100ms——延时值=需要等待的Tick数"
    ],
    "understand": ["Cortex-M上SysTick是24位递减计数器,配置为CPU时钟/分频后触发Periodic中断"]
}

S["4.7"] = {
    "core": [
        "vTaskDelay(ticks):将任务阻塞指定Tick数——ticks个Tick后进入Ready",
        "vTaskDelayUntil(&lastWakeTime, period):精确周期延时——用于恒定频率周期任务",
        "Delay和DelayUntil的区别:Delay是相对延时(从现在起),DelayUntil是绝对延时(从上次唤醒起)",
        "用Delay做周期任务会累积漂移(jitter accumulation);DelayUntil不会"
    ],
    "background": [
        "裸机中定时通过while(--delay)空转或定时器中断——RTOS的延时让出CPU给其他任务",
        "裸机中实现精确的1KHz数据采集需定时器中断——RTOS中vTaskDelayUntil可精确到Tick级"
    ],
    "understand": ["portTICK_PERIOD_MS宏将毫秒转换为Tick数(pdMS_TO_TICKS()),方便代码可读性"]
}

S["4.8"] = {
    "core": [
        "空闲任务(Idle Task)是调度器自动创建的最低优先级任务(优先级0)",
        "确保至少有一个任务可运行(当所有任务都阻塞时Idle Task运行)",
        "Idle Task Hook:用户可注册回调函数,在Idle Task中执行低优先级后台工作",
        "Hook函数中不能调用会阻塞IDLE任务的API(如vTaskDelay)"
    ],
    "background": [
        "STM32裸机main()的while(1)空循环=裸机的Idle Task——但RTOS的Idle Task还可执行清理工作",
        "Idle Task负责释放被删除任务的内存(如果任务删除时使用了动态分配)"
    ],
    "understand": ["configIDLE_SHOULD_YIELD控制Idle Task是否在相同优先级就绪时主动让出CPU"]
}

S["4.9"] = {
    "core": [
        "vTaskStartScheduler()启动调度器——从此CPU由调度器管理,永不返回",
        "调用前必须:创建至少一个任务、配置好SysTick、初始化heap",
        "启动流程:创建Idle Task→创建Timer Task(如果启用)→启动SysTick→启动第一个任务",
        "调用后main()函数永远不会继续执行——CPU控制权交给调度器"
    ],
    "background": [
        "裸机中调用HAL_Init()和SystemClock_Config()后进入while(1)——RTOS中最后调用vTaskStartScheduler()",
        "vTaskStartScheduler()调用后看不到main()的返回——因为调度器never returns"
    ],
    "understand": ["如果调度器不能启动,先检查configASSERT是否启用以获取调试信息"]
}

S["4.10"] = {
    "core": [
        "vTaskDelete(NULL):删除自己;vTaskDelete(TaskHandle):删除指定任务",
        "被删除任务的内存(TCB+栈)由Idle Task释放(非立即释放)",
        "任务删除后不能再访问其资源——包括其持有的队列/信号量",
        "被删除任务持有的mutex不会自动释放——可能导致死锁"
    ],
    "background": [
        "裸机中没有任务概念——RTOS中删除任务类似裸机中结束一个模块的执行",
        "任务删除前应释放其持有的所有资源(队列/信号量/分配的内存)"
    ],
    "understand": ["任务删除是异步的——vTaskDelete()调用后当前任务立即停止执行"]
}

S["4.11"] = {
    "core": [
        "vTaskSuspend(handle):挂起任务(从所有状态进入Suspended)",
        "vTaskResume(handle):恢复挂起的任务(从Suspended进入Ready)",
        "vTaskSuspendAll():挂起调度器(禁止任务切换,不禁止中断)",
        "xTaskResumeAll():恢复调度器并执行pending的上下文切换"
    ],
    "background": [
        "裸机中挂起操作对应关中断或标志位阻塞——RTOS提供更精确的任务级挂起",
        "挂起调度器是保护临界区的技术之一(比关中断更轻量,但仅保护任务间竞争)"
    ],
    "understand": ["vTaskSuspendAll()和xTaskResumeAll()需成对使用,支持嵌套(内部计数器)"]
}

S["4.12"] = {
    "core": [
        "vTaskPrioritySet():运行时动态修改任务优先级",
        "uxTaskPriorityGet():获取任务当前优先级",
        "修改优先级可能立即触发任务切换(如果新优先级高于当前任务)",
        "uxTaskGetStackHighWaterMark():获取任务栈使用峰值(剩余空间)",
        "栈水位监测通过检查栈空间中未被覆盖的已知模式实现"
    ],
    "background": [
        "裸机中不会动态调整函数执行优先级——RTOS提供动态优先级调整能力",
        "栈水位值是评估每个任务栈大小是否合理的关键指标——值太小说明栈可能溢出"
    ],
    "understand": ["eTaskStateGet()可查询任务当前状态(Running/Ready/Blocked/Suspended/Deleted)"]
}

# ==================== Chapter 5 ====================

S["5.1"] = {
    "core": [
        "队列(Queue)是FreeRTOS最基础的IPC机制——任务间/ISR与任务间传递数据",
        "队列是FIFO(先进先出)数据结构——先发送的数据先被接收",
        "队列按值拷贝传递——写入队列时拷贝数据值(而非指针),接收方有自己的副本",
        "队列有固定长度(创建时指定),满时发送可阻塞,空时接收可阻塞"
    ],
    "background": [
        "裸机中任务间通信通过全局变量+标志位——无阻塞等待,需轮询检查",
        "队列拷贝数据的代价:大数据量时会增加RAM开销和拷贝时间"
    ],
    "understand": ["队列是线程安全的——多任务同时访问无需额外同步(内核保证原子性)"]
}

S["5.2"] = {
    "core": [
        "xQueueCreate(queueLength, itemSize):创建队列,返回QueueHandle_t",
        "queueLength:队列可容纳的最大数据项数;itemSize:每项的字节大小",
        "创建失败返回NULL(heap不足)——必须检查返回值",
        "xQueueCreateStatic()用静态分配创建队列(需提供队列存储区和结构体内存)"
    ],
    "background": [
        "裸机中环形缓冲区(Circular Buffer)是自制的'队列'——需手动管理读写指针和满/空判断",
        "itemSize=0可创建特殊队列用于信号量实现(不存储数据,仅计信号数)"
    ],
    "understand": ["队列创建消耗的内存=queueLength×itemSize+队列结构体本身(约76字节)"]
}

S["5.3"] = {
    "core": [
        "xQueueSend(queue, data, timeout)/xQueueSendToBack():向队尾发送数据",
        "xQueueSendToFront():向队首发送(高优先级数据可插队)",
        "timeout=0:非阻塞,满则立即返回;timeout=portMAX_DELAY:无限期阻塞直到有空位",
        "xQueueSendFromISR():ISR安全版本,不阻塞(ISR不能阻塞)"
    ],
    "background": [
        "裸机中向环形缓冲写入:写指针递增→如果满则覆盖或丢弃——没有任何阻塞机制",
        "timeout参数是RTOS与裸机开发的关键差异——让等待不再浪费CPU"
    ],
    "understand": ["xQueueOverwrite()只对长度为1的队列有效,直接覆盖(不阻塞)"]
}

S["5.4"] = {
    "core": [
        "xQueueReceive(queue, data, timeout):从队首接收数据",
        "接收后队列中的数据项被移除",
        "timeout=0:非阻塞,空则立即返回pdFALSE;timeout=portMAX_DELAY:无限期阻塞",
        "xQueueReceiveFromISR():ISR安全版本,不阻塞",
        "xQueuePeek():读取但不移除队首数据项"
    ],
    "background": [
        "裸机中从环形缓冲读取:读指针递增→如果空则返回旧数据或0——没有阻塞等待机制",
        "阻塞接收比轮询接收省CPU且响应及时——是RTOS IPC的核心优势"
    ],
    "understand": ["xQueueMessagesWaiting()返回队列中当前等待的数据项数(不消费)"]
}

S["5.5"] = {
    "core": [
        "xQueueSend()如队列满则行为取决于timeout:0→立即返回errQUEUE_FULL",
        "xQueueReceive()如队列空则行为取决于timeout:0→立即返回pdFALSE",
        "portMAX_DELAY:无限期阻塞,永不超时(几乎永远等待)",
        "阻塞时间=timeout个Tick(实际Tick数,非毫秒)",
        "多个任务同时等同一队列时,最高优先级任务先获得数据/空间"
    ],
    "background": [
        "裸机中读空缓冲区或写满缓冲区的处理由开发者决定——无统一机制",
        "多个任务等待同一队列的优先级规则:最高优先级先得到通知"
    ],
    "understand": ["从ISR发送时触发的上下文切换在中断返回时才执行"]
}

S["5.6"] = {
    "core": [
        "队列集(Queue Set):多个队列/信号量组合成一个集合,任务可同时等待集合中任意一个",
        "xQueueCreateSet():创建队列集;xQueueAddToSet():注册队列到集合",
        "xQueueSelectFromSet():阻塞等待集合中任意队列有新数据",
        "队列集减少任务复杂度和Task数量(无需为每个队列创建监听任务)"
    ],
    "background": [
        "裸机中同时监控多个数据源(如多个串口)需要复杂的状态机或轮询——队列集简化此逻辑",
        "相当于POSIX的select()/poll()的多路I/O复用机制的FreeRTOS版"
    ],
    "understand": ["队列集不用时通过configUSE_QUEUE_SETS=0禁用以省ROM"]
}

S["5.7"] = {
    "core": [
        "队列在传输大数据时应传递指针而非拷贝——减少时间和内存开销",
        "传递指针时需注意:发送方和接收方不能同时访问(数据完整性)",
        "流缓冲区(Stream Buffer)和消息缓冲区(Message Buffer)适合流式数据",
        "消息缓冲区适合变长消息传递(如串口接收数据)"
    ],
    "background": [
        "STM32中DMA传输使用指针+长度描述符——RTOS流缓冲区的设计思路类似",
        "传递指针时用信号量同步访问时序——确保接收方读完前发送方不覆盖"
    ],
    "understand": ["流缓冲区设计用于字节流(如传感器数据),消息缓冲区设计用于离散消息(如通信协议包)"]
}

# ==================== Chapter 6 ====================

S["6.1"] = {
    "core": [
        "软件定时器(Software Timer)是基于Tick计数实现的定时器——不需要额外硬件定时器",
        "软件定时器的精度受Tick频率限制——最小精度=1/Tick频率",
        "软件定时器由Timer Daemon Task(定时器守护任务)管理回调函数执行",
        "定时器回调函数在Daemon Task上下文中运行——不是中断上下文"
    ],
    "background": [
        "裸机中所有定时器都是硬件定时器(TIM1-14)——软件定时器不消耗硬件资源",
        "软件定时器精度不如硬件定时器——需要微秒级精度请使用硬件定时器"
    ],
    "understand": ["启用软件定时器需在FreeRTOSConfig.h设置configUSE_TIMERS=1"]
}

S["6.2"] = {
    "core": [
        "xTimerCreate():创建软件定时器,指定周期、是否自动重载、回调函数",
        "One-shot定时器:到期后执行一次即停止;Auto-reload定时器:到期后自动重新启动",
        "定时器创建后不会自动启动——需xTimerStart()手动启动",
        "TimerHandle_t用于后续操作(启动/停止/修改周期)"
    ],
    "background": [
        "裸机硬件定时器需配置预分频/自动重载/中断使能——软件定时器API更简洁",
        "One-shot定时器=裸机的单次定时中断,Auto-reload=裸机的周期定时中断"
    ],
    "understand": ["定时器周期=Timer Period × Tick Period(如100 ticks × 1ms = 100ms)"]
}

S["6.3"] = {
    "core": [
        "Timer Daemon Task自动由调度器创建(如果configUSE_TIMERS=1)",
        "Timer Task优先级在FreeRTOSConfig.h中设置(configTIMER_TASK_PRIORITY)",
        "定时器回调执行在Timer Task上下文中——可调用大多数FreeRTOS API",
        "定时器命令(Start/Stop/Reset)通过队列发送给Timer Task执行"
    ],
    "background": [
        "裸机定时器回调在ISR中执行——不能调用阻塞函数;RTOS定时器回调在Task中执行——更灵活",
        "Timer Task也有栈大小配置(configTIMER_TASK_STACK_DEPTH)——定时器回调中局部变量过大需调整"
    ],
    "understand": ["定时器命令队列默认长度通过configTIMER_QUEUE_LENGTH配置"]
}

S["6.4"] = {
    "core": [
        "xTimerStart(handle, timeout):启动定时器(从当前Tick开始计时)",
        "xTimerStop(handle, timeout):停止定时器",
        "xTimerReset(handle, timeout):复位定时器(重新开始计时)",
        "xTimerChangePeriod(handle, period, timeout):运行时修改定时器周期"
    ],
    "background": [
        "裸机中修改定时器周期需直接操作寄存器——RTOS中通过API安全修改",
        "Start和Reset的区别:Start只能启动停止的定时器;Reset可重新启动运行中的定时器"
    ],
    "understand": ["timeout参数是等待命令发送到Timer Task队列的最长时间,不是定时器本身的超时"]
}

S["6.5"] = {
    "core": [
        "定时器回调函数原型:void vTimerCallback(TimerHandle_t xTimer)",
        "回调中可获取Timer ID(pvTimerGetTimerID)用于区分多个定时器共用一个回调",
        "回调中不应有长时间操作——会阻塞其他定时器的回调执行",
        "回调中可调用大部分FreeRTOS API(在Task上下文中)"
    ],
    "background": [
        "裸机定时器回调是ISR(不可阻塞,极简执行)——RTOS定时器回调在Task中(可阻塞,可调用更多API)",
        "长时间工作在回调中间接执行:在回调中发信号量,Application Task中做实际工作"
    ],
    "understand": ["xTimerIsTimerActive()检查定时器是否在运行;xTimerGetPeriod()获取当前周期"]
}

S["6.6"] = {
    "core": [
        "xTimerStartFromISR()/xTimerStopFromISR():从ISR操作软件定时器",
        "ISR版本不阻塞(不能等待队列空间),返回pdPASS或pdFAIL",
        "ISR版本需要一个额外参数:pxHigherPriorityTaskWoken(用于触发上下文切换)",
        "ISR中操作定时器也是通过队列命令实现——非直接操作"
    ],
    "background": [
        "裸机中定时器操作直接在ISR中配置寄存器——无需任何中间层",
        "pxHigherPriorityTaskWoken参数是FreeRTOS ISR API的通用模式"
    ],
    "understand": ["xTimerPendFunctionCallFromISR():从ISR延迟执行函数(通过Timer Task)"]
}

S["6.7"] = {
    "core": [
        "Timer ID:pvTimerGetTimerID()/vTimerSetTimerID()——给定时器附加用户数据",
        "Timer ID可用于区分同回调的多个定时器,或传递上下文数据",
        "xTimerGetExpiryTime():获取定时器下次到期时的Tick计数值",
        "xTimerGetTimerDaemonTaskHandle():获取Timer Task句柄"
    ],
    "background": [
        "裸机定时器通过TIM句柄区分不同定时器——RTOS通过TimerHandle和Timer ID区分"
    ],
    "understand": ["Timer ID是一个void*指针,可指向任意用户数据结构"]
}

S["6.8"] = {
    "core": [
        "软件定时器不适合:高精度(<Tick周期)定时、硬实时截止期限",
        "适合:后台状态轮询、超时检查、定期状态报告等非实时任务",
        "大量定时器同时到期会增加Timer Task执行时间——影响响应及时性",
        "总结:软件定时器=低精度+Task上下文回调;硬件定时器=高精度+ISR上下文回调"
    ],
    "background": ["裸机开发中不可能有软件定时器的概念——所有定时都是硬件的——这是RTOS带来的新设计维度"],
    "understand": ["软件定时器的节电优势:无额外硬件运行,仅在Tick中断和到期时消耗CPU"]
}

# ==================== Chapter 7 ====================

S["7.1"] = {
    "core": [
        "中断是MCU响应外部/内部事件的机制——RTOS中中断和任务协同工作",
        "ISR(中断服务例程)应尽可能短——将实际处理交给任务",
        "中断优先级:硬件中断优先级(由NVIC控制)vs FreeRTOS任务优先级是不同的概念",
        "FreeRTOS使用中断屏蔽(关中断)保护临界区——不是所有中断都被屏蔽"
    ],
    "background": [
        "裸机中ISR处理所有逻辑——RTOS中ISR只做关键部分(如清标志/读数据),然后通知任务处理",
        "中断和RTOS的关系是理解实时系统设计的关键"
    ],
    "understand": ["Cortex-M中断优先级数值越小优先级越高——与FreeRTOS任务优先级数值语义相反"]
}

S["7.2"] = {
    "core": [
        "FromISR后缀的API可在ISR中安全调用(如xQueueSendToBackFromISR)",
        "不能在ISR中调用任何可能阻塞的API(无FromISR后缀)",
        "FromISR API额外参数:pxHigherPriorityTaskWoken——指示是否需要上下文切换",
        "ISR返回前如pxHigherPriorityTaskWoken==pdTRUE,触发上下文切换"
    ],
    "background": [
        "裸机ISR中不能调用任何RTOS API——RTOS的FromISR API解决了ISR与RTOS的通信问题",
        "ISR中使用FromISR发送数据→任务用普通API接收——两级设计"
    ],
    "understand": ["中断结束时执行的上下文切换是FreeRTOS中断延迟的关键来源"]
}

S["7.3"] = {
    "core": [
        "延迟中断处理(Deferred Interrupt Processing):ISR做最小操作,创建任务做实际处理",
        "方案一:ISR中发送信号量唤醒高优先级处理任务",
        "方案二:ISR中发送队列数据,任务阻塞接收处理",
        "方案三:ISR中调用xTimerPendFunctionCallFromISR()延迟执行函数"
    ],
    "background": [
        "裸机开发中中断处理全在ISR中完成——Long ISR导致中断嵌套/丢失问题",
        "FreeRTOS鼓励Deferred Processing模式——ISR时间最小化=系统响应性最大化"
    ],
    "understand": ["处理任务的优先级应足够高以确保ISR后立即处理——这就是实时响应链"]
}

S["7.4"] = {
    "core": [
        "configKERNEL_INTERRUPT_PRIORITY:FreeRTOS使用的最高逻辑中断优先级",
        "configMAX_SYSCALL_INTERRUPT_PRIORITY:可安全调用FreeRTOS API的最高中断优先级",
        "优先级高于configMAX_SYSCALL_INTERRUPT_PRIORITY的中断不能调用任何FreeRTOS API",
        "在Cortex-M上,中断优先级值越高=优先级越低(数值语义反转)"
    ],
    "background": [
        "裸机中所有中断优先级自定——RTOS要求部分优先级遵守FreeRTOS约定",
        "中断优先级设置错误导致RTOS崩溃的最常见原因——尤其是在FreeRTOS API调用中"
    ],
    "understand": ["NVIC_PriorityGroup_4(4位抢占优先级,0位子优先级)是FreeRTOS推荐配置"]
}

S["7.5"] = {
    "core": [
        "xSemaphoreGiveFromISR():从ISR释放信号量表示事件发生",
        "xQueueSendToBackFromISR()/xQueueSendToFrontFromISR():从ISR向队列发数据",
        "xTaskNotifyFromISR()/vTaskNotifyGiveFromISR():从ISR通知任务",
        "以上API绝不阻塞——ISR中任何阻塞行为都是致命的"
    ],
    "background": [
        "裸机ISR中设置全局标志位→主循环轮询检查——RTOS用信号量/队列替代标志位,消除轮询",
        "FromISR API都返回BaseType_t(或void),通过pxHigherPriorityTaskWoken指示是否需切换"
    ],
    "understand": ["中断中调用API无需显式进入临界区——API内部已在需要时关中断"]
}

S["7.6"] = {
    "core": [
        "中断给RTOS带来的常见问题:中断频率过高导致任务饥饿(无CPU时间)",
        "中断优先级倒置:高优先级任务被低优先级中断阻塞",
        "中断嵌套:Cortex-M支持中断嵌套,但FreeRTOS的一些临界区操作暂时屏蔽特定优先级中断",
        "中断共享:多个中断源共享同一中断线时的仲裁和转发"
    ],
    "background": [
        "裸机中常见的中断优先级倒置是Task Priority不是Interrupt Priority——RTOS中两者都需小心",
        "在ISR中调用printf可能显著增加中断执行时间——调试时常见陷阱"
    ],
    "understand": ["中断负载监控可通过在Idle Task Hook中计数Tick判断CPU空闲度"]
}

S["7.7"] = {
    "core": [
        "xTaskGetTickCount()/xTaskGetTickCountFromISR():获取当前Tick计数值",
        "中断触发时间戳记录:ISR入口读Tick计数→传给任务→任务计算处理延迟",
        "中断延迟测量:ISR触发时刻到任务开始处理的时刻的时间差",
        "用Tick计数辅助调试中断响应时序"
    ],
    "background": [
        "裸机中测量延迟需逻辑分析仪或示波器——RTOS中Tick计数提供软件级时间戳",
        "Tick计数精度取决于Tick频率(1KHz=1ms精度)——微秒级测量需硬件定时器"
    ],
    "understand": ["Tick计数溢出处理:32位TickType_t在1KHz频率下约49.7天溢出"]
}

S["7.8"] = {
    "core": [
        "中断服务例程编写三原则:快速进入、快速处理、快速退出",
        "ISR第一要务:通知任务——不是处理全部逻辑",
        "使用Deferred Processing将耗时操作从ISR移到Task",
        "中断高频率场景用计数型信号量而非逐一触发任务——信号量计数值=待处理次数"
    ],
    "background": [
        "裸机中ISR直接操作所有逻辑因为'没有任务'——RTOS让ISR回归本质:硬件事件捕获",
        "任务化中断处理=引入确定性——ISR延迟可测量,任务处理时间可控"
    ],
    "understand": ["处理任务优先级设置策略:应高于所有消费型任务,低于时间关键型任务"]
}

# ==================== Chapter 8 ====================

S["8.1"] = {
    "core": [
        "信号量(Semaphore)用于事件通知——告知任务某事件已发生",
        "二进制信号量(Binary Semaphore):只有0和1两个值,表示事件是否发生",
        "计数信号量(Counting Semaphore):记录事件发生次数(如累积的中断次数)",
        "信号量和队列的底层实现相同(信号量基于queue.c),但语义不同"
    ],
    "background": [
        "裸机中事件通知=全局标志位volatile uint8_t flag——RTOS信号量提供阻塞等待+优先级继承",
        "信号量是实现Deferred Interrupt Processing的核心机制"
    ],
    "understand": ["xSemaphoreCreateBinary()创建的二进制信号量初始为空(不可用)——需先Give"]
}

S["8.2"] = {
    "core": [
        "xSemaphoreGive()/xSemaphoreGiveFromISR():释放信号量(使可用或计数+1)",
        "xSemaphoreTake(sem, timeout)/xSemaphoreTakeFromISR():获取信号量(阻塞直到可用或超时)",
        "Take二进制信号量成功后值归零(不可用)——必须再次Give才可用",
        "计数信号量Take一次计数减1,Give一次计数加1"
    ],
    "background": [
        "裸机中flag=1→主循环看到flag→处理→手动flag=0——RTOS信号量自动管理计数和阻塞",
        "timeout=portMAX_DELAY时Take永不超时——等效于等待事件发生"
    ],
    "understand": ["uxSemaphoreGetCount()获取计数信号量当前计数值(调试用)"]
}

S["8.3"] = {
    "core": [
        "Mutex(互斥锁)用于互斥访问共享资源——与信号量的语义完全不同",
        "事件=信号量(通知);资源保护=Mutex(互斥)",
        "Mutex是带有优先级继承(Priority Inheritance)的二进制信号量",
        "优先级继承防止优先级反转:低优先级持有Mutex时临时获高优先级直至释放"
    ],
    "background": [
        "裸机中保护共享资源靠关中断——RTOS中Mutex提供更精细的保护(仅互斥访问,不影响中断)",
        "优先级反转是嵌入式系统的经典问题——FreeRTOS Mutex的优先级继承机制自动解决"
    ],
    "understand": ["Recursive Mutex允许同一任务多次Take同一Mutex(需Release对应次数)"]
}

S["8.4"] = {
    "core": [
        "xSemaphoreCreateMutex():创建Mutex(初始可用,自动优先级继承)",
        "Mutex必须由获取它的任务释放——不能跨任务释放(与信号量不同)",
        "xSemaphoreCreateRecursiveMutex():创建递归Mutex",
        "Gatekeeper Task模式:用一个守护任务封装共享资源,其他任务通过队列请求—比直接Mutex更安全"
    ],
    "background": [
        "裸机中I2C/SPI总线共享需要手动管理访问顺序——RTOS中用Mutex保护总线使用权",
        "Mutex的开销:优先级继承逻辑比信号量更复杂,简单场景用信号量+编程规范即可"
    ],
    "understand": ["死锁四个条件:互斥/持有等待/不可剥夺/环路等待——Mutex解决互斥但需编程避免其他三项"]
}

# ==================== Chapter 9 ====================

S["9.1"] = {
    "core": [
        "事件组(Event Group)让任务等待多个事件标志的组合(AND/OR)",
        "每个事件组有configUSE_16_BIT_TICKS决定的位数(8/16/24/32位事件标志)",
        "事件位独立于信号量和队列——一个事件组可表示多个独立事件",
        "事件组比多个二进制信号量更节省RAM"
    ],
    "background": [
        "裸机中用uint32_t flags|=BIT0来标记多个事件——RTOS事件组提供阻塞等待机制",
        "事件组适合'等待所有初始化完成'或'等待任意传感器触发'这类场景"
    ],
    "understand": ["事件组默认用32位(EventBits_t),每事件组最多表示24个事件(剩余用于内部)"]
}

S["9.2"] = {
    "core": [
        "xEventGroupCreate():创建事件组,返回EventGroupHandle_t",
        "xEventGroupSetBits(group, bits)/xEventGroupSetBitsFromISR():置位事件标志",
        "xEventGroupWaitBits(group, bits, clearOnExit, waitForAll, timeout):等待事件位",
        "waitForAll=pdTRUE:等待所有指定位(AND);pdFALSE:等待任意位(OR)",
        "clearOnExit=pdTRUE:成功等待后自动清除指定位(适合一次性事件)"
    ],
    "background": [
        "裸机中检查多个条件需if(flag1&&flag2&&flag3)——RTOS事件组的And等待原子化检查",
        "事件组WaitBits是原子的——不会在检查位和清除位之间被其他任务打断"
    ],
    "understand": ["xEventGroupClearBits()手动清除事件位;xEventGroupGetBits()只读不修改"]
}

S["9.3"] = {
    "core": [
        "xEventGroupSync():任务间同步屏障(Barrier)——多任务在某个点等待彼此",
        "Sync操作置自己的位→等待所有其他参与者的位→所有任务同时被释放",
        "事件组合适场景:多任务初始化同步、多传感器数据采集完成后一起处理",
        "事件位在设置后保持直到被清除——与信号量不同(信号量可能丢失)"
    ],
    "background": [
        "裸机中多模块同步初始化只能靠延时或串行顺序保证——事件组提供并行初始化+同步等待",
        "事件位不丢失的特性使其适合表示状态(如:'SD卡已插入' '网络已连接')"
    ],
    "understand": ["阻塞等待事件组的任务按优先级顺序被唤醒"]
}

# ==================== Chapter 10 ====================

S["10.1"] = {
    "core": [
        "任务通知(Task Notification)是最快的IPC——直接操作TCB中的通知值",
        "每个任务有单个通知值(32位)和通知状态——内建于TCB,无需额外RAM",
        "任务通知不可用于ISR接收(ISR只能发送通知)",
        "任务通知是一对一的——一个通知源对应一个接收任务"
    ],
    "background": [
        "任务通知比队列/信号量快约45%——适合高效的一对一通信场景",
        "裸机中用全局标志通知特定函数——RTOS任务通知是其阻塞机制进化版"
    ],
    "understand": ["任务通知是FreeRTOS V8.2.0引入的轻量级机制,在V10.x中成熟"]
}

S["10.2"] = {
    "core": [
        "xTaskNotify(task, value, action):向任务发送通知(可带32位值)",
        "eNotifyAction:决定通知的行为(eSetBits/eIncrement/eSetValueWithOverwrite/eSetValueWithoutOverwrite)",
        "xTaskNotifyWait(bitsToClearOnEntry, bitsToClearOnExit, &value, timeout):阻塞等待通知",
        "xTaskNotifyGive(task):简单版通知(通知值+1),配合ulTaskNotifyTake()使用"
    ],
    "background": [
        "任务通知可替代:二进制信号量(xTaskNotifyGive+ulTaskNotifyTake)、计数信号量(多次NotifyGive)",
        "也可替代轻量级队列(传递32位值)、事件组(多位标志运算是其优势)"
    ],
    "understand": ["xTaskNotifyStateClear()清除任务通知状态(不改变通知值)"]
}

S["10.3"] = {
    "core": [
        "用任务通知替代二进制信号量:vTaskNotifyGiveFromISR()+ulTaskNotifyTake(pdTRUE,timeout)",
        "用任务通知替代队列:传递32位值(xTaskNotify(x,val,eSetValueWithOverwrite))",
        "用任务通知替代事件组:通知值按位操作(eSetBits+bitsToClearOnEntry/Exit)",
        "任务通知限制:仅一对一、一发一收(无广播能力)"
    ],
    "background": [
        "裸机中一对一通知用函数调用——RTOS中任务通知提供异步+阻塞等待的升级版",
        "设计时常问:这个通信是1:1吗?是→任务通知;否→队列或信号量"
    ],
    "understand": ["任务通知比信号量快45%,比队列快更——适合高频通信场景(如音频采样缓冲通知)"]
}

S["10.4"] = {
    "core": [
        "任务通知优势:RAM节省(每任务内建,无需额外分配)、速度最快",
        "任务通知劣势:仅一对一、无广播/多播、接收任务是固定的",
        "不适用场景:多任务等同一通知、需要数据缓冲队列长度>1、发送者任务未知",
        "选择流程:1对1用任务通知>1对多或N对1用队列>事件通知用信号量"
    ],
    "background": [
        "在STM32F4上任务通知vs队列性能对比:通知~50周期,队列~120周期(近似数)",
        "在没有DMA的简单MCU上,任务通知的速度优势更显著"
    ],
    "understand": ["版本兼容:任务通知API在V10.4.x中重新整理,旧API(如xTaskNotifyFromISR)仍可用"]
}

# ==================== Chapter 11 ====================

S["11.1"] = {
    "core": [
        "低功耗设计是电池供电嵌入式设备的刚需——RTOS需支持休眠",
        "FreeRTOS低功耗支持通过Tickless Idle Mode实现",
        "Tickless核心思想:当所有任务都阻塞时,停止SysTick,MCU进入低功耗休眠",
        "休眠时间=将任务阻塞时间转换为硬件定时器唤醒时间"
    ],
    "background": [
        "裸机低功耗:手动控制MCU进入Sleep/Stop/Standby模式——RTOS自动化此决策",
        "STM32的低功耗模式( Sleep/Sleep-now/Stop/Standby)与RTOS的Tickless协同工作"
    ],
    "understand": ["configUSE_TICKLESS_IDLE=1启用Tickless模式,需实现portSUPPRESS_TICKS_AND_SLEEP()"]
}

S["11.2"] = {
    "core": [
        "portSUPPRESS_TICKS_AND_SLEEP(expectedIdleTime):移植层需实现的休眠函数",
        "参数expectedIdleTime:预期空闲Tick数→转化为硬件定时器延时→进入休眠",
        "休眠前需:计算MCU可进入的最深层休眠模式、配置唤醒定时器",
        "唤醒后需:补偿Tick计数(休眠期间丢失的Tick计数需补回)"
    ],
    "background": [
        "STM32中通常用LPTIM(低功耗定时器)或RTC作为唤醒源——SysTick在休眠时停止",
        "Tick补偿:睡眠了N ms→唤醒后需在xTaskIncrementTick()中补偿N次Tick"
    ],
    "understand": ["某些MCU可选择是否在休眠时保持RAM内容——影响功耗和恢复时间"]
}

S["11.3"] = {
    "core": [
        "eTaskConfirmSleepModeStatus():检查是否可安全进入休眠",
        "configPRE_SLEEP_PROCESSING(msec)/configPOST_SLEEP_PROCESSING(msec):休眠前后用户钩子",
        "休眠前钩子可做:关外设、设GPIO为低功耗状态、调整时钟",
        "休眠后钩子可做:恢复外设、恢复时钟、重新校准(时间漂移补偿)"
    ],
    "background": [
        "裸机进入STOP模式前需手动关DMA/关UART/设GPIO——RTOS通过钩子统一管理",
        "Tickless模式在快速变化的系统中未必省电——频繁进出休眠反而增加开销"
    ],
    "understand": ["configEXPECTED_IDLE_TIME_BEFORE_SLEEP设置最小休眠阈值,避免短休眠的进出开销"]
}

# ==================== Chapter 12 ====================

S["12.1"] = {
    "core": [
        "FreeRTOS提供多种开发和调试支持特性,辅助开发和故障排查",
        "运行时统计(Run-Time Stats):每个任务的CPU占用时间",
        "栈溢出检测(Stack Overflow Detection):避免最危险的内存错误",
        "Trace钩子宏:关键事件(任务切换/队列操作)可记录到外部分析工具"
    ],
    "background": [
        "裸机调试靠断点和printf——RTOS增加运行时统计和栈检测功能提供更全面的可见性",
        "这些特性在调试阶段启用,发布时可关闭以节省ROM/RAM"
    ],
    "understand": ["调试辅助特性通过FreeRTOSConfig.h中的宏按需启用,大部分零开销"]
}

S["12.2"] = {
    "core": [
        "configASSERT(x):FreeRTOS断言宏,在Debug构建中验证条件,Release中禁用",
        "常用断言:检查API参数有效性(handle非NULL/优先级有效/ISR中未调用阻塞API)",
        "断言失败通常进入死循环——在调试器中立即发现错误位置",
        "configASSERT是捕获编码错误的有力工具——建议在Debug时始终启用"
    ],
    "background": [
        "裸机中assert()来自标准C库——configASSERT()是FreeRTOS定制的嵌入式级检查",
        "许多FreeRTOS API内部使用configASSERT检查参数有效性和调用上下文(Task vs ISR)"
    ],
    "understand": ["在发布版中可将configASSERT定义为空宏以消除开销和代码体积"]
}

S["12.3"] = {
    "core": [
        "栈溢出是导致不可预测行为的首要原因——FreeRTOS提供两种栈溢出检测方法",
        "方法1(configCHECK_FOR_STACK_OVERFLOW=1):每次上下文切换时检查栈指针是否越界",
        "方法2(configCHECK_FOR_STACK_OVERFLOW=2):栈初始化时填充已知模式,切换时检查是否被覆盖",
        "栈溢出Hook(vApplicationStackOverflowHook):栈溢出时调用,记录任务名和句柄"
    ],
    "background": [
        "裸机中栈溢出同样致命——但只有一个栈(主栈+进程栈),容易监控",
        "RTOS中每个任务独立栈——任何一个任务的栈溢出都可能破坏其他任务的数据",
        "uxTaskGetStackHighWaterMark()是预防栈溢出的最佳工具——在开发阶段监控每个任务的栈水位"
    ],
    "understand": ["方法1仅检测溢出导致的栈指针越界,方法2检测更彻底但消耗更多CPU"]
}

S["12.4"] = {
    "core": [
        "运行时统计显示每个任务的CPU占用绝对时间和百分比",
        "需在FreeRTOSConfig.h中启用configGENERATE_RUN_TIME_STATS",
        "需实现应用层高精度计时器(比Tick更高精度)用于时间计量",
        "vTaskGetRunTimeStats()/uxTaskGetSystemState():获取统计数据,格式化输出"
    ],
    "background": [
        "裸机中CPU利用率通过计时空闲循环次数估算——RTOS提供每个任务级别的精确统计",
        "STM32中用TIM2/5(32位定时器)提供微秒级运行时间基准是最佳实践"
    ],
    "understand": ["运行时统计需硬件定时器提供比Tick更高精度的时间源(如1us分辨率)"]
}

S["12.5"] = {
    "core": [
        "Trace钩子(traceTASK_SWITCHED_IN/OUT等)在每个关键内核事件处记录时间戳和事件信息",
        "开源工具(如Percepio Tracealyzer/SystemView)可图形化显示RTOS行为",
        "trace工具帮助发现:任务饥饿、优先级反转、IPC延迟、不合理设计",
        "配置:FreeRTOSConfig.h中启用trace宏,实现对应C文件中的回调函数"
    ],
    "background": [
        "裸机调试靠逻辑分析仪+GPIO引脚——RTOS的trace提供软件级的任务级时序图",
        "percepio Tracealyzer对FreeRTOS用户免费(限定MCU)——强烈推荐用于学习调度行为"
    ],
    "understand": ["trace宏是FreeRTOS中唯一被设计为应用程序实现的固定格式API"]
}

# ==================== Chapter 13 ====================

S["13.1"] = {
    "core": [
        "常见问题1:中断优先级配置错误——configMAX_SYSCALL_INTERRUPT_PRIORITY设置不正确",
        "常见问题2:栈溢出——任务栈太小或局部变量(尤其是大数组)太多",
        "常见问题3:内存不足——configTOTAL_HEAP_SIZE太小或内存碎片",
        "常见问题4:优先级反转——使用普通信号量而非互斥锁保护资源"
    ],
    "background": [
        "裸机调试经验部分适用:检查硬件(时钟/电源/复位)、检查外设初始化",
        "RTOS特有故障模式:任务死锁、任务饥饿、不必要的上下文切换开销"
    ],
    "understand": ["大部分RTOS问题根源可归为三类:配置错误、资源不足、时序问题"]
}

S["13.2"] = {
    "core": [
        "系统不工作(无任务运行):检查vTaskStartScheduler()是否被调用、SysTick中断是否产生",
        "任务未创建:检查xTaskCreate()返回值≠pdPASS、heap空间是否足够",
        "调度行为异常:检查configUSE_PREEMPTION、优先级设置、时间片配置",
        "IPC不通:检查队列/信号量创建成功、发送/接收API的超时参数"
    ],
    "background": [
        "裸机调试从检查硬件开始——RTOS调试从检查调度器是否启动开始",
        "设计阶段的排查清单:每个任务栈估算、heap预算、IPC流图——减少运行时调试工作量"
    ],
    "understand": ["vTaskList()可打印所有任务的状态/优先级/栈水位——是快速诊断的核心命令"]
}

S["13.3"] = {
    "core": [
        "调试策略:逐步增法——从单任务逐步增加到多任务,每添加一个任务验证一次",
        "运行Fast Test Duration:让系统长时间运行(24h+)暴露偶发性问题(内存泄漏/罕见竞争)",
        "使用configASSERT()捕获API参数错误;使用栈检测捕获栈越界",
        "printf调试在RTOS中需要注意:不可在ISR中使用、任务间的printf输出交错、print本身消耗大量时间"
    ],
    "background": [
        "裸机调试用调试器单步执行——RTOS多任务时单步影响调度时序,printf+日志更实用",
        "查找竞争条件(Race Condition)的经典手段:改变任务优先级人为触发条件"
    ],
    "understand": ["CPU负载分析:在Idle Task中计数idleCallCount,CPU使用率≈100%×(1-idleCallCount/maxCallCount)"]
}

# ========== Write JSON ==========
data = {"sections": S}
with open('/home/ubuntu/Edge-AI/tools/kp_rtos.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print(f"Total sections: {len(S)}")
print("kp_rtos.json written successfully")
