import RPi.GPIO  as GPIO
import time
import sys

GPIO.setmode(GPIO.BOARD)
int1=7 
int2=11
int3=13
int4=15
GPIO.setup(int1,GPIO.OUT)
GPIO.setup(int2,GPIO.OUT)
GPIO.setup(int3,GPIO.OUT)
GPIO.setup(int4,GPIO.OUT)
def handleRequest(s,d):
    handleTemp(s)
    handleRightLeft(d)

def handleRightLeft(n):
    if n==-2:
        sharpLeft()
    elif n==-1:
        mediumLeft()
    elif n==0:
        pass
    elif n==1:
        mediumRight()
    elif n==2:
        sharpRight()
    else:
        pass
#n=sleeptimer x=loop repeats
def handleTemp(n):
    if n==0:
        off();
    elif n==1:
        slowForward(0.02,5)
    elif n==2:
        slowForward(0.01,10)
    elif n==3:
        forward()
        time.sleep(0.2)
    elif n==-1:
        slowBack(0.02,10)
    else:
        pass
def sharpLeft():
    forward()
    time.sleep(0.0066)
    rightForward()
    time.sleep(0.0134)
def sharpRight():
    forward()
    time.sleep(0.0066)
    leftForward()
    time.sleep(0.0134)
def mediumLeft():
    forward()
    time.sleep(0.01)
    rightForward()
    time.sleep(0.01)
def mediumRight():
    forward()
    time.sleep(0.01)
    leftForward()
    time.sleep(0.01)        

def slowForward(n,x):
    for x in range(0,x):
        forward()
        time.sleep(n)
        off()
        time.sleep(n)

def slowBack(n,x):
    for x in range(0,x):
        backward()
        time.sleep(n)
        off()
        time.sleep(n)

def off():
    GPIO.output(int1,False)
    GPIO.output(int2,False)
    GPIO.output(int3,False)
    GPIO.output(int4,False)     


def forward():   
    GPIO.output(int1,False)
    GPIO.output(int2,True)
    GPIO.output(int3,False)
    GPIO.output(int4,True)

def backward():
    GPIO.output(int1,True)
    GPIO.output(int2,False)
    GPIO.output(int3,True)
    GPIO.output(int4,False)   

def leftForward():
    #l f
    GPIO.output(int1,False)
    GPIO.output(int2,False)
    GPIO.output(int3,False)
    GPIO.output(int4,True)

def rightForward():
    #r f
    GPIO.output(int1,False)
    GPIO.output(int2,True)
    GPIO.output(int3,False)
    GPIO.output(int4,False)


#r b
print("rb")
GPIO.output(int1,True)
GPIO.output(int2,False)
GPIO.output(int3,False)
GPIO.output(int4,False)
time.sleep(4)

#l b
print("lb")
GPIO.output(int1,False)
GPIO.output(int2,False)
GPIO.output(int3,True)
GPIO.output(int4,False)
time.sleep(4)



'''
for x in range(1,10):
    handleTemp(1)
for x in range(1,10):
    handleTemp(2)
for x in range(1,10):
    handleTemp(3)
'''
GPIO.cleanup()
print("finnish")

