#!/usr/bin/env python3
"""Generate kp_rtos.json with proper JSON escaping."""
import json

sections = {}

# ==================== Chapter 1 ====================

sections["1.1"] = {
    "core": [
        "多任务系统让MCU在单核上交替执行多个任务,营造同时运行的假象",
        "实时系统对外部事件的响应具有时间确定性,必须在截止期限内完成",
        "硬实时(Hard Real-Time)错过截止期限=系统失败;软实时(Soft Real-Time)允许偶尔超时",
        "裸机while(1)大循环不是多任务——所有任务共享同一个栈,没有独立的上下文",
        "RTOS内核:一个管理多个任务执行顺序和资源的系统软件层",
        "Context Switch(上下文切换)是RTOS的核心开销——保存当前任务寄存器,恢复下一个任务寄存器"
    ],
    "background": [
        "你已有STM32裸机开发经验,能理解中断响应、定时器PWM配置——RTOS在此基础上增加了任务调度层",
        "STM32的SysTick硬件定时器为FreeRTOS提供Tick(心跳)时钟源,驱动任务调度",
        '裸机中\'实时\'依赖精心设计的中断优先级和轮询策略;RTOS中由调度器保证关键任务的确定性响应'
    ],
    "understand": [
        "FreeRTOS是市场占有率最高的嵌入式RTOS之一,MIT开源许可",
        "多任务系统的任务数理论上只受RAM限制(每个任务需要独立的栈空间)"
    ]
}

sections["1.1.1"] = {
    "core": [
        "FreeRTOS Kernel是轻量级实时内核,提供任务调度、IPC、内存管理等核心功能",
        "FreeRTOS由Richard Barry主导开发,现由Amazon FreeRTOS团队维护",
        "FreeRTOS内核最小ROM占用约4-9KB,适合ROM/RAM受限的MCU",
        "FreeRTOS源代码用C编写,可移植到40+处理器架构"
    ],
    "background": [
        "与裸机开发相比,FreeRTOS提供标准化的多任务API,避免每次从头设计任务调度逻辑",
        "FreeRTOS的MIT许可允许商业闭源使用,无需公开源代码"
    ],
    "understand": [
        "Amazon FreeRTOS在FreeRTOS内核基础上增加了云连接库(MQTT/HTTPS)"
    ]
}

sections["1.1.2"] = {
    "core": [
        "FreeRTOS的价值在于:缩短嵌入式多任务系统的开发周期",
        "提供标准化的任务间通信和同步机制(Queue、Semaphore、Mutex)",
        "抢占式调度确保高优先级任务在可控延迟内得到CPU",
        "任务隔离防止单任务崩溃拖垮整个系统(与裸机共用栈不同)",
        "代码可移植性强——应用级代码在不同MCU间迁移时只需重编移植层"
    ],
    "background": [
        "裸机中新增一个外设功能往往需要重构主循环——RTOS中只需创建一个新任务",
        "裸机的中断响应延迟取决于最长关中断时间;RTOS中取决于Isr函数的最长执行时间"
    ],
    "understand": [
        "FreeRTOS被广泛应用于消费电子、工业控制、汽车电子和IoT设备"
    ]
}

sections["1.1.3"] = {
    "core": [
        "Task(任务):一个独立的无限循环程序片段,拥有自己的栈和TCB",
        "TCB(Task Control Block):内核维护每个任务的状态、优先级、栈指针等元数据",
        "Scheduler(调度器):决定哪个就绪任务获得CPU的内核组件",
        "Context Switch(上下文切换):保存当前任务寄存器状态,恢复目标任务寄存器状态",
        "Tick:RTOS的心跳中断,每个Tick触发调度器评估是否需要切换任务",
        "Critical Section(临界区):需要互斥访问的代码段,通常通过关中断保护"
    ],
    "background": [
        '裸机中\'上下文\'只有一个——main函数执行流;RTOS中每个任务有独立的上下文',
        "TCB结构体在task.c中定义,存储在任务堆栈中或专门分配的内存中"
    ],
    "understand": [
        "PendSV异常在ARM Cortex-M上用于触发上下文切换——利用其可悬起特性"
    ]
}

sections["1.1.4"] = {
    "core": [
        "裸机while(1)大循环的三大痛点:实时性难以保证、代码难以复用、功能难以扩展",
        "RTOS将复杂系统拆分为多个独立任务,降低代码耦合度",
        "任务隔离——一个任务的栈溢出不影响其他任务的正常运行",
        "RTOS提供标准化的同步原语避免竞态条件(Race Condition)",
        'RTOS让开发者从\'什么时候该执行什么\'中解放,专注于\'每个任务自己该做什么\''
    ],
    "background": [
        "裸机中所有模块共享同一个栈——一个函数局部变量过多会导致全局栈溢出",
        "裸机中新增功能需要仔细插入主循环时间片——RTOS中只需创建新任务并设置优先级"
    ],
    "understand": [
        "RTOS不是银弹——简单系统(单功能LED/按键)用RTOS反而增加复杂度和开销"
    ]
}

