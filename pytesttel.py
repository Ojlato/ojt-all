import telebot
from telebot.storage import StateMemoryStorage
from telebot.handler_backends import State,StatesGroup
from telebot import custom_filters
#-------------------------------------------------------------------------
state_storage=StateMemoryStorage()
bott= "7789371758:AAEv9TgWBsUGhAMDvXhsKaWuqJhBTw1I1Uw"
bot= telebot.TeleBot(token=bott,state_storage=state_storage)
#-------------------------------------------------------------------------
class info(StatesGroup):
    name=State()
    lastname=State()
    age=State()
@bot.message_handler(commands=['start'])
def start(m):
        bot.send_message(m.chat.id,"نامت چیست؟")
        bot.set_state(m.from_user.id,info.name,m.chat.id)
@bot.message_handler(State=info.name)
def name(m):
    bot.send_message(m.chat.id,"نام خانوادگی شما؟")
    bot.set_state(m.from_user.id,info.lastname,m.chat.id)
    with bot.retrieve_data(m.from_user.id,m.chat.id) as data:
         data['name']=m.text
@bot.message_handler(State=info.lastname)
def lastname(m):
    bot.send_message(m.chat.id,"سن شما؟")
    bot.set_state(m.from_user.id,info.age,m.chat.id)
    with bot.retrieve_data(m.from_user.id,m.chat.id) as data:
         data['lastname']=m.text
@bot.message_handler(State=info.age)
def age(m):
    with bot.retrieve_data(m.from_user.id,m.chat.id) as data:
         bot.send_message(m.chat.id,f"اسم شما است: {data['name']} \n فامیلی شما هست: {['lastname']} \n سن شما: {m.text} هست")
    bot.delete_state(m.from_user.id,m.chat.id)
bot.add_custom_filter(custom_filters.StateFilter(bot))

print("LOADING...")
bot.polling(timeout=1024)
#-------------------------------------------------------------------------
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
#-------------------------------------------------------------------------
