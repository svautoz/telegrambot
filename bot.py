

# Вы когда-нибудь играли в игру "Крестики-нолики"? Попробуйте создать её.

# Done! Congratulations on your new bot. You will find it at t.me/sidorenkovladimir_bot. You can now add a description, about section and profile picture for your bot, see /help for a list of commands. By the way, when you've finished creating your cool bot, ping our Bot Support if you want a better username for it. Just make sure the bot is fully operational before you do this.

# Use this token to access the HTTP API:
# 5155648528:AAEl6YLUXWSKkzmkitOJGS98y0HDxSRXkkY
# Keep your token secure and store it safely, it can be used by anyone to control your bot.

# For a description of the Bot API, see this page: https://core.telegram.org/bots/api

# ------------------------------------------------------------------------------------------------------------------------

from cgitb import text
import telebot
import library
import random
bot = telebot.TeleBot('5155648528:AAEl6YLUXWSKkzmkitOJGS98y0HDxSRXkkY')

# Напишите программу, удаляющую из текста все слова содержащие "абв".
# str = ''
# sub_str = ''

# @bot.message_handler(commands=['help'])
# def send_welcome(message):
#     bot.reply_to(message, "Бот занимается удалением слов в предложении, которые включают заданую подстроку.")

# @bot.message_handler(commands=['start'])
# def send_welcome(message):
#     bot.reply_to(message, "Введите предложение")
#     bot.register_next_step_handler(message, get_str)

# def get_str(message):
#     global str
#     str = message.text
#     bot.send_message(message.from_user.id, 'Введите подстроку')
#     bot.register_next_step_handler(message, get_sub_str)

# def get_sub_str(message):
#     global sub_str
#     global str
#     sub_str = message.text
#     str = library.clean_sub_str(str, sub_str)
#     bot.send_message(message.from_user.id, f'Результат удаления {str}')

# ------------------------------------------------------------------------------------------------------------------------


# sweets = 121
# max_sweets = 28
# turn = 1
# sweet_count = 0
# def get_hint_user(sweets, max_sweets):
#     if max_sweets >= sweets:
#         return sweets
#     number = sweets // max_sweets
#     y = number * max_sweets + 1
#     return sweets - y

# def get_hint_comp(sweets, max_sweets):
#     if max_sweets >= sweets:
#         return sweets
#     number = sweets // max_sweets    
#     y = number * max_sweets + 1
#     if y >= sweets:
#         y = (number - 1) * max_sweets + 1
#     return (random.randint(1, sweets if max_sweets > sweets else max_sweets) 
#     if sweets - y == 0 else sweets - y)

# def get_sweets(turn, message):
#     bot.reply_to(message, f'Конфет осталось {sweets}')
#     if turn == 1:
#         bot.reply_to(message, f'Заберите {get_hint_user(sweets, max_sweets)} конфет')
#         bot.reply_to(message, f'Сколько конфет забрать игроку?')
#         bot.register_next_step_handler(message, set_sweet_count)
#     else:
#         number = get_hint_comp(sweets, max_sweets)
#         bot.reply_to(message, f'Бот ввел число: {number}')
#         message.text = number
#         set_sweet_count(message)
        
            

# def set_sweet_count(message):
#     global sweet_count
#     global sweets
#     global turn
#     global bot
#     sweet_count = int(message.text)
#     if sweet_count >= max_sweets:
#             sweet_count = max_sweets
#     sweets -= sweet_count    
#     if sweets <= 0:
#         turn = 'Бот' if turn == 2 else 'Человек'
#         bot.reply_to(message, f'Победил игрок {turn}')
#         return    
#     turn = 2 if turn == 1 else 1
#     get_sweets(turn, message)


# @bot.message_handler(commands=['help'])
# def send_welcome(message):
#     bot.reply_to(message, "Игра в конфетки. Кто взял последние тот выиграл. За один раз можно взять 28 конфет")