sections["1.1.5"] = {
    "core": [
        "抢占式调度(Preemptive Scheduling):高优先级任务就绪时立即抢占低优先级任务",
        "协作式调度(Cooperative Scheduling):任务主动让出CPU才发生切换",
        "队列(Queue):任务间线程安全的数据传递机制(FIFO,按值拷贝)",
        "信号量(Semaphore):任务间/ISR与任务间的事件通知机制",
        "互斥锁(Mutex):带优先级继承的二进制信号量,用于保护共享资源",
        "软件定时器(Software Timer):基于Tick计数实现的可配置定时回调",
        "事件组(Event Group):任务等待多个事件位的AND/OR组合",
        "任务通知(Task Notification):轻量级一对一同步机制"
    ],
    "background": [
        "这些特性在裸机中需要开发者从头实现或使用复杂的状态机——RTOS提供标准化API",
        "FreeRTOS所有特性设计目标:最小RAM占用、确定行为、可配置裁剪"
    ],
    "understand": [
        "FreeRTOS还支持Stream Buffer、Message Buffer等较新的IPC机制",
        "每个特性都是可选的——通过FreeRTOSConfig.h中的宏裁剪不需要的功能以节省ROM"
    ]
}

sections["1.1.6"] = {
    "core": [
        "FreeRTOS使用MIT开源许可证,允许免费用于商业闭源产品",
        "开源意味着可以查看和修改内核源码,理解每个API的底层实现",
        "FreeRTOS内核代码有严格的编码规范和统一的代码风格",
        "许可证要求:在软件文档中保留FreeRTOS版权声明"
    ],
    "background": [
        "与GPL不同,MIT许可不要求衍生作品开源——适合商业嵌入式产品",
        "FreeRTOS初创时使用GPLv2,后来改为MIT许可以降低商业使用门槛"
    ],
    "understand": [
        "Amazon FreeRTOS增加了额外组件(OTA、AWS IoT集成),这些组件使用Amazon自己的许可"
    ]
}

sections["1.2"] = {
    "core": [
        "FreeRTOS源码发布包含:内核核心源文件、移植层(Port Layer)、示例工程",
        "FreeRTOS/Source/目录是内核核心代码,包含task.c、queue.c、timers.c等",
        "移植层(portable/)包含与特定编译器/MCU相关的适配代码",
        "每个官方发行版附带了多个MCU平台的Demo项目供快速上手"
    ],
    "background": [
        '从裸机到RTOS:需要理解\'移植层\'的概念——裸机代码直接操作硬件寄存器,RTOS移植层封装了硬件差异',
        "获取示例工程比从零搭建项目更高效——官方Demo已配置好FreeRTOSConfig.h和启动文件"
    ],
    "understand": [
        "FreeRTOS官网(www.freertos.org)提供完整的API文档和示例"
    ]
}

sections["1.2.1"] = {
    "core": [
        "示例项目可在多种开发板上直接编译运行(STM32 Discovery、LPCXpresso等)",
        "示例项目展示了FreeRTOS最小系统所需的所有文件配置",
        "从官方示例复制FreeRTOSConfig.h作为自己项目的起点是最佳实践",
        "示例工程通常包含多个任务的简单演示(LED闪烁、串口打印等)"
    ],
    "background": [
        "运行示例工程是验证开发环境搭建是否正确的最快方式",
        "STM32平台的Demo使用HAL或标准外设库,与你已有的STM32经验一致"
    ],
    "understand": [
        "FreeRTOS也提供Windows模拟器版本(FreeRTOSWindows),可在PC上调试RTOS应用"
    ]
}

# ==================== Chapter 2 ====================

sections["2.1"] = {
    "core": [
        "FreeRTOS内核源码通过解压官方ZIP包获得,包内包含内核源文件和预配置Demo",
        "理解分布结构是正确搭建FreeRTOS项目的前提",
        "每个Demo项目已经完成了FreeRTOSConfig.h配置、启动代码和链接脚本的集成",
        "从Demo入手能避免从零搭建时的文件遗漏和配置错误"
    ],
    "background": [
        "STM32裸机项目需要自行配置启动文件和链接脚本——FreeRTOS项目在此基础上增加内核源码引用",
        "官方ZIP包的目录结构遵循统一的命名模式,便于跨平台迁移"
    ],
    "understand": [
        "FreeRTOS Ziplib/目录已被弃用,不再需要引入到项目中"
    ]
}

