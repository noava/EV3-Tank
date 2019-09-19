#!/usr/bin/python3

"""
For ev3 which controls tank, gyro and stop sensor
"""

import rpyc
import time
from ev3dev2.motor import LargeMotor, MoveTank, OUTPUT_A, OUTPUT_B, OUTPUT_C, OUTPUT_D
from ev3dev2.sensor.lego import GyroSensor, TouchSensor
from ev3dev2.sensor import INPUT_1, INPUT_2, INPUT_3, INPUT_4

class RobotLeft(rpyc.Service):
    ALIASES = ['Left']

    def __init__(self, *args, **kwargs):
        self.exposed_tank_left = MoveTank(LargeMotor(OUTPUT_A), LargeMotor(OUTPUT_B))
        self.exposed_tank_right = MoveTank(LargeMotor(OUTPUT_C), LargeMotor(OUTPUT_D))
        self.exposed_gyro_up = GyroSensor(INPUT_1)
        self.exposed_gyro_side = GyroSensor(INPUT_2)
        self.exposed_stop = TouchSensor(INPUT_3)

        super().__init__(*args, **kwargs)

    def exposed_on_for_distance(self, length, speed, turn=0):
        degrees_left = degrees_right = length # TODO: Math to calculate how many degrees to run for and turn

        self.exposed_tank_left.on_for_degrees(speed, -speed, degrees_left)
        self.exposed_tank_right.on_for_degrees(speed, -speed, degrees_right)

    def exposed_on(self, left, right):
        self.exposed_tank_left.on(left, -left)
        self.exposed_tank_right.on(right, -right)

if __name__ == "__main__":
    from rpyc.utils.server import ThreadedServer
    t = ThreadedServer(RobotLeft, port=18862)
    t.start()