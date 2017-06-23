#!/usr/bin/env python
# Servo Control for Raspberry Pi with Adafruit servo control board 

#-------------------------------------------------------------------------------
#### Imports ####
# Download this file from github: https://github.com/adafruit/Adafruit-Raspberry-Pi-Python-Code/blob/master/Adafruit_PWM_Servo_Driver/Adafruit_PWM_Servo_Driver.py

import time
from Adafruit_PWM_Servo_Driver import PWM

#### Constants ####

#-------------------------------------------------------------------------------
#### Servo Initialization

#I2C address is 0x40
pwm = PWM(0x40)
#Servo frequency 50Hz
pwm.setPWMFreq(50)

# these values cannot be smaller than 104 and more than 521; otherwise your servos may be damaged. Use at your own risk!
_PAN_SERVO_CHANNEL=0
_TILT_SERVO_CHANNEL=1

_PAN_SERVO_LEFT=200
_PAN_SERVO_RIGHT=520
_PAN_SERVO_CENTER=225

_TILT_SERVO_CHANNEL=1
_TILT_SERVO_UP=200
_TILT_SERVO_DOWN=520
_TILT_SERVO_CENTER=225


#### Objects ####

#-------------------------------------------------------------------------------
class ServoControl(object):
    # Make sure there is only one instance of ServoControl

    _instances=[]

    # Initialize the object
    def __init__(self):
        if ( len(self._instances)>1 ):
            print("ERROR: One instance of ServoControl is running already.")
            exit(1)
        self._instances.append(self)

#-------------------------------------------------------------------------------        
    # "Look" left
    def panleft(self):
        pwm.setPWM(_PAN_SERVO_CHANNEL, 0, _PAN_SERVO_LEFT)
#-------------------------------------------------------------------------------        
    # "Look" right
    def panright(self):
        pwm.setPWM(_PAN_SERVO_CHANNEL, 0, _PAN_SERVO_RIGHT)
#-------------------------------------------------------------------------------        
    # Position pan servo in the middle
    def pancenter(self):
        pwm.setPWM(_PAN_SERVO_CHANNEL, 0, _PAN_SERVO_LEFT)
#-------------------------------------------------------------------------------        
    # "Look" up
    def tiltup(self):
        pwm.setPWM(_TILT_SERVO_CHANNEL, 0, _TILT_SERVO_UP)
#-------------------------------------------------------------------------------        
    # "Look" down
    def tiltdown(self):
        pwm.setPWM(_TILT_SERVO_CHANNEL, 0, _TILT_SERVO_DOWN)
#-------------------------------------------------------------------------------        
    # Position tilt servo in the middle
    def tiltcenter(self):
        pwm.setPWM(_TILT_SERVO_CHANNEL, 0, _TILT_SERVO_CENTER)
