#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile
import Robotiranyitas
# This program requires LEGO EV3 MicroPython v2.0 or higher.
# Click "Open user guide" on the EV3 extension tab for more information.

#főprogram
#robotom=Robotiranyitas():
oraiFeladat = Robotiranyitas.Robotiranyitas()

# Create your objects here.




oraiFeladat.kulsoPalya()

# Write your program here

#Robot irányítása

ev3.speaker.beep()