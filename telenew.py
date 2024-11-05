import telebot # type: ignore
##import requests # type: ignore

bot= telebot.TeleBot("7789371758:AAEv9TgWBsUGhAMDvXhsKaWuqJhBTw1I1Uw")

fi=telebot.types.InlineKeyboardButton("button 1", url="https://roocket.ir")
tw=telebot.types.InlineKeyboardButton("button 2", callback_data="Hi")
m=telebot.types.InlineKeyboardMarkup(row_width=1)
m.add(fi,tw)

@bot.callback_query_handler(func=lambda call:True)
def call(call):
    if call.data=="Hi":
    #bot.reply_to(call.message, "clicked!")
        bot.answer_callback_query(call.id,"Click!",show_alert=True)

@bot.message_handler(commands=['start'])
def send(message):
    bot.send_message(message.chat.id,"Hi",reply_markup=m)

key=telebot.types.ReplyKeyboardMarkup(resize_keyboard=True,row_width=1)
key.add("ثبت اطلاعات","one","two")

@bot.message_handler(commands=['help'])
def helpi(message):
    bot.reply_to(message,"why can i do",reply_markup=key)

bot.message_handler()
def kay(message):
    if message.text=="one":
        bot.send_message(message.chat.id,"HAHAHA")
    elif message.text=="two":
        bot.send_message(message.chat.id,"AHAHAH")

@bot.message_handler(func=lambda m:True)
def info(message):
    if message.text=="ثبت اطلاعات":
        msg=bot.send_message(message.chat.id,"نامت چیست؟")
        bot.register_next_step_handler(msg,name)
def name(message):
    global nm
    nm=message.text
    msg=bot.send_message(message.chat.id,"نام خانوادگی شما؟")
    bot.register_next_step_handler(msg,fname)
def fname(message):
    global fn
    fn=message.text
    msg=bot.send_message(message.chat.id,"شماره تلفن")
    bot.register_next_step_handler(msg,num)
def num(message):
    a=message.text
    bot.send_message(message.chat.id,"نام:{nm} \n نام خانوادگی:{fn} \n تلفن:{a}")
    
@bot.message_handler(commands=['end'])
def cancel(message):
    bot.send_message(message.chat.id,"این پیام یک دستور است",reply_markup=key)
@bot.message_handler(func=lambda m:m.text=="one")
def button(message):
    bot.send_message(message.chat.id,"HAHAHA")
@bot.message_handler(func=lambda m:m.text=="two")
def buttom(message):
    bot.send_message(message.chat.id,"AHAHAH")

@bot.message_handler(regexp=r'\d+')
def adad(message):
    bot.send_message(message.chat.id,"این پیام حاوی عدده")

@bot.message_handler(chat_types=['privete'])
def pv(message):
    bot.send_message(message.chat.id,"این پیام و کد در پی وی کار میکند")

@bot.message_handler(chat_types=['supergroup'])
def gr(message):
    bot.send_message(message.chat.id,"این پیام فقط از گروه دریافت میشود")

@bot.message_handler(content_types=['photo'])
def aks(message):
    bot.send_message(message.chat.id,"این پیام دارای تصویر میباشد")

bot.infinity_polling()