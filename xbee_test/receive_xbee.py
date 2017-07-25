# This example continuously reads the serial port and processes IO data
# received from a remote XBee.

from xbee import ZigBee
from serial import Serial
from time import sleep

PORT = '/dev/ttyUSB0'
BAUD_RATE = 9600

# Open serial port
ser = Serial(PORT, BAUD_RATE, timeout=1)

# Create API object
xbee = ZigBee(ser, escaped=True)

# Continuously read and print packets
while True:
    try:
        frame = xbee.wait_read_frame()
        clean_data = frame['rf_data'].decode("utf-8")
        print(clean_data)
        '''
        print(frame['id'])
        print(frame['source_addr'])
        print(frame['source_addr_long'])
        '''   
    except KeyboardInterrupt:
        break
ser.close()
