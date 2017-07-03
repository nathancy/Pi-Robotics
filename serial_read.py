import serial

ser = serial.Serial('/dev/ttyACM0', 9600)

while True:
    var = ser.readline()
    
    print(var)
    print("port was", ser.name)
    print("baudrate was", ser.baudrate)


