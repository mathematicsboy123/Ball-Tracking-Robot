# Written by Shreyans Daga
from luma.core.interface.serial import i2c
from luma.core.render import canvas
from luma.oled.device import ssd1306
import time
import threading

# Check if OLED is available on i2c
try:
	serial = i2c(port=1, address=0x3C)
	device = ssd1306(serial, rotate=0)
except:
	print('OLED disconnected')

text_1 = "Ball Tracking Robot"
text_2 = "Made By Shreyans Daga"
text_3 = "Code on Github"
text_4 = "Webstite with videos"
text_5 = "Official Documentation"
text_6 = "Bluestamp Engineering"

# Initialize OLED class that has all of the code to operate OLED
class OLED_ctrl(threading.Thread):
	# Initialize arguments
	def __init__(self, *args, **kwargs):
		super(OLED_ctrl, self).__init__(*args, **kwargs)
		self.__flag = threading.Event()
		self.__flag.set()
		self.__running = threading.Event()
		self.__running.set()

	# Display text
	def run(self):
		while self.__running.isSet():
			self.__flag.wait()
			with canvas(device) as draw:
				draw.text((0, 0), text_1, fill="white")
				draw.text((0, 10), text_2, fill="white")
				draw.text((0, 20), text_3, fill="white")
				draw.text((0, 30), text_4, fill="white")
				draw.text((0, 40), text_5, fill="white")
				draw.text((0, 50), text_6, fill="white")
			self.pause()

	# Define basic functionality
	def pause(self):
		self.__flag.clear()

	def resume(self):
		self.__flag.set()

	def stop(self):
		self.__flag.set()
		self.__running.clear()

	# Actually light up the screen with the text
	def screen_show(self, position, text):
		global text_1, text_2, text_3, text_4, text_5, text_6
		if position == 1:
			text_1 = text
		elif position == 2:
			text_2 = text
		elif position == 3:
			text_3 = text
		elif position == 4:
			text_4 = text
		elif position == 5:
			text_5 = text
		elif position == 6:
			text_6 = text
		self.resume()

if __name__ == '__main__':
	screen = OLED_ctrl()
	screen.start()
	while 1:
		time.sleep(10)
		pass
