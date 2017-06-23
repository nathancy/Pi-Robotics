#!/usr/bin/env python
# Sonar Control for Raspberry Pi with HC-SR04 

#-------------------------------------------------------------------------------
#### Imports ####

import time
import numpy as np
import RPi.GPIO as gpio

#### Constants ####

#-------------------------------------------------------------------------------
# Assign GPIO pins to variables

# Pins for sonar
_SONAR_OUT=16
_SONAR_IN=12

#***Set up sonar pins
gpio.setup(_SONAR_OUT, gpio.OUT)
gpio.setup(_SONAR_IN, gpio.IN)

#### Objects ####

#-------------------------------------------------------------------------------
class SonarControl(object):
    # Make sure there is only one instance of SonarControl

    _instances=[]

    # Initialize the object
    def __init__(self):
        if ( len(self._instances)>1 ):
            print "ERROR: One instance of SonarControl is running already."
            exit(1)
        self._instances.append(self)									

#-------------------------------------------------------------------------------        
    # Read DISTANCE ahead of the robot. We are taking 5 readings, removing outliers and averaging the rest of the values.
    def distance(self):
        #initializing sensor
        gpio.output(_SONAR_OUT, gpio.LOW)
        time.sleep(0.3)

        #creating an array to hold gathered data from sonar
        d = []
        #take 5 readings
        for i in range(0,5):
            #sending pulse
            gpio.output(_SONAR_OUT, True)
            
            #waiting 10 micro seconds
            time.sleep(0.00001)
            
            #stopping pulse
            gpio.output(_SONAR_OUT, False)
            
            #listening for the pulse
            while gpio.input(_SONAR_IN)== 0:
                signaloff = time.time()
                
            #record the time
            while gpio.input(_SONAR_IN)== 1:
                signalon = time.time()
                          
            #find out the difference
            timepassed = signalon - signaloff
            
            #convert the value above into centimeters
            distance = timepassed * 17000
            
            #insert read value into d[] array
            d.append(distance)
            
        d=np.array(d) #creating numpy 2d array
        m=2.
        
        #finding a median and removing outliers
        tempvar = np.abs(d - np.median(d))
        mdev = np.median(tempvar)
        s = tempvar/mdev if mdev else 0
        
        filtered_values = d[s<m] #this is an array updated with values without outliers
        
        prefinal = round(np.mean(filtered_values)) #taking the mean of all remaining values
        
        distance = int(prefinal) #converting the value to integer
        
        #return the distance
        return distance
        