sections["2.2"] = {
    "core": [
        "FreeRTOS发行版包含:Source/(内核源码)、Demo/(示例项目)、License/(许可证文件)",
        "Source/目录是所有FreeRTOS项目的核心,必须包含",
        "Demo/目录提供各平台的参考实现,用作学习和快速启动",
        "FreeRTOSConfig.h是内核配置的唯一入口,裁剪功能以节省ROM/RAM"
    ],
    "background": [
        "与STM32裸机中stm32xxxx.h作为MCU配置头文件类似,FreeRTOSConfig.h是内核配置头文件",
        "Demo项目的FreeRTOSConfig.h可作为模板,但需根据具体MCU的RAM/ROM大小调整"
    ],
    "understand": [
        "FreeRTOS发行版每个大版本号下包含多个子目录对应不同MCU系列"
    ]
}

sections["2.2.1"] = {
    "core": [
        "Port(移植层)是连接FreeRTOS内核与特定MCU/编译器的桥梁",
        "移植层负责三件核心工作:上下文切换、Tick中断管理、临界区进出",
        "每个硬件平台需要一个特定的移植层文件(如port.c、portmacro.h)",
        "ARM Cortex-M3/M4移植层位于portable/GCC/ARM_CM3/或portable/GCC/ARM_CM4F/"
    ],
    "background": [
        "裸机开发直接操作SCB、NVIC等寄存器——FreeRTOS移植层封装了这些操作",
        "不同编译器(GCC、IAR、KEIL)需要不同的移植层文件,因为内联汇编语法不同"
    ],
    "understand": [
        "Cortex-M系列利用SVC(系统服务调用)启动第一个任务,PendSV执行后续上下文切换"
    ]
}

sections["2.2.2"] = {
    "core": [
        "构建FreeRTOS需要将Source/下所有.c文件(不含portable/中的非目标平台文件)加入工程",
        "只需包含目标平台的移植层文件:port.c + portmacro.h",
        "heap_x.c根据项目需求选择一种(heap_1~heap_5)加入工程",
        "FreeRTOSConfig.h必须放在编译器的include path中"
    ],
    "background": [
        "STM32裸机项目中需要包含startup_stm32xxxx.s和外设库文件——RTOS项目额外增加约10个内核文件",
        "错误的文件选择(如加入非目标平台的port.c)会导致编译失败"
    ],
    "understand": [
        "heap_x.c文件位于portable/MemMang/目录下,同一时间只能有一个heap实现"
    ]
}

sections["2.2.3"] = {
    "core": [
        "FreeRTOSConfig.h是FreeRTOS的配置核心,所有功能裁剪通过宏定义控制",
        "关键配置:configTICK_RATE_HZ(Tick频率)、configUSE_PREEMPTION(是否抢占)",
        "内存相关配置:configTOTAL_HEAP_SIZE(heap总量)、configMINIMAL_STACK_SIZE(最小栈)",
        "功能开关:configUSE_QUEUE_SETS、configUSE_TIMERS、configUSE_MUTEXES等",
        "configMAX_PRIORITIES定义优先级数量(不是最大值),默认值影响RAM使用",
        "configSUPPORT_STATIC_ALLOCATION启用静态分配,不依赖heap"
    ],
    "background": [
        "STM32裸机中用SystemCoreClock变量和SysTick_Config()配置系统时钟——FreeRTOSConfig.h中的configTICK_RATE_HZ对应的是SysTick的触发频率",
        "错误的configTOTAL_HEAP_SIZE配置会导致运行时内存分配失败——需要通过xPortGetFreeHeapSize()调试确认"
    ],
    "understand": [
        "configASSERT()宏在调试阶段应启用——帮助捕获API参数错误等运行时问题"
    ]
}

sections["2.2.4"] = {
    "core": [
        "FreeRTOS官方发行版定期发布(LTS和标准版本),包含经过测试的稳定代码",
        "每个发行版包含Release Notes,说明新特性、Bug修复和已知问题",
        "官方发行版包含已验证的Demo工程,与对应MCU开发板配套",
        "长期支持版(LTS)提供更长时间的安全更新和Bug修复"
    ],
    "background": [
        "从裸机开发过渡:裸机代码通常固定使用某个HAL库版本——FreeRTOS也依赖版本匹配的移植层",
        "最新版不一定是最适合项目的版本——稳定性比新特性更重要"
    ],
    "understand": [
        "FreeRTOSv202604.00-LTS是当前使用的版本,基于FreeRTOS Kernel V10.x"
    ]
}

sections["2.2.6"] = {
    "core": [
        "所有FreeRTOS项目必须包含的通用源文件:task.c、list.c、queue.c",
        "task.c:任务创建、删除、调度、延时等核心功能",
        "list.c:内核链表实现,用于就绪列表、延迟列表等内部数据结构",
        "queue.c:队列和信号量(信号量基于队列实现)",
        "按需包含的文件:timers.c、event_groups.c、stream_buffer.c"
    ],
    "background": [
        "裸机中不需要这些基础设施——RTOS内核本身就是一个精心设计的软件架构",
        "list.c中的链表是侵入式链表(节点嵌入到TCB中),与裸机常见的独立链表节点不同"
    ],
    "understand": [
        "croutine.c(协程)是FreeRTOS的轻量级替代方案,但已不推荐新项目使用"
    ]
}

