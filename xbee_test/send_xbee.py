# This example continuously sends packets to a remote XBee. 

from xbee import ZigBee
from serial import Serial
from time import sleep

PORT = '/dev/ttyUSB0'
BAUD = 9600

# Open serial port
ser = Serial(PORT, BAUD, timeout=1)

# Create API object 
xbee = ZigBee(ser, escaped=True)

# Continuously send and print status packets
while True:
    try:
        # R --> C
        #xbee.send('tx', dest_addr_long = '\x00\x00\x00\x00\x00\x00\x00\x00', data='from router')

        # C --> R
        xbee.send('tx', data='from coord')

        # Print status 
        data = xbee.wait_read_frame()

        print(data)
        sleep(1)
    except KeyboardInterrupt:
        break
ser.close()
