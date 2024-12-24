import telebot
#import mysql.connector
#-------------------------------------------------------------------------
bott= "7789371758:AAEv9TgWBsUGhAMDvXhsKaWuqJhBTw1I1Uw"
bot= telebot.TeleBot(bott)
#cnx=mysql.connector.connect(
#    host='195.211.44.192',
#    database='چابکان',
#    user='rocky',
#    password='yh7WsVf1EXavQHm',
#    port=22
#)
#-------------------------------------------------------------------------
@bot.message_handler(commands=['link'])
def get(m):
   link=bot.create_chat_invite_link(m.chat.id)

#bot.polling()
#-------------------------------------------------------------------------
@bot.message_handler(content_types=['new_chat_members'])
def welcome(m):
    bot.reply_to(m,f"کاربر {m.from_user.first_name}\n به گروه خوش آمدید")
@bot.chat_join_request_handler(func=lambda r:True)
def gabool(r):
    bot.approve_chat_join_request(r.chat.id,r.from_user.id)
    bot.send_message(r.chat.id,f"کاربر {r.from_user.id}\n در گروه پذیرفته شد")
#-------------------------------------------------------------------------
@bot.message_handler(func=lambda m:m.text=="pin")
def pin(m):
    bot.pin_chat_message(m.chat.id,m.reply_to_message.id)
    bot .reply_to(m,"")
#-------------------------------------------------------------------------
@bot.message_handler(func=lambda m:m.text=="افزودن مدیر")
def pr(m):
    bot.promote_chat_member(
        m.chat.id,
        m.reply_to_message.json['from']['id'],
        can_change_info=False,
        can_delete_messages=True,
        can_edit_messages=True,
        can_invite_users=True,
        can_manage_chat=True,
        can_manage_topics=False,
        can_manage_video_chats=True,
        can_pin_messages=False,
        can_manage_voice_chats=True,
        can_post_messages=True,
        can_promote_members=False,
        can_restrict_members=True,
        can_delete_stories=False,
        can_edit_stories=False,
        can_post_stories=False
    )
    bot.send_message(m.chat.id,"کاربر مدیر گروه شد")
    #print(m.reply_to_message.json['from']['id'])
#-------------------------------------------------------------------------
@bot.message_handler(func=lambda m:m.text=="حذف مدیر")
def dele(m):
    bot.promote_chat_member(
        m.chat.id,
        m.reply_to_message.json['from']['id'],
        can_change_info=False,
        can_delete_messages=False,
        can_edit_messages=False,
        can_invite_users=False,
        can_manage_chat=False,
        can_manage_topics=False,
        can_manage_video_chats=False,
        can_pin_messages=False,
        can_manage_voice_chats=False,
        can_post_messages=False,
        can_promote_members=False,
        can_restrict_members=False,
        can_delete_stories=False,
        can_edit_stories=False,
        can_post_stories=False
    )
    bot.send_message(m.chat.id,"کاربر دیگر مدیر گروه نیست")
#-------------------------------------------------------------------------
@bot.message_handler(func=lambda m:m.text=="ban")
def ban(m):
    bot.ban_chat_member(m.chat.id,m.reply_to_message.from_user.id)
    bot.reply_to(m,f"کاربر {m.chat.id,m.reply_to_message.from_user.id} بن شد!")
#-------------------------------------------------------------------------
import datetime
@bot.message_handler(func=lambda m:m.text.startswith("ban"))
def ban2(m):
    duration=int(m.text.split()[-1])
    date=datetime.datetime.now()+datetime.timedelta(minutes=duration)
    until_date=datetime.datetime.timestamp(date)
    bot.ban_chat_member(
        m.chat.id,
        m.reply_to_message.from_user.id,
        until_date=until_date
    )
    bot.reply_to(m,f"کاربر {m.chat.id,m.reply_to_message.from_user.id} به مدت {duration} دقیقه بن شد!")
#-------------------------------------------------------------------------
@bot.message_handler(func=lambda m:m.text=="حذف بن")
def unban(m):
    bot.unban_chat_member(m.chat.id,m.reply_to_message.from_user.id)
    bot.reply_to(m,f"کاربر {m.chat.id,m.reply_to_message.from_user.id} حذف بن شد!")
#-------------------------------------------------------------------------
@bot.message_handler(func=lambda m:m.text=="سکوت")
def restrict(m):
    bot.restrict_chat_member(
        m.chat.id,
        m.reply_to_message.from_user.id,
        can_add_web_page_previews=False,
        can_change_info=False,
        can_invite_users=False,
        can_pin_messages=False,
        can_send_media_messages=False,
        can_send_messages=False,
        can_send_other_messages=False,
        can_send_polls=False
    )
    bot.reply_to(m,f"کاربر {m.chat.id,m.reply_to_message.from_user.id} در حالت سکوت قرار گرفت")
#-------------------------------------------------------------------------
import datetime
@bot.message_handler(func=lambda m:m.text.startswith("سکوت"))
def mute(m):
    duration=int(m.text.split()[-1])
    date=datetime.datetime.now()+datetime.timedelta(minutes=duration)
    until_date=datetime.datetime.timestamp(date)
    bot.restrict_chat_member(
        m.chat.id,
        m.reply_to_message.from_user.id,
        until_date=until_date,
        can_add_web_page_previews=False,
        can_change_info=False,
        can_invite_users=False,
        can_pin_messages=False,
        can_send_media_messages=False,
        can_send_messages=False,
        can_send_other_messages=False,
        can_send_polls=False
    )
    bot.reply_to(m,f"کاربر {m.chat.id,m.reply_to_message.from_user.id} به مدت {duration} دقیقه در حالت سکوت قرار گرفت")
#-------------------------------------------------------------------------
@bot.message_handler(func=lambda m:m.text=="حذف سکوت")
def derestrict(m):
    bot.restrict_chat_member(
        m.chat.id,
        m.reply_to_message.from_user.id,
        can_add_web_page_previews=True,
        can_change_info=True,
        can_invite_users=True,
        can_pin_messages=True,
        can_send_media_messages=True,
        can_send_messages=True,
        can_send_other_messages=True,
        can_send_polls=True
    )
    bot.reply_to(m,f"کاربر {m.chat.id,m.reply_to_message.from_user.id} از لیست سکوت خارج شد")

bot.polling(timeout=120)