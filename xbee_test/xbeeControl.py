#!/usr/bin/env python
# XBee Control for Raspberry Pi with Series S2C (XB24CZ7WIT-004)
# https://www.adafruit.com/product/968

#-------------------------------------------------------------------------------

#### Imports ####

from xbee import ZigBee
from serial import Serial

#### Constants ####

#-------------------------------------------------------------------------------

PORT = '/dev/ttyUSB0'
BAUD_RATE = 9600

# Open serial port
ser = Serial(PORT, BAUD_RATE, timeout = 1)

# Create API object 
xbee = ZigBee(ser, escaped=True)

#### Objects ####

#-------------------------------------------------------------------------------
class XbeeControl(object):
    # Make sure there is only one instance of XbeeControl

    _instances=[]

    # Initialize the object
    def __init__(self):
        if ( len(self._instances)>1 ):
            print("ERROR: One instance of XbeeControl is running already.")
            exit(1)
        self._instances.append(self)									
#-------------------------------------------------------------------------------        
    # Close serial port
    def cleanup(self):
        ser.close()
    
#-------------------------------------------------------------------------------        
    # Send packets
    def send(self, packet_data, mode):
        '''
        Parameter             Description               Default
        --------------------------------------------------------------
        id                    Frame Type                0x10
        frame_id              Frame ID                  0x01
        dest_addr             16 bit destination addr   FF FE
        dest_addr_long        64 bit destination addr   None 
        data                  RF data in packet         None
        '''
        # Router --> Coordinator (A Router node is running this program)
        if mode == 'R':
            xbee.send('tx', dest_addr_long = '\x00\x00\x00\x00\x00\x00\x00\x00', data = packet_data)
        # Coordinator --> Router (Coordinator is running this program)
        elif mode == 'C':
            xbee.send('tx', dest_addr_long = '\x00\x13\xA2\x00\x41\x55\xB9\xC7', data = packet_data)
        else:
            print("ERROR: Invalid XBee configuration mode. Set 'C' for Coordinator or 'R' for Router XBee.")
            exit(1)
    
    # Receive packets
    def receive(self):
        '''
        Parameter             Description               
        --------------------------------------------------------------
        id                    Frame Type                
        source_addr           16 bit source addr   
        source_addr_long      64 bit source addr   
        rf_data               RF data in packet         
        '''
        frame = xbee.wait_read_frame()
        clean_data = frame['rf_data'].decode("utf-8")
        return clean_data
        
