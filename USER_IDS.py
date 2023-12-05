from telethon import *
from telethon.sync import *
api_id = 1992385
api_hash = 'a470b85e27ed03b83571c42c499da412'
with TelegramClient('session', api_id, api_hash) as client:
    participants = client.get_participants(-1001626684605)
    user_ids = [participant.id for participant in participants]
    all_ids = user_ids
    print(all_ids)