from instagrapi import Client
from time import sleep
#-----------------------------------------------------------------------
cl=Client(delay_range=[2,5])
cl.load_settings("session.json")
cl.login(username="ojlato",password="39631244o")
#-----------------------------------------------------------------------
user=cl.user_info_by_username("omjalt")
cl.direct_send(text="سلام این پیام بصورت اتوماتیک و توسط پایتون ارسال شده است",
            user_ids=[user.pk])
#-----------------------------------------------------------------------
#selected_filter=(flagged,unread)
th=cl.direct_threads(amount=3)
for i in th:
    sleep(5)
    cl.direct_answer(i.id,text="❤")
#-----------------------------------------------------------------------
# media=cl.media_pk_from_url(
#     "https://www.instagram.com/p/C8UWHR0K9gzEH059hQWPKt-Ny_dH8x8lHepcMo0/?next=https%3A%2F%2Fwww.instagram.com%2Faccounts%2Fpassword%2Freset%2F"
# )
#--------------------------------------------
# mediai=cl.media_id(media)
# c=cl.media_comments(mediai,amount=5)
# for i in c:
#     print(i)
#     cl.media_comment(mediai,text="",replied_to_comment_id=int(i.pk))
#--------------------------------------------
# sleep(5)
# cl.media_like(mediai)
# sleep(10)
# cl.media_comment(mediai,text="Auto Comment")
# cl.media_save(mediai)
#--------------------------------------------
# print(media)
# mediai=cl.media_info(media)
# print(mediai.like_count)
# print(mediai.comment_count)
#-----------------------------------------------------------------------
# from config import USERNAME,PASSWORD
# userid=cl.user_id_from_username("omidjalalit")
# print(userid)
#-----------------------------------------------------------------------
# followers=cl.user_info(userid)
# print(followers.follower_count)
# print(followers.following_count)
#-----------------------------------------------------------------------

