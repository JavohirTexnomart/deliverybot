import os
import requests
import json
from flask import Flask, render_template, request, jsonify
import telebot

URL = 'http://vpn.texnomart.uz:8282/javoxir_ut_trendy/hs/deliverywebhook/e382d9ee722840d6a53e02d299331f4f'
TOKEN = '1886558847:AAHJEcszrZFebZUxbwLTK1X67ZKCNLmYyLM'

app = Flask(__name__)
secret = "e382d9ee722840d6a53e02d299331f4f"
bot = telebot.TeleBot(TOKEN)
bot.remove_webhook()
bot.set_webhook(url="https://https://deliverytelegrambot.herokuapp.com/{}".format(secret))

@app.route('/{}'.format(secret), methods=["POST"])
def hello():
    if request.method == 'POST':
        r = request.get_json()
        myobj = json.dumps(str(r))
        weburl = requests.post(URL,data = myobj)
        return jsonify(r)
    return 'ok'

@app.route('/', methods=["GET"])
def getHelloWorld():
    return 'ok'
if __name__ == 'main':
    # Bind to PORT if defined, otherwise default to 5000.
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
