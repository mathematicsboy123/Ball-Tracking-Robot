import time
import RPi.GPIO as GPIO
from servo import turn_front_servo

# motor_EN_A: Pin7  |  motor_EN_B: Pin11
# motor_A:  Pin8,Pin10    |  motor_B: Pin13,Pin12

# Configure RPI GPIO pins with what they are connected to
Motor_A_EN    = 4
Motor_B_EN    = 17

Motor_A_Pin1  = 26
Motor_A_Pin2  = 21
Motor_B_Pin1  = 27
Motor_B_Pin2  = 18

Dir_forward   = 0
Dir_backward  = 1

left_forward  = 1
left_backward = 0

right_forward = 0
right_backward= 1

pwn_A = 0
pwm_B = 0

# Motor stops
def motorStop():
	GPIO.output(Motor_A_Pin1, GPIO.LOW)
	GPIO.output(Motor_A_Pin2, GPIO.LOW)
	GPIO.output(Motor_B_Pin1, GPIO.LOW)
	GPIO.output(Motor_B_Pin2, GPIO.LOW)
	GPIO.output(Motor_A_EN, GPIO.LOW)
	GPIO.output(Motor_B_EN, GPIO.LOW)

# Motor initialization
def setup():
	global pwm_A, pwm_B
	GPIO.setwarnings(False)
	GPIO.setmode(GPIO.BCM)
	GPIO.setup(Motor_A_EN, GPIO.OUT)
	GPIO.setup(Motor_B_EN, GPIO.OUT)
	GPIO.setup(Motor_A_Pin1, GPIO.OUT)
	GPIO.setup(Motor_A_Pin2, GPIO.OUT)
	GPIO.setup(Motor_B_Pin1, GPIO.OUT)
	GPIO.setup(Motor_B_Pin2, GPIO.OUT)

	motorStop()
	try:
		pwm_A = GPIO.PWM(Motor_A_EN, 1000)
		pwm_B = GPIO.PWM(Motor_B_EN, 1000)
	except:
		pass

# Motor 2 positive and negative rotation
def motor_left(status, direction, speed):
	if status == 0: # stop
		GPIO.output(Motor_B_Pin1, GPIO.LOW)
		GPIO.output(Motor_B_Pin2, GPIO.LOW)
		GPIO.output(Motor_B_EN, GPIO.LOW)
	else:
		if direction == Dir_backward:
			GPIO.output(Motor_B_Pin1, GPIO.HIGH)
			GPIO.output(Motor_B_Pin2, GPIO.LOW)
			pwm_B.start(100)
			pwm_B.ChangeDutyCycle(speed)
		elif direction == Dir_forward:
			GPIO.output(Motor_B_Pin1, GPIO.LOW)
			GPIO.output(Motor_B_Pin2, GPIO.HIGH)
			pwm_B.start(0)
			pwm_B.ChangeDutyCycle(speed)

# Motor 1 positive and negative rotation
def motor_right(status, direction, speed):
	if status == 0: # stop
		GPIO.output(Motor_A_Pin1, GPIO.LOW)
		GPIO.output(Motor_A_Pin2, GPIO.LOW)
		GPIO.output(Motor_A_EN, GPIO.LOW)
	else:
		if direction == Dir_forward:#
			GPIO.output(Motor_A_Pin1, GPIO.HIGH)
			GPIO.output(Motor_A_Pin2, GPIO.LOW)
			pwm_A.start(100)
			pwm_A.ChangeDutyCycle(speed)
		elif direction == Dir_backward:
			GPIO.output(Motor_A_Pin1, GPIO.LOW)
			GPIO.output(Motor_A_Pin2, GPIO.HIGH)
			pwm_A.start(0)
			pwm_A.ChangeDutyCycle(speed)
	return direction


def move(speed, direction, turn, radius=0.6):# 0 < radius <= 1  
	# speed = 100
	if direction == 'forward':
		if turn == 'left':
			turn_front_servo("l")
			time.sleep(0.1)
			motor_left(1, left_backward, int(speed*radius))
			motor_right(1, right_forward, speed)
		elif turn == 'right':
			turn_front_servo("r")
			time.sleep(0.1)
			motor_left(1, left_forward, speed)
			motor_right(1, right_backward, int(speed*radius))
		else:
			turn_front_servo("s")
			time.sleep(0.1)
			motor_left(1, left_forward, speed)
			motor_right(1, right_forward, speed)
	elif direction == 'backward':
		if turn == 'left':
			turn_front_servo("r")
			time.sleep(0.1)
			motor_left(1, left_forward, int(speed*radius))
			motor_right(1, right_backward, speed)
		elif turn == 'right':
			turn_front_servo("l")
			time.sleep(0.1)
			motor_left(1, left_backward, speed)
			motor_right(1, right_forward, int(speed*radius))
		else:
			turn_front_servo("s")
			time.sleep(0.1)
			motor_left(1, left_backward, speed)
			motor_right(1, right_backward, speed)
	elif direction == 'no':
		if turn == 'right':
			turn_front_servo("r")
			time.sleep(0.1)
			motor_left(1, left_backward, speed)
			motor_right(1, right_forward, speed)
		elif turn == 'left':
			turn_front_servo("l")
			time.sleep(0.1)
			motor_left(1, left_forward, speed)
			motor_right(1, right_backward, speed)
		else:
			motorStop()
	else:
		pass

# Cleanp up GPIO pins
def destroy():
	motorStop()
	GPIO.cleanup()


if __name__ == '__main__':
	try:
		speed_set = 100
		setup()
		move(speed_set, 'forward', 'right', 0.9)
		time.sleep(5)
		move(speed_set, 'forward', 'left', 0.9)
		time.sleep(5)
		move(60, 'forward', 'no', 0.9)
		time.sleep(1)
		motorStop()
		destroy()
	except KeyboardInterrupt:
		destroy()
