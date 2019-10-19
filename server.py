from flask import Flask, request, Response, render_template, send_from_directory
from flask_restful import Resource, Api
from flask_socketio import SocketIO, send
from subprocess import call, check_output
from threading import Thread
import os
import socket
ip = (([ip for ip in socket.gethostbyname_ex(socket.gethostname())[2] if not ip.startswith("127.")] or [[(s.connect(("8.8.8.8", 53)), s.getsockname()[0], s.close()) for s in [socket.socket(socket.AF_INET, socket.SOCK_DGRAM)]][0][1]]) + ["no IP found"])[0]

app = Flask(__name__)
api = Api(app)
socketio = SocketIO(app, cors_allowed_origins="*")
todos = {}

# def listen():
#   global socketio
#   socketio.on('message', handleControl)

# def handleControl(message):
#   global socketio
#   socketio.emit('resp', message)
#   print('message')

@socketio.on('message')
def handleMessage(message):
  print('message: ', message)
  
@socketio.on('disconnect')
def handleClose():
  print('closed')
  
@socketio.on('connect')
def handleClose():
  print('connected')
  
@socketio.on('motion')
def handleClose(motion):
  print('Motion: ', motion)

@app.route("/")
def index():
  return render_template("index.html")

@app.route("/test")
def test():
  return render_template("test.html")

class Control(Resource):
  def put(self, command):
    return(command)

class InitCamera(Resource):
  def put(self):
    if (os.system('service camerastream status') == 0):
      call(['sudo', '/bin/systemctl', 'stop', 'camerastream.service'])
    else:
      call(['sudo', '/bin/systemctl', 'start', 'camerastream.service'])
    return(os.system('service camerastream status'))

api.add_resource(Control, '/control/<string:command>')
api.add_resource(InitCamera, '/camera')

if __name__ == "__main__":
  app.run(host=ip)
  socketio.run(app)
  
