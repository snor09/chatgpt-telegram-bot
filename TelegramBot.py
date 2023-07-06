import telebot

class TelegramBot:
    def __init__(self, token, allowed_users):
        self.token = token
        self.allowed_users = allowed_users
        self.bot = telebot.TeleBot(token)

    def initialize(self):
        print("Initializing telebot")
        print("Allowed users:")
        for user in self.allowed_users:
            print(user)
        print(f"token {self.token}")

    def sendMessage(self, chat_id, text):
        self.bot.send_message(chat_id, text)

    def replyMessage(self, chat_id, text):
        self.bot.reply_to(chat_id, text)