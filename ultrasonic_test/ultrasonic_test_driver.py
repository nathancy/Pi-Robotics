# Isolated test module for reading ultrasonic sensor on raspberry pi using GPIO

import ultrasonicControl
from time import sleep

# Instantiate object
ultrasonic = ultrasonicControl.UltrasonicControl()

try:
    while True:
        raw_distance = ultrasonic.distance(0)
        print("Measured Raw Distance = %f cm" % raw_distance)
        rounded_distance = ultrasonic.distance(1)
        print("Measured Rounded Distance = %.1f cm" % rounded_distance)
        sleep(1)
except KeyboardInterrupt:
    ultrasonic.cleanup()
    exit(1)