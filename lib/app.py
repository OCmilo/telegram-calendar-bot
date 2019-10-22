import subprocess, shlex
from flask import Flask, request, jsonify


from config import TELEGRAM_INIT_WEBHOOK_URL as webhook, WEBHOOK_HOSTNAME as hostname
from bot import TelegramBot

app = Flask(__name__)

if not TelegramBot.init_webhook(webhook):
    try:
        raise RuntimeError
    finally:
        print('Webhook not initialized properly')



@app.route('/webhook', methods=['POST'])
def index():




if __name__ == '__main__':
    app.run(port=5000)




