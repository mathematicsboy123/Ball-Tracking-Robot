import testing
import time
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
    
testing.config_camera()

#forward()
#time.sleep(5)
stop()
#exit()

while True:
    image_detection = testing.detect_ball()
    if image_detection[1] == "yes":
        print(image_detection[2])
        if image_detection[0] < 0.4:
            rightturn()
        elif 0.35 < image_detection[0] < 0.65:
            forward()
        elif image_detection[0] > 0.6:
            leftturn()
        if image_detection[2] > 24000 or 0.49 < image_detection[3] < 0.51 and image_detection[2] > 20000 and 0.49 < image_detection[0] < 0.51:
            stop()
            GPIO.cleanup()
            exit()
    else:
        rightturn()
    time.sleep(0.06)
    stop()
    time.sleep(0.1)
