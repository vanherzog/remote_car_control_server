#foward big round shape
#int1 - 7: forward right
#int2 - 11: backward left
#int3 - 13: forward right
#int4 - 15: backward left


import RPi.GPIO  as GPIO
import time


int1=7
int2=11
int3=13
int4=15

#setup
GPIO.setmode(GPIO.BOARD)
GPIO.setup(int1,GPIO.OUT)
GPIO.setup(int2,GPIO.OUT)
GPIO.setup(int3,GPIO.OUT)
GPIO.setup(int4,GPIO.OUT)

GPIO.output(int1,True)
GPIO.output(int2,False)
GPIO.output(int3,False)
GPIO.output(int4,False)
time.sleep(4)

GPIO.output(int1,False)
GPIO.output(int2,True)
GPIO.output(int3,False)
GPIO.output(int4,False)
time.sleep(4)

GPIO.output(int1,False)
GPIO.output(int2,False)
GPIO.output(int3,True)
GPIO.output(int4,False)
time.sleep(4)

GPIO.output(int1,False)
GPIO.output(int2,False)
GPIO.output(int3,False)
GPIO.output(int4,True)
time.sleep(4)

GPIO.cleanup()
print("finish")
