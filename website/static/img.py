# Written by Shreyans Daga
import numpy as np
import cv2
from picamera2 import Picamera2
import time

picam2 = Picamera2()
picam2.CAPTURE_TIMEOUT = 60 # seconds

cwidth = 640
cheight = 480

# Configure camera image types
def config_camera():
    config = picam2.still_configuration(main={"size": (cwidth, cheight)})
    picam2.configure(config)
    picam2.start()


def detect_ball():
    # Get image and convert to BGR to HSV
    buffer = picam2.capture_array()
    color = cv2.cvtColor(buffer, cv2.COLOR_RGB2BGR)
    hsv = cv2.cvtColor(color, cv2.COLOR_BGR2HSV)

    # Threshold of orange in HSV space
    lower_blue = np.array([1, 160, 170]) # Darker bound of color, Deafaut Values
    upper_blue = np.array([20, 255, 255]) # Lighter bound of color, Deafaut Values

    with open("hsv_values.txt", "r") as file:
        text = file.readline().strip().split(", ")
        lower_blue = np.array([int(text[0]), int(text[1]), int(text[2])]) # Darker bound of color
        upper_blue = np.array([int(text[3]), int(text[4]), int(text[5])]) # Lighter bound of color

    # Generate mask using the color bounds
    mask = cv2.inRange(hsv, lower_blue, upper_blue)
    cv2.imwrite('binary.jpg', mask)

if __name__ == "__main__":
    config_camera()
    while True:
        detect_ball()
        time.sleep(0.2)
