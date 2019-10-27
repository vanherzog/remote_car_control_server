from flask import Flask, request, Response, render_template, send_from_directory
from flask_restful import Resource, Api
from flask_socketio import SocketIO, send
from subprocess import call, check_output
from threading import Thread
import os
import socket
from control import Controller
from time import sleep
ip = (([ip for ip in socket.gethostbyname_ex(socket.gethostname())[2] if not ip.startswith("127.")] or [[(s.connect(("8.8.8.8", 53)), s.getsockname()[0], s.close()) for s in [socket.socket(socket.AF_INET, socket.SOCK_DGRAM)]][0][1]]) + ["no IP found"])[0]

app = Flask(__name__)
api = Api(app)
socketio = SocketIO(app, cors_allowed_origins="*")
controller = Controller()
x = 0
y = 0
connectedCount=0
controller.Setup()


def control():
  print("is here")
  global x, y, controller
  while True:
    controller.set(x, y)
    sleep(0.01)

thread = Thread(target=control)


@socketio.on('message')
def handleMessage(message):
  global x, y
  if "," in message:
    token = message.split(',')
    x = int(token[0])
    y = int(token[1])
  print(x, y)
  

@socketio.on('disconnect')
def handleClose():
  global x, y
  x =0
  y =0
  send('closed')
  print('closed disconnected')
 
@socketio.on('connect')
def handleConnection():
  global connectedCount
  if connectedCount == 0:
    thread.start()
    connectedCount+=1
  send('connected')
  print('closed')

@socketio.on('motion')
def handleCloseMotion(motion):
  print('Motion1: ')

@app.route("/")
def index():
  return render_template("index.html")

class Control(Resource):
  def put(self, command):
    return(command)

class terminate(Resource):
  def put(self):
    call(['sudo', 'systemctl', 'stop', 'server'])

class InitCamera(Resource):
  def put(self):
    if (os.system('service camera status') == 0):
      call(['sudo', 'systemctl', 'stop', 'camera'])
    else:
      call(['sudo', 'systemctl', 'start', 'camera'])
    return(os.system('service camera status'))
  
api.add_resource(Control, '/control/<string:command>')
api.add_resource(InitCamera, '/camera')
api.add_resource(terminate, '/terminate')

if __name__ == "__main__":
  app.run(host=ip, debug=True)
  socketio.run(app)
  
  
