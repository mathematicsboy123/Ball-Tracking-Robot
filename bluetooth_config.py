import serial
from utils import rightturn, leftturn, forward, stop, reverse
from controller import ball_tracking

ser = serial.Serial("/dev/rfcomm0", timeout=1, baudrate=9600)
ser.flushInput();ser.flushOutput()

while True:
    cmd = str(ser.read())[2].lower()
    if cmd == "f":
        forward()
    elif cmd == "b":
        reverse()
    elif cmd == "r":
        rightturn()
    elif cmd == "l":
        leftturn()
    elif cmd == "s":
        ball_tracking()
    elif cmd == "p":
        stop()
