# Pi-Blockchain

![](docs/robot.jpg)

Python code used to run an autonomous robot built using Arduino, Raspberry Pi, servos, motors, ultrasonic sensors, LIDAR sensors, XBee, and blockchain technology. For the autonomous demo, the robot initially turns the LIDAR to the left, right, and center to determine the longest direction through multiple readings, removes outliers, and returns a median value. It then moves the motors towards the direction of the farthest distance. The robot takes readings while in motion for collision checking using the ultrasonic sensors. If it encounters an obstacle, it stops and calibrates again to determine the next longest direction and then moves towards that direction.

For MVP test demos between the cars, look in the `demos/MVP` directory.

This repository contains several modules:
* LIDAR_test - LIDAR sensor test module
* motor_test - Motor test module
* servo_test - Servo test module
* ultrasonic_test - Ultrasonic sensor test module
* xbee_test - XBee test module
* demos/ - Test demos for autonomous cars (MVP demo)

For the autonomous demo, run with program with:
```
python main.py
```
- `main.py` - Main driver.
- `LIDARcontrol.py` - Module to read LIDAR sensor data on Raspberry Pi from Arduino through the serial port.
- `motorControl.py` - Module for motor control.
- `servoControl.py` - Module for servo control.
- `ultrasonicControl.py` - Module for reading ultrasonic sensor data on the Raspberry Pi.
- `xbeeControl.py` - Module for wireless communication on the Raspberry Pi.
- `auxiliary.py` - Auxiliary functions such as releasing GPIO pins and data logging.

# Parts
* [Raspberry Pi 3 Model B](https://www.adafruit.com/product/3055)
* [Arduino Uno R3 (Atmega328)](https://www.adafruit.com/product/50)
* [Iron Man-4 Indoor Tracked Chassis with motors](http://www.robotshop.com/en/iron-man-4-indoor-tracked-chassis.html)
* [MC33886 Raspberry Pi Motor Driver Board for Raspberry Pi](http://www.robotshop.com/en/mc33886-raspberry-pi-motor-driver-board-raspberry-pi.html)
* [Xbee S2C series (XB24CZ7WIT-004)](https://www.adafruit.com/product/968)
* [SparkFun XBee Explorer Dongle](https://www.sparkfun.com/products/11697)
* [HC-SR04 Ultrasonic Range Finder](http://www.robotshop.com/en/hc-sr04-ultrasonic-range-finder.html)
* [Lynxmotion Aluminum Multi-Purpose Sensor Bracket (for ultrasonic)]( http://www.robotshop.com/en/lynxmotion-multi-purpose-sensor-housing.html)
* [LIDAR-Lite v3](https://www.sparkfun.com/products/14032)
* [Lynxmotion Micro Pan and Tilt Kit with Servos (for LIDAR)](http://www.robotshop.com/en/lynxmotion-micro-pan-and-tilt-kit-with-servos-black.html?gclid=COqk_-jH0tQCFROBswod3hUNpg#reviewBox)
* [Adafruit 16-Channel 12-bit PWM/Servo Driver - I2C interface - PCA9685](https://www.adafruit.com/product/815)
* [Venom Fly 30C 4S 5000mAh 14.8V LiPo Battery](https://www.amazon.com/Venom-5000mAh-14-8V-Battery-Deans/dp/B016ZM1S66/ref=sr_1_1?s=toys-and-)
* [SMAKN Dc/dc Converter 12v Step Down to 5v/3a Power Supply Module](https://www.amazon.com/dp/B00CXKBJI2/ref=cm_sw_r_cp_ep_dp_bpzxzb294NQJ7)
* [USB Battery Pack for Raspberry Pi (10000mAh)](https://www.adafruit.com/product/1566)
* [USB to USBMicro (for battery pack to Pi3)](https://www.amazon.com/Eversame-USB2-0-4-Pack-Charge-Samsung/dp/B01K7DSRRC/ref=sr_1_4?ie=UTF8&qid=1498184169&sr=8-4&keywords=8%22+usb+to+micro+usb)

# Sensor Libraries/Datasheets
* LIDAR-Lite v3 
    * [LIDAR-Lite v3 Arduino Library (I2C)](https://github.com/garmin/LIDARLite_v3_Arduino_Library)
	* [Datasheet](http://static.garmin.com/pumac/LIDAR_Lite_v3_Operation_Manual_and_Technical_Specifications.pdf)
* HC-SR04 Ultrasonic Sensor
	* [RPi.GPIO](https://pypi.python.org/pypi/RPi.GPIO)
	* [Datasheet](https://cdn.sparkfun.com/datasheets/Sensors/Proximity/HCSR04.pdf)
* Servo 
    * [PWM/RPi.GPIO](https://sourceforge.net/p/raspberry-gpio-python/wiki/PWM/)
    * [PCA9685 Driver Board Datasheet](https://cdn-shop.adafruit.com/datasheets/PCA9685.pdf)
* Motor
    * [RPi.GPIO](https://pypi.python.org/pypi/RPi.GPIO)
    * [MC33886 Motor Driver Board Datasheet](http://www.robotshop.com/media/files/pdf2/rpi_motor_driver_board_-_waveshare_wiki.pdf)
* XBee
    * [python-xbee](https://github.com/nioinnovation/python-xbee)
    * [Datasheet](https://cdn-shop.adafruit.com/datasheets/ds_xbeezbmodules.pdf)

# Software Block Diagram
![](docs/block-diagram.jpg)

# Robot Wiring Diagram
![](docs/new-wiring-diagram.PNG)
