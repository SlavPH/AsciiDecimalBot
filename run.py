#!/usr/bin/env python3

# Libraries
import telebot

# Add config file
config = open("config.py", "r").read()
exec(config)

# Define the bot
bot = telebot.TeleBot(Token)
print(Running)

# Command handler for /start command
@bot.message_handler(commands=["start"])
def start_command(message):
    global Start
    first_name = message.from_user.first_name
    bot.send_chat_action(message.chat.id, "typing")
    bot.reply_to(message, Start.format(first_name))

# Handle all messaages except /start command
@bot.message_handler(func=lambda message: True)
def all_messages(message):
    global Result

    if message.text.lower() == "space":
        try:
            bot.send_chat_action(message.chat.id, "typing")
            bot.reply_to(message, Result.format(message.text, "32"))
        except Exception as e:
            bot.send_chat_action(message.chat.id, "typing")
            bot.reply_to(message, e)

    # You can filter the input, Like if user send 'space' to bot
    # it will you an error because it's not a character"
    # elif message.text == "":

    # elif message.text == "":  

    # elif message.text == "":

    # elif message.text == "":

    # elif message.text == "":

    # elif message.text == "":

    # elif message.text == "":

    else:
        try:
            bot.send_chat_action(message.chat.id, "typing")
            bot.reply_to(message, Result.format(message.text, ord(message.text)))
        except Exception as e:
            bot.send_chat_action(message.chat.id, "typing")
            bot.reply_to(message, e)

# Stop the bot with "ctrl+z OR ctrl+c"
bot.infinity_polling()
# SlavPH
