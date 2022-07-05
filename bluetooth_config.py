import serial
from utils import rightturn, leftturn, forward, stop, reverse, get_distance_forward, get_distance_reverse
from controller import ball_tracking
import RPi.GPIO as GPIO

# Configure connectivity with bluetooth module
ser = serial.Serial("/dev/rfcomm0", timeout=1, baudrate=9600)
ser.flushInput();ser.flushOutput()

while True:
    # Get command from Bluetooth module
    cmd = str(ser.read())[2].lower()

    # Move the robot in a particular direction depending on the command
    if cmd == "f":
        forward()
        dist = get_distance_forward()
        if dist < 20:
            stop()
            GPIO.cleanup()
            exit()
    elif cmd == "b":
        reverse()
        dist = get_distance_reverse()
        if dist < 20:
            stop()
            GPIO.cleanup()
            exit()
    elif cmd == "r":
        rightturn()
    elif cmd == "l":
        leftturn()
    elif cmd == "'":
        ball_tracking()
    elif cmd == "p":
        stop()
