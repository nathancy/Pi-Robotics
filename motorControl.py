#!/usr/bin/env python
# Motor Control for Raspberry Pi with MC33886 Motor Driver Board
# http://www.robotshop.com/en/mc33886-raspberry-pi-motor-driver-board-raspberry-pi.html

#-------------------------------------------------------------------------------
#### Imports ####
 
import time, sys, tempfile, os, string, shutil
import RPi.GPIO as gpio

#### Constants ####


#-------------------------------------------------------------------------------
# Assign GPIO pins to variables

# Pins for motors 
_RIGHT_MOTOR_FORWARD=11
_RIGHT_MOTOR_BACKWARD=7
_LEFT_MOTOR_FORWARD=15
_LEFT_MOTOR_BACKWARD=13

# Step duration is used for forward and backward commands.
_STEP_DURATION=1000

# Turn duration in milliseconds.
_TURN_DURATION=700

#-------------------------------------------------------------------------------
# Set up the GPIO pins
#***Set up motor pins
gpio.setwarnings(False)
gpio.setmode(gpio.BOARD)
gpio.setup(_RIGHT_MOTOR_FORWARD, gpio.OUT)
gpio.setup(_RIGHT_MOTOR_BACKWARD, gpio.OUT)
gpio.setup(_LEFT_MOTOR_FORWARD, gpio.OUT)
gpio.setup(_LEFT_MOTOR_BACKWARD, gpio.OUT)

# "Turn off" all motors
gpio.output(_LEFT_MOTOR_FORWARD, False)
gpio.output(_LEFT_MOTOR_BACKWARD, False)
gpio.output(_RIGHT_MOTOR_FORWARD, False)
gpio.output(_RIGHT_MOTOR_BACKWARD, False)

#### Objects ####

#-------------------------------------------------------------------------------
class MotorControl(object):
    # Make sure there is only one instance of MotorControl

    _instances=[]

    # Initialize the object
    def __init__(self):
        if ( len(self._instances)>1 ):
            print("ERROR: One instance of MotorControl is running already.")
            exit(1)
        self._instances.append(self)

        
#-------------------------------------------------------------------------------    
    # Move FORWARD so many units
    def forward(self):
#       for step in range(0,units):
        print("Forward")
        gpio.output(_LEFT_MOTOR_FORWARD, True)
        gpio.output(_LEFT_MOTOR_BACKWARD, False)
        gpio.output(_RIGHT_MOTOR_FORWARD, True)
        gpio.output(_RIGHT_MOTOR_BACKWARD, False)
        
#        time.sleep (_STEP_DURATION/1000)
        
#        gpio.output(_LEFT_MOTOR_FORWARD, False)
#        gpio.output(_RIGHT_MOTOR_FORWARD, False)
            
            
#-------------------------------------------------------------------------------
    # Move BACKWARD so many units
    def backward(self,units):
#        for step in range(0,units):
         print("Going Backward")
         gpio.output(_LEFT_MOTOR_FORWARD, False)
         gpio.output(_LEFT_MOTOR_BACKWARD, True)
         gpio.output(_RIGHT_MOTOR_FORWARD, False)
         gpio.output(_RIGHT_MOTOR_BACKWARD, True)

#            time.sleep (_STEP_DURATION/1000)
            
#            gpio.output(_LEFT_MOTOR_BACKWARD, False)
#            gpio.output(_RIGHT_MOTOR_BACKWARD, False)            

#-------------------------------------------------------------------------------
    # Move RIGHT so many units
    def right(self,units):
        for step in range(0,units):
            print("Right")
            gpio.output(_LEFT_MOTOR_FORWARD, True)
            gpio.output(_LEFT_MOTOR_BACKWARD, False)
            gpio.output(_RIGHT_MOTOR_FORWARD, False)
            gpio.output(_RIGHT_MOTOR_BACKWARD, True)

            time.sleep (_TURN_DURATION/1000)
            
            gpio.output(_LEFT_MOTOR_FORWARD, False)
            gpio.output(_RIGHT_MOTOR_BACKWARD, False)
						
#-------------------------------------------------------------------------------
    # Move LEFT so many units
    def left(self,units):
        for step in range(0,units):
            print("Left")
            gpio.output(_LEFT_MOTOR_FORWARD, False)
            gpio.output(_LEFT_MOTOR_BACKWARD, True)
            gpio.output(_RIGHT_MOTOR_FORWARD, True)
            gpio.output(_RIGHT_MOTOR_BACKWARD, False)

            time.sleep (_TURN_DURATION/1000)
            
            gpio.output(_LEFT_MOTOR_BACKWARD, False)
            gpio.output(_RIGHT_MOTOR_FORWARD, False)       

#-------------------------------------------------------------------------------           
    # STOP all the motors
    def allStop(self):
        gpio.output(_LEFT_MOTOR_FORWARD, False)
        gpio.output(_LEFT_MOTOR_BACKWARD, False)
        gpio.output(_RIGHT_MOTOR_FORWARD, False)
        gpio.output(_RIGHT_MOTOR_BACKWARD, False)

#-------------------------------------------------------------------------------
    #clean up GPIO
    def cleanup (self):
        gpio.cleanup()