sections["2.2.7"] = {
    "core": [
        "移植层文件分为两大部分:port.c(C/汇编实现)和portmacro.h(类型定义和宏)",
        "port.c包含:启动第一个任务(prvStartFirstTask)、上下文切换(xPortPendSVHandler)",
        "portmacro.h定义:TickType_t、BaseType_t、临界区宏(portENTER_CRITICAL等)",
        "不同MCU架构的移植层差异较大——ARM Cortex-M使用PendSV+SVC",
        "Cortex-M4F相比Cortex-M3增加了浮点寄存器保存/恢复(FPU上下文)"
    ],
    "background": [
        "裸机中对CPU寄存器的保存/恢复只在中断进出时发生——RTOS的上下文切换在每次任务切换时发生",
        "Cortex-M4F的FPU上下文切换增加约200字节的栈开销——任务栈设计时必须考虑"
    ],
    "understand": [
        "Lazy Stacking机制是Cortex-M3/M4的硬件特性,减少中断响应时的寄存器压栈开销"
    ]
}

sections["2.2.8"] = {
    "core": [
        "FreeRTOSConfig.h必须位于编译器的Include Path中,确保所有内核文件能访问",
        "Source/include/目录包含所有公共头文件(FreeRTOS.h、task.h、queue.h等)",
        "移植层的portmacro.h通常通过FreeRTOS.h中的路径包含",
        "应用代码只需包含FreeRTOS.h和具体功能头文件(如task.h、queue.h)"
    ],
    "background": [
        "STM32裸机工程中需要包含stm32f4xx.h等外设头文件——RTOS工程额外增加FreeRTOS头文件路径",
        "常见的路径遗漏错误:忘记将FreeRTOSConfig.h所在目录加入Include Path导致编译失败"
    ],
    "understand": [
        "FreeRTOSConfig.h中的#ifdef __ICCARM__等预编译指令兼容多编译器"
    ]
}

sections["2.2.9"] = {
    "core": [
        "应用代码包含头文件的规范顺序:FreeRTOS.h → 功能模块头文件(task.h、queue.h等)",
        "FreeRTOS.h自动包含portmacro.h(通过相对路径或移植层映射)",
        "功能头文件主要提供API函数声明和常量定义",
        "FreeRTOS.h中通过FreeRTOSConfig.h的配置宏决定哪些功能模块被编译"
    ],
    "background": [
        "裸机中包含stm32f4xx.h后即可操作所有外设寄存器——FreeRTOS的头文件分层更精细",
        "头文件的依赖链:应用→FreeRTOS.h→FreeRTOSConfig.h→portmacro.h→编译器相关定义"
    ],
    "understand": [
        "projdefs.h定义了pdTRUE/pdFALSE/pdPASS/pdFAIL等常用常量"
    ]
}

sections["2.3"] = {
    "core": [
        "FreeRTOS官方Demo是验证移植和配置正确性的最快途径",
        "Demo工程展示了完整的FreeRTOS项目结构:main.c、FreeRTOSConfig.h、启动文件、链接脚本",
        "运行Demo可以确认:Tick中断正常、任务切换发生、空闲任务运行",
        "Demo工程也是学习FreeRTOS API用法的参考代码"
    ],
    "background": [
        "从裸机到RTOS的第一步不是写应用代码——而是跑通一个Demo确认环境配置正确",
        "Demo中的vTaskStartScheduler()调用后如果系统不工作,首先检查SysTick配置和中断优先级分组"
    ],
    "understand": [
        "FreeRTOS的Demo中通常包含多个标准测试任务,用于验证内核功能完整性"
    ]
}

sections["2.4"] = {
    "core": [
        "创建FreeRTOS项目有两种方法:基于Demo修改、从零手动配置",
        "基于Demo修改:复制Demo目录,修改FreeRTOSConfig.h和任务代码",
        "从零配置:手动添加所有源文件路径、Include Path、链接脚本修改",
        "必须为Idle Task和可能的Timer Task预留栈空间(在FreeRTOSConfig.h中配置)",
        "启动文件需配置主栈大小和堆大小,与FreeRTOS的heap配置协同"
    ],
    "background": [
        "STM32CubeMX生成的代码可以集成FreeRTOS——但理解手动配置过程有助于排查问题",
        "从Demo修改是推荐方式——减少配置错误的可能性"
    ],
    "understand": [
        "FreeRTOS BSP(板级支持包)帮助文件在Demo/Common/目录中供参考"
    ]
}

sections["2.4.1"] = {
    "core": [
        "根据目标MCU选择最接近的Demo作为起点(如STM32F4选择Cortex-M4 Demo)",
        "修改FreeRTOSConfig.h匹配目标板的资源(时钟频率、内存大小、外设)",
        "替换Demo中的外设初始化代码为目标板的外设初始化",
        "逐步替换Demo任务为应用任务,每次替换后验证功能"
    ],
    "background": [
        "STM32不同系列(F1/F4/F7/H7)的Demo移植层文件相同(都是ARM_CM3/ARM_CM4F/ARM_CM7),差异在外设驱动",
        "从Demo出发比从零搭建快10倍以上——不要重造轮子"
    ],
    "understand": [
        "中断优先级分组必须与FreeRTOS的要求一致——通常设为4位抢占优先级(NVIC_PriorityGroup_4)"
    ]
}

