#!/usr/bin/env python3

"""
For ev3 which controls motor for candy and color sensor
"""

import rpyc
import time
from ev3dev2.motor import MediumMotor, OUTPUT_A, OUTPUT_B
from ev3dev2.sensor.lego import ColorSensor
from ev3dev2.sensor import INPUT_1, INPUT_2


class RobotRight(rpyc.Service):
    def __init__(self, *args, **kwargs):
        self.exposed_candy_loader = MediumMotor(OUTPUT_A)
        self.exposed_candy_thrower = MediumMotor(OUTPUT_B)
        self.exposed_left_cs = ColorSensor(INPUT_1)
        self.exposed_right_cs = ColorSensor(INPUT_2)

        super().__init__(*args, **kwargs)
    
    def exposed_candy_throw(self):
        # TODO fix value
        ### Loade the candy in the thrower
        self.exposed_candy_loader.on_for_degrees(80,75)
        self.exposed_candy_loader.on_for_degrees(80,-75)

        ### Throwe the candy
        self.exposed_candy_thrower.on_for_degrees(100,90)
        self.exposed_candy_thrower.on_for_degrees(50,-90)
