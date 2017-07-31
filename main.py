# Controlling a robot with two motors that can avoid obstacles by using a ultrasonic mounted on pan/tilt servos

import motorControl, servoControl, ultrasonicControl, auxiliary, LIDARcontrol
import time

#-------------------------------------------------------------------------------
# Setting direction (finding the longest way without obstacles)

_MOTOR_DELAY = 0.05
_SERVO_DELAY = 0.25
_TURN_DELAY = 0.15

def ultrasonic_reading():
    ultrasonic_distance = ultrasonic.distance(1)
    while ultrasonic_distance > 500.0:
        ultrasonic_distance = ultrasonic.distance(1)
        print("ultrasonic_distance is: ", ultrasonic_distance)
    return ultrasonic_distance


def findDirection():
    distanceArray = [0,0,0]

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

        global PAST_DIRECTION
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

        global PAST_DIRECTION
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
        time.sleep(_TURN_DELAY)
        motor.stop()
        aux.writetofile('Turning Left', distanceArray[maxindex])
    elif maxindex == 2:
        motor.right()
        time.sleep(_TURN_DELAY)
        motor.stop()
        aux.writetofile('Turning Right', distanceArray[maxindex])
    else:
        aux.writetofile('Not Turning', distanceArray[maxindex])

    print(distanceArray)

    del distanceArray[:]
  	
#------------------------------------------------------------------------------- 
def move():
    ultrasonic_distance = ultrasonic_reading()
    while ultrasonic_distance >= 20.0 and ultrasonic_distance <= 500.0:
        motor.forward()
        time.sleep(_MOTOR_DELAY)
        print("moving forward")
        ultrasonic_distance = ultrasonic_reading()
        print("ultrasonic_distance forward is: ", ultrasonic_distance)
    motor.stop()
    time.sleep(_MOTOR_DELAY)

    ultrasonic_distance = ultrasonic_reading()
    while ultrasonic_distance < 20.0:
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
