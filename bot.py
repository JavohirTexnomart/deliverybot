from flask import Flask, request
import telebot
from flask_sslify import SSLify
import urllib.request
import requests
import json

app = Flask(__name__)
sslify = SSLify(app)

secret = "e382d9ee722840d6a53e02d299331f4f"
bot = telebot.TeleBot('1886558847:AAHJEcszrZFebZUxbwLTK1X67ZKCNLmYyLM')
bot.remove_webhook()
bot.set_webhook(url="https://javohirtexnomart.pythonanywhere.com/{}".format(secret))

@app.route('/{}'.format(secret), methods=["POST"])
def getMessage():
    update = request.get_json()
    if "message" in update:
        #url = 'http://vpn.texnomart.uz:8282/javoxir_ut_trendy/hs/deliverywebhook/e382d9ee722840d6a53e02d299331f4f'
        #myobj = str(update)
        #jsontext = json.dumps(myobj)
        #x = http.request('POST', url,body=jsontext)
        #text = update["message"]["text"]
        #chat_id = update["message"]["chat"]["id"]
        # bot.send_message(chat_id, "you said '{}'".format(text))
        #bot.send_message(chat_id, "{}".format(str(update)))
        return "ok"
    return "ok"

@app.route('/', methods=["GET"])
def getHelloWorld():
    url = 'http://vpn.texnomart.uz:8282/javoxir_ut_trendy/hs/deliverywebhook/e382d9ee722840d6a53e02d299331f4f'
    weburl = requests.get(url)
    return str(weburl.text)
