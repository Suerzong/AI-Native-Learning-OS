# Hello World Example
#
# Welcome to the OpenMV IDE! Click on the green run arrow button below to run the script!

import sensor
import time
from machine import UART, LED

sensor.reset()  # Reset and initialize the sensor.
sensor.set_pixformat(sensor.RGB565)  # Set pixel format to RGB565 (or GRAYSCALE)
sensor.set_framesize(sensor.QVGA)  # Set frame size to QVGA (320x240)
sensor.skip_frames(time=2000)  # Wait for settings take effect.
clock = time.clock()  # Create a clock object to track the FPS.

black = (32, 100, -128, 127, -128, 127)
uart = UART(1, 9600)

LED("LED_RED").on()

while uart.any()==0:
    continue

LED("LED_BLUE").on()
LED("LED_GREEN").on()

while True:
    img = sensor.snapshot()  # Take a picture and return the image.
    blobs = img.find_blobs([black], invert=True, roi = [0,100,320,48])

    if len(blobs) == 2:
        img.draw_rectangle([0,100,320,48])
        img.draw_rectangle(blobs[0][0:4], color = (0, 255, 0))
        img.draw_rectangle(blobs[1][0:4], color = (0, 255, 0))
        c = int((blobs[0].cx()+blobs[1].cx())*0.5)
        img.draw_cross(c, 124, (255, 0, 0), size = 5)
        uart.write('#'+str(c)+'$')
        print('#'+str(c)+'$')
    elif len(blobs) == 0:
        uart.write('S')
        print('S')
        LED("LED_GREEN").off()
        while True:
            continue
