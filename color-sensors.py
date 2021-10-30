#!/usr/bin/env python3

import ev3dev2
import math
from time import sleep

from ev3dev2.sensor.lego import ColorSensor
from ev3dev2.sound import Sound
from ev3dev2.display import Display

display = Display()

snd = Sound()
snd.speak('Colors sensor now', play_type=Sound.PLAY_WAIT_FOR_COMPLETE)

c1 = ColorSensor()
while True:
    print('light: ' + str(c1.reflected_light_intensity))
    display.draw.text((10, 10), 'light: ' + str(c1.reflected_light_intensity))
    display.update()
    sleep(.01)
