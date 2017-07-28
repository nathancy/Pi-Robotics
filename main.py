# Controlling a robot with two motors that can avoid obstacles by using a ultrasonic mounted on pan/tilt servos

import motorControl, servoControl, ultrasonicControl, auxiliary, LIDARcontrol
import time

#-------------------------------------------------------------------------------
# Setting direction (finding the longest way without obstacles)

_MOTOR_DELAY = 0.05
_SERVO_DELAY = 0.2
_TURN_DELAY = 0.15


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
    data_points = []
    initial = ultrasonic.distance(1)
    count = 0
    
    ultrasonic_distance = ultrasonic.distance(1)
    while ultrasonic_distance >= 30.0 and ultrasonic_distance <= 3000.0:
        motor.forward()
        time.sleep(_MOTOR_DELAY)
       
        if count < 5:
            data_points.append(ultrasonic.distance(1))
            count += 1
        else:
            avg_data = (data_points[0]+data_points[1] + data_points[2] + data_points[3] + data_points[4])/5
            print("data points are", data_points)
            if (initial > (avg_data - 5.00)) and (initial < (avg_data + 5.00)):
                break;

        print(ultrasonic.distance(1))
        #print("moving forward")
        ultrasonic_distance = ultrasonic.distance(1)
    print("stopping")
    motor.stop()
    time.sleep(_MOTOR_DELAY)

    # Add when have ultrasonic back sensor
    ultrasonic_distance = ultrasonic.distance(1)
    while ultrasonic_distance < 30.0 or ultrasonic_distance >= 3000.0:
        print("moving backward")
        motor.backward()	
        time.sleep(_MOTOR_DELAY)
        ultrasonic_distance = ultrasonic.distance(1)
    motor.stop()
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
