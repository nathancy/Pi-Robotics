import ultrasonicControl
from time import sleep

ultrasonic = ultrasonicControl.UltrasonicControl()

try:
    while True:
        distance = ultrasonic.distance()
        print("Measured Distance = %.1f cm" % distance)
        sleep(1)

except KeyboardInterrupt:
    exit(1)
