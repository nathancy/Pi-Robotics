#!/usr/bin/env python
# Motor Control for Raspberry Pi with MC33886 Motor Driver Board
# http://www.robotshop.com/en/mc33886-raspberry-pi-motor-driver-board-raspberry-pi.html

#-------------------------------------------------------------------------------
#### Imports ####
 
import time
import RPi.GPIO as GPIO

#### Constants ####

#-------------------------------------------------------------------------------
# Assign GPIO pins to variables

# Pins for motors 

# Step duration is used for forward and backward commands.

# Turn duration in milliseconds.
_TURN_DURATION = 1800
#-------------------------------------------------------------------------------
# Set up the GPIO pins
#***Set up motor pins

# Right
M1 = 38
M2 = 40

# Left
M3 = 31
M4 = 33
PWMA = 37
PWMB = 32

GPIO.setmode(GPIO.BOARD)
GPIO.setup(M1, GPIO.OUT)
GPIO.setup(M2, GPIO.OUT)
GPIO.setup(M3, GPIO.OUT)
GPIO.setup(M4, GPIO.OUT)
GPIO.setup(PWMA, GPIO.OUT)
GPIO.setup(PWMB, GPIO.OUT)

p1 = GPIO.PWM(PWMA, 5000)
p2 = GPIO.PWM(PWMB, 5000)
p1.start(50)
p2.start(50)

# "Turn off" all motors
GPIO.output(M1, False)
GPIO.output(M2, False)
GPIO.output(M3, False)
GPIO.output(M4, False)

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
        GPIO.output(M1, True)
        GPIO.output(M2, False)
        GPIO.output(M3, False)
        GPIO.output(M4, True)
        
#        time.sleep (_STEP_DURATION/1000)
        
#        GPIO.output(_LEFT_MOTOR_FORWARD, False)
#        GPIO.output(_RIGHT_MOTOR_FORWARD, False)
            
            
#-------------------------------------------------------------------------------
    # Move BACKWARD so many units
    def backward(self):
#        for step in range(0,units):
         print("Going Backward")
         GPIO.output(M1, False)
         GPIO.output(M2, True)
         GPIO.output(M3, True)
         GPIO.output(M4, False)

#            time.sleep (_STEP_DURATION/1000)
            
#            GPIO.output(_LEFT_MOTOR_BACKWARD, False)
#            GPIO.output(_RIGHT_MOTOR_BACKWARD, False)            

#-------------------------------------------------------------------------------
    # Move RIGHT so many units
    def right(self):
        #for step in range(0,units):
            print("Right")


            GPIO.output(M1, True)
            GPIO.output(M2, False)
            GPIO.output(M3, True)
            GPIO.output(M4, False) #
            
            #time.sleep (_TURN_DURATION/1000)
            '''
            time.sleep (_TURN_DURATION/1000)
            
            GPIO.output(M2, False)
            GPIO.output(M3, False)
	    '''

#-------------------------------------------------------------------------------
    # Move LEFT so many units
    def left(self):
#        for step in range(0,units):
            print("Left")

            GPIO.output(M1, False)
            GPIO.output(M2, True)
            GPIO.output(M3, False)
            GPIO.output(M4, True)
           
            '''
            time.sleep (_TURN_DURATION/1000)
            
            GPIO.output(M2, False)
            GPIO.output(M3, False)
            '''

#-------------------------------------------------------------------------------           
    # STOP all the motors
    def allStop(self):
        GPIO.output(M1, False)
        GPIO.output(M2, False)
        GPIO.output(M3, False)
        GPIO.output(M4, False)

#-------------------------------------------------------------------------------
    #clean up GPIO
    def cleanup (self):
        GPIO.cleanup()



