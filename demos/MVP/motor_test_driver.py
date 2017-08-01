# Isolated test module for controlling motors on raspberry pi using GPIO

import motorControl 
from time import sleep

# Instantiate object
motor = motorControl.MotorControl()

duration = 1
delay = 1.5
try:
    while True:
        
        print('''
        Move forward    w
        Move backward   s
        Move left       a
        Move right      d
        Quit            q
            ''')
        command = str(input("Enter command: ")).lower()

        if command == 'd':
            for num in range(duration):
                print("Right")
                motor.right()
                sleep(delay)
            motor.stop()
        elif command == 'a':
            for num in range(duration):
                print("Left")
                motor.left()
                sleep(delay)
            motor.stop()
        elif command == 'w':
            for num in range(duration):
                print("Forward")
                motor.forward()
                sleep(delay)
            motor.stop()
        elif command == 's':
            for num in range(duration):
                print("Backward")
                motor.backward()
                sleep(delay)
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
