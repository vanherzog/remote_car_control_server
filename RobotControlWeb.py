# Autor:	Ingmar Stapel
# Date:		20160104
# Version:	1.1
# Homepage:	www.custom-build-robots.com

import sys
sys.path.append("/home/pi/robot")

import L298NHBridge as HBridge

import webiopi

speedleft = 0
speedright = 0
speed = 0
# the variable step sets the step length for the acceleration
step = 0

def initiate():
	global speedleft
	global speedright
	global speed
	global step

	speedleft = 0
	speedright = 0
	step = 0.3
	
# ButtonForward is the arrow to drive forward with the Cardboard-Car
@webiopi.macro
def ButtonForward():
	global speedleft
	global speedright
	
	# accelerate the Cardboard-Car
	speedleft = speedleft + step
	speedright = speedright + step

	if speedleft > 1:
		speedleft = 1
	if speedright > 1:
		speedright = 1
	
	HBridge.setMotorLeft(speedleft)
	HBridge.setMotorRight(speedright)
		
# ButtonReverse is the arrow to reverse / drive back with the Cardboard-Car
@webiopi.macro
def ButtonReverse():	
	global speedleft
	global speedright
	
	# slow down the Cardboard-Car
	speedleft = speedleft - step
	speedright = speedright - step

	if speedleft < -1:
		speedleft = -1
	if speedright < -1:
		speedright = -1
	
	HBridge.setMotorLeft(speedleft)
	HBridge.setMotorRight(speedright)
	
# ButtonTurnLeft is the arrow to turn the Cardboard-Car left
@webiopi.macro
def ButtonTurnLeft():
	global speedleft
	global speedright

	speedleft = speedleft - step
	speedright = speedright + step
		
	if speedleft < -1:
		speedleft = -1
	
	if speedright > 1:
		speedright = 1
	
	HBridge.setMotorLeft(speedleft)
	HBridge.setMotorRight(speedright)

# ButtonTurnRight is the arrow to turn the Cardboard-Car right
@webiopi.macro
def ButtonTurnRight():	
	global speedleft
	global speedright
		
	speedright = speedright - step
	speedleft = speedleft + step
	
	if speedright < -1:
		speedright = -1
	if speedleft > 1:
		speedleft = 1
	
	HBridge.setMotorLeft(speedleft)
	HBridge.setMotorRight(speedright)
	
# ButtonStop is the stop button and stops the Cardboard-Car.	
@webiopi.macro
def ButtonStop():	
	global speedleft
	global speedright
	
	speedleft = 0
	speedright = 0
	HBridge.setMotorLeft(speedleft)
	HBridge.setMotorRight(speedright)

initiate()	
	
# starten des Web-Servers
server = webiopi.Server(port=8000, coap_port=8081, configfile=None)
# Hier werden die Buttons mit den definierten Funktionen hinterlegt
server.addMacro(ButtonForward)
server.addMacro(ButtonStop)
server.addMacro(ButtonReverse)
server.addMacro(ButtonTurnRight)
server.addMacro(ButtonTurnLeft)

webiopi.runLoop()
server.stop()
	
# End
