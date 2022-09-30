import RPi.GPIO as GPIO
import time
GPIO.setwarnings(False)

red = 2
blue = 4
yellow = 3
green = 7



GPIO.setmode(GPIO.BCM)


GPIO.setup(red,GPIO.OUT)
GPIO.setup(blue,GPIO.OUT)
GPIO.setup(yellow, GPIO.OUT)
GPIO.setup(green, GPIO.OUT)

def red_on():
	GPIO.output(red,1)

def blue_on():
	GPIO.output(blue,1)

def green_on():
	GPIO.output(green,1)

def yellow_on():
	GPIO.output(yellow,1)


def all_off():
	GPIO.output(red,0)
	GPIO.output(blue,0)
	GPIO.output(yellow,0)
	GPIO.output(green,0)


all_off()
