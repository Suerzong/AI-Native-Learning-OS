/*
 * Copyright (c) 2023, Texas Instruments Incorporated - http://www.ti.com
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

/*
 *  ============ ti_msp_dl_config.h =============
 *  Configured MSPM0 DriverLib module declarations
 *
 *  DO NOT EDIT - This file is generated for the MSPM0G350X
 *  by the SysConfig tool.
 */
#ifndef ti_msp_dl_config_h
#define ti_msp_dl_config_h

#define CONFIG_MSPM0G350X

#if defined(__ti_version__) || defined(__TI_COMPILER_VERSION__)
#define SYSCONFIG_WEAK __attribute__((weak))
#elif defined(__IAR_SYSTEMS_ICC__)
#define SYSCONFIG_WEAK __weak
#elif defined(__GNUC__)
#define SYSCONFIG_WEAK __attribute__((weak))
#endif

#include <ti/devices/msp/msp.h>
#include <ti/driverlib/driverlib.h>
#include <ti/driverlib/m0p/dl_core.h>

#ifdef __cplusplus
extern "C" {
#endif

/*
 *  ======== SYSCFG_DL_init ========
 *  Perform all required MSP DL initialization
 *
 *  This function should be called once at a point before any use of
 *  MSP DL.
 */


/* clang-format off */

#define POWER_STARTUP_DELAY                                                (16)


#define CPUCLK_FREQ                                                     32000000



/* Defines for PWM_MOTOR */
#define PWM_MOTOR_INST                                                     TIMA0
#define PWM_MOTOR_INST_IRQHandler                               TIMA0_IRQHandler
#define PWM_MOTOR_INST_INT_IRQN                                 (TIMA0_INT_IRQn)
#define PWM_MOTOR_INST_CLK_FREQ                                         32000000
/* GPIO defines for channel 0 */
#define GPIO_PWM_MOTOR_C0_PORT                                             GPIOA
#define GPIO_PWM_MOTOR_C0_PIN                                      DL_GPIO_PIN_8
#define GPIO_PWM_MOTOR_C0_IOMUX                                  (IOMUX_PINCM19)
#define GPIO_PWM_MOTOR_C0_IOMUX_FUNC                 IOMUX_PINCM19_PF_TIMA0_CCP0
#define GPIO_PWM_MOTOR_C0_IDX                                DL_TIMER_CC_0_INDEX
/* GPIO defines for channel 1 */
#define GPIO_PWM_MOTOR_C1_PORT                                             GPIOA
#define GPIO_PWM_MOTOR_C1_PIN                                      DL_GPIO_PIN_9
#define GPIO_PWM_MOTOR_C1_IOMUX                                  (IOMUX_PINCM20)
#define GPIO_PWM_MOTOR_C1_IOMUX_FUNC                 IOMUX_PINCM20_PF_TIMA0_CCP1
#define GPIO_PWM_MOTOR_C1_IDX                                DL_TIMER_CC_1_INDEX
/* GPIO defines for channel 2 */
#define GPIO_PWM_MOTOR_C2_PORT                                             GPIOB
#define GPIO_PWM_MOTOR_C2_PIN                                      DL_GPIO_PIN_0
#define GPIO_PWM_MOTOR_C2_IOMUX                                  (IOMUX_PINCM12)
#define GPIO_PWM_MOTOR_C2_IOMUX_FUNC                 IOMUX_PINCM12_PF_TIMA0_CCP2
#define GPIO_PWM_MOTOR_C2_IDX                                DL_TIMER_CC_2_INDEX
/* GPIO defines for channel 3 */
#define GPIO_PWM_MOTOR_C3_PORT                                             GPIOB
#define GPIO_PWM_MOTOR_C3_PIN                                      DL_GPIO_PIN_2
#define GPIO_PWM_MOTOR_C3_IOMUX                                  (IOMUX_PINCM15)
#define GPIO_PWM_MOTOR_C3_IOMUX_FUNC                 IOMUX_PINCM15_PF_TIMA0_CCP3
#define GPIO_PWM_MOTOR_C3_IDX                                DL_TIMER_CC_3_INDEX



/* Defines for UART_OPENMV */
#define UART_OPENMV_INST                                                   UART1
#define UART_OPENMV_INST_IRQHandler                             UART1_IRQHandler
#define UART_OPENMV_INST_INT_IRQN                                 UART1_INT_IRQn
#define GPIO_UART_OPENMV_RX_PORT                                           GPIOB
#define GPIO_UART_OPENMV_TX_PORT                                           GPIOB
#define GPIO_UART_OPENMV_RX_PIN                                    DL_GPIO_PIN_7
#define GPIO_UART_OPENMV_TX_PIN                                    DL_GPIO_PIN_6
#define GPIO_UART_OPENMV_IOMUX_RX                                (IOMUX_PINCM24)
#define GPIO_UART_OPENMV_IOMUX_TX                                (IOMUX_PINCM23)
#define GPIO_UART_OPENMV_IOMUX_RX_FUNC                 IOMUX_PINCM24_PF_UART1_RX
#define GPIO_UART_OPENMV_IOMUX_TX_FUNC                 IOMUX_PINCM23_PF_UART1_TX
#define UART_OPENMV_BAUD_RATE                                             (9600)
#define UART_OPENMV_IBRD_32_MHZ_9600_BAUD                                  (208)
#define UART_OPENMV_FBRD_32_MHZ_9600_BAUD                                   (21)





/* Port definition for Pin Group GPIO_BUTTON */
#define GPIO_BUTTON_PORT                                                 (GPIOB)

/* Defines for PIN_S2: GPIOB.21 with pinCMx 49 on package pin 20 */
#define GPIO_BUTTON_PIN_S2_PIN                                  (DL_GPIO_PIN_21)
#define GPIO_BUTTON_PIN_S2_IOMUX                                 (IOMUX_PINCM49)
/* Port definition for Pin Group GPIO_LED */
#define GPIO_LED_PORT                                                    (GPIOA)

/* Defines for PIN_LED1: GPIOA.0 with pinCMx 1 on package pin 33 */
#define GPIO_LED_PIN_LED1_PIN                                    (DL_GPIO_PIN_0)
#define GPIO_LED_PIN_LED1_IOMUX                                   (IOMUX_PINCM1)
/* Defines for PIN_FL1: GPIOA.26 with pinCMx 59 on package pin 30 */
#define GPIO_MOTOR_PIN_FL1_PORT                                          (GPIOA)
#define GPIO_MOTOR_PIN_FL1_PIN                                  (DL_GPIO_PIN_26)
#define GPIO_MOTOR_PIN_FL1_IOMUX                                 (IOMUX_PINCM59)
/* Defines for PIN_FL2: GPIOB.24 with pinCMx 52 on package pin 23 */
#define GPIO_MOTOR_PIN_FL2_PORT                                          (GPIOB)
#define GPIO_MOTOR_PIN_FL2_PIN                                  (DL_GPIO_PIN_24)
#define GPIO_MOTOR_PIN_FL2_IOMUX                                 (IOMUX_PINCM52)
/* Defines for PIN_FR1: GPIOB.9 with pinCMx 26 on package pin 61 */
#define GPIO_MOTOR_PIN_FR1_PORT                                          (GPIOB)
#define GPIO_MOTOR_PIN_FR1_PIN                                   (DL_GPIO_PIN_9)
#define GPIO_MOTOR_PIN_FR1_IOMUX                                 (IOMUX_PINCM26)
/* Defines for PIN_FR2: GPIOA.27 with pinCMx 60 on package pin 31 */
#define GPIO_MOTOR_PIN_FR2_PORT                                          (GPIOA)
#define GPIO_MOTOR_PIN_FR2_PIN                                  (DL_GPIO_PIN_27)
#define GPIO_MOTOR_PIN_FR2_IOMUX                                 (IOMUX_PINCM60)
/* Defines for PIN_BL1: GPIOB.3 with pinCMx 16 on package pin 51 */
#define GPIO_MOTOR_PIN_BL1_PORT                                          (GPIOB)
#define GPIO_MOTOR_PIN_BL1_PIN                                   (DL_GPIO_PIN_3)
#define GPIO_MOTOR_PIN_BL1_IOMUX                                 (IOMUX_PINCM16)
/* Defines for PIN_BL2: GPIOA.17 with pinCMx 39 on package pin 10 */
#define GPIO_MOTOR_PIN_BL2_PORT                                          (GPIOA)
#define GPIO_MOTOR_PIN_BL2_PIN                                  (DL_GPIO_PIN_17)
#define GPIO_MOTOR_PIN_BL2_IOMUX                                 (IOMUX_PINCM39)
/* Defines for PIN_BR1: GPIOA.24 with pinCMx 54 on package pin 25 */
#define GPIO_MOTOR_PIN_BR1_PORT                                          (GPIOA)
#define GPIO_MOTOR_PIN_BR1_PIN                                  (DL_GPIO_PIN_24)
#define GPIO_MOTOR_PIN_BR1_IOMUX                                 (IOMUX_PINCM54)
/* Defines for PIN_BR2: GPIOA.18 with pinCMx 40 on package pin 11 */
#define GPIO_MOTOR_PIN_BR2_PORT                                          (GPIOA)
#define GPIO_MOTOR_PIN_BR2_PIN                                  (DL_GPIO_PIN_18)
#define GPIO_MOTOR_PIN_BR2_IOMUX                                 (IOMUX_PINCM40)
/* Defines for PIN_FSTBY: GPIOB.19 with pinCMx 45 on package pin 16 */
#define GPIO_MOTOR_PIN_FSTBY_PORT                                        (GPIOB)
#define GPIO_MOTOR_PIN_FSTBY_PIN                                (DL_GPIO_PIN_19)
#define GPIO_MOTOR_PIN_FSTBY_IOMUX                               (IOMUX_PINCM45)
/* Defines for PIN_BSTBY: GPIOB.13 with pinCMx 30 on package pin 1 */
#define GPIO_MOTOR_PIN_BSTBY_PORT                                        (GPIOB)
#define GPIO_MOTOR_PIN_BSTBY_PIN                                (DL_GPIO_PIN_13)
#define GPIO_MOTOR_PIN_BSTBY_IOMUX                               (IOMUX_PINCM30)

/* clang-format on */

void SYSCFG_DL_init(void);
void SYSCFG_DL_initPower(void);
void SYSCFG_DL_GPIO_init(void);
void SYSCFG_DL_SYSCTL_init(void);
void SYSCFG_DL_PWM_MOTOR_init(void);
void SYSCFG_DL_UART_OPENMV_init(void);


bool SYSCFG_DL_saveConfiguration(void);
bool SYSCFG_DL_restoreConfiguration(void);

#ifdef __cplusplus
}
#endif

#endif /* ti_msp_dl_config_h */
