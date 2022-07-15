from robot_controls import Robot as R

Robot = R()

def ball_tracking():
    # Get information about the image
    image_detection = Robot.image_data()
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
        Robot.right_turn()
    Robot.movement_time()


if __name__ == "__main__":
    Robot.config_camera()
    Robot.servo_reset()
    Robot.led_on()
    Robot.motor_setup()
    while True:
        try:
            ball_tracking()
        except KeyboardInterrupt:
            Robot.terminate()
