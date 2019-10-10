import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BOARD)

GPIO.setup(7,GPIO.OUT)
GPIO.setup(11,GPIO.OUT)
GPIO.setup(13,GPIO.OUT)
GPIO.setup(15,GPIO.OUT)

GPIO.output(7,GPIO.True)
time.sleep(1)
GPIO.output(7,GPIO.False)
GPIO.output(11,GPIO.True)
time.sleep(1)
GPIO.output(11,GPIO.False)
GPIO.output(13,GPIO.True)
time.sleep(1)
GPIO.output(13,GPIO.False)
GPIO.output(15,GPIO.True)
time.sleep(1)
GPIO.output(15,GPIO.False)

GPIO.cleanup()