sections["2.4.2"] = {
    "core": [
        "从零创建需要准备:FreeRTOSConfig.h、main.c、链接脚本、启动文件",
        "需添加的源文件:所有内核通用文件 + 目标移植层 + 一种heap实现",
        "FreeRTOSConfig.h中的configCPU_CLOCK_HZ必须匹配MCU实际时钟频率",
        "SysTick中断优先级必须设置为FreeRTOS允许的最低优先级(通过configKERNEL_INTERRUPT_PRIORITY)",
        "启动文件中的栈大小(Stack_Size)设为至少configMINIMAL_STACK_SIZE的2倍"
    ],
    "background": [
        "STM32裸机项目用SystemInit()配置时钟——RTOS项目中configCPU_CLOCK_HZ必须与SystemCoreClock保持一致",
        "SysTick优先级设置错误是RTOS系统不工作的首要原因——Cortex-M上数值越小优先级越高"
    ],
    "understand": [
        "FreeRTOS的portable/目录中包含了常见编译器和MCU的预配置启动文件参考"
    ]
}

sections["2.5"] = {
    "core": [
        "FreeRTOS定义了独特的命名规范:变量前缀表示类型(x=结构体/Basetype, u=unsigned, p=pointer)",
        "函数返回值类型通过前缀标注(pdPASS/pdFAIL, errCOULD_NOT_ALLOCATE_REQUIRED_MEMORY)",
        "TickType_t根据配置决定是16位还是32位——影响延时最大值和精度",
        "BaseType_t通常对应于MCU最自然的整数宽度(Cortex-M上为32位)",
        "代码规范统一提高了跨平台代码的可读性和可维护性"
    ],
    "background": [
        "裸机代码通常没有严格的命名规范——FreeRTOS的命名规范有助于一眼看出变量类型",
        "显式类型转换在FreeRTOS代码中大量使用——是为了兼容不同编译器的类型检查差异"
    ],
    "understand": [
        "FreeRTOS的命名规范源于嵌入式系统需要精确控制数据类型大小的需求"
    ]
}

sections["2.5.1"] = {
    "core": [
        "FreeRTOS重定义了基本数据类型(如TickType_t、BaseType_t),不直接使用C标准类型",
        "这样做的目的是保证跨平台移植时数据类型大小的一致性",
        "portmacro.h中定义了这些类型到编译器类型的映射",
        "应用代码应尽量使用FreeRTOS定义的类型而非标准C类型"
    ],
    "background": [
        "STM32裸机开发中使用uint32_t、int16_t等标准类型——FreeRTOS的封装层提供了额外抽象",
        "移植到新平台时只需修改portmacro.h中的类型定义,应用代码无需改动"
    ],
    "understand": [
        "portCHAR、portSHORT、portLONG等基础类型别名也定义在portmacro.h中"
    ]
}

sections["2.5.2"] = {
    "core": [
        "TickType_t是FreeRTOS的Tick计数值类型——用于延时和超时参数",
        "configTICK_TYPE_WIDTH_IN_BITS决定TickType_t是16位还是32位(默认与MCU位宽一致)",
        "16位TickType_t的portMAX_DELAY约65535个Tick——32位约4.29e9个Tick",
        "在RAM受限的8位MCU上应使用16位TickType_t以节省时间相关的TCB成员空间"
    ],
    "background": [
        "STM32F4是32位MCU——TickType_t默认32位,portMAX_DELAY接近无限期阻塞",
        "TickType_t的位数直接影响vTaskDelay()和队列超时的最大可指定值"
    ],
    "understand": [
        "configUSE_16_BIT_TICKS在8位和16位MCU上启用以减小RAM占用"
    ]
}

sections["2.5.3"] = {
    "core": [
        "BaseType_t定义为MCU架构最高效的整数类型(Cortex-M上为long,32位)",
        "BaseType_t用于布尔值、错误码、计数等频繁使用的场景",
        "返回值为pdTRUE/pdFALSE的API操作BaseType_t",
        "UBaseType_t是BaseType_t的无符号版本"
    ],
    "background": [
        "STM32(ARM Cortex-M)上是32位——BaseType_t和int等效",
        "在8位AVR MCU上BaseType_t是char(8位)——同样的API行为但计数范围不同"
    ],
    "understand": [
        "BaseType_t也是configSTACK_DEPTH_TYPE的基础类型"
    ]
}

