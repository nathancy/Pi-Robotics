# Pi-Blockchain

Python code used to run an autonomous robot built using Arduino, Raspberry Pi, and LIDAR, and blockchain technology. The robot initially turns the LIDAR to the left, right, and center to calibrate by taking 5 readings, removes outliers and returns a median value. It then moves in the direction of the farthest distance. THe robot takes readings while in motion. If it encounters an obstacle, it stops and calibrates again to determine the next direction. 

This repository contains several modules:
* LIDAR_test - LIDAR sensor test module
* motor_test - Motor test module
* servo_test - Servo test module
* ultrasonic_test - Ultrasonic sensor test module

Run with program with:
```
python main.py
```
main.py - Main driver.
LIDARcontrol.py - Module to read LIDAR sensor data on Raspberry Pi from Arduino through serial port.
motorControl.py - Module for motor control.
servoControl.py - Module for servo control.
ultrasonicControl.py - Module for reading ultrasonic sensor data on Raspberry Pi.
auxiliary.py - Auxiliary functions such as releasing GPIO pins data logging.
