#include "ti_msp_dl_config.h"
#include "delay.h"

//设置CPU频率
#define CPU_Frequency 32000000
/*
 *函数名称：elay_cycles(cycles)
 *   功能：延时指定周期的CPU时钟
 *   参数：cycles：延时周期，单位为CPU时钟
 *   说明：CPU周期为1/32000000秒
 *         1us=32/32000000=10e-6秒              延时1us需要32个CPU时钟
 *         1ms=1000us=32000个CPU时钟=10e-3秒     延时1ms需要32000个CPU时钟
 *
 *
 *      
*/


void delay_us(uint32_t us)
{
    delay_cycles(32*us);
}



void delay_ms(uint32_t ms)
{
    delay_cycles(32000*ms);
}