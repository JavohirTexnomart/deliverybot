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
    PORT = int(os.environ.get('PORT', 3000))
    app.run(host='0.0.0.0', port=PORT)
