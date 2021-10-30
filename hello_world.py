#!/usr/bin/env python3

import math
from ev3dev2.sound import Sound
from ev3dev2.led import *

sound = Sound()

sound.speak('Hello, Denis! Glad to see you! I am robot verter! Ha-ha-ha!')
Leds.all_off()
time.sleep(.1)

# cycle LEDs like a traffic light
sound.speak('traffic light!')
print('traffic light')

for _ in range(3):
    for color in (Leds.GREEN, Leds.YELLOW, Leds.RED):
        for group in (Leds.LEFT, Leds.RIGHT):
            Leds.set_color(group, color)
        time.sleep(0.5)

print('Color fade!')

for i in range(360):
    rd = math.radians(10 * i)
    Leds.red_left.brightness_pct = .5 * (1 + math.cos(rd))
    Leds.green_left.brightness_pct = .5 * (1 + math.sin(rd))
    Leds.red_right.brightness_pct = .5 * (1 + math.sin(rd))
    Leds.green_right.brightness_pct = .5 * (1 + math.cos(rd))
    time.sleep(0.05)