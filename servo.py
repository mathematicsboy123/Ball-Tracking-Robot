from time import *
from adafruit_servokit import ServoKit

# Create a kit of all servos attached to the robot hat
kit = ServoKit(channels=16)

# 2-Horizontal = 90
# 3-min0, max65
# offset for servo 3: 90

# Set a particular servo to a specific angle
def servo(number, angle):
    kit.servo[number].angle = angle

# Turn the front servo according to the direction that the car needs to travel
def turn_front_servo(direction):
    if direction == "r":
        servo(0, 0)
    elif direction == "l":
        servo(0, 180)
    elif direction == "s":
        servo(0, 100)

# Reset all servos to their base position
def reset_servos():
    turn_front_servo("s")
    servo(1, 83)
    servo(2, 180)
    servo(3, 65)
    servo(4, 180)

# Generate angle for the location of the arm based on where the center of the ball is
def apply_offset_clipper(center):
    print(center)
    offset = center - 0.5
    offset /= 0.01
    angle = 83 + (-1*(offset))
    return angle


if __name__ == "__main__":
    while True:
        reset_servos()
