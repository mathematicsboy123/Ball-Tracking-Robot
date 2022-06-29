import serial
ser = serial.Serial('/dev/hci0', timeout=1, baudrate=115000)
serial.flushInput();serial.flushOutput()
   
while True:
    out = serial.readline().decode()
    if out!='' : print (out)
