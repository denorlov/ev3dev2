#!/usr/bin/env python3

# Import the necessary libraries
from ev3dev2.motor import *
from ev3dev2.sound import Sound

# Create the sensors and motors objects
motorA = LargeMotor(OUTPUT_A)
motorB = LargeMotor(OUTPUT_B)
left_motor = motorA
right_motor = motorB

spkr = Sound()

# Here is where your code starts

left_motor.position = 0
right_motor.position = 0
spkr.speak('start')
motorA.on(20)
motorB.on_for_rotations(20, 5)
motorA.off()
motorB.off()
spkr.speak('right')
motorA.on_for_rotations(20, 1.4)
spkr.speak('forward')
motorA.on(20)
motorB.on_for_rotations(20, 5)
motorA.off()
motorB.off()