#!/usr/bin/python3

"""
For ev3 which controls motor for suport and distance sensor
"""

import rpyc
import time
from ev3dev2.motor import LargeMotor, MediumMotor, OUTPUT_A, OUTPUT_B, OUTPUT_D
from ev3dev2.sensor.lego import UltrasonicSensor
from ev3dev2.sensor import INPUT_1, INPUT_2, INPUT_3, INPUT_4

class RobotHead(rpyc.Service):
    def __init__(self, *args, **kwargs):
        self.exposed_support_tilt = LargeMotor(OUTPUT_A)
        self.exposed_support_power = LargeMotor(OUTPUT_B)
        self.exposed_right_us = UltrasonicSensor(INPUT_1)
        self.exposed_left_us = UltrasonicSensor(INPUT_2)
        self.exposed_drop_us = UltrasonicSensor(INPUT_3)
        self.exposed_rear_us = UltrasonicSensor(INPUT_4)

        super().__init__(*args, **kwargs)

    def exposed_lower_support(self):
        self.exposed_support_tilt.on(-100)
        while self.exposed_rear_us.distance_centimeters > 5:
            time.sleep(0.01)
        self.exposed_support_tilt.on(0, True)

    def exposed_raise_support(self):
        self.exposed_support_tilt.on_for_degrees(25, 540)

if __name__ == "__main__":
    from rpyc.utils.server import ThreadedServer
    t = ThreadedServer(RobotHead, port=18861)
    t.start()