#this is for 4 random notes
import RPi.GPIO as GPIO
import time
import random
#breadboard
GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
#assign pin
buzz_pin = 32
#set passive buzzer pins mode
GPIO.setup(buzz_pin, GPIO.OUT)
Buzz= GPIO.PWM(buzz_pin, 1000)

frequencies = [220, 440, 880, 1760]
n=random.randint(0,3)
Buzz.ChangeFrequency(frequencies[n])
Buzz.start(50)
time.sleep(0.5)
Buzz.stop()

