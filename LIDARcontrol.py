#!/usr/bin/env python
# Read LIDAR sensor data on Raspberry Pi from Arduino through serial

#-------------------------------------------------------------------------------
#### Imports ####

import serial
from pprint import pprint
import re

#### Objects ####

#-------------------------------------------------------------------------------        
# Open serial port
ser = serial.Serial('/dev/ttyACM0', 115200)

# Set number of readings to take, a higher value provides more precise readings
ACCURACY = 10

class LIDARControl(object):

    # Make sure there is only one instance of LIDARControl
    _instances=[]

    # Initialize the object
    def __init__(self):
        if (len(self._instances) > 1):
            print("ERROR: One instance of LIDARControl is running already.")
            exit(1)
        self._instances.append(self)							 

    # Reads the serial port for LIDAR sensor reading from Arduino
    def distance(self):
       
        total = 0

        # Poll the sensor and average out the readings according to the desired precision
        for num in range(ACCURACY):
            # Read serial port and extract only digits
            sensor_reading = str(ser.readline())
            clean_sensor_reading = re.findall(r'\d+', sensor_reading)
              
            # Ensure reading is valid 
            if len(clean_sensor_reading) is 1:
                if str(clean_sensor_reading[0]).isdigit():
                    total += int(clean_sensor_reading[0])

        # Average the readings
        total = total/ACCURACY
        return total

