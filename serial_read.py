import serial
from pprint import pprint
ser = serial.Serial('/dev/ttyACM0', 115200)

while True:
    var = ser.readline()
    #print(type(var))
    print(var) 
    #print("baudrate was", ser.baudrate)


