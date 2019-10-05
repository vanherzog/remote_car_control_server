from flask import Flask
app = Flask(__name__)

@app.route("/")
def index():
  return "<html><body><h1>Test site running under Flaskkkk</h1></body></html>"

@app.route("/test")
def test():
  return "<html><body><h1>Testing testing</h1></body></html>"

if __name__ == "__main__":
  app.run(host='0.0.0.0',debug=True)
