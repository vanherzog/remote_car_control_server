from flask import Flask, request, Response, render_template, send_from_directory

app = Flask(__name__)

@app.route("/")
def index():
  return render_template("index.html")

@app.route("/test")
def test():
  return render_template("test.html")

if __name__ == "__main__":
  app.run(host='0.0.0.0',debug=True)
