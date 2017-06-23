# Controlling a robot with two motors that can avoid obstacles by using a sonar mounted on pan/tilt servos

import motorcontrol, servocontrol, sonarcontrol, auxiliary
import time

#instantiate objects
motor = motorcontrol.MotorControl()
servo = servocontrol.ServoControl()
sonar = sonarcontrol.SonarControl()
aux = auxiliary.AuxiliaryHelp()

#center servos
servo.pancenter()
servo.tiltcenter()

#start logging data
aux.writetofile('Servos are dead center', 0)

#-------------------------------------------------------------------------------
# Setting direction (finding the longest way without obstacles

def findWay(self):
    distanceArray = []

    #pan left
    servo.panleft()
    time.sleep(1)
    distanceArray.append(sonar.distance())
    aux.writetofile('Pan Left Distace', distanceArray[0])
	
    #pan center
    servo.pancenter()
    time.sleep(1)
    distanceArray.append(sonar.distance())
    aux.writetofile('Pan Center Distace', distanceArray[1])
	
    #pan right
    servo.panright()
    time.sleep(1)
    distanceArray.append(sonar.distance())
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
def move(self):
    while sonar.distance()>=10:
        motor.forward()
        print("moving forward")
    print("stopping")
    motor.allStop()
    time.sleep(0.5)
    while sonar.distance()<10:
        print("moving backward")
        motor.backward()	
    motor.allStop()
    print("resetting position")
#-------------------------------------------------------------------------------

try:
    while True: 
        findWay()
        move()
          
except KeyboardInterrupt:
    aux.cleanup()
