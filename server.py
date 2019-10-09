from flask import Flask, request, Response, render_template, send_from_directory
from flask_restful import Resource, Api
from subprocess import call

app = Flask(__name__)
api = Api(app)

todos = {}

@app.route("/")
def index():
  return render_template("index.html")

@app.route("/test")
def test():
  return render_template("test.html")

class TodoSimple(Resource):
    def get(self, todo_id):
        return 'what'

    def put(self, todo_id):
        todos[todo_id] = request.form['data']
        return {todo_id: todos[todo_id]}

class SimpleTest(Resource):
  def put(self, message):
    return message

class InitCamera(Resource):
    def put(self):
        call(['python3', 'camera.py'])
        return 'Camera Initialized'

api.add_resource(TodoSimple, '/<string:todo_id>')
api.add_resource(InitCamera, '/camera')
api.add_resource(SimpleTest, '/simpletest/<string:message>')

if __name__ == "__main__":
  app.run(host='0.0.0.0',debug=True)
