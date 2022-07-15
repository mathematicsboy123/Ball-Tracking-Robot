import numpy as np
import cv2
from picamera2 import Picamera2
import time

picam2 = Picamera2()

# medium = 523.5 30-10cm
# close = 415.5 10cm double check
# far = 590 120-30

cwidth = 640
cheight = 480
ball_width = 6

# Configure camera image types
def config_camera():
    config = picam2.still_configuration(main={"size": (cwidth, cheight)})
    picam2.configure(config)
    picam2.start()


def detect_ball():
    focal_distance = 415.5
    # Get image and convert to BGR to HSV
    buffer = picam2.capture_array()
    color = cv2.cvtColor(buffer, cv2.COLOR_RGB2BGR)
    hsv = cv2.cvtColor(color, cv2.COLOR_BGR2HSV)
    
    # Threshold of red in HSV space
    lower_blue = np.array([1, 160, 170]) # Darker bound of color
    upper_blue = np.array([20, 255, 255]) # Lighter bound of color

    # Generate mask useing the color bounds
    mask = cv2.inRange(hsv, lower_blue, upper_blue)
    cv2.imwrite('binary.jpg', mask)

    # Find the white pixels and initialize basic variables
    white_pix = np.sum(mask == 255)
    cX = 0
    cY = 0
    red_found = "no"

    if white_pix > 500:
        # Generate kernal for image
        kernel = np.ones((5,5), np.uint8)

        # Erode and dialate binary image
        img_erosion = cv2.erode(mask, kernel, iterations=1)
        mask = cv2.dilate(img_erosion, kernel, iterations=3)
        cv2.imwrite('new_binary.jpg', mask)

        # Find contours in the image
        contours, hierarchy = cv2.findContours(image=mask, mode=cv2.RETR_TREE, method=cv2.CHAIN_APPROX_NONE)
        biggest_contour = None
        areabig = 0 

        # Loop through all of the countours and get the index for the biggest one
        for c in range(0, len(contours)):
            rect = cv2.boundingRect(contours[c])
            x,y,w,h = rect
            area = w*h
            if area > areabig:
                biggest_contour = c
                areabig = area

        # Draw a bounding rectangle around the largest contour
        try:
            rect = cv2.boundingRect(contours[biggest_contour])
            x,y,w,h = rect
            cv2.rectangle(color, (x,y), (x+w,y+h), (0,255,0), 2)
        except TypeError:
            print("TypeError")
            pass
        
        # Update center coordinates of the ball
        cX = int(round(((x + (w / 2))), 0))
        cY = int(round(((y + (h / 2))), 0))

        # Calculate distance from the ball and generate new focal distance
        dist = ((ball_width * focal_distance) / w)
        print(dist)
        if 11.5 < dist < 12.5:
            return [dist, cX/cwidth]

        # Find the center of the circle using the binary image
        cv2.circle(color, (cX,cY), radius=5, color=(255, 0, 0), thickness=-1)
        cv2.imwrite("center.jpg", color)
        red_found = "yes"

    # Return values to the controller program
    return [cX/cwidth, red_found, white_pix]

if __name__ == "__main__":
    config_camera()
    while True:
        detect_ball()
        time.sleep(0.2)