sections["2.5.4"] = {
    "core": [
        "大多数返回BaseType_t的API用pdPASS(0)表示成功,非0值(pdFAIL/errCOULD_NOT_ALLOCATE)表示失败",
        "pdTRUE(1)和pdFALSE(0)用于条件判断型API",
        "检查返回值是嵌入式开发的基本习惯——FreeRTOS API调用后应始终检查返回值",
        "内存分配失败(errCOULD_NOT_ALLOCATE_REQUIRED_MEMORY)是常见的返回值错误"
    ],
    "background": [
        "裸机中函数通常返回void或int表示状态——FreeRTOS统一使用pdPASS/pdFAIL便于错误链检查",
        "不检查xTaskCreate的返回值是初学者的常见错误——导致任务未创建但后续代码仍向其发数据"
    ],
    "understand": [
        "部分API(如xQueueReceive)的超时特性使其在portMAX_DELAY时永不返回错误"
    ]
}

sections["2.5.5"] = {
    "core": [
        "变量命名前缀规则:x=结构体/非标准类型, u=unsigned, p=pointer, c=char, s=string(char*)",
        "组合前缀:ux=unsigned BaseType_t, pc=char指针, px=指向结构体的指针",
        "pv=void指针, v=void, uc=unsigned char",
        "命名规范帮助代码阅读者从变量名直接推断类型"
    ],
    "background": [
        "裸机代码中变量名通常只反映业务含义——FreeRTOS通过前缀暴露变量类型,便于代码审查",
        "pxTaskCode命名表示这是一个指向TaskFunction_t的指针"
    ],
    "understand": [
        "prv前缀表示这是一个私有(private)函数,应用代码不应直接调用"
    ]
}

sections["2.5.6"] = {
    "core": [
        "函数名前缀规则与变量类似:vTaskFunction(返回值类型+所属模块+功能名)",
        "API函数名使用帕斯卡命名(PascalCase),如xQueueCreate、xTaskCreate",
        "私有函数(static)以prv开头,如prvIdleTask、prvAddCurrentTaskToDelayedList",
        "FromISR后缀的API表示ISR安全版本,如xQueueSendToBackFromISR"
    ],
    "background": [
        "裸机函数命名由开发者自定——FreeRTOS的统一命名规范有助于一眼区分Task/Queue/ISR API",
        'API函数名的x前缀表示返回BaseType_t或非标准类型——不是返回值\'成功/失败\'的指示'
    ],
    "understand": [
        "参数命名也遵循前缀规则,如pvParameters表示void指针参数"
    ]
}

# ==================== Chapter 3 ====================

sections["3.1"] = {
    "core": [
        "RTOS需要在运行时动态创建内核对象(任务、队列、信号量等)——需要内存分配机制",
        "标准C库malloc()在嵌入式MCU中不一定可用(缺少线程安全、不确定的碎片行为)",
        "FreeRTOS提供多个heap实现方案(heap_1~heap_5),每种有不同的性能和碎片特性",
        "开发者根据项目需求选择最合适的heap方案——无固定最佳方案",
        "所有heap实现位于portable/MemMang/目录下,同一时间只能选择一个",
        "FreeRTOS不提供动态内存释放后的碎片整理——设计时需考虑内存预算"
    ],
    "background": [
        "裸机开发中内存分配通常是静态的(全局变量、固定数组)——不需要动态分配",
        "STM32的标准malloc属于heap_3类型(封装stdlib malloc),在裸机和RTOS中行为不同",
        "裸机的全局变量分配在BSS段,大小在编译时确定——RTOS的动态对象分配在heap区域"
    ],
    "understand": [
        "heap区域在启动时从主RAM中划出一块连续区域作为FreeRTOS的堆空间",
        "configTOTAL_HEAP_SIZE决定了heap的总大小——过小导致分配失败,过大浪费RAM"
    ]
}

sections["3.2"] = {
    "core": [
        "五种heap方案的核心区别:是否支持释放、是否合并碎片、是否支持多RAM区域",
        "选择指南:简单系统用heap_1,通用场景用heap_4,多RAM区域用heap_5",
        "heap_2已被heap_4取代(heap_4包含了heap_2的功能并增加了碎片合并)",
        "heap_3封装编译器自带的malloc/free——线程安全取决于编译器实现",
        "所有heap方案在分配失败时返回NULL——调用者必须检查返回值"
    ],
    "background": [
        "STM32项目中总RAM有限(如STM32F407有192KB)——heap大小需要与全局变量、栈空间统筹分配",
        "heap_4的碎片合并特性意味着释放后相邻空闲块会被合并,缓解长时间运行的碎片问题"
    ],
    "understand": [
        "heap实现的选择不影响应用API——所有API使用同样的pvPortMalloc/vPortFree接口"
    ]
}

