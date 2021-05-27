import os
import requests
import json
from flask import Flask, render_template, request, jsonify
import telebot
import datetime

URL = 'http://vpn.texnomart.uz:8282/javoxir_ut_trendy/hs/deliverywebhook/e382d9ee722840d6a53e02d299331f4f'
TOKEN = '1886558847:AAHJEcszrZFebZUxbwLTK1X67ZKCNLmYyLM'

app = Flask(__name__)
bot = telebot.TeleBot(TOKEN)


@app.route('/', methods=['POST', 'GET'])
def hello():
    if request.method == 'POST':
        r = request.get_json()
        myobj = json.dumps(str(r))
        weburl = requests.post(URL,data = myobj)
        return jsonify(r)
    else:
        r = request.get_json()
        bot.send_message('500324557', 'text:\n' + str(r))
    return '<a href=\'login/\'>/login/</a><br> <a href=\'auth/\'>/auth/</a><br><a href=\'users/\'>/users/</a><br>'

if __name__ == 'main':
    # Bind to PORT if defined, otherwise default to 5000.
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
