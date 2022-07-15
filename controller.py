import image_processing
import time
from move import move, motorStop, destroy, setup
from led import set_all_switch_off, switch, switchSetup
from servo import servo, apply_offset_clipper, reset_servos
from armutils import solver
    
image_processing.config_camera()


def ball_tracking():
    # Get information about the image
    image_detection = image_processing.detect_ball()
    if len(image_detection) == 2:
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
        time.sleep(5)
        servo(4, 0)
        time.sleep(10)
        servo(2, 180)
        set_all_switch_off()
        motorStop()
        destroy()
        exit()
    elif image_detection[1] == "yes":
        # If image is found then rotate appropriately to try and bring it into the center of the camera
        if image_detection[0] < 0.4:
            move(100, "forward", "left", 0.9)
        elif 0.35 < image_detection[0] < 0.65:
            move(80, "forward", "no", 0.9)
        elif image_detection[0] > 0.6:
            move(100, "forward", "right", 0.9)
    else:
        move(100, "forward", "right", 0.9)
    time.sleep(0.08)
    motorStop()
    time.sleep(0.1)


if __name__ == "__main__":
    reset_servos()
    switchSetup()
    switch(1,1)
    switch(2,1)
    switch(3,1)
    setup()
    while True:
        try:
            ball_tracking()
        except KeyboardInterrupt:
            set_all_switch_off()
            motorStop()
            destroy()
            exit()
