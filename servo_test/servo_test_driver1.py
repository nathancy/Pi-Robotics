# Isolated test module for servo control using Adafruit servo control board  

import servoControl 
from time import sleep

# Instantiate object
servo = servoControl.ServoControl()

# Minimum and maximum allowable servo range
_MIN = 100
_MAX = 700

# Verify degrees are valid and within bounds
def degreeVerify():
    flag = 'Invalid'
    while flag == 'Invalid': 
        degree = input("Degree: ")
        if degree.isnumeric():
            degree = int(degree)
            if degree > _MIN and degree < _MAX:
                return degree
            else:
                print("Invalid. Degree out of range") 
        else:
            print("Invalid. Not numeric input") 

try:

    # Initially center servos
    servo.panCenter()
    servo.tiltCenter()
    
    # Ensure valid mode selection
    mode = input('''
    default servo mode - 1
    exact servo mode   - 2 
    
    ''')
    if mode.isnumeric():
        mode = int(mode)
    while mode != 1 and mode != 2:
        mode = input('''
        default servo mode - 1
        exact servo mode   - 2 
        
        ''')
        if mode.isnumeric():
            mode = int(mode)
    
    # Default servo mode
    if mode == 1:
        print('-' * 60)
        print("Default servo mode")
        print('-' * 60)
        while True:
            print('''
            Look left       l
            Look right      r 
            Look center     c
            Tilt up         tu
            Tilt down       td
            Tilt center     tc
            Mode            m
            Reset           re
            Quit            q
                ''')
            command = str(input("Enter command: ")).lower()

            if command == 'l':
                print("Left")
                servo.panLeft()
            elif command == 'r':
                print("Right")
                servo.panRight()
            elif command == 'c':
                print("Center")
                servo.panCenter()
            elif command == 'tu':
                print("Tilt up")
                servo.tiltUp()
            elif command == 'td':
                print("Tilt down")
                servo.tiltDown()
            elif command == 'tc':
                print("Tilt center")
                servo.tiltCenter()
            elif command == 're':
                print("Reset")
                servo.tiltCenter()
                servo.panCenter()
            elif command =='m':
                print('-' * 60)
                print("Default servo mode")
                print('-' * 60)
            elif command == 'q':
                print("Quit")
                exit(1)
    # Exact servo mode
    else:
        print('-' * 60)
        print("Exact servo mode")
        print('-' * 60)
        while True:
            print('''
            Look left       l
            Look right      r 
            Look center     c
            Tilt up         tu
            Tilt down       td
            Tilt center     tc
            Mode            m
            Reset           re
            Quit            q
                ''')
            command = str(input("Enter command: ")).lower()

            if command == 'l':
                print("Left")
                servo.panExactLeft(degreeVerify())
            elif command == 'r':
                print("Right")
                servo.panExactRight(degreeVerify())
            elif command == 'c':
                print("Center")
                servo.panExactCenter(degreeVerify())
            elif command == 'tu':
                print("Tilt up")
                servo.tiltExactUp(degreeVerify())
            elif command == 'td':
                print("Tilt down")
                servo.tiltExactDown(degreeVerify())
            elif command == 'tc':
                print("Tilt center")
                servo.tiltExactCenter(degreeVerify())
            elif command == 're':
                print("Reset")
                servo.panCenter()
                servo.tiltCenter()
            elif command =='m':
                print('-' * 60)
                print("Exact servo mode")
                print('-' * 60)
            elif command == 'q':
                print("Quit")
                exit(1)

except KeyboardInterrupt:
    exit(1)

