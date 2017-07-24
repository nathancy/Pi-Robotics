from xbee import ZigBee
from serial import Serial
from time import sleep
PORT = '/dev/ttyUSB0'
BAUD = 9600

ser = Serial(PORT, BAUD)
xbee = ZigBee(ser)

#destination = u'\x00\x13\xA2\x00\x41\x55\xB9\xC7'
#destination.encode('utf-8')

while True:
    try:
        # R --> C
        xbee.send('tx', dest_addr_long='\x00\x00\x00\x00\x00\x00\x00\x00', data='Hello WOrld')

        # C --> R
        #xbee.send('tx', dest_addr_long='\x00\x13\xA2\x00\x41\x55\xB9\xC7', data='from coord')
        
        data = xbee.wait_read_frame()

        print(data)
        sleep(1)
    except KeyboardInterrupt:
        break
ser.close()
