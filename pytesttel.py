import telebot
#-------------------------------------------------------------------------
bott= "7789371758:AAHxCthTSEzvSCBH92pyp8E-DsW8o34oi9Y"
bot= telebot.TeleBot(bott)
#-------------------------------------------------------------------------
@bot.message_handler(content_types=['new_chat_members'])
def welcome(m):
    bot.reply_to(m,f"کاربر{m.from_user.id}\n به گروه خوش آمدید")
@bot.chat_join_request_handler(func=lambda r:True)
def gabool(r):
    bot.approve_chat_join_request(r.chat.id,r.from_user.id)
    bot.send_message(r.chat.id,f"کاربر {r.from_user.first_name}\n در گروه پذیرفته شد")

bot.polling(timeout=120)
##import time
##from telebot import types
##fp=open("C:/Users/POURALI PC CENTER/Downloads/R (1).jpg",'rb')
##sp=open("C:/Users/POURALI PC CENTER/Downloads/1da20f66-6c98-4079-8536-147c43d3b006.jpg",'rb')
##key=types.InlineKeyboardMarkup()
##btn=types.InlineKeyboardButton("دکمه 1",callback_data="btn1")
##key.add(btn)
###-------------------------------------------------------------------------
##@bot.message_handler(commands=['start'])
##def welcome(message):
##    bot.send_chat_action(message.chat.id,action='upload_photo')
##    m= bot.send_photo(chat_id=message.chat.id,photo=sp,reply_markup=key)
##    global Mk
##    Mk=m.message_id
##    time.sleep(3)
##key2=types.InlineKeyboardMarkup()
##btn2=types.InlineKeyboardButton("دکمه جدید",callback_data="btn2")
##key2.add(btn2)
##@bot.callback_query_handler(func=lambda call:call.data=="btn1")
##def change(call):
##    bot.edit_message_reply_markup(chat_id=call.message.chat.id,message_id=Mk,reply_markup=key2)
##    time.sleep(3)
##    bot.delete_message(chat_id= call.message.chat.id,message_id=Mk)
##    bot.send_message(chat_id=call.message.chat.id,text="پیام حذف شد")

