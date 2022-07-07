from operator import ge
import numpy as np
import time
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)

# Left Motor Motor 1
A1A = 5
A1B = 7

# Right Motor Motor 2
B1A = 11
B1B = 13

trigger = 15
echo = 19

trigger_2 = 16
echo_2 = 18

# Set up GPIO pins
GPIO.setup(trigger, GPIO.OUT)
GPIO.setup(echo, GPIO.IN)

GPIO.setup(trigger_2, GPIO.OUT)
GPIO.setup(echo_2, GPIO.IN)

GPIO.setup(A1B, GPIO.OUT)
GPIO.setup(A1A, GPIO.OUT)

GPIO.setup(B1B, GPIO.OUT)
GPIO.setup(B1A, GPIO.OUT)


# Get distance for the forward ultrasonic sensor
def get_distance_forward():
    # Emmit sound wave from trigger pin
    GPIO.output(trigger, True)

    time.sleep(0.00001)
    GPIO.output(trigger, False)
    
    # Get start and stop time
    start = time.time()
    stop = time.time()
    
    # Measure the time that it takes for the wave to come back
    while GPIO.input(echo) == 0:
        start = time.time()
    
    while GPIO.input(echo) == 1:
        stop = time.time()

    # Calculate the distance of the object
    elapsed = stop - start
    distance = (elapsed * 34300) / 2
    return distance


# Get the distance from the back ultrasonic sensor
def get_distance_reverse():
    # Emmit sound wave from trigger pin
    GPIO.output(trigger_2, True)

    time.sleep(0.00001)
    GPIO.output(trigger_2, False)

    # Get start and stop time
    start = time.time()
    stop = time.time()
    
    # Measure the time that it takes for the wave to come back
    while GPIO.input(echo_2) == 0:
        start = time.time()
    
    while GPIO.input(echo_2) == 1:
        stop = time.time()

    # Calculate the distance of the object
    elapsed = stop - start
    distance = (elapsed * 34300) / 2
    return distance

# Reverse
def reverse():
    GPIO.output(A1B, GPIO.HIGH)
    GPIO.output(A1A, GPIO.LOW)
    GPIO.output(B1B, GPIO.HIGH)
    GPIO.output(B1A, GPIO.LOW)

# Forward
def forward():
    GPIO.output(A1B, GPIO.LOW)
    GPIO.output(A1A, GPIO.HIGH)
    GPIO.output(B1B, GPIO.LOW)
    GPIO.output(B1A, GPIO.HIGH)

# Right
def rightturn():
    GPIO.output(A1B,GPIO.LOW)
    GPIO.output(A1A,GPIO.HIGH)
    GPIO.output(B1B,GPIO.HIGH)
    GPIO.output(B1A,GPIO.LOW)

# Left
def leftturn():
    GPIO.output(A1B,GPIO.HIGH)
    GPIO.output(A1A,GPIO.LOW)
    GPIO.output(B1B,GPIO.LOW)
    GPIO.output(B1A,GPIO.HIGH)

# Stop
def stop():
    GPIO.output(A1A,GPIO.LOW)
    GPIO.output(A1B,GPIO.LOW)
    GPIO.output(B1A,GPIO.LOW)
    GPIO.output(B1B,GPIO.LOW)

# Find the color values in the center of an image (Troubleshooting)
def center_average(hsv):
    avg = np.array([0, 0, 0])
    for i in range(10):
        x = int(len(hsv)/2)
        row = hsv[x]
        y = int(len(row)/2) 
        y += i

        pixel = row[y]
        avg += pixel
    
    divided = avg/10
    for i in range(0, 3):
        divided[i] = int(divided[i])
    print(divided)

if __name__ == "__main__":
    try:
        while True:
            dist = get_distance_reverse()
            print(dist)
    except KeyboardInterrupt:
        print("Measurement stopped by User")
        GPIO.cleanup()
