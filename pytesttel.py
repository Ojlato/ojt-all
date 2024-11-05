import telebot
#-------------------------------------------------------------------------
bott= "7789371758:AAEv9TgWBsUGhAMDvXhsKaWuqJhBTw1I1Uw"
bot= telebot.TeleBot(bott)
#-------------------------------------------------------------------------
import time
from telebot import types
fp=open("C:/Users/POURALI PC CENTER/Downloads/R (1).jpg",'rb')
sp=open("C:/Users/POURALI PC CENTER/Downloads/1da20f66-6c98-4079-8536-147c43d3b006.jpg",'rb')
key=types.InlineKeyboardMarkup()
btn=types.InlineKeyboardButton("دکمه 1",callback_data="btn1")
key.add(btn)
#-------------------------------------------------------------------------
@bot.message_handler(commands=['start'])
def welcome(message):
    bot.send_chat_action(message.chat.id,action='upload_photo')
    m= bot.send_photo(chat_id=message.chat.id,photo=sp,reply_markup=key)
    global Mk
    Mk=m.message_id
    time.sleep(3)
key2=types.InlineKeyboardMarkup()
btn2=types.InlineKeyboardButton("دکمه جدید",callback_data="btn2")
key2.add(btn2)
@bot.callback_query_handler(func=lambda call:call.data=="btn1")
def change(call):
    bot.edit_message_reply_markup(chat_id=call.message.chat.id,message_id=Mk,reply_markup=key2)
    time.sleep(3)
    bot.delete_message(chat_id= call.message.chat.id,message_id=Mk)
    bot.send_message(chat_id=call.message.chat.id,text="پیام حذف شد")
#-------------------------------------------------------------------------