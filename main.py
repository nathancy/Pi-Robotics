'''
Autonomous robot main driver to avoid obstacles and navigate through its surroundings.

Python code used to run an autonomous robot built using Arduino, Raspberry Pi, servos, motors, 
ultrasonic sensors, LIDAR sensors, XBee, and blockchain technology. The robot initially turns 
the LIDAR to the left, right, and center to determine the longest direction through multiple 
readings, removes outliers, and returns a median value. It then moves the motors towards the 
direction of the farthest distance. The robot takes readings while in motion for collision 
checking using the ultrasonic sensors. If it encounters an obstacle, it stops and 
calibrates again to determine the next longest direction and then moves towards that direction.
'''

import motorControl, servoControl, ultrasonicControl, auxiliary, LIDARcontrol
import time

#-------------------------------------------------------------------------------
# Setting direction (finding the longest way without obstacles)

# Duration for motors to operate
_MOTOR_DELAY = 0.05

# Duration for servo turning speed
_SERVO_DELAY = 0.25

# Duration for right and left motor turn amount
_MOTOR_TURN_DELAY = 0.15

# Ultrasonic sensitivity for collision checking. Increase for greater collision avoidance
_SENSITIVITY = 20.0

# Ultrasonic max sensor reading. Any values over this reading are invalid
_ULTRASONIC_MAX = 500.0

#-------------------------------------------------------------------------------

# Poll ultrasonic sensor and ensure readings are valid
def ultrasonic_reading():
    ultrasonic_distance = ultrasonic.distance(1)
    while ultrasonic_distance > _ULTRASONIC_MAX:
        ultrasonic_distance = ultrasonic.distance(1)
        print("ultrasonic_distance is: ", ultrasonic_distance)
    return ultrasonic_distance

# Turn LIDAR sensor to the left, right, and center to determine the longest direction through multiple
# readings. Then uses the motor to shift the robot towards the longest direction.
def findDirection():
    distanceArray = [0,0,0]
    global PAST_DIRECTION

    # Previous was right, move left 
    if PAST_DIRECTION == RIGHT:

        # Pan left
        servo.panLeft()
        time.sleep(_SERVO_DELAY)
        distanceArray[0] = lidar.distance()
        print("left distance: ", distanceArray[0])
#        aux.writetofile('Pan Left Distace', distanceArray[0])

        # Pan center
        servo.panCenter()
        time.sleep(_SERVO_DELAY)
        distanceArray[1] = lidar.distance()
        print("center distance: ", distanceArray[1])
#        aux.writetofile('Pan Center Distace', distanceArray[1])
            
        # Pan right
        servo.panRight()
        time.sleep(_SERVO_DELAY)
        distanceArray[2] = lidar.distance()
        print("right distance: ", distanceArray[2])
#        aux.writetofile('Pan Right Distace', distanceArray[2])

        PAST_DIRECTION = LEFT
        servo.panCenter()

    # Previous was left, move right 
    else:

        # Pan right
        servo.panRight()
        time.sleep(_SERVO_DELAY)
        distanceArray[2] = lidar.distance()
        print("right distance: ", distanceArray[2])
#        aux.writetofile('Pan Right Distace', distanceArray[2])

        # Pan center
        servo.panCenter()
        time.sleep(_SERVO_DELAY)
        distanceArray[1] = lidar.distance()
        print("center distance: ", distanceArray[1])
#        aux.writetofile('Pan Center Distace', distanceArray[1])
            
        # Pan left
        servo.panLeft()
        time.sleep(_SERVO_DELAY)
        distanceArray[0] = lidar.distance()
        print("left distance: ", distanceArray[0])
#        aux.writetofile('Pan Left Distace', distanceArray[0])

        PAST_DIRECTION = RIGHT
        servo.panCenter()

    maxdistance = max(distanceArray)
    maxindex = distanceArray.index(maxdistance)

    '''
    maxindex   0   left
    maxindex   1   center 
    maxindex   2   right
    '''
    if maxindex == 0:
        motor.left()
        time.sleep(_MOTOR_TURN_DELAY)
        motor.stop()
        aux.writetofile('Turning Left', distanceArray[maxindex])
    elif maxindex == 2:
        motor.right()
        time.sleep(_MOTOR_TURN_DELAY)
        motor.stop()
        aux.writetofile('Turning Right', distanceArray[maxindex])
    else:
        aux.writetofile('Not Turning', distanceArray[maxindex])

    print(distanceArray)

    del distanceArray[:]
  	
#------------------------------------------------------------------------------- 

# Move the robot forward or backward by using the ultrasonic sensor to determine collision checking.
def move():
    # Move robot forward
    ultrasonic_distance = ultrasonic_reading()
    while ultrasonic_distance >= _SENSITIVITY and ultrasonic_distance <= _ULTRASONIC_MAX:
        motor.forward()
        time.sleep(_MOTOR_DELAY)
        print("moving forward")
        ultrasonic_distance = ultrasonic_reading()
        print("ultrasonic_distance forward is: ", ultrasonic_distance)
    motor.stop()
    time.sleep(_MOTOR_DELAY)

    # Move robot backwards 
    ultrasonic_distance = ultrasonic_reading()
    while ultrasonic_distance < _SENSITIVITY:
        motor.backward()	
        time.sleep(_MOTOR_DELAY)
        print("moving backward")
        ultrasonic_distance = ultrasonic_reading()
        print("ultrasonic_distance backward is: ", ultrasonic_distance)
    motor.stop()
    time.sleep(_MOTOR_DELAY)
    print("resetting position")
#-------------------------------------------------------------------------------

# Instantiate objects
motor = motorControl.MotorControl()
servo = servoControl.ServoControl()
ultrasonic = ultrasonicControl.UltrasonicControl()
lidar = LIDARcontrol.LIDARControl()
aux = auxiliary.AuxiliaryHelp()

LEFT = 0
CENTER = 1
RIGHT = 2

# Initially search left 
global PAST_DIRECTION 
PAST_DIRECTION = 0

# Center servos
servo.resetServo()

# Start logging data
aux.writetofile('Servos are dead center', 0)

try:
    while True: 
        findDirection()
        move()
          
except KeyboardInterrupt:
    servo.resetServo()
    aux.cleanup()
