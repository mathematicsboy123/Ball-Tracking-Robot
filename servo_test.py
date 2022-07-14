from time import *
from adafruit_servokit import ServoKit
kit = ServoKit(channels=16)


def turn_front_servo(direction):
    if direction == "r":
        kit.servo[0].angle = 0
    elif direction == "l":
        kit.servo[0].angle = 180
    elif direction == "s":
        kit.servo[0].angle = 90

if __name__ == "__main__":
    while True:
        turn_front_servo("r")
        sleep(2)
        turn_front_servo("s")
        sleep(2)
        turn_front_servo("l")
        sleep(2)
