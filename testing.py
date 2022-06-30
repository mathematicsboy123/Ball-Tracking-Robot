import numpy as np
import cv2
from picamera2 import Picamera2

picam2 = Picamera2()

# Configure camera image types
def config_camera():
    config = picam2.still_configuration(main={"size": (320, 240)})
    picam2.configure(config)
    picam2.start()

def detect_ball():
    # Get image and convert to BGR to HSV
    buffer = picam2.capture_array()
    color = cv2.cvtColor(buffer, cv2.COLOR_RGB2BGR)
    hsv = cv2.cvtColor(color, cv2.COLOR_BGR2HSV)
    
    # Threshold of red in HSV space
    lower_blue = np.array([140, 160, 10]) # Darker bound of color
    upper_blue = np.array([200, 255, 255]) # Lighter bound of color

    # Generate mask useing the color bounds
    mask = cv2.inRange(hsv, lower_blue, upper_blue)
    cv2.imwrite('binary.jpg', mask)

    # Find the white pixels and then calculate the center point
    white_pix = np.sum(mask == 255)
    cX = 0
    cY = 0
    red_found = "no"
    if white_pix > 1000:
    # Find the center of the circle using the binary image
        M = cv2.moments(mask)
        try:
            cX = int(M["m10"] / M["m00"])
            cY = int(M["m01"] / M["m00"])
            cv2.circle(color, (cX, cY), 5, (255, 0, 0), -1)
        except ZeroDivisionError:
            pass

        cv2.circle(color, (cX,cY), radius=0, color=(0, 0, 255), thickness=-1)
        cv2.imwrite("center.jpg", color)
        red_found = "yes"

    return [cX/320, red_found, white_pix, cY/240]

if __name__ == "__main__":
    config_camera()
    detect_ball()
