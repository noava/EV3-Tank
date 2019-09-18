#!/usr/bin/env python3
import rpyc

#TODO add ip adress
c_head = rpyc.connect("localhost", 18861)
robot_head = c_head.root

#TODO add ip adress
c_left = rpyc.connect("localhost", 18862)
robot_left = c_left.root

#TODO add ip adress
c_right = rpyc.connect("localhost", 18863)
robot_right = c_right.root
