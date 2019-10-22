import RPi.GPIO  as GPIO
import time

#int1 - 7: forward right
#int2 - 11: backward right
#int3 - 13: forward left
#int4 - 15: backward left


class Controller:
	#wiring scheme needs to be clearer
	def __init__(self):
		self.l = GPIO.PWM(en1, 100)
		self.r = GPIO.PWM(en2, 100)
		self.l.start(0)
		self.r.start(0)
		self.int1 = 7
		self.int2 = 11
		self.int3 = 13
		self.int4 = 15
		self.en1 = 16
		self.en2= 18
		self.l=0
		self.r=0
		# self.Setup();

	def Setup(self):
		GPIO.setmode(GPIO.BOARD)
		GPIO.setup(self.int1,GPIO.OUT)
		GPIO.setup(self.int2,GPIO.OUT)
		GPIO.setup(self.int3,GPIO.OUT)
		GPIO.setup(self.int4,GPIO.OUT)
		GPIO.setup(self.en1,GPIO.OUT)
		GPIO.setup(self.en2,GPIO.OUT)

	# Setup()
	
	
	#en1,en2 one is left one is right

	#p = GPIO.PWM(channel, duty cycle)

	def Forward(self):
		GPIO.output(self.int1, True)
		GPIO.output(self.int2, False)
		GPIO.output(self.int3, True)
		GPIO.output(self.int4, False)
  
	def Backward(self):
		GPIO.output(self.int1, False)
		GPIO.output(self.int2, True)
		GPIO.output(self.int3, False)
		GPIO.output(self.int4, True)
  
	def Turnright(self):
		GPIO.output(self.int1, True)
		GPIO.output(self.int2, False)
		GPIO.output(self.int3, False)
		GPIO.output(self.int4, False)
  
	def Turnleft(self):
		GPIO.output(self.int1, False)
		GPIO.output(self.int2, False)
		GPIO.output(self.int3, True)
		GPIO.output(self.int4, False)
  
	def _Break_(self):
		GPIO.output(self.int1, False)
		GPIO.output(self.int2, False)
		GPIO.output(self.int3, False)
		GPIO.output(self.int4, False)
			
			
	#-left +right x 
	#+for -backward y
	def X_axis(self):
		if self.x < 0:
			self.x = -self.x
			self.l.ChangeDutyCycle(self.x*10)
			self.Turnright()
			print ("turning left")
		else:
			self.r.ChangeDutyCycle(self.x*10)
			self.Turnleft()
			print ("turning right")
			
	def Y_axis(self):
		if self.y < 0:
			self.y = -self.y
			self.l.ChangeDutyCycle(self.y*20)
			self.r.ChangeDutyCycle(self.y*20)
			self.Backward()
			print ("go back")
		else:
			self.l.ChangeDutyCycle(self.y*20)
			self.r.ChangeDutyCycle(self.y*20)
			self.Forward()
			print ("go forth")
			
	def Control(self):
		if self.x != 0:
			self.X_axis(x)
		else:
			self.Y_axis(y)
  
	def set(self, x, y):
		self.x = x
		self.y = y
		self.Control()
   
	def CleanUp(self):
		GPIO.cleanup()


	# while True:

	# 	val1 = input("x_axis: ")
	# 	val2 = input("y_axis: ")
	# 	Control(val1, val2)
	# 	time.sleep(3)
		
	# 	GPIO.cleanup()
	# 	Setup()
			
			