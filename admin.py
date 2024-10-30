import telebot
#-------------------------------------------------------------------------
bott= "7789371758:AAHxCthTSEzvSCBH92pyp8E-DsW8o34oi9Y"
bot= telebot.TeleBot(bott)
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
@bot.message_handler(func=lambda m:m.text=="حذف بن")
def unban(m):
    bot.unban_chat_member(m.chat.id,m.reply_to_message.from_user.id)
    bot.reply_to(m,f"کاربر {m.chat.id,m.reply_to_message.from_user.id} حذف بن شد!")


bot.polling(timeout=120)