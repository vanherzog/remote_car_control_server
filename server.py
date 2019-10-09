from flask import Flask, request, Response, render_template, send_from_directory
import camera

app = Flask(__name__)

@app.route("/")
def index():
  return render_template("index.html")

def gen(camera):
    while True:
        frame = camera.get_frame()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

@app.route("/test")
def test():
  return render_template("test.html")

@app.route("/stream")
def stream():
    return Response(gen(Camera()),
                    mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__ == "__main__":
  app.run(host='0.0.0.0',debug=True)
