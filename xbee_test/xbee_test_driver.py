# Isolated test module for testing XBee on raspberry pi

import xbeeControl 
from time import sleep

# Instantiate object
xbee = xbeeControl.XbeeControl()

mode = input('''
        Receive - R
        Send    - S
        ''')
try:
    # Send packets
    if mode.lower() == 's':
        while True:
            xbee.send("hello from the router", 'R')
            sleep(1)
    # Receive Packets
    elif mode.lower() == 'r':
        while True:
            data = xbee.receive()
            print(data)
            sleep(1)
except KeyboardInterrupt:
    xbee.cleanup()
