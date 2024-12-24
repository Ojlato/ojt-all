import requests
import time
import telebot
bot= telebot.TeleBot("7789371758:AAHxCthTSEzvSCBH92pyp8E-DsW8o34oi9Y")
btm=telebot.types.InlinekeyboardButton("شروع",url="https://roocket.ir")
scn=telebot.types.InlinekeyboardMarkup(row_width=1)
scn.add(btm)
@bot.message_handler(commands=['help'])
def helpi(message):
    bot.reply_to(message,"what can i do?",reply_markup=key)
key=telebot.types.ReplykeyboardMarkup(resize_keyboard=True)
key.add("one","two")
@bot.message_handler(commands=['start'])
def send(message):
    bot.send_message(message.chat.id,"hehehe",reply_markup=scn)
@bot.message_handler()
def keyb(message):
    if message.text=="one":
        bot.send_message(message.chat.id,"ok")
    elif message.text=="two":
        bot.send_message(message.chat.id,"Yes")
bot.infinity_polling()