# @bot.message_handler(commands=['start'])
# def send_welcome(message):
#     global turn
#     turn = 1
#     global sweets
#     sweets = 121
#     global max_sweets
#     max_sweets = 28
#     global sweet_count
#     sweet_count = 0  
#     get_sweets(turn, message)


# ------------------------------------------------------------------------------------------------------------------------


bot.infinity_polling()



# @bot.message_handler(content_types=['text'])
# def get_text_messages(message):
#     if message.text == "Привет":
#         bot.send_message(message.from_user.id, "Привет, чем я могу тебе помочь?")
#     elif message.text == "/help":
#         bot.send_message(message.from_user.id, "Напиши привет")
#     else:
#         bot.send_message(message.from_user.id, "Я тебя не понимаю. Напиши /help.")

# ------------------------------------------------------------------------------------------------------------------------

# name = ''
# surname = ''
# age = 0
# @bot.message_handler(content_types=['text'])
# def start(message):
#     if message.text == '/reg':
#         bot.send_message(message.from_user.id, "Как тебя зовут?")
#         bot.register_next_step_handler(message, get_name) #следующий шаг – функция get_name
#     else:
#         bot.send_message(message.from_user.id, 'Напиши /reg')

# def get_name(message):
#     global name
#     name = message.text
#     bot.send_message(message.from_user.id, 'Какая у тебя фамилия?')
#     bot.register_next_step_handler(message, get_surname)

# def get_surname(message):
#     global surname
#     surname = message.text
#     bot.send_message(message.from_user.id,'Сколько тебе лет?')
#     bot.register_next_step_handler(message, get_age)

# def get_age(message):
#     global age
#     while age == 0: #проверяем что возраст изменился
#         try:
#              age = int(message.text) #проверяем, что возраст введен корректно
#         except Exception:
#              bot.send_message(message.from_user.id, 'Цифрами, пожалуйста')
#         keyboard = telebot.types.InlineKeyboardMarkup(); #наша клавиатура
#         key_yes = telebot.types.InlineKeyboardButton(text='Да', callback_data='yes'); #кнопка «Да»
#         keyboard.add(key_yes); #добавляем кнопку в клавиатуру
#         key_no= telebot.types.InlineKeyboardButton(text='Нет', callback_data='no')
#         keyboard.add(key_no)
#         question = 'Тебе '+str(age)+' лет, тебя зовут '+name+' '+surname+'?'
#         bot.send_message(message.from_user.id, text=question, reply_markup=keyboard)

# @bot.callback_query_handler(func=lambda call: True)
# def callback_worker(call):
#     if call.data == "yes":
#         bot.send_message(call.message.chat.id, 'Запомню : )')
#     elif call.data == "no":
#         pass

# bot.polling(none_stop=True, interval=1)

# ------------------------------------------------------------------------------------------------------------------------

# This is a simple echo bot using the decorator mechanism.
# It echoes any incoming text messages.

# import telebot

# API_TOKEN = '<api_token>'

# bot = telebot.TeleBot(API_TOKEN)


# # Handle '/start' and '/help'
# @bot.message_handler(commands=['help', 'start'])
# def send_welcome(message):
#     bot.reply_to(message, """\
# Hi there, I am EchoBot.
# I am here to echo your kind words back to you. Just say anything nice and I'll say the exact same thing to you!\
# """)


# # Handle all other messages with content_type 'text' (content_types defaults to ['text'])
# @bot.message_handler(func=lambda message: True)
# def echo_message(message):
#     bot.reply_to(message, message.text)


# bot.infinity_polling()

# ------------------------------------------------------------------------------------------------------------------------

# from telegram import Update
# from telegram.ext import Updater, CommandHandler, CallbackContext


# def hello(update: Update, context: CallbackContext) -> None:
#     update.message.reply_text(f'Hello {update.effective_user.first_name}')


# updater = Updater('YOUR TOKEN HERE')

# updater.dispatcher.add_handler(CommandHandler('hello', hello))

# updater.start_polling()
# updater.idle()
