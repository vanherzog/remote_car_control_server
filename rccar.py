import RPi.GPIO as GPIO
import time
import sys
import Tkinter as tk

def init():
	GPIO.setmode(GPIO.BOARD)
	GPIO.setup(7, GPIO.OUT)
	GPIO.setup(11, GPIO.OUT)

	
def up(t):
	init()
	GPIO.output(7, False)
	GPIO.output(11, True)
	GPIO.output(13, True)
	GPIO.output(15, False)
	time.sleep(t)
	GPIO.cleanup()
	
def down(t):
	init()
	GPIO.output(7, True)
	GPIO.output(11, False)
	GPIO.output(15, True)
	GPIO.output(13, False)
	time.sleep(t)
	GPIO.cleanup()
	
def left(t):
	init()
	GPIO.output(7, True)
	GPIO.output(11, True)
	GPIO.output(13, True)
	GPIO.output(15, False)
	time.sleep(t)
	GPIO.cleanup()
	
def right(t):
	init()
	GPIO.output(7, False)
	GPIO.output(11, True)
	GPIO.output(13, False)
	GPIO.output(13, False)
	time.sleep(t)
	GPIO.cleanup()
	
def key_input(event):
	init()
	print 'Key: ', event.char
	key_press = event.char
	sleep_time = 1
	
	if key_press.lower() == 'w':
		up(sleep_time)
	elif key_press.lower() == 's':
		down(sleep_time)
	elif key_press.lower() == 'a':
		left(sleep_time)
	elif key_press.lower() == 'd':
		right(sleep_time)
		
command = tk.Tk()
command.bind('<KeyPress>', key_input)
command.mainloop()