import time 
import random
import RPi.GPIO as GPIO
import LEDRGB as LED
colors = ['R', 'G', 'B', 'Y']
x=0
colors = ['R', 'G', 'B', 'Y']
R_pin = 11
G_pin = 12
B_pin = 13
LED.setup(R_pin, G_pin, B_pin)
while x==0:
	def append_list():
		n = random.randint(0,3)
		LED.setColor(colors[n])
		time.sleep(0.3)
	if __name__=='__main__':
		try:
			append_list()
		except KeyboardInterrupt:
			print"Good Bye"
			x=1
			LED.destroy()
