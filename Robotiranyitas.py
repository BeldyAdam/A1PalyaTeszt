#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor, InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile

class Robotiranyitas():

    def __init__(self):
        # tégla
        self.ev3 = EV3Brick()
        # motorok
        self.jm = Motor(Port.B)
        self.bm = Motor(Port.C)
        self.km = Motor(Port.A)
        # szenzorok
        self.cs = ColorSensor(Port.S3)
        self.ts = TouchSensor(Port.S1)
        self.gs = GyroSensor(Port.S2)
        # self.us = UltrasonicSensor(Port.S4)
        self.us = UltrasonicSensor(Port.S4)

        # dupla motorkezelő
        self.robot = DriveBase(self.jm, self.bm, 55, 115)

    def kulsoPalya(self):
        self.robot.straight(1900)
        self.robot.turn(-90)
        self.robot.straight(1900)
        self.robot.turn(-90)
        self.robot.straight(3000)
        self.robot.turn(-90)
        self.robot.straight(1900)
        self.robot.turn(-90)
        self.robot.straight(1100)

    def kozepsoPalya(self):
        self.robot.straight(100)
        self.robot.turn(-90)
        self.robot.straight(100)
        self.robot.turn(-90)
        self.robot.straight(100)
        self.robot.turn(-90)
        self.robot.straight(100)
        self.robot.turn(-90)
        self.robot.straight(100)

    def belsoPalya(self):
        self.robot.straight(100)
        self.robot.turn(-90)
        self.robot.straight(100)
        self.robot.turn(-90)
        self.robot.straight(100)
        self.robot.turn(-90)
        self.robot.straight(100)
        self.robot.turn(-90)
        self.robot.straight(100)