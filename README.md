# Pi-Blockchain

Python code used to run an autonomous robot built using Arduino, Raspberry Pi, servos, motors, ultrasonic sensors, LIDAR sensors, XBee, and blockchain technology. The robot initially turns the LIDAR to the left, right, and center to determine the longest direction through multiple readings, removes outliers, and returns a median value. It then moves the motors towards the direction of the farthest distance. The robot takes readings while in motion for collision checking using the ultrasonic sensors. If it encounters an obstacle, it stops and calibrates again to determine the next longest direction and then moves towards that direction.

This repository contains several modules:
* LIDAR_test - LIDAR sensor test module
* motor_test - Motor test module
* servo_test - Servo test module
* ultrasonic_test - Ultrasonic sensor test module
* xbee_test - XBee test module
* demos/ - Test demos for autonomous cars

Run with program with:
```
python main.py
```
- `main.py` - Main driver.
- `LIDARcontrol.py` - Module to read LIDAR sensor data on Raspberry Pi from Arduino through serial port.
- `motorControl.py` - Module for motor control.
- `servoControl.py` - Module for servo control.
- `ultrasonicControl.py` - Module for reading ultrasonic sensor data on Raspberry Pi.
- `xbeeControl.py` - Module for wireless communication on Raspberry Pi.
- `auxiliary.py` - Auxiliary functions such as releasing GPIO pins data logging.
