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
        data = xbee.wait_read_frame()
        print(data)
    except KeyboardInterrupt:
        break
ser.close()
