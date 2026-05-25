//////////////////////////////////////////////////////////////////////////////////	 
//测试硬件：单片机MSPM0G3507,CPU频率32MHz
//QDtech-TFT液晶驱动 for MSPM0G3507 
//LCD屏幕wiki技术网站：http://www.lcdwiki.com
//创建日期:2024/07/24
//版本：V1.0
//注：CCS打开会报很多警告，不影响使用，可以忽略（字体库报错）。
/****************************************************************************************************
//=========================================电源接线================================================//
//     LCD模块                MSPM0G3507
//      VCC          接        DC5V/3.3V      //电源
//      GND          接          GND          //电源地
//=======================================液晶屏数据线接线==========================================//
//本模块默认数据总线类型为SPI总线
//     LCD模块                     MSPM0G3507    
//    SDI(MOSI)PICO      接          PB8         //液晶屏SPI总线数据写信号
//    SDO(MISO)POCI      接          PB7         //液晶屏SPI总线数据读信号，如果不需要读，可以不接线
//=======================================液晶屏控制线接线==========================================//
//     LCD模块 					      MSPM0G3507 
//       LED         接          PB12          //液晶屏背光控制信号，如果不需要控制，接5V或3.3V
//       SCK         接          PB9         //液晶屏SPI总线时钟信号
//      DC/RS        接          PB15         //液晶屏数据/命令控制信号
//       RST         接          PB17         //液晶屏复位控制信号
//       CS          接          PB6         //液晶屏片选控制信号

**************************************************************************************************/	

#include "ti_msp_dl_config.h"
#include "gui.h"
#include "lcd.h"
#include "test.h"

int main(void)
{
    SYSCFG_DL_init();

    NVIC_EnableIRQ(TIMERG0_Alive_INST_INT_IRQN);
    DL_Timer_startCounter(TIMERG0_Alive_INST);

    LCD_Init();	   //液晶屏初始化
    while (1) 
    {
        main_test(); 		//测试主界面
        Test_Color();  		//简单刷屏填充测试
		Test_FillRec();		//GUI矩形绘图测试
		Test_Circle(); 		//GUI画圆测试
		Test_Triangle();    //GUI三角形绘图测试
		English_Font_test();//英文字体示例测试
		Chinese_Font_test();//中文字体示例测试
		Pic_test();			//图片显示示例测试
		Rotate_Test();   //旋转显示测试

    }
}

void TIMERG0_Alive_INST_IRQHandler(void)
{
    switch(DL_TimerG_getPendingInterrupt(TIMERG0_Alive_INST))
    {
        case DL_TIMER_IIDX_ZERO:
          DL_GPIO_togglePins(GPIO_LED_PORT,GPIO_LED_PA0_Alive_PIN);
          break;

        default:
          break;
    }
}