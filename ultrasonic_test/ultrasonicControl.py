#!/usr/bin/env python
# Ultrasonic Control for Raspberry Pi with HC-SR04 

#-------------------------------------------------------------------------------
#### Imports ####

import time
import numpy as np
import RPi.GPIO as GPIO 

#### Constants ####

#-------------------------------------------------------------------------------
# GPIO Mode (BOARD/BCM)
GPIO.setmode(GPIO.BOARD)

# Assign GPIO pins to variables
_ULTRASONIC_TRIG=16
_ULTRASONIC_ECHO=12

# Set up ultrasonic pins
# Ultrasonic sensor TRIG pin is input so set the pin on the PI as output
# Ultrasonic sensor ECHO pin is output so set the pin on the PI as input
GPIO.setup(_ULTRASONIC_TRIG, GPIO.OUT)
GPIO.setup(_ULTRASONIC_ECHO, GPIO.IN)

#### Objects ####

#-------------------------------------------------------------------------------
class UltrasonicControl(object):
    # Make sure there is only one instance of UltrasonicControl  

    _instances=[]

    # Initialize the object
    def __init__(self):
        if ( len(self._instances)>1 ):
            print("ERROR: One instance of UltrasonicControl is running already.")
            exit(1)
        self._instances.append(self)									
#-------------------------------------------------------------------------------        
    # Properly close GPIO pins
    def cleanup(self):
        GPIO.cleanup()

#-------------------------------------------------------------------------------        
    # Read DISTANCE ahead of the robot. We are taking 5 readings and averaging the values.
    # reads distance data in centimeters
    # Set mode 0 for raw data, set mode 1 for rounded data
    def distance(self, mode):
    
        # Create array to hold gathered data from ultrasonic readings
        ultrasonic_data = []

        for num in range(5):
            # set Trigger to HIGH
            GPIO.output(_ULTRASONIC_TRIG, True)
         
            # set Trigger after 0.01ms to LOW
            time.sleep(0.00001)
            GPIO.output(_ULTRASONIC_TRIG, False)
         
            StartTime = time.time()
            StopTime = time.time()
         
            # save StartTime
            while GPIO.input(_ULTRASONIC_ECHO) == 0:
                StartTime = time.time()
         
            # save time of arrival
            while GPIO.input(_ULTRASONIC_ECHO) == 1:
                StopTime = time.time()
         
            # time difference between start and arrival
            TimeElapsed = StopTime - StartTime

            # multiply with the sonic speed (34300 cm/s)
            # and divide by 2, because there and back
            distance = (TimeElapsed * 34300) / 2

            ultrasonic_data.append(distance)
         
        # Creating numpy 2d array
        ultrasonic_data = np.array(ultrasonic_data)
        m = 2.

        # Find median and remove outliers
        tempvar = np.abs(ultrasonic_data - np.median(ultrasonic_data))
        median = np.median(tempvar)
        s = tempvar/median if median else 0

        # Array updated with values without outliers
        filtered_values = ultrasonic_data[s<m]

        # Take mean of all remaining values
        distance = round(np.mean(filtered_values))
        
        # Return raw data
        if (mode == 0):
            return distance
        # Return rounded data to two decimal places
        elif mode == 1:
            return round(distance,2)

