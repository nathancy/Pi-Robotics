# Isolated test module for controlling motors on raspberry pi using GPIO

import motorControl 
from time import sleep

# Instantiate object
motor = motorControl.MotorControl()

try:
    while True:
        command = input("Enter command: ")
        if command == 'r':
            for num in range(10):
                motor.right()
                sleep(.25)
        elif command == 'l':
            for num in range(10):
                motor.left()
                sleep(.25)
        elif command == 'f':
            for num in range(10):
                motor.forward()
                sleep(.25)
        elif command == 'b':
            for num in range(10):
                motor.backward()
                sleep(.25)
        else: 
            motor.allstop()


except KeyboardInterrupt:
    motor.cleanup()
    exit(1)
