from telethon import TelegramClient, events, sync
from db_helper import DBHelper

db = DBHelper()
api_id = 427808
api_hash = '7399ee2f5b9ed4556ed519a921a9ed5f'
client = TelegramClient('session_name', api_id, api_hash)
client.start()
limit = 100
message = " invite link here "
# print(client.get_me().stringify())

total_users = db.getusertocontact(limit)
for users in total_users:
    for user in users:
        client.send_message(user, message)
        db.updateuser_to_contacted(user)
