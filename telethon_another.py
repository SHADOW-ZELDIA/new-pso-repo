api_id = 1992385
api_hash = "a470b85e27ed03b83571c42c499da412"
uri = "mongodb+srv://scrapuserbot:1976abcd?@scrap.8mcz1vh.mongodb.net/?retryWrites=true&w=majority"
from telethon import *
from telethon.sync import *
import USER_IDS , pymongo , time
from pymongo.mongo_client import MongoClient
from bson.objectid import ObjectId
from pymongo.server_api import ServerApi
mongo_client = MongoClient(uri, server_api=ServerApi('1'))
db = mongo_client['scrapper-db']
T = TelegramClient('SESSION',api_id,api_hash)
all_ids=USER_IDS.all_ids
print("working")

@T.on(events.NewMessage(outgoing=True,pattern='\.kidnap'))
async def user_id_getter(event):
    chat = await event.get_chat()
    user_ids=db.get_collection("user_ids")
    obj_id=user_ids.find_one()['_id']
    user_id=user_ids.find_one()['user_ids']
    gays=0
    already_in=0
    for i in range(len(all_ids)):
        if all_ids[i] in user_id:
            already_in+=1
            print(f"already in {i}") 
        else:
            for_check=0
            try:
                await T.send_message(all_ids[i], "umm can you try this bot\n@pso_sobot\nit's not like i saying you have to but you can try it once\nit's a game bot")
                user_id.append(all_ids[i])
            except:
                for_check+=1
                gays+=1
                print(f"failed {i}")
            if for_check!=1:
                time.sleep(60)
    await T.send_message(chat,f"Kidnapping done\n\nTotal Kidnapped User : {len(all_ids)-gays-already_in}\n\nTotal Gays : {gays}\n\nALREADY KIDNAPPED USER : {already_in}")
    user_ids.update_one({"_id":ObjectId(obj_id)},{"$set":{'user_ids':user_id}})

T.start()
T.run_until_disconnected()
