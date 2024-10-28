#"ربات تلگرام"

import requests
import time
import telebot

bot= telebot.TeleBot("7789371758:AAHxCthTSEzvSCBH92pyp8E-DsW8o34oi9Y")

butten=telebot.types.InlineKeyboardButton("شروع برنامه نویسی",url= "https://roocket.ir")
butten2=telebot.types.InlineKeyboardButton("ارتباط با ادمین",url= "https://t.me/omidjalalit")

secend=telebot.types.InlineKeyboardMarkup(row_width=1)
secend.add(butten,butten2)

@bot.message_handler(commands=['help'])
def helpi(message):
    bot.reply_to(message, "What Can I Do?!", reply_markup=key)

#@bot.message_handler(commands=['hello'])
#def send(message):
#    bot.send_message(message.chat.id,"Hi")

key=telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
key.add("One","Two","Three")

@bot.message_handler(commands=['start'])
def send(message):
    bot.send_message(message.chat.id,"درود.میخوای برنامه نویسی رو شروع کنی؟ پس همراه من باش",reply_markup=secend)


@bot.message_handler()
def keyb(message):
    if message.text=="One":
        bot.send_message(message.chat.id,"You Topped on One button")
    elif message.text=="Two":
        bot.send_message(message.chat.id,"You Topped on Two button")
bot.infinity_polling()




