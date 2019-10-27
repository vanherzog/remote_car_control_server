import RPi.GPIO  as GPIO
import time

class Controller:
	
	def __init__(self):
		print("hello world")
		self.int1 = 7
		self.int2 = 11
		self.int3 = 13
		self.int4 = 15
		self.en1 = 16
		self.en2= 18
		self.x =0
		self.y =0


		self.l=0
		self.r=0
		GPIO.setmode(GPIO.BOARD)
		GPIO.setup(self.en1,GPIO.OUT)
		GPIO.setup(self.en2,GPIO.OUT)
		self.l = GPIO.PWM(self.en1, 600)
		self.r = GPIO.PWM(self.en2, 600)
		self.l.start(0)
		self.r.start(0)
		# self.Setup();

	def Setup(self):
		GPIO.setup(self.int1,GPIO.OUT)
		GPIO.setup(self.int2,GPIO.OUT)
		GPIO.setup(self.int3,GPIO.OUT)
		GPIO.setup(self.int4,GPIO.OUT)
		
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
			
			
	def X_axis(self):
		if self.x < 0:
			self.x = -self.x
			if self.x == 1:
				self.l.ChangeDutyCycle(self.x*35)
				self.r.ChangeDutyCycle(self.x*12)
				self.Forward()
			if self.x == 2:
				self.l.ChangeDutyCycle(self.x*23)
				self.Turnright()
			print ("turning left")
		else:
			if self.x == 1:
				self.r.ChangeDutyCycle(self.x*35)
				self.l.ChangeDutyCycle(self.x*12)
				self.Forward()
			if self.x == 2:
				self.r.ChangeDutyCycle(self.x*23)
				self.Turnleft()
			print ("turning right")
			
	def Y_axis(self):
		if self.y < 0:
			self.y = -self.y
			if self.y <3:
				self.l.ChangeDutyCycle(self.y*30)
				self.r.ChangeDutyCycle(self.y*30)
			if self.y == 3:
				self.l.ChangeDutyCycle(self.y*33)
			self.Backward()
			print ("go back")
		else:
			if self.y <3:
				self.l.ChangeDutyCycle(self.y*30)
				self.r.ChangeDutyCycle(self.y*30)
			if self.y == 3:
				self.l.ChangeDutyCycle(self.y*33)
			self.Forward()
			print ("go forth")
			
	def Control(self):
		if self.x != 0:
			self.X_axis()
		else:
			self.Y_axis()
  
	def set(self, x, y):
		self.x = x
		self.y = y
		self.Control()
   
	def CleanUp(self):
		print("clean Up")
		GPIO.cleanup()
