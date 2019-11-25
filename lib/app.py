import subprocess
import shlex
from flask import Flask, request, jsonify


from config import TELEGRAM_INIT_WEBHOOK_URL as webhook, WEBHOOK_HOSTNAME as hostname
from bot import TelegramBot

app = Flask(__name__)

if not TelegramBot.init_webhook(webhook):
    try:
        raise RuntimeError
    finally:
        print("Webhook not initialized properly")


@app.route("/webhook", methods=["POST"])
def index():
    res = request.get_json()
    robot = TelegramBot()
    robot.parseData(res)
    isSuccessful = robot.conditionalResponse()
    return jsonify(success=isSuccessful)


def webhookProccess(hostname):
    shCommand = "ssh -o ServerAliveInterval=60 -R {}:80:localhost:8888 serveo.net".format(
        hostname
    )
    args = shlex.split(shCommand)
    subprocess.Popen(args)


if __name__ == "__main__":
    webhookProccess(hostname)
    app.run(port=5000)
