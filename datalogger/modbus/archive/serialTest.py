import serial
ser = serial.Serial('/dev/ttyAMA0', 9600, timeout=1)
print (ser)

while (1):
    ser.write(':0101010101010101')
#print repr(ser.read(1000))
