#Бот для групппы ВК
import vk_api
import time

say_hi = ('привет', 'привет!', 'привет.', 'hi', 'hello', 'прив', 'прива', 'ку', 'бу', 'хеллоу', 'здравствуйте', 'здрасти')
rewards = ('награда', 'награды', 'арена', 'га', 'время награды', 'время', 'время наград', 'когда награда')
members = ('состав', 'гильдия', 'согильдийцы' ,'члены' ,'mates', 'состав гильдии')
members_msg = 'https://vk.com/club156782249?w=page-156782249_53937664'
other_msg = 'Что ты имеешь ввиду?. Для просмотра времени награды введи НАГРАДА.'
rewards_msg = '''zorixx - 06:00
Царь Давид - 15:00
rexar - 19:00
Jonny - 20:00
Злой Ёжик - 20:00
BMW - 21:00
Lom - 22-00'''

token = "d0df0c1f1a3b14ad460fa449a6c87859537915e20c6e4d8dba7799f3f340f7876971c64b51aaaaf2d64b9"
vk = vk_api.VkApi(token=token)
vk._auth_token()

while True:
    try:
        messages = vk.method("messages.getConversations", {"offset": 0, "count": 20, "filter": "unanswered"})
        if messages["count"] >= 1:
            id = messages["items"][0]["last_message"]["from_id"]
            body = messages["items"][0]["last_message"]["text"]
            print('Message recieved!')
            #if body.lower() == "привет":
            if (body.lower() in say_hi):
                hi_msg = 'Привет, @' + str(id)
                vk.method("messages.send", {"peer_id": id, "message": hi_msg, 'random_id': 0})
                print('Message "Hi" to ', id, ' answered!')
            elif body.lower() in rewards:
                vk.method("messages.send", {"peer_id": id, "message": rewards_msg, 'random_id': 0})
                print('Message', rewards_msg, ' answered!')
            elif body.lower() in members:
                vk.method("messages.send", {"peer_id": id, "message": members_msg, 'random_id': 0})
                print('Message "', members_msg, ' answered!')
            else:
                vk.method("messages.send", {"peer_id": id, "message": other_msg, 'random_id': 0})
                print('Message', other_msg, 'answered!')
        else:
            print('Message didn\'t recieve!')
    except Exception as E:
        time.sleep(1)
