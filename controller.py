import testing
import time
from utils import rightturn, leftturn, forward, stop
import RPi.GPIO as GPIO
    
testing.config_camera()


def ball_tracking():
    # Get information about the image
    image_detection = testing.detect_ball()
    if image_detection[1] == "yes":
        # If image is found then rotate appropriately to try and bring it into the center of the camera
        if image_detection[0] < 0.4:
            rightturn()
        elif 0.35 < image_detection[0] < 0.65:
            forward()
        elif image_detection[0] > 0.6:
            leftturn()
        if image_detection[2] > 40000 or 0.49 < image_detection[3] < 0.51 and image_detection[2] > 30000 and 0.49 < image_detection[0] < 0.51:
            stop()
            GPIO.cleanup()
            exit()
    else:
        rightturn()
    time.sleep(0.06)
    stop()
    time.sleep(0.1)


if __name__ == "__main__":
    ball_tracking()
