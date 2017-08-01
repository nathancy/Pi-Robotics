# Script for MVP demo (Car #1 with Coordinator XBee)
'''
Car #2 -> Car #1

Two cars following each other

Scenario #1: Car #1 is trustworthy
             Car #1 sends stop signal to car #2
             Car #1 moves forward, car #2 stops 

Scenario #2: Car #1 is not trustworthy
             Car #1 sends stop signal to car #2
             Car #2 continues on since car #1 is not trusted
             Both keep going forward
'''

import motorControl, servoControl, xbeeControl 
from time import sleep
import sys

delay = 1.5

# Instantiate object
motor = motorControl.MotorControl()
xbee = xbeeControl.XbeeControl()

if len(sys.argv) is not 2:
    print('''
    Usage: python car1_coord.py [options]
    Mode options: 1        (Scenario #1)
                  2        (Scenario #2)
    Examples:
    python car1_coord.py 1 (Demo Scenario #1)
    python car1_coord.py 2 (Demo Scenario #2)
        ''')
    sys.exit()

try:
    # Scenario #1
    if(sys.argv[1] == '1'):
        print(sys.argv[1], "Scenario #1 Coordinator Car")
        motor.backward()
        sleep(delay)

        # Send stop signal from Car #1 to Car #2
        xbee.send("1", "C")
        print("Sent 1 from Car #1 to Car #2")
        motor.backward()
        sleep(2)
        motor.stop()
        motor.cleanup()
        sys.exit(1)

    # Scenario #2
    if(sys.argv[1] == '2'):
        print(sys.argv[1], "Scenario #2 Coordinator Car")
        motor.backward()
        sleep(delay)
        
        # Send stop signal from Car #1 to Car #2
        xbee.send("2", "C")
        print("Sent 2 from Car #1 to Car #2")
        motor.backward()
        sleep(3.5)
        motor.stop()
        motor.cleanup()
        sys.exit(1)

except KeyboardInterrupt:
    motor.stop()
    motor.cleanup()
    sys.exit(1)

