#Telegram configurations
TOKEN = '838321161:AAGu3-keIMZpWjiOaYEbZmta0TgcD4sh41s'
TELEGRAM_URL = 'https://api.telegram.org/bot{}'.format(TOKEN)

WEBHOOK_HOSTNAME = 'fateor'
WEBHOOK_URL = 'https://fateor.serveo.net'

WEBHOOK_ENDPOINT = '{}/webhook'.format(WEBHOOK_URL)
TELEGRAM_INIT_WEBHOOK_URL = '{}/setWebhook?url={}'.format(TELEGRAM_URL, WEBHOOK_ENDPOINT)
TELEGRAM_SEND_MESSAGE_URL = TELEGRAM_URL + '/sendMessage?chat_id={}&text={}'