import os
from flask import Flask

app = Flask(__name__)

@app.route('/', methods=["POST"])
def hello():
    return 'ok'

@app.route('/', methods=["GET"])
def getHelloWorld():
    return 'ok'
  
if __name__ == 'main':
    # Bind to PORT if defined, otherwise default to 5000.
    app.run(threaded=True, port=3001)
