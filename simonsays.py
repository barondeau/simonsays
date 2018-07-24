import time 
import random
import RPi.GPIO as GPIO
import LEDRGB as LED
from getpass import getpass
GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
colors = ['R', 'G', 'B', 'Y']
freq = [300, 432, 528, 1300]

buzz_pin = 32
GPIO.setup(buzz_pin, GPIO.OUT)
Buzz= GPIO.PWM(buzz_pin, 1000)
x=0
y=0
counter = 0
R_pin = 11
G_pin = 12
B_pin = 13
LED.setup(R_pin, G_pin, B_pin)

while x==0:
	def validate_guess(c_seq_string,guess):
		if c_seq_string == guess:
			print"Nice"
		if c_seq_string != guess:
			print"Game over man! Game Over!"
			Buzz.ChangeFrequency(1000)
			Buzz.start(50)
			time.sleep(0.5)
			Buzz.stop()
			x=1
			exit()
	def loop():
		n=random.randint(0,3)
		n=y
		c_seq =[colors[n]]
		while True:
			for color in c_seq:
				Buzz.ChangeFrequency(freq[n])
				Buzz.start(50)
				LED.setColor(color)
				time.sleep(0.5)
				Buzz.stop()
				LED.noColor()
				time.sleep(0.5)
			guess = getpass('Guess the color sequence?(r,g,b,y)')
			c_seq_string = ''.join(c_seq)
			validate_guess(c_seq_string,guess.upper())
			n=random.randint(0,3)
			c_seq.append(colors[n])
			time.sleep(0.5)
			
	if __name__=='__main__':
		try:
			loop()
			
		except KeyboardInterrupt:
			print"Good Bye"
			x=1
			LED.destroy()
