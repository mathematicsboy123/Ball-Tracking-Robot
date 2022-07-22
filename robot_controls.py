# Written by Shreyans Daga
import image_processing
import time
from move import move, motorStop, destroy, setup
from led import set_all_switch_off, switch, switchSetup
from servo import servo, apply_offset_clipper, reset_servos
from armutils import solver
from OLED import OLED_ctrl

"""Define Robot class where all the functions are imported and setup 
so that this class can be used in the controller code"""

class Robot:
    def config_camera(self):
        image_processing.config_camera()

    def image_data(self):
        return image_processing.detect_ball()

    def forward(self):
        move(80, "forward", "no", 0.9)
    
    def right_turn(self):
        move(100, "forward", "right", 0.9)
    
    def left_turn(self):
        move(100, "forward", "left", 0.9)

    def reverse(self):
        move(80, "backward", "no", 0.9)
    
    def movement_time(self):
        time.sleep(0.08)
        motorStop()
        time.sleep(0.1)
    
    def pickup_protocol(self, image_detection):
        angles = solver(image_detection[0])
        move(80, "forward", "no", 0.9)
        time.sleep(0.08)
        motorStop()
        time.sleep(0.1)
        offset = apply_offset_clipper(image_detection[1])
        print(offset)
        servo(1, offset)
        servo(2, (angles[0] + 90))
        if angles[1] < 65:
            servo(3, (angles[1]))
        time.sleep(1)
        servo(4, 40)
        time.sleep(3)
        servo(2, 180)

    def servo_reset(self):
        reset_servos()
    
    def led_on(self):
        switchSetup()
        switch(1,1)
        switch(2,1)
        switch(3,1)
    
    def oled(self):
        screen = OLED_ctrl()
        screen.start()
    
    def motor_setup(self):
        setup()
    
    def terminate(self):
        set_all_switch_off()
        motorStop()
        destroy()
        exit()
