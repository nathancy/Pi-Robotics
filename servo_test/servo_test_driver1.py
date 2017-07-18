# Isolated test module for servo control using Adafruit servo control board  

import servoControl 
from time import sleep

# Instantiate object
servo = servoControl.ServoControl()

try:

    # Center servos
    servo.pancenter()
    servo.tiltcenter()
    
    while True:
        print('''
        Look left       l
        Look right      r 
        Look center     c
        Tilt up         tu
        Tilt down       td
        Tilt center     tc
        Quit            q
            ''')
        command = str(input("Enter command: ")).lower()

        if command == 'l':
            for num in range(10):
                print("Left")
                servo.panleft()
                sleep(.25)
        elif command == 'r':
            for num in range(10):
                print("Right")
                servo.panright()
                sleep(.25)
        elif command == 'c':
            for num in range(10):
                print("Center")
                servo.pancenter()
                sleep(.25)
        elif command == 'tu':
            for num in range(10):
                print("Tilt up")
                servo.tiltup()
                sleep(.25)
        elif command == 'td':
            for num in range(10):
                print("Tilt down")
                servo.tiltdown()
                sleep(.25)
        elif command == 'tc':
            for num in range(10):
                print("Tilt center")
                servo.tiltcenter()
                sleep(.25)
        elif command == 'q':
            print("Quit")
            exit(1)

except KeyboardInterrupt:
    exit(1)
