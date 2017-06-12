#!/usr/bin/env python3
import cozmo
from cozmo.util import degrees, distance_mm, speed_mmps
import sys

class bcolors:
    OK = '\033[92m'
    LOW = '\033[91m'
    MEDIUM = '\033[33m'
    NORMAL = '\033[0m'

def cozmo_program(robot: cozmo.robot.Robot):

    nivel = robot.battery_voltage
    if nivel < 3.5:
        print (bcolors.LOW + "Bateria baja: " + bcolors.NORMAL + nivel)
        robot.say_text('low battery').wait_for_completed()

    if nivel > 3.5 and nivel < 4:
        print (bcolors.MEDIUM + "Bateria media: " + bcolors.NORMAL + str(nivel))
        robot.say_text('medium battery level').wait_for_completed()

    else:
        print (bcolors.OK + "Nivel de bateria OK: " + bcolors.NORMAL + str(nivel))
        robot.say_text('battery is Ok').wait_for_completed()

    robot.drive_straight(distance_mm(-10), speed_mmps(50)).wait_for_completed()
#
cozmo.run_program(cozmo_program)
