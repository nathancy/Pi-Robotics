# Script to reset all possible GPIO pins on Raspberry Pi
# Ensure pins are not hanging from prior use

import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)
GPIO.setup(3, GPIO.IN)
GPIO.setup(5, GPIO.IN)
GPIO.setup(7, GPIO.IN)
GPIO.setup(11, GPIO.IN)
GPIO.setup(13, GPIO.IN)
GPIO.setup(15, GPIO.IN)
GPIO.setup(19, GPIO.IN)
GPIO.setup(21, GPIO.IN)
GPIO.setup(23, GPIO.IN)
GPIO.setup(29, GPIO.IN)
GPIO.setup(31, GPIO.IN)
GPIO.setup(33, GPIO.IN)
GPIO.setup(35, GPIO.IN)
GPIO.setup(37, GPIO.IN)
GPIO.setup(12, GPIO.IN)
GPIO.setup(16, GPIO.IN)
GPIO.setup(18, GPIO.IN)
GPIO.setup(22, GPIO.IN)
GPIO.setup(24, GPIO.IN)
GPIO.setup(26, GPIO.IN)
GPIO.setup(32, GPIO.IN)
GPIO.setup(36, GPIO.IN)
GPIO.setup(38, GPIO.IN)
GPIO.setup(40, GPIO.IN)

GPIO.cleanup()
