api_id = 1992385
api_hash = "a470b85e27ed03b83571c42c499da412"
uri = "mongodb+srv://scrapuserbot:1976abcd?@scrap.8mcz1vh.mongodb.net/?retryWrites=true&w=majority"
from telethon import *
from telethon.sync import *
T = TelegramClient('SESSION',api_id,api_hash)



@T.on(events.NewMessage(outgoing=True,pattern='\.kidnap'))
async def user_id_getter(event):
    chat = await event.get_chat()
    await T.send_message(chat,f"ok")

T.start()
T.run_until_disconnected()