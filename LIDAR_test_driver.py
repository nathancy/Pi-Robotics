# Isolated test module for reading LIDAR sensor on Raspberry Pi from Arduino through serial

import LIDARcontrol 

# Instantiate object  
lidar = LIDARcontrol.LIDARControl()

try: 
    while True:
        print(lidar.distance())
except KeyboardInterrupt:
    exit(1) 

