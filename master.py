#!/usr/bin/env python3
import rpyc

#TODO add ip adress
c_head = rpyc._connect_by_service("Head")
robot_head = c_head.root

#TODO add ip adress
c_left = rpyc._connect_by_service("Left")
robot_left = c_left.root

#TODO add ip adress
c_right = rpyc._connect_by_service("Right")
robot_right = c_right.root
