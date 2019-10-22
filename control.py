import RPi.GPIO  as GPIO
import time

#int1 - 7: forward right
#int2 - 11: backward right
#int3 - 13: forward left
#int4 - 15: backward left

#wiring scheme needs to be clearer
int1 = 7
int2 = 11
int3 = 13
int4 = 15
en1 = 16
en2= 18
l=0
r=0

def Setup():
	global int1, int2, int3, int4, en1, en2, l, r

	GPIO.setmode(GPIO.BOARD)
	GPIO.setup(int1,GPIO.OUT)
	GPIO.setup(int2,GPIO.OUT)
	GPIO.setup(int3,GPIO.OUT)
	GPIO.setup(int4,GPIO.OUT)
	GPIO.setup(en1,GPIO.OUT)
	GPIO.setup(en2,GPIO.OUT)

Setup()
l = GPIO.PWM(en1, 100)
r = GPIO.PWM(en2, 100)
l.start(0)
r.start(0)
#en1,en2 one is left one is right

#p = GPIO.PWM(channel, duty cycle)

def Forward():
	GPIO.output(int1, True)
	GPIO.output(int2, False)
	GPIO.output(int3, True)
	GPIO.output(int4, False)
def Backward():
	GPIO.output(int1, False)
	GPIO.output(int2, True)
	GPIO.output(int3, False)
	GPIO.output(int4, True)
def Turnright():
	GPIO.output(int1, True)
	GPIO.output(int2, False)
	GPIO.output(int3, False)
	GPIO.output(int4, False)
def Turnleft():
	GPIO.output(int1, False)
	GPIO.output(int2, False)
	GPIO.output(int3, True)
	GPIO.output(int4, False)
def _Break_():
	GPIO.output(int1, False)
	GPIO.output(int2, False)
	GPIO.output(int3, False)
	GPIO.output(int4, False)
		
		
#-left +right x 
#+for -backward y
def X_axis(x):
	if x < 0:
		x = -x
		l.ChangeDutyCycle(x*10)
		Turnright()
		print ("turning left")
	elif x >= 0:
		r.ChangeDutyCycle(x*10)
		Turnleft()
		print ("turning right")
		
def Y_axis(y):
	if y < 0:
		y = -y
		l.ChangeDutyCycle(y*20)
		r.ChangeDutyCycle(y*20)
		Backward()
		print ("go back")
	elif y >=0:
		l.ChangeDutyCycle(y*20)
		r.ChangeDutyCycle(y*20)
		Forward()
		print ("go forth")
		
def Control(x, y):
	if x != 0:
		X_axis(x)
	else:
		Y_axis(y)


while True:

	val1 = input("x_axis: ")
	val2 = input("y_axis: ")
	Control(val1, val2)
	time.sleep(3)
	
	GPIO.cleanup()
	Setup()
		
		
