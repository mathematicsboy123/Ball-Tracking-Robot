import serial
from move import motorStop
from robot_controls import Robot as R

# Initialize Robot class instance
Robot = R()

# Setup all hardware to function
Robot.config_camera()
Robot.servo_reset()
Robot.led_on()
Robot.motor_setup()
Robot.oled()

# Configure connectivity with bluetooth module
ser = serial.Serial("/dev/rfcomm0", timeout=1, baudrate=9600)
ser.flushInput();ser.flushOutput()

while True:
    # Get command from Bluetooth module
    cmd = str(ser.read())[2].lower()

    # Move the robot in a particular direction depending on the command
    if cmd == "f":
        Robot.forward()
    elif cmd == "b":
        Robot.reverse()
    elif cmd == "r":
        Robot.right_turn()
    elif cmd == "l":
        Robot.left_turn()
    elif cmd == "p":
        motorStop()
