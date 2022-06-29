import numpy as np
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)

# Left Motor Motor 1
A1A = 5
A1B = 7

# Right Motor Motor 2
B1A = 11
B1B = 13

GPIO.setup(A1B, GPIO.OUT)
GPIO.setup(A1A, GPIO.OUT)

GPIO.setup(B1B, GPIO.OUT)
GPIO.setup(B1A, GPIO.OUT)

def reverse():
    GPIO.output(A1B, GPIO.HIGH)
    GPIO.output(A1A, GPIO.LOW)
    GPIO.output(B1B, GPIO.HIGH)
    GPIO.output(B1A, GPIO.LOW)
    
def forward():
    GPIO.output(A1B, GPIO.LOW)
    GPIO.output(A1A, GPIO.HIGH)
    GPIO.output(B1B, GPIO.LOW)
    GPIO.output(B1A, GPIO.HIGH)
    
def rightturn():
    GPIO.output(A1B,GPIO.LOW)
    GPIO.output(A1A,GPIO.HIGH)
    GPIO.output(B1B,GPIO.HIGH)
    GPIO.output(B1A,GPIO.LOW)
     
def leftturn():
    GPIO.output(A1B,GPIO.HIGH)
    GPIO.output(A1A,GPIO.LOW)
    GPIO.output(B1B,GPIO.LOW)
    GPIO.output(B1A,GPIO.HIGH)

def stop():
    GPIO.output(A1A,GPIO.LOW)
    GPIO.output(A1B,GPIO.LOW)
    GPIO.output(B1A,GPIO.LOW)
    GPIO.output(B1B,GPIO.LOW)

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
