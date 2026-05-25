/*
 * Copyright (c) 2021, Texas Instruments Incorporated
 * All rights reserved.
 *
 * Redistribution and use in source and binary forms, with or without
 * modification, are permitted provided that the following conditions
 * are met:
 *
 * *  Redistributions of source code must retain the above copyright
 *    notice, this list of conditions and the following disclaimer.
 *
 * *  Redistributions in binary form must reproduce the above copyright
 *    notice, this list of conditions and the following disclaimer in the
 *    documentation and/or other materials provided with the distribution.
 *
 * *  Neither the name of Texas Instruments Incorporated nor the names of
 *    its contributors may be used to endorse or promote products derived
 *    from this software without specific prior written permission.
 *
 * THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
 * AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO,
 * THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR
 * PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT OWNER OR
 * CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL,
 * EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO,
 * PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS;
 * OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY,
 * WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR
 * OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE,
 * EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
 */

#include "ti_msp_dl_config.h"
#include "motor.h"

int16_t rxbuf = 0, cx = 160;
int16_t baseSpeed = 15;
int16_t SpeedL = 0, SpeedR = 0;
float Kp = 0.5;

void Motor_Ctrl(void);

int main(void)
{
    SYSCFG_DL_init();
    NVIC_ClearPendingIRQ(UART_OPENMV_INST_INT_IRQN);
    NVIC_EnableIRQ(UART_OPENMV_INST_INT_IRQN);

    while(DL_GPIO_readPins(GPIO_BUTTON_PORT, GPIO_BUTTON_PIN_S2_PIN));
    DL_UART_transmitDataBlocking(UART_OPENMV_INST, 'S');

    delay_cycles(32000000);

    Set_Speed(0, baseSpeed);
    Set_Speed(1, baseSpeed);
    Motor_On();

    while (1) 
    {
        Motor_Ctrl();
    }
}

void Motor_Ctrl(void)
{
    SpeedL = baseSpeed + (cx - 160)*Kp;
    SpeedR = baseSpeed - (cx - 160)*Kp;

    if(SpeedL > 30)
        SpeedL = 30;
    else if(SpeedL < 0)
        SpeedL = 0;

    if(SpeedR > 30)
        SpeedR = 30;
    else if(SpeedR < 0)
        SpeedR = 0;

    Set_Speed(0, SpeedL);
    Set_Speed(1, SpeedR);
}

void UART_OPENMV_INST_IRQHandler(void)
{
    uint8_t gData;
    switch (DL_UART_Main_getPendingInterrupt(UART_OPENMV_INST)) {
        case DL_UART_MAIN_IIDX_RX:
            gData = DL_UART_Main_receiveData(UART_OPENMV_INST);
            if(gData == 'S')
            {
                Motor_Off();
                DL_GPIO_clearPins(GPIO_LED_PORT, GPIO_LED_PIN_LED1_PIN);
            }
            else if(gData == '#')
                rxbuf = 0;
            else if(gData == '$')
                cx = rxbuf;
            else
                rxbuf = rxbuf*10 + (gData - '0');
            break;
        default:
            break;
    }
}