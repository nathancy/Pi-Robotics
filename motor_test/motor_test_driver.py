# Isolated test module for controlling motors on raspberry pi using GPIO

import motorControl 
from time import sleep

# Instantiate object
motor = motorControl.MotorControl()

try:
    while True:
        
        print('''
        Move forward - f
        Move backward - b
        Move right - r
        Move left - l
            ''')
        command = str(input("Enter command: ")).lower()

        if command == 'r':
            for num in range(10):
                print("Right")
                motor.right()
                sleep(.25)
            motor.stop()
        elif command == 'l':
            for num in range(10):
                print("Left")
                motor.left()
                sleep(.25)
            motor.stop()
        elif command == 'f':
            for num in range(10):
                print("Forward")
                motor.forward()
                sleep(.25)
            motor.stop()
        elif command == 'b':
            for num in range(10):
                print("Backward")
                motor.backward()
                sleep(.25)
            motor.stop()
        elif command == 'q':
            print("Quit")
            motor.stop()
            motor.cleanup()
            exit(1)
        else: 
            motor.stop()

except KeyboardInterrupt:
    motor.stop()
    motor.cleanup()
    exit(1)
