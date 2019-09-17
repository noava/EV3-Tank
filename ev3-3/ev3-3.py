#!/usr/bin/python3
import rpyc
from ev3dev2.motor import LargeMotor, MediumMotor, OUTPUT_A, OUTPUT_B, OUTPUT_D
from ev3dev2.sensor.lego import UltrasonicSensor
from ev3dev2.sensor import INPUT_A

class RobotHead(rpyc.Service):
    def __init__(self):
        self._support_tilt = LargeMotor(OUTPUT_A)
        self._support_power = LargeMotor(OUTPUT_B)
        self._arm = MediumMotor(OUTPUT_D)
        self._rear_us = UltrasonicSensor(INPUT_A)
        super().__init__()

    @property
    def rear_us(self):
        return self._rear_us = 

    @property
    def support_tilt(self):
        return self._support_tilt

    @property
    def support_power(self):
        return self._support_power

    @support_power.setter
    def _support_power_setter(self, value):
        self.support_power.on(value, False)

    def lower_support(self):
        self.support_tilt.on(-100)
        while self.rear_us.distance_centimeters > 5:
            time.sleep(0.01)
        self.support_tilt.on(0, True)

    @property
    def arm(self):
        return self._arm

    def grab(self):
        pass

    def release(self):
        pass

    