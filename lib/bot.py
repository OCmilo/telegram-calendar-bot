import requests
import re

from calendarIntegration import authentication
from config import TELEGRAM_SEND_MESSAGE_URL


class TelegramBot: 
    def __init__(self):
        #initializing fields for parsing
        self.chat_id = None
        self.incoming_message_text = None
        self.first_name = None
        #creating Google Calendar API Service
        self.service = authentication()

    #Store received JSON in data attributes
    def parseData(self, data):
        response = data['message']

        self.chat_id = response['chat']['id']
        self.incoming_message_text = response['text'].lower()
        self.first_name = response['from']['first_name']

    def __sendMessage(self):
        res = requests.get(TELEGRAM_SEND_MESSAGE_URL.format(self.chat_id, self.outgoing_message_text)) 

        return res.status_code == 200

    def conditionalResponse(self):
        pass

    @staticmethod
    def init_webhook(url):
        init = requests.get(url)

        return init.status_code == 200

