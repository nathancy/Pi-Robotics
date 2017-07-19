# Controlling a robot with two motors that can avoid obstacles by using a ultrasonic mounted on pan/tilt servos

import motorControl, servoControl, ultrasonicControl, auxiliary
import time

#-------------------------------------------------------------------------------
# Setting direction (finding the longest way without obstacles

def findWay():
    distanceArray = []

    # Pan left
    servo.panLeft()
    time.sleep(1)
    distanceArray.append(ultrasonic.distance(1))
    aux.writetofile('Pan Left Distace', distanceArray[0])
	
    # Pan center
    servo.panCenter()
    time.sleep(1)
    distanceArray.append(ultrasonic.distance(1))
    aux.writetofile('Pan Center Distace', distanceArray[1])
	
    # Pan right
    servo.panRight()
    time.sleep(1)
    distanceArray.append(ultrasonic.distance(1))
    aux.writetofile('Pan Right Distace', distanceArray[2])

    maxdistance=max(distanceArray)
    maxindex=distanceArray.index(maxdistance)

    if maxindex == 0:
        motor.left()
        aux.writetofile('Turning Left', distanceArray[maxindex])
    elif maxindex ==2:
        motor.right()
        aux.writetofile('Turning Right', distanceArray[maxindex])
    else:
        aux.writetofile('Not Turning', distanceArray[maxindex])
      
    del distanceArray[:]
  	
#------------------------------------------------------------------------------- 
def move():
    while ultrasonic.distance(1)>=10:
        motor.forward()
        print(ultrasonic.distance(1))
        print("moving forward")
    print("stopping")
    motor.stop()
    time.sleep(0.5)
    while ultrasonic.distance(1)<10:
        print("moving backward")
        motor.backward()	
    motor.stop()
    print("resetting position")
#-------------------------------------------------------------------------------

# Instantiate objects
motor = motorControl.MotorControl()
servo = servoControl.ServoControl()
ultrasonic = ultrasonicControl.UltrasonicControl()
aux = auxiliary.AuxiliaryHelp()

# Center servos
servo.resetServo()

# Start logging data
aux.writetofile('Servos are dead center', 0)

try:
    while True: 
        findWay()
        move()
          
except KeyboardInterrupt:
    aux.cleanup()
