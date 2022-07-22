# Written by Shreyans Daga
from robot_controls import Robot as R
import time

Robot = R()

def ball_tracking():
    # Get information about the image
    image_detection = Robot.image_data()
    # If close enough to the object then start pickup protocol
    if len(image_detection) == 2:
        Robot.pickup_protocol(image_detection)
        Robot.terminate()
    elif image_detection[1] == "yes":
        # If image is found then rotate appropriately to try and bring it into the center of the camera
        if image_detection[0] < 0.4:
            Robot.left_turn()
        elif 0.35 < image_detection[0] < 0.65:
            Robot.forward()
        elif image_detection[0] > 0.6:
            Robot.right_turn()
    else:
        # If robot is not it frame then turn right until it comes back into frame
        Robot.right_turn()
    Robot.movement_time()


if __name__ == "__main__":
    # Configure basic settings and turn on lights and OLED
    time.sleep(1)
    Robot.config_camera()
    Robot.servo_reset()
    Robot.led_on()
    Robot.motor_setup()
    while True:
        Robot.oled()
        try:
            ball_tracking()
        except KeyboardInterrupt:
            Robot.terminate()
