# Sometimes you want to dance

import servoControl 
from time import sleep

# Instantiate object
servo = servoControl.ServoControl()

def loading():
    loadMsg = "Loading: ["
    for num in range(10):
        loadMsg = loadMsg + "="
        print(loadMsg + ">", end='\r')
        sleep(0.05 * num)
    loadMsg = loadMsg + "] Complete"
    print(loadMsg)

try:
    # Initially center servos
    servo.panCenter()
    servo.tiltCenter()
   
    loading()

    servo.panLeft()
    sleep(.25)    
    servo.panRight()
    sleep(.25)    
    servo.tiltDown()
    sleep(.25)
    servo.tiltUp()
    sleep(.25)
    servo.tiltDown()
    sleep(.25)
    servo.tiltUp()
    sleep(.25)
    servo.panLeft()
    sleep(.25)
    servo.tiltDown()
    sleep(.25)
    servo.tiltUp()
    sleep(.25)
    servo.tiltDown()
    sleep(.25)
    servo.tiltUp()
    sleep(.25)

    servo.panCenter()
    servo.tiltCenter()
    sleep(.25) 

    servo.tiltDown()
    servo.panLeft()
    sleep(.25)
    servo.tiltUp()
    sleep(.25)

    servo.tiltDown()
    servo.panLeft()
    sleep(.5)
    servo.panRight()
    sleep(.5)
    servo.panLeft()
    sleep(.5)
    servo.panRight()
    sleep(.5)

    servo.tiltUp()
    servo.panLeft()
    sleep(.5)
    servo.panRight()
    sleep(.5)
    servo.panLeft()
    sleep(.5)
    servo.panRight()
    sleep(.5)
    
    servo.panRight()
    servo.tiltDown()
    sleep(.5)
    servo.panLeft()
    servo.tiltUp()
    sleep(.5)

    servo.tiltDown()
    sleep(.5)
    servo.panRight()
    servo.tiltUp()
    sleep(.5)

    servo.panRight()
    servo.tiltDown()
    sleep(.5)
    servo.panLeft()
    servo.tiltUp()
    sleep(.5)

    servo.panLeft()
    servo.tiltUp()
    sleep(.5)
    servo.panRight()
    servo.tiltDown()
    sleep(.5)

    servo.panCenter()
    servo.tiltCenter()
    sleep(.25)
    servo.tiltDown()
    sleep(.25)
    servo.tiltUp()
    sleep(.25)
    servo.tiltDown()
    sleep(.25)
    servo.tiltUp()
    sleep(.25)
   
    servo.panRight()
    servo.tiltDown()
    sleep(.15)
    servo.tiltUp()
    sleep(.15)
    servo.panCenter()
    servo.tiltDown()
    sleep(.15)
    servo.tiltUp()
    sleep(.15)
    servo.panLeft()
    servo.tiltDown()
    sleep(.15)
    servo.tiltUp()
    sleep(.15)

    servo.panCenter()
    servo.tiltCenter()

    servo.panLeft()
    servo.tiltUp()
    sleep(.15)
    servo.tiltDown()
    sleep(.15)
    servo.panCenter()
    servo.tiltUp()
    sleep(.15)
    servo.tiltDown()
    sleep(.15)
    servo.panRight()
    servo.tiltUp()
    sleep(.15)
    servo.tiltDown()
    sleep(.15)

    servo.panCenter()
    servo.tiltCenter()

    servo.tiltDown()
    sleep(.75)
    servo.tiltUp()
    sleep(.75)
    servo.tiltDown()
    sleep(.75)
    servo.tiltUp()
    sleep(.75)

    servo.panCenter()
    servo.tiltCenter()

except KeyboardInterrupt:
    # Reset servo to center 
    servo.panCenter()
    servo.tiltCenter()
    print("Quit")
    exit(1)

