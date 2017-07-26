# Controlling a robot with two motors that can avoid obstacles by using a ultrasonic mounted on pan/tilt servos

import motorControl, servoControl, ultrasonicControl, auxiliary, LIDARcontrol
import time

#-------------------------------------------------------------------------------
# Setting direction (finding the longest way without obstacles)

_MOTOR_DELAY = 0.15
_SERVO_DELAY = 0.2

def findDirection():
    distanceArray = [0,0,0]

    # Previous was right, move left 
    if PAST_DIRECTION == RIGHT:

        # Pan left
        servo.panLeft()
        time.sleep(_SERVO_DELAY)
#        distance = ultrasonic.distance(1)
        distance = lidar.distance()
        distanceArray[0] = distance
        print("left distance: ", distance)
#        aux.writetofile('Pan Left Distace', distanceArray[0])

        # Pan center
        servo.panCenter()
        time.sleep(_SERVO_DELAY)
#        distance = ultrasonic.distance(1)
        distance = lidar.distance()
        distanceArray[1] = distance
        print("center distance: ", distance)
#        aux.writetofile('Pan Center Distace', distanceArray[1])
            
        # Pan right
        servo.panRight()
        time.sleep(_SERVO_DELAY)
#        distance = ultrasonic.distance(1)
        distance = lidar.distance()
        distanceArray[2] = distance
        print("right distance: ", distance)
#        aux.writetofile('Pan Right Distace', distanceArray[2])

        global PAST_DIRECTION
        PAST_DIRECTION = LEFT
        servo.panCenter()
#        print("Past is", PAST_DIRECTION)

    # Previous was left, move right 
    else:

        # Pan right
        servo.panRight()
        time.sleep(_SERVO_DELAY)
#        distance = ultrasonic.distance(1)
        distance = lidar.distance()
        distanceArray[2] = distance
        print("right distance: ", distance)
#        aux.writetofile('Pan Right Distace', distanceArray[2])

        # Pan center
        servo.panCenter()
        time.sleep(_SERVO_DELAY)
#        distance = ultrasonic.distance(1)
        distance = lidar.distance()
        distanceArray[1] = distance
        print("center distance: ", distance)
#        aux.writetofile('Pan Center Distace', distanceArray[1])
            
        # Pan left
        servo.panLeft()
        time.sleep(_SERVO_DELAY)
#        distance = ultrasonic.distance(1)
        distance = lidar.distance()
        distanceArray[0] = distance
        print("left distance: ", distance)
#        aux.writetofile('Pan Left Distace', distanceArray[0])

        global PAST_DIRECTION
        PAST_DIRECTION = RIGHT
        servo.panCenter()
#        print("Past is", PAST_DIRECTION)

    maxdistance = max(distanceArray)
    maxindex = distanceArray.index(maxdistance)
#    print("maxindex is: ", maxindex)

    '''
    maxindex   0   left
    maxindex   1   center 
    maxindex   2   right
    '''
    if maxindex == 0:
        #motor.left()
        time.sleep(_MOTOR_DELAY)
        aux.writetofile('Turning Left', distanceArray[maxindex])
    elif maxindex == 2:
        #motor.right()
        time.sleep(0.27)
        aux.writetofile('Turning Right', distanceArray[maxindex])
    else:
        aux.writetofile('Not Turning', distanceArray[maxindex])

    print(distanceArray)

    del distanceArray[:]
  	
#------------------------------------------------------------------------------- 
def move():
    while ultrasonic.distance(1) >= 30.0:
        motor.forward()
        time.sleep(_MOTOR_DELAY)
        print(ultrasonic.distance(1))
        print("moving forward")
    print("stopping")
    motor.stop()
    time.sleep(_MOTOR_DELAY)

    # Add when have ultrasonic back sensor
    '''
    while ultrasonic.distance(1) < 30.0:
        print("moving backward")
        motor.backward()	
        time.sleep(_MOTOR_DELAY)
    motor.stop()
    '''
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
PAST_DIRECTION = 0

# Center servos
servo.resetServo()

# Start logging data
aux.writetofile('Servos are dead center', 0)

try:
    while True: 
        findDirection()
        time.sleep(1)
        #move()
          
except KeyboardInterrupt:
    servo.resetServo()
    aux.cleanup()
