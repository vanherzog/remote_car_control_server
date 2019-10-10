import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BOARD)

int1=7
int2=11

GPIO.setup(7,GPIO.OUT)
GPIO.setup(11,GPIO.OUT)

GPIO.output(int1,GPIO.HIGH)
GPIO.output(int2,GPIO.LOW)
time.sleep(5)

GPIO.cleanup()