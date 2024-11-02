import telebot
import time
from telebot import types
#-------------------------------------------------------------------------
bott= "7789371758:AAHxCthTSEzvSCBH92pyp8E-DsW8o34oi9Y"
bot= telebot.TeleBot(bott)
#-------------------------------------------------------------------------
fp=open("C:/Users/POURALI PC CENTER/Downloads/R (1).jpg",'rb')
sp=open("C:/Users/POURALI PC CENTER/Downloads/1da20f66-6c98-4079-8536-147c43d3b006.jpg",'rb')
media=[]
#-------------------------------------------------------------------------
@bot.message_handler(commands=['start'])
def welcome(message):
    bot.send_chat_action(message.chat.id,action='upload_photo')
#-------------------------------------------------------------------------
    m= bot.send_photo(chat_id=message.chat.id,photo=fp,caption="عکس اولیه")
    time.sleep(3)
    bot.edit_message_media(chat_id=message.chat.id,message_id=m.message_id,media=types.InputMediaPhoto(sp,caption="عکس تعویض شد"))
    bot.edit_message_caption(chat_id=message.chat.id,message_id=m.message_id,caption="متن ادیت شد")
#-------------------------------------------------------------------------
    m=bot.send_message(message.chat.id,"این تست است")
    bot.edit_message_text(chat_id=message.chat.id,message_id=m.message_id,text="متن ادیت شد")
#-------------------------------------------------------------------------
    bot.send_video(message.chat.id,open("D:/FFOutput/Shahrzad.S02E14.480p.Film2Movie_Asia 00_00_00-00_03_39.mp4",'rb'))
#-------------------------------------------------------------------------
    bot.send_document(message.chat.id,open("C:/Users/POURALI PC CENTER/OneDrive/Documents/khayati.pdf",'r'))
#-------------------------------------------------------------------------
    bot.send_audio(message.chat.id,open("C:/Users/POURALI PC CENTER/Downloads/Telegram Desktop/Shahin Najafi - ADHD (320).mp3",'rb'))
#-------------------------------------------------------------------------
    p1=types.InputMediaPhoto(open("C:/Users/POURALI PC CENTER/Downloads/1da20f66-6c98-4079-8536-147c43d3b006.jpg",'rb'))
    p2=types.InputMediaPhoto(open("C:/Users/POURALI PC CENTER/Downloads/Top-programmer-wallpapers-768x407.jpg",'rb'))
    p3=types.InputMediaPhoto(open("C:/Users/POURALI PC CENTER/Downloads/New folder/er.jpeg" , 'rb'))
    media.append(p1)
    media.append(p2)
    media.append(p3)
    bot.send_media_group(message.chat.id,media=media)
#-------------------------------------------------------------------------
def get(m):
    markup=types.ReplyKeyboardMarkup(resize_keyboard=True,row_width=1)
    but=types.KeyboardButton(text='تلفن',request_contact=True)
    markup.add(but)
    bot.send_message(m.chat.id,"شماره خود را تایید کنید",reply_markup=markup)
#-------------------------------------------------------------------------
@bot.message_handler(content_types=['photo','text','audio','video','docuoment','location','contact'])
def contact(m):
    print(m.contact)
#-------------------------------------------------------------------------
@bot.channel_post_handler(content_types=['photo','text','audio','video','docuoment','location','contact'])
def forward(m):
    o= -1002263295830
    o1=-1002488560509
    bot.forward_message(
        chat_id=o1,
        from_chat_id=o,
        message_id=m.message_id,
        protect_content=True
    )
    bot.copy_message(
        chat_id=o1,
        from_chat_id=o,
        message_id=m.message_id
    )

bot.polling()