sections["3.2.1"] = {
    "core": [
        "heap_1:最简单的分配器——只能分配,不能释放",
        "内部维护一个nextFreeByte地址指针,每次分配时将指针后移",
        "确定性行为——分配时间固定(O(1)),无碎片问题",
        "适用场景:项目不需要动态删除任务或创建/删除队列(任务数固定)",
        "最适合安全关键系统——确定行为+最小化代码复杂度"
    ],
    "background": [
        "裸机中静态全局数组分配与heap_1行为类似——所有资源在初始化时就确定",
        "如果不需要vTaskDelete(),heap_1是最佳选择——无碎片风险,代码量最小"
    ],
    "understand": [
        "heap_1的实现代码大约只有80行C代码,是理解FreeRTOS内存管理的起点"
    ]
}

sections["3.2.2"] = {
    "core": [
        "heap_2:可释放但不合并相邻空闲块——已被heap_4取代",
        "使用最佳适应(Best-Fit)算法:寻找大小最匹配的空闲块",
        "碎片问题:多次分配释放后会产生不可合并的碎片(即使相邻)",
        "不推荐新项目使用——直接使用功能等同但更好的heap_4",
        "历史意义:展示FreeRTOS内存管理的发展路径"
    ],
    "background": [
        "heap_2不能合并相邻空闲块的缺陷在长时间运行的系统中尤为致命",
        "heap_4在heap_2基础上增加了合并逻辑——选择heap_4而不选择heap_2"
    ],
    "understand": [
        "heap_2的代码在FreeRTOS 10.x版本后标记为过时"
    ]
}

sections["3.2.3"] = {
    "core": [
        "heap_3:简单封装标准C库的malloc()和free(),通过挂起调度器保证线程安全",
        "依赖编译器提供的标准库实现(newlib/musl等)——行为因编译器而异",
        "分配/释放动作由标准库管理——heap_3不维护自己的空闲列表",
        "heap_3的堆空间来自编译器链接脚本中的Heap_Size设置——而非configTOTAL_HEAP_SIZE",
        "适用场景:项目已经在使用标准malloc,或需要realloc等heap_3才支持的功能"
    ],
    "background": [
        "STM32裸机中设置Heap_Size=0(不使用动态分配)——RTOS中使用heap_3时需要确保Heap_Size足够",
        "标准库的malloc在嵌入式MCU上可能有不确定的调用时间——实时性要求高的场景避免使用heap_3"
    ],
    "understand": [
        "newlib(GCC嵌入式工具链常用)的malloc在heap_3中的线程安全由挂起调度器保证"
    ]
}

sections["3.2.4"] = {
    "core": [
        "heap_4:最推荐的通用方案——支持释放并合并相邻空闲块",
        "使用最佳适应(Best-Fit)算法从空闲列表中查找合适块",
        "插入排序维护空闲列表(按地址升序排列)——释放时检查并与前后块合并",
        "虽然分配时间不是严格O(1),但碎片程度远低于heap_2",
        "所有FreeRTOS官方Demo中heap_4是默认选择",
        "适用场景:绝大多数需要动态分配/释放的FreeRTOS项目"
    ],
    "background": [
        'heap_4中的\'合并\'是释放时的关键操作——连续两次释放相邻地址后合并为一个更大的空闲块',
        "即使使用heap_4,长期运行的系统中仍可能有碎片——监控xPortGetMinimumEverFreeHeapSize()的变化趋势",
        "从裸机思维过渡:裸机中很少考虑堆碎片——RTOS中长时间运行后heap_4也可能耗尽"
    ],
    "understand": [
        "heap_4使用end指针标记heap区域的结束边界,分配时确保不超过该边界"
    ]
}

sections["3.2.5"] = {
    "core": [
        "heap_5:在heap_4的基础上支持跨多个非连续RAM区域分配",
        "需要在使用任何动态分配API前调用vPortDefineHeapRegions()初始化各区域",
        "每个区域由起始地址和大小定义,按地址升序排列",
        "区域列表以{NULL, 0}结尾——必须正确终止",
        "适用场景:MCU有多个不连续RAM块(如Cortex-M的DTCM+SRAM+SDRAM)",
        "分配时首先在低地址区域寻找可用空间——区域间不进行碎片合并"
    ],
    "background": [
        "STM32F7/H7系列有多个RAM区域(ITCM、DTCM、AXI SRAM、SRAM1/2)——heap_5可以统一管理",
        "裸机中在不同RAM区域分配变量需要手动指定section属性——heap_5自动管理",
        "vPortDefineHeapRegions()必须在vTaskStartScheduler()之前调用,且只调用一次"
    ],
    "understand": [
        "heap_5无法合并不同区域的空闲块——如果区域1的空闲空间小于请求大小但区域2足够,仍会分配失败"
    ]
}

sections["3.3"] = {
    "core": [
        "xPortGetFreeHeapSize():返回当前未分配的heap字节数——监控heap使用量",
        "xPortGetMinimumEverFreeHeapSize():返回启动以来最少空闲heap字节数——系统最紧张时的heap余量",
        "pvPortMalloc()和vPortFree()是FreeRTOS内部使用的内存分配/释放接口",
        "通过uxTaskGetStackHighWaterMark()监控每个任务的栈使用峰值",
        "空闲heap监控是嵌入式系统Long-Run测试的必要部分"
    ],
    "background": [
        "裸机中通过实时查看全局变量数组的使用情况来估算内存——RTOS提供了标准化接口",
        "xPortGetMinimumEverFreeHeapSize()是评估堆大小是否足够的核心指标——不应接近0"
    ],
    "understand": [
        "Malloc Failed Hook(configUSE_MALLOC_FAILED_HOOK)可在分配失败时触发调试断点"
    ]
}

