from time import *
from adafruit_servokit import ServoKit
kit = ServoKit(channels=16)

# 2-Horizontal = 90
# 3-min0, max65
# offset for servo 3: 90

def servo(number, angle):
    kit.servo[number].angle = angle

def turn_front_servo(direction):
    if direction == "r":
        servo(0, 0)
    elif direction == "l":
        servo(0, 180)
    elif direction == "s":
        servo(0, 100)

def reset_servos():
    turn_front_servo("s")
    servo(1, 83)
    servo(2, 180)
    servo(3, 65)
    servo(4, 180)


def apply_offset_clipper(center):
    print(center)
    offset = center - 0.5
    offset /= 0.01
    angle = 83 + (-1*(offset))
    return angle


if __name__ == "__main__":
    while True:
        reset_servos()
