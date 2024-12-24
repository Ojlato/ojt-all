from telebot import TeleBot
from telebot.util import update_types
#-------------------------------------------------------------------------
bot= TeleBot("7789371758:AAEv9TgWBsUGhAMDvXhsKaWuqJhBTwlIlUw")
#-------------------------------------------------------------------------
t="""<blockquote>It's blockquote</blockquote>
<pre>It's code</pre>
<pre><code class="language-python">It's CODE WITH LANG</code></pre>"""
@bot.message_handler(commands=['start'])
def start(m):
    bot.send_message(chat_id=m.chat.id,text=t,parse_mode="HTML")

print("LOADING...")
bot.polling(timeout=1024,allowed_updates=update_types)
#-------------------------------------------------------------------------

#-------------------------------------------------------------------------
##@bot.message_handler(commands=['start'])
##def start(m):
##    bot.send_chat_action(m.chat.id,action='typing')
##    text="<b>این متن بولد است</b>"
##    text1="<i>این متن کج است</i>"
##    text2="<code>این متن دارای قابلیت کپی برداری است</code>"
##    text3="<ins>این متن زیرخط دار است</ins>"
##    text4="<s>این متن اشتباه است</s>"
##    text5="|| این متن مخفی است ||"
##    text6="[این متن لینک است](https://t.me/omidjalalit)"
##    bot.send_message(m.chat.id,text,parse_mode="HTML")
##    bot.send_message(m.chat.id,text1,parse_mode="HTML")
##    bot.send_message(m.chat.id,text2,parse_mode="HTML")
##    bot.send_message(m.chat.id,text3,parse_mode="HTML")
##    bot.send_message(m.chat.id,text4,parse_mode="HTML")
##    bot.send_message(m.chat.id,text5,parse_mode="MarkdownV2")
##    bot.send_message(m.chat.id,text6,parse_mode="MarkdownV2",disable_web_page_preview=True)
##
##bot.polling()
