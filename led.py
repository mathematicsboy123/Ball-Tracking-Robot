import RPi.GPIO as GPIO

# Set up LED switches
def switchSetup():
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(5, GPIO.OUT)
    GPIO.setup(6, GPIO.OUT)
    GPIO.setup(13, GPIO.OUT)

# Change the LED's states
def switch(port, status):
    if port == 1:
        if status == 1:
            GPIO.output(5, GPIO.HIGH)
        elif status == 0:
            GPIO.output(5,GPIO.LOW)
        else:
            pass
    elif port == 2:
        if status == 1:
            GPIO.output(6, GPIO.HIGH)
        elif status == 0:
            GPIO.output(6,GPIO.LOW)
        else:
            pass
    elif port == 3:
        if status == 1:
            GPIO.output(13, GPIO.HIGH)
        elif status == 0:
            GPIO.output(13,GPIO.LOW)
        else:
            pass
    else:
        print('Wrong Command: Example--switch(3, 1)->to switch on port3')

# Turn off all switches
def set_all_switch_off():
    switch(1,0)
    switch(2,0)
    switch(3,0)

if __name__ == "__main__":
    switchSetup()
    while 1:
        try:
            switch(1,1)
            switch(2,1)
            switch(3,1)
        except KeyboardInterrupt:
            set_all_switch_off()
            exit()
