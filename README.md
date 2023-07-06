# Telegram ChatGPT Bot

This is a Python project that uses the OpenAI library to interact with ChatGPT through a Telegram bot. 

## Requirements

To run this project, you will need to install the following libraries:
- python 3.7 or newer
- python-telegram-bot
- openai
- all the requirements included in requirements.txt (you can install this by using pip install -r requirements.txt)

You will also need to create a Telegram bot (Follow this guide: https://core.telegram.org/bots#how-do-i-create-a-bot) and get an OpenAI API key (create an account on openai and go https://platform.openai.com/account/api-keys to get api key).
Either the keys are essential.

## Usage

To use this bot, first clone the repository:

```
git clone https://github.com/snor09/chatgpt-assistant.git
```

Then, create a file named `config.ini` in the root directory of the project and add the following configuration variables:
```
[openai]
API_KEY = <insert-your-openai-key>
[bot]
BOT_KEY = <insert-your-telegram-bot-key> # Follow these for getting it https://core.telegram.org/bots#creating-a-new-bot
DEBUG_BOT_KEY = <insert-your-debug-telegram-bot-key> # Optional if you are doing debug whilst your main bot is running
ALLOWED_USERS= <insert-list-of-allowed-users-ids> # You can insert a list of ids to limitate use of bot like this: 1111111,22222222,3333333,44444444
[string]
NOT_ALLOWED_USER = <insert-default-string-for-not-allowed-users>
NOT_VALID_REQUEST = <insert-default-string-for-invalid-requests>
```
Next, navigate to the project directory and start the bot:

```
cd chatgpt-assistant
python3 main.py
```

You can now interact with your Telegram bot by sending messages and receiving responses from ChatGPT.

## Contributing

If you find any bugs or have suggestions for improvement, please feel free to submit an issue or create a pull request.
