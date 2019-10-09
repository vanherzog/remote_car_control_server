from flask import Flask, request, Response, render_template, send_from_directory
from flask_restful import Resource, Api
from subprocess import call, check_output
from threading import Thread
import os

app = Flask(__name__)
api = Api(app)

todos = {}

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
  app.run(host='0.0.0.0',debug=True)