sections["3.4"] = {
    "core": [
        "静态内存分配在编译时就确定所有资源——不使用heap_1~heap_5中的任何方案",
        "启用方法:在FreeRTOSConfig.h中设置configSUPPORT_STATIC_ALLOCATION为1",
        "使用静态分配时,对象创建API改为xTaskCreateStatic()、xQueueCreateStatic()等",
        "需要为Idle Task和Timer Daemon Task提供静态TCB和栈——通过回调函数提供",
        "静态分配适合航空/汽车/医疗等安全关键领域——避免运行时分配失败的风险",
        "缺点:灵活性降低,任务/队列数量在编译时固定"
    ],
    "background": [
        "裸机开发天然使用静态分配——所有变量在编译时确定——RTOS的静态分配是回归裸机思维",
        "安全标准(如MISRA C、IEC 61508)倾向于静态分配——避免动态内存的不可预测行为",
        "动态vs静态的取舍:动态分配灵活但需预估堆大小,静态分配安全但不够灵活"
    ],
    "understand": [
        "静态分配不意味着不使用heap——只是内核对象的内存由用户提供而非从heap分配"
    ]
}

# ==================== Chapter 4 ====================

sections["4.1"] = {
    "core": [
        "任务是FreeRTOS中可被调度的独立执行单元——每个任务有独立的栈空间和TCB",
        "任务函数的标准原型:void vTaskFunction(void *pvParameters)",
        "任务函数通常是一个无限循环(for(;;)或while(1))——返回意味着任务被自动删除",
        "TCB(Task Control Block)存储任务的完整上下文:寄存器状态、栈指针、优先级等",
        "任务切换发生在RTOS调度器选择另一个任务获得CPU时——保存/恢复TCB中的寄存器",
        "裸机的main()函数是一个单任务——所有代码共享一个栈"
    ],
    "background": [
        "裸机while(1)是独占CPU的——RTOS中每个任务的while(1)在调用阻塞API时自动让出CPU",
        "STM32裸机中函数返回后回到调用者——RTOS任务函数返回后任务被销毁",
        "多任务的代价:每个任务需要独立栈空间——RAM大小决定了可创建的任务数量"
    ],
    "understand": [
        "TCB占用RAM(约40-80字节,取决于配置)——创建大量任务时需要计入TCB的内存开销"
    ]
}

sections["4.2"] = {
    "core": [
        "任务函数必须是一个永不返回的无限循环——或调用vTaskDelete(NULL)自我终止",
        "任务函数不接受参数时,参数应设为NULL——pvParameters是void*类型",
        "任务函数内部可以定义局部变量——这些变量存储在任务的栈上(不是全局栈)",
        "任务函数可以调用任何FreeRTOS API和标准C函数",
        "如果任务函数返回,必须调用vTaskDelete(NULL)——否则会触发configASSERT进入死循环"
    ],
    "background": [
        "裸机main()中所有局部变量都在同一个栈上分配——RTOS中每个任务的局部变量在各自栈上",
        "裸机函数的return返回调用者——RTOS任务函数的return触发prvDeleteTask,是正常的清理流程"
    ],
    "understand": [
        "在进入任务函数之前,调度器已通过prvPortStartFirstTask()恢复任务的初始寄存器状态"
    ]
}

sections["4.3"] = {
    "core": [
        "RTOS任务有四种主要状态:Running、Ready、Blocked、Suspended",
        "Running:当前正在执行的任务——每个CPU核心在任意时刻只有一个Running任务",
        "Ready:已经就绪可以被调度但尚未获得CPU的任务",
        "Blocked:等待某个事件(延时到期、队列非空、信号量可用)而不能执行的任务",
        "Suspended:通过vTaskSuspend()显式挂起,只能通过vTaskResume()恢复",
        '非Running状态是FreeRTOS实现\'多任务\'的关键——让CPU在就绪任务间快速切换',
        '裸机的\'等待\'就是while(flag==0);空转——RTOS的Blocked不消耗CPU'
    ],
    "background": [
        "裸机中的delay_ms(100)通过SysTick忙等——RTOS的vTaskDelay(100)让任务进入Blocked,CPU去执行其他任务",
        "理解任务状态转换是所有FreeRTOS开发的基础——必须能手画状态转换图"
    ],
    "understand": [
        "Task状态事件:延时到期→Blocked→Ready→被调度→Running;信号量Give→Blocked→Ready"
    ]
}

print("Script loaded successfully - sections defined up to 4.3")
