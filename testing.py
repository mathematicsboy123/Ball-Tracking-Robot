import cv2
import numpy as np
import time
import cv2
from picamera2 import Picamera2, Preview, MappedArray

# Configure camera image types
picam2 = Picamera2()
config = picam2.still_configuration(main={"size": (320, 240)})
picam2.configure(config)

# Configure camera to be able to take pictures
picam2.start()
while True:
    start_time = time.monotonic()
    # Get color and convert to gray-scale
    buffer = picam2.capture_array()
    cv2.imwrite('color.jpg', buffer)
    color = cv2.cvtColor(buffer, cv2.COLOR_RGB2BGR)

    hsv = cv2.cvtColor(color, cv2.COLOR_BGR2HSV)
    
    # Threshold of blue in HSV space
    lower_blue = np.array([40, 40, 40]) # Darker bound of color
    upper_blue = np.array([100, 100, 100]) # Lighter bound of color
 
    mask = cv2.inRange(hsv, lower_blue, upper_blue)
    cv2.imwrite('binary.jpg', mask)

    # Get contours in image 
    contours, hierarchy = cv2.findContours(image=mask, mode=cv2.RETR_TREE, method=cv2.CHAIN_APPROX_NONE)

    # Convert grey-scale into RGB image to display contours
    cv2.drawContours(image=buffer, contours=contours, contourIdx=-1, color=(0, 255, 0), thickness=2, lineType=cv2.LINE_AA)

    # Save image with contours drawn on top
    cv2.waitKey(500)
    cv2.imwrite('contours.jpg', buffer)

    end_time = time.monotonic()
    print((end_time - start_time))
