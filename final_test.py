#!/usr/bin/python3
import time
import logging
import time
import os
import cv2
from picamera2 import Picamera2, Preview, MappedArray

# This version creates a lores YUV stream, extracts the Y channel and runs the face
# detector directly on that. We use the supplied OpenGL accelerated preview window
# and delegate the face box drawing to its callback function, thereby running the
# preview at the full rate with face updates as and when they are ready.

def draw_faces(request):
    pass


picam2 = Picamera2()
picam2.start_preview(Preview.QTGL)
config = picam2.preview_configuration(main={"size": (640, 480)},
                                      lores={"size": (320, 240), "format": "YUV420"})
picam2.configure(config)

(w0, h0) = picam2.stream_configuration("main")["size"]
(w1, h1) = picam2.stream_configuration("lores")["size"]
s1 = picam2.stream_configuration("lores")["stride"]
picam2.post_callback = draw_faces

picam2.start()

start_time = time.monotonic()
# Run for 10 seconds so that we can include this example in the test suite.
while True:
    buffer = picam2.capture_buffer("lores")
    grey = buffer[:s1 * h1].reshape((h1, s1))
    cv2.imshow("grey", grey)

    ret, thresh = cv2.threshold(grey, 150, 255, cv2.THRESH_BINARY)
    cv2.imshow('Binary image', thresh)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    contours, hierarchy = cv2.findContours(image=thresh, mode=cv2.RETR_TREE, method=cv2.CHAIN_APPROX_NONE)
    image_copy = thresh.copy()
    color = cv2.cvtColor(grey, cv2.COLOR_GRAY2RGB)
    cv2.imshow("color", color)
    cv2.drawContours(image=color, contours=contours, contourIdx=-1, color=(0, 255, 0), thickness=2, lineType=cv2.LINE_AA)

    cv2.imshow("contours_drawn", color)
    cv2.waitKey(0)
    cv2.imwrite('contours.jpg', color)
    cv2.destroyAllWindows()
