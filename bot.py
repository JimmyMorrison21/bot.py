import os

import requests
import telebot
from translator import message_taker as mt


token = '*************************'


bot = telebot.TeleBot(token=token,parse_mode=None)


@bot.message_handler(commands=['Полетели'])
def send_welcome(message):
	bot.reply_to(message, "Приветствую тебя")


@bot.message_handler(commands=['Помоги'])
def send_help_instr(message):
	bot.reply_to(message, "Нужна моя помощь?")


@bot.message_handler(content_types=['text'])
def echo_all(message):
	bot.send_message(message.chat.id, message.text)


@bot.message_handler(content_types=['photo', 'text'])
def send_text(message):
    print
    'message.photo =', message.photo
    fileID = message.photo[-1].file_id
    print
    'fileID =', fileID
    file_info = bot.get_file(fileID)
    print
    'file.file_path =', file_info.file_path
    downloaded_file = bot.download_file(file_info.file_path)
    with open("image.jpg", 'wb') as new_file:
        new_file.write(downloaded_file)
    print(message)
    bot.send_message(message.chat.id, mt('image.jpg', lang=message.caption))
    os.remove('image.jpg')


@bot.message_handler(content_types=['voice'])
def try_to_regcognize(message):
    file_info = bot.get_file(message.voice.file_id)
    file = requests.get('https://api.telegram.org/file/bot{0}/{1}'.format(token, file_info.file_path))

    with open('voice.ogg', 'wb') as f:
        f.write(file.content)


if __name__ == '__main__':
    bot.polling(none_stop=True, interval=0)