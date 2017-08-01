#!/usr/bin/env python
# Motor Control for Raspberry Pi with MC33886 Motor Driver Board
# Product: http://www.robotshop.com/en/mc33886-raspberry-pi-motor-driver-board-raspberry-pi.html
# Datasheet: http://www.robotshop.com/media/files/pdf2/rpi_motor_driver_board_-_waveshare_wiki.pdf
# Schematic: http://www.robotshop.com/media/files/pdf2/rpi-motor-driver-board-schematic.pdf

'''
On the Motor Driver board, M1 and M2 are connected to the right motor while
M3 and M4 are connected to the left motor. The orientation of the actual 
(black or red wire) doesn't matter when connected to the motor driver board. 
Motors are interally controlled by outputting signals through GPIO.
PWMA and PWMB are output enable pins. When driven high, the PWM pulse will be 
outputted from the motor pins to control the speed of the motor.

          Interface       Pin name
-------------------------------------------------------------------------------
Right motor: M1        --> _RIGHT_MOTOR_1
             M2        --> _RIGHT_MOTOR_2
             PWMA      --> _RIGHT_MOTOR_PWM_SPEED

Left motor:  M3        --> _LEFT_MOTOR_1
             M4        --> _LEFT_MOTOR_2
             PWMB      --> _LEFT_MOTOR_PWM_SPEED

The orientation of the driver board taken from the data sheet 

   Left motor              Right motor

M3           M4          M1           M2        

'''
#-------------------------------------------------------------------------------
#### Imports ####
 
import time
import RPi.GPIO as GPIO

#### Constants ####

#-------------------------------------------------------------------------------
# GPIO Mode (BOARD/BCM)
GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)

# Assign GPIO pins for motors
# Right motor
_RIGHT_MOTOR_1 = 38
_RIGHT_MOTOR_2 = 40

# Left motor
_LEFT_MOTOR_1 = 31
_LEFT_MOTOR_2 = 33

# Output enable pins (active high enable)
# Right motor
_RIGHT_MOTOR_PWM_SPEED = 37
# Left motor
_LEFT_MOTOR_PWM_SPEED = 32

# Step duration is used for forward and backward commands.
_STEP_DURATION = 1000

# Controls motor strength
_MOTOR_SPEED = 1000

# Turn duration in milliseconds.
_TURN_DURATION = 1800
#-------------------------------------------------------------------------------
# Set up the motor GPIO pins
GPIO.setup(_RIGHT_MOTOR_1, GPIO.OUT)
GPIO.setup(_RIGHT_MOTOR_2, GPIO.OUT)
GPIO.setup(_LEFT_MOTOR_1, GPIO.OUT)
GPIO.setup(_LEFT_MOTOR_2, GPIO.OUT)
GPIO.setup(_RIGHT_MOTOR_PWM_SPEED, GPIO.OUT)
GPIO.setup(_LEFT_MOTOR_PWM_SPEED, GPIO.OUT)

# Settings for motors to run straight
''' MOTOR SETTINGS FOR CAR #1 Coordinator 

p1 = GPIO.PWM(_RIGHT_MOTOR_PWM_SPEED, 1550)
p2 = GPIO.PWM(_LEFT_MOTOR_PWM_SPEED, _MOTOR_SPEED)

'''
''' MOTOR SETTINGS FOR CAR #2 Router

p1 = GPIO.PWM(_RIGHT_MOTOR_PWM_SPEED, 1050)
p2 = GPIO.PWM(_LEFT_MOTOR_PWM_SPEED, _MOTOR_SPEED)

'''

p1 = GPIO.PWM(_RIGHT_MOTOR_PWM_SPEED, 1550)
p2 = GPIO.PWM(_LEFT_MOTOR_PWM_SPEED, _MOTOR_SPEED)

p1.start(50)
p2.start(50)

# Initially "Turn off" all motors
GPIO.output(_RIGHT_MOTOR_1, False)
GPIO.output(_RIGHT_MOTOR_2, False)
GPIO.output(_LEFT_MOTOR_1, False)
GPIO.output(_LEFT_MOTOR_2, False)

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
    # Move FORWARD 
    def forward(self):
        #print("Forward")
        GPIO.output(_RIGHT_MOTOR_1, False)
        GPIO.output(_RIGHT_MOTOR_2, True)
        GPIO.output(_LEFT_MOTOR_1, True)
        GPIO.output(_LEFT_MOTOR_2, False)
        
        '''
        time.sleep (_STEP_DURATION/1000)
        
        GPIO.output(_RIGHT_MOTOR_1, False)
        GPIO.output(_LEFT_MOTOR_2, False)
	'''
            
#-------------------------------------------------------------------------------
    # Move BACKWARD 
    def backward(self):
        #print("Backward")
        GPIO.output(_RIGHT_MOTOR_1, True)
        GPIO.output(_RIGHT_MOTOR_2, False)
        GPIO.output(_LEFT_MOTOR_1, False)
        GPIO.output(_LEFT_MOTOR_2, True)

        '''
        time.sleep (_STEP_DURATION/1000)
        
        GPIO.output(_RIGHT_MOTOR_2, False)
        GPIO.output(_LEFT_MOTOR_1, False)
	'''

#-------------------------------------------------------------------------------
    # Move RIGHT 
    def right(self):
        #print("right")
        GPIO.output(_RIGHT_MOTOR_1, True)
        GPIO.output(_RIGHT_MOTOR_2, False)
        GPIO.output(_LEFT_MOTOR_1, True)
        GPIO.output(_LEFT_MOTOR_2, False) 
        
        '''
        time.sleep (_TURN_DURATION/1000)
        
        GPIO.output(_RIGHT_MOTOR_1, False)
        GPIO.output(_LEFT_MOTOR_1, False)
	'''

#-------------------------------------------------------------------------------
    # Move LEFT 
    def left(self):
        #print("Left")
        GPIO.output(_RIGHT_MOTOR_1, False)
        GPIO.output(_RIGHT_MOTOR_2, True)
        GPIO.output(_LEFT_MOTOR_1, False)
        GPIO.output(_LEFT_MOTOR_2, True)
       
        '''
        time.sleep (_TURN_DURATION/1000)
        
        GPIO.output(_RIGHT_MOTOR_2, False)
        GPIO.output(_LEFT_MOTOR_1, False)
        '''

#-------------------------------------------------------------------------------           
    # STOP all the motors
    def stop(self):
        GPIO.output(_RIGHT_MOTOR_1, False)
        GPIO.output(_RIGHT_MOTOR_2, False)
        GPIO.output(_LEFT_MOTOR_1, False)
        GPIO.output(_LEFT_MOTOR_2, False)

#-------------------------------------------------------------------------------
    # Properly clean up GPIO
    def cleanup (self):
        GPIO.cleanup()

