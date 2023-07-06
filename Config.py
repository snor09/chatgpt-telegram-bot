import configparser
import os

class Config:
    def __init__(self):
        config_parser = configparser.ConfigParser()
        config_parser.read(os.path.join(os.getcwd(), "config.ini"))
        self.api_key = config_parser['openai']["API_KEY"]
        self.bot_key = config_parser['bot']['BOT_KEY']
        self.debug_bot_key = config_parser['bot']['DEBUG_BOT_KEY']
        self.allowed_users = config_parser.get('bot', 'ALLOWED_USERS').split(",")
        self.not_allowed_user_string = config_parser.get('string', 'NOT_ALLOWED_USER')
        self.not_valid_request = config_parser.get('string', 'NOT_VALID_REQUEST')

