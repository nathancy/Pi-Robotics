import serial
from pprint import pprint
import re

ser = serial.Serial('/dev/ttyACM0', 115200)

while True:
    sensor_reading = str(ser.readline())
    clean_sensor_reading = re.findall(r'\d+', sensor_reading)[0]
    print(clean_sensor_reading)
    #print("baudrate was", ser.baudrate)


