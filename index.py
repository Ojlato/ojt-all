import telebot
from telebot import types
#-------------------------------------------------------------------------
bott= "7789371758:AAEv9TgWBsUGhAMDvXhsKaWuqJhBTw1I1Uw"
bot= telebot.TeleBot(bott)
#-------------------------------------------------------------------------
item=[
    {"id":"1",
     "title":"مَنّ",
     "description":"کانال شخصی حاوی دلنوشته های امیدی که به فردای بهتر امید دارد اما گفته هایش چیز دیگری میگویند",
     "thumb":"https://i.imgur.com/D5Eani6.jpeg",
     "message":"کانال شخصی دلنوشته ها \n https://t.me/ojlato"},
    {"id":"2",
     "title":"Python with OJT",
     "description":"با من همراه باشید جهت ساخت ربات های مجازی",
     "thumb":"https://i.imgur.com/baVQQrB.png",
     "message":"Let`s Go! \n https://t.me/+MrhlgWbVf1k0MzI0"}
]
@bot.inline_handler(lambda query:len(query.query)==0)
def hand(query):
    results=[]
    for i in item:
        result=types.InlineQueryResultArticle(
            id=i["id"],
            title=i["title"],
            description=i["description"],
            input_message_content=types.InputTextMessageContent(
                message_text=i["message"]
            ),
            thumbnail_url=i["thumb"]
        )
        results.append(result)
    bot.answer_inline_query(query.id,results)
bot.polling()
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
