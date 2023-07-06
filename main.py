from Config import Config
from GptRequest import GptRequest
from TelegramBot import TelegramBot
import rx
from rx import operators as ops
from rx.scheduler import threadpoolscheduler
from Utils import saveLog

def main():
    debug = False
    # Initialize the config
    config = Config()
    # Initialize openai class
    gpt_request = GptRequest()
    gpt_request.initialize(config.api_key)
    # Initialize bot class
    if debug:
        bot_key = config.debug_bot_key
    else:
        bot_key = config.bot_key

    telegram_bot = TelegramBot(bot_key, config.allowed_users)
    telegram_bot.initialize()
    
    # Create a scheduler for the operations
    pool_scheduler = threadpoolscheduler.ThreadPoolScheduler(10)

    # Bot test command    
    @telegram_bot.bot.message_handler(commands=['test'])
    def test2(query):
        print(query)
        saveLog(query)
        if str(query.from_user.id) in config.allowed_users:
            telegram_bot.bot.reply_to(query, f"{query.from_user.id} {query.text}")
        else:
            telegram_bot.bot.send_message(query.chat.id, config.not_allowed_user_string)

    # Bot ChatGpt query command
    @telegram_bot.bot.message_handler(commands=['askGpt', 'askgpt'])
    def ask_gpt(query):
        print(query)
        if query.text[8:] == "":
            telegram_bot.replyMessage(query, config.not_valid_request)
        else:
            saveLog(query)

            if str(query.from_user.id) in config.allowed_users:
                final_query = query.text[8:]
                rx.concat(gpt_request.gptRequest(final_query)).pipe(
                    ops.subscribe_on(pool_scheduler),
                    ops.map(lambda s: s)
                    ).subscribe(
                        on_next=lambda response: telegram_bot.replyMessage(query, response),
                        on_error= print("error")
                    )
            else:
                telegram_bot.replyMessage(query, config.not_allowed_user_string)

    # Set the polling for the bot
    try:
        telegram_bot.bot.infinity_polling()
    except:
        print("Bot polling error")

if __name__ == "__main__":
    main()

