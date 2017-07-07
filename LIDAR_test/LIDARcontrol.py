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

        # Read serial port and extract only digits
        sensor_reading = str(ser.readline())
        clean_sensor_reading = re.findall(r'\d+', sensor_reading)
          
        # Ensure reading is valid 
        if len(clean_sensor_reading) is 1:
            if str(clean_sensor_reading[0]).isnumeric():
                return int(clean_sensor_reading[0])

