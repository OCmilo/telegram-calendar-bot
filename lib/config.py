TOKEN = "838321161:AAGu3-keIMZpWjiOaYEbZmta0TgcD4sh41s"
WEBHOOK_HOSTNAME = "fateor"

TELEGRAM_URL = "https://api.telegram.org/bot{}".format(TOKEN)
WEBHOOK_URL = "https://{}.serveo.net".format(WEBHOOK_HOSTNAME)

WEBHOOK_ENDPOINT = "{}/webhook".format(WEBHOOK_URL)
TELEGRAM_INIT_WEBHOOK_URL = "{}/setWebhook?url={}".format(
    TELEGRAM_URL, WEBHOOK_ENDPOINT
)

