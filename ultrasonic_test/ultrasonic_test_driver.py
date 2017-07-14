import ultrasonicControl

ultrasonic = ultrasonicControl.UltrasonicControl()

try:
    while True:
        print(ultrasonic.distance())
except KeyboardInterrupt:
    exit(1)
