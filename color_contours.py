import logging
import cv2
from picamera2 import Picamera2, Preview, MappedArray

# Configure camera image types
picam2 = Picamera2()
config = picam2.preview_configuration(main={"size": (640, 480)},
                                      lores={"size": (320, 240), "format": "YUV420"})
picam2.configure(config)

# Configure camera to be able to take pictures
(w0, h0) = picam2.stream_configuration("main")["size"]
(w1, h1) = picam2.stream_configuration("lores")["size"]
s1 = picam2.stream_configuration("lores")["stride"]
picam2.start()

while True:
    # Get color and convert to gray-scale
    buffer = picam2.capture_buffer("lores")
    grey = buffer[:s1 * h1].reshape((h1, s1))
    color = cv2.cvtColor(grey, cv2.COLOR_GRAY2RGB)

    # Convert gray-scale to binary
    thresh = cv2.adaptiveThreshold(grey, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 601, 2)
    cv2.waitKey(500)
    cv2.imwrite('binary.jpg', thresh)

    # Get contours in image 
    contours, hierarchy = cv2.findContours(image=thresh, mode=cv2.RETR_TREE, method=cv2.CHAIN_APPROX_NONE)
    print(contours)
    
    # Convert grey-scale into RGB image to display contours
    cv2.drawContours(image=color, contours=contours, contourIdx=-1, color=(0, 255, 0), thickness=2, lineType=cv2.LINE_AA)

    # Save image with contours drawn on top
    cv2.waitKey(500)
    cv2.imwrite('contours.jpg', color)
    break
