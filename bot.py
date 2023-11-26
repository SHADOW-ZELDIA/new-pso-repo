API_KEY = '6149996968:AAHjfT6t-6wxjUPgTGiPZqgkk9ZcOG3iOnA'
uri = "mongodb+srv://shadow_userbot:1976abcd?@shadowbot.jcgbzsl.mongodb.net/?retryWrites=true&w=majority"
from telegram import *
from telegram.ext import *
import random , logging , html , char , datetime , pymongo , asyncio , time , monster , os , PIL , pytz
from pymongo.mongo_client import MongoClient
from bson.objectid import ObjectId
from datetime import time as tyyme
from pymongo.server_api import ServerApi
from PIL import Image, ImageDraw, ImageFont
logging.basicConfig(format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO)
logger = logging.getLogger(__name__)
print("BOT RUNNING")
mongo_client = MongoClient(uri, server_api=ServerApi('1'))
db = mongo_client['test-database'] 
beta_collection=db.get_collection("beta_users")
begin_char=char.begginner_char
weapons=char.weapons 
gift_weapon=char.begginer_weapons
insiders=[]
battlers=[]
maintenance_mode="OFF"
admins_id=[1864257459,1325708894]
playable_character=[char.SHADOW_char,char.morax_char,char.ry_char,
                   #5 star character down 3 to ....
                    char.kartos_char , char.claudia_char,
                   #4 star character down 5 to ....
                    char.fischl_char,char.echo_char,char.qiqi_char]
CHANGE_WEAPON,GACHA_LUCK,BATTLE_FINISH,TEAM_CHANGER,PVP_FINISH,KINGDOM_HANDLER, *_ = range(100)


def start(update,context):
    if maintenance_mode == "ON":
        if update.effective_user.id not in admins_id:
            update.message.reply_text("*BOT UNDER MAINTENANCE*",parse_mode=ParseMode.MARKDOWN)
            return
    msgsort = update.message
    split_msg=msgsort.text.split("_")
    if msgsort.text == "/start" or update.message.text == "/start@PSO_SoBot" or split_msg[0] == "/start reffer":
        col=db.get_collection("user_ids")
        users_lister=col.find_one()['user_ids']
        user = update.message.from_user.id
        chat=update.effective_chat
        if chat.id != user:
            keyboard=[[InlineKeyboardButton('PM',url='https://t.me/pso_sobot?start')]]
            update.message.reply_video(video='https://graph.org/file/e663ce2ffd9c8c32d3247.mp4',caption="*USE THE COMMAND IN PM*",reply_markup=InlineKeyboardMarkup(keyboard),parse_mode=ParseMode.MARKDOWN)
            return
        if user in users_lister:
            context.bot.send_message(chat_id=chat.id,text="*U HAVE ALREADY STARTED THE BOT ONCE\n    WHAT R U TRYING TO DO ?*",parse_mode=ParseMode.MARKDOWN)
            return
        char = (begin_char[0])
        inbuttons = [[InlineKeyboardButton('OBTAIN',callback_data='oba_sha_cha')],[InlineKeyboardButton('NEXT',callback_data='nex1')]]
        if split_msg[0] == "/start reffer":
            cd=context.chat_data
            cd.clear()
            cd[user]={}
            cd[user]['REFFERED']=update.message.text.split("_")[-1]
        else:
            cd=context.chat_data
            cd.clear()
            cd[user]={}
            cd[user]['REFFERED']=None
        context.bot.send_video(chat_id = update.effective_chat.id, video = char['video'],
        reply_markup=InlineKeyboardMarkup(inbuttons),caption=f"*Choose your first character :*\n\n`Character : `*{char['name']}*\n`Element : `*{char['element']}*\n`Attack Power : `*{char['atk']}*\n`Health Points : `*{char['hp']}*\n`Defense :`*{char['def']}*\n`Speed : `*{char['speed']}*\n`Critical Rate : `*{char['crit_rate']}*\n`Critical DMG :`*{char['crit_dmg']}*",
        parse_mode = ParseMode.MARKDOWN)
    elif split_msg[0] == "/start character":
        c_stats(update,context)
    elif split_msg[0] == "/start gacha":
        gacha(update,context)
    elif split_msg[0] == "/start team":
        team_selection(update,context)
    elif split_msg[0] == "/start dungeon":
        enter_dungeon(update,context)
    elif split_msg[0] == "/start travel":
        travel_logger(update,context)
    elif split_msg[0] == "/start explore":
        explore_cmd(update,context)
    elif split_msg[0] == "/start tower":
        tower_enter(update,context)
    elif split_msg[0] == "/start store":
        store_cmd(update,context)
    elif split_msg[0] == "/start events":
        event_cmd(update,context)
    

def charobitan(update, context):
    if maintenance_mode == "ON":
        if update.effective_user.id not in admins_id:
            try:
                update.callback_query.message.edit_text("*BOT UNDER MAINTENANCE*",parse_mode=ParseMode.MARKDOWN)
            except:
                update.callback_query.message.edit_caption(caption="*BOT UNDER MAINTENANCE*",parse_mode=ParseMode.MARKDOWN)
            return
    query = update.callback_query.data
    global insiders 
    user=update.callback_query.from_user
    split_data=query.split("_")[0]
    update.callback_query.answer()
    beta_user=beta_collection.find_one()['beta_players']
    cd=context.chat_data
    try:
        REFFERED_BY=cd[user.id]['REFFERED']
    except:
        update.callback_query.message.delete()
        context.bot.send_message(chat_id=update.effective_chat.id,text="*SOMETHING WENT WRONG\nTRY AGAIN*",parse_mode=ParseMode.MARKDOWN)
        return
    if 'nex1' in query:
        update.callback_query.message.delete()
        if update.callback_query.from_user.id not in beta_user:
            char = (begin_char[1])
            inbuttons = [[InlineKeyboardButton('OBTAIN',callback_data='oba_mor_cha')],[InlineKeyboardButton('NEXT',callback_data='nex2')]]
            context.bot.send_video(chat_id =update.effective_chat.id, video =char['video'],caption=f"*Choose your first character :*\n\n`Character : `*{char['name']}*\n`Element : `*{char['element']}*\n`Attack Power : `*{char['atk']}*\n`Health Points : `*{char['hp']}*\n`Defense :`*{char['def']}*\n`Speed : `*{char['speed']}*\n`Critical Rate : `*{char['crit_rate']}*\n`Critical DMG :`*{char['crit_dmg']}*",
                                                       reply_markup=InlineKeyboardMarkup(inbuttons),parse_mode=ParseMode.MARKDOWN)
            return
        context.bot.send_message(chat_id=update.effective_chat.id,text="U r not beta user") 
        return
    if 'nex2' in query:
        update.callback_query.message.delete()
        if update.callback_query.from_user.id not in beta_user:
            char = (begin_char[2])
            inbuttons = [[InlineKeyboardButton('OBTAIN',callback_data='oba_ryz_cha')],[InlineKeyboardButton('NEXT',callback_data='nex3')]]
            context.bot.send_video(chat_id =update.effective_chat.id, video=char['video'],caption=f"*Choose your first character :*\n\n`Character : `*{char['name']}*\n`Element : `*{char['element']}*\n`Attack Power : `*{char['atk']}*\n`Health Points : `*{char['hp']}*\n`Defense :`*{char['def']}*\n`Speed : `*{char['speed']}*\n`Critical Rate : `*{char['crit_rate']}*\n`Critical DMG :`*{char['crit_dmg']}*",
                                                       reply_markup=InlineKeyboardMarkup(inbuttons),parse_mode=ParseMode.MARKDOWN)
            return
        context.bot.send_message(chat_id=update.effective_chat.id,text="U r not beta user") 
        return
    if 'nex3' in query:
        update.callback_query.message.delete()
        if update.callback_query.from_user.id not in beta_user:
            char = (begin_char[0])
            inbuttons = [[InlineKeyboardButton('OBTAIN',callback_data='oba_sha_cha')],[InlineKeyboardButton('NEXT',callback_data='nex1')]]
            context.bot.send_video(chat_id =update.effective_chat.id,video=char['video'],caption=f"*Choose your first character :*\n\n`Character : `*{char['name']}*\n`Element : `*{char['element']}*\n`Attack Power : `*{char['atk']}*\n`Health Points : `*{char['hp']}*\n`Defense :`*{char['def']}*\n`Speed : `*{char['speed']}*\n`Critical Rate : `*{char['crit_rate']}*\n`Critical DMG :`*{char['crit_dmg']}*",
                                                       reply_markup=InlineKeyboardMarkup(inbuttons),parse_mode=ParseMode.MARKDOWN)
            return
        context.bot.send_message(chat_id=update.effective_chat.id,text="U r not beta user") 
        return
    if 'oba_sha_cha' in query:
            if update.callback_query.from_user.id not in beta_user:
                char = begin_char[0]
                user=update.callback_query.from_user
                update.callback_query.message.edit_caption(caption=f"Claiming The Character...")
                update.callback_query.message.edit_caption(caption=f"☆")
                update.callback_query.message.edit_caption(caption=f"☆☆")
                update.callback_query.message.edit_caption(caption=f"☆☆☆")
                update.callback_query.message.edit_caption(caption=f"☆☆☆☆")
                update.callback_query.message.edit_caption(caption=f"☆☆☆☆☆")
                for_check=db.get_collection("user_ids")
                if update.callback_query.from_user.id in for_check.find_one()['user_ids']:
                    update.callback_query.message.delete()
                    time.sleep(1)
                    update.callback_query.message.reply_text("*U HAVE ALREADY THE CLAIMED THE CHARACTER CAN'T CLAIM AGAIN*",parse_mode=ParseMode.MARKDOWN)
                    if user.id in insiders:
                        insiders.remove(user.id)
                    return
                update.callback_query.message.delete()
                if REFFERED_BY!=None:
                    fukin_data=[db.get_collection("user_datas"),db.get_collection("user_data"),db.get_collection("user_ids"),db.get_collection("beta_users")]
                    data=fukin_data[1].find_one({'_id': ObjectId(REFFERED_BY)})['user_id']
                    context.bot.send_message(chat_id=data,text=f"*SEEMS LIKE {user.first_name} USED YOUR REFFERAL AND JOINED THE BOT \nNOW IF THE PLAYER REACH RANK 3 THEN YOU WILL GET SOME AWESOME REWARDS*",parse_mode=ParseMode.MARKDOWN) 
                user_datas = {"user": f"{user.first_name}",
                              "user_id": user.id ,
                              "bag": {"segil":200,"stargems":0,"primostar":5,"tow_en":200,"starspliter_gems":0} ,
                              "gacha_details":{"event_banner":{"gacha_history":[],"gacha_pity":0},"standard_banner":{"gacha_history":[],"gacha_pity":0},"weapon_banner":{"gacha_history":[],"gacha_pity":0}},
                              "user_char":[char],
                              "weapons":gift_weapon,
                              "user_info":{'rank':0,'exp':0,'kills':0,'explores':{'normal':0,'dungeon':0},'battle_logs':{'win':0,'loss':0},'pfp':None,'region':'HELL_GATE_CASTLE_YARD'},
                              "team":{"team_player_1":{"name":"None"},"team_player_2":{"name":"None"},"team_player_3":{"name":"None"},"team_player_4":{"name":"None"}},
                              "artifacts" : [],
                              "myartifacts":{"myartifacts_1":None,"myartifacts_2":None,"myartifacts_3":None,"myartifacts_4":None,"myartifacts_5":None},
                              "date": datetime.datetime.utcnow(),
                              'extras':{"INSIDE":"NOPE",'refferal':{'total_reffered':0,"reffered_users":[],"reffered_by":REFFERED_BY}}}
                post = db.user_data
                post_id = post.insert_one(user_datas).inserted_id
                usr_dt , user_obj = db.get_collection("user_ids") , db.get_collection("user_datas")
                user_ids , user_obj_id = usr_dt.find_one()['user_ids'] , user_obj.find_one()['user_data']
                user_ids.append(user.id)
                usr_dt.update_one({"_id":ObjectId(usr_dt.find_one()['_id'])},{'$set': {'user_ids':user_ids}})
                user_obj_id.update({f'user_{user.id}':post_id})
                user_obj.update_one({"_id":ObjectId(user_obj.find_one()['_id'])},{'$set':{'user_data':user_obj_id}})
                context.bot.send_message(chat_id=update.effective_chat.id ,text=f"`You have claimed the Character `*{char['name']}*\n`Rank : `*5 Star (☆☆☆☆☆)*",parse_mode=ParseMode.MARKDOWN)
                context.bot.send_message(chat_id=-1001170323135,text=f"New User\nUser: {user.first_name}\nUser ID : {user.id}\nPOST ID : {post_id}")
                return
            context.bot.send_message(chat_id=update.effective_chat.id,text="U r not beta user")
            return
    if 'oba_mor_cha' not in query:
            if update.callback_query.from_user.id not in beta_user:
                char = begin_char[2]
                user=update.callback_query.from_user
                update.callback_query.message.edit_caption(caption=f"Claiming The Character...")
                update.callback_query.message.edit_caption(caption=f"☆")
                update.callback_query.message.edit_caption(caption=f"☆☆")
                update.callback_query.message.edit_caption(caption=f"☆☆☆")
                update.callback_query.message.edit_caption(caption=f"☆☆☆☆")
                update.callback_query.message.edit_caption(caption=f"☆☆☆☆☆")
                for_check=db.get_collection("user_ids")
                if update.callback_query.from_user.id in for_check.find_one()['user_ids']:
                    update.callback_query.message.delete()
                    time.sleep(1)
                    update.callback_query.message.reply_text("*U HAVE ALREADY THE CLAIMED THE CHARACTER CAN'T CLAIM AGAIN*",parse_mode=ParseMode.MARKDOWN)
                    if user.id in insiders:
                        insiders.remove(user.id)
                    return
                update.callback_query.message.delete()
                if REFFERED_BY!=None:
                    fukin_data=[db.get_collection("user_datas"),db.get_collection("user_data"),db.get_collection("user_ids"),db.get_collection("beta_users")]
                    data=fukin_data[1].find_one({'_id': ObjectId(REFFERED_BY)})['user_id']
                    context.bot.send_message(chat_id=data,text=f"*SEEMS LIKE {user.first_name} USED YOUR REFFERAL AND JOINED THE BOT \nNOW IF THE PLAYER REACH RANK 3 THEN YOU WILL GET SOME AWESOME REWARDS*",parse_mode=ParseMode.MARKDOWN) 
                user_datas = {"user": f"{user.first_name}",
                              "user_id": user.id ,
                              "bag": {"segil":200,"stargems":0,"primostar":5,"tow_en":200,"starspliter_gems":0} ,
                              "gacha_details":{"event_banner":{"gacha_history":[],"gacha_pity":0},"standard_banner":{"gacha_history":[],"gacha_pity":0},"weapon_banner":{"gacha_history":[],"gacha_pity":0}},
                              "user_char":[char],
                              "weapons":gift_weapon,
                              "user_info":{'rank':0,'exp':0,'kills':0,'explores':{'normal':0,'dungeon':0},'battle_logs':{'win':0,'loss':0},'pfp':None,'region':'HELL_GATE_CASTLE_YARD'},
                              "team":{"team_player_1":{"name":"None"},"team_player_2":{"name":"None"},"team_player_3":{"name":"None"},"team_player_4":{"name":"None"}},
                              "artifacts" : [],
                              "myartifacts":{"myartifacts_1":None,"myartifacts_2":None,"myartifacts_3":None,"myartifacts_4":None,"myartifacts_5":None},
                              "date": datetime.datetime.utcnow(),
                              'extras':{"INSIDE":"NOPE",'refferal':{'total_reffered':0,"reffered_users":[],"reffered_by":REFFERED_BY}}}
                post = db.user_data
                post_id = post.insert_one(user_datas).inserted_id
                usr_dt , user_obj = db.get_collection("user_ids") , db.get_collection("user_datas")
                user_ids , user_obj_id = usr_dt.find_one()['user_ids'] , user_obj.find_one()['user_data']
                user_ids.append(user.id)
                usr_dt.update_one({"_id":ObjectId(usr_dt.find_one()['_id'])},{'$set': {'user_ids':user_ids}})
                user_obj_id.update({f'user_{user.id}':post_id})
                user_obj.update_one({"_id":ObjectId(user_obj.find_one()['_id'])},{'$set':{'user_data':user_obj_id}})
                context.bot.send_message(chat_id=update.effective_chat.id ,text=f"`You have claimed the Character `*{char['name']}*\n`Rank : `*5 Star (☆☆☆☆☆)*",parse_mode=ParseMode.MARKDOWN)
                context.bot.send_message(chat_id=-1001170323135,text=f"New User\nUser: {user.first_name}\nUser ID : {user.id}\nPOST ID : {post_id}")
                return
            context.bot.send_message(chat_id=update.effective_chat.id,text="U r not beta user")
            return
    if 'oba_ryz_cha' not in query:
            if update.callback_query.from_user.id not in beta_user:
                char = begin_char[1]
                user=update.callback_query.from_user
                update.callback_query.message.edit_caption(caption=f"Claiming The Character...")
                update.callback_query.message.edit_caption(caption=f"☆")
                update.callback_query.message.edit_caption(caption=f"☆☆")
                update.callback_query.message.edit_caption(caption=f"☆☆☆")
                update.callback_query.message.edit_caption(caption=f"☆☆☆☆")
                update.callback_query.message.edit_caption(caption=f"☆☆☆☆☆")
                for_check=db.get_collection("user_ids")
                if update.callback_query.from_user.id in for_check.find_one()['user_ids']:
                    update.callback_query.message.delete()
                    time.sleep(1)
                    update.callback_query.message.reply_text("*U HAVE ALREADY THE CLAIMED THE CHARACTER CAN'T CLAIM AGAIN*",parse_mode=ParseMode.MARKDOWN)
                    if user.id in insiders:
                        insiders.remove(user.id)
                    return
                update.callback_query.message.delete()
                if REFFERED_BY!=None:
                    fukin_data=[db.get_collection("user_datas"),db.get_collection("user_data"),db.get_collection("user_ids"),db.get_collection("beta_users")]
                    data=fukin_data[1].find_one({'_id': ObjectId(REFFERED_BY)})['user_id']
                    context.bot.send_message(chat_id=data,text=f"*SEEMS LIKE {user.first_name} USED YOUR REFFERAL AND JOINED THE BOT \nNOW IF THE PLAYER REACH RANK 3 THEN YOU WILL GET SOME AWESOME REWARDS*",parse_mode=ParseMode.MARKDOWN) 
                user_datas = {"user": f"{user.first_name}",
                              "user_id": user.id ,
                              "bag": {"segil":200,"stargems":0,"primostar":5,"tow_en":200,"starspliter_gems":0} ,
                              "gacha_details":{"event_banner":{"gacha_history":[],"gacha_pity":0},"standard_banner":{"gacha_history":[],"gacha_pity":0},"weapon_banner":{"gacha_history":[],"gacha_pity":0}},
                              "user_char":[char],
                              "weapons":gift_weapon,
                              "user_info":{'rank':0,'exp':0,'kills':0,'explores':{'normal':0,'dungeon':0},'battle_logs':{'win':0,'loss':0},'pfp':None,'region':'HELL_GATE_CASTLE_YARD'},
                              "team":{"team_player_1":{"name":"None"},"team_player_2":{"name":"None"},"team_player_3":{"name":"None"},"team_player_4":{"name":"None"}},
                              "artifacts" : [],
                              "myartifacts":{"myartifacts_1":None,"myartifacts_2":None,"myartifacts_3":None,"myartifacts_4":None,"myartifacts_5":None},
                              "date": datetime.datetime.utcnow(),
                              'extras':{"INSIDE":"NOPE",'refferal':{'total_reffered':0,"reffered_users":[],"reffered_by":REFFERED_BY}}}
                post = db.user_data
                post_id = post.insert_one(user_datas).inserted_id
                usr_dt , user_obj = db.get_collection("user_ids") , db.get_collection("user_datas")
                user_ids , user_obj_id = usr_dt.find_one()['user_ids'] , user_obj.find_one()['user_data']
                user_ids.append(user.id)
                usr_dt.update_one({"_id":ObjectId(usr_dt.find_one()['_id'])},{'$set': {'user_ids':user_ids}})
                user_obj_id.update({f'user_{user.id}':post_id})
                user_obj.update_one({"_id":ObjectId(user_obj.find_one()['_id'])},{'$set':{'user_data':user_obj_id}})
                context.bot.send_message(chat_id=update.effective_chat.id ,text=f"`You have claimed the Character `*{char['name']}*\n`Rank : `*5 Star (☆☆☆☆☆)*",parse_mode=ParseMode.MARKDOWN)
                context.bot.send_message(chat_id=-1001170323135,text=f"New User\nUser: {user.first_name}\nUser ID : {user.id}\nPOST ID : {post_id}")
                return
            context.bot.send_message(chat_id=update.effective_chat.id,text="U r not beta user")
            return

def c_stats(update,context):
    if maintenance_mode == "ON":
        if update.effective_user.id not in admins_id:
            update.message.reply_text("*BOT UNDER MAINTENANCE*",parse_mode=ParseMode.MARKDOWN)
            return
    user=update.effective_user
    user_data=[db.get_collection("user_datas"),db.get_collection("user_data"),db.get_collection("user_ids"),db.get_collection("beta_users")]
    if user.id in user_data[3].find_one()['beta_players']:
        update.message.reply_text("*SEDLY U R NOT ELIGIBLE TO USE THIS COMMAND*",parse_mode=ParseMode.MARKDOWN)
    else:
        if user.id not in user_data[2].find_one()['user_ids']:
            keyboard=[[InlineKeyboardButton('PM',url='https://t.me/PSO_SoBot?start')]]
            update.message.reply_video(video='https://graph.org/file/e663ce2ffd9c8c32d3247.mp4',caption="*It seems like u haven't started\nClick on the button given below and start the bot*",reply_markup=InlineKeyboardMarkup(keyboard),parse_mode=ParseMode.MARKDOWN)
            return
        user_obj_id = user_data[0].find_one()['user_data'][f'user_{user.id}']
        user_character=user_data[1].find_one({'_id': ObjectId(user_obj_id)})['user_char']
        if len(update.message.text.split(" "))==1:
            update.message.reply_text("*Use stats with a character name*",parse_mode=ParseMode.MARKDOWN)
            return
        char_name=update.message.text.split(" ")[1].lower()
        char_number=None
        for i in range(len(user_character)):
            if char_name in user_character[i]['call_name']:
                char_number=i
        if char_number==None:
            update.message.reply_text("*Sadly u don't have that character to see it*",parse_mode=ParseMode.MARKDOWN)
            return
        character=user_character[char_number]
        buff_level=character['level']-1
        character['atk']+=round(buff_level*0.8)
        character['def']+=round(buff_level*0.5)
        character['hp']+=round(buff_level*8)
        if update.effective_chat.id == user.id:   
            buttons=[[InlineKeyboardButton('Change weapon',callback_data=f'change_weapon_0')],[InlineKeyboardButton('INFO AND MOVES',callback_data=f'charinfo')],[InlineKeyboardButton('LEVEL UP',callback_data=f'level_up')]]
        else:
            buttons=[[InlineKeyboardButton('Change weapon',url=f"https://t.me/PSO_SoBot?start=character_{character['call_name'][0]}_user{user.id}")],[InlineKeyboardButton('INFO AND MOVES',callback_data=f'charinfo')],[InlineKeyboardButton('LEVEL UP',url=f"https://t.me/PSO_SoBot?start=character_{character['call_name'][0]}_user{user.id}")]]
        if character['rank']==5:
            message = update.message.reply_video(video=character['video'],caption=f"`Character : `*{character['name']}*\n\n`Element : `*{character['element']}*\n`Rank : `*☆☆☆☆☆*\n`Level : `*{character['level']}*\n`Health Point : `*{character['hp']}*\n`Attack Power : `*{character['atk']}*\n`Defense : `*{character['def']}*\n`Speed : `*{character['speed']}*\n`Crit. Rate : `*{character['crit_rate']}%*  &  `Crit Dmg : `*{character['crit_dmg']}%*\n`Constellation : `*{character['constellation']}*\n\n`Equiped Weapon : `\n*{character['weapon'][0]['weapon_name']}*\n`Attack Boost : `*{character['weapon'][0]['buff_atk']}*",
                                                 reply_markup=InlineKeyboardMarkup(buttons),parse_mode=ParseMode.MARKDOWN)
            message_id = message.message_id
            cd = context.chat_data
            cd[message_id] = {} 
            cd[message_id]['user_id'] = user.id 
            cd[message_id]['user_ob_id'] = char_number
            return
        if character['rank']==4:
            message = update.message.reply_photo(photo=character['photo'],caption=f"`Character : `*{character['name']}*\n\n`Element : `*{character['element']}*\n`Rank : `*☆☆☆☆*\n`Level : `*{character['level']}*\n`Health Point : `*{character['hp']}*\n`Attack Power : `*{character['atk']}*\n`Defense : `*{character['def']}*\n`Speed : `*{character['speed']}*\n`Crit. Rate : `*{character['crit_rate']}%*  &  `Crit Dmg : `*{character['crit_dmg']}%*\n`Constellation : `*{character['constellation']}*\n\n`Equiped Weapon : `\n*{character['weapon'][0]['weapon_name']}*\n`Attack Boost : `*{character['weapon'][0]['buff_atk']}*",
                                                 reply_markup=InlineKeyboardMarkup(buttons),parse_mode=ParseMode.MARKDOWN)
            message_id = message.message_id
            cd = context.chat_data
            cd[message_id] = {} 
            cd[message_id]['user_id'] = user.id 
            cd[message_id]['user_ob_id'] = char_number
            return

def char_info(update,context):
    if maintenance_mode == "ON":
        if update.effective_user.id not in admins_id:
            try:
                update.callback_query.message.edit_text("*BOT UNDER MAINTENANCE*",parse_mode=ParseMode.MARKDOWN)
            except:
                update.callback_query.message.edit_caption(caption="*BOT UNDER MAINTENANCE*",parse_mode=ParseMode.MARKDOWN)
            return
    user = update.effective_user
    query = update.callback_query
    if user.id in insiders:
        query.message.edit_text("*You Cannot use this while in a Battle *",parse_mode=ParseMode.MARKDOWN)
        return
    cd = context.chat_data
    message_id= query.message.message_id
    try:
        char_num=cd[message_id]['user_ob_id']
    except:
        query.answer("INVALID NOW",show_alert=True)
        return
    if query.data.split("_")[0] != 'charinfo_stats':
        if user.id == cd[message_id]['user_id']:
            user_data_collections = [db.get_collection("user_datas"),db.get_collection("user_data"),db.get_collection("user_ids"),db.get_collection("beta_users")]
            user_obj_id = user_data_collections[0].find_one()['user_data'][f'user_{user.id}']
            user_character = user_data_collections[1].find_one({'_id': ObjectId(user_obj_id)})['user_char'][char_num]
            character_info=char.char_info(user_character['name'])
            character_moves=character_info['moves_info']
            text=f"*ABOUT {user_character['name']} :*\n`{character_info['char_info']}`\n\n*MOVES INFO : \n\n\t\t\t\t\t\tNORMAL MOVE : *\n\n\t\t\t\t\t\t`MOVE NAME : `*{character_moves['move1']['move_name']}*\n\t\t\t\t\t\t`DAMAGE : `*{character_moves['move1']['move_dmg']}*\n\t\t\t\t\t\t`INFO` : *{character_moves['move1']['move_style']}*\n\n\t\t\t\t\t\t*SKILL MOVE : *\n\n\t\t\t\t\t\t`MOVE NAME : `*{character_moves['move2']['move_name']}*\n\t\t\t\t\t\t`SKILL : `*{character_moves['move2']['move_dmg']}*\n\t\t\t\t\t\t`INFO` :*{character_moves['move2']['move_style']}*"
            button=[[InlineKeyboardButton('BACK TO STATS',callback_data=f'charinfo_stats')]]
            query.message.edit_caption(caption=text,reply_markup=InlineKeyboardMarkup(button),parse_mode=ParseMode.MARKDOWN)
            cd[message_id]['user_id'] = user.id
            cd[message_id]['user_ob_id'] = char_num
        else:
            query.answer("NOT YOUR CHARACTER",show_alert=True)
            return
    elif query.data.split("_")[1] != 'stats':
        if user.id == cd[message_id]['user_id']:
            user_data_collections = [db.get_collection("user_datas"),db.get_collection("user_data"),db.get_collection("user_ids"),db.get_collection("beta_users")]
            user_obj_id = user_data_collections[0].find_one()['user_data'][f'user_{user.id}']
            character = user_data_collections[1].find_one({'_id': ObjectId(user_obj_id)})['user_char'][char_num]
            if update.effective_chat.id == user.id:
                buttons=[[InlineKeyboardButton('Change weapon',callback_data=f'change_weapon_0')],[InlineKeyboardButton('INFO AND MOVES',callback_data=f'charinfo')]]
                if user.id == 1864257459:
                    buttons=[[InlineKeyboardButton('Change weapon',callback_data=f'change_weapon_0')],[InlineKeyboardButton('INFO AND MOVES',callback_data=f'charinfo')],[InlineKeyboardButton('LEVEL UP',callback_data=f'level_up')]]
            else:
                buttons=[[InlineKeyboardButton('Change weapon',url=f"https://t.me/PSO_SoBot?start=character_{character['call_name'][0]}_user{user.id}")],[InlineKeyboardButton('INFO AND MOVES',callback_data=f'charinfo')]]
                if user.id == 1864257459:
                    buttons=[[InlineKeyboardButton('Change weapon',callback_data=f'change_weapon_0')],[InlineKeyboardButton('INFO AND MOVES',callback_data=f'charinfo')],[InlineKeyboardButton('LEVEL UP',callback_data=f'level_up')]]
            if character['rank']==5:
                message = update.message.reply_video(video=character['video'],caption=f"`Character : `*{character['name']}*\n\n`Element : `*{character['element']}*\n`Rank : `*☆☆☆☆☆*\n`Level : `*{character['level']}*\n`Health Point : `*{character['hp']}*\n`Attack Power : `*{character['atk']}*\n`Defense : `*{character['def']}*\n`Speed : `*{character['speed']}*\n`Crit. Rate : `*{character['crit_rate']}%*  &  `Crit Dmg : `*{character['crit_dmg']}%*\n`Constellation : `*{character['constellation']}*\n\n`Equiped Weapon : `\n*{character['weapon'][0]['weapon_name']}*\n`Attack Boost : `*{character['weapon'][0]['buff_atk']}*",
                                        reply_markup=InlineKeyboardMarkup(buttons),parse_mode=ParseMode.MARKDOWN)
                message_id = message.message_id
                cd = context.chat_data
                cd[message_id] = {} 
                cd[message_id]['user_id'] = user.id 
                cd[message_id]['user_ob_id'] = char_num
                return
            if character['rank']==4:
                message = update.message.reply_photo(photo=character['photo'],caption=f"`Character : `*{character['name']}*\n\n`Element : `*{character['element']}*\n`Rank : `*☆☆☆☆*\n`Level : `*{character['level']}*\n`Health Point : `*{character['hp']}*\n`Attack Power : `*{character['atk']}*\n`Defense : `*{character['def']}*\n`Speed : `*{character['speed']}*\n`Crit. Rate : `*{character['crit_rate']}%*  &  `Crit Dmg : `*{character['crit_dmg']}%*\n`Constellation : `*{character['constellation']}*\n\n`Equiped Weapon : `\n*{character['weapon'][0]['weapon_name']}*\n`Attack Boost : `*{character['weapon'][0]['buff_atk']}*",
                                        reply_markup=InlineKeyboardMarkup(buttons),parse_mode=ParseMode.MARKDOWN)
                message_id = message.message_id
                cd = context.chat_data
                cd[message_id] = {} 
                cd[message_id]['user_id'] = user.id 
                cd[message_id]['user_ob_id'] = char_num
                return
        else:
            query.answer("NOT YOUR CHARACTER",show_alert=True)
            return
def change_weapon(update , context):
    if maintenance_mode == "ON":
        if update.effective_user.id not in admins_id:
            try:
                update.callback_query.message.edit_text("*BOT UNDER MAINTENANCE*",parse_mode=ParseMode.MARKDOWN)
            except:
                update.callback_query.message.edit_caption(caption="*BOT UNDER MAINTENANCE*",parse_mode=ParseMode.MARKDOWN)
            return
    user=update.effective_user
    query = update.callback_query
    if user.id in insiders:
        query.message.edit_text("*You Cannot use this while in a Battle *",parse_mode=ParseMode.MARKDOWN)
        return
    cd = context.chat_data
    message_id = query.message.message_id
    user_data_collections = [db.get_collection("user_datas"),db.get_collection("user_data"),db.get_collection("user_ids"),db.get_collection("beta_users")]
    user_ob_id = cd[message_id]['user_ob_id']
    user_obj_id = user_data_collections[0].find_one()['user_data'][f'user_{user.id}']
    user_character = user_data_collections[1].find_one({'_id': ObjectId(user_obj_id)})['user_char'][user_ob_id]
    weapon_num = []
    
    for i, weapon in enumerate(user_data_collections[1].find_one({'_id': ObjectId(user_obj_id)})['weapons']):
        if weapon['weapon_type'] == user_character['weapon_type']:
            weapon_num.append(i)

    keyboard1, keyboard2, keyboard3, keyboard4 = [[]], [[], []], [[], [], []], [[], [], [], []]
    n = int(query.data.split("_")[-1])
    m = int(query.data.split("_")[-1])
    print(m)
    print(n)
    weapons_list = f"`Equipped Weapon : `\n\n*{user_character['weapon'][0]['weapon_name']}*\n\n`Usable Weapons : `\n\n"
    update.callback_query.message.delete()
    if len(weapon_num)-m > 20:
        for i in range(20):
            L = user_data_collections[1].find_one({'_id': ObjectId(user_obj_id)})['weapons'][weapon_num[n]]
            weapons_list += f"*{n+1}. {L['weapon_name']}\n*"
            if len(weapon_num)-m > 0 and len(weapon_num)-m < 6:
                keyboard1[0].append(InlineKeyboardButton(f'{n+1}',callback_data=f"weapon-{weapon_num[n]}"))
            if len(weapon_num)-m > 5 and len(weapon_num)-m < 11:
                if n < 5+m :
                    keyboard2[0].append(InlineKeyboardButton(f'{n+1}',callback_data=f"weapon-{weapon_num[n]}"))
                if n > 4+m :
                    keyboard2[1].append(InlineKeyboardButton(f'{n+1}',callback_data=f"weapon-{weapon_num[n]}"))
            elif len(weapon_num)-m > 10 and len(weapon_num)-m < 16:
                if n < 5+m :
                    keyboard3[0].append(InlineKeyboardButton(f'{n+1}',callback_data=f"weapon-{weapon_num[n]}"))
                if n > 4+m and n < 10+m :
                    keyboard3[1].append(InlineKeyboardButton(f'{n+1}',callback_data=f"weapon-{weapon_num[n]}"))
                if n > 9+m :
                    keyboard3[2].append(InlineKeyboardButton(f'{n+1}',callback_data=f"weapon-{weapon_num[n]}"))
            else:
                if n < 5+m :
                    keyboard4[0].append(InlineKeyboardButton(f'{n+1}',callback_data=f"weapon-{weapon_num[n]}"))
                if n > 4+m and n < 10+m :
                    keyboard4[1].append(InlineKeyboardButton(f'{n+1}',callback_data=f"weapon-{weapon_num[n]}"))
                if n > 9+m and n < 15+m :
                    keyboard4[2].append(InlineKeyboardButton(f'{n+1}',callback_data=f"weapon-{weapon_num[n]}"))
                if n > 14+m : 
                    keyboard4[3].append(InlineKeyboardButton(f'{n+1}',callback_data=f"weapon-{weapon_num[n]}"))
            n=n+1
        if len(weapon_num)-m > 0 and len(weapon_num)-m < 6:
            keyboard=keyboard1
        elif len(weapon_num)-m > 5 and len(weapon_num)-m < 11:
            keyboard=keyboard2
        elif len(weapon_num)-m > 10 and len(weapon_num)-m < 16:
            keyboard=keyboard3
        else:
            keyboard=keyboard4
        keyboard4.append([(InlineKeyboardButton('CLOSE', callback_data='weaponchange_close'))])
        keyboard4.append([(InlineKeyboardButton('NEXT', callback_data=f"change_weapon_{n}"))])
        keyboard = keyboard4
        message = context.bot.send_message(chat_id=update.effective_chat.id, text=weapons_list, reply_markup=InlineKeyboardMarkup(keyboard), parse_mode=ParseMode.MARKDOWN)
        message_id = message.message_id
        cd[message_id] = {}
        cd[message_id]['user_ob_id'] = user_ob_id
        cd[message_id]['user_id'] = user.id
        return CHANGE_WEAPON
    if len(weapon_num)-m < 21:
        for i in range(len(weapon_num)-m):
            L=user_data_collections[1].find_one({'_id': ObjectId(user_obj_id)})['weapons'][weapon_num[n]]
            weapons_list+=f"*{n+1}. {L['weapon_name']}\n*"
            if len(weapon_num)-m > 0 and len(weapon_num)-m < 6:
                keyboard1[0].append(InlineKeyboardButton(f'{n+1}',callback_data=f"weapon-{weapon_num[n]}"))
            if len(weapon_num)-m > 5 and len(weapon_num)-m < 11:
                if n < 5+m :
                    keyboard2[0].append(InlineKeyboardButton(f'{n+1}',callback_data=f"weapon-{weapon_num[n]}"))
                if n > 4+m :
                    keyboard2[1].append(InlineKeyboardButton(f'{n+1}',callback_data=f"weapon-{weapon_num[n]}"))
            elif len(weapon_num)-m > 10 and len(weapon_num)-m < 16:
                if n < 5+m :
                    keyboard3[0].append(InlineKeyboardButton(f'{n+1}',callback_data=f"weapon-{weapon_num[n]}"))
                if n > 4+m and n < 10+m :
                    keyboard3[1].append(InlineKeyboardButton(f'{n+1}',callback_data=f"weapon-{weapon_num[n]}"))
                if n > 9+m :
                    keyboard3[2].append(InlineKeyboardButton(f'{n+1}',callback_data=f"weapon-{weapon_num[n]}"))
            else:
                if n < 5+m :
                    keyboard4[0].append(InlineKeyboardButton(f'{n+1}',callback_data=f"weapon-{weapon_num[n]}"))
                if n > 4+m and n < 10+m :
                    keyboard4[1].append(InlineKeyboardButton(f'{n+1}',callback_data=f"weapon-{weapon_num[n]}"))
                if n > 9+m and n < 15+m :
                    keyboard4[2].append(InlineKeyboardButton(f'{n+1}',callback_data=f"weapon-{weapon_num[n]}"))
                if n > 14+m and n < 21+m :
                    keyboard4[3].append(InlineKeyboardButton(f'{n+1}',callback_data=f"weapon-{weapon_num[n]}"))
            n=n+1
        if len(weapon_num)-m > 0 and len(weapon_num)-m < 6:
            keyboard=keyboard1
        elif len(weapon_num)-m > 5 and len(weapon_num)-m < 11:
            keyboard=keyboard2
        elif len(weapon_num)-m > 10 and len(weapon_num)-m < 16:
            keyboard=keyboard3
        else:
            keyboard=keyboard4
        keyboard.append([(InlineKeyboardButton('CLOSE', callback_data='weaponchange_close'))])
        message = context.bot.send_message(chat_id=update.effective_chat.id, text=weapons_list, reply_markup=InlineKeyboardMarkup(keyboard), parse_mode=ParseMode.MARKDOWN)
        message_id = message.message_id
        cd[message_id] = {}
        cd[message_id]['user_ob_id'] = user_ob_id
        cd[message_id]['user_id'] = user.id
        return CHANGE_WEAPON

def weapon_changed(update,context):
    if maintenance_mode == "ON":
        if update.effective_user.id not in admins_id:
            try:
                update.callback_query.message.edit_text("*BOT UNDER MAINTENANCE*",parse_mode=ParseMode.MARKDOWN)
            except:
                update.callback_query.message.edit_caption(caption="*BOT UNDER MAINTENANCE*",parse_mode=ParseMode.MARKDOWN)
            return
    user=update.callback_query.from_user
    query = update.callback_query
    if user.id in insiders:
        query.message.edit_text("*You Cannot use this while in a Battle *",parse_mode=ParseMode.MARKDOWN)
        return
    cd = context.chat_data
    message_id = query.message.message_id
    character_id = cd[message_id]['user_ob_id']
    user_id = cd[message_id]['user_id']
    weapon_id = query.data.split('-')[1]
    if query.data == 'weaponchange_close':
        query.edit_text('Closed')
        return 
    user_data=[db.get_collection("user_datas"),db.get_collection("user_data"),db.get_collection("user_ids"),db.get_collection("beta_users")]
    user_obj_id = user_data[0].find_one()['user_data'][f'user_{user_id}']
    user_characters=user_data[1].find_one({'_id': ObjectId(user_obj_id)})['user_char']
    user_weapons=user_data[1].find_one({'_id': ObjectId(user_obj_id)})['weapons']
    selected_character=user_characters[int(character_id)]
    char_weapon = selected_character['weapon']
    selected_weapon = user_weapons[int(weapon_id)]
    if selected_weapon['weapon_type'] != selected_character['weapon_type']:
        query.message.edit_text("Something Went wrong\n   Try again ",parse_mode=ParseMode.MARKDOWN)
        return
    query.message.edit_text(f"`Character : `*{selected_character['name']}*\n`Weapon : `*Changed from {selected_character['weapon'][0]['weapon_name']} to {selected_weapon['weapon_name']}*",parse_mode=ParseMode.MARKDOWN)
    char_weapon.append(selected_weapon)
    user_weapons.append(char_weapon[0])
    char_weapon.pop(0)
    user_weapons.pop(int(weapon_id))
    selected_character['weapon']=char_weapon
    user_characters.insert(int(character_id),selected_character)
    user_characters.pop(int(character_id))
    user_data[1].update_one({"_id":ObjectId(user_obj_id)},{"$set":{'user_char':user_characters}})
    user_data[1].update_one({"_id":ObjectId(user_obj_id)},{"$set":{'weapons':user_weapons}})
    return -1

def user_checker(update,context):
    user=update.effective_user
    if user.id == 1864257459 :
        replied_user=update.message.reply_to_message.from_user
        user_data=[db.get_collection("user_datas"),db.get_collection("user_data"),db.get_collection("user_ids"),db.get_collection("beta_users")]
        user_obj_id = user_data[0].find_one()['user_data'][f'user_{replied_user.id}']
        user_gacha_detail=user_data[1].find_one({'_id': ObjectId(user_obj_id)})['gacha_details']
        user_gacha_history=user_gacha_detail['standard_banner']['gacha_history']
        text="*USER STANDARD BANNER GACHA HISTORY : *\n\n"
        text+="`LAST 10 PULL HISTORY :`\n"
        if len(user_gacha_history)>9:
            for i in range(10):
                text+=f"*{user_gacha_history[len(user_gacha_history)-i-1]}\n*"
                print(user_gacha_history[len(user_gacha_history)-i-1],"\n")
            update.message.reply_text(text,parse_mode=ParseMode.MARKDOWN)
        else:
            update.message.reply_text("*NOTHING SUSPECIOUS*",parse_mode=ParseMode.MARKDOWN)
    else:
        update.message.reply_text("FUCK OFF")

def event_cmd(update,context):
    if maintenance_mode == "ON":
        if update.effective_user.id not in admins_id:
            update.message.reply_text("*BOT UNDER MAINTENANCE*",parse_mode=ParseMode.MARKDOWN)
            return
    user=update.effective_user
    user_data=[db.get_collection("user_datas"),db.get_collection("user_data"),db.get_collection("user_ids"),db.get_collection("beta_users")]
    if user.id in user_data[3].find_one()['beta_players']:
        update.message.reply_text("*SEDLY U R NOT WORTHY TO USE THIS COMMAND*",parse_mode=ParseMode.MARKDOWN)
    else:
        if user.id not in user_data[2].find_one()['user_ids']:
            keyboard=[[InlineKeyboardButton('PM',url='https://t.me/PSO_SoBot?start')]]
            update.message.reply_video(video='https://graph.org/file/e663ce2ffd9c8c32d3247.mp4',caption="*It seems like u haven't started\nClick on the button given below and start the bot*",reply_markup=InlineKeyboardMarkup(keyboard),parse_mode=ParseMode.MARKDOWN)
            return
        user_obj_id = user_data[0].find_one()['user_data'][f'user_{user.id}']
        user_bag=user_data[1].find_one({'_id': ObjectId(user_obj_id)})['bag']
        if update.effective_chat.id != user.id:
            keyboard=[[InlineKeyboardButton('USE IN PM',url='https://t.me/PSO_SoBot?start=events')]]
            update.message.reply_text("*USE IN PM*",reply_markup=InlineKeyboardMarkup(keyboard),parse_mode=ParseMode.MARKDOWN)
            return
        else:
            if user.id not in [1864257459]:
                keyboard=[[InlineKeyboardButton('REFFERAL',callback_data=f'reffer_maker'),InlineKeyboardButton('DAILY LOGIN',callback_data=f'claimdaily')],[InlineKeyboardButton('STORY EVENT',callback_data=f'story_event')]]
                update.message.reply_text("*SELECT THE EVENT WHICH U WANT TO ENTER*",reply_markup=InlineKeyboardMarkup(keyboard),parse_mode=ParseMode.MARKDOWN)
                return
            keyboard=[[InlineKeyboardButton('REFFERAL',callback_data=f'reffer_maker'),InlineKeyboardButton('DAILY LOGIN',callback_data=f'claimdaily')],[InlineKeyboardButton('STORY EVENT',callback_data=f'story_event')]]
            update.message.reply_text("*SELECT THE EVENT WHICH U WANT TO ENTER*",reply_markup=InlineKeyboardMarkup(keyboard),parse_mode=ParseMode.MARKDOWN)
            return

def back_to_event(update,context):
    if maintenance_mode == "ON":
        if update.effective_user.id not in admins_id:
            try:
                update.callback_query.message.edit_text("*BOT UNDER MAINTENANCE*",parse_mode=ParseMode.MARKDOWN)
            except:
                update.callback_query.message.edit_caption(caption="*BOT UNDER MAINTENANCE*",parse_mode=ParseMode.MARKDOWN)
            return
    user=update.effective_user
    query=update.callback_query
    keyboard=[[InlineKeyboardButton('REFFERAL',callback_data=f'reffer_maker'),InlineKeyboardButton('DAILY LOGIN',callback_data=f'claimdaily')],[InlineKeyboardButton('STORY EVENT',callback_data=f'story_event')]]
    query.message.edit_text("*SELECT THE EVENT WHICH U WANT TO ENTER*",reply_markup=InlineKeyboardMarkup(keyboard),parse_mode=ParseMode.MARKDOWN)
    return

def user_Remover(update,context):
    user=update.effective_user
    if user.id == 1864257459 :
        replied_user=update.message.reply_to_message.from_user
        user_data=[db.get_collection("user_datas"),db.get_collection("user_data"),db.get_collection("user_ids"),db.get_collection("beta_users")]
        user_obj_id = user_data[0].find_one()['user_data'][f'user_{replied_user.id}']
        user_character=user_data[1].find_one({'_id': ObjectId(user_obj_id)})['user_char']
        for i in range(len(user_character)):
            if user_character[i]['name']=='QIQI':
                user_character.pop(i)
        user_data[1].update_one({"_id":ObjectId(user_obj_id)},{"$set":{'user_char':user_character}})
        user_weapons=user_data[1].find_one({'_id': ObjectId(user_obj_id)})['weapons']
        for i in range(9):
            user_weapons.pop(27)
        user_data[1].update_one({"_id":ObjectId(user_obj_id)},{"$set":{'weapons':user_weapons}})
        update.message.reply_text("DONE")
    else:
        update.message.reply_text("FUCK OFF")

def store_cmd(update,context):
    if maintenance_mode == "ON":
        if update.effective_user.id not in admins_id:
            update.message.reply_text("*BOT UNDER MAINTENANCE*",parse_mode=ParseMode.MARKDOWN)
            return
    user=update.message.from_user
    user_data=[db.get_collection("user_datas"),db.get_collection("user_data"),db.get_collection("user_ids"),db.get_collection("beta_users")]
    if user.id in user_data[3].find_one()['beta_players']:
        update.message.reply_text("*SEDLY U R NOT WORTHY TO USE THIS COMMAND*",parse_mode=ParseMode.MARKDOWN)
    else:
        if user.id not in user_data[2].find_one()['user_ids']:
            keyboard=[[InlineKeyboardButton('PM',url='https://t.me/PSO_SoBot?start')]]
            update.message.reply_video(video='https://graph.org/file/e663ce2ffd9c8c32d3247.mp4',caption="*It seems like u haven't started\nClick on the button given below and start the bot*",reply_markup=InlineKeyboardMarkup(keyboard),parse_mode=ParseMode.MARKDOWN)
            return
        user_obj_id = user_data[0].find_one()['user_data'][f'user_{user.id}']
        user_bag=user_data[1].find_one({'_id': ObjectId(user_obj_id)})['bag']
        if update.effective_chat.id != user.id:
            keyboard=[[InlineKeyboardButton('USE IN PM',url='https://t.me/PSO_SoBot?start=store')]]
            update.message.reply_text("*USE IN PM*",reply_markup=InlineKeyboardMarkup(keyboard),parse_mode=ParseMode.MARKDOWN)
            return
        else:
            if user.id not in [1864257459]:
                keyboard=[[InlineKeyboardButton('STARGEMS AND PRIMO STORE',callback_data=f'mfstore_1')]]
                update.message.reply_text("*WELCOME TO STORE\nSELECT THE STORE WHICH U WANT TO ENTER*",reply_markup=InlineKeyboardMarkup(keyboard),parse_mode=ParseMode.MARKDOWN)
                return
            keyboard=[[InlineKeyboardButton('STARGEMS AND PRIMO STORE',callback_data=f'mfstore_1')],[InlineKeyboardButton('STARSPLITER STORE',callback_data=f'mfstore_1=2'),InlineKeyboardButton('DRESSING STORE',callback_data=f'mfstore_3')]]
            update.message.reply_text("*WELCOME TO STORE\nSELECT THE STORE WHICH U WANT TO ENTER*",reply_markup=InlineKeyboardMarkup(keyboard),parse_mode=ParseMode.MARKDOWN)
            return

def store_inline(update,context):
    if maintenance_mode == "ON":
        if update.effective_user.id not in admins_id:
            try:
                update.callback_query.message.edit_text("*BOT UNDER MAINTENANCE*",parse_mode=ParseMode.MARKDOWN)
            except:
                update.callback_query.message.edit_caption(caption="*BOT UNDER MAINTENANCE*",parse_mode=ParseMode.MARKDOWN)
            return
    user=update.effective_user
    query=update.callback_query
    if query.data.split("_")[-1]=='1':
        keyboard=[[InlineKeyboardButton('STARGEMS TO PRIMOSTAR',callback_data=f'starstore_1')],[InlineKeyboardButton('PRIMOSTAR TO STARGEMS',callback_data=f'starstore_3')],[InlineKeyboardButton('BACK',callback_data=f'mfstore_4')]]
        query.message.edit_text("*SELECT THE CONVERTER WHICH U WANT TO USE*",reply_markup=InlineKeyboardMarkup(keyboard),parse_mode=ParseMode.MARKDOWN)
        return
    elif query.data.split("_")[-1]=='2':
        print('STARSPLITTER')
    elif query.data.split("_")[-1]=='3':
        print('DRESS')
    elif query.data.split("_")[-1]=='4':
        keyboard=[[InlineKeyboardButton('STARGEMS AND PRIMO STORE',callback_data=f'mfstore_1')]]
        query.message.edit_text("*SELECT THE STORE WHICH U WANT TO ENTER*",reply_markup=InlineKeyboardMarkup(keyboard),parse_mode=ParseMode.MARKDOWN)
        return

def primo_and_star_store(update,context):
    if maintenance_mode == "ON":
        if update.effective_user.id not in admins_id:
            try:
                update.callback_query.message.edit_text("*BOT UNDER MAINTENANCE*",parse_mode=ParseMode.MARKDOWN)
            except:
                update.callback_query.message.edit_caption(caption="*BOT UNDER MAINTENANCE*",parse_mode=ParseMode.MARKDOWN)
            return
    user=update.effective_user
    query=update.callback_query
    query.message.edit_text("*PROCESSING*",parse_mode=ParseMode.MARKDOWN)
    user_data=[db.get_collection("user_datas"),db.get_collection("user_data"),db.get_collection("user_ids"),db.get_collection("beta_users")]
    user_obj_id = user_data[0].find_one()['user_data'][f'user_{user.id}']
    user_bag=user_data[1].find_one({'_id':ObjectId(user_obj_id)})['bag']
    if query.data.split("_")[-1]=='1':
        if user_bag['stargems']>(5*150)-1:
            keyboard=[[InlineKeyboardButton('BUY 1 PRIMOSTAR',callback_data=f'purchasemaker_primostar_1')],[InlineKeyboardButton('BUY 5 PRIMOSTAR',callback_data=f'purchasemaker_primostar_5')],[InlineKeyboardButton('BACK',callback_data=f'mfstore_4')]]
        else:
            keyboard=[[InlineKeyboardButton('BUY 1 PRIMOSTAR',callback_data=f'purchasemaker_primostar_1')],[InlineKeyboardButton('BACK',callback_data=f'mfstore_4')]]
        query.message.edit_text(f"*CLICK ON THE BUTTON DOWN BELLOW TO PURCHASE PRIMOSTAR*\n\n`TOTAL STARGEMS IN BAG : ` *{user_bag['stargems']}\n\nTO BUY 1 PRIMOSTAR YOU NEED 150 STARGEMS*",reply_markup=InlineKeyboardMarkup(keyboard),parse_mode=ParseMode.MARKDOWN)
        return
    if query.data.split("_")[-1]=='3':
        if user_bag['primostar']>4:
            keyboard=[[InlineKeyboardButton('SELL 1 PRIMOSTAR',callback_data=f'purchasemaker_stargems_1')],[InlineKeyboardButton('SELL 5 PRIMOSTAR',callback_data=f'purchasemaker_stargems_5')],[InlineKeyboardButton('BACK',callback_data=f'mfstore_4')]]
        else:
            keyboard=[[InlineKeyboardButton('SELL 1 PRIMOSTAR',callback_data=f'purchasemaker_stargems_1')],[InlineKeyboardButton('BACK',callback_data=f'mfstore_4')]]
        query.message.edit_text(f"*CLICK ON THE BUTTON DOWN BELLOW TO SELL PRIMOSTAR*\n\n`TOTAL PRIMOSTAR IN BAG : ` *{user_bag['primostar']}\n\nBY SELLING 1 PRIMOSTAR YOU WILL GET 100 STARGEMS*",reply_markup=InlineKeyboardMarkup(keyboard),parse_mode=ParseMode.MARKDOWN)
        return

def purchase_maker_1(update,context):
    if maintenance_mode == "ON":
        if update.effective_user.id not in admins_id:
            try:
                update.callback_query.message.edit_text("*BOT UNDER MAINTENANCE*",parse_mode=ParseMode.MARKDOWN)
            except:
                update.callback_query.message.edit_caption(caption="*BOT UNDER MAINTENANCE*",parse_mode=ParseMode.MARKDOWN)
            return
    user=update.effective_user
    query=update.callback_query
    query.message.edit_text("*PROCESSING*",parse_mode=ParseMode.MARKDOWN)
    user_data=[db.get_collection("user_datas"),db.get_collection("user_data"),db.get_collection("user_ids"),db.get_collection("beta_users")]
    user_obj_id = user_data[0].find_one()['user_data'][f'user_{user.id}']
    user_bag=user_data[1].find_one({'_id':ObjectId(user_obj_id)})['bag']
    if query.data.split("_")[-2]=='stargems':
        if user_bag['primostar']<int(query.data.split("_")[-1]):
            query.message.edit_text(f"*EXITED THE STORE\nDUE TO NOT ENOUGH PRIMOSTAR*",parse_mode=ParseMode.MARKDOWN)
            return
        else:
            user_bag['primostar']-=int(query.data.split("_")[-1])
            user_bag['stargems']+=(int(query.data.split("_")[-1])*100)
            user_data[1].update_one({"_id":ObjectId(user_obj_id)},{"$set":{'bag':user_bag}})
            if user_bag['primostar']>4:
                keyboard=[[InlineKeyboardButton('SELL 1 PRIMOSTAR',callback_data=f'purchasemaker_stargems_1')],[InlineKeyboardButton('SELL 5 PRIMOSTAR',callback_data=f'purchasemaker_stargems_5')],[InlineKeyboardButton('BACK',callback_data=f'mfstore_4')]]
            else:
                keyboard=[[InlineKeyboardButton('SELL 1 PRIMOSTAR',callback_data=f'purchasemaker_stargems_1')],[InlineKeyboardButton('BACK',callback_data=f'mfstore_4')]]
            query.message.edit_text(f"*SOLD {int(query.data.split('_')[-1])} PRIMOSTAR AND GOT {int(query.data.split('_')[-1])*100} STARGEMS\n\nIF YOU WANT TO SELL MORE CLICK ON THE BUTTON DOWN BELLOW TO SELL PRIMOSTAR*\n\n`TOTAL PRIMOSTAR IN BAG : ` *{user_bag['primostar']}\n\nBY SELLING 1 PRIMOSTAR YOU WILL GET 100 STARGEMS*",reply_markup=InlineKeyboardMarkup(keyboard),parse_mode=ParseMode.MARKDOWN)
            return
    else:
        if user_bag['stargems']<(int(query.data.split("_")[-1])*150):
            query.message.edit_text(f"*EXITED THE STORE\nDUE TO NOT ENOUGH STARGEMS*",parse_mode=ParseMode.MARKDOWN)
            return
        else:
            user_bag['primostar']+=int(query.data.split("_")[-1])
            user_bag['stargems']-=(int(query.data.split("_")[-1])*150)
            user_data[1].update_one({"_id":ObjectId(user_obj_id)},{"$set":{'bag':user_bag}})
            if user_bag['stargems']>(5*150)-1:
                keyboard=[[InlineKeyboardButton('BUY 1 PRIMOSTAR',callback_data=f'purchasemaker_primostar_1')],[InlineKeyboardButton('BUY 5 PRIMOSTAR',callback_data=f'purchasemaker_primostar_5')],[InlineKeyboardButton('BACK',callback_data=f'mfstore_4')]]
            else:
                keyboard=[[InlineKeyboardButton('BUY 1 PRIMOSTAR',callback_data=f'purchasemaker_primostar_1')],[InlineKeyboardButton('BACK',callback_data=f'mfstore_4')]]
            query.message.edit_text(f"*BOUGHT {int(query.data.split('_')[-1])} PRIMOSTAR AND GAVE AWAY {int(query.data.split('_')[-1])*150} STARGEMS\n\nIF YOU WANT TO BUY MORE CLICK ON THE BUTTON DOWN BELLOW TO PURCHASE PRIMOSTAR*\n\n`TOTAL STARGEMS IN BAG : ` *{user_bag['stargems']}\n\nTO BUY 1 PRIMOSTAR YOU NEED 150 STARGEMS*",reply_markup=InlineKeyboardMarkup(keyboard),parse_mode=ParseMode.MARKDOWN)
            return

def refferal(update,context):
    if maintenance_mode == "ON":
        if update.effective_user.id not in admins_id:
            try:
                update.callback_query.message.edit_text("*BOT UNDER MAINTENANCE*",parse_mode=ParseMode.MARKDOWN)
            except:
                update.callback_query.message.edit_caption(caption="*BOT UNDER MAINTENANCE*",parse_mode=ParseMode.MARKDOWN)
            return
    user=update.effective_user
    query=update.callback_query
    user_data=[db.get_collection("user_datas"),db.get_collection("user_data"),db.get_collection("user_ids"),db.get_collection("beta_users")]
    user_obj_id = user_data[0].find_one()['user_data'][f'user_{user.id}']
    refferal=user_data[1].find_one({'_id': ObjectId(user_obj_id)})['extras']['refferal']
    refferal_link=f'`https://t.me/PSO_SoBot?start=reffer_{user_obj_id}`'
    keyboard=[[InlineKeyboardButton('BACK',callback_data=f'back_to_event')]]
    query.message.edit_text("*YOUR REFFERAL LINK : *"+refferal_link+f"\n\n*TOTAL REFFERED USER : *`{refferal['total_reffered']}`",reply_markup=InlineKeyboardMarkup(keyboard),parse_mode=ParseMode.MARKDOWN)


def kingdom_updater(update,context):
    if maintenance_mode == "ON":
        if update.effective_user.id not in admins_id:
            update.message.reply_text("*BOT UNDER MAINTENANCE*",parse_mode=ParseMode.MARKDOWN)
            return
    user=update.effective_user
    if user.id == 1864257459 :
        kingdoms=db.get_collection("all_kingdoms")
        kingdom_data = kingdoms.find_one()['kingdom_datas']
        kingdom_data['kingdom_1']['king_chat']=11111111
        print(kingdom_data['kingdom_1'])
        update.message.reply_text("*LOADING....*",parse_mode=ParseMode.MARKDOWN)
    else:
        update.messasge.reply_text("IC YOU'RE REALLY A NIGGA")

def kingdom_adder(update,context):
    if maintenance_mode == "ON":
        if update.effective_user.id not in admins_id:
            update.message.reply_text("*BOT UNDER MAINTENANCE*",parse_mode=ParseMode.MARKDOWN)
            return
    user=update.message.from_user
    if user.id == 1864257459:
        kingdoms=db.get_collection("all_kingdoms")
        kingdom_data = kingdoms.find_one()['kingdom_datas']
        kingdom_data[f"kingdom_{len(list(kingdom_data.keys()))+1}"]={"name":f"{update.message.text.split(' ')[1].upper()} {update.message.text.split(' ')[2].upper()}",
                                                                    "resources":{"gold":800,"silver":0},
                                                                    "structural":{"houses":20,"kingdom_def":50000},
                                                                    "members":[],
                                                                    "member_role":{},
                                                                    "KING_DUKE":{'KING':int(update.message.text.split(' ')[-2].upper()),'DUKE':int(update.message.text.split(' ')[-1].upper())}
                                                                    }
        kingdoms.update_one({"_id":ObjectId(kingdoms.find_one()['_id'])},{'$set':{'kingdom_datas':kingdom_data}})
        update.message.reply_text("*DOING.....*",parse_mode=ParseMode.MARKDOWN)
    else:
        update.message.reply_text("*EHH NIGGA SPOTTED*",parse_mode=ParseMode.MARKDOWN)
    return

def kingdom_joiner(update,context):
    if maintenance_mode == "ON":
        if update.effective_user.id not in admins_id:
            try:
                update.callback_query.message.edit_text("*BOT UNDER MAINTENANCE*",parse_mode=ParseMode.MARKDOWN)
            except:
                update.callback_query.message.edit_caption(caption="*BOT UNDER MAINTENANCE*",parse_mode=ParseMode.MARKDOWN)
            return
    user=update.effective_user
    query=update.callback_query
    cd=context.chat_data
    message_id = query.message.message_id
    try:
        user_id=cd[message_id]['user_id']
    except:
        query.message_edit_text("*THIS COMMAND IS NOW INVALID*",parse_mode=ParseMode.MARKDOWN)
    if user_id==user.id:
        kingdoms=db.get_collection("all_kingdoms")
        kingdom_data = kingdoms.find_one()['kingdom_datas']
        all_members=[]
        kings_id=[]
        dukes_id=[]
        for i in range(len(list(kingdom_data.keys()))):
            kingdom_members=kingdom_data[f"kingdom_{i+1}"]['members']
            for j in range(len(kingdom_members)):
                all_members.append(kingdom_members[j])
            if user.id == kingdom_data[f"kingdom_{i+1}"]['KING_DUKE']['KING']:
                query.answer(f"YOU'RE THE KING OF {kingdom_data[f'kingdom_{i+1}']['name']}",show_alert=True)
                return
            elif user.id in dukes_id:
                query.answer(f"YOU'RE THE DUKE OF {kingdom_data[f'kingdom_{i+1}']['name']}",show_alert=True)
                return
        if user.id in all_members:
            query.answer("YOU'RE ALREADY IN A KINGDOM",show_alert=True)
            return
        query.message.edit_text("*COLLECTING DATA*",parse_mode=ParseMode.MARKDOWN)
        buttons=[]
        for k in range(len(list(kingdom_data.keys()))):
            buttons.append([InlineKeyboardButton(f"{kingdom_data[f'kingdom_{k+1}']['name']}",callback_data=f'kingdomjoinextra_back_{k+1}')])
        buttons.append([InlineKeyboardButton(f"BACK",callback_data=f'kingdomjoinextra_back')])
        message=query.message.edit_text("*SELECT THE KINGDOM YOU WANT TO JOIN*",reply_markup=InlineKeyboardMarkup(buttons),parse_mode=ParseMode.MARKDOWN)
        cd=context.chat_data
        message_id = message.message_id
        cd[message_id]={}
        cd[message_id]['user_id']=user.id
        return
    else:
        query.answer("NOT YOUR COMMAND",show_alert=True)
        return

def kingdom_joined(update,context):
    if maintenance_mode == "ON":
        if update.effective_user.id not in admins_id:
            try:
                update.callback_query.message.edit_text("*BOT UNDER MAINTENANCE*",parse_mode=ParseMode.MARKDOWN)
            except:
                update.callback_query.message.edit_caption(caption="*BOT UNDER MAINTENANCE*",parse_mode=ParseMode.MARKDOWN)
            return
    user=update.effective_user
    query=update.callback_query
    cd=context.chat_data
    message_id = query.message.message_id
    try:
        user_id=cd[message_id]['user_id']
    except:
        query.message.edit_text("*THIS COMMAND IS NOW INVALID*",parse_mode=ParseMode.MARKDOWN)
    if user_id==user.id:
        kingdoms=db.get_collection("all_kingdoms")
        kingdom_data = kingdoms.find_one()['kingdom_datas']
        if query.data.split("_")[-1]=="back":
            msg = query.message.edit_text("*LOADING.....*",parse_mode=ParseMode.MARKDOWN)
            text=""
            if len(list(kingdom_data.keys()))<1:
                text+="*NO KINGDOMS FOUND YET*"
            else:
                for i in range(len(list(kingdom_data.keys()))):
                    kingdom=kingdom_data[f'kingdom_{i+1}']
                    text+=f"*{i+1}. {kingdom['name']}\n*`   TOTAL MEMBERS : `*{len(kingdom['members'])}*\n\n"
            keyboard=[[InlineKeyboardButton('ENTER KINGDOM',callback_data=f'kingjoin')]]
            message=query.message.edit_text(f"*KINGOMS : \n\n*"+text,reply_markup=InlineKeyboardMarkup(keyboard),parse_mode=ParseMode.MARKDOWN)
            cd=context.chat_data
            message_id = message.message_id
            cd[message_id]={}
            cd[message_id]['user_id']=user.id
            return
        else:
            all_members=[]
            kings_id=[]
            dukes_id=[]
            for i in range(len(list(kingdom_data.keys()))):
                kingdom_members=kingdom_data[f"kingdom_{i+1}"]['members']
                for j in range(len(kingdom_members)):
                    all_members.append(kingdom_members[j])
                kings_id.append(kingdom_data[f"kingdom_{i+1}"]['KING_DUKE']['KING'])
                dukes_id.append(kingdom_data[f"kingdom_{i+1}"]['KING_DUKE']['DUKE'])
            if user.id in all_members:
                query.answer("YOU'RE ALREADY IN A KINGDOM",show_alert=True)
                return
            elif user.id in kings_id:
                query.answer("YOU'RE THE KING OF A KINGDOM",show_alert=True)
                return
            elif user.id in dukes_id:
                query.answer("YOU'RE THE DUKE OF A KINGDOM",show_alert=True)
                return
            query.message.edit_text("*COLLECTING DATA*",parse_mode=ParseMode.MARKDOWN)
            buttons=[[InlineKeyboardButton(f"ATTACKER 🗡",callback_data=f'Kingdomjoiner-role_atk'),InlineKeyboardButton(f"DEFENDER 🛡",callback_data=f'Kingdomjoiner-role_def')],[InlineKeyboardButton(f"BACK",callback_data=f'kingdomjoinextra_back')]]
            message=query.message.edit_text("*SELECT THE ROLE YOU WANT TO TAKE\nNOTE : REMEMBER THIS ROLE CANNOT BE CHANGED*",reply_markup=InlineKeyboardMarkup(buttons),parse_mode=ParseMode.MARKDOWN)
            message_id = message.message_id
            cd[message_id]={}
            cd[message_id]['user_id']=user.id
            cd[message_id]['kingdom']=int(query.data.split("_")[-1])
            return
    else:
        query.answer("NOT YOUR COMMAND",show_alert=True)
        return

def kingdom(update,context):
    if maintenance_mode == "ON":
        if update.effective_user.id not in admins_id:
            update.message.reply_text("*BOT UNDER MAINTENANCE*",parse_mode=ParseMode.MARKDOWN)
            return
    user=update.message.from_user
    user_data=[db.get_collection("user_datas"),db.get_collection("user_data"),db.get_collection("user_ids"),db.get_collection("beta_users")]
    if user.id in user_data[3].find_one()['beta_players']:
        update.message.reply_text("*SEDLY U R NOT WORTHY TO USE THIS COMMAND*",parse_mode=ParseMode.MARKDOWN)
    else:
        if user.id not in user_data[2].find_one()['user_ids']:
            keyboard=[[InlineKeyboardButton('PM',url='https://t.me/PSO_SoBot?start')]]
            update.message.reply_video(video='https://graph.org/file/e663ce2ffd9c8c32d3247.mp4',caption="*It seems like u haven't started\nClick on the button given below and start the bot*",reply_markup=InlineKeyboardMarkup(keyboard),parse_mode=ParseMode.MARKDOWN)
            return
        user_obj_id = user_data[0].find_one()['user_data'][f'user_{user.id}']
        kingdoms=db.get_collection("all_kingdoms")
        kingdom_data = kingdoms.find_one()['kingdom_datas']
        if update.effective_chat.id != user.id:
            msg = update.message.reply_text("*LOADING.....*",parse_mode=ParseMode.MARKDOWN)
        else:
            msg = update.message.reply_text("*LOADING.....*",parse_mode=ParseMode.MARKDOWN)
        text=""
        if len(list(kingdom_data.keys()))<1:
            text+="*NO KINGDOMS FOUND YET*"
        else:
            for i in range(len(list(kingdom_data.keys()))):
                kingdom=kingdom_data[f'kingdom_{i+1}']
                text+=f"*{i+1}. {kingdom['name']}\n*`   TOTAL MEMBERS : `*{len(kingdom['members'])}*\n\n"
        keyboard=[[InlineKeyboardButton('ENTER KINGDOM',callback_data=f'kingjoin')]]
        for s in range(len(list(kingdom_data.keys()))):
            kingdom_members=kingdom_data[f"kingdom_{s+1}"]['members']
            if user.id in kingdom_members:
                keyboard=[[InlineKeyboardButton('MY KINGDOM',callback_data=f'mykingdom')]]
                message=context.bot.editMessageText(chat_id=update.effective_chat.id, message_id=msg.message_id, text=f"*KINGOMS : \n\n*"+text,reply_markup=InlineKeyboardMarkup(keyboard),parse_mode=ParseMode.MARKDOWN)
                cd=context.chat_data
                message_id = message.message_id
                cd[message_id]={}
                cd[message_id]['user_id']=user.id
                return
            elif user.id == kingdom_data[f"kingdom_{s+1}"]['KING_DUKE']['KING']:
                keyboard=[[InlineKeyboardButton('MY KINGDOM',callback_data=f'mykingdom')]]
                message=context.bot.editMessageText(chat_id=update.effective_chat.id, message_id=msg.message_id, text=f"*KINGOMS : \n\n*"+text,reply_markup=InlineKeyboardMarkup(keyboard),parse_mode=ParseMode.MARKDOWN)
                cd=context.chat_data
                message_id = message.message_id
                cd[message_id]={}
                cd[message_id]['user_id']=user.id
                return
            elif user.id == kingdom_data[f"kingdom_{s+1}"]['KING_DUKE']['DUKE']:
                keyboard=[[InlineKeyboardButton('MY KINGDOM',callback_data=f'mykingdom')]]
                message=context.bot.editMessageText(chat_id=update.effective_chat.id, message_id=msg.message_id, text=f"*KINGOMS : \n\n*"+text,reply_markup=InlineKeyboardMarkup(keyboard),parse_mode=ParseMode.MARKDOWN)
                cd=context.chat_data
                message_id = message.message_id
                cd[message_id]={}
                cd[message_id]['user_id']=user.id
                return
            else:
                print("RUN AGAIN")
        message=context.bot.editMessageText(chat_id=update.effective_chat.id, message_id=msg.message_id, text=f"*KINGOMS : \n\n*"+text,reply_markup=InlineKeyboardMarkup(keyboard),parse_mode=ParseMode.MARKDOWN)
        cd=context.chat_data
        message_id = message.message_id
        cd[message_id]={}
        cd[message_id]['user_id']=user.id
        return

def kingdom_role(update,context):
    if maintenance_mode == "ON":
        if update.effective_user.id not in admins_id:
            try:
                update.callback_query.message.edit_text("*BOT UNDER MAINTENANCE*",parse_mode=ParseMode.MARKDOWN)
            except:
                update.callback_query.message.edit_caption(caption="*BOT UNDER MAINTENANCE*",parse_mode=ParseMode.MARKDOWN)
            return
    user=update.effective_user
    query=update.callback_query
    cd=context.chat_data
    message_id = query.message.message_id
    try:
        user_id=cd[message_id]['user_id']
    except:
        query.message.edit_text("*THIS COMMAND IS NOW INVALID*",parse_mode=ParseMode.MARKDOWN)
        return
    if user_id==user.id:
        kingdoms=db.get_collection("all_kingdoms")
        kingdom_data = kingdoms.find_one()['kingdom_datas']
        all_members=[]
        kings_id=[]
        dukes_id=[]
        for i in range(len(list(kingdom_data.keys()))):
            kingdom_members=kingdom_data[f"kingdom_{i+1}"]['members']
            for j in range(len(kingdom_members)):
                all_members.append(kingdom_members[j])
            kings_id.append(kingdom_data[f"kingdom_{i+1}"]['KING_DUKE']['KING'])
            dukes_id.append(kingdom_data[f"kingdom_{i+1}"]['KING_DUKE']['DUKE'])
        if user.id in all_members:
            query.answer("YOU'RE ALREADY IN A KINGDOM",show_alert=True)
            return
        elif user.id in kings_id:
            query.answer("YOU'RE THE KING OF A KINGDOM",show_alert=True)
            return
        elif user.id in dukes_id:
            query.answer("YOU'RE THE DUKE OF A KINGDOM",show_alert=True)
            return
        user_role={"user_id":user.id,"user_role":f"{query.data.split('_')[-1]}","user_gold":0,"user_silver":10}
        kingdom_id=cd[message_id]['kingdom']
        if kingdom_id == 1 :
            chat_id=-1001812693196
        elif kingdom_id == 2 :
            chat_id=-1001977139712
        user_data=[db.get_collection("user_datas"),db.get_collection("user_data"),db.get_collection("user_ids"),db.get_collection("beta_users")]
        user_obj_id = user_data[0].find_one()['user_data'][f'user_{user.id}']
        user_rank=user_data[1].find_one({'_id': ObjectId(user_obj_id)})['user_info']['rank']
        query.message.edit_text("*REQUEST SEND SUCCESSFULLY\nNOW STAY STILL*",parse_mode=ParseMode.MARKDOWN)
        keyboard=[[InlineKeyboardButton(f"ACCEPT",callback_data=f"kingdoom-accept-{kingdom_id}-{user.id}-{user_role['user_role']}"),InlineKeyboardButton(f"REJECT",callback_data=f"kingdoom-reject-{kingdom_id}-{user.id}-{user_role['user_role']}")]]
        context.bot.send_message(chat_id=chat_id,text=f"`USER ID : `*{user.id}*\n`USER RANK : `*{user_rank}*\n*USER {user.first_name} WANTS TO JOIN {kingdom_data[f'kingdom_{kingdom_id}']['name']}*",reply_markup=InlineKeyboardMarkup(keyboard),parse_mode=ParseMode.MARKDOWN)
        return
    else:
        query.answer("NOT YOUR COMMAND",show_alert=True)
        return

def kingdoom_requester(update,context):
    if maintenance_mode == "ON":
        if update.effective_user.id not in admins_id:
            try:
                update.callback_query.message.edit_text("*BOT UNDER MAINTENANCE*",parse_mode=ParseMode.MARKDOWN)
            except:
                update.callback_query.message.edit_caption(caption="*BOT UNDER MAINTENANCE*",parse_mode=ParseMode.MARKDOWN)
            return
    user=update.effective_user
    query=update.callback_query
    message_id = query.message.message_id
    about_user={"user_id":int(query.data.split("-")[3]),"user_role":query.data.split("-")[4]}
    kingdom_id=query.data.split("-")[2]
    kingdoms=db.get_collection("all_kingdoms")
    kingdom_data = kingdoms.find_one()['kingdom_datas']
    kingdom=kingdom_data[f'kingdom_{kingdom_id}']
    king_and_duke=[1864257459]
    king_and_duke.append(kingdom['KING_DUKE']['KING'])
    king_and_duke.append(kingdom['KING_DUKE']['DUKE'])
    if user.id in king_and_duke :
        if query.data.split("-")[1]=="accept":
            all_members=[]
            for i in range(len(list(kingdom_data.keys()))):
                kingdom_members=kingdom_data[f"kingdom_{i+1}"]['members']
                for j in range(len(kingdom_members)):
                    all_members.append(kingdom_members[j])
            if user.id in all_members:
                query.message.edit_text(f"*USER {about_user['user_id']} ALREADY IN A KINGDOM*",parse_mode=ParseMode.MARKDOWN)
                return
            if len(kingdom_data[f"kingdom_{i+1}"]['members'])>kingdom_data[f"kingdom_{i+1}"]['structural']['houses']-1:
                query.message.edit_text(f"*THERE'S ONLY {kingdom_data[f'kingdom_{i+1}']['structural']['houses']} HOUSES\n FOR {kingdom_data[f'kingdom_{i+1}']['structural']['houses']} MEMBERS*",parse_mode=ParseMode.MARKDOWN)
                return
            user_job={"user_role":about_user["user_role"],"user_gold":0,"user_silver":10,"user_kingdom":f"{kingdom_data[f'kingdom_{kingdom_id}']['name']}"}
            user_data=[db.get_collection("user_datas"),db.get_collection("user_data"),db.get_collection("user_ids"),db.get_collection("beta_users")]
            user_obj_id = user_data[0].find_one()['user_data'][f"user_{about_user['user_id']}"]
            extras=user_data[1].find_one({'_id': ObjectId(user_obj_id)})['extras']
            extras['in_kingdom_data']=user_job
            user_data[1].update_one({"_id":ObjectId(user_obj_id)},{"$set":{'extras':extras}})
            kingdom_data[f"kingdom_{kingdom_id}"]["members"].append(about_user['user_id'])
            kingdom_data[f"kingdom_{kingdom_id}"]["member_role"][f"user_{about_user['user_id']}"]={"user_id":about_user['user_id'],"user_role":about_user["user_role"]}
            kingdoms.update_one({"_id":ObjectId(kingdoms.find_one()['_id'])},{'$set':{'kingdom_datas':kingdom_data}})
            query.message.edit_text(f"*USER {about_user['user_id']} REQUEST ACCEPTED BY {user.first_name}*",parse_mode=ParseMode.MARKDOWN)
            context.bot.send_message(chat_id=about_user['user_id'],text=f"YOUR REQUEST OF JOINING {kingdom['name']} IS ACCEPTED BY {user.first_name}",parse_mode=ParseMode.MARKDOWN)
            return
        else:
            query.message.edit_text(f"*USER {about_user['user_id']} REQUEST REJECTED BY {user.first_name}*",parse_mode=ParseMode.MARKDOWN)
            context.bot.send_message(chat_id=about_user['user_id'],text=f"YOUR REQUEST OF JOINING {kingdom['name']} IS REJECTED BY {user.first_name}",parse_mode=ParseMode.MARKDOWN)
            return
    else:
        query.answer("U R NOT WORTHY",show_alert=True)
        return

def kingdom_joined(update,context):
    if maintenance_mode == "ON":
        if update.effective_user.id not in admins_id:
            try:
                update.callback_query.message.edit_text("*BOT UNDER MAINTENANCE*",parse_mode=ParseMode.MARKDOWN)
            except:
                update.callback_query.message.edit_caption(caption="*BOT UNDER MAINTENANCE*",parse_mode=ParseMode.MARKDOWN)
            return
    user=update.effective_user
    query=update.callback_query
    cd=context.chat_data
    message_id = query.message.message_id
    try:
        user_id=cd[message_id]['user_id']
    except:
        query.message.edit_text("*THIS COMMAND IS NOW INVALID*",parse_mode=ParseMode.MARKDOWN)
    if user_id==user.id:
        kingdoms=db.get_collection("all_kingdoms")
        kingdom_data = kingdoms.find_one()['kingdom_datas']
        if query.data.split("_")[-1]=="back":
            msg = query.message.edit_text("*LOADING.....*",parse_mode=ParseMode.MARKDOWN)
            text=""
            if len(list(kingdom_data.keys()))<1:
                text+="*NO KINGDOMS FOUND YET*"
            else:
                for i in range(len(list(kingdom_data.keys()))):
                    kingdom=kingdom_data[f'kingdom_{i+1}']
                    text+=f"*{i+1}. {kingdom['name']}\n*`   TOTAL MEMBERS : `*{len(kingdom['members'])}*\n\n"
            keyboard=[[InlineKeyboardButton('ENTER KINGDOM',callback_data=f'kingjoin')]]
            for s in range(len(list(kingdom_data.keys()))):
                kingdom_members=kingdom_data[f"kingdom_{s+1}"]['members']
                if user.id in kingdom_members:
                    keyboard=[[InlineKeyboardButton('MY KINGDOM',callback_data=f'mykingdom')]]
                if user.id == kingdom_data[f"kingdom_{s+1}"]['KING_DUKE']['KING']:
                    keyboard=[[InlineKeyboardButton('MY KINGDOM',callback_data=f'mykingdom')]]
                elif user.id == kingdom_data[f"kingdom_{s+1}"]['KING_DUKE']['DUKE']:
                    keyboard=[[InlineKeyboardButton('MY KINGDOM',callback_data=f'mykingdom')]]
            message=query.message.edit_text(f"*KINGOMS : \n\n*"+text,reply_markup=InlineKeyboardMarkup(keyboard),parse_mode=ParseMode.MARKDOWN)
            cd=context.chat_data
            message_id = message.message_id
            cd[message_id]={}
            cd[message_id]['user_id']=user.id
            return
        else:
            all_members=[]
            kings_id=[]
            dukes_id=[]
            for i in range(len(list(kingdom_data.keys()))):
                kingdom_members=kingdom_data[f"kingdom_{i+1}"]['members']
                for j in range(len(kingdom_members)):
                    all_members.append(kingdom_members[j])
                kings_id.append(kingdom_data[f"kingdom_{i+1}"]['KING_DUKE']['KING'])
                dukes_id.append(kingdom_data[f"kingdom_{i+1}"]['KING_DUKE']['DUKE'])
            if user.id in all_members:
                query.answer("YOU'RE ALREADY IN A KINGDOM",show_alert=True)
                return
            elif user.id in kings_id:
                query.answer("YOU'RE THE KING OF A KINGDOM",show_alert=True)
                return
            elif user.id in dukes_id:
                query.answer("YOU'RE THE DUKE OF A KINGDOM",show_alert=True)
                return
            query.message.edit_text("*COLLECTING DATA*",parse_mode=ParseMode.MARKDOWN)
            buttons=[[InlineKeyboardButton(f"ATTACKER 🗡",callback_data=f'Kingdomjoiner-role_atk'),InlineKeyboardButton(f"DEFENDER 🛡",callback_data=f'Kingdomjoiner-role_def')],[InlineKeyboardButton(f"BACK",callback_data=f'kingdomjoinextra_back')]]
            message=query.message.edit_text("*SELECT THE ROLE YOU WANT TO TAKE\nNOTE : REMEMBER THIS ROLE CANNOT BE CHANGED*",reply_markup=InlineKeyboardMarkup(buttons),parse_mode=ParseMode.MARKDOWN)
            message_id = message.message_id
            cd[message_id]={}
            cd[message_id]['user_id']=user.id
            cd[message_id]['kingdom']=int(query.data.split("_")[-1])
            return
    else:
        query.answer("NOT YOUR COMMAND",show_alert=True)
        return

def bag(update,context):
    if maintenance_mode == "ON":
        if update.effective_user.id not in admins_id:
            update.message.reply_text("*BOT UNDER MAINTENANCE*",parse_mode=ParseMode.MARKDOWN)
            return
    user=update.effective_user
    user_data=[db.get_collection("user_datas"),db.get_collection("user_data"),db.get_collection("user_ids"),db.get_collection("beta_users")]
    if user.id in user_data[3].find_one()['beta_players']:
        update.message.reply_text("*SEDLY U R NOT WORTHY TO USE THIS COMMAND*",parse_mode=ParseMode.MARKDOWN)
        return
    else:
        if user.id not in user_data[2].find_one()['user_ids']:
            keyboard=[[InlineKeyboardButton('PM',url='https://t.me/PSO_SoBot?start')]]
            update.message.reply_video(video='https://graph.org/file/e663ce2ffd9c8c32d3247.mp4',caption="*It seems like u haven't started\nClick on the button given below and start the bot*",reply_markup=InlineKeyboardMarkup(keyboard),parse_mode=ParseMode.MARKDOWN)
            return
        user_obj_id = user_data[0].find_one()['user_data'][f'user_{user.id}']
        user_bag=user_data[1].find_one({'_id': ObjectId(user_obj_id)})['bag']
        text = f"*COINS POUCH :*\n\n`USER : `*{user.first_name}*\n\n`🪙 Segils : `*{user_bag['segil']}*\n`❇️ Stargems : `*{user_bag['stargems']}*\n`💠 Primostar : `*{user_bag['primostar']}*\n\n`💳 SHOP CURRENCY :\n💎 Starspliter Gems` : *{user_bag['starspliter_gems']}*\n\n`⚔ TOWER ENERGY : `*{user_bag['tow_en']}*"
        buttons = [[InlineKeyboardButton('Weapons',callback_data=f"bag_weapon_user{user.id}_0"),InlineKeyboardButton('ITEMS',callback_data=f"bag_items_user{user.id}")]]
        update.message.reply_video(video='https://graph.org/file/406cb76e6b0e49d41cca5.mp4',caption=text,reply_markup=InlineKeyboardMarkup(buttons),parse_mode=ParseMode.MARKDOWN)

def fgp(update,context):
    if maintenance_mode == "ON":
        if update.effective_user.id not in admins_id:
            update.message.reply_text("*BOT UNDER MAINTENANCE*",parse_mode=ParseMode.MARKDOWN)
            return
    buttons = [{KeyboardButton("/explore"),KeyboardButton("/back")}]
    chat_id = update.effective_chat.id
    content = "opening...."
    context.bot.send_message(chat_id=chat_id, text = content ,
    reply_markup=ReplyKeyboardMarkup(buttons,resize_keyboard=True))

def fgp_close(update,context):
    if maintenance_mode == "ON":
        if update.effective_user.id not in admins_id:
            update.message.reply_text("*BOT UNDER MAINTENANCE*",parse_mode=ParseMode.MARKDOWN)
            return
    chat_id = update.effective_chat.id
    content= " closed "
    context.bot.send_message(chat_id=chat_id, text = content ,
    reply_markup=ReplyKeyboardRemove())

def gacha(update,context):
    if maintenance_mode == "ON":
        if update.effective_user.id not in admins_id:
            update.message.reply_text("*BOT UNDER MAINTENANCE*",parse_mode=ParseMode.MARKDOWN)
            return
    user=update.effective_user
    if user.id in insiders:
        update.message.reply_text("*You cannot use this while in a Battle *",parse_mode=ParseMode.MARKDOWN)
        return
    user_data=[db.get_collection("user_datas"),db.get_collection("user_data"),db.get_collection("user_ids"),db.get_collection("beta_users")]
    if user.id in user_data[3].find_one()['beta_players']:
        update.message.reply_text("*SEDLY U R NOT WORTHY TO USE THIS COMMAND*",parse_mode=ParseMode.MARKDOWN)
        return
    else:
        if user.id not in user_data[2].find_one()['user_ids']:
            keyboard=[[InlineKeyboardButton('PM',url='https://t.me/PSO_SoBot?start')]]
            update.message.reply_video(video='https://graph.org/file/e663ce2ffd9c8c32d3247.mp4',caption="*It seems like u haven't started\nClick on the button given below and start the bot*",reply_markup=InlineKeyboardMarkup(keyboard),parse_mode=ParseMode.MARKDOWN)
            return
        user_obj_id = user_data[0].find_one()['user_data'][f'user_{user.id}']
        user_bag=user_data[1].find_one({'_id': ObjectId(user_obj_id)})['bag']
        if update.effective_chat.id != user.id:
            keyboard=[[InlineKeyboardButton('PM',url='https://t.me/PSO_SoBot?start=gacha')]]
            update.message.reply_text("*USE  IN  PM  OF  THE  BOT*",reply_markup=InlineKeyboardMarkup(keyboard),parse_mode=ParseMode.MARKDOWN)
            return
        keyboard=[[InlineKeyboardButton('Event Banner 1',callback_data='gacha_event_1'),InlineKeyboardButton('Event Banner 2',callback_data='gacha_event_2')],
                  [InlineKeyboardButton('Standard Banner',callback_data='gacha_standard'),InlineKeyboardButton('Weapon Banner',callback_data='gacha_weapon')],[InlineKeyboardButton('Close',callback_data='gacha_close')]]
        update.message.reply_text("*Select the banner where u would like to pull*",reply_markup=InlineKeyboardMarkup(keyboard),parse_mode=ParseMode.MARKDOWN)
        return

def gacha_selector(update,context):
    if maintenance_mode == "ON":
        if update.effective_user.id not in admins_id:
            try:
                update.callback_query.message.edit_text("*BOT UNDER MAINTENANCE*",parse_mode=ParseMode.MARKDOWN)
            except:
                update.callback_query.message.edit_caption(caption="*BOT UNDER MAINTENANCE*",parse_mode=ParseMode.MARKDOWN)
            return
    user=update.callback_query.from_user
    query=update.callback_query
    if user.id in insiders:
        query.message.edit_text("*You Cannot use this while in a Battle *",parse_mode=ParseMode.MARKDOWN)
        return
    user_data=[db.get_collection("user_datas"),db.get_collection("user_data"),db.get_collection("user_ids"),db.get_collection("beta_users")]
    user_obj_id = user_data[0].find_one()['user_data'][f'user_{user.id}']
    user_bag=user_data[1].find_one({'_id': ObjectId(user_obj_id)})['bag']
    user_gacha_detail=user_data[1].find_one({'_id': ObjectId(user_obj_id)})['gacha_details']
    if 'gacha_standard' in query.data: 
        query.message.delete()
        buttton=[[InlineKeyboardButton('1 PULL',callback_data='gachapull_standard_1'),InlineKeyboardButton('10 PULL',callback_data='gachapull_standard_10')],
                 [InlineKeyboardButton('GACHA Details',callback_data='gacha_close_details_standard')],
                 [InlineKeyboardButton('CLOSE',callback_data='gacha_close_img')]]
        context.bot.send_photo(chat_id=update.effective_chat.id,photo='https://graph.org/file/632127facbb5e30803e84.jpg',
        caption=f"`🪧 Banner Name : `*Warrio Standard Banner*\n`💮 Pity : `*{user_gacha_detail['standard_banner']['gacha_pity']}*\n`❇️ Stargems : `*{user_bag['stargems']}\nPer Spin 120 Stargems*",reply_markup=InlineKeyboardMarkup(buttton),parse_mode=ParseMode.MARKDOWN)
        return GACHA_LUCK
    if 'gacha_event' in query.data: 
        query.message.delete()
        buttton=[[InlineKeyboardButton('1 PULL',callback_data=f"gachapull_event_{query.data.split('_')[-1]}_1"),
                 InlineKeyboardButton('10 PULL',callback_data=f"gachapull_event_{query.data.split('_')[-1]}_10")],
                 [InlineKeyboardButton('GACHA Details',callback_data='gacha_close_details_event')],
                 [InlineKeyboardButton('CLOSE',callback_data='gacha_close_img')]]
        if query.data.split('_')[-1] == "1":
            context.bot.send_photo(chat_id=update.effective_chat.id,photo='https://graph.org/file/25eaad6d7ca09013c2006.jpg',
            caption=f"`🪧 Banner Name : `*TO YOUR ETERNITY*\n`💮 Pity : `*{user_gacha_detail['event_banner']['gacha_pity']}*\n`💠 Primostar : `*{user_bag['primostar']}\nPer Spin 1 Primostar*",reply_markup=InlineKeyboardMarkup(buttton),parse_mode=ParseMode.MARKDOWN)
        else:
            context.bot.send_photo(chat_id=update.effective_chat.id,photo='https://graph.org/file/271eb519044b41db949eb.jpg',
            caption=f"`🪧 Banner Name : `*DIE TWICE*\n`💮 Pity : `*{user_gacha_detail['event_banner']['gacha_pity']}*\n`💠 Primostar : `*{user_bag['primostar']}\nPer Spin 1 Primostar*",reply_markup=InlineKeyboardMarkup(buttton),parse_mode=ParseMode.MARKDOWN)
        return GACHA_LUCK
    if 'gacha_weapon' in query.data:
        query.message.delete()
        buttton=[[InlineKeyboardButton('1 PULL',callback_data='gachapull_weapon_1'),InlineKeyboardButton('10 PULL',callback_data='gachapull_weapon_10')],
                 [InlineKeyboardButton('GACHA Details',callback_data='gacha_close_details_weapon')],
                 [InlineKeyboardButton('CLOSE',callback_data='gacha_close_img')]]
        context.bot.send_photo(chat_id=update.effective_chat.id,photo='https://graph.org/file/a45717ce19551451ec3e4.jpg',
        caption=f"`🪧 Banner Name : `*Eternity of Mortal Sins*\n`💮 Pity : `*{user_gacha_detail['weapon_banner']['gacha_pity']}*\n`💠 Primostar : `*{user_bag['primostar']}\nPer Spin 1 Primostar*",reply_markup=InlineKeyboardMarkup(buttton),parse_mode=ParseMode.MARKDOWN)
        return GACHA_LUCK
    if 'gacha_close' in query.data:
        if query.data.split("_")[-1] == 'img':
            query.message.delete()
            context.bot.send_message(chat_id=update.effective_chat.id,text="*CLOSED*",parse_mode=ParseMode.MARKDOWN)
            return
        if query.data.split("_")[-2] == 'details':
            if query.data.split("_")[-1] == 'event':
                back_button=[[InlineKeyboardButton('BACK',callback_data='gacha_event')],[InlineKeyboardButton('CLOSE',callback_data='gacha_close_img')]]
                query.message.edit_caption(caption="*soon*",reply_markup=InlineKeyboardMarkup(back_button),parse_mode=ParseMode.MARKDOWN)
                return
            if query.data.split("_")[-1] == 'standard':
                back_button=[[InlineKeyboardButton('BACK',callback_data='gacha_standard')],[InlineKeyboardButton('CLOSE',callback_data='gacha_close_img')]]
                query.message.edit_caption(caption="*soon*",reply_markup=InlineKeyboardMarkup(back_button),parse_mode=ParseMode.MARKDOWN)
                return
            if query.data.split("_")[-1] == 'weapon':
                back_button=[[InlineKeyboardButton('BACK',callback_data='gacha_weapon')],[InlineKeyboardButton('CLOSE',callback_data='gacha_close_img')]]
                query.message.edit_caption(caption="*soon*",reply_markup=InlineKeyboardMarkup(back_button),parse_mode=ParseMode.MARKDOWN)
                return
        query.message.edit_text("*Closed*",parse_mode=ParseMode.MARKDOWN)
        return

def gacha_got(update,context):
    if maintenance_mode == "ON":
        if update.effective_user.id not in admins_id:
            try:
                update.callback_query.message.edit_text("*BOT UNDER MAINTENANCE*",parse_mode=ParseMode.MARKDOWN)
            except:
                update.callback_query.message.edit_caption(caption="*BOT UNDER MAINTENANCE*",parse_mode=ParseMode.MARKDOWN)
            return
    user=update.callback_query.from_user
    query=update.callback_query
    if user.id in insiders:
        query.message.edit_caption(caption="*You Cannot use this while in a Battle *",parse_mode=ParseMode.MARKDOWN)
        return
    user_data=[db.get_collection("user_datas"),db.get_collection("user_data"),db.get_collection("user_ids"),db.get_collection("beta_users")]
    user_obj_id = user_data[0].find_one()['user_data'][f'user_{user.id}']
    user_bag=user_data[1].find_one({'_id': ObjectId(user_obj_id)})['bag']
    user_gacha_detail=user_data[1].find_one({'_id': ObjectId(user_obj_id)})['gacha_details']
    user_inside=user_data[1].find_one({'_id': ObjectId(user_obj_id)})['extras']
    user_inside['INSIDE']='IN_GACHA'
    if 'gachapull_standard' in query.data:
        query.message.delete()
        if user_bag['stargems'] < int(query.data.split("_")[-1])*120:
            context.bot.send_message(chat_id=update.effective_chat.id,text=f"*You dont have enough stargems*",parse_mode=ParseMode.MARKDOWN)
            return
        user_starspliter_gems=user_bag['starspliter_gems']
        user_primostar=user_bag['stargems']
        user_weapons=user_data[1].find_one({'_id': ObjectId(user_obj_id)})['weapons']
        user_character=user_data[1].find_one({'_id': ObjectId(user_obj_id)})['user_char']
        user_event_gacha_details=user_gacha_detail['standard_banner']
        user_pity , user_gacha_history = user_event_gacha_details['gacha_pity'] , user_event_gacha_details['gacha_history']        
        user_data[1].update_one({"_id":ObjectId(user_obj_id)},{"$set":{'extras':user_inside}})
        text="*GACHA PULLS*\n"
        for i in range(int(query.data.split("_")[-1])):
            user_primostar=user_primostar-120
            character=playable_character
            char_4_star=char.char_4_star
            weapon_4_star=char.event_rank_4_weapons
            weapon_low_star=char.low_rank_weapons
            random_4_char=random.choices(char_4_star,weights=(40,40,40,40,40,40,40,40,40,40),k=1)[0]
            random_5_char=character[3]
            random_5_weapon=char.rank_5_weapons[0]
            random_low_star=random.choice(weapon_low_star)
            random_4_weapon=random.choice(weapon_4_star)
            if user_pity > 74 and user_pity < 89 :
                total_out=random.choices([random_4_char,random_4_weapon,random_low_star,random_5_weapon,random_5_char],weights=(5,5,80,5,5),k=1)
            if user_pity < 75 :
                total_out=random.choices([random_4_char,random_4_weapon,random_low_star,random_5_weapon,random_5_char],weights=(4.7,4.7,90,0.3,0.3),k=1)
            if user_pity == 89 :
                total_out=random.choices([random_4_char,random_4_weapon,random_low_star,random_5_weapon,random_5_char],weights=(0,0,0,100,100),k=1)
            if list(total_out[0].keys())[0] == 'weapon_name':
                user_starspliter_gems=user_starspliter_gems+20
                user_weapons.append(total_out[0])
                if list(total_out[0].values())[0] == 'Molten Gauntlets':
                    user_starspliter_gems=user_starspliter_gems+10
                    user_pity=0
                    user_pity-=1
                    user_gacha_history=[]
                for_ex = context.bot.send_message(chat_id=update.effective_chat.id,text=f"You got {list(total_out[0].values())[0]}",parse_mode=ParseMode.MARKDOWN)
                time.sleep(0.6)
                text +=f"`{list(total_out[0].values())[0]} (weapon)\n`"
            if list(total_out[0].keys())[0] == 'name':
                n=None
                for i in range(len(user_character)):
                    if  user_character[i]['name'] == list(total_out[0].values())[0]:
                        n=i  
                if n != None:
                    the_character=user_character[n]
                    if the_character['constellation']==6:
                        the_character['constellation']-=1
                    the_character['constellation']+=1
                    user_character.insert(n,the_character)
                    user_character.pop(n)       
                if n == None:
                    user_character.append(total_out[0])
                if total_out[0]['rank'] == 5:
                    user_starspliter_gems=user_starspliter_gems+40
                    user_pity=0
                    user_pity-=1
                    user_gacha_history=[]
                    for_ex = context.bot.send_video(chat_id=update.effective_chat.id,video=total_out[0]['video'],caption=f"You got {list(total_out[0].values())[0]}",parse_mode=ParseMode.MARKDOWN)
                    time.sleep(1)
                if total_out[0]['rank'] == 4:
                    user_starspliter_gems=user_starspliter_gems+30
                    for_ex = context.bot.send_photo(chat_id=update.effective_chat.id,photo=total_out[0]['photo'],caption=f"You got {list(total_out[0].values())[0]}",parse_mode=ParseMode.MARKDOWN)
                    time.sleep(0.8)
                text +=f"`{list(total_out[0].values())[0]} (character)\n`" 
            user_pity+=1
            user_gacha_history.append(list(total_out[0].values())[0])
            context.bot.delete_message(chat_id=for_ex.chat_id, message_id=for_ex.message_id)
        user_bag['stargems']=user_primostar
        user_bag['starspliter_gems']=user_starspliter_gems
        user_event_gacha_details['gacha_pity']=user_pity
        user_event_gacha_details['gacha_history']=user_gacha_history
        user_ba_checkerg=user_data[1].find_one({'_id': ObjectId(user_obj_id)})['bag']
        if user_ba_checkerg['stargems']<int(query.data.split("_")[-1])*120:
            user_inside['INSIDE']='NOPE'
            user_data[1].update_one({"_id":ObjectId(user_obj_id)},{"$set":{'extras':user_inside}})
            context.bot.send_message(chat_id=update.effective_chat.id,text=f"*It seems like user : {user.first_name} trying to heck the bot\nSEDLy u cant due to higher secondary Protection",parse_mode=ParseMode.MARKDOWN)
            return
        user_ba_checkerg['stargems']-=int(query.data.split("_")[-1])*120
        if user_ba_checkerg['stargems']!=user_bag['stargems']:
            user_data[1].update_one({"_id":ObjectId(user_obj_id)},{"$set":{'bag':user_ba_checkerg}})
        else:
            user_data[1].update_one({"_id":ObjectId(user_obj_id)},{"$set":{'bag':user_bag}})
        user_data[1].update_one({"_id":ObjectId(user_obj_id)},{"$set":{'gacha_details':user_gacha_detail}})
        user_data[1].update_one({"_id":ObjectId(user_obj_id)},{"$set":{'weapons':user_weapons}})
        user_data[1].update_one({"_id":ObjectId(user_obj_id)},{"$set":{'user_char':user_character}})
        context.bot.send_message(chat_id=update.effective_chat.id,text=text,parse_mode=ParseMode.MARKDOWN)
        user_inside['INSIDE']='NOPE'
        user_data[1].update_one({"_id":ObjectId(user_obj_id)},{"$set":{'extras':user_inside}})
        return
    if 'gachapull_event' in query.data:
        query.message.delete()
        if user_bag['primostar'] < int(query.data.split("_")[-1]):
            context.bot.send_message(chat_id=update.effective_chat.id,text=f"*You dont have enough primostars*",parse_mode=ParseMode.MARKDOWN)
            return
        user_starspliter_gems=user_bag['starspliter_gems']
        user_primostar=user_bag['primostar']
        user_weapons=user_data[1].find_one({'_id': ObjectId(user_obj_id)})['weapons']
        user_character=user_data[1].find_one({'_id': ObjectId(user_obj_id)})['user_char']
        user_event_gacha_details=user_gacha_detail['event_banner']
        user_pity , user_gacha_history = user_event_gacha_details['gacha_pity'] , user_event_gacha_details['gacha_history']
        user_data[1].update_one({"_id":ObjectId(user_obj_id)},{"$set":{'extras':user_inside}})
        text="*GACHA PULLS*\n"
        for i in range(int(query.data.split("_")[-1])):
            user_primostar=user_primostar-1
            character=playable_character
            char_4_star=char.char_4_star
            weapon_4_star=char.event_rank_4_weapons
            weapon_low_star=char.low_rank_weapons
            random_4_char=random.choices(char_4_star,weights=(10,10,10,10,10,10,10,30,30,30),k=1)[0]
            if int(query.data.split("_")[-2]) == 1 :
                random_5_char=char.raiden_char
            else:
                random_5_char=char.sekiro_char
            random_low_star=random.choice(weapon_low_star)
            random_4_weapon=random.choice(weapon_4_star)
            if user_pity > 74 and user_pity < 89 :
                total_out=random.choices([random_4_char,random_4_weapon,random_low_star,random_5_char],weights=(7,3,80,10),k=1)
            if user_pity < 75 :
                total_out=random.choices([random_4_char,random_4_weapon,random_low_star,random_5_char],weights=(6,3.4,90,0.6),k=1)
            if user_pity == 89:
                total_out=random.choices([random_4_char,random_4_weapon,random_low_star,random_5_char],weights=(0,0,0,100),k=1)
            if list(total_out[0].keys())[0] == 'weapon_name':
                user_starspliter_gems=user_starspliter_gems+20
                user_weapons.append(total_out[0])
                for_ex = context.bot.send_message(chat_id=update.effective_chat.id,text=f"You got {list(total_out[0].values())[0]}",parse_mode=ParseMode.MARKDOWN)
                time.sleep(0.6)
                text +=f"`{list(total_out[0].values())[0]} (weapon)\n`"
            if list(total_out[0].keys())[0] == 'name':
                n=None
                for i in range(len(user_character)):
                    if  user_character[i]['name'] == list(total_out[0].values())[0]:
                        n=i  
                if n != None:
                    the_character=user_character[n]
                    if the_character['constellation']==6:
                        the_character['constellation']-=1
                    the_character['constellation']+=1
                    user_character.insert(n,the_character)
                    user_character.pop(n)       
                if n == None:
                    user_character.append(total_out[0])
                if total_out[0]['rank'] == 5:
                    user_starspliter_gems=user_starspliter_gems+40
                    user_pity=0
                    user_pity-=1
                    user_gacha_history=[]
                    for_ex = context.bot.send_video(chat_id=update.effective_chat.id,video=total_out[0]['video'],caption=f"You got {list(total_out[0].values())[0]}",parse_mode=ParseMode.MARKDOWN)
                    time.sleep(1)
                if total_out[0]['rank'] == 4:
                    user_starspliter_gems=user_starspliter_gems+30
                    for_ex = context.bot.send_photo(chat_id=update.effective_chat.id,photo=total_out[0]['photo'],caption=f"You got {list(total_out[0].values())[0]}",parse_mode=ParseMode.MARKDOWN)
                    time.sleep(0.8)
                text +=f"`{list(total_out[0].values())[0]} (character)\n`" 
            user_pity+=1
            user_gacha_history.append(list(total_out[0].values())[0])
            context.bot.delete_message(chat_id=for_ex.chat_id, message_id=for_ex.message_id)
        user_bag['primostar']=user_primostar
        user_bag['starspliter_gems']=user_starspliter_gems
        user_event_gacha_details['gacha_pity']=user_pity
        user_event_gacha_details['gacha_history']=user_gacha_history
        user_bag_checker=user_data[1].find_one({'_id': ObjectId(user_obj_id)})['bag']
        if user_bag_checker['primostar']<int(query.data.split("_")[-1]):
            user_inside['INSIDE']='NOPE'
            user_data[1].update_one({"_id":ObjectId(user_obj_id)},{"$set":{'extras':user_inside}})
            context.bot.send_message(chat_id=update.effective_chat.id,text=f"*It seems like user : {user.first_name} trying to heck the bot\nSEDLy u cant due to higher secondary Protection",parse_mode=ParseMode.MARKDOWN)
            return
        user_bag_checker['primostar']-=int(query.data.split("_")[-1])
        if user_bag_checker['primostar']!=user_bag['primostar']:
            user_data[1].update_one({"_id":ObjectId(user_obj_id)},{"$set":{'bag':user_bag_checker}})
        else:
            user_data[1].update_one({"_id":ObjectId(user_obj_id)},{"$set":{'bag':user_bag}})
        user_data[1].update_one({"_id":ObjectId(user_obj_id)},{"$set":{'gacha_details':user_gacha_detail}})
        user_data[1].update_one({"_id":ObjectId(user_obj_id)},{"$set":{'weapons':user_weapons}})
        user_data[1].update_one({"_id":ObjectId(user_obj_id)},{"$set":{'user_char':user_character}})
        context.bot.send_message(chat_id=update.effective_chat.id,text=text,parse_mode=ParseMode.MARKDOWN)
        user_inside['INSIDE']='NOPE'
        user_data[1].update_one({"_id":ObjectId(user_obj_id)},{"$set":{'extras':user_inside}})
        return
    if 'gachapull_weapon' in query.data:
        query.message.delete()
        if user_bag['primostar'] < int(query.data.split("_")[-1]):
            context.bot.send_message(chat_id=update.effective_chat.id,text=f"*You dont have enough primostars*",parse_mode=ParseMode.MARKDOWN)
            return
        user_starspliter_gems=user_bag['starspliter_gems']
        user_primostar=user_bag['primostar']
        user_weapons=user_data[1].find_one({'_id': ObjectId(user_obj_id)})['weapons']
        user_event_gacha_details=user_gacha_detail['weapon_banner']
        user_pity , user_gacha_history = user_event_gacha_details['gacha_pity'] , user_event_gacha_details['gacha_history']
        user_data[1].update_one({"_id":ObjectId(user_obj_id)},{"$set":{'extras':user_inside}})
        text="*GACHA PULLS*\n"
        for i in range(int(query.data.split("_")[-1])):
            user_primostar=user_primostar-1
            weapon_4_star=char.event_rank_4_weapons
            weapon_low_star=char.low_rank_weapons
            random_5_weapon=random.choice([char.rank_5_weapons[3],char.rank_5_weapons[4]])
            random_low_star=random.choice(weapon_low_star)
            random_4_weapon=random.choices(weapon_4_star,weights=(20,20,20,20,20,20,40,40,40),k=1)
            if user_pity > 74 and user_pity < 89 :
                total_out=random.choices([random_4_weapon[0],random_low_star,random_5_weapon],weights=(5,85,10),k=1)
            if user_pity < 75 :
                total_out=random.choices([random_4_weapon[0],random_low_star,random_5_weapon],weights=(9.4,90,0.6),k=1)
            if user_pity == 89 :
                total_out=random.choices([random_4_weapon[0],random_low_star,random_5_weapon],weights=(0,0,100),k=1)
            if list(total_out[0].keys())[0] == 'weapon_name':
                user_starspliter_gems=user_starspliter_gems+20
                user_weapons.append(total_out[0])
                if list(total_out[0].values())[0] == 'Engulfing Lightning' or list(total_out[0].values())[0] == 'Mortal Blade' :
                    user_starspliter_gems=user_starspliter_gems+10
                    user_pity=0
                    user_pity-=1
                    user_gacha_history=[]
                    for_ex_1= context.bot.send_message(chat_id=update.effective_chat.id,text=f"🌟",parse_mode=ParseMode.MARKDOWN)
                    time.sleep(1)                    
                for_ex = context.bot.send_message(chat_id=update.effective_chat.id,text=f"You got {list(total_out[0].values())[0]}",parse_mode=ParseMode.MARKDOWN)
                text +=f"`{list(total_out[0].values())[0]} (weapon)\n`"
                time.sleep(0.6)
            user_pity+=1
            user_gacha_history.append(list(total_out[0].values())[0])
            context.bot.delete_message(chat_id=for_ex.chat_id, message_id=for_ex.message_id)
        user_bag['primostar']=user_primostar
        user_bag['starspliter_gems']=user_starspliter_gems
        user_event_gacha_details['gacha_pity']=user_pity
        user_event_gacha_details['gacha_history']=user_gacha_history
        user_bag_checker=user_data[1].find_one({'_id': ObjectId(user_obj_id)})['bag']
        if user_bag_checker['primostar']<int(query.data.split("_")[-1]):
            context.bot.send_message(chat_id=update.effective_chat.id,text=f"*It seems like user : {user.first_name} trying to heck the bot\nSEDLy u cant due to higher secondary Protection",parse_mode=ParseMode.MARKDOWN)
            user_inside['INSIDE']='NOPE'
            user_data[1].update_one({"_id":ObjectId(user_obj_id)},{"$set":{'extras':user_inside}})
            return
        else:
            user_bag_checker['primostar']-=int(query.data.split("_")[-1])
            if user_bag_checker['primostar']!=user_bag['primostar']:
                user_data[1].update_one({"_id":ObjectId(user_obj_id)},{"$set":{'bag':user_bag_checker}})
            else:
                user_data[1].update_one({"_id":ObjectId(user_obj_id)},{"$set":{'bag':user_bag}})
            user_data[1].update_one({"_id":ObjectId(user_obj_id)},{"$set":{'bag':user_bag}})
            user_data[1].update_one({"_id":ObjectId(user_obj_id)},{"$set":{'gacha_details':user_gacha_detail}})
            user_data[1].update_one({"_id":ObjectId(user_obj_id)},{"$set":{'weapons':user_weapons}})
            context.bot.send_message(chat_id=update.effective_chat.id,text=text,parse_mode=ParseMode.MARKDOWN)
            user_inside['INSIDE']='NOPE'
            user_data[1].update_one({"_id":ObjectId(user_obj_id)},{"$set":{'extras':user_inside}})
            return

def bag_cmd(update,context):
    if maintenance_mode == "ON":
        if update.effective_user.id not in admins_id:
            try:
                update.callback_query.message.edit_text("*BOT UNDER MAINTENANCE*",parse_mode=ParseMode.MARKDOWN)
            except:
                update.callback_query.message.edit_caption(caption="*BOT UNDER MAINTENANCE*",parse_mode=ParseMode.MARKDOWN)
            return
    user=update.callback_query.from_user
    query = update.callback_query.data
    if user.id in insiders:
        query.message.edit_caption(caption="*You Cannot use this while in a Battle *",parse_mode=ParseMode.MARKDOWN)
        return
    split_data=query.split("_")[0]
    update.callback_query.answer()
    beta_user=beta_collection.find_one()['beta_players']
    if "bag" in split_data:
        if "weapon" in query.split("_")[1]:
            user=update.callback_query.from_user
            user_data=[db.get_collection("user_datas"),db.get_collection("user_data"),db.get_collection("user_ids"),db.get_collection("beta_users")]
            if f"user{user.id}" != query.split("_")[2]:
                query1=update.callback_query
                query1.answer("You are not bag owner", show_alert = True)
                return
            user_obj_id = user_data[0].find_one()['user_data'][f'user_{user.id}']
            user_weapons=user_data[1].find_one({'_id':ObjectId(user_obj_id)})['weapons']
            weapon_name=f"`Total Weapons : {len(user_weapons)}\nWeapon List : `\n\n"
            n=int(query.split("_")[-1])
            m=int(query.split("_")[-1])
            if len(user_weapons)-n < 21:
                for i in range(len(user_weapons)-n):
                    weapon_name+=f"*{m+1}. {user_weapons[m]['weapon_name']} • {user_weapons[m]['buff_atk']}\n*"
                    m=m+1
                weapon_name+="\n*Weapons attack buff values are given side by side of the weapons*"
                cd=context.chat_data
                buttons=[[InlineKeyboardButton('Pouch',callback_data =f"bag_pouch_user{user.id}"),InlineKeyboardButton('Items',callback_data=f"bag_items_user{user.id}")],[InlineKeyboardButton('SMELT WEAPON',callback_data=f"bag_WEponsmlt")]]
                update.callback_query.message.edit_caption(caption=weapon_name,reply_markup=InlineKeyboardMarkup(buttons),parse_mode=ParseMode.MARKDOWN)
                return
            if len(user_weapons)-n > 20:
                for i in range(20):
                    weapon_name+=f"*{m+1}. {user_weapons[m]['weapon_name']} • {user_weapons[m]['buff_atk']}\n*"
                    m=m+1
                weapon_name+="\n*Weapons attack buff values are given side by side of the weapons*"
                cd=context.chat_data
                buttons=[[InlineKeyboardButton('NEXT',callback_data =f"bag_weapon_user{user.id}_{m}")],[InlineKeyboardButton('Pouch',callback_data =f"bag_pouch_user{user.id}"),InlineKeyboardButton('Items',callback_data=f"bag_items_user{user.id}")],[InlineKeyboardButton('SMELT WEAPON',callback_data=f"bag_WEponsmlt")]]
                update.callback_query.message.edit_caption(caption=weapon_name,reply_markup=InlineKeyboardMarkup(buttons),parse_mode=ParseMode.MARKDOWN)
                return
        if "pouch" in query.split("_")[1]:
            user=update.callback_query.from_user
            if f"user{user.id}" != query.split("_")[2]:
                query1=update.callback_query
                query1.answer("You are not bag owner", show_alert = True)
                return
            user_data=[db.get_collection("user_datas"),db.get_collection("user_data"),db.get_collection("user_ids"),db.get_collection("beta_users")]
            user_obj_id = user_data[0].find_one()['user_data'][f'user_{user.id}']
            user_bag=user_data[1].find_one({'_id': ObjectId(user_obj_id)})['bag']
            text = f"*COINS POUCH :*\n\n`USER : `*{user.first_name}*\n\n`🪙 Segils : `*{user_bag['segil']}*\n`❇️ Stargems : `*{user_bag['stargems']}*\n`💠 Primostar : `*{user_bag['primostar']}*\n\n`💳 SHOP CURRENCY :\n💎 Starspliter Gems` : *{user_bag['starspliter_gems']}*\n\n`⚔ TOWER ENERGY : `*{user_bag['tow_en']}*"
            buttons = [[InlineKeyboardButton('Weapons',callback_data=f"bag_weapon_user{user.id}_0"),InlineKeyboardButton('ITEMS',callback_data=f"bag_items_user{user.id}")]]
            update.callback_query.message.edit_caption(caption=text,reply_markup=InlineKeyboardMarkup(buttons),parse_mode=ParseMode.MARKDOWN)
        if "items" in query.split("_")[1]:
            user=update.callback_query.from_user
            if f"user{user.id}" != query.split("_")[2]:
                query1=update.callback_query
                query1.answer("You are not bag owner", show_alert = True)
                return
            user_data=[db.get_collection("user_datas"),db.get_collection("user_data"),db.get_collection("user_ids"),db.get_collection("beta_users")]
            user_obj_id = user_data[0].find_one()['user_data'][f'user_{user.id}']
            user_items=user_data[1].find_one({'_id': ObjectId(user_obj_id)})['bag']
            user_bag_items_len=len(user_items)-5
            if user_bag_items_len>0:
                text="`YOUR ITEMS : `\n\n"
                for i in range(user_bag_items_len):
                    try:
                        user_item_key=list(user_items.keys())[i+5].split("users_")[1]
                    except:
                        user_item_key=list(user_items.keys())[i+5].split("user_")[1]
                    user_item_value=list(user_items.values())[i+5]
                    text+=f"`{user_item_key.upper()} : `*{user_item_value}*\n"
            else:
                text='*YOU DON"T HAVE ANYTHING TO SHOW*'
            buttons=[[InlineKeyboardButton('Pouch',callback_data =f"bag_pouch_user{user.id}"),InlineKeyboardButton('Weapons',callback_data=f"bag_weapon_user{user.id}_0")]]
            update.callback_query.message.edit_caption(caption=text,reply_markup=InlineKeyboardMarkup(buttons),parse_mode=ParseMode.MARKDOWN)
            return
        if "WEponsmlt" in query.split("_")[1]:
            chat=update.effective_chat
            user=update.callback_query.from_user
            user_data=[db.get_collection("user_datas"),db.get_collection("user_data"),db.get_collection("user_ids"),db.get_collection("beta_users")]
            user_obj_id = user_data[0].find_one()['user_data'][f'user_{user.id}']
            user_inside=user_data[1].find_one({'_id': ObjectId(user_obj_id)})['extras']
            if user_inside['INSIDE'].split("_")[0] == 'IN':
                update.message.reply_text(f"*You're currently using {user_inside['INSIDE'].split('_')[1]}*",parse_mode=ParseMode.MARKDOWN)
                return
            elif chat.id==user.id:
                cd=context.chat_data
                buttons=[[InlineKeyboardButton('ENTER',callback_data =f"smelt_weapon_0")],[InlineKeyboardButton('BACK',callback_data =f"bag_weapon_user{user.id}_0")]]
                message=update.callback_query.message.edit_caption(caption="ENTER WEAPON SMELTER ?",reply_markup=InlineKeyboardMarkup(buttons),parse_mode=ParseMode.MARKDOWN)
                cd.clear()
                message_id = message.message_id
                cd[message_id] = {}
                cd[message_id]['user']=user
                cd[message_id]['user_ob_id']=user_obj_id
                return
            elif chat.id!=user.id:
                query=update.callback_query
                buttons=[[InlineKeyboardButton('BACK',callback_data =f"bag_weapon_user{user.id}_0")]]
                query.message.edit_caption(caption='*USE IN BOT PM*',reply_markup=InlineKeyboardMarkup(buttons),parse_mode=ParseMode.MARKDOWN)
                return

def smelt_weapon(update,context):
    if maintenance_mode == "ON":
        if update.effective_user.id not in admins_id:
            try:
                update.callback_query.message.edit_text("*BOT UNDER MAINTENANCE*",parse_mode=ParseMode.MARKDOWN)
            except:
                update.callback_query.message.edit_caption(caption="*BOT UNDER MAINTENANCE*",parse_mode=ParseMode.MARKDOWN)
            return
    query=update.callback_query
    user=query.from_user
    chat=update.effective_chat
    if user.id == chat.id :
        cd=context.chat_data
        user_data_collections = [db.get_collection("user_datas"),db.get_collection("user_data"),db.get_collection("user_ids"),db.get_collection("beta_users")]
        message_id = query.message.message_id
        try:
            user_obj_id =cd[message_id]['user_ob_id']
        except:
            query.answer("GEY INVALID")
        fukin_user=cd[message_id]['user_ob_id']
        weapon_num = user_data_collections[1].find_one({'_id': ObjectId(user_obj_id)})['weapons']
        keyboard1, keyboard2, keyboard3, keyboard4 = [[]], [[], []], [[], [], []], [[], [], [], []]
        n = int(query.data.split("_")[-1])
        m = int(query.data.split("_")[-1])
        weapons_list = f"`SMELTABLE Weapons : `\n\n"
        update.callback_query.message.delete()
        if len(weapon_num)-m > 20:
            for i in range(20):
                L = user_data_collections[1].find_one({'_id': ObjectId(user_obj_id)})['weapons'][n]
                weapons_list += f"*{n+1}. {L['weapon_name']}\n*"
                if len(weapon_num)-m > 0 and len(weapon_num)-m < 6:
                    keyboard1[0].append(InlineKeyboardButton(f'{n+1}',callback_data=f"SMELTWEAPON-{n}"))
                if len(weapon_num)-m > 5 and len(weapon_num)-m < 11:
                    if n < 5+m :
                        keyboard2[0].append(InlineKeyboardButton(f'{n+1}',callback_data=f"SMELTWEAPON-{n}"))
                    if n > 4+m :
                        keyboard2[1].append(InlineKeyboardButton(f'{n+1}',callback_data=f"SMELTWEAPON-{n}"))
                elif len(weapon_num)-m > 10 and len(weapon_num)-m < 16:
                    if n < 5+m :
                        keyboard3[0].append(InlineKeyboardButton(f'{n+1}',callback_data=f"SMELTWEAPON-{n}"))
                    if n > 4+m and n < 10+m :
                        keyboard3[1].append(InlineKeyboardButton(f'{n+1}',callback_data=f"SMELTWEAPON-{n}"))
                    if n > 9+m :
                        keyboard3[2].append(InlineKeyboardButton(f'{n+1}',callback_data=f"SMELTWEAPON-{n}"))
                else:
                    if n < 5+m :
                        keyboard4[0].append(InlineKeyboardButton(f'{n+1}',callback_data=f"SMELTWEAPON-{n}"))
                    if n > 4+m and n < 10+m :
                        keyboard4[1].append(InlineKeyboardButton(f'{n+1}',callback_data=f"SMELTWEAPON-{n}"))
                    if n > 9+m and n < 15+m :
                        keyboard4[2].append(InlineKeyboardButton(f'{n+1}',callback_data=f"SMELTWEAPON-{n}"))
                    if n > 14+m : 
                        keyboard4[3].append(InlineKeyboardButton(f'{n+1}',callback_data=f"SMELTWEAPON-{n}"))
                n=n+1
            if len(weapon_num)-m > 0 and len(weapon_num)-m < 6:
                keyboard=keyboard1
            elif len(weapon_num)-m > 5 and len(weapon_num)-m < 11:
                keyboard=keyboard2
            elif len(weapon_num)-m > 10 and len(weapon_num)-m < 16:
                keyboard=keyboard3
            else:
                keyboard=keyboard4
            keyboard4.append([(InlineKeyboardButton('CLOSE', callback_data='smelter_close'))])
            keyboard4.append([(InlineKeyboardButton('NEXT', callback_data=f"smelt_weapon_{n}"))])
            keyboard = keyboard4
            message = context.bot.send_message(chat_id=update.effective_chat.id, text=weapons_list, reply_markup=InlineKeyboardMarkup(keyboard), parse_mode=ParseMode.MARKDOWN)
            message_id = message.message_id
            cd[message_id] = {}
            cd[message_id]['user_ob_id'] = user_obj_id
            cd[message_id]['user'] = user
            return
        if len(weapon_num)-m < 21:
            for i in range(len(weapon_num)-m):
                L=user_data_collections[1].find_one({'_id': ObjectId(user_obj_id)})['weapons'][n]
                weapons_list+=f"*{n+1}. {L['weapon_name']}\n*"
                if len(weapon_num)-m > 0 and len(weapon_num)-m < 6:
                    keyboard1[0].append(InlineKeyboardButton(f'{n+1}',callback_data=f"SMELTWEAPON-{n}"))
                if len(weapon_num)-m > 5 and len(weapon_num)-m < 11:
                    if n < 5+m :
                        keyboard2[0].append(InlineKeyboardButton(f'{n+1}',callback_data=f"SMELTWEAPON-{n}"))
                    if n > 4+m :
                        keyboard2[1].append(InlineKeyboardButton(f'{n+1}',callback_data=f"SMELTWEAPON-{n}"))
                elif len(weapon_num)-m > 10 and len(weapon_num)-m < 16:
                    if n < 5+m :
                        keyboard3[0].append(InlineKeyboardButton(f'{n+1}',callback_data=f"SMELTWEAPON-{n}"))
                    if n > 4+m and n < 10+m :
                        keyboard3[1].append(InlineKeyboardButton(f'{n+1}',callback_data=f"SMELTWEAPON-{n}"))
                    if n > 9+m :
                        keyboard3[2].append(InlineKeyboardButton(f'{n+1}',callback_data=f"SMELTWEAPON-{n}"))
                else:
                    if n < 5+m :
                        keyboard4[0].append(InlineKeyboardButton(f'{n+1}',callback_data=f"SMELTWEAPON-{n}"))
                    if n > 4+m and n < 10+m :
                        keyboard4[1].append(InlineKeyboardButton(f'{n+1}',callback_data=f"SMELTWEAPON-{n}"))
                    if n > 9+m and n < 15+m :
                        keyboard4[2].append(InlineKeyboardButton(f'{n+1}',callback_data=f"SMELTWEAPON-{n}"))
                    if n > 14+m and n < 21+m :
                        keyboard4[3].append(InlineKeyboardButton(f'{n+1}',callback_data=f"SMELTWEAPON-{n}"))
                n=n+1
            if len(weapon_num)-m > 0 and len(weapon_num)-m < 6:
                keyboard=keyboard1
            elif len(weapon_num)-m > 5 and len(weapon_num)-m < 11:
                keyboard=keyboard2
            elif len(weapon_num)-m > 10 and len(weapon_num)-m < 16:
                keyboard=keyboard3
            else:
                keyboard=keyboard4
            keyboard.append([(InlineKeyboardButton('CLOSE', callback_data='smelter_close'))])
            message = context.bot.send_message(chat_id=update.effective_chat.id, text=weapons_list, reply_markup=InlineKeyboardMarkup(keyboard), parse_mode=ParseMode.MARKDOWN)
            message_id = message.message_id
            cd[message_id] = {}
            cd[message_id]['user_ob_id'] = user_obj_id
            cd[message_id]['user'] = user
            return 
    else:
        query.answer("THIS IS NOT UR BAG GEY",show_alert=True)
        return

def smelting_place(update,context):
    if maintenance_mode == "ON":
        if update.effective_user.id not in admins_id:
            try:
                update.callback_query.message.edit_text("*BOT UNDER MAINTENANCE*",parse_mode=ParseMode.MARKDOWN)
            except:
                update.callback_query.message.edit_caption(caption="*BOT UNDER MAINTENANCE*",parse_mode=ParseMode.MARKDOWN)
            return
    query=update.callback_query
    user=query.from_user
    cd=context.chat_data
    message_id=query.message.message_id
    user_obj_id=cd[message_id]['user_ob_id']
    poping_weapon_id=query.data.split("-")[-1]
    button=[[InlineKeyboardButton("CONFIRM",callback_data='smelter_CONFIRMED')],[InlineKeyboardButton("CLOSE",callback_data='smelter_close')]]
    query.message.edit_text("*ARE SURE U WANT TO REMOVE THE WEAPON ?*",reply_markup=InlineKeyboardMarkup(button),parse_mode=ParseMode.MARKDOWN)
    cd[message_id]['poping_weapon_id']=poping_weapon_id
    cd[message_id]['user_ob_id']=user_obj_id
    return

def smelting(update,context):
    if maintenance_mode == "ON":
        if update.effective_user.id not in admins_id:
            try:
                update.callback_query.message.edit_text("*BOT UNDER MAINTENANCE*",parse_mode=ParseMode.MARKDOWN)
            except:
                update.callback_query.message.edit_caption(caption="*BOT UNDER MAINTENANCE*",parse_mode=ParseMode.MARKDOWN)
            return
    query=update.callback_query
    user=query.from_user
    if query.data.split("_")[-1].lower()=='close':
        query.message.edit_text("*CLOSED*",parse_mode=ParseMode.MARKDOWN)
        return
    elif query.data.split("_")[-1].lower()=='confirmed':
        cd=context.chat_data
        message_id=query.message.message_id
        user_data_collections = [db.get_collection("user_datas"),db.get_collection("user_data"),db.get_collection("user_ids"),db.get_collection("beta_users")]
        user_obj_id=cd[message_id]['user_ob_id']
        user_weapons=user_data_collections[1].find_one({'_id': ObjectId(user_obj_id)})['weapons']
        pop_id=int(cd[message_id]['poping_weapon_id'])
        user_bag=user_data_collections[1].find_one({'_id': ObjectId(user_obj_id)})['bag']
        try:
            user_iron=user_bag['users_iron']
            user_steel=user_bag['users_steel']
        except:
            user_bag['users_iron']=0
            user_bag['users_steel']=0
            user_iron=user_bag['users_iron']
            user_steel=user_bag['users_steel']
        if user_weapons[pop_id] in char.low_rank_weapons:
            metal_type=['iron','steel']
            random_metal=random.choices(metal_type,weights=(20,80),k=1)
            if random_metal[0]=='iron':
                rnd_res=random.choice([1,2,3])
                user_iron+=rnd_res
                user_bag['users_iron']=user_iron
            elif random_metal[0]=='steel':
                rnd_res=random.choice([4,5,6,7,8])
                user_steel+=rnd_res
                user_bag['users_steel']=user_steel
        elif user_weapons[pop_id] in char.rank_4_weapons:
            metal_type=['iron','steel']
            random_metal=random.choices(metal_type,weights=(40,60),k=1)
            if random_metal[0]=='iron':
                rnd_res=random.choice([4,5,6])
                user_iron+=rnd_res
                user_bag['users_iron']=user_iron
            elif random_metal[0]=='steel':
                rnd_res=random.choice([6,7,8,9,10])
                user_steel+=rnd_res
                user_bag['users_steel']=user_steel
        elif user_weapons[pop_id] in char.rank_5_weapons:
            metal_type=['iron','steel']
            random_metal=random.choices(metal_type,weights=(50,50),k=1)
            if random_metal[0]=='iron':
                rnd_res=random.choice([8,9,10])
                user_iron+=rnd_res
                user_bag['users_iron']=user_iron
            elif random_metal[0]=='steel':
                rnd_res=random.choice([10,12,14,15,20])
                user_steel+=rnd_res
                user_bag['users_steel']=user_steel
        else:
            print('gey')
        user_bag['segil']+=10
        user_data_collections[1].update_one({"_id":ObjectId(user_obj_id)},{"$set":{'bag':user_bag}})
        query.message.edit_text(f"*SMELTED {user_weapons[pop_id]['weapon_name']} AND YOU GOT {rnd_res} {random_metal[0].upper()} + 10 Segil*",parse_mode=ParseMode.MARKDOWN)
        user_weapons.pop(pop_id)
        user_data_collections[1].update_one({"_id":ObjectId(user_obj_id)},{"$set":{'weapons':user_weapons}})
        return

def status_plate(update,context):
    if maintenance_mode == "ON":
        if update.effective_user.id not in admins_id:
            update.message.reply_text("*BOT UNDER MAINTENANCE*",parse_mode=ParseMode.MARKDOWN)
            return
    user=update.message.from_user
    user_data=[db.get_collection("user_datas"),db.get_collection("user_data"),db.get_collection("user_ids"),db.get_collection("beta_users")]
    if user.id in user_data[3].find_one()['beta_players']:
        update.message.reply_text("*SEDLY U R NOT WORTHY TO USE THIS COMMAND*",parse_mode=ParseMode.MARKDOWN)
        return
    else:
        if user.id not in user_data[2].find_one()['user_ids']:
            keyboard=[[InlineKeyboardButton('PM',url='https://t.me/PSO_SoBot?start')]]
            update.message.reply_video(video='https://graph.org/file/e663ce2ffd9c8c32d3247.mp4',caption="*It seems like u haven't started\nClick on the button given below and start the bot*",reply_markup=InlineKeyboardMarkup(keyboard),parse_mode=ParseMode.MARKDOWN)
            return
        user_obj_id = user_data[0].find_one()['user_data'][f'user_{user.id}']
        user_info=user_data[1].find_one({'_id': ObjectId(user_obj_id)})['user_info']
        date=user_data[1].find_one({'_id': ObjectId(user_obj_id)})['date']
        join_date=f"{date}"
        print(join_date.split(" ")[0])
        background=user_data[1].find_one({'_id': ObjectId(user_obj_id)})['user_info']['pfp']
        if background==None:
            img=Image.open("STATUS.png")
        else:
            print("gay")
            return
        font= ImageFont.truetype("Battle Bots Italic.ttf",100)
        draw=ImageDraw.Draw(img)
        text=f"USER ID : {user.id}"
        if user.username==None:
            users_name=f"NAME  :  {user.first_name}"
        else:
            users_name=f"NAME  :  {user.username.upper()}"
        draw.text((10,100*1),users_name,(0,0,0),font=font)
        draw.text((10,100*2),text,(0,0,0),font=font)
        draw.text((10,100*3),f"TOTAL EXPLORES : {user_info['explores']['normal']}",(0,0,0),font=font)
        draw.text((10,100*4),f"TOTAL KILLS : {user_info['kills']}",(0,0,0),font=font)
        draw.text((10,100*5),f"RANK : {user_info['rank']}",(0,0,0),font=font)
        if user_info['region']=='HELL_GATE_CASTLE_YARD':
            region="CURRENT REGION : HELL GATE CASTLE YARD"
        else:
            region="CURRENT REGION : DUNGEON"
        draw.text((10,100*6),f"EXPERIENCE POINTs : {user_info['exp']} / {(10000)+(10000*user_info['rank']*2-user_info['rank']*2500)}",(0,0,0),font=font)
        draw.text((9,100*7),region,(0,0,0),font=font)
        img.save(f"NEW_STATUS_{user.id}.png")
        update.message.reply_photo(photo=open(f"NEW_STATUS_{user.id}.png","rb"),caption=f"*STATUS PLATE : *\n\n`JOIN DATE : `*{join_date.split(' ')[0]}*",parse_mode=ParseMode.MARKDOWN)
        os.remove(f"NEW_STATUS_{user.id}.png")

def add_res(update,context):
    if maintenance_mode == "ON":
        if update.effective_user.id not in admins_id:
            update.message.reply_text("*BOT UNDER MAINTENANCE*",parse_mode=ParseMode.MARKDOWN)
            return
    user=update.effective_user
    if user.id == 1864257459:
        user_data=[db.get_collection("user_datas"),db.get_collection("user_data"),db.get_collection("user_ids"),db.get_collection("beta_users")]
        if user.id in user_data[3].find_one()['beta_players']:
            update.message.reply_text("*SEDLY U R NOT ELIGIBLE TO USE THIS COMMAND*",parse_mode=ParseMode.MARKDOWN)
        else:
            if user.id not in user_data[2].find_one()['user_ids']:
                keyboard=[[InlineKeyboardButton('PM',url='https://t.me/game_sobot?start')]]
                update.message.reply_video(video='https://graph.org/file/e663ce2ffd9c8c32d3247.mp4',caption="*It seems like u haven't started\nClick on the button given below and start the bot*",reply_markup=InlineKeyboardMarkup(keyboard),parse_mode=ParseMode.MARKDOWN)
                return
            replied_user=update.message.reply_to_message.from_user
            user_obj_id = user_data[0].find_one()['user_data'][f'user_{replied_user.id}']
            user_bag=user_data[1].find_one({'_id': ObjectId(user_obj_id)})['bag']
            user_res=user_bag[update.message.text.split(" ")[1].lower()]
            user_res+=int(update.message.text.split(" ")[2])
            user_bag[update.message.text.split(" ")[1].lower()]=user_res
            user_data[1].update_one({"_id":ObjectId(user_obj_id)},{"$set":{'bag':user_bag}})
            update.message.reply_text(f"*ADDED {update.message.text.split(' ')[2]} {update.message.text.split(' ')[1]} into {replied_user.first_name}'s bag*",parse_mode=ParseMode.MARKDOWN)
            return
    else:
        update.message.reply_text("*FUCK OFF*",parse_mode=ParseMode.MARKDOWN)

def team_selection(update,context):
    if maintenance_mode == "ON":
        if update.effective_user.id not in admins_id:
            update.message.reply_text("*BOT UNDER MAINTENANCE*",parse_mode=ParseMode.MARKDOWN)
            return
    user=update.effective_user
    if user.id in insiders:
        update.message.reply_text("*You're Cannot use this while in a Battle *",parse_mode=ParseMode.MARKDOWN)
        return
    user_data=[db.get_collection("user_datas"),db.get_collection("user_data"),db.get_collection("user_ids"),db.get_collection("beta_users")]
    if user.id in user_data[3].find_one()['beta_players']:
        update.message.reply_text("*SEDLY U R NOT WORTHY TO USE THIS COMMAND*",parse_mode=ParseMode.MARKDOWN)
        return
    else:
        if user.id not in user_data[2].find_one()['user_ids']:
            keyboard=[[InlineKeyboardButton('PM',url='https://t.me/PSO_SoBot?start')]]
            update.message.reply_video(video='https://graph.org/file/e663ce2ffd9c8c32d3247.mp4',caption="*It seems like u haven't started\nClick on the button given below and start the bot*",reply_markup=InlineKeyboardMarkup(keyboard),parse_mode=ParseMode.MARKDOWN)
            return
        if update.effective_chat.id != user.id:
            user_obj_id = user_data[0].find_one()['user_data'][f'user_{user.id}']
            user_team=user_data[1].find_one({'_id': ObjectId(user_obj_id)})['team']
            keyboard=[[InlineKeyboardButton('USE IN PM',url='https://t.me/PSO_SoBot?start=team')]]
            characters=user_data[1].find_one({'_id': ObjectId(user_obj_id)})['user_char']
            team_players=[]
            team_text=""
            for i in range(4):
                if user_team[f"team_player_{i+1}"]['name']!="None":
                    for j in range(len(characters)):
                        if user_team[f"team_player_{i+1}"]['name']==characters[j]['name']:
                            team_players.append(characters[j])
            if len(team_players)<1:
                team_text+="*NO TEAM SET YET*"
            else:
                for k in range(len(team_players)):
                    team_text+=f"*◇ {team_players[k]['name']} • {team_players[k]['level']}\n*"
            update.message.reply_text("*YOUR TEAM : *\n\n"+team_text+"\n*Levels are shown by the side of the characters name*",reply_markup=InlineKeyboardMarkup(keyboard),parse_mode=ParseMode.MARKDOWN)
            return
        user_obj_id = user_data[0].find_one()['user_data'][f'user_{user.id}']
        user_team=user_data[1].find_one({'_id': ObjectId(user_obj_id)})['team']
        keyboard=[[InlineKeyboardButton(f'{user_team["team_player_1"]["name"]}',callback_data=f"teamselect_1"),InlineKeyboardButton(f'{user_team["team_player_2"]["name"]}',callback_data=f"teamselect_2")]
        ,[InlineKeyboardButton(f'{user_team["team_player_3"]["name"]}',callback_data=f"teamselect_3"),InlineKeyboardButton(f'{user_team["team_player_4"]["name"]}',callback_data=f"teamselect_4")]
        ,[InlineKeyboardButton(f'RESET TEAM',callback_data=f"teamselect_RESET")]]
        context.bot.send_message(chat_id=update.effective_chat.id,text="Your Team : ",reply_markup=InlineKeyboardMarkup(keyboard),parse_mode=ParseMode.MARKDOWN)

def tem_selecter(update,context):
    if maintenance_mode == "ON":
        if update.effective_user.id not in admins_id:
            try:
                update.callback_query.message.edit_text("*BOT UNDER MAINTENANCE*",parse_mode=ParseMode.MARKDOWN)
            except:
                update.callback_query.message.edit_caption(caption="*BOT UNDER MAINTENANCE*",parse_mode=ParseMode.MARKDOWN)
            return
    user=update.effective_user
    query=update.callback_query
    if user.id in insiders:
        query.message.edit_text("*You Cannot use this while in a Battle *",parse_mode=ParseMode.MARKDOWN)
        return
    cd = context.chat_data
    user_data=[db.get_collection("user_datas"),db.get_collection("user_data"),db.get_collection("user_ids"),db.get_collection("beta_users")]
    user_obj_id = user_data[0].find_one()['user_data'][f'user_{user.id}']
    user_team=user_data[1].find_one({'_id': ObjectId(user_obj_id)})['team']
    if query.data.split("_")[-1] == 'RESET':
        user_team={"team_player_1":{"name":"None"},"team_player_2":{"name":"None"},"team_player_3":{"name":"None"},"team_player_4":{"name":"None"}}
        user_data[1].update_one({"_id":ObjectId(user_obj_id)},{"$set":{'team':user_team}})
        query.message.edit_text("*TEAM RESETED*",parse_mode=ParseMode.MARKDOWN)
        return
    user_team_1=user_data[1].find_one({'_id': ObjectId(user_obj_id)})['team']["team_player_1"]
    characters=user_data[1].find_one({'_id': ObjectId(user_obj_id)})['user_char']
    out_team_char=characters
    if query.data.split("_")[-1]== "close":
        query.message.edit_text("*CLOSED*",parse_mode=ParseMode.MARKDOWN)
        return
    character_text="`Characters : `\n\n"
    keyboard1, keyboard2, keyboard3, keyboard4 = [[]], [[], []], [[], [], []], [[], [], [], []]
    nm=0
    for i in range(len(characters)):
        n=0
        for j in range(4):
            n+=1
            if user_team[f"team_player_{n}"]['name'] == characters[nm]['name']:
                out_team_char.remove(characters[nm])
                nm-=1
        nm+=1
    m=0
    for i in range(len(out_team_char)):
        character_text+=f"*{i+1}. {out_team_char[i]['name']}*\n"
        if len(out_team_char) < 7 and len(out_team_char) > 0  :
            keyboard1[0].append(InlineKeyboardButton(f'{m+1}',callback_data=f"team_change_{out_team_char[i]['name']}"))
        elif len(out_team_char) < 13 and len(out_team_char) > 6 :
            if m+1 < 7 :
                keyboard2[0].append(InlineKeyboardButton(f'{m+1}',callback_data=f"team_change_{out_team_char[i]['name']}"))
            else:
                keyboard2[1].append(InlineKeyboardButton(f'{m+1}',callback_data=f"team_change_{out_team_char[i]['name']}"))
        elif len(out_team_char) < 19 and len(out_team_char) > 12 :
            if m+1 < 7 and m+1 > 0:
                keyboard3[0].append(InlineKeyboardButton(f'{m+1}',callback_data=f"team_change_{out_team_char[i]['name']}"))
            elif m+1 < 13 and m+1 > 6:
                keyboard3[1].append(InlineKeyboardButton(f'{m+1}',callback_data=f"team_change_{out_team_char[i]['name']}"))
            else:
                keyboard3[2].append(InlineKeyboardButton(f'{m+1}',callback_data=f"team_change_{out_team_char[i]['name']}"))
        else:
            if m+1 < 7 and m+1 > 0:
                keyboard4[0].append(InlineKeyboardButton(f'{m+1}',callback_data=f"team_change_{out_team_char[i]['name']}"))
            elif m+1 < 13 and m+1 > 6:
                keyboard4[1].append(InlineKeyboardButton(f'{m+1}',callback_data=f"team_change_{out_team_char[i]['name']}"))
            elif m+1 < 13 and m+1 > 6:
                keyboard4[2].append(InlineKeyboardButton(f'{m+1}',callback_data=f"team_change_{out_team_char[i]['name']}"))
            else:
                keyboard4[3].append(InlineKeyboardButton(f'{m+1}',callback_data=f"team_change_{out_team_char[i]['name']}"))
        m+=1
    if len(out_team_char) > 0 and len(out_team_char) < 7:
        keyboard=keyboard1
    elif len(out_team_char) > 6 and len(out_team_char) < 13:
        keyboard=keyboard2
    elif len(out_team_char) > 12 and len(out_team_char) < 19:
        keyboard=keyboard3
    else:
        keyboard=keyboard4
    keyboard.append([(InlineKeyboardButton('CLOSE', callback_data='teamselect_close'))])
    message = query.message.edit_text(character_text,reply_markup=InlineKeyboardMarkup(keyboard),parse_mode=ParseMode.MARKDOWN)
    message_id = message.message_id
    cd[message_id] = {}
    cd[message_id]['player_place'] = f"{query.data.split('_')[-1]}"
    return TEAM_CHANGER

def team_changer(update,context):
    if maintenance_mode == "ON":
        if update.effective_user.id not in admins_id:
            try:
                update.callback_query.message.edit_text("*BOT UNDER MAINTENANCE*",parse_mode=ParseMode.MARKDOWN)
            except:
                update.callback_query.message.edit_caption(caption="*BOT UNDER MAINTENANCE*",parse_mode=ParseMode.MARKDOWN)
            return
    user=update.effective_user
    query=update.callback_query
    if user.id in insiders:
        query.message.edit_text("*You Cannot use this while in a Battle *",parse_mode=ParseMode.MARKDOWN)
        return
    cd = context.chat_data
    message_id = query.message.message_id
    team_id = cd[message_id]['player_place']
    user_data=[db.get_collection("user_datas"),db.get_collection("user_data"),db.get_collection("user_ids"),db.get_collection("beta_users")]
    user_obj_id = user_data[0].find_one()['user_data'][f'user_{user.id}']
    user_team=user_data[1].find_one({'_id': ObjectId(user_obj_id)})['team']
    user_team_1=user_data[1].find_one({'_id': ObjectId(user_obj_id)})['team'][f"team_player_{team_id}"]
    ctr=0
    for i in range(4):
        if query.data.split("_")[-1] == user_team[f"team_player_{i+1}"]['name']:
            query.message.edit_text(f"*THE character is already in team*",parse_mode=ParseMode.MARKDOWN)
            return
    user_team_1['name']=query.data.split("_")[-1]
    user_team[f"team_player_{team_id}"]=user_team_1
    user_data[1].update_one({"_id":ObjectId(user_obj_id)},{"$set":{'team':user_team}})
    msg= query.message.edit_text(f"*Change TEAM Player {team_id} to {query.data.split('_')[-1]}*",parse_mode=ParseMode.MARKDOWN)
    context.bot.delete_message(chat_id=msg.chat_id, message_id=msg.message_id)
    context.bot.send_message(chat_id=update.effective_chat.id,text="*IF u want to change team again then use the command given below*",parse_mode=ParseMode.MARKDOWN)
    team_selection(update,context)
    return

def giv_cmd(update,context):
    if maintenance_mode == "ON":
        if update.effective_user.id not in admins_id:
            update.message.reply_text("*BOT UNDER MAINTENANCE*",parse_mode=ParseMode.MARKDOWN)
            return
    user=update.effective_user
    if user.id in insiders:
        update.message.reply_text("*You're Cannot use this while in a Battle *",parse_mode=ParseMode.MARKDOWN)
        return
    if not update.message.reply_to_message:
        update.message.reply_text("*REPLY TO A USER*",parse_mode=ParseMode.MARKDOWN)
        return
    replied=update.message.reply_to_message.from_user
    user_data=[db.get_collection("user_datas"),db.get_collection("user_data"),db.get_collection("user_ids"),db.get_collection("beta_users")]
    if user.id in user_data[3].find_one()['beta_players']:
        update.message.reply_text("*SEDLY U R NOT ELIGIBLE TO USE THIS COMMAND*",parse_mode=ParseMode.MARKDOWN)
        return
    elif replied.id in user_data[3].find_one()['beta_players']:
        update.message.reply_text("*SEDLY THE USER U R GIVING THE ITEM IS NOT ELIGIBLE TO USE BOT*",parse_mode=ParseMode.MARKDOWN)
        return
    elif user.id == replied.id:
        update.message.reply_text("*SEDLY You can't give the resources to yourself*",parse_mode=ParseMode.MARKDOWN)
        return
    else:
        if user.id not in user_data[2].find_one()['user_ids']:
            keyboard=[[InlineKeyboardButton('PM',url='https://t.me/PSO_SoBot?start')]]
            update.message.reply_video(video='https://graph.org/file/e663ce2ffd9c8c32d3247.mp4',caption="*It seems like u haven't started\nClick on the button given below and start the bot*",reply_markup=InlineKeyboardMarkup(keyboard),parse_mode=ParseMode.MARKDOWN)
            return
        if  replied.id not in user_data[2].find_one()['user_ids']:
            keyboard=[[InlineKeyboardButton('PM',url='https://t.me/PSO_SoBot?start')]]
            update.message.reply_video(video='https://graph.org/file/e663ce2ffd9c8c32d3247.mp4',caption="*It seems like u haven't started\nClick on the button given below and start the bot*",reply_markup=InlineKeyboardMarkup(keyboard),parse_mode=ParseMode.MARKDOWN)
            return
        user_obj_id = user_data[0].find_one()['user_data'][f'user_{user.id}']
        reciever_obj_id = user_data[0].find_one()['user_data'][f'user_{replied.id}']
        user_inside=user_data[1].find_one({'_id': ObjectId(user_obj_id)})['extras']
        replied_inside=user_data[1].find_one({'_id': ObjectId(reciever_obj_id)})['extras']
        if user_inside['INSIDE'].split("_")[0] == 'IN':
            update.message.reply_text(f"*You're currently using {user_inside['INSIDE'].split('_')[1]}*",parse_mode=ParseMode.MARKDOWN)
            return
        if replied_inside['INSIDE'].split("_")[0] == 'IN':
            update.message.reply_text(f"*The Replied User Currently using {replied_inside['INSIDE'].split('_')[1]}*",parse_mode=ParseMode.MARKDOWN)
            return
        user_bag=user_data[1].find_one({'_id': ObjectId(user_obj_id)})['bag']
        reciever_bag=user_data[1].find_one({'_id': ObjectId(reciever_obj_id)})['bag']
        number_wea=update.message.text.split(" ")[2]
        user_info=user_data[1].find_one({'_id': ObjectId(user_obj_id)})['user_info']
        if len(update.message.text.split(" ")) < 3:
            update.message.reply_text("*Invalid Sentence*",parse_mode=ParseMode.MARKDOWN)
            return
        elif update.message.text.split(" ")[1] not in list(user_bag.keys()):
            update.message.reply_text("*Invalid Object*",parse_mode=ParseMode.MARKDOWN)
            return
        elif update.message.text.split(" ")[1].lower()=='primostar':
            if user_info['rank']<9:
                update.message.reply_text("*RANK UP TO 10 TO SEND PRIMOSTAR*",parse_mode=ParseMode.MARKDOWN)
                return
        elif update.message.text.split(" ")[1].lower()=='stargems':
            if user_info['rank']<5:
                update.message.reply_text("*RANK UP TO 5 TO SEND STARGEMS*",parse_mode=ParseMode.MARKDOWN)
                return
        elif update.message.text.split(" ")[1].lower()=='segil':
            if user_info['rank']<3:
                update.message.reply_text("*RANK UP TO 3 TO SEND Segil*",parse_mode=ParseMode.MARKDOWN)
                return
        elif number_wea.isalpha():
            update.message.reply_text("*Invalid NUMBER*",parse_mode=ParseMode.MARKDOWN)
            return
        ctr=0
        reciver_coi=0
        try:
            reciver_coi+=int(number_wea)
            ctr+=1
        except :
            ctr=0
        if ctr == 0:
            update.message.reply_text("*Invalid NUMBER*",parse_mode=ParseMode.MARKDOWN)
        else:
            if user_bag[update.message.text.split(" ")[1]] < int(number_wea):
                keyboard=[[InlineKeyboardButton('Check Bag',callback_data =f"bag_pouch_user{user.id}")]]
                update.message.reply_video(video='https://graph.org/file/5c63bd654ddb894a6750d.mp4',caption=f"*You Don't have Enough {update.message.text.split(' ')[1]}\nCheck Bag ?*",reply_markup=InlineKeyboardMarkup(keyboard),parse_mode=ParseMode.MARKDOWN)
                return
            if int(number_wea) < 1:
                update.message.reply_text("*Invalid Number*",parse_mode=ParseMode.MARKDOWN)
                return
            if user_bag[update.message.text.split(" ")[1]] >= int(number_wea):
                user_bag[update.message.text.split(" ")[1]]-=int(number_wea)
                reciever_bag[update.message.text.split(" ")[1]]+=int(number_wea)
                keyboard=[[InlineKeyboardButton('Check Bag',callback_data =f"bag_pouch_user{user.id}")]]
                update.message.reply_video(video='https://graph.org/file/29d5128844d972a49823c.mp4',caption=f"*Sent {number_wea} {update.message.text.split(' ')[1]} to {replied.first_name}\nTime : {datetime.datetime.utcnow()}\nCheck Your Bag ?*",reply_markup=InlineKeyboardMarkup(keyboard),parse_mode=ParseMode.MARKDOWN)
                context.bot.send_message(chat_id=1864257459,text=f"* USER : {user.id}\nRECIEVER : {replied.id}\nSent {number_wea} {update.message.text.split(' ')[1]} to {replied.first_name}\nTime : {datetime.datetime.utcnow()}*",parse_mode=ParseMode.MARKDOWN)
                user_data[1].update_one({"_id":ObjectId(user_obj_id)},{"$set":{'bag':user_bag}})
                user_data[1].update_one({"_id":ObjectId(reciever_obj_id)},{"$set":{'bag':reciever_bag}})
                return
            else:
                update.message.reply_text("*NO BITCHES*",parse_mode=ParseMode.MARKDOWN)

def gift_all(update,context):
    if maintenance_mode == "ON":
        if update.effective_user.id not in admins_id:
            update.message.reply_text("*BOT UNDER MAINTENANCE*",parse_mode=ParseMode.MARKDOWN)
            return
    user=update.message.from_user
    if user.id == 1864257459:
        user_data=[db.get_collection("user_datas"),db.get_collection("user_data"),db.get_collection("user_ids"),db.get_collection("beta_users")]
        n=0
        for i in range(len(user_data[2].find_one()['user_ids'])):
            user_obj_id = user_data[0].find_one()['user_data'][f"user_{user_data[2].find_one()['user_ids'][i]}"]
            user_bag=user_data[1].find_one({'_id': ObjectId(user_obj_id)})['bag']
            user_bag[f"{update.message.text.split(' ')[-2]}"]+=int(update.message.text.split(" ")[-1])
            user_data[1].update_one({"_id":ObjectId(user_obj_id)},{"$set":{'bag':user_bag}})
            try:
                context.bot.send_message(chat_id=int(user_data[2].find_one()['user_ids'][i]),text=f"`YOU GOT `*{update.message.text.split(' ')[-1]} {update.message.text.split(' ')[-2]} from Bot Owner\n\nAND HERE WE RELEASE THE VERSION 1.2 OF PSO\nA NEW ELEMENT IS HERE THE PHYSICAL\nTHE BANNER OF RAIDEN SHOGUN AND SEKIRO IS HERE ASWELL\AND NEW MONSTERS ARE WAITING FOR YOU*",parse_mode=ParseMode.MARKDOWN)
                n+=1
            except:
                print('user is gay')
        update.message.reply_text(f"*Gifted {n} Users\n{update.message.text.split(' ')[-1]} {update.message.text.split(' ')[-2]}*",parse_mode=ParseMode.MARKDOWN)
        return
    update.message.reply_text("*NO BITCHES*",parse_mode=ParseMode.MARKDOWN)

def broadcast_all(update,context):
    if maintenance_mode == "ON":
        if update.effective_user.id not in admins_id:
            update.message.reply_text("*BOT UNDER MAINTENANCE*",parse_mode=ParseMode.MARKDOWN)
            return
    user =update.message.from_user
    if user.id == 1864257459:
        user_data=[db.get_collection("user_datas"),db.get_collection("user_data"),db.get_collection("user_ids"),db.get_collection("beta_users")]
        gey=0
        for i in range(len(user_data[2].find_one()['user_ids'])):
            try:
                context.bot.send_message(chat_id=int(user_data[2].find_one()['user_ids'][i]),text="*HEYA Traveler \nTHE LONG WAITED CHARACTER IS HERE\nWHY NOT GO ON GACHA AND CHECK IT BY YOURSELF\nTHE CHARACTER HAVING A OVERPOWERED ABILITY OF HEALING WHICH WILL NEVER LET U DOWN*",parse_mode=ParseMode.MARKDOWN)
            except:
                gey+=1
        update.message.reply_text(f"Recieved User : {len(user_data[2].find_one()['user_ids'])-gey}\n\nGAYS : {gey}")

def reset_cmd(update,context):
    if maintenance_mode == "ON":
        if update.effective_user.id not in admins_id:
            update.message.reply_text("*BOT UNDER MAINTENANCE*",parse_mode=ParseMode.MARKDOWN)
            return
    user=update.message.from_user
    if user.id == 1864257459:
        user_id=update.message.text.split(" ")[1]
        user_data=[db.get_collection("user_datas"),db.get_collection("user_data"),db.get_collection("user_ids"),db.get_collection("beta_users")]
        user_obj_id = user_data[0].find_one()['user_data'][f'user_{user_id}']
        char=user_data[1].find_one({'_id': ObjectId(user_obj_id)})['user_char'][0]
        user_data[1].update_one({"_id":ObjectId(user_obj_id)},{"$set":{'bag':{"segil":100,"stargems":0,"primostar":5,"tow_en":200,"starspliter_gems":0}}})
        user_data[1].update_one({"_id":ObjectId(user_obj_id)},{"$set":{'gacha_details':{"event_banner":{"gacha_history":[],"gacha_pity":0},"standard_banner":{"gacha_history":[],"gacha_pity":0},"weapon_banner":{"gacha_history":[],"gacha_pity":0}}}})
        user_data[1].update_one({"_id":ObjectId(user_obj_id)},{"$set":{'weapons':gift_weapon}})
        user_data[1].update_one({"_id":ObjectId(user_obj_id)},{"$set":{'user_info':{'rank':0,'exp':0,'kills':0,'explores':{'normal':0,'dungeon':0},'battle_logs':{'win':0,'loss':0},'pfp':None,'region':'HELL_GATE_CASTLE_YARD'}}})
        user_data[1].update_one({"_id":ObjectId(user_obj_id)},{"$set":{'team':{"team_player_1":{"name":"None"},"team_player_2":{"name":"None"},"team_player_3":{"name":"None"},"team_player_4":{"name":"None"}}}})
        user_data[1].update_one({"_id":ObjectId(user_obj_id)},{"$set":{'artifacts':[]}})
        user_data[1].update_one({"_id":ObjectId(user_obj_id)},{"$set":{'myartifacts':{"myartifacts_1":None,"myartifacts_2":None,"myartifacts_3":None,"myartifacts_4":None,"myartifacts_5":None}}})
        user_data[1].update_one({"_id":ObjectId(user_obj_id)},{"$set":{'user_char':[char]}})
        user_data[1].update_one({"_id":ObjectId(user_obj_id)},{"$set":{'extras':{"INSIDE":"NOPE",'refferal':{'total_reffered':0,"reffered_users":[],"reffered_by":None}}}})
        update.message.reply_text("*RESET DONE*",parse_mode=ParseMode.MARKDOWN)
        return
    update.message.reply_text("*NO BITCHES*",parse_mode=ParseMode.MARKDOWN)

def rest_stuk(update,context):
    if maintenance_mode == "ON":
        if update.effective_user.id not in admins_id:
            update.message.reply_text("*BOT UNDER MAINTENANCE*",parse_mode=ParseMode.MARKDOWN)
            return
    user=update.message.from_user
    global insiders
    if user.id in insiders:
        insiders.remove(user.id)
        update.message.reply_text("*DONE*",parse_mode=ParseMode.MARKDOWN)
    else:
        update.message.reply_text("*SEEMS LIKE U R NOT STUCK*",parse_mode=ParseMode.MARKDOWN)
    return

def element_types(update,context):
    if maintenance_mode == "ON":
        if update.effective_user.id not in admins_id:
            update.message.reply_text("*BOT UNDER MAINTENANCE*",parse_mode=ParseMode.MARKDOWN)
            return
    user=update.message.from_user
    user_data=[db.get_collection("user_datas"),db.get_collection("user_data"),db.get_collection("user_ids"),db.get_collection("beta_users")]
    if user.id in user_data[3].find_one()['beta_players']:
        update.message.reply_text("*SEDLY U R NOT WORTHY TO USE THIS COMMAND*",parse_mode=ParseMode.MARKDOWN)
    else:
        if user.id not in user_data[2].find_one()['user_ids']:
            keyboard=[[InlineKeyboardButton('PM',url='https://t.me/PSO_SoBot?start')]]
            update.message.reply_video(video='https://graph.org/file/e663ce2ffd9c8c32d3247.mp4',caption="*It seems like u haven't started\nClick on the button given below and start the bot*",reply_markup=InlineKeyboardMarkup(keyboard),parse_mode=ParseMode.MARKDOWN)
            return
        update.message.reply_text("`Fire - `*15% attack buff*\n\n`Earth - `*15% Defense buff*\n\n`Water- `*7.5% healing buff + Slowing 7.5% Speed of opponent*\n\n`Ice - `*15% Chance of freezing opponent + 15% Crit rate boost on freezed enemy*\n\n`Wind - `*30% chance of getting 15% Extra Speed Every Moves*\n\n`Electric - `*30% Speed boost At the starting of the game + Defeating every Enemy Increases team speed with +15%*\n\n`Light - `*15% resistance against all elements and 15% Extra Damage on Dark element*\n\n`Dark - `*15% Extra Damage on all elements (Except Light and dark) and 15% Extra defense on all elements (Except Light and dark)*",parse_mode=ParseMode.MARKDOWN)

def add_fuker(update,context):
    if maintenance_mode == "ON":
        if update.effective_user.id not in admins_id:
            update.message.reply_text("*BOT UNDER MAINTENANCE*",parse_mode=ParseMode.MARKDOWN)
            return
    user=update.message.from_user
    user_data=[db.get_collection("user_datas"),db.get_collection("user_data"),db.get_collection("user_ids"),db.get_collection("beta_users")]
    if user.id in user_data[3].find_one()['beta_players']:
        update.message.reply_text("*SEDLY U R NOT WORTHY TO USE THIS COMMAND*",parse_mode=ParseMode.MARKDOWN)
    else:
        if user.id not in user_data[2].find_one()['user_ids']:
            keyboard=[[InlineKeyboardButton('PM',url='https://t.me/PSO_SoBot?start')]]
            update.message.reply_video(video='https://graph.org/file/e663ce2ffd9c8c32d3247.mp4',caption="*It seems like u haven't started\nClick on the button given below and start the bot*",reply_markup=InlineKeyboardMarkup(keyboard),parse_mode=ParseMode.MARKDOWN)
            return
        if user.id in [1864257459]:
            try:
                replied_user=update.message.reply_to_message.from_user
                user_obj_id = user_data[0].find_one()['user_data'][f'user_{replied_user.id}']
            except:
                user_obj_id = user_data[0].find_one()['user_data'][f'user_{user.id}']
            user_characters=user_data[1].find_one({'_id': ObjectId(user_obj_id)})['user_char']
            add_3_char=char.sekiro_char
            add_3_char['weapon']=[char.weapons['mortal_blade']]
            user_characters.append(add_3_char)
            user_data[1].update_one({"_id":ObjectId(user_obj_id)},{"$set":{'user_char':user_characters}})
            return
        else:
            print('hecker detected')
    
def enter_dungeon(update,context):
    if maintenance_mode == "ON":
        if update.effective_user.id not in admins_id:
            update.message.reply_text("*BOT UNDER MAINTENANCE*",parse_mode=ParseMode.MARKDOWN)
            return
    user=update.message.from_user
    if user.id in insiders:
        update.message.reply_text("*You're Cannot use this while in a Battle *",parse_mode=ParseMode.MARKDOWN)
        return
    user_data=[db.get_collection("user_datas"),db.get_collection("user_data"),db.get_collection("user_ids"),db.get_collection("beta_users")]
    if user.id in user_data[3].find_one()['beta_players']:
        update.message.reply_text("*SEDLY U R NOT WORTHY TO USE THIS COMMAND*",parse_mode=ParseMode.MARKDOWN)
        return
    else:
        if user.id not in user_data[2].find_one()['user_ids']:
            keyboard=[[InlineKeyboardButton('PM',url='https://t.me/PSO_SoBot?start')]]
            update.message.reply_video(video='https://graph.org/file/e663ce2ffd9c8c32d3247.mp4',caption="*It seems like u haven't started\nClick on the button given below and start the bot*",reply_markup=InlineKeyboardMarkup(keyboard),parse_mode=ParseMode.MARKDOWN)
            return
        user_obj_id = user_data[0].find_one()['user_data'][f'user_{user.id}']
        user_bag=user_data[1].find_one({'_id': ObjectId(user_obj_id)})['user_info']
        if user_bag['region'].split("_")[0]=='DUNGEON':
            keyboard=[[InlineKeyboardButton('EXIT',callback_data=f'dungeon_selection_{user.id}_exit')]]
            update.message.reply_text("*SEEMS LIKE U R ALREADY U IN DUNGEON\n\n\t\t\tYou cannot enter dungeon again while already in dungeon\nFor exiting click on exit*",reply_markup=InlineKeyboardMarkup(keyboard),parse_mode=ParseMode.MARKDOWN)
            return
        else:
            if update.effective_chat.id == user.id:
                keyboard=[[InlineKeyboardButton('SELECT LEVEL : ',callback_data='flase')],[InlineKeyboardButton('1',callback_data='dungeon_selection_1'),InlineKeyboardButton('2',callback_data='dungeon_selection_2'),InlineKeyboardButton('3',callback_data='dungeon_selection_3'),InlineKeyboardButton('4',callback_data='dungeon_selection_4')]]
            else:
                keyboard=[[InlineKeyboardButton('USE IN PM',url='https://t.me/PSO_SoBot?start=dungeon')]]
            update.message.reply_photo(photo='https://telegra.ph/file/05677c8f246ee0dbeefc0.jpg',caption="*WELCOME TO DUNGEON OF HELL GATE\n\nFor Entering Dunegon our GATE keeper Uncle Dimension Slayer will take 100 segil\nDO you want to enter gate ?\nThen just select the Level and Enter the Dungeon of Hell Gate\n\nCOST : 100 Segil\nSELECT THE LEVEL*",reply_markup=InlineKeyboardMarkup(keyboard),parse_mode=ParseMode.MARKDOWN)
            return

def dungon_slt(update,context):
    if maintenance_mode == "ON":
        if update.effective_user.id not in admins_id:
            try:
                update.callback_query.message.edit_text("*BOT UNDER MAINTENANCE*",parse_mode=ParseMode.MARKDOWN)
            except:
                update.callback_query.message.edit_caption(caption="*BOT UNDER MAINTENANCE*",parse_mode=ParseMode.MARKDOWN)
            return
    user=update.callback_query.from_user
    query = update.callback_query
    user_data=[db.get_collection("user_datas"),db.get_collection("user_data"),db.get_collection("user_ids"),db.get_collection("beta_users")]
    user_obj_id = user_data[0].find_one()['user_data'][f'user_{user.id}']
    user_bag=user_data[1].find_one({'_id': ObjectId(user_obj_id)})['bag']
    user_info=user_data[1].find_one({'_id': ObjectId(user_obj_id)})['user_info']
    if query.data.split("_")[-1]=='exit':
        if user.id in insiders:
            query.message.edit_text("*You Cannot use this while in a Battle *",parse_mode=ParseMode.MARKDOWN)
            return
        touch_id=int(query.data.split("_")[-2])
        if user.id != touch_id:
            return
        msg = query.message.edit_text("`Processing..`",parse_mode=ParseMode.MARKDOWN)
        msg = query.message.edit_text("`Processing....`",parse_mode=ParseMode.MARKDOWN)
        msg = query.message.edit_text("`Processing......`",parse_mode=ParseMode.MARKDOWN)
        query.message.reply_text(f"*EXITED THE DUNGEON*",parse_mode=ParseMode.MARKDOWN)
        context.bot.delete_message(chat_id=msg.chat_id, message_id=msg.message_id)
        user_explores=user_info['explores']
        user_explores['dungeon']=0
        user_info['explores']=user_explores
        user_info['region']='HELL_GATE_CASTLE_YARD'
    else:
        if user.id in insiders:
            query.message.edit_caption(caption="*You Cannot use this while in a Battle *",parse_mode=ParseMode.MARKDOWN)
            return
        if user_bag['segil'] < 100:
            msg = query.message.edit_caption(caption="*You Don't have enough Segil to enter Dungeon\nGo hunt in normal*",parse_mode=ParseMode.MARKDOWN)
            context.bot.delete_message(chat_id=msg.chat_id, message_id=msg.message_id)
            return
        msg = query.message.edit_caption(caption="`Processing..`",parse_mode=ParseMode.MARKDOWN)
        msg = query.message.edit_caption(caption="`Processing....`",parse_mode=ParseMode.MARKDOWN)
        msg = query.message.edit_caption(caption="`Processing......`",parse_mode=ParseMode.MARKDOWN)
        context.bot.delete_message(chat_id=msg.chat_id, message_id=msg.message_id)
        user_bag_checker=user_data[1].find_one({'_id': ObjectId(user_obj_id)})['bag']
        if user_info['region'].split('_')[0]=='DUNGEON':
            context.bot.send_message(chat_id=update.effective_chat.id,text=f"*seems like you're already in that region\nYou can't join the same region again",parse_mode=ParseMode.MARKDOWN)
            return
        if user_bag_checker['segil']==0:
            context.bot.send_message(chat_id=update.effective_chat.id,text=f"*It seems like user : {user.first_name} trying to heck the bot\nSEDLy u cant due to higher secondary Protection",parse_mode=ParseMode.MARKDOWN)
            return
        query.message.reply_text(f"*Your have entered dungeon level {query.data.split('_')[-1]} Succesfully\nUSE /explore to encounter dungeon monsters*",parse_mode=ParseMode.MARKDOWN)
        user_bag['segil']-=100
        user_info['region']=f'DUNGEON_{query.data.split("_")[-1]}'
        user_data[1].update_one({"_id":ObjectId(user_obj_id)},{"$set":{'bag':user_bag}})
    user_data[1].update_one({"_id":ObjectId(user_obj_id)},{"$set":{'user_info':user_info}})
    return

def travel_logger(update,context):
    if maintenance_mode == "ON":
        if update.effective_user.id not in admins_id:
            update.message.reply_text("*BOT UNDER MAINTENANCE*",parse_mode=ParseMode.MARKDOWN)
            return
    user=update.message.from_user
    if user.id in insiders:
        update.message.reply_text("*You're Cannot use this while in a Battle *",parse_mode=ParseMode.MARKDOWN)
        return
    user_data=[db.get_collection("user_datas"),db.get_collection("user_data"),db.get_collection("user_ids"),db.get_collection("beta_users")]
    if user.id in user_data[3].find_one()['beta_players']:
        update.message.reply_text("*SEDLY U R NOT WORTHY TO USE THIS COMMAND*",parse_mode=ParseMode.MARKDOWN)
        return
    else:
        if user.id not in user_data[2].find_one()['user_ids']:
            keyboard=[[InlineKeyboardButton('PM',url='https://t.me/PSO_SoBot?start')]]
            update.message.reply_video(video='https://graph.org/file/e663ce2ffd9c8c32d3247.mp4',caption="*It seems like u haven't started\nClick on the button given below and start the bot*",reply_markup=InlineKeyboardMarkup(keyboard),parse_mode=ParseMode.MARKDOWN)
            return
        user_obj_id = user_data[0].find_one()['user_data'][f'user_{user.id}']
        user_info=user_data[1].find_one({'_id': ObjectId(user_obj_id)})['user_info']
        if update.effective_chat.id == user.id:
            keyboard=[[InlineKeyboardButton('HELL GATE CASTLE FIELD',callback_data='travel_HELL_GATE')]]
        else:
            keyboard=[[InlineKeyboardButton('USE IN PM',url='https://t.me/PSO_SoBot?start=travel')]]
        if user_info['region'].split("_")[0]=='DUNGEON':
            update.message.reply_photo(photo='https://telegra.ph/file/05677c8f246ee0dbeefc0.jpg',caption="*SEEMS like you're in DUNGEON\nDO you want to exit Dungeon\nthen SELECT the region to TRAVEL and EXIT the dungeon\n\nTRAVEL TO ?*",reply_markup=InlineKeyboardMarkup(keyboard),parse_mode=ParseMode.MARKDOWN)
            return
        else:
            update.message.reply_photo(photo='https://graph.org/file/19b23bacc92d9e2db43a9.jpg',caption="*WHERE DO YOU WANT TO TRAVEL?*",reply_markup=InlineKeyboardMarkup(keyboard),parse_mode=ParseMode.MARKDOWN)
            return

def travel_slt(update,context):
    if maintenance_mode == "ON":
        if update.effective_user.id not in admins_id:
            try:
                update.callback_query.message.edit_text("*BOT UNDER MAINTENANCE*",parse_mode=ParseMode.MARKDOWN)
            except:
                update.callback_query.message.edit_caption(caption="*BOT UNDER MAINTENANCE*",parse_mode=ParseMode.MARKDOWN)
            return
    user=update.callback_query.from_user
    query = update.callback_query
    if user.id in insiders:
        query.message.edit_caption(caption="*You're Cannot use this while in a Battle *",parse_mode=ParseMode.MARKDOWN)
        return
    user_data=[db.get_collection("user_datas"),db.get_collection("user_data"),db.get_collection("user_ids"),db.get_collection("beta_users")]
    user_obj_id = user_data[0].find_one()['user_data'][f'user_{user.id}']
    user_bag=user_data[1].find_one({'_id': ObjectId(user_obj_id)})['bag']
    user_info=user_data[1].find_one({'_id': ObjectId(user_obj_id)})['user_info']
    msg = query.message.edit_caption(caption="`Processing..`",parse_mode=ParseMode.MARKDOWN)
    msg = query.message.edit_caption(caption="`Processing....`",parse_mode=ParseMode.MARKDOWN)
    msg = query.message.edit_caption(caption="`Processing......`",parse_mode=ParseMode.MARKDOWN)
    context.bot.delete_message(chat_id=msg.chat_id, message_id=msg.message_id)
    if user_info['region']=='HELL_GATE_CASTLE_YARD':
        query.message.reply_text(f"*You are already in the same region*",parse_mode=ParseMode.MARKDOWN)
    if query.data == 'travel_HELL_GATE':
        user_explores=user_info['explores']
        user_explores['dungeon']=0
        user_info['explores']=user_explores
        user_info['region']='HELL_GATE_CASTLE_YARD'
    query.message.reply_text(f"*YOU have Entered the region {user_info['region']}*",parse_mode=ParseMode.MARKDOWN)
    user_data[1].update_one({"_id":ObjectId(user_obj_id)},{"$set":{'user_info':user_info}})

def explore_cmd(update,context):
    if maintenance_mode == "ON":
        if update.effective_user.id not in admins_id:
            update.message.reply_text("*BOT UNDER MAINTENANCE*",parse_mode=ParseMode.MARKDOWN)
            return
    user = update.message.from_user
    cd = context.chat_data
    global insiders
    if user.id in insiders:
        update.message.reply_text("*You're already in a Battle *",parse_mode=ParseMode.MARKDOWN)
        return
    user_data=[db.get_collection("user_datas"),db.get_collection("user_data"),db.get_collection("user_ids"),db.get_collection("beta_users")]
    if user.id in user_data[3].find_one()['beta_players']:
        update.message.reply_text("*SEDLY U R NOT WORTHY TO USE THIS COMMAND*",parse_mode=ParseMode.MARKDOWN)
        return
    else:
        if user.id not in user_data[2].find_one()['user_ids']:
            keyboard=[[InlineKeyboardButton('PM',url='https://t.me/PSO_SoBot?start')]]
            update.message.reply_video(video='https://graph.org/file/e663ce2ffd9c8c32d3247.mp4',caption="*It seems like u haven't started\nClick on the button given below and start the bot*",reply_markup=InlineKeyboardMarkup(keyboard),parse_mode=ParseMode.MARKDOWN)
            return
        user_obj_id = user_data[0].find_one()['user_data'][f'user_{user.id}']
        if update.effective_chat.id != user.id:
            keyboard=[[InlineKeyboardButton('USE IN PM',url='https://t.me/PSO_SoBot?start=explore')]]
            update.message.reply_text("*THIS COMMAND CAN'T BE USED IN GROUP CHAT*",reply_markup=InlineKeyboardMarkup(keyboard),parse_mode=ParseMode.MARKDOWN)
        else:
            user_info=user_data[1].find_one({'_id': ObjectId(user_obj_id)})['user_info']
            if user_info['rank'] < 6 :
                level=random.randint(1,10)
            elif user_info['rank'] > 5 and user_info['rank'] < 12 :
                level=random.randint(5,15)
            else:
                level=random.randint(10,20)
            if user_info['region'].split("_")[0] == 'DUNGEON':
                user_info['explores']['normal']+=1
                mobs=monster.dungeon_mobs[f"level_{user_info['region'].split('_')[1]}"]
                user_explores=user_info['explores']
                if user_explores['dungeon']==50:
                    user_explores['dungeon']=0
                    user_info['region']='HELL_GATE_CASTLE_YARD'
                    user_info['explores']=user_explores
                    user_data[1].update_one({"_id":ObjectId(user_obj_id)},{"$set":{'user_info':user_info}})
                    update.message.reply_text("*SEEMS LIKE UR QUOTA OF DUNGEON EXPLORES OVER\n FOR ENJOYING MORE IN DUNGEON USE /enter_dungeon TO ENTER AGAIN*",parse_mode=ParseMode.MARKDOWN)
                    return
                else:
                    user_explores['dungeon']+=1
                user_info['explores']=user_explores
                user_data[1].update_one({"_id":ObjectId(user_obj_id)},{"$set":{'user_info':user_info}})
                random_mobs=random.choice(mobs)
                random_mobs['level']=level
                keyboard=[[InlineKeyboardButton('BATTLE',callback_data=f"mobbattle_{level}")]]
                message = update.message.reply_photo(photo=random_mobs['media'],caption=f"*Seems like a Monster appeared\nIt appeared to be a level {level} {random_mobs['name']}*\n`Element : `*{random_mobs['element']}\nWanna Fight it then click on Battle*",reply_markup=InlineKeyboardMarkup(keyboard),parse_mode=ParseMode.MARKDOWN)
                message_id = message.message_id
                cd.clear()
                cd[message_id] = {}
                cd[user.id] = {}
                cd[user.id]['mob'] = random_mobs
                cd[user.id]['MESSAGE_ID']=message.message_id
                return
            else:
                mobs=monster.mobs
                user_info['explores']['normal']+=1
                user_data[1].update_one({"_id":ObjectId(user_obj_id)},{"$set":{'user_info':user_info}})
                level=random.randint(1,12)
                random_mobs=random.choice(mobs)
                random_mobs['level']=level
                keyboard=[[InlineKeyboardButton('BATTLE',callback_data=f"mobbattle_{level}")]]
                message = update.message.reply_photo(photo=random_mobs['media'],caption=f"*Seems like a Monster appeared\nIt appeated to be a level {level} {random_mobs['name']}*\n`Element : `*{random_mobs['element']}\nWanna Fight it then click on Battle*",reply_markup=InlineKeyboardMarkup(keyboard),parse_mode=ParseMode.MARKDOWN)
                message_id = message.message_id
                cd.clear()
                cd[message_id] = {}
                cd[user.id] = {}
                cd[user.id]['mob'] = random_mobs
                cd[user.id]['MESSAGE_ID']=message.message_id
                return

def mob_level_buff(x,y,z):
    level=x
    try:
        mob=y[f'level_{level}']
    except:
        mob=y
    user_id=z
    if mob['name'] in ["CHARISMATIC FLAWLESS",'LIGHT MENDER',"ELECTRO WARRIO","GENESIS","OSIAL","DIAMONES","ICE DRAGON","IFRIT"]:
        mob[f'hp_{user_id}']=mob['hp']
        mob[f'atk_{user_id}']=mob['atk']
        mob[f'speed_{user_id}']=mob['speed']
        mob[f'def_{user_id}']=mob['def']
    else:
        extra_hp_mons=(mob['level']*random.randint(3,4)+mob['hp'])-(random.randint(4,5))
        extra_atk_mons=(mob['level']*random.choice([0.5,0.6,0.7,0.8])+mob['atk'])-(random.choice([0.5,0.6]))
        extra_spe_mons=(mob['level']*random.randint(5,8)+mob['speed'])-(random.randint(5,8))
        mob[f'hp_{user_id}']=extra_hp_mons
        mob[f'atk_{user_id}']=extra_atk_mons
        mob[f'speed_{user_id}']=mob['speed']
        mob[f'def_{user_id}']=mob['def']
    return mob

def battle_start(update,context):
    if maintenance_mode == "ON":
        if update.effective_user.id not in admins_id:
            try:
                update.callback_query.message.edit_text("*BOT UNDER MAINTENANCE*",parse_mode=ParseMode.MARKDOWN)
            except:
                update.callback_query.message.edit_caption(caption="*BOT UNDER MAINTENANCE*",parse_mode=ParseMode.MARKDOWN)
            return
    user=update.effective_user
    query=update.callback_query
    query.message.edit_caption(caption="`Processing .... `",parse_mode=ParseMode.MARKDOWN)
    cd = context.chat_data
    global insiders,active_users
    message_id = query.message.message_id
    try:
        CHECKER = cd[user.id]['MESSAGE_ID']
    except:
        query.message.edit_caption("*MONSTER ALREADY FLED*",parse_mode=ParseMode.MARKDOWN)
        time.sleep(2)
        if user.id in insiders:
            active_users.remove(user.first_name)
            insiders.remove(user.id)
            query.message.edit_caption("*Don't Spam\nSpam will Flee the Monster*",parse_mode=ParseMode.MARKDOWN)
        else:
            query.message.edit_caption("*Nigga*",parse_mode=ParseMode.MARKDOWN)
        return
    mob = cd[user.id]['mob']
    level=query.data.split("_")[1]
    mob=mob_level_buff(level,mob,user.id)
    user_data=[db.get_collection("user_datas"),db.get_collection("user_data"),db.get_collection("user_ids"),db.get_collection("beta_users")]
    user_obj_id = user_data[0].find_one()['user_data'][f'user_{user.id}']
    user_team=user_data[1].find_one({'_id': ObjectId(user_obj_id)})['team']
    user_characters=user_data[1].find_one({'_id': ObjectId(user_obj_id)})['user_char']
    user_character_log=user_team['team_player_1']
    if user_character_log['name']=='None':
        query.message.edit_caption("*SET TEAM BY USING /team*",parse_mode=ParseMode.MARKDOWN)
        return
    user_character=[]
    user_char_skil={}
    total_chars=4
    for i in range(4):
        if user_team[f'team_player_{i+1}']['name']=='None':
            total_chars-=1
        else:
            user_team[f'team_player_{i+1}']['dead']='False'
            team_player_name=user_team[f'team_player_{i+1}']['name']
            user_char_skil[f'{team_player_name}']={}
            user_char_skil[f'{team_player_name}']['rounds']=0
    for j in range(len(user_characters)):
        user_characters[j]['usage_pas']=charamoves(user_characters[j])['skill_move']['usage']
        buff_level=user_characters[j]['level']-1
        user_characters[j]['atk']+=round(buff_level*0.8)
        user_characters[j]['def']+=round(buff_level*0.5)
        user_characters[j]['hp']+=round(buff_level*8)
        user_characters[j]['new_hp']=user_characters[j]['hp']
        if user_characters[j]['name']=="SEKIRO":
            user_characters[j]['immortality']=1
    for sj in range(len(user_characters)):
        if user_characters[sj]['name']==user_character_log['name']:
            user_character=user_characters[sj]
    insiders.append(user.id)
    bro_user="*ACTIVE USERS :*\n\n"
    for m in range(len(insiders)):
        active_users=context.bot.getChat(insiders[m])
        bro_user+=f"*{m+1}* [{active_users.first_name}](tg://user?id={insiders[m]})\n"
    try:
        context.bot.editMessageText(text=bro_user, chat_id=-1001931792224, message_id=3,parse_mode=ParseMode.MARKDOWN)
    except:
        print("alright")
    moves=charamoves(user_character)
    mob[f'new_hp_{user.id}']=mob[f'hp_{user.id}']
    keyboard=[[InlineKeyboardButton(f"{moves['normal_move']['name']}",callback_data='mobb_normal')],[InlineKeyboardButton(f"{moves['skill_move']['name']} ({user_character['usage_pas']})",callback_data='mobb_skill')],[InlineKeyboardButton(f"{moves['dodge_move']['name']}",callback_data='mobb_dodge'),InlineKeyboardButton(f"SWAP",callback_data='mobbb_swap'),InlineKeyboardButton(f"EXIT",callback_data='mobbb_exit')]]      
    message=query.message.edit_caption(caption=f"`Enemy : `*{mob['name']}*\n`Enemy HP : `*{mob[f'hp_{user.id}']}*\n\n`Your Character : `*{user_character['name']} [{user_character['element']}]*\n`Character HP : `*{user_character['new_hp']}*\n\n\t\t`SELECT YOUR CHARACTER MOVE`",reply_markup=InlineKeyboardMarkup(keyboard),parse_mode=ParseMode.MARKDOWN)
    message_id = message.message_id
    cd.clear()
    cd[message_id] = {}
    cd[user.id] = {}
    cd[user.id]['mob'] = mob
    cd[user.id]['chars_avail']=total_chars
    cd[user.id]['char_playing']=user_team
    cd[user.id]['char_in_battle']=user_character
    cd[user.id]['user_characters']=user_characters
    cd[message_id]['MESSAGE_ID']=message.message_id
    cd[user.id]['passive']=user_char_skil
    return

def char_skill_explorer(update,context):
    if maintenance_mode == "ON":
        if update.effective_user.id not in admins_id:
            try:
                update.callback_query.message.edit_text("*BOT UNDER MAINTENANCE*",parse_mode=ParseMode.MARKDOWN)
            except:
                update.callback_query.message.edit_caption(caption="*BOT UNDER MAINTENANCE*",parse_mode=ParseMode.MARKDOWN)
            return
    query=update.callback_query
    print("working")
    user=update.callback_query.from_user
    message_id = query.message.message_id
    cd=context.chat_data
    global insiders
    try:
        user_message_id=cd[message_id]['MESSAGE_ID']
    except:
        query.message.edit_caption(caption=f"*MONSTER FLED*",parse_mode=ParseMode.MARKDOWN)
        time.sleep(2)
        if user.id in insiders:
            active_users.remove(user.first_name)
            query.message.edit_caption(caption=f"*Don't Spam\nSpam will Flee the Monster*",parse_mode=ParseMode.MARKDOWN)
        return
    user_team=cd[user.id]['char_playing']
    passive=cd[user.id]['passive']
    user_character=cd[user.id]['char_in_battle']
    user_characters=cd[user.id]['user_characters']
    mob = cd[user.id]['mob'] 
    moves=charamoves(user_character)
    chars_avail=cd[user.id]['chars_avail']
    mob_crit=[True,False]
    mob_possible=random.choices(mob_crit,weights=(mob['crit_rate'],100-mob['crit_rate']),k=1)
    if mob_possible[0]==True:
        monster_atk_dmg=round(mob[f'atk_{user.id}']+mob[f'atk_{user.id}']*mob['crit_dmg']/100)
    else:
        monster_atk_dmg=round(mob[f'atk_{user.id}'])
    mons_speed=mob[f"speed_{user.id}"]
    char_crit=[True,False]
    char_possible=random.choices(char_crit,weights=(user_character['crit_rate'],100-user_character['crit_rate']),k=1)
    if char_possible[0]==True:
        text='*You Hit Critical Attack*\n'
        chara_Atk_dmg=round((user_character['atk']+user_character['weapon'][0]['buff_atk'])+((user_character['weapon'][0]['buff_atk']+user_character['atk'])*user_character['crit_dmg']/100))
    else:
        text=''
        chara_Atk_dmg=round(user_character['atk']+user_character['weapon'][0]['buff_atk'])
    chara_def=user_character['def']
    mons_def=mob[f'def_{user.id}']
    char_speed=user_character['speed']
    if query.data.split("_")[-1]=='skill':
        if round(chara_def*0.9)<monster_atk_dmg:
            monster_atk_dmg-=round(chara_def*0.9)
        else:
            monster_atk_dmg=0
        if user_character['usage_pas']<1:
            query.answer("NO more skill move left",show_alert=True)
            return
        else:
            user_character['usage_pas']-=1
            text=''
            if user_character['name']=='RYZA ( BETA CHAR )':
                text+=f"*{user_character['name'] } USED {moves['skill_move']['name']}\n*"
                find=passive[f"{user_character['name']}"]
                passive[f"{user_character['name']}"]['rounds']+=2
                cd[user.id]['passive'] = passive
            if user_character['name']=='SHADOW ( BETA CHAR )':
                text+=f"*{user_character['name'] } USED {moves['skill_move']['name']}\n*"
                find=passive[f"{user_character['name']}"]
                passive[f"{user_character['name']}"]['rounds']+=9999
                cd[user.id]['passive'] = passive
            if user_character['name']=='YUKONG':
                text+=f"*{user_character['name'] } USED {moves['skill_move']['name']}\n*"
                find=passive[f"{user_character['name']}"]
                passive[f"{user_character['name']}"]['rounds']+=2
                cd[user.id]['passive'] = passive
            if user_character['name']=='FIONA':
                text+=f"*{user_character['name'] } USED {moves['skill_move']['name']}\n*"
                find=passive[f"{user_character['name']}"]
                passive[f"{user_character['name']}"]['rounds']+=3
                cd[user.id]['passive'] = passive
            if user_character['name']=='MORAX ( BETA CHAR )':
                text+=f"*{user_character['name'] } USED {moves['skill_move']['name']}\n*"
                find=passive[f"{user_character['name']}"]
                passive[f"{user_character['name']}"]['rounds']+=2
                passive[f"{user_character['name']}"]['skill_def']=round(user_character['hp']*1/10)
                cd[user.id]['passive'] = passive
            if user_character['name']=='CANDACE':
                text+=f"*{user_character['name'] } USED {moves['skill_move']['name']}\n*"
                find=passive[f"{user_character['name']}"]
                passive[f"{user_character['name']}"]['rounds']+=3
                passive[f"{user_character['name']}"]['skill_def']=round(user_character['def']/2.5)
                cd[user.id]['passive'] = passive
            if user_character['name']=='CLAUDIA':
                text+=f"*{user_character['name'] } USED {moves['skill_move']['name']}\n*"
                find=passive[f"{user_character['name']}"]
                passive[f"{user_character['name']}"]['rounds']+=4
                passive[f"{user_character['name']}"]['clau_dmg']=round(chara_Atk_dmg*1/4.9)
                cd[user.id]['passive'] = passive
            if user_character['name']=='DIAN FARRELL':
                text+=f"*{user_character['name'] } USED {moves['skill_move']['name']}\n*"
                find=passive[f"{user_character['name']}"]
                passive[f"{user_character['name']}"]['rounds']+=2
                cd[user.id]['passive'] = passive
            if user_character['name']=='TIAN LANG':
                text+=f"*{user_character['name'] } USED {moves['skill_move']['name']}\n*"
                find=passive[f"{user_character['name']}"]
                passive[f"{user_character['name']}"]['rounds']+=4
                passive[f"{user_character['name']}"]['tia_Speed']=char_speed*2.5
                cd[user.id]['passive'] = passive
            if user_character['name']=='JEAN':
                mob[f'new_hp_{user.id}']-=round(chara_Atk_dmg*1.2)
                text+=f"*{user_character['name'] } USED {moves['skill_move']['name']}\nMONSTER STUCK FOR NEXT 1 MOVE AND {round(chara_Atk_dmg*1.2)} DEALT DMG TO MONSTER\n\n*"
                find=passive[f"{user_character['name']}"]
                passive[f"{user_character['name']}"]['rounds']+=1
                cd[user.id]['passive'] = passive
            if user_character['name']=='FISCHL':
                text+=f"*{user_character['name'] } USED {moves['skill_move']['name']}\n*"
                find=passive[f"{user_character['name']}"]
                passive[f"{user_character['name']}"]['rounds']+=5
                passive[f"{user_character['name']}"]['fis_dmg']=chara_Atk_dmg
                cd[user.id]['passive'] = passive
            if user_character['name']=='ECHO':
                text+=f"*{user_character['name'] } USED {moves['skill_move']['name']}\n*"
                find=passive[f"{user_character['name']}"]
                passive[f"{user_character['name']}"]['rounds']+=3
                cd[user.id]['passive'] = passive
            if user_character['name']=='QIQI':
                text+=f"*{user_character['name'] } USED {moves['skill_move']['name']}\n*"
                find=passive[f"{user_character['name']}"]
                passive[f"{user_character['name']}"]['rounds']+=3
                passive[f"{user_character['name']}"]['qiqi_hp']=user_character['hp']
                cd[user.id]['passive'] = passive
            if user_character['name']=='KLAUDIA VALENTZ':
                text+=f"*{user_character['name'] } USED {moves['skill_move']['name']}\n*"
                find=passive[f"{user_character['name']}"]
                passive[f"{user_character['name']}"]['rounds']+=3
                passive[f"{user_character['name']}"]['klaudia_hp']=round(user_character['hp']/5)
                cd[user.id]['passive'] = passive
            if user_character['name']=='KAYLA':
                text+=f"*{user_character['name'] } USED {moves['skill_move']['name']}\n*"
                find=passive[f"{user_character['name']}"]
                passive[f"{user_character['name']}"]['rounds']+=999
                cd[user.id]['passive'] = passive
            if user_character['name']=='SEKIRO':
                text+=f"*{user_character['name'] } USED {moves['skill_move']['name']}\n*"
                find=passive[f"{user_character['name']}"]
                passive[f"{user_character['name']}"]['rounds']+=9999
                cd[user.id]['passive'] = passive
            if user_character['name']=='LISA':
                text+=f"*{user_character['name'] } USED {moves['skill_move']['name']}\n*"
                find=passive[f"{user_character['name']}"]
                passive[f"{user_character['name']}"]['rounds']+=3
                passive[f"{user_character['name']}"]['area_dmg']=round(chara_Atk_dmg)
                cd[user.id]['passive'] = passive
            if user_character['name']=='RAIDEN SHOGUN':
                if passive[f"{user_character['name']}"]['rounds'] > 0:
                    query.answer("SKILL IS ALREADY ACTIVE\nTHIS CHARACTER SKILL IS NOT STACKABLE",show_alert=True)
                    user_character['usage_pas']+=1
                    return
                text+=f"*{user_character['name'] } USED {moves['skill_move']['name']}\n*"
                find=passive[f"{user_character['name']}"]
                passive[f"{user_character['name']}"]['rounds']+=10
                passive[f"{user_character['name']}"]['lighting_dmg']=round(chara_Atk_dmg/2.5)
                cd[user.id]['passive'] = passive
            if user_character['name']=='BENNETT':
                text+=f"*{user_character['name'] } USED {moves['skill_move']['name']}\n*"
                find=passive[f"{user_character['name']}"]
                passive[f"{user_character['name']}"]['rounds']+=1
                passive[f"{user_character['name']}"]['benny_fire']=round(chara_Atk_dmg/5)
                cd[user.id]['passive'] = passive
                char_crit=[True,False]
                char_possible=random.choices(char_crit,weights=(user_character['crit_rate'],100-user_character['crit_rate']),k=1)
                if char_possible[0]==True:
                    text+='*You Hit Critical Attack*\n'
                    chara_Atk_dmg=round((user_character['atk']+user_character['weapon'][0]['buff_atk'])+((user_character['weapon'][0]['buff_atk']+user_character['atk'])*user_character['crit_dmg']/100))
                else:
                    text+=''
                    chara_Atk_dmg=round(user_character['atk']+user_character['weapon'][0]['buff_atk'])
                if round(mons_def*0.9)<chara_Atk_dmg:
                    chara_Atk_dmg-=round(mons_def*0.9)
                else:
                    chara_Atk_dmg=0
                mob[f'new_hp_{user.id}']-=round(chara_Atk_dmg*1.5)
                text+=f"{user_character['name']} Dealt {round(chara_Atk_dmg)} to {mob['name']}\n"
            if user_character['name']=='DOOMFIST':
                char_crit=[True,False]
                char_possible=random.choices(char_crit,weights=(user_character['crit_rate'],100-user_character['crit_rate']),k=1)
                if char_possible[0]==True:
                    text+='*You Hit Critical Attack*\n'
                    chara_Atk_dmg=round(((user_character['atk']+user_character['weapon'][0]['buff_atk'])+((user_character['weapon'][0]['buff_atk']+user_character['atk'])*user_character['crit_dmg']/100))*1.75)
                else:
                    text+=''
                    chara_Atk_dmg=round((user_character['atk']+user_character['weapon'][0]['buff_atk'])*1.75)
                if round(mons_def*0.9)<chara_Atk_dmg:
                    chara_Atk_dmg-=round(mons_def*0.9)
                else:
                    chara_Atk_dmg=0
                mob[f'new_hp_{user.id}']-=round(chara_Atk_dmg*1.5)
                text+=f"{user_character['name']} Dealt {round(chara_Atk_dmg*1.5)} to {mob['name']}\n"
            if user_character['name']=='KRATOS':
                char_crit=[True,False]
                char_possible=random.choices(char_crit,weights=(user_character['crit_rate'],100-user_character['crit_rate']),k=1)
                if char_possible[0]==True:
                    text+='*You Hit Critical Attack*\n'
                    chara_Atk_dmg=round(((user_character['atk']+user_character['weapon'][0]['buff_atk'])+((user_character['weapon'][0]['buff_atk']+user_character['atk'])*user_character['crit_dmg']/100))*1.8)
                else:
                    text+=''
                    chara_Atk_dmg=round((user_character['atk']+user_character['weapon'][0]['buff_atk'])*1.8)
                mob[f'new_hp_{user.id}']-=round(chara_Atk_dmg*1.5)
                text+=f"Kratos Dealt {round(chara_Atk_dmg*1.5)} to {mob['name']}\n"
            user_character['new_hp']-=monster_atk_dmg
            if mob[f'new_hp_{user.id}']<1:
                message=query.message.edit_caption(caption="`MONSTER `",parse_mode=ParseMode.MARKDOWN)
                message=query.message.edit_caption(caption="`MONSTER EXECUTED`",parse_mode=ParseMode.MARKDOWN)
                message=query.message.edit_caption(caption="`MONSTER EXECUTED SUCCEFULLY`",parse_mode=ParseMode.MARKDOWN)
                battle_finsh(update,context)
                return
            elif user_character['new_hp']<1:
                if user_character['name']=="SEKIRO":
                    if user_character['immortality']>0:
                        user_character['immortality']-=1
                        user_character['new_hp']=round(user_character['hp']/2)
                        keyboard=[[InlineKeyboardButton(f"{moves['normal_move']['name']}",callback_data='mobb_normal')],[InlineKeyboardButton(f"{moves['skill_move']['name']} ({user_character['usage_pas']})",callback_data='mobb_skill')],[InlineKeyboardButton(f"{moves['dodge_move']['name']}",callback_data='mobb_dodge'),InlineKeyboardButton(f"SWAP",callback_data='mobbb_swap'),InlineKeyboardButton(f"EXIT",callback_data='mobbb_exit')]]      
                        text+=f"`DUE TO THE POWER OF IMMORTALITY SEKIRO REVIVED`"
                        message=query.message.edit_caption(caption=text+f"\n\n`Enemy : `*{mob['name']}*\n`Enemy HP : `*{mob[f'new_hp_{user.id}']}/{mob[f'hp_{user.id}']}*\n\n`Your Character : `*{user_character['name']} [{user_character['element']}]*\n`Character HP : `*{user_character['new_hp']}/{user_character['hp']}*\n\n\t\t`SELECT YOUR CHARACTER MOVE`",reply_markup=InlineKeyboardMarkup(keyboard),parse_mode=ParseMode.MARKDOWN)
                        cd[user.id]['mob'] = mob
                        cd[user.id]['chars_avail']=chars_avail
                        cd[user.id]['char_in_battle']=user_character
                        cd[user.id]['user_characters']=user_characters
                        cd[user.id]['char_playing']=user_team
                        cd[message_id]['MESSAGE_ID']=message.message_id
                        return
                for i in range(4):
                    if user_character['name']==user_team[f'team_player_{i+1}']['name']:
                        user_team[f'team_player_{i+1}']['dead']='True'
                chars_avail-=1
                if chars_avail==0:
                    query.message.delete()
                    context.bot.send_message(chat_id=user.id,text="`YOU R DED`",parse_mode=ParseMode.MARKDOWN)
                    insiders.remove(user.id)
                    return
                keyboard=[[InlineKeyboardButton(f"SWAP",callback_data='mobbb_swap')]]
                text+=f"`And the monster damaged {monster_atk_dmg} to you`"
                message=query.message.edit_caption(caption=text+f"\n`AND YOUR CHARACTER DED`\n\n`Enemy : `*{mob['name']}*\n`Enemy HP : `*{mob[f'new_hp_{user.id}']}/{mob[f'hp_{user.id}']}*\n\n\t\t`SELECT YOUR CHARACTER`",reply_markup=InlineKeyboardMarkup(keyboard),parse_mode=ParseMode.MARKDOWN)
                cd[user.id]['mob'] = mob
                cd[user.id]['chars_avail']=chars_avail
                cd[user.id]['char_in_battle']=user_character
                cd[user.id]['user_characters']=user_characters
                cd[user.id]['char_playing']=user_team
                cd[message_id]['MESSAGE_ID']=message.message_id
                return
            else:
                keyboard=[[InlineKeyboardButton(f"{moves['normal_move']['name']}",callback_data='mobb_normal')],[InlineKeyboardButton(f"{moves['skill_move']['name']} ({user_character['usage_pas']})",callback_data='mobb_skill')],[InlineKeyboardButton(f"{moves['dodge_move']['name']}",callback_data='mobb_dodge'),InlineKeyboardButton(f"SWAP",callback_data='mobbb_swap'),InlineKeyboardButton(f"EXIT",callback_data='mobbb_exit')]]      
                text+=f"`And the monster damaged {monster_atk_dmg} to you`"
                message=query.message.edit_caption(caption=text+f"\n\n`Enemy : `*{mob['name']}*\n`Enemy HP : `*{mob[f'new_hp_{user.id}']}/{mob[f'hp_{user.id}']}*\n\n`Your Character : `*{user_character['name']} [{user_character['element']}]*\n`Character HP : `*{user_character['new_hp']}/{user_character['hp']}*\n\n\t\t`SELECT YOUR CHARACTER MOVE`",reply_markup=InlineKeyboardMarkup(keyboard),parse_mode=ParseMode.MARKDOWN)
                cd[user.id]['mob'] = mob
                cd[user.id]['chars_avail']=chars_avail
                cd[user.id]['char_in_battle']=user_character
                cd[user.id]['user_characters']=user_characters
                cd[user.id]['char_playing']=user_team
                cd[message_id]['MESSAGE_ID']=message.message_id
                return

def middle_of_battle(update,context):
    if maintenance_mode == "ON":
        if update.effective_user.id not in admins_id:
            try:
                update.callback_query.message.edit_text("*BOT UNDER MAINTENANCE*",parse_mode=ParseMode.MARKDOWN)
            except:
                update.callback_query.message.edit_caption(caption="*BOT UNDER MAINTENANCE*",parse_mode=ParseMode.MARKDOWN)
            return
    query=update.callback_query
    user=update.callback_query.from_user
    message_id = query.message.message_id
    cd=context.chat_data
    global insiders
    try:
        user_message_id=cd[message_id]['MESSAGE_ID']
    except:
        query.message.edit_caption(caption=f"*MONSTER FLED*",parse_mode=ParseMode.MARKDOWN)
        time.sleep(2)
        if user.id in insiders:
            active_users.remove(user.first_name)
            query.message.edit_caption(caption=f"*Don't Spam\nSpam will Flee the Monster*",parse_mode=ParseMode.MARKDOWN)
        return
    user_team=cd[user.id]['char_playing']
    passive=cd[user.id]['passive']
    user_character=cd[user.id]['char_in_battle']
    user_characters=cd[user.id]['user_characters']
    mob = cd[user.id]['mob'] 
    moves=charamoves(user_character)
    chars_avail=cd[user.id]['chars_avail']
    mob_crit=[True,False]
    mob_possible=random.choices(mob_crit,weights=(mob['crit_rate'],100-mob['crit_rate']),k=1)
    if mob_possible[0]==True:
        monster_atk_dmg=round(mob[f'atk_{user.id}']+mob[f'atk_{user.id}']*mob['crit_dmg']/100)
    else:
        monster_atk_dmg=round(mob[f'atk_{user.id}'])
    mons_speed=mob[f"speed_{user.id}"]
    char_crit=[True,False]
    char_possible=random.choices(char_crit,weights=(user_character['crit_rate'],100-user_character['crit_rate']),k=1)
    if char_possible[0]==True:
        text='*You Hit Critical Attack*\n'
        chara_Atk_dmg=round((user_character['atk']+user_character['weapon'][0]['buff_atk'])+((user_character['weapon'][0]['buff_atk']+user_character['atk'])*user_character['crit_dmg']/100))
    else:
        text=''
        chara_Atk_dmg=round(user_character['atk']+user_character['weapon'][0]['buff_atk'])
    chara_def=user_character['def']
    mons_def=mob[f'def_{user.id}']
    char_speed=user_character['speed']
    for i in range(len(list(passive.keys()))):
        if list(passive.keys())[i]=="RYZA ( BETA CHAR )":
            if passive[f'{list(passive.keys())[i]}']['rounds']>0:
                mons_speed=1
                passive[f'{list(passive.keys())[i]}']['rounds']-=1
            else:
                passive[f'{list(passive.keys())[i]}']['rounds']=0
        if list(passive.keys())[i]=="SHADOW ( BETA CHAR )":
            if passive[f'{list(passive.keys())[i]}']['rounds']>0:
                if user_character['name']=="SHADOW ( BETA CHAR )":
                    chara_Atk_dmg+=round(chara_Atk_dmg*0.6)
                passive[f'{list(passive.keys())[i]}']['rounds']-=1
            else:
                passive[f'{list(passive.keys())[i]}']['rounds']=0
        if list(passive.keys())[i]=="YUKONG":
            if passive[f'{list(passive.keys())[i]}']['rounds']>0:
                chara_Atk_dmg+=round(chara_Atk_dmg*25/100)
                passive[f'{list(passive.keys())[i]}']['rounds']-=1
            else:
                passive[f'{list(passive.keys())[i]}']['rounds']=0
        if list(passive.keys())[i]=="MORAX ( BETA CHAR )":
            if passive[f'{list(passive.keys())[i]}']['rounds']>0:
                chara_def+=passive[f'{list(passive.keys())[i]}']['skill_def']
                passive[f'{list(passive.keys())[i]}']['rounds']-=1
            else:
                passive[f'{list(passive.keys())[i]}']['rounds']=0
        if list(passive.keys())[i]=="CANDACE":
            if passive[f'{list(passive.keys())[i]}']['rounds']>0:
                chara_def+=passive[f'{list(passive.keys())[i]}']['skill_def']
                passive[f'{list(passive.keys())[i]}']['rounds']-=1
            else:
                passive[f'{list(passive.keys())[i]}']['rounds']=0
        if list(passive.keys())[i]=="CLAUDIA":
            if passive[f'{list(passive.keys())[i]}']['rounds']>0:
                mob[f'new_hp_{user.id}']-=passive[f'{list(passive.keys())[i]}']['clau_dmg']
                text+=f"*CLAUDIA DEALT {passive[f'{list(passive.keys())[i]}']['clau_dmg']} BURN 🔥 DMG TO MONSTER\n*"
                passive[f'{list(passive.keys())[i]}']['rounds']-=1
            else:
                passive[f'{list(passive.keys())[i]}']['rounds']=0
        if list(passive.keys())[i]=="BENNETT":
            if passive[f'{list(passive.keys())[i]}']['rounds']>0:
                mob[f'new_hp_{user.id}']-=passive[f'{list(passive.keys())[i]}']['benny_fire']
                text+=f"*BENNETT DEALT {passive[f'{list(passive.keys())[i]}']['benny_fire']} BURN 🔥 DMG TO MONSTER\n*"
                passive[f'{list(passive.keys())[i]}']['rounds']-=1
            else:
                passive[f'{list(passive.keys())[i]}']['rounds']=0
        if list(passive.keys())[i]=='DIAN FARRELL':
            if passive[f'{list(passive.keys())[i]}']['rounds']>0:
                chara_Atk_dmg=round(chara_Atk_dmg*1.5)
                mons_speed+=mob[f'speed_{user.id}']*random.randint(20,30)/100
                passive[f'{list(passive.keys())[i]}']['rounds']-=1
            else:
                passive[f'{list(passive.keys())[i]}']['rounds']=0
        if list(passive.keys())[i]=='LISA':
            if passive[f'{list(passive.keys())[i]}']['rounds']>0:
                dmg_nfsknf=round(passive[f'{list(passive.keys())[i]}']['area_dmg'])
                DMG_success=random.choice([True,False])
                if DMG_success==True:
                    mob[f'new_hp_{user.id}']-=dmg_nfsknf
                    text+=f"*LISA dealt {dmg_nfsknf} ELECTRO AREA ⚡️ DMG TO MONSTER*\n"
                else:
                    text+=f"*LISA AREA DMG FAILED*\n"
                passive[f'{list(passive.keys())[i]}']['rounds']-=1
            else:
                passive[f'{list(passive.keys())[i]}']['rounds']=0
        if list(passive.keys())[i]=='RAIDEN SHOGUN':
            if passive[f'{list(passive.keys())[i]}']['rounds']>0:
                dmg_nfsknf=round(passive[f'{list(passive.keys())[i]}']['lighting_dmg'])
                fjabchbeckb=[True,False]
                DMG_success=random.choices(fjabchbeckb,weights=(40,60),k=1)
                print(DMG_success)
                if DMG_success[0]==True:
                    mob[f'new_hp_{user.id}']-=dmg_nfsknf
                    text+=f"*RAIDEN dealt {dmg_nfsknf} LIGHTNING ⚡️ DMG TO MONSTER*\n"
                else:
                    text+=f"*RAIDEN LIGHTNING DMG FAILED*\n"
                passive[f'{list(passive.keys())[i]}']['rounds']-=1
            else:
                passive[f'{list(passive.keys())[i]}']['rounds']=0
        if list(passive.keys())[i]=="FIONA":
            if passive[f'{list(passive.keys())[i]}']['rounds']>0:
                if user_character['weapon_type']=='sword':
                    chara_Atk_dmg+=round(chara_Atk_dmg*0.6)
                    text+="*CHARACTER ATTACK DMG BUFFED TO 1.5x DUE TO Sword enhance*\n"
                passive[f'{list(passive.keys())[i]}']['rounds']-=1
            else:
                passive[f'{list(passive.keys())[i]}']['rounds']=0
        if list(passive.keys())[i]=="JEAN":
            if passive[f'{list(passive.keys())[i]}']['rounds']>0:
                monster_atk_dmg=0
                text+="MONSTER UNABLE TO DMG U COZ THEY ARE STUCK IN WIND\n"
                passive[f'{list(passive.keys())[i]}']['rounds']-=1
            else:
                passive[f'{list(passive.keys())[i]}']['rounds']=0
        if list(passive.keys())[i]=="FISCHL":
            if passive[f'{list(passive.keys())[i]}']['rounds']>0:
                dmg_nfsknf=round(passive[f'{list(passive.keys())[i]}']['fis_dmg']*1/5)
                mob[f'new_hp_{user.id}']-=dmg_nfsknf
                text+=f"OZ dealt {dmg_nfsknf} ELECTRO ⚡️ DMG TO MONSTER\n"
                passive[f'{list(passive.keys())[i]}']['rounds']-=1
            else:
                passive[f'{list(passive.keys())[i]}']['rounds']=0
        if list(passive.keys())[i]=="ECHO":
            if passive[f'{list(passive.keys())[i]}']['rounds']>0:
                char_speed+=char_speed*90/100
                passive[f'{list(passive.keys())[i]}']['rounds']-=1
            else:
                passive[f'{list(passive.keys())[i]}']['rounds']=0
        if list(passive.keys())[i]=="QIQI":
            if passive[f'{list(passive.keys())[i]}']['rounds']>0:
                yes_or_not=[True,False]
                frozen=random.choices(yes_or_not,weights=(40,60),k=1)
                if frozen[0]==True:
                    text+="MONSTER UNABLE TO MOVE COZ OF FROZEN ❄️\n"
                    monster_atk_dmg=0
                    user_character['crit_rate']+=15
                heal=int(passive[f'{list(passive.keys())[i]}']['qiqi_hp']/5)
                if user_character['new_hp']==user_character['hp']:
                    text+='QIQI heal not working due to full hp\n'
                elif user_character['new_hp']+heal>user_character['hp']:
                    user_character['new_hp']=user_character['hp']
                    text+='character hp fully healed by QIQI\n'
                else:
                    user_character['new_hp']+=heal
                    text+=f'Qiqi skill healed {heal} HP\n'
                passive[f'{list(passive.keys())[i]}']['rounds']-=1
            else:
                passive[f'{list(passive.keys())[i]}']['rounds']=0
        if list(passive.keys())[i]=='KLAUDIA VALENTZ':
            if passive[f'{list(passive.keys())[i]}']['rounds']>0:
                yes_or_not=[True,False]
                frozen=random.choices(yes_or_not,weights=(60,40),k=1)
                if frozen[0]==True:
                    text+="MONSTER UNABLE TO MOVE COZ OF FROZEN ❄️\n"
                    monster_atk_dmg=0
                user_character['crit_rate']+=15
                heal=int(passive[f'{list(passive.keys())[i]}']['klaudia_hp'])
                if user_character['new_hp']==user_character['hp']:
                    text+='KLAUDIA heal not working due to full hp\n'
                elif user_character['new_hp']+heal>user_character['hp']:
                    user_character['new_hp']=user_character['hp']
                    text+='character hp fully healed by KLAUDIA\n'
                else:
                    user_character['new_hp']+=heal
                    text+=f'KLAUDIA skill healed {heal} HP\n'
                passive[f'{list(passive.keys())[i]}']['rounds']-=1
            else:
                passive[f'{list(passive.keys())[i]}']['rounds']=0
        if list(passive.keys())[i]=='TIAN LANG':
            if passive[f'{list(passive.keys())[i]}']['rounds']>0:
                mob[f'new_hp_{user.id}']-=1
                minus_spe=random.randint(60,80)/100
                if user_character['name']=='TIAN LANG':
                    char_speed=passive[f'{list(passive.keys())[i]}']['tia_Speed']
                    mons_speed-=mob[f'speed_{user.id}']*minus_spe
                    text+=f"Tian speed buffed to {char_speed}\nMob speed lower by {minus_spe}% due to Tian Skill\n"
                text+=f"MOB HP -1 due to Tian Skill\n"
                passive[f'{list(passive.keys())[i]}']['rounds']-=1
            else:
                passive[f'{list(passive.keys())[i]}']['rounds']=0
        if list(passive.keys())[i]=='KAYLA':
            if passive[f'{list(passive.keys())[i]}']['rounds']>0:
                char_crit=[True,False]
                char_possible=random.choices(char_crit,weights=(user_character['crit_rate'],100-user_character['crit_rate']),k=1)
                if char_possible[0]==True:
                    text+='*You Hit A Critical Attack*\n'
                    char_crit_dmg=user_character['crit_dmg']+50
                    chara_Atk_dmg=round((user_character['atk']+user_character['weapon'][0]['buff_atk'])+((user_character['weapon'][0]['buff_atk']+user_character['atk'])*char_crit_dmg/100))
                else:
                    text=''
                    chara_Atk_dmg=round(user_character['atk']+user_character['weapon'][0]['buff_atk'])
                passive[f'{list(passive.keys())[i]}']['rounds']-=1
            else:
                passive[f'{list(passive.keys())[i]}']['rounds']=0
        if list(passive.keys())[i]=="SEKIRO":
            if passive[f'{list(passive.keys())[i]}']['rounds']>0:
                if user_character['name']=="SEKIRO":
                    if user_character['element']=="Fire":
                        user_character['element']="Dark"
                    else:
                        user_character['element']="Fire"
                passive[f'{list(passive.keys())[i]}']['rounds']-=1
            else:
                passive[f'{list(passive.keys())[i]}']['rounds']=0
        cd[user.id]['passive'] = passive
    if query.data.split("_")[-1]=='normal':
        if round(mons_def*0.9)<chara_Atk_dmg:
            chara_Atk_dmg-=round(mons_def*0.9)
        else:
            chara_Atk_dmg=0
        if round(chara_def*0.9)<monster_atk_dmg:
            monster_atk_dmg-=round(chara_def*0.9)
        else:
            monster_atk_dmg=0
        monster_dodge=[True,False]
        monster_doge=random.choices(monster_dodge,weights=(mons_speed/10,100-mons_speed/10))
        if monster_doge[0]==True:
            mons_recoil_dmg=round(1.2*chara_Atk_dmg)
            user_character['new_hp']-=mons_recoil_dmg
            if user_character['new_hp']<1:
                if user_character['name']=="SEKIRO":
                    if user_character['immortality']>0:
                        user_character['immortality']-=1
                        user_character['new_hp']=round(user_character['hp']/2)
                        keyboard=[[InlineKeyboardButton(f"{moves['normal_move']['name']}",callback_data='mobb_normal')],[InlineKeyboardButton(f"{moves['skill_move']['name']} ({user_character['usage_pas']})",callback_data='mobb_skill')],[InlineKeyboardButton(f"{moves['dodge_move']['name']}",callback_data='mobb_dodge'),InlineKeyboardButton(f"SWAP",callback_data='mobbb_swap'),InlineKeyboardButton(f"EXIT",callback_data='mobbb_exit')]]      
                        text+=f"`Seems like The Monster `*{mob['name']}*` Dodged Your Attack and you got hit by Recoil\nDUE TO THE POWER OF IMMORTALITY SEKIRO REVIVED`"
                        message=query.message.edit_caption(caption=text+f"\n\n`Enemy : `*{mob['name']}*\n`Enemy HP : `*{mob[f'new_hp_{user.id}']}/{mob[f'hp_{user.id}']}*\n\n`Your Character : `*{user_character['name']} [{user_character['element']}]*\n`Character HP : `*{user_character['new_hp']}/{user_character['hp']}*\n\n\t\t`SELECT YOUR CHARACTER MOVE`",reply_markup=InlineKeyboardMarkup(keyboard),parse_mode=ParseMode.MARKDOWN)
                        cd[user.id]['mob'] = mob
                        cd[user.id]['chars_avail']=chars_avail
                        cd[user.id]['char_in_battle']=user_character
                        cd[user.id]['user_characters']=user_characters
                        cd[user.id]['char_playing']=user_team
                        cd[message_id]['MESSAGE_ID']=message.message_id
                        return
                for i in range(4):
                    if user_character['name']==user_team[f'team_player_{i+1}']['name']:
                        user_team[f'team_player_{i+1}']['dead']='True'
                chars_avail-=1
                if chars_avail==0:
                    query.message.delete()
                    context.bot.send_message(chat_id=user.id,text="`YOU R DED`",parse_mode=ParseMode.MARKDOWN)
                    insiders.remove(user.id)
                    return
                keyboard=[[InlineKeyboardButton(f"SWAP",callback_data='mobbb_swap')]]
                text+=f"`Seems like The Monster `*{mob['name']}*` Dodged Your Attack and you got hit by Recoil\nRecoil Damage : `*{mons_recoil_dmg}*"
                message=query.message.edit_caption(caption=text+f"\n`AND YOUR CHARACTER DED`\n\n`Enemy : `*{mob['name']}*\n`Enemy HP : `*{mob[f'new_hp_{user.id}']}/{mob[f'hp_{user.id}']}*\n\n\t\t`SELECT YOUR CHARACTER`",reply_markup=InlineKeyboardMarkup(keyboard),parse_mode=ParseMode.MARKDOWN)
                cd[user.id]['mob'] = mob
                cd[user.id]['chars_avail']=chars_avail
                cd[user.id]['char_in_battle']=user_character
                cd[user.id]['user_characters']=user_characters
                cd[user.id]['char_playing']=user_team
                cd[message_id]['MESSAGE_ID']=message.message_id
                return
            else:
                keyboard=[[InlineKeyboardButton(f"{moves['normal_move']['name']}",callback_data='mobb_normal')],[InlineKeyboardButton(f"{moves['skill_move']['name']} ({user_character['usage_pas']})",callback_data='mobb_skill')],[InlineKeyboardButton(f"{moves['dodge_move']['name']}",callback_data='mobb_dodge'),InlineKeyboardButton(f"SWAP",callback_data='mobbb_swap'),InlineKeyboardButton(f"EXIT",callback_data='mobbb_exit')]]      
                text+=f"`Seems like The Monster `*{mob['name']}*` Dodged Your Attack and you got hit by Recoil\nRecoil Damage : `*{mons_recoil_dmg}*"
                message=query.message.edit_caption(caption=text+f"\n\n`Enemy : `*{mob['name']}*\n`Enemy HP : `*{mob[f'new_hp_{user.id}']}/{mob[f'hp_{user.id}']}*\n\n`Your Character : `*{user_character['name']} [{user_character['element']}]*\n`Character HP : `*{user_character['new_hp']}/{user_character['hp']}*\n\n\t\t`SELECT YOUR CHARACTER MOVE`",reply_markup=InlineKeyboardMarkup(keyboard),parse_mode=ParseMode.MARKDOWN)
                cd[user.id]['mob'] = mob
                cd[user.id]['chars_avail']=chars_avail
                cd[user.id]['char_in_battle']=user_character
                cd[user.id]['user_characters']=user_characters
                cd[user.id]['char_playing']=user_team
                cd[message_id]['MESSAGE_ID']=message.message_id
                return
        else:
            user_character['new_hp']-=monster_atk_dmg
            mob[f'new_hp_{user.id}']-=chara_Atk_dmg
            if mob[f'new_hp_{user.id}']<1:
                message=query.message.edit_caption(caption="`MONSTER `",parse_mode=ParseMode.MARKDOWN)
                message=query.message.edit_caption(caption="`MONSTER EXECUTED`",parse_mode=ParseMode.MARKDOWN)
                message=query.message.edit_caption(caption="`MONSTER EXECUTED SUCCEFULLY`",parse_mode=ParseMode.MARKDOWN)
                battle_finsh(update,context)
                return
            elif user_character['new_hp']<1:
                if user_character['name']=="SEKIRO":
                    if user_character['immortality']>0:
                        user_character['immortality']-=1
                        user_character['new_hp']=round(user_character['hp']/2)
                        keyboard=[[InlineKeyboardButton(f"{moves['normal_move']['name']}",callback_data='mobb_normal')],[InlineKeyboardButton(f"{moves['skill_move']['name']} ({user_character['usage_pas']})",callback_data='mobb_skill')],[InlineKeyboardButton(f"{moves['dodge_move']['name']}",callback_data='mobb_dodge'),InlineKeyboardButton(f"SWAP",callback_data='mobbb_swap'),InlineKeyboardButton(f"EXIT",callback_data='mobbb_exit')]]      
                        text+=f"`YOU ALMOST GOT KILLED \nBUT THE POWER OF IMMORTALITY REVIVED SEKIRO`"
                        message=query.message.edit_caption(caption=text+f"\n\n`Enemy : `*{mob['name']}*\n`Enemy HP : `*{mob[f'new_hp_{user.id}']}/{mob[f'hp_{user.id}']}*\n\n`Your Character : `*{user_character['name']} [{user_character['element']}]*\n`Character HP : `*{user_character['new_hp']}/{user_character['hp']}*\n\n\t\t`SELECT YOUR CHARACTER MOVE`",reply_markup=InlineKeyboardMarkup(keyboard),parse_mode=ParseMode.MARKDOWN)
                        cd[user.id]['mob'] = mob
                        cd[user.id]['chars_avail']=chars_avail
                        cd[user.id]['char_in_battle']=user_character
                        cd[user.id]['user_characters']=user_characters
                        cd[user.id]['char_playing']=user_team
                        cd[message_id]['MESSAGE_ID']=message.message_id
                        return
                for i in range(4):
                    if user_character['name']==user_team[f'team_player_{i+1}']['name']:
                        user_team[f'team_player_{i+1}']['dead']='True'
                chars_avail-=1
                if chars_avail==0:
                    query.message.delete()
                    context.bot.send_message(chat_id=user.id,text="`YOU R DED`",parse_mode=ParseMode.MARKDOWN)
                    insiders.remove(user.id)
                    return
                keyboard=[[InlineKeyboardButton(f"SWAP",callback_data='mobbb_swap')]]
                text+=f"`You Damaged {chara_Atk_dmg} to monster and the monster damaged {monster_atk_dmg} to you`"
                message=query.message.edit_caption(caption=text+f"\n`AND YOUR CHARACTER DED`\n\n`Enemy : `*{mob['name']}*\n`Enemy HP : `*{mob[f'new_hp_{user.id}']}/{mob[f'hp_{user.id}']}*\n\n\t\t`SELECT YOUR CHARACTER`",reply_markup=InlineKeyboardMarkup(keyboard),parse_mode=ParseMode.MARKDOWN)
                cd[user.id]['mob'] = mob
                cd[user.id]['chars_avail']=chars_avail
                cd[user.id]['char_in_battle']=user_character
                cd[user.id]['user_characters']=user_characters
                cd[user.id]['char_playing']=user_team
                cd[message_id]['MESSAGE_ID']=message.message_id
                return
            else:
                keyboard=[[InlineKeyboardButton(f"{moves['normal_move']['name']}",callback_data='mobb_normal')],[InlineKeyboardButton(f"{moves['skill_move']['name']} ({user_character['usage_pas']})",callback_data='mobb_skill')],[InlineKeyboardButton(f"{moves['dodge_move']['name']}",callback_data='mobb_dodge'),InlineKeyboardButton(f"SWAP",callback_data='mobbb_swap'),InlineKeyboardButton(f"EXIT",callback_data='mobbb_exit')]]      
                text+=f"`You Damaged {chara_Atk_dmg} to monster and the monster damaged {monster_atk_dmg} to you`"
                message=query.message.edit_caption(caption=text+f"\n\n`Enemy : `*{mob['name']}*\n`Enemy HP : `*{mob[f'new_hp_{user.id}']}/{mob[f'hp_{user.id}']}*\n\n`Your Character : `*{user_character['name']} [{user_character['element']}]*\n`Character HP : `*{user_character['new_hp']}/{user_character['hp']}*\n\n\t\t`SELECT YOUR CHARACTER MOVE`",reply_markup=InlineKeyboardMarkup(keyboard),parse_mode=ParseMode.MARKDOWN)
                cd[user.id]['mob'] = mob
                cd[user.id]['chars_avail']=chars_avail
                cd[user.id]['char_in_battle']=user_character
                cd[user.id]['user_characters']=user_characters
                cd[user.id]['char_playing']=user_team
                cd[message_id]['MESSAGE_ID']=message.message_id
                return
    elif query.data.split("_")[-1]=='ult':
        print("normal")
    elif query.data.split("_")[-1]=='dodge':
        if round(mons_def*0.9)<chara_Atk_dmg:
            chara_Atk_dmg-=round(mons_def*0.9)
        else:
            chara_Atk_dmg=0
        if round(chara_def*0.9)<monster_atk_dmg:
            monster_atk_dmg-=round(chara_def*0.9)
        else:
            monster_atk_dmg=0
        dodge=[True,False]
        if 'BETA' in user_character['name'].split(" "):
            possibility=char_speed/10+8
        else:
            possibility=char_speed/10+25
        dodge_possiblity=random.choices(dodge,weights=(possibility,100-possibility),k=1)
        query.message.edit_caption(caption=f"*You*",parse_mode=ParseMode.MARKDOWN)
        query.message.edit_caption(caption=f"*You Used *",parse_mode=ParseMode.MARKDOWN)
        query.message.edit_caption(caption=f"*You Used Dodge *",parse_mode=ParseMode.MARKDOWN)
        query.message.edit_caption(caption=f"*You Used Dodge\nAND It*",parse_mode=ParseMode.MARKDOWN)
        if dodge_possiblity[0]==True:
            recoil_dmg=round(1.5*monster_atk_dmg)
            keyboard=[[InlineKeyboardButton(f"{moves['normal_move']['name']}",callback_data='mobb_normal')],[InlineKeyboardButton(f"{moves['skill_move']['name']} ({user_character['usage_pas']})",callback_data='mobb_skill')],[InlineKeyboardButton(f"{moves['dodge_move']['name']}",callback_data='mobb_dodge'),InlineKeyboardButton(f"SWAP",callback_data='mobbb_swap'),InlineKeyboardButton(f"EXIT",callback_data='mobbb_exit')]]      
            query.message.edit_caption(caption=f"`You Used Dodge\nAND It is successful`",parse_mode=ParseMode.MARKDOWN)
            mob[f'new_hp_{user.id}']-=recoil_dmg
            if mob[f'new_hp_{user.id}']<1:
                message=query.message.edit_caption(caption="`MONSTER `",parse_mode=ParseMode.MARKDOWN)
                message=query.message.edit_caption(caption="`MONSTER EXECUTED`",parse_mode=ParseMode.MARKDOWN)
                message=query.message.edit_caption(caption="`MONSTER EXECUTED SUCCEFULLY`",parse_mode=ParseMode.MARKDOWN)
                battle_finsh(update,context)
                return
            message=query.message.edit_caption(caption=f"`You Dodged the Enemy's atk and the enemy got hit by a `*{recoil_dmg}*` Recoil Damage`\n\n`Enemy : `*{mob['name']}*\n`Enemy HP : `*{mob[f'new_hp_{user.id}']}/{mob['hp']}*\n\n`Your Character : `*{user_character['name']} [{user_character['element']}]*\n`Character HP : `*{user_character['new_hp']}/{user_character['hp']}*\n\n\t\t`SELECT YOUR CHARACTER MOVE`",reply_markup=InlineKeyboardMarkup(keyboard),parse_mode=ParseMode.MARKDOWN)
            cd[user.id]['mob'] = mob
            cd[user.id]['chars_avail']=chars_avail
            cd[user.id]['char_playing']=user_team
            cd[user.id]['char_in_battle']=user_character
            cd[user.id]['user_characters']=user_characters
            cd[message_id]['MESSAGE_ID']=message.message_id
            return
        else:
            keyboard=[[InlineKeyboardButton(f"{moves['normal_move']['name']}",callback_data='mobb_normal')],[InlineKeyboardButton(f"{moves['skill_move']['name']} ({user_character['usage_pas']})",callback_data='mobb_skill')],[InlineKeyboardButton(f"{moves['dodge_move']['name']}",callback_data='mobb_dodge'),InlineKeyboardButton(f"SWAP",callback_data='mobbb_swap'),InlineKeyboardButton(f"EXIT",callback_data='mobbb_exit')]]      
            query.message.edit_caption(caption=f"*You Tried To Dodge\nAND It is Unsuccessful*",parse_mode=ParseMode.MARKDOWN)
            user_character['new_hp']-=round(monster_atk_dmg)
            if user_character['new_hp']<1:
                if user_character['name']=="SEKIRO":
                    if user_character['immortality']>0:
                        user_character['immortality']-=1
                        user_character['new_hp']=round(user_character['hp']/2)
                        keyboard=[[InlineKeyboardButton(f"{moves['normal_move']['name']}",callback_data='mobb_normal')],[InlineKeyboardButton(f"{moves['skill_move']['name']} ({user_character['usage_pas']})",callback_data='mobb_skill')],[InlineKeyboardButton(f"{moves['dodge_move']['name']}",callback_data='mobb_dodge'),InlineKeyboardButton(f"SWAP",callback_data='mobbb_swap'),InlineKeyboardButton(f"EXIT",callback_data='mobbb_exit')]]      
                        text+=f"`YOUR DODGE FAILED AND U HIT BY RECOIL\nBUT THE POWER OF IMMORTALITY REVIVED SEKIRO`"
                        message=query.message.edit_caption(caption=text+f"\n\n`Enemy : `*{mob['name']}*\n`Enemy HP : `*{mob[f'new_hp_{user.id}']}/{mob[f'hp_{user.id}']}*\n\n`Your Character : `*{user_character['name']} [{user_character['element']}]*\n`Character HP : `*{user_character['new_hp']}/{user_character['hp']}*\n\n\t\t`SELECT YOUR CHARACTER MOVE`",reply_markup=InlineKeyboardMarkup(keyboard),parse_mode=ParseMode.MARKDOWN)
                        cd[user.id]['mob'] = mob
                        cd[user.id]['chars_avail']=chars_avail
                        cd[user.id]['char_in_battle']=user_character
                        cd[user.id]['user_characters']=user_characters
                        cd[user.id]['char_playing']=user_team
                        cd[message_id]['MESSAGE_ID']=message.message_id
                        return
                chars_avail-=1
                for i in range(4):
                    if user_character['name']==user_team[f'team_player_{i+1}']['name']:
                        user_team[f'team_player_{i+1}']['dead']='True'
                if chars_avail==0:
                    query.message.delete()
                    context.bot.send_message(chat_id=user.id,text="`YOU R DED`",parse_mode=ParseMode.MARKDOWN)
                    insiders.remove(user.id)
                    return
                keyboard=[[InlineKeyboardButton(f"SWAP",callback_data='mobbb_swap')]]
                message=query.message.edit_caption(caption=f"`You Failed to Dodge the Opponent And Got a `*{monster_atk_dmg}*` Damage hit by Enemy\nAnd Your Character Died`\n\n`Enemy : `*{mob['name']}*\n`Enemy HP : `*{mob[f'new_hp_{user.id}']}/{mob[f'hp_{user.id}']}*\n\n\t\t`SELECT YOUR CHARACTER`",reply_markup=InlineKeyboardMarkup(keyboard),parse_mode=ParseMode.MARKDOWN)
                cd[user.id]['mob'] = mob
                cd[user.id]['chars_avail']=chars_avail
                cd[user.id]['char_playing']=user_team
                cd[user.id]['char_in_battle']=user_character
                cd[user.id]['user_characters']=user_characters
                cd[message_id]['MESSAGE_ID']=message.message_id
                return
            else:
                keyboard=[[InlineKeyboardButton(f"{moves['normal_move']['name']}",callback_data='mobb_normal')],[InlineKeyboardButton(f"{moves['skill_move']['name']} ({user_character['usage_pas']})",callback_data='mobb_skill')],[InlineKeyboardButton(f"{moves['dodge_move']['name']}",callback_data='mobb_dodge'),InlineKeyboardButton(f"SWAP",callback_data='mobbb_swap'),InlineKeyboardButton(f"EXIT",callback_data='mobbb_exit')]]      
                message=query.message.edit_caption(caption=f"`You Failed to Dodge the Opponent And Got a `*{monster_atk_dmg}*` Damage hit by Enemy`\n\n`Enemy : `*{mob['name']}*\n`Enemy HP : `*{mob[f'new_hp_{user.id}']}/{mob[f'hp_{user.id}']}*\n\n`Your Character : `*{user_character['name']} [{user_character['element']}]*\n`Character HP : `*{user_character['new_hp']}/{user_character['hp']}*\n\n\t\t`SELECT YOUR CHARACTER MOVE`",reply_markup=InlineKeyboardMarkup(keyboard),parse_mode=ParseMode.MARKDOWN)
                cd[user.id]['mob'] = mob
                cd[user.id]['chars_avail']=chars_avail
                cd[user.id]['char_in_battle']=user_character
                cd[user.id]['user_characters']=user_characters
                cd[user.id]['char_playing']=user_team
                cd[message_id]['MESSAGE_ID']=message.message_id
                return

def battle_swapper(update,context):
    if maintenance_mode == "ON":
        if update.effective_user.id not in admins_id:
            try:
                update.callback_query.message.edit_text("*BOT UNDER MAINTENANCE*",parse_mode=ParseMode.MARKDOWN)
            except:
                update.callback_query.message.edit_caption(caption="*BOT UNDER MAINTENANCE*",parse_mode=ParseMode.MARKDOWN)
            return
    query=update.callback_query
    print("working")
    user=update.callback_query.from_user
    message_id = query.message.message_id
    cd=context.chat_data
    global insiders
    try:
        user_message_id=cd[message_id]['MESSAGE_ID']
    except:
        query.message.edit_caption(caption=f"*MONSTER FLED*",parse_mode=ParseMode.MARKDOWN)
        time.sleep(2)
        if user.id in insiders:
            active_users.remove(user.first_name)
            query.message.edit_caption(caption=f"*Don't Spam\nSpam will Flee the Monster*",parse_mode=ParseMode.MARKDOWN)
        return
    user_team=cd[user.id]['char_playing']
    passive=cd[user.id]['passive']
    user_character=cd[user.id]['char_in_battle']
    user_characters=cd[user.id]['user_characters']
    mob = cd[user.id]['mob'] 
    moves=charamoves(user_character)
    chars_avail=cd[user.id]['chars_avail']
    mob_crit=[True,False]
    mob_possible=random.choices(mob_crit,weights=(mob['crit_rate'],100-mob['crit_rate']),k=1)
    if mob_possible[0]==True:
        monster_atk_dmg=round(mob[f'atk_{user.id}']+mob[f'atk_{user.id}']*mob['crit_dmg']/100)
    else:
        monster_atk_dmg=round(mob[f'atk_{user.id}'])
    mons_speed=mob[f"speed_{user.id}"]
    char_crit=[True,False]
    char_possible=random.choices(char_crit,weights=(user_character['crit_rate'],100-user_character['crit_rate']),k=1)
    if char_possible[0]==True:
        text='*You Hit Critical Attack*\n'
        chara_Atk_dmg=round((user_character['atk']+user_character['weapon'][0]['buff_atk'])+((user_character['weapon'][0]['buff_atk']+user_character['atk'])*user_character['crit_dmg']/100))
    else:
        text=''
        chara_Atk_dmg=round(user_character['atk']+user_character['weapon'][0]['buff_atk'])
    chara_def=user_character['def']
    mons_def=mob[f'def_{user.id}']
    char_speed=user_character['speed']
    if query.data.split("_")[-1]=='swap':
        keyboard=[]
        for i in range (4):
            if user_team[f'team_player_{i+1}']['name']!=user_character['name']:
                if user_team[f'team_player_{i+1}']['name']!='None':
                    print(user_team[f'team_player_{i+1}'])
                    if user_team[f'team_player_{i+1}']['dead']!='True':
                        keyboard.append([InlineKeyboardButton(f"{user_team[f'team_player_{i+1}']['name']}",callback_data=f'mobbb_swapper_{i+1}')])
            else:
                if user_team[f'team_player_{i+1}']['dead']!='True':
                    keyboard.append([InlineKeyboardButton(f"BACK",callback_data=f'mobbb_swapper_{i+1}')])
        query.message.edit_caption(caption=f"*SELECT THE CHARACTER YOU WANT TO SWAP*",reply_markup=InlineKeyboardMarkup(keyboard),parse_mode=ParseMode.MARKDOWN)
        return
    elif query.data.split("_")[-2]=='swapper':
        oldchar=user_character
        user_character_log=user_team[f"team_player_{query.data.split('_')[-1]}"]
        for i in range(len(user_characters)):
            if user_characters[i]['name']==user_character_log['name']:
                user_character=user_characters[i]
        moves=charamoves(user_character)
        keyboard=[[InlineKeyboardButton(f"{moves['normal_move']['name']}",callback_data='mobb_normal')],[InlineKeyboardButton(f"{moves['skill_move']['name']} ({user_character['usage_pas']})",callback_data='mobb_skill')],[InlineKeyboardButton(f"{moves['dodge_move']['name']}",callback_data='mobb_dodge'),InlineKeyboardButton(f"SWAP",callback_data='mobbb_swap'),InlineKeyboardButton(f"EXIT",callback_data='mobbb_exit')]]      
        text=f"`Character {oldchar['name']} changed to character {user_character['name']}`\n\n"
        query.message.edit_caption(caption=text+f"`Enemy : `*{mob['name']}*\n`Enemy HP : `*{mob[f'new_hp_{user.id}']}/{mob[f'hp_{user.id}']}*\n\n`Your Character : `*{user_character['name']} [{user_character['element']}]*\n`Character HP : `*{user_character['new_hp']}/{user_character['hp']}*\n\n\t\t`SELECT YOUR CHARACTER MOVE`",reply_markup=InlineKeyboardMarkup(keyboard),parse_mode=ParseMode.MARKDOWN)
        cd[user.id]['mob'] = mob
        cd[user.id]['char_playing']=user_team
        cd[user.id]['char_in_battle']=user_character
        cd[user.id]['user_characters']=user_characters
        return
    elif query.data.split("_")[-1]=='exit':
        insiders.remove(user.id)
        bro_user="*ACTIVE USERS :*\n\n"
        if len(insiders)>0:
            for m in range(len(insiders)):
                active_users=context.bot.getChat(insiders[m])
                bro_user+=f"*{m+1}* [{active_users.first_name}](tg://user?id={insiders[m]})\n"
        else:
            bro_user+="*NO ACTIVES*"
        context.bot.editMessageText(text=bro_user, chat_id=-1001931792224, message_id=3,parse_mode=ParseMode.MARKDOWN)
        query.message.edit_caption(caption=f"*Exited*",parse_mode=ParseMode.MARKDOWN)
        return

def battle_finsh(update,context):
    if maintenance_mode == "ON":
        if update.effective_user.id not in admins_id:
            try:
                update.callback_query.message.edit_text("*BOT UNDER MAINTENANCE*",parse_mode=ParseMode.MARKDOWN)
            except:
                update.callback_query.message.edit_caption(caption="*BOT UNDER MAINTENANCE*",parse_mode=ParseMode.MARKDOWN)
            return
    user=update.callback_query.from_user
    query=update.callback_query
    cd=context.chat_data
    monster=cd[user.id]['mob']
    defeated_monster=monster['name'].lower()
    user_data=[db.get_collection("user_datas"),db.get_collection("user_data"),db.get_collection("user_ids"),db.get_collection("beta_users")]
    user_obj_id = user_data[0].find_one()['user_data'][f'user_{user.id}']
    user_bag=user_data[1].find_one({'_id': ObjectId(user_obj_id)})['bag']
    user_weapons=user_data[1].find_one({'_id': ObjectId(user_obj_id)})['weapons']
    user_info=user_data[1].find_one({'_id': ObjectId(user_obj_id)})['user_info']
    global insiders    
    insiders.remove(user.id)
    bro_user="*ACTIVE USERS :*\n\n"
    if len(insiders)>0:
        for m in range(len(insiders)):
            active_users=context.bot.getChat(insiders[m])
            bro_user+=f"*{m+1}* [{active_users.first_name}](tg://user?id={insiders[m]}) \n"
    else:
        bro_user+="*NO ACTIVES*"
    context.bot.editMessageText(text=bro_user, chat_id=-1001931792224, message_id=3,parse_mode=ParseMode.MARKDOWN)
    query.message.delete()
    cd.clear()
    try:
        exp=user_info['exp']
    except:
        user_info['exp']=0
        exp=user_info['exp']
    if defeated_monster.upper() in ["CHARISMATIC FLAWLESS",'LIGHT MENDER',"ELECTRO WARRIO","GENESIS","OSIAL","DIAMONES","ICE DRAGON","IFRIT","ISSHIN"]:
        boss_level=monster['level']
        if boss_level==1:
            exp=500
            segil=50
            stargems=random.randint(5,10)
        elif boss_level==2:
            exp=800
            segil=80
            stargems=random.randint(6,12)
        elif boss_level==3:
            exp=1200
            segil=120
            stargems=random.randint(14,18)
        elif boss_level==4:
            exp=1500
            segil=180
            stargems=random.randint(16,20)
        elif boss_level==5:
            exp=2300
            segil=200
            stargems=random.randint(25,30)
        elif boss_level==6:
            exp=3000
            segil=450
            stargems=30
        user_bag['segil']+=segil
        user_bag['stargems']+=stargems
        user_info['exp']+=exp
        if defeated_monster.upper() == "IFRIT":
            reward=(random.randint(1,2))*boss_level
            drop_item="users_fire orb"
        elif defeated_monster.upper() == "ICE DRAGON":
            reward=(random.randint(1,2))*boss_level
            drop_item="users_ice orb"
        elif defeated_monster.upper() == "DIAMONES":
            reward=(random.randint(1,2))*boss_level
            drop_item="users_wind orb"
        elif defeated_monster.upper() == "OSIAL":
            reward=(random.randint(1,2))*boss_level
            drop_item="users_water orb"
        elif defeated_monster.upper() == "GENESIS":
            reward=(random.randint(1,2))*boss_level
            drop_item="users_earth orb"
        elif defeated_monster.upper() == "ELECTRO WARRIO":
            reward=(random.randint(1,2))*boss_level
            drop_item="users_electric orb"
        elif defeated_monster.upper() == "LIGHT MENDER":
            reward=(random.randint(1,2))*boss_level
            drop_item="users_light orb"
        elif defeated_monster.upper() == "CHARISMATIC FLAWLESS":
            reward=(random.randint(1,2))*boss_level
            drop_item="users_dark orb"
        elif defeated_monster.upper() == "ISSHIN":
            reward=(random.randint(1,2))*boss_level
            drop_item="users_physical orb"
        keyboard=[[InlineKeyboardButton("OBTAIN",callback_data='tow_claim')]]
        text=f"`MONSTER : `*{defeated_monster.upper()}*\n`POWER LEVEL : `*{boss_level}*\n\n*REWARDS YOU GOT : *\n*{reward}* `{drop_item.split('_')[1].upper()}`\n*{exp}* `EXPERIENCE POINTS`\n*{segil}* `SEGIL`\n*{stargems}* `STARGEMS`"
        message=context.bot.send_message(chat_id=update.effective_chat.id,text=f"YOU HAVE DEFEATED THE MONSTER *{defeated_monster.upper()}* AND U R GOING TO GET *SOME REWARDS* ON CLICKING THE OBTAIN BUTTON\n\nBUT YOU NEED TO USE *40 TOWER ENERGY* TO CLAIM THE REWARD",reply_markup=InlineKeyboardMarkup(keyboard),parse_mode=ParseMode.MARKDOWN)
        message_id=message.message_id
        cd[message_id]={}
        cd[message_id]['text']=text
        cd[message_id]['segil']=segil
        cd[message_id]['stargems']=stargems
        cd[message_id]['exp']=exp
        cd[message_id]['drop_item']=drop_item
        cd[message_id]['reward']=reward
        return
    else:
        if "slime" in defeated_monster.split(" "):
            drope=[True,False]
            if user_info['region'].split("_")[0] == 'DUNGEON':
                how_many=random.choice([1,2])
                drop=random.choices(drope,weights=(15,85),k=1)
                user_got_exp=random.randint(10,50)
                rewards=["segil","stargems"]
                reward=random.choices(rewards,weights=(80,20),k=1)
                if reward[0] == "segil":
                    amount=random.choice([5,6,7,8])
                elif reward[0] == "stargems":
                    amount=random.choice([1,2,3])
                else:
                    amount=1
            else:
                how_many=1
                drop=random.choices(drope,weights=(25,75),k=1)
                user_got_exp=random.randint(100,500)
                rewards=["segil","stargems"]
                reward=random.choices(rewards,weights=(83,17),k=1)
                if reward[0] == "segil":
                    amount=random.choice([5,6,7,8,9,10,12])
                elif reward[0] == "stargems":
                    amount=random.choice([1,2,3,4,5])
            if drop[0]==True:
                drop_item="users_gel"
                drop_text=f"\n\n`As You Defeated A `*{defeated_monster.upper()}* `You Got `*{how_many}*` `*{drop_item.split('_')[1].upper()}*"
            else:
                drop_text=""
        elif 'goblin' in defeated_monster.split(" "):
            drope=[True,False]
            if user_info['region'].split("_")[0] == 'DUNGEON':
                how_many=random.choice([1,2])
                drop=random.choices(drope,weights=(17,83),k=1)
                user_got_exp=random.randint(50,100)
                rewards=["segil","stargems"]
                reward=random.choices(rewards,weights=(75,25),k=1)
                if reward[0] == "segil":
                    amount=random.choice([6,7,8,9])
                elif reward[0] == "stargems":
                    amount=random.choice([3,4,5,6])
                else:
                    amount=1
            else:
                how_many=1
                drop=random.choices(drope,weights=(30,70),k=1)
                user_got_exp=random.randint(100,500)
                rewards=["segil","stargems"]
                reward=random.choices(rewards,weights=(83,17),k=1)
                if reward[0] == "segil":
                    amount=random.choice([10,11,12,13])
                elif reward[0] == "stargems":
                    amount=random.choice([1,4,6,8,10])
            if drop[0]==True:
                drop_item="users_goblin ears"
                drop_text=f"\n\n`As You Defeated A `*{defeated_monster.upper()}* `You Got `*{how_many}*` `*{drop_item.split('_')[1].upper()}*"
            else:
                drop_text=""
        elif 'kobold' in defeated_monster.split(" "):
            drope=[True,False]
            if user_info['region'].split("_")[0] == 'DUNGEON':
                how_many=random.choice([1,2])
                drop=random.choices(drope,weights=(25,75),k=1)
                user_got_exp=random.randint(100,120)
                rewards=["segil","stargems"]
                reward=random.choices(rewards,weights=(72,28),k=1)
                if reward[0] == "segil":
                    amount=random.choice([4,5,6,7,8])
                elif reward[0] == "stargems":
                    amount=random.choice([5,6,7,8,9,10,11,12])
                else:
                    print('gey')
            else:
                how_many=1
                drop=random.choices(drope,weights=(30,70),k=1)
                user_got_exp=random.randint(100,500)
                rewards=["segil","stargems"]
                reward=random.choices(rewards,weights=(83,17),k=1)
                if reward[0] == "segil":
                    amount=random.choice([10,11,12,13])
                elif reward[0] == "stargems":
                    amount=random.choice([1,4,6,8,10])
            if drop[0]==True:
                drop_item="users_kobold salt"
                drop_text=f"\n\n`As You Defeated A `*{defeated_monster.upper()}* `You Got `*{how_many}*` `*{drop_item.split('_')[1].upper()}*"
            else:
                drop_text=""
        elif 'lizard-man' in defeated_monster.split(" ") :
            drope=[True,False]
            if user_info['region'].split("_")[0] == 'DUNGEON':
                how_many=random.choice([1,2])
                drop=random.choices(drope,weights=(25,75),k=1)
                user_got_exp=random.randint(100,120)
                rewards=["segil","stargems"]
                reward=random.choices(rewards,weights=(58,42),k=1)
                if reward[0] == "segil":
                    amount=random.choice([6,7,8,9,10,11,12])
                elif reward[0] == "stargems":
                    amount=random.choice([5,6,7,8,9,10])
                else:
                    print('gey')
            else:
                how_many=1
                drop=random.choices(drope,weights=(30,70),k=1)
                user_got_exp=random.randint(100,500)
                rewards=["segil","stargems"]
                reward=random.choices(rewards,weights=(83,17),k=1)
                if reward[0] == "segil":
                    amount=random.choice([10,11,12,13])
                elif reward[0] == "stargems":
                    amount=random.choice([1,4,6,8,10])
            if drop[0]==True:
                drop_item="users_lizard tail"
                drop_text=f"\n\n`As You Defeated A `*{defeated_monster.upper()}* `You Got `*{how_many}*` `*{drop_item.split('_')[1].upper()}*"
            else:
                drop_text=""
        elif 'skeleton' in defeated_monster.split(" ") :
            drope=[True,False]
            if user_info['region'].split("_")[0] == 'DUNGEON':
                how_many=random.choice([1,2])
                drop=random.choices(drope,weights=(27,73),k=1)
                user_got_exp=random.randint(100,120)
                rewards=["segil","stargems"]
                reward=random.choices(rewards,weights=(70,30),k=1)
                if reward[0] == "segil":
                    amount=random.choice([6,7,8,9,10,11,12])
                elif reward[0] == "stargems":
                    amount=random.choice([5,6,7,8,9,10])
                else:
                    print('gey')
            else:
                how_many=1
                drop=random.choices(drope,weights=(30,70),k=1)
                user_got_exp=random.randint(100,500)
                rewards=["segil","stargems"]
                reward=random.choices(rewards,weights=(83,17),k=1)
                if reward[0] == "segil":
                    amount=random.choice([10,11,12,13])
                elif reward[0] == "stargems":
                    amount=random.choice([1,2,4,6,8,10])
            if drop[0]==True:
                drop_item="users_bones"
                drop_text=f"\n\n`As You Defeated A `*{defeated_monster.upper()}* `You Got `*{how_many}*` `*{drop_item.split('_')[1].upper()}*"
            else:
                drop_text=""
        elif 'illuminated' in defeated_monster.split(" ") :
            drope=[True,False]
            if user_info['region'].split("_")[0] == 'DUNGEON':
                how_many=random.choice([1,2])
                drop=random.choices(drope,weights=(25,75),k=1)
                user_got_exp=random.randint(100,120)
                rewards=["segil","stargems"]
                reward=random.choices(rewards,weights=(58,42),k=1)
                if reward[0] == "segil":
                    amount=random.choice([6,7,8,9,10,11,12])
                elif reward[0] == "stargems":
                    amount=random.choice([5,6,7,8,9,10,11,12])
                else:
                    print('gey')
            else:
                how_many=1
                drop=random.choices(drope,weights=(40,60),k=1)
                user_got_exp=random.randint(100,500)
                rewards=["segil","stargems"]
                reward=random.choices(rewards,weights=(60,40),k=1)
                if reward[0] == "segil":
                    amount=random.choice([6,7,8,10])
                elif reward[0] == "stargems":
                    amount=random.choice([1,4,6,8,12])
            if drop[0]==True:
                drop_item="users_sweet floweer"
                drop_text=f"\n\n`As You Defeated A `*{defeated_monster.upper()}* `You Got `*{how_many}*` `*{drop_item.split('_')[1].upper()}*"
            else:
                drop_text=""
        elif 'gardener' in defeated_monster.split(" ") :
            drope=[True,False]
            if user_info['region'].split("_")[0] == 'DUNGEON':
                how_many=random.choice([1,2])
                drop=random.choices(drope,weights=(25,75),k=1)
                user_got_exp=random.randint(100,120)
                rewards=["segil","stargems"]
                reward=random.choices(rewards,weights=(58,42),k=1)
                if reward[0] == "segil":
                    amount=random.choice([6,7,8,9,10,11,12])
                elif reward[0] == "stargems":
                    amount=random.choice([5,6,7,8,9,10,11,12])
                else:
                    print('gey')
            else:
                how_many=1
                drop=random.choices(drope,weights=(40,60),k=1)
                user_got_exp=random.randint(100,500)
                rewards=["segil","stargems"]
                reward=random.choices(rewards,weights=(60,40),k=1)
                if reward[0] == "segil":
                    amount=random.choice([6,7,8,9,10])
                elif reward[0] == "stargems":
                    amount=random.choice([1,4,6,8,12])
            if drop[0]==True:
                drop_item="users_sweet floweer"
                drop_text=f"\n\n`As You Defeated A `*{defeated_monster.upper()}* `You Got `*{how_many}*` `*{drop_item.split('_')[1].upper()}*"
            else:
                drop_text=""
        elif 'chained' in defeated_monster.split(" ") :
            drope=[True,False]
            if user_info['region'].split("_")[0] == 'DUNGEON':
                how_many=random.choice([1,2])
                drop=random.choices(drope,weights=(25,75),k=1)
                user_got_exp=random.randint(100,120)
                rewards=["segil","stargems"]
                reward=random.choices(rewards,weights=(58,42),k=1)
                if reward[0] == "segil":
                    amount=random.choice([6,7,8,9,10,11,12])
                elif reward[0] == "stargems":
                    amount=random.choice([5,6,7,8,9,10,11,12])
                else:
                    print('gey')
            else:
                how_many=1
                drop=random.choices(drope,weights=(40,60),k=1)
                user_got_exp=random.randint(100,500)
                rewards=["segil","stargems"]
                reward=random.choices(rewards,weights=(60,40),k=1)
                if reward[0] == "segil":
                    amount=random.choice([6,7,8,10])
                elif reward[0] == "stargems":
                    amount=random.choice([1,4,6,8,12])
            if drop[0]==True:
                drop_item="users_blood of dead"
                drop_text=f"\n\n`As You Defeated A `*{defeated_monster.upper()}* `You Got `*{how_many}*` `*{drop_item.split('_')[1].upper()}*"
            else:
                drop_text=""
        elif 'centipede-infested' in defeated_monster.split(" ") :
            drope=[True,False]
            if user_info['region'].split("_")[0] == 'DUNGEON':
                how_many=random.choice([1,2])
                drop=random.choices(drope,weights=(25,75),k=1)
                user_got_exp=random.randint(100,120)
                rewards=["segil","stargems"]
                reward=random.choices(rewards,weights=(58,42),k=1)
                if reward[0] == "segil":
                    amount=random.choice([6,7,8,9,10,11,12])
                elif reward[0] == "stargems":
                    amount=random.choice([5,6,7,8,9,10,11,12])
                else:
                    print('gey')
            else:
                how_many=1
                drop=random.choices(drope,weights=(40,60),k=1)
                user_got_exp=random.randint(100,500)
                rewards=["segil","stargems"]
                reward=random.choices(rewards,weights=(60,40),k=1)
                if reward[0] == "segil":
                    amount=random.choice([6,7,8,10])
                elif reward[0] == "stargems":
                    amount=random.choice([1,4,6,8,12])
            if drop[0]==True:
                drop_item="users_blood of dead"
                drop_text=f"\n\n`As You Defeated A `*{defeated_monster.upper()}* `You Got `*{how_many}*` `*{drop_item.split('_')[1].upper()}*"
            else:
                drop_text=""
        else:
            print("error report to owner")
        if drop[0]==True:
            try:
                user_bag[drop_item]+=how_many
            except:
                user_bag[drop_item]=how_many
        else:
            drop_text="\n\n`IT SEEMS LIKE U DIDN'T GOT ANY DROP ITEM`"
        required_exp=(10000)+(10000*user_info['rank']*2-user_info['rank']*2500)
        if user_info['rank']>59:
            print("no rewards for you")
        else:
            if exp>required_exp-1:
                user_characters=user_data[1].find_one({'_id': ObjectId(user_obj_id)})['user_char']
                if user_characters[0]['constellation']<6:
                    user_characters[0]['constellation']+=1
                    context.bot.send_message(chat_id=update.effective_chat.id,text=f"*YOUR STARTER CHARACTER CONSTELLATION INCREASED DUE TO RANK UP*",parse_mode=ParseMode.MARKDOWN)
                    user_data[1].update_one({"_id":ObjectId(user_obj_id)},{"$set":{'user_char':user_characters}})
                elif user_characters[0]['constellation']>5:
                    print('gye')
                exp=exp-required_exp
                user_info['rank']+=1
                if user_info['rank'] > 0 and user_info['rank'] < 11:
                    reward1_type="segil"
                    reward2_type="stargems"
                    reward3_type="WEAPON"
                    reward1=50+user_info['rank']*2
                    reward2=10+user_info['rank']
                    if user_info['rank'] > 0 and user_info['rank'] < 6:
                        weapons=random.choice([{"weapon_name":"Rookie Rankers Sword","weapon_type":"sword","level":1,"buff_atk":2,"special_buff":None},
                                            {"weapon_name":"Rookie Rankers Spear","weapon_type":"spear","level":1,"buff_atk":2,"special_buff":None},
                                            {"weapon_name":"Rookie Rankers staff","weapon_type":"magic_staff","level":1,"buff_atk":2,"special_buff":None},
                                            {"weapon_name":"Rookie Rankers gauntlets","weapon_type":"gauntlets","level":1,"buff_atk":2,"special_buff":None},
                                            {"weapon_name":"Rookie Rankers Bow","weapon_type":"bow","level":1,"buff_atk":2,"special_buff":None}])
                    else:
                        weapons=random.choice([{"weapon_name":"Rankers Sword","weapon_type":"sword","level":1,"buff_atk":3,"special_buff":None},
                                            {"weapon_name":"Rankers Spear","weapon_type":"spear","level":1,"buff_atk":3,"special_buff":None},
                                            {"weapon_name":"Rankers staff","weapon_type":"magic_staff","level":1,"buff_atk":3,"special_buff":None},
                                            {"weapon_name":"Rankers gauntlets","weapon_type":"gauntlets","level":1,"buff_atk":3,"special_buff":None},
                                            {"weapon_name":"Rankers Bow","weapon_type":"bow","level":1,"buff_atk":3,"special_buff":None}])
                    user_bag[reward1_type]+=reward1
                    user_bag[reward2_type]+=reward2
                    user_weapons.append(weapons)
                    if user_info['rank']==3:
                        reffer_by=user_data[1].find_one({'_id': ObjectId(user_obj_id)})['extras']['refferal']
                        if reffer_by['reffered_by']==None:
                            print("NOT REFFERED")
                        else:
                            reffer_data=user_data[1].find_one({'_id': ObjectId(reffer_by['reffered_by'])})
                            things=['primostar','segil','stargems','weapons']
                            random_reward_of_reffer=random.choices(things,weights=(20,20,50,10),k=1)
                            if random_reward_of_reffer[0] in ['primostar','segil','stargems']:
                                reffer_bag=reffer_data['bag']
                                if random_reward_of_reffer[0]=='primostar':
                                    ref_amount=random.randint(1,5)
                                    reffer_bag[f'primostar']+=ref_amount
                                if random_reward_of_reffer[0]=='segil':
                                    ref_amount=random.randint(1000,3000)
                                    reffer_bag[f'segil']+=ref_amount
                                if random_reward_of_reffer[0]=='stargems':
                                    ref_amount=random.randint(50,600)
                                    reffer_bag[f'stargems']+=ref_amount
                                user_data[1].update_one({"_id":ObjectId(reffer_by['reffered_by'])},{"$set":{'bag':reffer_bag}})
                                context.bot.send_message(chat_id=reffer_data['user_id'],text=f"{user.first_name} RANKED UP TO RANK 3 SO YOU GOT {ref_amount} {random_reward_of_reffer[0]}",parse_mode=ParseMode.MARKDOWN)
                            else:
                                reffer_weapon=reffer_data['weapons']
                                refffera_weapons=[{"weapon_name":"Gifters Sword","weapon_type":"sword","level":1,"buff_atk":5,"special_buff":None},
                                                  {"weapon_name":"Gifters Spear","weapon_type":"spear","level":1,"buff_atk":5,"special_buff":None},
                                                  {"weapon_name":"Gifters staff","weapon_type":"magic_staff","level":1,"buff_atk":5,"special_buff":None},
                                                  {"weapon_name":"Gifters gauntlets","weapon_type":"gauntlets","level":1,"buff_atk":5,"special_buff":None},
                                                  {"weapon_name":"Gifters Bow","weapon_type":"bow","level":1,"buff_atk":5,"special_buff":None},
                                                  {"weapon_name":"Saint Gift Sword","weapon_type":"sword","level":1,"buff_atk":3,"special_buff":"path of sage"},
                                                  {"weapon_name":"Saint Gift Spear","weapon_type":"spear","level":1,"buff_atk":3,"special_buff":"path of sage"},
                                                  {"weapon_name":"Saint Gift staff","weapon_type":"magic_staff","level":1,"buff_atk":3,"special_buff":"path of sage"},
                                                  {"weapon_name":"Saint Gift gauntlets","weapon_type":"gauntlets","level":1,"buff_atk":3,"special_buff":"path of sage"},
                                                  {"weapon_name":"Saint Gift Bow","weapon_type":"bow","level":1,"buff_atk":3,"special_buff":"path of sage"}]
                                random_reffer_weapons=random.choices(refffera_weapons,weights=(15,15,15,15,15,5,5,5,5,5),k=1)
                                reffer_weapon.append(random_reffer_weapons[0])
                                user_data[1].update_one({"_id":ObjectId(reffer_by['reffered_by'])},{"$set":{'weapons':reffer_weapon}})
                                context.bot.send_message(chat_id=reffer_data['user_id'],text=f"{user.first_name} RANKED UP TO RANK 3 SO YOU GOT 1 {random_reffer_weapons['weapon_name']}",parse_mode=ParseMode.MARKDOWN)
                    if user_info['rank']==5:
                        user_char=user_data[1].find_one({'_id': ObjectId(user_obj_id)})['user_char']
                        free_char=char.kayla_char
                        char_in_list=False
                        for i in range(len(user_char)):
                            if user_char[i]['name']=='KAYLA':
                                if user_char[i]['constellation']<6:
                                    user_char[i]['constellation']+=1
                                char_in_list=True
                        if char_in_list!=True:
                            user_char.append(free_char)
                        context.bot.send_photo(chat_id=update.effective_chat.id,photo=free_char['photo'],caption=f"*YOU GOT A FREE CHARACTER AS A RANK UP REWARD*\n\n` Character Name : `*{free_char['name']}*",parse_mode=ParseMode.MARKDOWN)
                        user_data[1].update_one({"_id":ObjectId(user_obj_id)},{"$set":{'user_char':user_char}})
                if user_info['rank'] > 10 and user_info['rank'] < 21:
                    reward1_type="segil"
                    reward2_type="stargems"
                    reward3_type="WEAPON"
                    reward1=100+user_info['rank']*5
                    reward2=20+user_info['rank']*2
                    weapons=random.choice([{"weapon_name":"Rankers Sword","weapon_type":"sword","level":1,"buff_atk":3,"special_buff":None},
                                        {"weapon_name":"Rankers Spear","weapon_type":"spear","level":1,"buff_atk":3,"special_buff":None},
                                        {"weapon_name":"Rankers staff","weapon_type":"magic_staff","level":1,"buff_atk":3,"special_buff":None},
                                        {"weapon_name":"Rankers gauntlets","weapon_type":"gauntlets","level":1,"buff_atk":3,"special_buff":None},
                                        {"weapon_name":"Rankers Bow","weapon_type":"bow","level":1,"buff_atk":3,"special_buff":None},
                                        {"weapon_name":"Rankerds Sword","weapon_type":"sword","level":1,"buff_atk":3,"special_buff":None},
                                        {"weapon_name":"Rankerds Spear","weapon_type":"spear","level":1,"buff_atk":3,"special_buff":None},
                                        {"weapon_name":"Rankerds staff","weapon_type":"magic_staff","level":1,"buff_atk":3,"special_buff":None},
                                        {"weapon_name":"Rankerds gauntlets","weapon_type":"gauntlets","level":1,"buff_atk":3,"special_buff":None},
                                        {"weapon_name":"Rankerds Bow","weapon_type":"bow","level":1,"buff_atk":3,"special_buff":None}])
                    user_bag[reward1_type]+=reward1
                    user_bag[reward2_type]+=reward2
                    user_weapons.append(weapons)
                if user_info['rank'] > 20  and user_info['rank'] < 31:
                    reward1_type="segil"
                    reward2_type="stargems"
                    reward3_type="WEAPON"
                    reward1=200+user_info['rank']*5
                    reward2=40+user_info['rank']*2
                    weapons=random.choice([{"weapon_name":"Rankerds Sword","weapon_type":"sword","level":1,"buff_atk":3,"special_buff":None},
                                        {"weapon_name":"Rankerds Spear","weapon_type":"spear","level":1,"buff_atk":3,"special_buff":None},
                                        {"weapon_name":"Rankerds staff","weapon_type":"magic_staff","level":1,"buff_atk":3,"special_buff":None},
                                        {"weapon_name":"Rankerds gauntlets","weapon_type":"gauntlets","level":1,"buff_atk":3,"special_buff":None},
                                        {"weapon_name":"Rankerds Bow","weapon_type":"bow","level":1,"buff_atk":3,"special_buff":None}])
                    user_bag[reward1_type]+=reward1
                    user_bag[reward2_type]+=reward2
                    user_weapons.append(weapons)
                if user_info['rank'] > 30 and user_info['rank'] < 41:
                    reward1_type="segil"
                    reward2_type="stargems"
                    reward3_type="WEAPON"
                    reward1=250+user_info['rank']*5
                    reward2=50+user_info['rank']*2
                    weapons=random.choice([{"weapon_name":"Rankerds Sword","weapon_type":"sword","level":1,"buff_atk":3,"special_buff":None},
                                        {"weapon_name":"Rankerds Spear","weapon_type":"spear","level":1,"buff_atk":3,"special_buff":None},
                                        {"weapon_name":"Rankerds staff","weapon_type":"magic_staff","level":1,"buff_atk":3,"special_buff":None},
                                        {"weapon_name":"Rankerds gauntlets","weapon_type":"gauntlets","level":1,"buff_atk":3,"special_buff":None},
                                        {"weapon_name":"Rankerds Bow","weapon_type":"bow","level":1,"buff_atk":3,"special_buff":None},
                                        {"weapon_name":"Sword of Gold","weapon_type":"sword","level":1,"buff_atk":4,"special_buff":None},
                                        {"weapon_name":"Spear of Gold","weapon_type":"spear","level":1,"buff_atk":4,"special_buff":None},
                                        {"weapon_name":"staff of Gold","weapon_type":"magic_staff","level":1,"buff_atk":4,"special_buff":None},
                                        {"weapon_name":"gauntlets of Gold","weapon_type":"gauntlets","level":1,"buff_atk":4,"special_buff":None},
                                        {"weapon_name":"Bow of Gold","weapon_type":"bow","level":1,"buff_atk":4,"special_buff":None}])
                    user_bag[reward1_type]+=reward1
                    user_bag[reward2_type]+=reward2
                    user_weapons.append(weapons)
                if user_info['rank'] > 40 and user_info['rank'] < 51:
                    reward1_type="segil"
                    reward2_type="stargems"
                    reward3_type="WEAPON"
                    reward1=300+user_info['rank']*10
                    reward2=80+user_info['rank']*2
                    weapons=random.choice([{"weapon_name":"Sword of Gold","weapon_type":"sword","level":1,"buff_atk":4,"special_buff":None},
                                        {"weapon_name":"Spear of Gold","weapon_type":"spear","level":1,"buff_atk":4,"special_buff":None},
                                        {"weapon_name":"staff of Gold","weapon_type":"magic_staff","level":1,"buff_atk":4,"special_buff":None},
                                        {"weapon_name":"gauntlets of Gold","weapon_type":"gauntlets","level":1,"buff_atk":4,"special_buff":None},
                                        {"weapon_name":"Bow of Gold","weapon_type":"bow","level":1,"buff_atk":4,"special_buff":None}])
                    user_bag[reward1_type]+=reward1
                    user_bag[reward2_type]+=reward2
                    user_weapons.append(weapons)
                if user_info['rank'] > 50 and user_info['rank'] < 56:
                    reward1_type="segil"
                    reward2_type="stargems"
                    reward3_type="WEAPON"
                    reward1=500+user_info['rank']*5
                    reward2=100+user_info['rank']*2
                    weapons=random.choice([{"weapon_name":"Platinum Sword","weapon_type":"sword","level":1,"buff_atk":6,"special_buff":"path of ranker"},
                                        {"weapon_name":"Platinum Spear","weapon_type":"spear","level":1,"buff_atk":6,"special_buff":"path of ranker"},
                                        {"weapon_name":"staff of Platinum","weapon_type":"magic_staff","level":1,"buff_atk":5,"special_buff":"path of ranker"},
                                        {"weapon_name":"Platinum gauntlets","weapon_type":"gauntlets","level":1,"buff_atk":6,"special_buff":"path of ranker"},
                                        {"weapon_name":"Bow of Platinum","weapon_type":"bow","level":1,"buff_atk":5,"special_buff":"path of ranker"}])
                    user_bag[reward1_type]+=reward1
                    user_bag[reward2_type]+=reward2
                    user_weapons.append(weapons)
                if user_info['rank'] > 55 and user_info['rank'] < 61:
                    reward1_type="primostar"
                    reward2_type="stargems"
                    reward3_type="WEAPON"
                    reward1=5
                    reward2=120+user_info['rank']*2
                    weapons=random.choice([{"weapon_name":"Platinum Sword","weapon_type":"sword","level":1,"buff_atk":6,"special_buff":"path of ranker"},
                                        {"weapon_name":"Platinum Spear","weapon_type":"spear","level":1,"buff_atk":6,"special_buff":"path of ranker"},
                                        {"weapon_name":"staff of Platinum","weapon_type":"magic_staff","level":1,"buff_atk":5,"special_buff":"path of ranker"},
                                        {"weapon_name":"Platinum gauntlets","weapon_type":"gauntlets","level":1,"buff_atk":6,"special_buff":"path of ranker"},
                                        {"weapon_name":"Bow of Platinum","weapon_type":"bow","level":1,"buff_atk":5,"special_buff":"path of ranker"}])
                    user_bag[reward1_type]+=reward1
                    user_bag[reward2_type]+=reward2
                    user_weapons.append(weapons)
                    if user_info['rank']==60:
                        free_weapon=random.choice(char.free_5_weapon)
                        context.bot.send_message(chat_id=update.effective_chat.id,text=f"*YOU GOT A FREE 5 STAR WEAPON AS A RANK UP REWARD*\n\n` WEAPON Name : `*{free_weapon['weapon_name']}*",parse_mode=ParseMode.MARKDOWN)
                        user_weapons.append(free_weapon)
                context.bot.send_message(chat_id=update.effective_chat.id,text=f"*CONGRATULATION*\n\n\t\t\t`RANK INCREASED FROM {user_info['rank']-1} TO {user_info['rank']}`\n\n*AND YOU GOT {reward1} {reward1_type} , {reward2} {reward2_type} and {weapons['weapon_name']}*",parse_mode=ParseMode.MARKDOWN )
        user_bag[f'{reward[0]}']+=amount
        user_info['kills']+=1
        if user.id in [1325708894,1864257459,1927291805]:
            user_got_exp=10000
        exp+=user_got_exp
        user_info['exp']=exp
        user_data[1].update_one({"_id":ObjectId(user_obj_id)},{"$set":{'weapons':user_weapons}})
        user_data[1].update_one({"_id":ObjectId(user_obj_id)},{"$set":{'user_info':user_info}})
        user_data[1].update_one({"_id":ObjectId(user_obj_id)},{"$set":{'bag':user_bag}})
        context.bot.send_message(chat_id=update.effective_chat.id,text=f"`You have defeated a `*{defeated_monster}*\n`REWARD : `*{amount} {reward[0].upper()}\nAND GOT {user_got_exp} EXP*"+drop_text,parse_mode=ParseMode.MARKDOWN)
        return

def charamoves(x):
    character=x
    moves={}
    if character['name']=='RYZA ( BETA CHAR )':
        moves['normal_move']={'name':'Light Ray'}
        moves['skill_move']={'name':'Light Enchance','usage':2}
        moves['ult_move']={'name':'LIGHT FALL','cost':250}
        moves['dodge_move']={'name':'DODGE','chances':character['speed']/10}
    if character['name']=='SHADOW ( BETA CHAR )':
        moves['normal_move']={'name':'Sword Hit'}
        moves['skill_move']={'name':'Slime Sword','usage':1}
        moves['ult_move']={'name':' ATOMIC ! ','cost':300}
        moves['dodge_move']={'name':'DODGE','chances':character['speed']/10}
    if character['name']=='MORAX ( BETA CHAR )':
        moves['normal_move']={'name':'Spear Slide'}
        moves['skill_move']={'name':'Stone summon','usage':2}
        moves['ult_move']={'name':'Spear Throw','cost':200,'video':None}
        moves['dodge_move']={'name':'DODGE','chances':character['speed']/10}
    if character['name']=='KRATOS':
        moves['normal_move']={'name':'Gauntlet punch'}
        moves['skill_move']={'name':'Gauntlet Rush','usage':1}
        moves['ult_move']={'name':'Leviathan Arm','cost':300,'video':None}
        moves['dodge_move']={'name':'DODGE','chances':character['speed']/10}
    if character['name']=='CLAUDIA':
        moves['normal_move']={'name':'Sword Cut'}
        moves['skill_move']={'name':'Deviation','usage':3}
        moves['ult_move']={'name':'Dimensional Cut','cost':200,'video':None}
        moves['dodge_move']={'name':'DODGE','chances':character['speed']/10}
    if character['name']=='FISCHL':
        moves['normal_move']={'name':'Arrow Throw'}
        moves['skill_move']={'name':'Summon Oz','usage':2}
        moves['ult_move']={'name':'The one with Oz','cost':150,'photo':None}
        moves['dodge_move']={'name':'DODGE','chances':character['speed']/10}
    if character['name']=='ECHO':
        moves['normal_move']={'name':'Spear slide'}
        moves['skill_move']={'name':'Electro Rush','usage': 2}
        moves['ult_move']={'name':'Electric Ray','cost':250,'photo':None}
        moves['dodge_move']={'name':'DODGE','chances':character['speed']/10}
    if character['name']=='QIQI':
        moves['normal_move']={'name':'Sword Sting'}
        moves['skill_move']={'name':'Ice Heal','usage': 1}
        moves['ult_move']={'name':'Ice Field','cost':200,'photo':None}
        moves['dodge_move']={'name':'DODGE','chances':character['speed']/10}
    if character['name']=='JEAN':
        moves['normal_move']={'name':'Sword Sting'}
        moves['skill_move']={'name':'Air Blow','usage': 2}
        moves['ult_move']={'name':'Dandelion Field','cost':200,'video':None}
        moves['dodge_move']={'name':'DODGE','chances':character['speed']/10}
    if character['name']=='TIAN LANG':
        moves['normal_move']={'name':'Magic !'}
        moves['skill_move']={'name':'Electric field','usage': 2}
        moves['ult_move']={'name':'ELectro Staffing','cost':300,'video':None}
        moves['dodge_move']={'name':'DODGE','chances':character['speed']/10}
    if character['name']=='DIAN FARRELL':
        moves['normal_move']={'name':'Scratch'}
        moves['skill_move']={'name':'Rage !','usage': 2}
        moves['ult_move']={'name':'Rage Attacks','cost':250,'video':None}
        moves['dodge_move']={'name':'DODGE','chances':character['speed']/10}
    if character['name']=='KAYLA':
        moves['normal_move']={'name':'MAGIC'}
        moves['skill_move']={'name':'FLAME ENHANCE','usage': 1}
        moves['ult_move']={'name':'FLAME BURST','cost':250,'photo':None}
        moves['dodge_move']={'name':'DODGE','chances':character['speed']/10}
    if character['name']=='KLAUDIA VALENTZ':
        moves['normal_move']={'name':'HIT'}
        moves['skill_move']={'name':'ICE HEAL !','usage':2}
        moves['ult_move']={'name':'FLOWER GARDEN','cost':250,'video':None}
        moves['dodge_move']={'name':'DODGE','chances':character['speed']/10}
    if character['name']=='LISA':
        moves['normal_move']={'name':'electric'}
        moves['skill_move']={'name':'ELECTRO AREA','usage': 2}
        moves['ult_move']={'name':'ELECTRO BURST','cost':300,'photo':None}
        moves['dodge_move']={'name':'DODGE','chances':character['speed']/10}
    if character['name']=='DOOMFIST':
        moves['normal_move']={'name':'Fist Attack'}
        moves['skill_move']={'name':'DOOM SHOT !','usage': 1}
        moves['ult_move']={'name':'DOOM !!!','cost':250,'photo':None}
        moves['dodge_move']={'name':'DODGE','chances':character['speed']/10}
    if character['name']=='FIONA':
        moves['normal_move']={'name':'Slice'}
        moves['skill_move']={'name':'Sword Enhance !','usage': 2}
        moves['ult_move']={'name':'Water field','cost':300,'photo':None}
        moves['dodge_move']={'name':'DODGE','chances':character['speed']/10}
    if character['name']=='RAIDEN SHOGUN':
        moves['normal_move']={'name':'STICK !'}
        moves['skill_move']={'name':'Lightning !','usage': 2}
        moves['ult_move']={'name':'ISLAND BREAKER : LIGHTNING','cost':300,'photo':None}
        moves['dodge_move']={'name':'DODGE','chances':character['speed']/10}
    if character['name']=='SEKIRO':
        moves['normal_move']={'name':'Slash'}
        moves['skill_move']={'name':'ELEMENTAL ENHANCE !','usage': 2}
        moves['ult_move']={'name':'BLOOD MASSACRE','cost':250,'photo':None}
        moves['dodge_move']={'name':'DODGE','chances':character['speed']/10}
    if character['name']=='BENNETT':
        moves['normal_move']={'name':'peck'}
        moves['skill_move']={'name':'Flame sword','usage': 3}
        moves['ult_move']={'name':'FLAME GROUND','cost':300,'photo':None}
        moves['dodge_move']={'name':'DODGE','chances':character['speed']/10}
    if character['name']=='YUKONG':
        moves['normal_move']={'name':'Stance !'}
        moves['skill_move']={'name':'ATTACK Enhance !','usage': 2}
        moves['ult_move']={'name':'Water field','cost':250,'photo':None}
        moves['dodge_move']={'name':'DODGE','chances':character['speed']/10}
    if character['name']=='CANDACE':
        moves['normal_move']={'name':'Knock'}
        moves['skill_move']={'name':'Shield !','usage': 1}
        moves['ult_move']={'name':'Shield burst','cost':250,'photo':None}
        moves['dodge_move']={'name':'DODGE','chances':character['speed']/10}
    return moves

def bot_status(update,context):
    if maintenance_mode == "ON":
        if update.effective_user.id not in admins_id:
            update.message.reply_text("*BOT UNDER MAINTENANCE*",parse_mode=ParseMode.MARKDOWN)
            return
    user=update.effective_user
    if user.id == 1864257459:
        global insiders
        msg = update.message.reply_text("*GETTING INFO..*",parse_mode=ParseMode.MARKDOWN)
        context.bot.editMessageText(chat_id=update.effective_chat.id, message_id=msg.message_id, text=f"*GETTING INFO....*",parse_mode=ParseMode.MARKDOWN)
        context.bot.editMessageText(chat_id=update.effective_chat.id, message_id=msg.message_id, text=f"*GETTING INFO......*",parse_mode=ParseMode.MARKDOWN)
        context.bot.editMessageText(chat_id=update.effective_chat.id, message_id=msg.message_id, text=f"*GETTING INFO........*",parse_mode=ParseMode.MARKDOWN)
        user_data=[db.get_collection("user_datas"),db.get_collection("user_data"),db.get_collection("user_ids"),db.get_collection("beta_users")]
        context.bot.editMessageText(chat_id=update.effective_chat.id, message_id=msg.message_id, text=f"`TOTAL USERS : `*{len(user_data[2].find_one()['user_ids'])}\n*\n`TOTAL BANNED USER : `*{len(user_data[3].find_one()['beta_players'])}*\n\n`TOTAL ACTIVE USERS : `*{len(insiders)}*",parse_mode=ParseMode.MARKDOWN)
        return
    else:
        update.message.reply_text("*U R GAY*",parse_mode=ParseMode.MARKDOWN)

def beta_adder(update,context):
    if maintenance_mode == "ON":
        if update.effective_user.id not in admins_id:
            update.message.reply_text("*BOT UNDER MAINTENANCE*",parse_mode=ParseMode.MARKDOWN)
            return
    user=update.message.from_user
    if user.id == 1864257459:
        ddatabse=db.get_collection("beta_users")
        replied_user=update.message.reply_to_message.from_user
        ddt=ddatabse.find_one()['beta_players']
        if replied_user.id in ddt:
            context.bot.send_message(chat_id=update.effective_chat.id,text=f"USER : {replied_user.first_name} already added in beta")
            return
        ddt.append(replied_user.id)
        ddatabse.update_one({"_id":ObjectId(ddatabse.find_one()['_id'])},{'$set':{'beta_players':ddt}})
        context.bot.send_message(chat_id=update.effective_chat.id,text=f"USER : {replied_user.first_name} added in beta")
        return
    context.bot.send_message(chat_id=update.effective_chat.id,text="You're Not worthy of giving beta permission")

def send_gift(context):
    user_data=[db.get_collection("user_datas"),db.get_collection("user_data"),db.get_collection("user_ids"),db.get_collection("beta_users")]
    total_users=user_data[2].find_one()['user_ids']
    for i in range(len(total_users)):
        user_obj_id = user_data[0].find_one()['user_data'][f'user_{total_users[i]}']
        bag = user_data[1].find_one({'_id':ObjectId(user_obj_id)})['bag']
        bag['tow_en']=200
        user_data[1].update_one({"_id":ObjectId(user_obj_id)},{"$set":{'bag':bag}})
    daily_login=db.get_collection("daily_login")
    login_data=daily_login.find_one()['claimed_users']
    login_data=[]
    daily_login.update_one({"_id":ObjectId(daily_login.find_one()['_id'])},{'$set':{'claimed_users':login_data}})
    context.bot.send_message(chat_id=-1001170323135,text=f"WORKING\nTOTAL USER : {len(total_users)}",parse_mode=ParseMode.MARKDOWN)
    return

def gift_getter(update,context):
    if maintenance_mode == "ON":
        if update.effective_user.id not in admins_id:
            try:
                update.callback_query.message.edit_text("*BOT UNDER MAINTENANCE*",parse_mode=ParseMode.MARKDOWN)
            except:
                update.callback_query.message.edit_caption(caption="*BOT UNDER MAINTENANCE*",parse_mode=ParseMode.MARKDOWN)
            return
    user=update.effective_user
    query=update.callback_query
    query.message.edit_text("PROCESSING....")
    daily_login=db.get_collection("daily_login")
    login_data=daily_login.find_one()['claimed_users']
    keyboard=[[InlineKeyboardButton('BACK',callback_data=f'back_to_event')]]
    user_data=[db.get_collection("user_datas"),db.get_collection("user_data"),db.get_collection("user_ids"),db.get_collection("beta_users")]
    user_obj_id = user_data[0].find_one()['user_data'][f'user_{user.id}']
    user_info=user_data[1].find_one({'_id':ObjectId(user_obj_id)})['user_info']
    if user_info['rank']>0:
        print("I GOT YOU")
    else:
        query.message.edit_text(f"*YOU'RE NOT ELIGIBE TO CLAIM DAILY REWARD\nYOU NEED A MINIMUM RANK 1 TO GET ACCESS OF DAILY LOGIN*",reply_markup=InlineKeyboardMarkup(keyboard),parse_mode=ParseMode.MARKDOWN)
        return
    if user.id not in login_data:
        login_data.append(user.id)
        user_bag=user_data[1].find_one({'_id':ObjectId(user_obj_id)})['bag']
        user_bag['primostar']+=1
        query.message.edit_text(f"*CONGRATULATION 😃🎊!\nYOU HAVE SUCCESFULLY OBTAINED 1 PRIMOSTAR*\n\n`TOTAL PRIMOSTAR : `*{user_bag['primostar']}*",reply_markup=InlineKeyboardMarkup(keyboard),parse_mode=ParseMode.MARKDOWN)
        user_data[1].update_one({"_id":ObjectId(user_obj_id)},{"$set":{'bag':user_bag}})
        daily_login.update_one({"_id":ObjectId(daily_login.find_one()['_id'])},{'$set':{'claimed_users':login_data}})
        return
    else:
        query.message.edit_text(f"*You can't claim twice or more than that per day*",reply_markup=InlineKeyboardMarkup(keyboard),parse_mode=ParseMode.MARKDOWN)
        return

def tower_enter(update,context):
    if maintenance_mode == "ON":
        if update.effective_user.id not in admins_id:
            update.message.reply_text("*BOT UNDER MAINTENANCE*",parse_mode=ParseMode.MARKDOWN)
            return
    user = update.message.from_user
    cd = context.chat_data
    global insiders
    if user.id in insiders:
        update.message.reply_text("*You're already in a Battle *",parse_mode=ParseMode.MARKDOWN)
        return
    user_data=[db.get_collection("user_datas"),db.get_collection("user_data"),db.get_collection("user_ids"),db.get_collection("beta_users")]
    if user.id in user_data[3].find_one()['beta_players']:
        update.message.reply_text("*SEDLY U R NOT WORTHY TO USE THIS COMMAND*",parse_mode=ParseMode.MARKDOWN)
        return
    else:
        if user.id not in user_data[2].find_one()['user_ids']:
            keyboard=[[InlineKeyboardButton('PM',url='https://t.me/PSO_SoBot?start')]]
            update.message.reply_video(video='https://graph.org/file/e663ce2ffd9c8c32d3247.mp4',caption="*It seems like u haven't started\nClick on the button given below and start the bot*",reply_markup=InlineKeyboardMarkup(keyboard),parse_mode=ParseMode.MARKDOWN)
            return
        user_obj_id = user_data[0].find_one()['user_data'][f'user_{user.id}']
        if update.effective_chat.id != user.id:
            keyboard=[[InlineKeyboardButton('USE IN PM',url='https://t.me/PSO_SoBot?start=tower')]]
            update.message.reply_text("*THIS COMMAND CAN'T BE USED IN GROUP CHAT*",reply_markup=InlineKeyboardMarkup(keyboard),parse_mode=ParseMode.MARKDOWN)
        else:
            user_info=user_data[1].find_one({'_id':ObjectId(user_obj_id)})['user_info']
            if user_info['rank']<1:
                update.message.reply_text("*NOT ENOUGH RANK TO FIGHT THE BOSS\nMINIMUM RANK 1 IS REQUIRED*",parse_mode=ParseMode.MARKDOWN)
                return
            else:
                button=[[InlineKeyboardButton('IFRIT 🔥',callback_data =f"tow_En_fire"),InlineKeyboardButton('ICE DRAGON ❄️',callback_data =f"tow_En_ice")],
                        [InlineKeyboardButton('DIAMONES 🌪',callback_data =f"tow_En_wind"),InlineKeyboardButton('OSIAL 🌊',callback_data =f"tow_En_water")],
                        [InlineKeyboardButton('GENESIS 🪨',callback_data =f"tow_En_earth"),InlineKeyboardButton('ELECTRO WARRIO ⚡️',callback_data =f"tow_En_electric")],
                        [InlineKeyboardButton('LIGHT MENDER ✴️',callback_data =f"tow_En_light"),InlineKeyboardButton('CHARISMATIC FLAWLESS ⚫️',callback_data =f"tow_En_dark")],
                        [InlineKeyboardButton('ISSHIN 🦾',callback_data =f"tow_En_physical")],
                        [InlineKeyboardButton('EXIT',callback_data =f"tow_En_exit")]]
                update.message.reply_text("*SELECT THE BOSS WHICH U WANT TO FIGHT*",reply_markup=InlineKeyboardMarkup(button),parse_mode=ParseMode.MARKDOWN)
                return

def tower_level(update,context):
    if maintenance_mode == "ON":
        if update.effective_user.id not in admins_id:
            try:
                update.callback_query.message.edit_text("*BOT UNDER MAINTENANCE*",parse_mode=ParseMode.MARKDOWN)
            except:
                update.callback_query.message.edit_caption(caption="*BOT UNDER MAINTENANCE*",parse_mode=ParseMode.MARKDOWN)
            return
    user=update.effective_user
    query=update.callback_query
    if user.id in insiders:
        query.message.edit_text("*You're already in a Battle *",parse_mode=ParseMode.MARKDOWN)
        return
    if query.data == 'tow_En_exit':
        try:
            query.message.edit_text("*EXITED*",parse_mode=ParseMode.MARKDOWN)
        except:
            query.message.delete()
            context.bot.send_message(chat_id=update.effective_chat.id,text="*EXITED*",parse_mode=ParseMode.MARKDOWN)
        return
    elif query.data == 'tow_En_back':
        button=[[InlineKeyboardButton('IFRIT 🔥',callback_data =f"tow_En_fire"),InlineKeyboardButton('ICE DRAGON ❄️',callback_data =f"tow_En_ice")],
                        [InlineKeyboardButton('DIAMONES 🌪',callback_data =f"tow_En_wind"),InlineKeyboardButton('OSIAL 🌊',callback_data =f"tow_En_water")],
                        [InlineKeyboardButton('GENESIS 🪨',callback_data =f"tow_En_earth"),InlineKeyboardButton('ELECTRO WARRIO ⚡️',callback_data =f"tow_En_electric")],
                        [InlineKeyboardButton('LIGHT MENDER ✴️',callback_data =f"tow_En_light"),InlineKeyboardButton('CHARISMATIC FLAWLESS ⚫️',callback_data =f"tow_En_dark")],
                        [InlineKeyboardButton('EXIT',callback_data =f"tow_En_exit")]]
        query.message.delete()
        context.bot.send_message(chat_id=update.effective_chat.id,text="*SELECT THE BOSS WHICH U WANT TO FIGHT*",reply_markup=InlineKeyboardMarkup(button),parse_mode=ParseMode.MARKDOWN)
        return
    cd=context.chat_data
    mob_type=query.data.split("_")[-1]
    all_monster=monster.tower_mons
    boss=all_monster[f"tow_{mob_type}"]
    user_data=[db.get_collection("user_datas"),db.get_collection("user_data"),db.get_collection("user_ids"),db.get_collection("beta_users")]
    user_obj_id = user_data[0].find_one()['user_data'][f'user_{user.id}']
    user_info=user_data[1].find_one({'_id':ObjectId(user_obj_id)})['user_info']
    if user_info['rank']<6 and user_info['rank']>0:
        level_button=[[InlineKeyboardButton('LEVEL 1',callback_data =f"mobbattle_1"),InlineKeyboardButton('LEVEL 2',callback_data =f"mobbattle_2")],
                      [InlineKeyboardButton('BACK',callback_data =f"tow_En_back"),InlineKeyboardButton('EXIT',callback_data =f"tow_En_exit")]]
    elif user_info['rank']<11 and user_info['rank']>5:
        level_button=[[InlineKeyboardButton('LEVEL 1',callback_data =f"mobbattle_1"),InlineKeyboardButton('LEVEL 2',callback_data =f"mobbattle_2"),InlineKeyboardButton('LEVEL 3',callback_data =f"mobbattle_3")],
                      [InlineKeyboardButton('LEVEL 4',callback_data =f"mobbattle_4")],
                      [InlineKeyboardButton('BACK',callback_data =f"tow_En_back"),InlineKeyboardButton('EXIT',callback_data =f"tow_En_exit")]]
    else:
        level_button=[[InlineKeyboardButton('LEVEL 1',callback_data =f"mobbattle_1"),InlineKeyboardButton('LEVEL 2',callback_data =f"mobbattle_2"),InlineKeyboardButton('LEVEL 3',callback_data =f"mobbattle_3")],
                      [InlineKeyboardButton('LEVEL 4',callback_data =f"mobbattle_4"),InlineKeyboardButton('LEVEL 5',callback_data =f"mobbattle_5"),InlineKeyboardButton('LEVEL 6',callback_data =f"mobbattle_6")],
                      [InlineKeyboardButton('BACK',callback_data =f"tow_En_back"),InlineKeyboardButton('EXIT',callback_data =f"tow_En_exit")]]
    query.message.delete()
    message=context.bot.send_photo(chat_id=update.effective_chat.id,photo=boss['level_1']['media'],caption=f"`BOSS NAME : `*{boss['level_1']['name']}*\n*SELECT THE LEVEL : *",reply_markup=InlineKeyboardMarkup(level_button),parse_mode=ParseMode.MARKDOWN)
    message_id = message.message_id
    cd.clear()
    cd[message_id] = {}
    cd[user.id] = {}
    cd[user.id]['mob'] = boss
    cd[user.id]['MESSAGE_ID']=message.message_id
    return

def tower_claimer(update,context):
    if maintenance_mode == "ON":
        if update.effective_user.id not in admins_id:
            try:
                update.callback_query.message.edit_text("*BOT UNDER MAINTENANCE*",parse_mode=ParseMode.MARKDOWN)
            except:
                update.callback_query.message.edit_caption(caption="*BOT UNDER MAINTENANCE*",parse_mode=ParseMode.MARKDOWN)
            return
    user=update.effective_user
    query=update.callback_query
    message_id=query.message.message_id
    cd=context.chat_data
    if user.id in insiders:
        query.message.edit_text("*You're in a Battle so this message got invalid*",parse_mode=ParseMode.MARKDOWN)
        return
    try:
        segil=cd[message_id]['segil']
    except:
        query.message.edit_text("*INVALID*",parse_mode=ParseMode.MARKDOWN)
        return
    user_data=[db.get_collection("user_datas"),db.get_collection("user_data"),db.get_collection("user_ids"),db.get_collection("beta_users")]
    user_obj_id = user_data[0].find_one()['user_data'][f'user_{user.id}']
    user_info=user_data[1].find_one({'_id':ObjectId(user_obj_id)})['user_info']
    user_bag=user_data[1].find_one({'_id':ObjectId(user_obj_id)})['bag']
    text=cd[message_id]['text']
    stargems=cd[message_id]['stargems']
    exp=cd[message_id]['exp']
    drop_item=cd[message_id]['drop_item']
    reward=cd[message_id]['reward']
    query.message.edit_text("*USING YOUR TOWER ENERGY ..*",parse_mode=ParseMode.MARKDOWN)
    if user_bag['tow_en']<40:
        query.message.edit_text("*YOU DON'T HAVE ENOUGH TOWER ENERGY*",parse_mode=ParseMode.MARKDOWN)
        return
    else:
        user_bag['tow_en']-=40
    user_bag['segil']+=segil
    user_bag['stargems']+=stargems
    time.sleep(0.2)
    query.message.edit_text("*USING YOUR TOWER ENERGY ....*",parse_mode=ParseMode.MARKDOWN)
    user_info['exp']+=exp
    time.sleep(0.2)
    query.message.edit_text("*USING YOUR TOWER ENERGY ......*",parse_mode=ParseMode.MARKDOWN)
    try:
        user_bag[drop_item]+=reward
    except:
        user_bag[drop_item]=reward
    time.sleep(0.2)
    query.message.edit_text("*40 TOWER ENERGY HAVE BEEN USED*",parse_mode=ParseMode.MARKDOWN)
    time.sleep(1)
    query.message.edit_text(text,parse_mode=ParseMode.MARKDOWN)
    user_data[1].update_one({"_id":ObjectId(user_obj_id)},{"$set":{'user_info':user_info}})
    user_data[1].update_one({"_id":ObjectId(user_obj_id)},{"$set":{'bag':user_bag}})
    return 

def c_level_up(update,context):
    if maintenance_mode == "ON":
        if update.effective_user.id not in admins_id:
            try:
                update.callback_query.message.edit_text("*BOT UNDER MAINTENANCE*",parse_mode=ParseMode.MARKDOWN)
            except:
                update.callback_query.message.edit_caption(caption="*BOT UNDER MAINTENANCE*",parse_mode=ParseMode.MARKDOWN)
            return
    user=update.effective_user
    query=update.callback_query
    if user.id in insiders:
        query.message.edit_caption(caption="*You're currently in a Battle *",parse_mode=ParseMode.MARKDOWN)
        return
    cd=context.chat_data
    message_id=query.message.message_id
    try:
        char_id=cd[message_id]['user_ob_id']
    except:
        query.message.edit_caption(caption="*INVALID*",parse_mode=ParseMode.MARKDOWN)
    user_data=[db.get_collection("user_datas"),db.get_collection("user_data"),db.get_collection("user_ids"),db.get_collection("beta_users")]
    user_obj_id = user_data[0].find_one()['user_data'][f'user_{user.id}']
    user_bag=user_data[1].find_one({'_id':ObjectId(user_obj_id)})['bag']
    user_characters=user_data[1].find_one({'_id': ObjectId(user_obj_id)})['user_char']
    character=user_characters[char_id]
    if character['level']>9:
        query.answer("YOUR CHARACTER IS ALREADY AT MAX LEVEL",show_alert=True)
        return
    materials_required=materials_of_chars(character)
    button=[[InlineKeyboardButton(f"CURRENT LEVEL : {character['level']}",callback_data="fuk off")],
            [InlineKeyboardButton(f"LEVEL UP TO {character['level']+1}",callback_data="level_mychar")],
            [InlineKeyboardButton("BACK",callback_data="back")]]
    query.message.edit_caption(caption=f"*SELECT THE NUMBER OF LEVEL U WANT TO INCREASE :*\n\n*MATERIALS REQUIRED : *\n\n`{materials_required['name'].split('users_')[1].upper()}` : *{materials_required['amount']}*\n`{materials_required['orb'].split('users_')[1].upper()}` : *1*\n`SEGILS : `*1000*",reply_markup=InlineKeyboardMarkup(button),parse_mode=ParseMode.MARKDOWN)
    cd[message_id]['char_num']=char_id
    return

def main_level_up(update,context):
    if maintenance_mode == "ON":
        if update.effective_user.id not in admins_id:
            try:
                update.callback_query.message.edit_text("*BOT UNDER MAINTENANCE*",parse_mode=ParseMode.MARKDOWN)
            except:
                update.callback_query.message.edit_caption(caption="*BOT UNDER MAINTENANCE*",parse_mode=ParseMode.MARKDOWN)
            return
    user=update.effective_user
    query=update.callback_query
    if user.id in insiders:
        query.message.edit_caption(caption="*You're currently in a Battle *",parse_mode=ParseMode.MARKDOWN)
        return
    cd=context.chat_data
    message_id=query.message.message_id
    try: 
        char_id=cd[message_id]['char_num']
    except:
        query.message.edit_caption(caption="*INVALID*",parse_mode=ParseMode.MARKDOWN)
    user_data=[db.get_collection("user_datas"),db.get_collection("user_data"),db.get_collection("user_ids"),db.get_collection("beta_users")]
    user_obj_id = user_data[0].find_one()['user_data'][f'user_{user.id}']
    user_characters=user_data[1].find_one({'_id': ObjectId(user_obj_id)})['user_char']
    character=user_characters[char_id]
    if character['level']>9:
        query.answer("YOUR CHARACTER IS ALREADY AT MAX LEVEL",show_alert=True)
        return
    else:
        materials_required=materials_of_chars(character)
        bag=user_data[1].find_one({'_id':ObjectId(user_obj_id)})['bag']
        material_1=materials_required['name']
        try:
            item=bag[f"{material_1}"]
        except:
            query.answer(f"YOU DON'T HAVE ENOUGH {materials_required['name'].split('users_')[1].upper()}",show_alert=True)
            return
        try:
            item_2=bag[f"{materials_required['orb']}"]
        except:
            query.answer(f"YOU DON'T HAVE ENOUGH {character['element'].upper()} ORB",show_alert=True)
            return
        if bag[f"{material_1}"]<materials_required['amount']:
            query.answer(f"YOU DON'T HAVE ENOUGH {materials_required['name'].split('users_')[1].upper()}",show_alert=True)
            return
        if bag[f"segil"]<1000:
            query.answer(f"YOU DON'T HAVE ENOUGH SEGIL",show_alert=True)
            return
        if bag[f"{materials_required['orb']}"]<1:
            query.answer(f"YOU DON'T HAVE ENOUGH {character['element'].upper()} ORB",show_alert=True)
            return
        user_characters[char_id]['level']+=1
        bag[f"{material_1}"]-=materials_required['amount']
        bag[f"segil"]-=1000
        bag[f"{materials_required['orb']}"]-=1
        user_data[1].update_one({"_id":ObjectId(user_obj_id)},{"$set":{'bag':bag}})
        user_data[1].update_one({"_id":ObjectId(user_obj_id)},{"$set":{'user_char':user_characters}})
        button=[[InlineKeyboardButton(f"CURRENT LEVEL : {character['level']}",callback_data="fuk off")],
                [InlineKeyboardButton(f"LEVEL UP TO {character['level']+1}",callback_data="level_mychar")],
                [InlineKeyboardButton("BACK",callback_data="back")]]
        materials_required=materials_of_chars(character)
        query.message.edit_caption(caption=f"*CHARACTER {character['name']} LEVELED UP TO {character['level']}\nIF YOU WANT TO LEVEL UP MORE THEN CHECKOUT THE MATERIAL :*\n\n*MATERIALS REQUIRED : *\n\n`{materials_required['name'].split('users_')[1].upper()}` : *{materials_required['amount']}*\n`{materials_required['orb'].split('users_')[1].upper()}` : *1*\n`SEGILS : `*1000*",reply_markup=InlineKeyboardMarkup(button),parse_mode=ParseMode.MARKDOWN)
        return

def back_to_character(update,context):
    if maintenance_mode == "ON":
        if update.effective_user.id not in admins_id:
            try:
                update.callback_query.message.edit_text("*BOT UNDER MAINTENANCE*",parse_mode=ParseMode.MARKDOWN)
            except:
                update.callback_query.message.edit_caption(caption="*BOT UNDER MAINTENANCE*",parse_mode=ParseMode.MARKDOWN)
            return
    user=update.effective_user
    query=update.callback_query
    if user.id in insiders:
        query.message.edit_caption(caption="*You're currently in a Battle *",parse_mode=ParseMode.MARKDOWN)
        return
    cd=context.chat_data
    message_id=query.message.message_id
    try:
        char_id=cd[message_id]['char_num']
    except:
        query.message.edit_caption(caption="*INVALID*",parse_mode=ParseMode.MARKDOWN)
    user_data=[db.get_collection("user_datas"),db.get_collection("user_data"),db.get_collection("user_ids"),db.get_collection("beta_users")]
    user_obj_id = user_data[0].find_one()['user_data'][f'user_{user.id}']
    user_character=user_data[1].find_one({'_id': ObjectId(user_obj_id)})['user_char']
    character=user_character[char_id]
    buff_level=character['level']-1
    character['atk']+=round(buff_level*0.8)
    character['def']+=round(buff_level*0.5)
    character['hp']+=round(buff_level*8)
    if update.effective_chat.id == user.id:   
        buttons=[[InlineKeyboardButton('Change weapon',callback_data=f'change_weapon_0')],[InlineKeyboardButton('INFO AND MOVES',callback_data=f'charinfo')],[InlineKeyboardButton('LEVEL UP',callback_data=f'level_up')]]
    if character['rank']==5:
        message = query.message.edit_caption(caption=f"`Character : `*{character['name']}*\n\n`Element : `*{character['element']}*\n`Rank : `*☆☆☆☆☆*\n`Level : `*{character['level']}*\n`Health Point : `*{character['hp']}*\n`Attack Power : `*{character['atk']}*\n`Defense : `*{character['def']}*\n`Speed : `*{character['speed']}*\n`Crit. Rate : `*{character['crit_rate']}%*  &  `Crit Dmg : `*{character['crit_dmg']}%*\n`Constellation : `*{character['constellation']}*\n\n`Equiped Weapon : `\n*{character['weapon'][0]['weapon_name']}*\n`Attack Boost : `*{character['weapon'][0]['buff_atk']}*",
                                             reply_markup=InlineKeyboardMarkup(buttons),parse_mode=ParseMode.MARKDOWN)
        message_id = message.message_id
        cd = context.chat_data
        cd[message_id] = {} 
        cd[message_id]['user_id'] = user.id 
        cd[message_id]['user_ob_id'] = char_id
        return
    if character['rank']==4:
        message = query.message.edit_caption(caption=f"`Character : `*{character['name']}*\n\n`Element : `*{character['element']}*\n`Rank : `*☆☆☆☆*\n`Level : `*{character['level']}*\n`Health Point : `*{character['hp']}*\n`Attack Power : `*{character['atk']}*\n`Defense : `*{character['def']}*\n`Speed : `*{character['speed']}*\n`Crit. Rate : `*{character['crit_rate']}%*  &  `Crit Dmg : `*{character['crit_dmg']}%*\n`Constellation : `*{character['constellation']}*\n\n`Equiped Weapon : `\n*{character['weapon'][0]['weapon_name']}*\n`Attack Boost : `*{character['weapon'][0]['buff_atk']}*",
                                             reply_markup=InlineKeyboardMarkup(buttons),parse_mode=ParseMode.MARKDOWN)
        message_id = message.message_id
        cd = context.chat_data
        cd[message_id] = {} 
        cd[message_id]['user_id'] = user.id 
        cd[message_id]['user_ob_id'] = char_id
        return

def materials_of_chars(c):
    character=c
    character_name=character['name']
    if character_name=='SHADOW ( BETA CHAR )':
        material_needed='users_gel'
        how_many=5*character['level']-3
        material_2=f"users_{character['element'].lower()} orb"
    elif character_name=='MORAX ( BETA CHAR )':
        material_needed="users_kobold salt"
        how_many=5*character['level']-3
        material_2=f"users_{character['element'].lower()} orb"
    elif character_name=='RYZA ( BETA CHAR )':
        material_needed='users_lizard tail'
        how_many=5*character['level']-3
        material_2=f"users_{character['element'].lower()} orb"
    elif character_name=='KRATOS':
        material_needed='users_bones'
        how_many=5*character['level']-3
        material_2=f"users_{character['element'].lower()} orb"
    elif character_name=='DIAN FARRELL':
        material_needed='users_lizard tail'
        how_many=5*character['level']-3
        material_2=f"users_{character['element'].lower()} orb"
    elif character_name=='CLAUDIA':
        material_needed='users_gel'
        how_many=5*character['level']-3
        material_2=f"users_{character['element'].lower()} orb"
    elif character_name=='TIAN LANG':
        material_needed='users_gel'
        how_many=5*character['level']-3
        material_2=f"users_{character['element'].lower()} orb"
    elif character_name=='JEAN':
        material_needed='users_goblin ears'
        how_many=5*character['level']-3
        material_2=f"users_{character['element'].lower()} orb"
    elif character_name=='FISCHL':
        material_needed='users_gel'
        how_many=5*character['level']-4
        material_2=f"users_{character['element'].lower()} orb"
    elif character_name=='ECHO':
        material_needed='users_lizard tail'
        how_many=5*character['level']-4
        material_2=f"users_{character['element'].lower()} orb"
    elif character_name=='QIQI':
        material_needed='users_bones'
        how_many=5*character['level']-4
        material_2=f"users_{character['element'].lower()} orb"
    elif character_name=='KAYLA':
        material_needed='users_goblin ears'
        how_many=5*character['level']-4
        material_2=f"users_{character['element'].lower()} orb"
    elif character_name=='KLAUDIA VALENTZ':
        material_needed='users_sweet floweer'
        how_many=5*character['level']-3
        material_2=f"users_{character['element'].lower()} orb"
    elif character_name=='FIONA':
        material_needed='users_sweet floweer'
        how_many=5*character['level']-4
        material_2=f"users_{character['element'].lower()} orb"
    elif character_name=='DOOMFIST':
        material_needed='users_kobold salt'
        how_many=5*character['level']-4
        material_2=f"users_{character['element'].lower()} orb"
    elif character_name=='LISA':
        material_needed='users_goblin ears'
        how_many=5*character['level']-4
        material_2=f"users_{character['element'].lower()} orb"
    elif character_name=='RAIDEN SHOGUN':
        material_needed='users_gel'
        how_many=5*character['level']-3
        material_2=f"users_{character['element'].lower()} orb"
    elif character_name=='SEKIRO':
        material_needed='users_blood of dead'
        how_many=5*character['level']-3
        material_2=f"users_{character['element'].lower()} orb"
    elif character_name=='BENNETT':
        material_needed='users_gel'
        how_many=5*character['level']-4
        material_2=f"users_{character['element'].lower()} orb"
    elif character_name=='CANDACE':
        material_needed='users_lizard tail'
        how_many=5*character['level']-4
        material_2=f"users_{character['element'].lower()} orb"
    elif character_name=='YUKONG':
        material_needed='users_blood of dead'
        how_many=5*character['level']-4
        material_2=f"users_{character['element'].lower()} orb"
    else:
        material_needed='users_gel'
        how_many=5*character['level']-3
        material_2=f"users_{character['element'].lower()} orb"
    material={"name":material_needed,"amount":how_many,"orb":material_2}
    return material
    
def my_kingdom(update,context):
    if maintenance_mode == "ON":
        if update.effective_user.id not in admins_id:
            try:
                update.callback_query.message.edit_text("*BOT UNDER MAINTENANCE*",parse_mode=ParseMode.MARKDOWN)
            except:
                update.callback_query.message.edit_caption(caption="*BOT UNDER MAINTENANCE*",parse_mode=ParseMode.MARKDOWN)
            return
    user=update.effective_user
    query=update.callback_query
    cd=context.chat_data
    message_id = query.message.message_id
    try:
        user_id=cd[message_id]['user_id']
    except:
        query.message.edit_text("*THIS COMMAND IS NOW INVALID*",parse_mode=ParseMode.MARKDOWN)
        return
    if user_id==user.id:
        kingdom_id=None
        kingdoms=db.get_collection("all_kingdoms")
        kingdom_data = kingdoms.find_one()['kingdom_datas']
        for i in range(len(list(kingdom_data.keys()))):
            kingdom_members=kingdom_data[f"kingdom_{i+1}"]['members']
            if user.id in kingdom_members:
                kingdom_id=i+1
            if user.id == kingdom_data[f"kingdom_{i+1}"]['KING_DUKE']['KING']:
                kingdom_id=i+1
            if user.id == kingdom_data[f"kingdom_{i+1}"]['KING_DUKE']['DUKE']:
                kingdom_id=i+1
        print(kingdom_id)
        if kingdom_id==None:
            query.message.edit_text("*SEEMS LIKE YOU'RE NOT IN ANY KINGDOM*",parse_mode=ParseMode.MARKDOWN)
            return
        else:
            kingdom=kingdom_data[f"kingdom_{kingdom_id}"]
            user_data=[db.get_collection("user_datas"),db.get_collection("user_data"),db.get_collection("user_ids"),db.get_collection("beta_users")]
            user_obj_id = user_data[0].find_one()['user_data'][f"user_{user.id}"]
            try:
                user_kingdom=user_data[1].find_one({'_id': ObjectId(user_obj_id)})['extras']['in_kingdom_data']
            except:
                user_extras=user_data[1].find_one({'_id': ObjectId(user_obj_id)})['extras']
                if user.id==kingdom_data[f"kingdom_{kingdom_id}"]['KING_DUKE']['DUKE']:
                    user_extras['in_kingdom_data']={"user_role":"DUKE (BUTLER OF KING)","user_gold":2,"user_silver":50,"user_kingdom":f"{kingdom_data[f'kingdom_{kingdom_id}']['name']}"}
                    user_data[1].update_one({"_id":ObjectId(user_obj_id)},{"$set":{'extras':user_extras}})
                elif user.id==kingdom_data[f"kingdom_{kingdom_id}"]['KING_DUKE']['KING']:
                    user_extras['in_kingdom_data']={"user_role":"KING (RULER OF KINGDOM)","user_gold":5,"user_silver":50,"user_kingdom":f"{kingdom_data[f'kingdom_{kingdom_id}']['name']}"}
                    user_data[1].update_one({"_id":ObjectId(user_obj_id)},{"$set":{'extras':user_extras}})
                else:
                    query.message.edit_text("*SOMETHING WENT WRONG\nREPORT TO @Shadow_Iord*",parse_mode=ParseMode.MARKDOWN)
                    return
                user_kingdom=user_extras['in_kingdom_data']
            button=[[InlineKeyboardButton(f"BACK",callback_data=f'kingdomjoinextra_back')]]
            text=""
            if user_kingdom['user_role']=="atk":
                user_role="`🗡 ROLE : `*ATTACKER*"
            elif user_kingdom['user_role']=="def":
                user_role="`🛡 ROLE : `*DEFENDER*"
            else:
                button=[[InlineKeyboardButton(f"KINGDOM STRENGTH",callback_data=f'king_military')],[InlineKeyboardButton(f"TOTAL CITIZANS",callback_data=f'king_members')],[InlineKeyboardButton(f"BACK",callback_data=f'kingdomjoinextra_back')]]
                user_role=f"`🤴 ROLE : `*{user_kingdom['user_role']}*\n\n`KINGDOM BANK : \nGOLD : `*{kingdom_data[f'kingdom_{kingdom_id}']['resources']['gold']}*\n`SILVERS : `*{kingdom_data[f'kingdom_{kingdom_id}']['resources']['silver']}*\n`TOTAL KINGDOM HOUSES : `*{kingdom_data[f'kingdom_{kingdom_id}']['structural']['houses']}*"
            text+=f"`NAME : `*{user.first_name}*\n\n`🟡 GOLD : {user_kingdom['user_gold']}`\n`🪙 SILVER : {user_kingdom['user_silver']}`\n{user_role}\n\n`🏰 KINGDOM : `*{kingdom['name']}*"
            query.message.edit_text(text,reply_markup=InlineKeyboardMarkup(button),parse_mode=ParseMode.MARKDOWN)
    else:
        query.answer("NOT YOUR COMMAND",show_alert=True)
        return

def kingdom_power(update,context):
    if maintenance_mode == "ON":
        if update.effective_user.id not in admins_id:
            try:
                update.callback_query.message.edit_text("*BOT UNDER MAINTENANCE*",parse_mode=ParseMode.MARKDOWN)
            except:
                update.callback_query.message.edit_caption(caption="*BOT UNDER MAINTENANCE*",parse_mode=ParseMode.MARKDOWN)
            return
    user=update.effective_user
    query=update.callback_query
    cd=context.chat_data
    message_id = query.message.message_id
    try:
        user_id=cd[message_id]['user_id']
    except:
        query.message.edit_text("*THIS COMMAND IS NOW INVALID*",parse_mode=ParseMode.MARKDOWN)
        return
    if query.data == "king_military":
        if user_id==user.id:
            kingdom_id=None
            kingdoms=db.get_collection("all_kingdoms")
            kingdom_data = kingdoms.find_one()['kingdom_datas']
            for i in range(len(list(kingdom_data.keys()))):
                kingdom_members=kingdom_data[f"kingdom_{i+1}"]['members']
                if user.id == kingdom_data[f"kingdom_{i+1}"]['KING_DUKE']['KING']:
                    kingdom_id=i+1
                if user.id == kingdom_data[f"kingdom_{i+1}"]['KING_DUKE']['DUKE']:
                    kingdom_id=i+1
            if kingdom_id == None:
                query.message.edit_text("*YOU'RE NOT A KING NOR A DUKE\Access Denied*",parse_mode=ParseMode.MARKDOWN)
                return
            kingdom=kingdom_data[f'kingdom_{kingdom_id}']
            button=[[InlineKeyboardButton(f"BACK",callback_data=f'kingdomjoinextra_back')]]
            user_data=[db.get_collection("user_datas"),db.get_collection("user_data"),db.get_collection("user_ids"),db.get_collection("beta_users")]
            kingdom_hp=kingdom['structural']['kingdom_def']
            kingdom_attack=2
            kingdom_def=2
            kingdom_speed=20
            for i in range(len(kingdom['members'])):
                user_obj_id=user_data[0].find_one()['user_data'][f"user_{kingdom['members'][i]}"]
                user_role=user_data[1].find_one({'_id': ObjectId(user_obj_id)})['extras']['in_kingdom_data']['user_role']
                if user_role == 'atk':
                    kingdom_attack+=0.6
                    kingdom_speed+=8
                elif user_role == 'def':
                    kingdom_def+=0.6
                    kingdom_hp+=802
            text=f"`KINGDOM : {kingdom['name']}`\n\n`KINGDOM HP : `*{round(kingdom_hp)}*\n`KINGDOM ATTACK POWER : `*{round(kingdom_attack)}*\n`KINGDOM DEFENSE POWER : `*{round(kingdom_def)}*\n`KINGDOM MILITARY SPEED : `*{round(kingdom_speed)}*"
            query.message.edit_text(text,reply_markup=InlineKeyboardMarkup(button),parse_mode=ParseMode.MARKDOWN)
        else:
            query.answer("NOT YOUR COMMAND",show_alert=True)
            return
    if query.data == "king_members":
        if user_id==user.id:
            kingdom_id=None
            kingdoms=db.get_collection("all_kingdoms")
            kingdom_data = kingdoms.find_one()['kingdom_datas']
            for i in range(len(list(kingdom_data.keys()))):
                kingdom_members=kingdom_data[f"kingdom_{i+1}"]['members']
                if user.id == kingdom_data[f"kingdom_{i+1}"]['KING_DUKE']['KING']:
                    kingdom_id=i+1
                if user.id == kingdom_data[f"kingdom_{i+1}"]['KING_DUKE']['DUKE']:
                    kingdom_id=i+1
            if kingdom_id == None:
                query.message.edit_text("*YOU'RE NOT A KING NOR A DUKE\Access Denied*",parse_mode=ParseMode.MARKDOWN)
                return
            kingdom=kingdom_data[f'kingdom_{kingdom_id}']
            button=[[InlineKeyboardButton(f"KICK CITIZEN",callback_data=f'king_kicker')],[InlineKeyboardButton(f"BACK",callback_data=f'kingdomjoinextra_back')]]
            text=f"`YOUR KINGDOM MEMBERS : `\n\n"
            for s in range(len(kingdom['members'])):
                user_of_king = context.bot.getChat(kingdom['members'][s])
                text+=f"[{user_of_king.first_name}](tg://user?id={kingdom['members'][s]}) \n"
            query.message.edit_text(text,reply_markup=InlineKeyboardMarkup(button),parse_mode=ParseMode.MARKDOWN)
            return
        else:
            query.answer("NOT YOUR COMMAND",show_alert=True)
            return
    if query.data == "king_members":
        if user_id==user.id:
            kingdom_id=None
            kingdoms=db.get_collection("all_kingdoms")
            kingdom_data = kingdoms.find_one()['kingdom_datas']
            for i in range(len(list(kingdom_data.keys()))):
                kingdom_members=kingdom_data[f"kingdom_{i+1}"]['members']
                if user.id == kingdom_data[f"kingdom_{i+1}"]['KING_DUKE']['KING']:
                    kingdom_id=i+1
                if user.id == kingdom_data[f"kingdom_{i+1}"]['KING_DUKE']['DUKE']:
                    kingdom_id=i+1
            if kingdom_id == None:
                query.message.edit_text("*YOU'RE NOT A KING NOR A DUKE\Access Denied*",parse_mode=ParseMode.MARKDOWN)
                return
            kingdom=kingdom_data[f'kingdom_{kingdom_id}']
            text=f"`YOUR KINGDOM MEMBERS : `\n\n"
            for s in range(len(kingdom['members'])):
                user_of_king = context.bot.getChat(kingdom['members'][s])
                text+=f"{i+1}"+"}"+f" [{user_of_king.first_name}](tg://user?id={kingdom['members'][s]}) \n"
            text+="*SELECT THE USER YOU WOULD LIKE TO KICK*"
            button=[[InlineKeyboardButton(f"BACK",callback_data=f'kingdomjoinextra_back')]]
            query.message.edit_text(text,reply_markup=InlineKeyboardMarkup(button),parse_mode=ParseMode.MARKDOWN)
            return
        else:
            query.answer("NOT YOUR COMMAND",show_alert=True)
            return
        
def charac(update,context):
    if maintenance_mode == "ON":
        if update.effective_user.id not in admins_id:
            update.message.reply_text("*BOT UNDER MAINTENANCE*",parse_mode=ParseMode.MARKDOWN)
            return
    user=update.effective_user
    user_data=[db.get_collection("user_datas"),db.get_collection("user_data"),db.get_collection("user_ids"),db.get_collection("beta_users")]
    if user.id in user_data[3].find_one()['beta_players']:
        update.message.reply_text("*SEDLY U R NOT ELIGIBLE TO USE THIS COMMAND*",parse_mode=ParseMode.MARKDOWN)
        return
    else:
        if user.id not in user_data[2].find_one()['user_ids']:
            keyboard=[[InlineKeyboardButton('PM',url='https://t.me/PSO_SoBot?start=characters')]]
            update.message.reply_video(video='https://graph.org/file/e663ce2ffd9c8c32d3247.mp4',caption="*It seems like u haven't started\nClick on the button given below and start the bot*",reply_markup=InlineKeyboardMarkup(keyboard),parse_mode=ParseMode.MARKDOWN)
            return
        user_obj_id = user_data[0].find_one()['user_data'][f'user_{user.id}']
        user_character=user_data[1].find_one({'_id': ObjectId(user_obj_id)})['user_char']
        text = "`Your characters :`\n\n"
        n=0
        for i in user_character:
            text+=f"*◇ {user_character[n]['name']} [ {user_character[n]['level']} ]\n*"
            n+=1
        update.message.reply_text(text+"\n*LEVEL's are given besides the character name*",parse_mode=ParseMode.MARKDOWN)
        return

def update_db(update,context):
    if maintenance_mode == "ON":
        if update.effective_user.id not in admins_id:
            update.message.reply_text("*BOT UNDER MAINTENANCE*",parse_mode=ParseMode.MARKDOWN)
            return
    user=update.message.from_user
    if user.id == 1864257459:
        user_data=[db.get_collection("user_datas"),db.get_collection("user_data"),db.get_collection("user_ids"),db.get_collection("beta_users")]
        for i in range(len(user_data[2].find_one()['user_ids'])):
            user_obj_id = user_data[0].find_one()['user_data'][f"user_{user_data[2].find_one()['user_ids'][i]}"]
            user_info = user_data[1].find_one({'_id':ObjectId(user_obj_id)})['user_info']
            user_info['mana']=800
            user_data[1].update_one({"_id":ObjectId(user_obj_id)},{"$set":{'user_info':user_info}})
        update.message.reply_text("*UPDATED*",parse_mode=ParseMode.MARKDOWN)
        return
    update.message.reply_text("*NO BITCHES*",parse_mode=ParseMode.MARKDOWN)

def battle_maker(update,context):
    if maintenance_mode == "ON":
        if update.effective_user.id not in admins_id:
            update.message.reply_text("*BOT UNDER MAINTENANCE*",parse_mode=ParseMode.MARKDOWN)
    user=update.effective_user
    if not update.message.reply_to_message:
        update.message.reply_text("*REPLY TO A USER*",parse_mode=ParseMode.MARKDOWN)
        return
    replied_user=update.message.reply_to_message.from_user
    cd=context.chat_data
    global insiders , battlers
    if user.id == replied_user.id :
        update.message.reply_text("*YOU CANNOT FIGHT YOURSELF*",parse_mode=ParseMode.MARKDOWN) 
        return
    if replied_user.id in [6343863154,6149996968]:
        update.message.reply_text("*HUH TRYING TO CHALLENGE ME ?\n\nI'M FAR STRONGER THAN U KIDDO\nGET LOST*",parse_mode=ParseMode.MARKDOWN) 
        return
    if replied_user in insiders or replied_user in battlers :
        update.message.reply_text("*REPLIED USER IS CURRENTLY IN A BATTLE*",parse_mode=ParseMode.MARKDOWN) 
        return
    if user.id in insiders or user.id in battlers :
        update.message.reply_text("*YOU'RE CURRENTLY IN A BATTLE*",parse_mode=ParseMode.MARKDOWN) 
        return
    button=[[InlineKeyboardButton(f" Accept ",callback_data=f'pvpstarter_accept_{replied_user.id}'),InlineKeyboardButton(f"CANCEL",callback_data=f'pvpstarter_cancel_{user.id}')]]
    message=update.message.reply_text(f"[You](tg://user?id={user.id}) have challenge to the USER : [{replied_user.first_name}](tg://user?id={replied_user.id})\n\n[{replied_user.first_name}](tg://user?id={replied_user.id}) would you like to accept ?",reply_markup=InlineKeyboardMarkup(button),parse_mode=ParseMode.MARKDOWN)
    message_id=message.message_id
    cd[message_id]={}
    cd[message_id]['user_id']=user.id
    return

def pvp_battle_handler(update,context):
    if maintenance_mode == "ON":
        if update.effective_user.id not in admins_id:
            try:
                update.callback_query.message.edit_text("*BOT UNDER MAINTENANCE*",parse_mode=ParseMode.MARKDOWN)
            except:
                update.callback_query.message.edit_caption(caption="*BOT UNDER MAINTENANCE*",parse_mode=ParseMode.MARKDOWN)
            return
    user=update.callback_query.from_user
    query=update.callback_query
    cd=context.chat_data
    if query.data.split("_")[1]=="cancel":
        if user.id == int(query.data.split("_")[-1]):
            query.message.edit_text("*CANCELLED THE BATTLE*",parse_mode=ParseMode.MARKDOWN)
            return
        else:
            query.answer("NOT YOUR COMMAND NIGGA",show_alert=True)
            return
    message_id= query.message.message_id
    user_1_id=int(query.data.split("_")[-1])
    user_2_id=cd[message_id]['user_id']
    user_data=[db.get_collection("user_datas"),db.get_collection("user_data"),db.get_collection("user_ids"),db.get_collection("beta_users")]
    if user.id == user_1_id:
        query.message.edit_text("*BATTLING STARTING \nNIGGAS GET READY *",parse_mode=ParseMode.MARKDOWN)
        try:
            user_1_obj_id = user_data[0].find_one()['user_data'][f'user_{user_1_id}']
        except:
            query.message.edit_text(f"[PLAYER 1](tg://user?id={user_1_id}) HAVE'NT STARTED THE BOT YET",parse_mode=ParseMode.MARKDOWN)
            return
        try:
            user_2_obj_id = user_data[0].find_one()['user_data'][f'user_{user_2_id}']
        except:
            query.message.edit_text(f"[PLAYER 2](tg://user?id={user_2_id}) HAVE'NT STARTED THE BOT YET",parse_mode=ParseMode.MARKDOWN)
            return
        user_1_id_team= user_data[1].find_one({'_id': ObjectId(user_1_obj_id)})['team']
        user_2_id_team= user_data[1].find_one({'_id': ObjectId(user_2_obj_id)})['team']
        user_1_characters=user_data[1].find_one({'_id': ObjectId(user_1_obj_id)})['user_char']
        user_2_characters=user_data[1].find_one({'_id': ObjectId(user_2_obj_id)})['user_char']
        for ij1 in range(len(user_1_characters)):
            user_1_characters[ij1]['usage_pas']=charamoves(user_1_characters[ij1])['skill_move']['usage']
            buff_level=user_1_characters[ij1]['level']-1
            user_1_characters[ij1]['atk']+=round(buff_level*0.8)
            user_1_characters[ij1]['def']+=round(buff_level*0.5)
            user_1_characters[ij1]['hp']+=round(buff_level*8)
            user_1_characters[ij1]['new_hp']=user_1_characters[ij1]['hp']
            if user_1_characters[ij1]['name']=="SEKIRO":
                user_1_characters[ij1]['immortality']=1
        for ij2 in range(len(user_2_characters)):
            user_2_characters[ij2]['usage_pas']=charamoves(user_2_characters[ij2])['skill_move']['usage']
            buff_level=user_2_characters[ij2]['level']-1
            user_2_characters[ij2]['atk']+=round(buff_level*0.8)
            user_2_characters[ij2]['def']+=round(buff_level*0.5)
            user_2_characters[ij2]['hp']+=round(buff_level*8)
            user_2_characters[ij2]['new_hp']=user_2_characters[ij2]['hp']
            if user_2_characters[ij2]['name']=="SEKIRO":
                user_2_characters[ij2]['immortality']=1
        if_not_1=4
        if_not_2=4
        user_1_char_skil={}
        user_2_char_skil={}
        for i in range(4):
            if user_1_id_team[f'team_player_{i+1}']['name']=='None':
                if_not_1-=1
            else:
                for j in range(len(user_1_characters)):
                    if user_1_characters[j]['name']==user_1_id_team[f'team_player_{i+1}']['name']:
                        user_1_id_team[f'team_player_{i+1}']=user_1_characters[j]
                        user_1_id_team[f'team_player_{i+1}']['atk']+=round(user_1_id_team[f'team_player_{i+1}']['weapon'][0]['buff_atk'])
                        user_1_id_team[f'team_player_{i+1}']['dead']='False'
                user_1_player_name=user_1_id_team[f'team_player_{i+1}']['name']
                user_1_char_skil[f'{user_1_player_name}']={}
                user_1_char_skil[f'{user_1_player_name}']['rounds']=0
            if user_2_id_team[f'team_player_{i+1}']['name']=='None':
                if_not_2-=1
            else:
                for k in range(len(user_2_characters)):
                    if user_2_characters[k]['name']==user_2_id_team[f'team_player_{i+1}']['name']:
                        user_2_id_team[f'team_player_{i+1}']=user_2_characters[k]
                        user_2_id_team[f'team_player_{i+1}']['atk']+=round(user_2_id_team[f'team_player_{i+1}']['weapon'][0]['buff_atk'])
                        user_2_id_team[f'team_player_{i+1}']['dead']='False'
                user_2_player_name=user_2_id_team[f'team_player_{i+1}']['name']
                user_2_char_skil[f'{user_2_player_name}']={}
                user_2_char_skil[f'{user_2_player_name}']['rounds']=0
        if if_not_1<1 or if_not_2<1:
            if if_not_1<1 :
                query.message.edit_text(f"[PLAYER 1 ](tg://user?id={user_1_id}) *TEAM NOT SET*",parse_mode=ParseMode.MARKDOWN)
                return
            elif if_not_2<1 :
                query.message.edit_text(f"[PLAYER 2 ](tg://user?id={user_2_id}) *TEAM NOT SET*",parse_mode=ParseMode.MARKDOWN)
                return
            else:
                query.message.edit_text("*BUG IN TEAM REPORT TO OWNER*",parse_mode=ParseMode.MARKDOWN)
                return
        global insiders
        insiders.append(user_1_id)
        insiders.append(user_2_id)
        if user_1_id_team[f'team_player_{1}']['speed']>user_2_id_team[f'team_player_{1}']['speed']:
            moves=charamoves(user_1_id_team[f"team_player_{1}"])
            keyboard=[[InlineKeyboardButton(f"{moves['normal_move']['name']}",callback_data=f'pvpmu_normal_{user_1_id}')],[InlineKeyboardButton(f"{moves['dodge_move']['name']}",callback_data=f'pvpmu_dodge_{user_1_id}'),InlineKeyboardButton(f"SWAP",callback_data=f'pvpmuu_swap_{user_1_id}'),InlineKeyboardButton(f"DRA",callback_data=f'pvpmuu_draw_{user_1_id}_{user_2_id}')],[InlineKeyboardButton(f"WITHDRAW",callback_data=f'pvpmu_withdraw_{user_1_id}_{user_2_id}')]]
            message=query.message.edit_text(f"*IT SEEMS *[PLAYER 1](tg://user?id={user_1_id}) *{user_1_id_team[f'team_player_{1}']['name']} is Faster than *[PLAYER 2](tg://user?id={user_2_id}) *{user_2_id_team[f'team_player_{1}']['name']}*\n\n[PLAYER 1](tg://user?id={user_1_id}) :  *{user_1_id_team[f'team_player_{1}']['name']} [ {user_1_id_team[f'team_player_{1}']['element']} ]*\n`{user_1_id_team[f'team_player_{1}']['name']} HP : `*{user_1_id_team[f'team_player_{1}']['hp']}*\n\n[PLAYER 2](tg://user?id={user_2_id}) :  *{user_2_id_team[f'team_player_{1}']['name']} [ {user_2_id_team[f'team_player_{1}']['element']} ]*\n`{user_2_id_team[f'team_player_{1}']['name']} HP : `*{user_2_id_team[f'team_player_{1}']['hp']}*\n\n[PLAYER 1](tg://user?id={user_2_id}) *CHOOSE THE MOVE :*",reply_markup=InlineKeyboardMarkup(keyboard),parse_mode=ParseMode.MARKDOWN)
            message_id = message.message_id
            cd[message_id] = {}
            cd[message_id]['users']={"user_1_id":user_1_id,"user_2_id":user_2_id}
            cd[message_id]['teams']={"user_1_team":user_1_id_team,"user_2_team":user_2_id_team}
            cd[message_id]['passive']={"user_1_pass":user_1_char_skil,"user_2_pass":user_2_char_skil}
            cd[message_id]['move_done']={f"user_{user_1_id}_move":"",f"user_{user_2_id}_move":""}
            cd[message_id]['pvp_player_no']={"user_1s_id":1,"user_2s_id":1}
            return
        else:
            moves=charamoves(user_2_id_team[f"team_player_{1}"])
            keyboard=[[InlineKeyboardButton(f"{moves['normal_move']['name']}",callback_data=f'pvpmu_normal_{user_2_id}')],[InlineKeyboardButton(f"{moves['dodge_move']['name']}",callback_data=f'pvpmu_dodge_{user_2_id}'),InlineKeyboardButton(f"SWAP",callback_data=f'pvpmuu_swap_{user_2_id}'),InlineKeyboardButton(f"DRAW",callback_data=f'pvpmuu_draw_{user_1_id}_{user_2_id}')],[InlineKeyboardButton(f"WITHDRAW",callback_data=f'pvpmu_withdraw_{user_1_id}_{user_2_id}')]]
            message=query.message.edit_text(f"*IT SEEMS *[PLAYER 2](tg://user?id={user_2_id}) *{user_2_id_team[f'team_player_{1}']['name']} is Faster than *[PLAYER 1](tg://user?id={user_1_id}) *{user_1_id_team[f'team_player_{1}']['name']}*\n\n[PLAYER 2](tg://user?id={user_2_id}) :  *{user_2_id_team[f'team_player_{1}']['name']} [ {user_2_id_team[f'team_player_{1}']['element']} ]*\n`{user_2_id_team[f'team_player_{1}']['name']} HP : `*{user_2_id_team[f'team_player_{1}']['hp']}*\n\n[PLAYER 1](tg://user?id={user_1_id}) :  *{user_1_id_team[f'team_player_{1}']['name']} [ {user_1_id_team[f'team_player_{1}']['element']} ]*\n`{user_1_id_team[f'team_player_{1}']['name']} HP : `*{user_1_id_team[f'team_player_{1}']['hp']}*\n\n[PLAYER 2](tg://user?id={user_2_id}) *CHOOSE THE MOVE :*",reply_markup=InlineKeyboardMarkup(keyboard),parse_mode=ParseMode.MARKDOWN)
            message_id = message.message_id
            cd[message_id] = {}
            cd[message_id]['users']={"user_1_id":user_1_id,"user_2_id":user_2_id}
            cd[message_id]['teams']={"user_1_team":user_1_id_team,"user_2_team":user_2_id_team}
            cd[message_id]['passive']={"user_1_pass":user_1_char_skil,"user_2_pass":user_2_char_skil}
            cd[message_id]['move_done']={f"user_{user_1_id}_move":"",f"user_{user_2_id}_move":""}
            cd[message_id]['pvp_player_no']={"user_1s_id":1,"user_2s_id":1}
            return
    else:
        query.answer("NOT YOUR COMMAND NIGGA",show_alert=True)
        return

def pvp_muu(update,context):
    global insiders
    if maintenance_mode == "ON":
        if update.effective_user.id not in admins_id:
            try:
                update.callback_query.message.edit_text("*BOT UNDER MAINTENANCE*",parse_mode=ParseMode.MARKDOWN)
            except:
                update.callback_query.message.edit_caption(caption="*BOT UNDER MAINTENANCE*",parse_mode=ParseMode.MARKDOWN)
            return
    user=update.callback_query.from_user
    query=update.callback_query
    cd=context.chat_data
    message_id=query.message.message_id
    user_passive=cd[message_id]['passive']
    user_teams=cd[message_id]['teams']
    users=cd[message_id]['users']
    move=cd[message_id]['move_done']
    player_no=cd[message_id]['pvp_player_no']
    user_1_player=player_no['user_1s_id']
    user_2_player=player_no['user_2s_id']
    user_1_id = users['user_1_id']
    user_2_id = users['user_2_id']
    if query.data.split("_")[1] == "normal":
        if user.id != int(query.data.split('_')[2]):
            query.answer("NOT YOUR COMMAND NIGGA",show_alert=True)
            return
        move[f"user_{int(query.data.split('_')[2])}_move"]="normal"
        rool_aa=2
        for i in range(2):
            if move[f"user_{users[f'user_{i+1}_id']}_move"] == "":
                if i+1 == 1 :
                    user_1_id_team = user_teams['user_1_team']
                    user_2_id_team = user_teams['user_2_team']
                    moves=charamoves(user_1_id_team[f"team_player_{player_no['user_1s_id']}"])
                    keyboard=[[InlineKeyboardButton(f"{moves['normal_move']['name']}",callback_data=f'pvpmu_normal_{user_1_id}')],[InlineKeyboardButton(f"{moves['dodge_move']['name']}",callback_data=f'pvpmu_dodge_{user_1_id}'),InlineKeyboardButton(f"SWAP",callback_data=f'pvpmuu_swap_{user_1_id}'),InlineKeyboardButton(f"DRA",callback_data=f'pvpmuu_draw_{user_1_id}_{user_2_id}')],[InlineKeyboardButton(f"WITHDRAW",callback_data=f'pvpmu_withdraw_{user_1_id}_{user_2_id}')]]
                    text1=""
                    text1+=f"*AS *[PLAYER 2](tg://user?id={users['user_2_id']})* have already choosen the Attack\nNOW *[PLAYER 1](tg://user?id={users['user_1_id']})* choose the attack you would like to do*"
                    text1+=f"\n\n[PLAYER 1](tg://user?id={users['user_1_id']}) :  *{user_1_id_team[f'team_player_{user_1_player}']['name']} [ {user_1_id_team[f'team_player_{user_1_player}']['element']} ]*\n`{user_1_id_team[f'team_player_{user_1_player}']['name']} HP : `*{user_1_id_team[f'team_player_{user_1_player}']['hp']}*\n\n[PLAYER 2](tg://user?id={users['user_2_id']}) :  *{user_2_id_team[f'team_player_{user_2_player}']['name']} [ {user_2_id_team[f'team_player_{user_2_player}']['element']} ]*\n`{user_2_id_team[f'team_player_{user_2_player}']['name']} HP : `*{user_2_id_team[f'team_player_{user_2_player}']['hp']}*"
                    text1+=f"\n\n[PLAYER 1](tg://user?id={users['user_1_id']}) *choose the move*"
                    message=query.message.edit_text(text1,reply_markup=InlineKeyboardMarkup(keyboard),parse_mode=ParseMode.MARKDOWN)
                    message_id = message.message_id
                    cd[message_id] = {}
                    cd[message_id]['users']=users
                    cd[message_id]['teams']=user_teams
                    cd[message_id]['passive']=user_passive
                    cd[message_id]['move_done']=move
                    cd[message_id]['pvp_player_no']=player_no
                elif i+1 == 2 :
                    user_2_id_team = user_teams['user_2_team']
                    user_1_id_team = user_teams['user_1_team']
                    moves=charamoves(user_2_id_team[f"team_player_{1}"])
                    keyboard=[[InlineKeyboardButton(f"{moves['normal_move']['name']}",callback_data=f'pvpmu_normal_{user_2_id}')],[InlineKeyboardButton(f"{moves['dodge_move']['name']}",callback_data=f'pvpmu_dodge_{user_2_id}'),InlineKeyboardButton(f"SWAP",callback_data=f'pvpmuu_swap_{user_2_id}'),InlineKeyboardButton(f"DRAW",callback_data=f'pvpmuu_draw_{user_1_id}_{user_2_id}')],[InlineKeyboardButton(f"WITHDRAW",callback_data=f'pvpmu_withdraw_{user_1_id}_{user_2_id}')]]
                    text2=""
                    text2+=f"*AS *[PLAYER 1](tg://user?id={users['user_1_id']})* have already choosen the Attack\nNOW *[PLAYER 2](tg://user?id={users['user_2_id']})* choose the attack you would like to do*"
                    text2+=f"\n\n[PLAYER 2](tg://user?id={users['user_2_id']}) :  *{user_2_id_team[f'team_player_{user_2_player}']['name']} [ {user_2_id_team[f'team_player_{user_2_player}']['element']} ]*\n`{user_2_id_team[f'team_player_{user_2_player}']['name']} HP : `*{user_2_id_team[f'team_player_{user_2_player}']['hp']}*\n\n[PLAYER 1](tg://user?id={users['user_1_id']}) :  *{user_1_id_team[f'team_player_{user_1_player}']['name']} [ {user_1_id_team[f'team_player_{user_1_player}']['element']} ]*\n`{user_1_id_team[f'team_player_{user_1_player}']['name']} HP : `*{user_1_id_team[f'team_player_{user_1_player}']['hp']}*"
                    text2+=f"\n\n[PLAYER 2](tg://user?id={users['user_2_id']}) *choose the move*"
                    message=query.message.edit_text(text2,reply_markup=InlineKeyboardMarkup(keyboard),parse_mode=ParseMode.MARKDOWN)
                    message_id = message.message_id
                    cd[message_id] = {}
                    cd[message_id]['users']=users
                    cd[message_id]['teams']=user_teams
                    cd[message_id]['passive']=user_passive
                    cd[message_id]['move_done']=move
                    cd[message_id]['pvp_player_no']=player_no 
            else:
                rool_aa-=1
        if rool_aa == 0 :
            passer_pvp(update,context)
            return
    elif query.data.split("_")[1] == "dodge":
        if user.id != int(query.data.split('_')[2]):
            query.answer("NOT YOUR COMMAND NIGGA",show_alert=True)
            return
        move[f"user_{int(query.data.split('_')[2])}_move"]="dodge"
        rool_aa=2
        for i in range(2):
            if move[f"user_{users[f'user_{i+1}_id']}_move"] == "":
                if i+1 == 1 :
                    user_1_id_team = user_teams['user_1_team']
                    user_2_id_team = user_teams['user_2_team']
                    moves=charamoves(user_1_id_team[f"team_player_{player_no['user_1s_id']}"])
                    keyboard=[[InlineKeyboardButton(f"{moves['normal_move']['name']}",callback_data=f'pvpmu_normal_{user_1_id}')],[InlineKeyboardButton(f"{moves['dodge_move']['name']}",callback_data=f'pvpmu_dodge_{user_1_id}'),InlineKeyboardButton(f"SWAP",callback_data=f'pvpmuu_swap_{user_1_id}'),InlineKeyboardButton(f"DRA",callback_data=f'pvpmuu_draw_{user_1_id}_{user_2_id}')],[InlineKeyboardButton(f"WITHDRAW",callback_data=f'pvpmu_withdraw_{user_1_id}_{user_2_id}')]]
                    text1=""
                    text1+=f"*AS *[PLAYER 2](tg://user?id={users['user_2_id']})* have already choosen the Attack\nNOW *[PLAYER 1](tg://user?id={users['user_1_id']})* choose the attack you would like to do*"
                    text1+=f"\n\n[PLAYER 1](tg://user?id={users['user_1_id']}) :  *{user_1_id_team[f'team_player_{user_1_player}']['name']} [ {user_1_id_team[f'team_player_{user_1_player}']['element']} ]*\n`{user_1_id_team[f'team_player_{user_1_player}']['name']} HP : `*{user_1_id_team[f'team_player_{user_1_player}']['hp']}*\n\n[PLAYER 2](tg://user?id={users['user_2_id']}) :  *{user_2_id_team[f'team_player_{user_2_player}']['name']} [ {user_2_id_team[f'team_player_{user_2_player}']['element']} ]*\n`{user_2_id_team[f'team_player_{user_2_player}']['name']} HP : `*{user_2_id_team[f'team_player_{user_2_player}']['hp']}*"
                    text1+=f"\n\n[PLAYER 1](tg://user?id={users['user_1_id']}) *choose the move*"
                    message=query.message.edit_text(text1,reply_markup=InlineKeyboardMarkup(keyboard),parse_mode=ParseMode.MARKDOWN)
                    message_id = message.message_id
                    cd[message_id] = {}
                    cd[message_id]['users']=users
                    cd[message_id]['teams']=user_teams
                    cd[message_id]['passive']=user_passive
                    cd[message_id]['move_done']=move
                    cd[message_id]['pvp_player_no']=player_no
                elif i+1 == 2 :
                    user_2_id_team = user_teams['user_2_team']
                    user_1_id_team = user_teams['user_1_team']
                    moves=charamoves(user_2_id_team[f"team_player_{1}"])
                    keyboard=[[InlineKeyboardButton(f"{moves['normal_move']['name']}",callback_data=f'pvpmu_normal_{user_2_id}')],[InlineKeyboardButton(f"{moves['dodge_move']['name']}",callback_data=f'pvpmu_dodge_{user_2_id}'),InlineKeyboardButton(f"SWAP",callback_data=f'pvpmuu_swap_{user_2_id}'),InlineKeyboardButton(f"DRAW",callback_data=f'pvpmuu_draw_{user_1_id}_{user_2_id}')],[InlineKeyboardButton(f"WITHDRAW",callback_data=f'pvpmu_withdraw_{user_1_id}_{user_2_id}')]]
                    text2=""
                    text2+=f"*AS *[PLAYER 1](tg://user?id={users['user_1_id']})* have already choosen the Attack\nNOW *[PLAYER 2](tg://user?id={users['user_2_id']})* choose the attack you would like to do*"
                    text2+=f"\n\n[PLAYER 2](tg://user?id={users['user_2_id']}) :  *{user_2_id_team[f'team_player_{user_2_player}']['name']} [ {user_2_id_team[f'team_player_{user_2_player}']['element']} ]*\n`{user_2_id_team[f'team_player_{user_2_player}']['name']} HP : `*{user_2_id_team[f'team_player_{user_2_player}']['hp']}*\n\n[PLAYER 1](tg://user?id={users['user_1_id']}) :  *{user_1_id_team[f'team_player_{user_1_player}']['name']} [ {user_1_id_team[f'team_player_{user_1_player}']['element']} ]*\n`{user_1_id_team[f'team_player_{user_1_player}']['name']} HP : `*{user_1_id_team[f'team_player_{user_1_player}']['hp']}*"
                    text2+=f"\n\n[PLAYER 2](tg://user?id={users['user_2_id']}) *choose the move*"
                    message=query.message.edit_text(text2,reply_markup=InlineKeyboardMarkup(keyboard),parse_mode=ParseMode.MARKDOWN)
                    message_id = message.message_id
                    cd[message_id] = {}
                    cd[message_id]['users']=users
                    cd[message_id]['teams']=user_teams
                    cd[message_id]['passive']=user_passive
                    cd[message_id]['move_done']=move
                    cd[message_id]['pvp_player_no']=player_no 
            else:
                rool_aa-=1
        if rool_aa == 0 :
            passer_pvp(update,context)
            return
    elif query.data.split("_")[1] == "sapru":
        if user.id != int(query.data.split('_')[-1]):
            query.answer("NOT YOUR COMMAND NIGGA",show_alert=True)
            return
        move[f"user_{int(query.data.split('_')[-1])}_move"]=f"swap_{query.data.split('_')[-2]}"
        if query.data.split('_')[-2] == "back":
            move[f"user_{int(query.data.split('_')[-1])}_move"]=f""
            if user.id == user_1_id :
                keyboard=[[InlineKeyboardButton(f"{moves['normal_move']['name']}",callback_data=f'pvpmu_normal_{user_1_id}')],[InlineKeyboardButton(f"{moves['dodge_move']['name']}",callback_data=f'pvpmu_dodge_{user_1_id}'),InlineKeyboardButton(f"SWAP",callback_data=f'pvpmuu_swap_{user_1_id}'),InlineKeyboardButton(f"DRA",callback_data=f'pvpmuu_draw_{user_1_id}_{user_2_id}')],[InlineKeyboardButton(f"WITHDRAW",callback_data=f'pvpmu_withdraw_{user_1_id}_{user_2_id}')]]
                text1=f"\n*Waiting for *[PLAYER 1](tg://user?id={users['user_1_id']}) *move*"
                text1+=f"\n\n[PLAYER 1](tg://user?id={users['user_1_id']}) :  *{user_1_id_team[f'team_player_{user_1_player}']['name']} [ {user_1_id_team[f'team_player_{user_1_player}']['element']} ]*\n`{user_1_id_team[f'team_player_{user_1_player}']['name']} HP : `*{user_1_id_team[f'team_player_{user_1_player}']['hp']}*\n\n[PLAYER 2](tg://user?id={users['user_2_id']}) :  *{user_2_id_team[f'team_player_{user_2_player}']['name']} [ {user_2_id_team[f'team_player_{user_2_player}']['element']} ]*\n`{user_2_id_team[f'team_player_{user_2_player}']['name']} HP : `*{user_2_id_team[f'team_player_{user_2_player}']['hp']}*"
                text1+=f"\n\n[PLAYER 1](tg://user?id={users['user_1_id']}) *choose the move*"
                message=query.message.edit_text(text1,reply_markup=InlineKeyboardMarkup(keyboard),parse_mode=ParseMode.MARKDOWN)
                message_id = message.message_id
                cd[message_id] = {}
                cd[message_id]['users']=users
                cd[message_id]['teams']=user_teams
                cd[message_id]['passive']=user_passive
                cd[message_id]['move_done']=move
                cd[message_id]['pvp_player_no']=player_no
                return
            if user.id == user_2_id :
                keyboard=[[InlineKeyboardButton(f"{moves['normal_move']['name']}",callback_data=f'pvpmu_normal_{user_2_id}')],[InlineKeyboardButton(f"{moves['dodge_move']['name']}",callback_data=f'pvpmu_dodge_{user_2_id}'),InlineKeyboardButton(f"SWAP",callback_data=f'pvpmuu_swap_{user_2_id}'),InlineKeyboardButton(f"DRAW",callback_data=f'pvpmuu_draw_{user_1_id}_{user_2_id}')],[InlineKeyboardButton(f"WITHDRAW",callback_data=f'pvpmu_withdraw_{user_1_id}_{user_2_id}')]]
                text2=f"\n*Waiting for *[PLAYER 2](tg://user?id={users['user_2_id']}) *move*"
                text2+=f"\n\n[PLAYER 2](tg://user?id={users['user_2_id']}) :  *{user_2_id_team[f'team_player_{user_2_player}']['name']} [ {user_2_id_team[f'team_player_{user_2_player}']['element']} ]*\n`{user_2_id_team[f'team_player_{user_2_player}']['name']} HP : `*{user_2_id_team[f'team_player_{user_2_player}']['hp']}*\n\n[PLAYER 1](tg://user?id={users['user_1_id']}) :  *{user_1_id_team[f'team_player_{user_1_player}']['name']} [ {user_1_id_team[f'team_player_{user_1_player}']['element']} ]*\n`{user_1_id_team[f'team_player_{user_1_player}']['name']} HP : `*{user_1_id_team[f'team_player_{user_1_player}']['hp']}*"
                text2+=f"\n\n[PLAYER 2](tg://user?id={users['user_2_id']}) *choose the move*"
                message=query.message.edit_text(text2,reply_markup=InlineKeyboardMarkup(keyboard),parse_mode=ParseMode.MARKDOWN)
                message_id = message.message_id
                cd[message_id] = {}
                cd[message_id]['users']=users
                cd[message_id]['teams']=user_teams
                cd[message_id]['passive']=user_passive
                cd[message_id]['move_done']=move
                cd[message_id]['pvp_player_no']=player_no
                return
        rool_aa=2
        for i in range(2):
            if move[f"user_{users[f'user_{i+1}_id']}_move"] == "":
                if i+1 == 1 :
                    user_1_id_team = user_teams['user_1_team']
                    user_2_id_team = user_teams['user_2_team']
                    moves=charamoves(user_1_id_team[f"team_player_{player_no['user_1s_id']}"])
                    keyboard=[[InlineKeyboardButton(f"{moves['normal_move']['name']}",callback_data=f'pvpmu_normal_{user_1_id}')],[InlineKeyboardButton(f"{moves['dodge_move']['name']}",callback_data=f'pvpmu_dodge_{user_1_id}'),InlineKeyboardButton(f"SWAP",callback_data=f'pvpmuu_swap_{user_1_id}'),InlineKeyboardButton(f"DRA",callback_data=f'pvpmuu_draw_{user_1_id}_{user_2_id}')],[InlineKeyboardButton(f"WITHDRAW",callback_data=f'pvpmu_withdraw_{user_1_id}_{user_2_id}')]]
                    text1=""
                    text1+=f"*AS *[PLAYER 2](tg://user?id={users['user_2_id']})* have already choosen the Attack\nNOW *[PLAYER 1](tg://user?id={users['user_1_id']})* choose the attack you would like to do*"
                    text1+=f"\n\n[PLAYER 1](tg://user?id={users['user_1_id']}) :  *{user_1_id_team[f'team_player_{user_1_player}']['name']} [ {user_1_id_team[f'team_player_{user_1_player}']['element']} ]*\n`{user_1_id_team[f'team_player_{user_1_player}']['name']} HP : `*{user_1_id_team[f'team_player_{user_1_player}']['hp']}*\n\n[PLAYER 2](tg://user?id={users['user_2_id']}) :  *{user_2_id_team[f'team_player_{user_2_player}']['name']} [ {user_2_id_team[f'team_player_{user_2_player}']['element']} ]*\n`{user_2_id_team[f'team_player_{user_2_player}']['name']} HP : `*{user_2_id_team[f'team_player_{user_2_player}']['hp']}*"
                    text1+=f"\n\n[PLAYER 1](tg://user?id={users['user_1_id']}) *choose the move*"
                    message=query.message.edit_text(text1,reply_markup=InlineKeyboardMarkup(keyboard),parse_mode=ParseMode.MARKDOWN)
                    message_id = message.message_id
                    cd[message_id] = {}
                    cd[message_id]['users']=users
                    cd[message_id]['teams']=user_teams
                    cd[message_id]['passive']=user_passive
                    cd[message_id]['move_done']=move
                    cd[message_id]['pvp_player_no']=player_no
                elif i+1 == 2 :
                    user_2_id_team = user_teams['user_2_team']
                    user_1_id_team = user_teams['user_1_team']
                    moves=charamoves(user_2_id_team[f"team_player_{1}"])
                    keyboard=[[InlineKeyboardButton(f"{moves['normal_move']['name']}",callback_data=f'pvpmu_normal_{user_2_id}')],[InlineKeyboardButton(f"{moves['dodge_move']['name']}",callback_data=f'pvpmu_dodge_{user_2_id}'),InlineKeyboardButton(f"SWAP",callback_data=f'pvpmuu_swap_{user_2_id}'),InlineKeyboardButton(f"DRAW",callback_data=f'pvpmuu_draw_{user_1_id}_{user_2_id}')],[InlineKeyboardButton(f"WITHDRAW",callback_data=f'pvpmu_withdraw_{user_1_id}_{user_2_id}')]]
                    text2=""
                    text2+=f"*AS *[PLAYER 1](tg://user?id={users['user_1_id']})* have already choosen the Attack\nNOW *[PLAYER 2](tg://user?id={users['user_2_id']})* choose the attack you would like to do*"
                    text2+=f"\n\n[PLAYER 2](tg://user?id={users['user_2_id']}) :  *{user_2_id_team[f'team_player_{user_2_player}']['name']} [ {user_2_id_team[f'team_player_{user_2_player}']['element']} ]*\n`{user_2_id_team[f'team_player_{user_2_player}']['name']} HP : `*{user_2_id_team[f'team_player_{user_2_player}']['hp']}*\n\n[PLAYER 1](tg://user?id={users['user_1_id']}) :  *{user_1_id_team[f'team_player_{user_1_player}']['name']} [ {user_1_id_team[f'team_player_{user_1_player}']['element']} ]*\n`{user_1_id_team[f'team_player_{user_1_player}']['name']} HP : `*{user_1_id_team[f'team_player_{user_1_player}']['hp']}*"
                    text2+=f"\n\n[PLAYER 2](tg://user?id={users['user_2_id']}) *choose the move*"
                    message=query.message.edit_text(text2,reply_markup=InlineKeyboardMarkup(keyboard),parse_mode=ParseMode.MARKDOWN)
                    message_id = message.message_id
                    cd[message_id] = {}
                    cd[message_id]['users']=users
                    cd[message_id]['teams']=user_teams
                    cd[message_id]['passive']=user_passive
                    cd[message_id]['move_done']=move
                    cd[message_id]['pvp_player_no']=player_no 
            else:
                rool_aa-=1
        if rool_aa == 0 :
            passer_pvp(update,context)
            return
    elif query.data.split("_")[1] == "withdraw":
        if user.id == user_1_id or user.id == user_2_id :
            if user_1_id in insiders :
                insiders.remove(user_1_id)
            if user_2_id in insiders :
                insiders.remove(user_2_id)
            query.message.edit_text("*Withdraw Done*",parse_mode=ParseMode.MARKDOWN)
            return
        else:
            query.answer("OUTSIDER NIGGA",show_alert=True)
            return

def passer_pvp(update,context):
    global insiders
    if maintenance_mode == "ON":
        if update.effective_user.id not in admins_id:
            try:
                update.callback_query.message.edit_text("*BOT UNDER MAINTENANCE*",parse_mode=ParseMode.MARKDOWN)
            except:
                update.callback_query.message.edit_caption(caption="*BOT UNDER MAINTENANCE*",parse_mode=ParseMode.MARKDOWN)
            return
    user=update.callback_query.from_user
    query=update.callback_query
    cd=context.chat_data
    message_id=query.message.message_id
    user_passive=cd[message_id]['passive']
    user_teams=cd[message_id]['teams']
    users=cd[message_id]['users']
    move=cd[message_id]['move_done']
    player_no=cd[message_id]['pvp_player_no']
    user_1_player=player_no['user_1s_id']
    user_2_player=player_no['user_2s_id']
    user_1_id = users['user_1_id']
    text=""
    user_2_id = users['user_2_id']
    char_of_1=user_teams['user_1_team']
    char_of_2=user_teams['user_2_team']
    def_of_1=char_of_1[f'team_player_{user_1_player}']['def']
    def_of_2=char_of_2[f'team_player_{user_2_player}']['def']
    char_crit=[True,False]
    char1_possible=random.choices(char_crit,weights=(char_of_1[f'team_player_{user_1_player}']['crit_rate'],100-char_of_1[f'team_player_{user_1_player}']['crit_rate']),k=1)
    char2_possible=random.choices(char_crit,weights=(char_of_2[f'team_player_{user_2_player}']['crit_rate'],100-char_of_2[f'team_player_{user_2_player}']['crit_rate']),k=1)
    if char1_possible[0]==True:
        text+=f"\n{(char_of_1[f'team_player_{user_1_player}']['name']).upper()} HIT CRIT"
        char_1_dmg=round((char_of_1[f'team_player_{user_1_player}']['atk'])+((+char_of_1[f'team_player_{user_1_player}']['atk'])*char_of_1[f'team_player_{user_1_player}']['crit_dmg']/100))
    else:
        char_1_dmg=char_of_1[f'team_player_{user_1_player}']['atk']
        text+=""
    if char2_possible[0]==True:
        text+=f"\n{(char_of_2[f'team_player_{user_2_player}']['name']).upper()} HIT CRIT"
        char_2_dmg=round((char_of_2[f'team_player_{user_2_player}']['atk'])+((+char_of_2[f'team_player_{user_2_player}']['atk'])*char_of_2[f'team_player_{user_2_player}']['crit_dmg']/100))
    else:
        char_2_dmg=char_of_2[f'team_player_{user_2_player}']['atk']
        text+=""
    if move[f"user_{user_1_id}_move"]=="normal" and move[f"user_{user_2_id}_move"]=="normal":
        player_gota_1=char_of_1[f'team_player_{user_1_player}']
        player_gota_2=char_of_2[f'team_player_{user_2_player}']
        if char_of_1[f'team_player_{user_1_player}']['speed'] > char_of_2[f'team_player_{user_2_player}']['speed']:
            char_of_2[f'team_player_{user_2_player}']['hp']-=char_1_dmg
            text+=f"*\n{char_of_1[f'team_player_{user_1_player}']['name']} Dealt {char_1_dmg} to {char_of_2[f'team_player_{user_2_player}']['name']}*"
            if char_of_2[f'team_player_{user_2_player}']['hp']<1:
                query.message.edit_text(text+f"\n\n{char_of_2[f'team_player_{user_2_player}']['name']} is now dead\n\nAND [PLAYER 2](tg://user?id={user_2_id}) is defeated by [PLAYER 1](tg://user?id={user_1_id})",parse_mode=ParseMode.MARKDOWN)
                if user_1_id in insiders :
                    insiders.remove(user_1_id)
                if user_2_id in insiders :
                    insiders.remove(user_2_id)
                return
            else:
                char_of_1[f'team_player_{user_1_player}']['hp']-=char_2_dmg
                if char_of_1[f'team_player_{user_1_player}']['hp']<1:
                    query.message.edit_text(text+f"\n\n{char_of_1[f'team_player_{user_1_player}']['name']} is now dead\n\nAND [PLAYER 1](tg://user?id={user_1_id}) is defeated by [PLAYER 2](tg://user?id={user_2_id})",parse_mode=ParseMode.MARKDOWN)
                    if user_1_id in insiders :
                        insiders.remove(user_1_id)
                    if user_2_id in insiders :
                        insiders.remove(user_2_id)
                    return
                text+=f"*\n{char_of_2[f'team_player_{user_2_player}']['name']} Dealt {char_2_dmg} to {char_of_1[f'team_player_{user_1_player}']['name']}*"
                moves=charamoves(char_of_1[f"team_player_{user_1_player}"])
                text1=f"\n\n[PLAYER 1](tg://user?id={users['user_1_id']}) :  *{char_of_1[f'team_player_{user_1_player}']['name']} [ {char_of_1[f'team_player_{user_1_player}']['element']} ]*\n`{char_of_1[f'team_player_{user_1_player}']['name']} HP : `*{char_of_1[f'team_player_{user_1_player}']['hp']}*\n\n[PLAYER 2](tg://user?id={users['user_2_id']}) :  *{char_of_2[f'team_player_{user_2_player}']['name']} [ {char_of_2[f'team_player_{user_2_player}']['element']} ]*\n`{char_of_2[f'team_player_{user_2_player}']['name']} HP : `*{char_of_2[f'team_player_{user_2_player}']['hp']}*"
                keyboard=[[InlineKeyboardButton(f"{moves['normal_move']['name']}",callback_data=f'pvpmu_normal_{user_1_id}')],[InlineKeyboardButton(f"{moves['dodge_move']['name']}",callback_data=f'pvpmu_dodge_{user_1_id}'),InlineKeyboardButton(f"SWAP",callback_data=f'pvpmuu_swap_{user_1_id}'),InlineKeyboardButton(f"DRA",callback_data=f'pvpmuu_draw_{user_1_id}_{user_2_id}')],[InlineKeyboardButton(f"WITHDRAW",callback_data=f'pvpmu_withdraw_{user_1_id}_{user_2_id}')]]
                message=query.message.edit_text(text+text1+f"\n\n[PLAYER 1](tg://user?id={users['user_1_id']}) *choose the move*",reply_markup=InlineKeyboardMarkup(keyboard),parse_mode=ParseMode.MARKDOWN)
                message_id = message.message_id
                cd[message_id] = {}
                cd[message_id]['users']={"user_1_id":user_1_id,"user_2_id":user_2_id}
                cd[message_id]['teams']={"user_1_team":char_of_1,"user_2_team":char_of_2}
                cd[message_id]['passive']=user_passive
                cd[message_id]['move_done']={f"user_{user_1_id}_move":"",f"user_{user_2_id}_move":""}
                cd[message_id]['pvp_player_no']={"user_1s_id":user_1_player,"user_2s_id":user_2_player}
                return
        else:
            char_of_1[f'team_player_{user_1_player}']['hp']-=char_2_dmg
            text+=f"*\n{char_of_2[f'team_player_{user_2_player}']['name']} Dealt {char_2_dmg} to {char_of_1[f'team_player_{user_1_player}']['name']}*"
            if char_of_1[f'team_player_{user_1_player}']['hp']<1:
                query.message.edit_text(text+f"\n\n{char_of_1[f'team_player_{user_1_player}']['name']} is now dead\n\nAND [PLAYER 1](tg://user?id={user_1_id}) is defeated by [PLAYER 2](tg://user?id={user_2_id})",parse_mode=ParseMode.MARKDOWN)
                if user_1_id in insiders :
                    insiders.remove(user_1_id)
                if user_2_id in insiders :
                    insiders.remove(user_2_id)
                return
            else:
                char_of_2[f'team_player_{user_2_player}']['hp']-=char_1_dmg
                if char_of_2[f'team_player_{user_2_player}']['hp']<1:
                    query.message.edit_text(text+f"\n\n{char_of_2[f'team_player_{user_2_player}']['name']} is now dead\n\nAND [PLAYER 2](tg://user?id={user_2_id}) is defeated by [PLAYER 1](tg://user?id={user_1_id})",parse_mode=ParseMode.MARKDOWN)
                    if user_1_id in insiders :
                        insiders.remove(user_1_id)
                    if user_2_id in insiders :
                        insiders.remove(user_2_id)
                    return
                text+=f"*\n{char_of_1[f'team_player_{user_1_player}']['name']} Dealt {char_1_dmg} to {char_of_2[f'team_player_{user_2_player}']['name']}*"
                moves=charamoves(char_of_2[f"team_player_{user_2_player}"])
                text2=f"\n\n[PLAYER 2](tg://user?id={users['user_2_id']}) :  *{char_of_2[f'team_player_{user_2_player}']['name']} [ {char_of_2[f'team_player_{user_2_player}']['element']} ]*\n`{char_of_2[f'team_player_{user_2_player}']['name']} HP : `*{char_of_2[f'team_player_{user_2_player}']['hp']}*\n\n[PLAYER 1](tg://user?id={users['user_1_id']}) :  *{char_of_1[f'team_player_{user_1_player}']['name']} [ {char_of_1[f'team_player_{user_1_player}']['element']} ]*\n`{char_of_1[f'team_player_{user_1_player}']['name']} HP : `*{char_of_1[f'team_player_{user_1_player}']['hp']}*"
                keyboard=[[InlineKeyboardButton(f"{moves['normal_move']['name']}",callback_data=f'pvpmu_normal_{user_2_id}')],[InlineKeyboardButton(f"{moves['dodge_move']['name']}",callback_data=f'pvpmu_dodge_{user_2_id}'),InlineKeyboardButton(f"SWAP",callback_data=f'pvpmuu_swap_{user_2_id}'),InlineKeyboardButton(f"DRA",callback_data=f'pvpmuu_draw_{user_2_id}_{user_1_id}')],[InlineKeyboardButton(f"WITHDRAW",callback_data=f'pvpmu_withdraw_{user_2_id}_{user_1_id}')]]
                message=query.message.edit_text(text+text2+f"\n\n[PLAYER 2](tg://user?id={users['user_2_id']}) *choose the move*",reply_markup=InlineKeyboardMarkup(keyboard),parse_mode=ParseMode.MARKDOWN)
                message_id = message.message_id
                cd[message_id] = {}
                cd[message_id]['users']={"user_1_id":user_1_id,"user_2_id":user_2_id}
                cd[message_id]['teams']={"user_1_team":char_of_1,"user_2_team":char_of_2}
                cd[message_id]['passive']=user_passive
                cd[message_id]['move_done']={f"user_{user_1_id}_move":"",f"user_{user_2_id}_move":""}
                cd[message_id]['pvp_player_no']={"user_1s_id":user_1_player,"user_2s_id":user_2_player}
                return
    elif move[f"user_{user_1_id}_move"]=="dodge" and move[f"user_{user_2_id}_move"]=="dodge":
        text1=f"*BOTH USED DODGE\nAttack dismissed*"
        moves=charamoves(char_of_2[f"team_player_{user_2_player}"])
        text2=f"\n\n[PLAYER 2](tg://user?id={users['user_2_id']}) :  *{char_of_2[f'team_player_{user_2_player}']['name']} [ {char_of_2[f'team_player_{user_2_player}']['element']} ]*\n`{char_of_2[f'team_player_{user_2_player}']['name']} HP : `*{char_of_2[f'team_player_{user_2_player}']['hp']}*\n\n[PLAYER 1](tg://user?id={users['user_1_id']}) :  *{char_of_1[f'team_player_{user_1_player}']['name']} [ {char_of_1[f'team_player_{user_1_player}']['element']} ]*\n`{char_of_1[f'team_player_{user_1_player}']['name']} HP : `*{char_of_1[f'team_player_{user_1_player}']['hp']}*"
        keyboard=[[InlineKeyboardButton(f"{moves['normal_move']['name']}",callback_data=f'pvpmu_normal_{user_2_id}')],[InlineKeyboardButton(f"{moves['dodge_move']['name']}",callback_data=f'pvpmu_dodge_{user_2_id}'),InlineKeyboardButton(f"SWAP",callback_data=f'pvpmuu_swap_{user_2_id}'),InlineKeyboardButton(f"DRAW",callback_data=f'pvpmuu_draw_{user_2_id}_{user_1_id}')],[InlineKeyboardButton(f"WITHDRAW",callback_data=f'pvpmu_withdraw_{user_2_id}_{user_1_id}')]]
        message=query.message.edit_text(text1+text2+f"\n\n[PLAYER 2](tg://user?id={users['user_2_id']}) *choose the move*",reply_markup=InlineKeyboardMarkup(keyboard),parse_mode=ParseMode.MARKDOWN)
        message_id = message.message_id
        cd[message_id] = {}
        cd[message_id]['users']={"user_1_id":user_1_id,"user_2_id":user_2_id}
        cd[message_id]['teams']={"user_1_team":char_of_1,"user_2_team":char_of_2}
        cd[message_id]['passive']=user_passive
        cd[message_id]['move_done']={f"user_{user_1_id}_move":"",f"user_{user_2_id}_move":""}
        cd[message_id]['pvp_player_no']={"user_1s_id":user_1_player,"user_2s_id":user_2_player}
        return
    elif move[f"user_{user_1_id}_move"]=="dodge" and move[f"user_{user_2_id}_move"]=="normal" :
        possibility=(char_of_1[f'team_player_{user_1_player}']['speed'])*0.1
        dodge=[True,False]
        dodged_not=random.choices(dodge,weights=(possibility,100-possibility),k=1)
        if dodged_not[0] == True:
            recoil_dmg=round(1.5*char_2_dmg)
            char_of_2[f'team_player_{user_2_player}']['hp']-=recoil_dmg
            if char_of_2[f'team_player_{user_2_player}']['hp']<1:
                query.message.edit_text(text+f"\n\n{char_of_2[f'team_player_{user_2_player}']['name']} is now dead\n\nAND [PLAYER 2](tg://user?id={user_2_id}) is defeated by [PLAYER 1](tg://user?id={user_1_id})",parse_mode=ParseMode.MARKDOWN)
                if user_1_id in insiders :
                    insiders.remove(user_1_id)
                if user_2_id in insiders :
                    insiders.remove(user_2_id)
                return
            else:
                moves=charamoves(char_of_1[f"team_player_{user_1_player}"])
                text1=f"\n\n[PLAYER 1](tg://user?id={users['user_1_id']}) :  *{char_of_1[f'team_player_{user_1_player}']['name']} [ {char_of_1[f'team_player_{user_1_player}']['element']} ]*\n`{char_of_1[f'team_player_{user_1_player}']['name']} HP : `*{char_of_1[f'team_player_{user_1_player}']['hp']}*\n\n[PLAYER 2](tg://user?id={users['user_2_id']}) :  *{char_of_2[f'team_player_{user_2_player}']['name']} [ {char_of_2[f'team_player_{user_2_player}']['element']} ]*\n`{char_of_2[f'team_player_{user_2_player}']['name']} HP : `*{char_of_2[f'team_player_{user_2_player}']['hp']}*"
                keyboard=[[InlineKeyboardButton(f"{moves['normal_move']['name']}",callback_data=f'pvpmu_normal_{user_1_id}')],[InlineKeyboardButton(f"{moves['dodge_move']['name']}",callback_data=f'pvpmu_dodge_{user_1_id}'),InlineKeyboardButton(f"SWAP",callback_data=f'pvpmuu_swap_{user_1_id}'),InlineKeyboardButton(f"DRA",callback_data=f'pvpmuu_draw_{user_1_id}_{user_2_id}')],[InlineKeyboardButton(f"WITHDRAW",callback_data=f'pvpmu_withdraw_{user_1_id}_{user_2_id}')]]
                message=query.message.edit_text(text+text1+f"\n\n[PLAYER 1](tg://user?id={users['user_1_id']}) *choose the move*",reply_markup=InlineKeyboardMarkup(keyboard),parse_mode=ParseMode.MARKDOWN)
                message_id = message.message_id
                cd[message_id] = {}
                cd[message_id]['users']={"user_1_id":user_1_id,"user_2_id":user_2_id}
                cd[message_id]['teams']={"user_1_team":char_of_1,"user_2_team":char_of_2}
                cd[message_id]['passive']=user_passive
                cd[message_id]['move_done']={f"user_{user_1_id}_move":"",f"user_{user_2_id}_move":""}
                cd[message_id]['pvp_player_no']={"user_1s_id":user_1_player,"user_2s_id":user_2_player}
                return
        else:
            char_of_1[f'team_player_{user_1_player}']['hp']-=char_2_dmg
            text+=f"*\n{char_of_1[f'team_player_{user_1_player}']['name']} Tried to Dodge {char_of_2[f'team_player_{user_2_player}']['name']} but Failed\nAND got Hit by {char_of_2[f'team_player_{user_2_player}']['name']} Attack*"
            if char_of_1[f'team_player_{user_1_player}']['hp']<1:
                query.message.edit_text(text+f"\n\n{char_of_1[f'team_player_{user_1_player}']['name']} is now dead\n\nAND [PLAYER 1](tg://user?id={user_1_id}) is defeated by [PLAYER 2](tg://user?id={user_2_id})",parse_mode=ParseMode.MARKDOWN)
                if user_1_id in insiders :
                    insiders.remove(user_1_id)
                if user_2_id in insiders :
                    insiders.remove(user_2_id)
                return
            else:
                moves=charamoves(char_of_1[f"team_player_{user_1_player}"])
                text1=f"\n\n[PLAYER 1](tg://user?id={users['user_1_id']}) :  *{char_of_1[f'team_player_{user_1_player}']['name']} [ {char_of_1[f'team_player_{user_1_player}']['element']} ]*\n`{char_of_1[f'team_player_{user_1_player}']['name']} HP : `*{char_of_1[f'team_player_{user_1_player}']['hp']}*\n\n[PLAYER 2](tg://user?id={users['user_2_id']}) :  *{char_of_2[f'team_player_{user_2_player}']['name']} [ {char_of_2[f'team_player_{user_2_player}']['element']} ]*\n`{char_of_2[f'team_player_{user_2_player}']['name']} HP : `*{char_of_2[f'team_player_{user_2_player}']['hp']}*"
                keyboard=[[InlineKeyboardButton(f"{moves['normal_move']['name']}",callback_data=f'pvpmu_normal_{user_1_id}')],[InlineKeyboardButton(f"{moves['dodge_move']['name']}",callback_data=f'pvpmu_dodge_{user_1_id}'),InlineKeyboardButton(f"SWAP",callback_data=f'pvpmuu_swap_{user_1_id}'),InlineKeyboardButton(f"DRA",callback_data=f'pvpmuu_draw_{user_1_id}_{user_2_id}')],[InlineKeyboardButton(f"WITHDRAW",callback_data=f'pvpmu_withdraw_{user_1_id}_{user_2_id}')]]
                message=query.message.edit_text(text+text1+f"\n\n[PLAYER 1](tg://user?id={users['user_1_id']}) *choose the move*",reply_markup=InlineKeyboardMarkup(keyboard),parse_mode=ParseMode.MARKDOWN)
                message_id = message.message_id
                cd[message_id] = {}
                cd[message_id]['users']={"user_1_id":user_1_id,"user_2_id":user_2_id}
                cd[message_id]['teams']={"user_1_team":char_of_1,"user_2_team":char_of_2}
                cd[message_id]['passive']=user_passive
                cd[message_id]['move_done']={f"user_{user_1_id}_move":"",f"user_{user_2_id}_move":""}
                cd[message_id]['pvp_player_no']={"user_1s_id":user_1_player,"user_2s_id":user_2_player}
                return
    elif move[f"user_{user_1_id}_move"]=="normal" and move[f"user_{user_2_id}_move"]=="dodge" :
        possibility=(char_of_2[f'team_player_{user_2_player}']['speed'])*0.1
        dodge=[True,False]
        dodged_not=random.choices(dodge,weights=(possibility,100-possibility),k=1)
        if dodged_not[0] == True:
            recoil_dmg=round(1.5*char_1_dmg)
            char_of_1[f'team_player_{user_1_player}']['hp']-=recoil_dmg
            text+=f"*\n{char_of_2[f'team_player_{user_2_player}']['name']} dodged {char_of_1[f'team_player_{user_1_player}']['name']} Attack And\nThe {char_of_1[f'team_player_{user_1_player}']['name']} got hit by {recoil_dmg} DMG*"
            if char_of_1[f'team_player_{user_1_player}']['hp']<1:
                query.message.edit_text(text+f"\n\n{char_of_1[f'team_player_{user_1_player}']['name']} is now dead\n\nAND [PLAYER 1](tg://user?id={user_1_id}) is defeated by [PLAYER 2](tg://user?id={user_2_id})",parse_mode=ParseMode.MARKDOWN)
                if user_1_id in insiders :
                    insiders.remove(user_1_id)
                if user_2_id in insiders :
                    insiders.remove(user_2_id)
                return
            else:
                moves=charamoves(char_of_1[f"team_player_{user_1_player}"])
                text1=f"\n\n[PLAYER 1](tg://user?id={users['user_1_id']}) :  *{char_of_1[f'team_player_{user_1_player}']['name']} [ {char_of_1[f'team_player_{user_1_player}']['element']} ]*\n`{char_of_1[f'team_player_{user_1_player}']['name']} HP : `*{char_of_1[f'team_player_{user_1_player}']['hp']}*\n\n[PLAYER 2](tg://user?id={users['user_2_id']}) :  *{char_of_2[f'team_player_{user_2_player}']['name']} [ {char_of_2[f'team_player_{user_2_player}']['element']} ]*\n`{char_of_2[f'team_player_{user_2_player}']['name']} HP : `*{char_of_2[f'team_player_{user_2_player}']['hp']}*"
                keyboard=[[InlineKeyboardButton(f"{moves['normal_move']['name']}",callback_data=f'pvpmu_normal_{user_1_id}')],[InlineKeyboardButton(f"{moves['dodge_move']['name']}",callback_data=f'pvpmu_dodge_{user_1_id}'),InlineKeyboardButton(f"SWAP",callback_data=f'pvpmuu_swap_{user_1_id}'),InlineKeyboardButton(f"DRA",callback_data=f'pvpmuu_draw_{user_1_id}_{user_2_id}')],[InlineKeyboardButton(f"WITHDRAW",callback_data=f'pvpmu_withdraw_{user_1_id}_{user_2_id}')]]
                message=query.message.edit_text(text+text1+f"\n\n[PLAYER 1](tg://user?id={users['user_1_id']}) *choose the move*",reply_markup=InlineKeyboardMarkup(keyboard),parse_mode=ParseMode.MARKDOWN)
                message_id = message.message_id
                cd[message_id] = {}
                cd[message_id]['users']={"user_1_id":user_1_id,"user_2_id":user_2_id}
                cd[message_id]['teams']={"user_1_team":char_of_1,"user_2_team":char_of_2}
                cd[message_id]['passive']=user_passive
                cd[message_id]['move_done']={f"user_{user_1_id}_move":"",f"user_{user_2_id}_move":""}
                cd[message_id]['pvp_player_no']={"user_1s_id":user_1_player,"user_2s_id":user_2_player}
                return
        else:
            char_of_2[f'team_player_{user_1_player}']['hp']-=char_1_dmg
            if char_of_2[f'team_player_{user_2_player}']['hp']<1:
                query.message.edit_text(text+f"\n\n{char_of_2[f'team_player_{user_2_player}']['name']} is now dead\n\nAND [PLAYER 2](tg://user?id={user_2_id}) is defeated by [PLAYER 1](tg://user?id={user_1_id})",parse_mode=ParseMode.MARKDOWN)
                if user_1_id in insiders :
                    insiders.remove(user_1_id)
                if user_2_id in insiders :
                    insiders.remove(user_2_id)
                return
            else:
                text+=f"*\n{char_of_2[f'team_player_{user_2_player}']['name']} Tried to Dodge {char_of_1[f'team_player_{user_1_player}']['name']} but Failed\nAND got Hit by {char_of_1[f'team_player_{user_1_player}']['name']} Attack*"
                moves=charamoves(char_of_1[f"team_player_{user_1_player}"])
                text1=f"\n\n[PLAYER 1](tg://user?id={users['user_1_id']}) :  *{char_of_1[f'team_player_{user_1_player}']['name']} [ {char_of_1[f'team_player_{user_1_player}']['element']} ]*\n`{char_of_1[f'team_player_{user_1_player}']['name']} HP : `*{char_of_1[f'team_player_{user_1_player}']['hp']}*\n\n[PLAYER 2](tg://user?id={users['user_2_id']}) :  *{char_of_2[f'team_player_{user_2_player}']['name']} [ {char_of_2[f'team_player_{user_2_player}']['element']} ]*\n`{char_of_2[f'team_player_{user_2_player}']['name']} HP : `*{char_of_2[f'team_player_{user_2_player}']['hp']}*"
                keyboard=[[InlineKeyboardButton(f"{moves['normal_move']['name']}",callback_data=f'pvpmu_normal_{user_1_id}')],[InlineKeyboardButton(f"{moves['dodge_move']['name']}",callback_data=f'pvpmu_dodge_{user_1_id}'),InlineKeyboardButton(f"SWAP",callback_data=f'pvpmuu_swap_{user_1_id}'),InlineKeyboardButton(f"DRAW",callback_data=f'pvpmuu_draw_{user_1_id}_{user_2_id}')],[InlineKeyboardButton(f"WITHDRAW",callback_data=f'pvpmu_withdraw_{user_1_id}_{user_2_id}')]]
                message=query.message.edit_text(text+text1+f"\n\n[PLAYER 1](tg://user?id={users['user_1_id']}) *choose the move*",reply_markup=InlineKeyboardMarkup(keyboard),parse_mode=ParseMode.MARKDOWN)
                message_id = message.message_id
                cd[message_id] = {}
                cd[message_id]['users']={"user_1_id":user_1_id,"user_2_id":user_2_id}
                cd[message_id]['teams']={"user_1_team":char_of_1,"user_2_team":char_of_2}
                cd[message_id]['passive']=user_passive
                cd[message_id]['move_done']={f"user_{user_1_id}_move":"",f"user_{user_2_id}_move":""}
                cd[message_id]['pvp_player_no']={"user_1s_id":user_1_player,"user_2s_id":user_2_player}
                return
    elif move[f"user_{user_1_id}_move"].split("_")[0]=="swap" and move[f"user_{user_2_id}_move"].split("_")[0]=="swap" :
        new_player_1=int(move[f"user_{user_1_id}_move"].split("_")[1])
        new_player_2=int(move[f"user_{user_2_id}_move"].split("_")[1])
        text1=f"[PLAYER 1](tg://user?id={users['user_1_id']})* swapped {char_of_1[f'team_player_{new_player_1}']['name']} with {char_of_1[f'team_player_{user_1_player}']['name']}*"
        text1+="*\nAND*"
        text1+=f"\n[PLAYER 2](tg://user?id={users['user_2_id']})* swapped {char_of_2[f'team_player_{new_player_2}']['name']} with {char_of_2[f'team_player_{user_2_player}']['name']}*"
        user_1_player=new_player_1
        user_2_player=new_player_2
        moves=charamoves(char_of_2[f"team_player_{user_2_player}"])
        text2=f"\n\n[PLAYER 2](tg://user?id={users['user_2_id']}) :  *{char_of_2[f'team_player_{user_2_player}']['name']} [ {char_of_2[f'team_player_{user_2_player}']['element']} ]*\n`{char_of_2[f'team_player_{user_2_player}']['name']} HP : `*{char_of_2[f'team_player_{user_2_player}']['hp']}*\n\n[PLAYER 1](tg://user?id={users['user_1_id']}) :  *{char_of_1[f'team_player_{user_1_player}']['name']} [ {char_of_1[f'team_player_{user_1_player}']['element']} ]*\n`{char_of_1[f'team_player_{user_1_player}']['name']} HP : `*{char_of_1[f'team_player_{user_1_player}']['hp']}*"
        keyboard=[[InlineKeyboardButton(f"{moves['normal_move']['name']}",callback_data=f'pvpmu_normal_{user_2_id}')],[InlineKeyboardButton(f"{moves['dodge_move']['name']}",callback_data=f'pvpmu_dodge_{user_2_id}'),InlineKeyboardButton(f"SWAP",callback_data=f'pvpmuu_swap_{user_2_id}'),InlineKeyboardButton(f"DRAW",callback_data=f'pvpmuu_draw_{user_2_id}_{user_1_id}')],[InlineKeyboardButton(f"WITHDRAW",callback_data=f'pvpmu_withdraw_{user_2_id}_{user_1_id}')]]
        message=query.message.edit_text(text1+text2+f"\n\n[PLAYER 2](tg://user?id={users['user_2_id']}) *choose the move*",reply_markup=InlineKeyboardMarkup(keyboard),parse_mode=ParseMode.MARKDOWN)
        message_id = message.message_id
        cd[message_id] = {}
        cd[message_id]['users']={"user_1_id":user_1_id,"user_2_id":user_2_id}
        cd[message_id]['teams']={"user_1_team":char_of_1,"user_2_team":char_of_2}
        cd[message_id]['passive']=user_passive
        cd[message_id]['move_done']={f"user_{user_1_id}_move":"",f"user_{user_2_id}_move":""}
        cd[message_id]['pvp_player_no']={"user_1s_id":user_1_player,"user_2s_id":user_2_player}
        return
    elif move[f"user_{user_1_id}_move"]=="normal" and move[f"user_{user_2_id}_move"].split("_")[0]=="swap" :
        new_player_2=int(move[f"user_{user_2_id}_move"].split("_")[1])
        text1=f"\n[PLAYER 2](tg://user?id={users['user_2_id']})* swapped {char_of_2[f'team_player_{new_player_2}']['name']} with {char_of_2[f'team_player_{user_2_player}']['name']}*"
        user_2_player=new_player_2
        text1+="*\nAND*"
        char_of_2[f'team_player_{user_2_player}']['hp']-=char_1_dmg
        if char_of_2[f'team_player_{user_2_player}']['hp'] < 1:
            query.message.edit_text(text+text1+f"\n\n{char_of_2[f'team_player_{user_2_player}']['name']} is now dead\n\nAND [PLAYER 2](tg://user?id={user_2_id}) is defeated by [PLAYER 1](tg://user?id={user_1_id})",parse_mode=ParseMode.MARKDOWN)
            if user_1_id in insiders :
                insiders.remove(user_1_id)
            if user_2_id in insiders :
                insiders.remove(user_2_id)
            return
        else:
            text1+=f"*\n{char_of_1[f'team_player_{user_1_player}']['name']} Dealt {char_1_dmg} to {char_of_2[f'team_player_{user_2_player}']['name']}*"
            text2=f"\n\n[PLAYER 2](tg://user?id={users['user_2_id']}) :  *{char_of_2[f'team_player_{user_2_player}']['name']} [ {char_of_2[f'team_player_{user_2_player}']['element']} ]*\n`{char_of_2[f'team_player_{user_2_player}']['name']} HP : `*{char_of_2[f'team_player_{user_2_player}']['hp']}*\n\n[PLAYER 1](tg://user?id={users['user_1_id']}) :  *{char_of_1[f'team_player_{user_1_player}']['name']} [ {char_of_1[f'team_player_{user_1_player}']['element']} ]*\n`{char_of_1[f'team_player_{user_1_player}']['name']} HP : `*{char_of_1[f'team_player_{user_1_player}']['hp']}*"
            moves=charamoves(char_of_1[f"team_player_{user_1_player}"])
            keyboard=[[InlineKeyboardButton(f"{moves['normal_move']['name']}",callback_data=f'pvpmu_normal_{user_1_id}')],[InlineKeyboardButton(f"{moves['dodge_move']['name']}",callback_data=f'pvpmu_dodge_{user_1_id}'),InlineKeyboardButton(f"SWAP",callback_data=f'pvpmuu_swap_{user_1_id}'),InlineKeyboardButton(f"DRAW",callback_data=f'pvpmuu_draw_{user_1_id}_{user_2_id}')],[InlineKeyboardButton(f"WITHDRAW",callback_data=f'pvpmu_withdraw_{user_1_id}_{user_2_id}')]]
            message=query.message.edit_text(text1+text2+f"\n\n[PLAYER 1](tg://user?id={users['user_1_id']}) *choose the move*",reply_markup=InlineKeyboardMarkup(keyboard),parse_mode=ParseMode.MARKDOWN)
            message_id = message.message_id
            cd[message_id] = {}
            cd[message_id]['users']={"user_1_id":user_1_id,"user_2_id":user_2_id}
            cd[message_id]['teams']={"user_1_team":char_of_1,"user_2_team":char_of_2}
            cd[message_id]['passive']=user_passive
            cd[message_id]['move_done']={f"user_{user_1_id}_move":"",f"user_{user_2_id}_move":""}
            cd[message_id]['pvp_player_no']={"user_1s_id":user_1_player,"user_2s_id":user_2_player}
            return
    elif move[f"user_{user_1_id}_move"].split("_")[0]=="swap" and move[f"user_{user_2_id}_move"]=="normal" :
        new_player_1=int(move[f"user_{user_1_id}_move"].split("_")[1])
        text1=f"[PLAYER 1](tg://user?id={users['user_1_id']})* swapped {char_of_1[f'team_player_{new_player_1}']['name']} with {char_of_1[f'team_player_{user_1_player}']['name']}*"
        user_1_player=new_player_1
        text1+="*\nAND*"
        char_of_1[f'team_player_{user_2_player}']['hp']-=char_2_dmg
        if char_of_1[f'team_player_{user_1_player}']['hp'] < 1:
            query.message.edit_text(text+f"\n\n{char_of_1[f'team_player_{user_1_player}']['name']} is now dead\n\nAND [PLAYER 1](tg://user?id={user_1_id}) is defeated by [PLAYER 2](tg://user?id={user_2_id})",parse_mode=ParseMode.MARKDOWN)
            if user_1_id in insiders :
                insiders.remove(user_1_id)
            if user_2_id in insiders :
                insiders.remove(user_2_id)
            return
        else:
            text1+=f"*\n{char_of_2[f'team_player_{user_2_player}']['name']} Dealt {char_2_dmg} to {char_of_1[f'team_player_{user_1_player}']['name']}*"
            text2=f"\n\n[PLAYER 2](tg://user?id={users['user_2_id']}) :  *{char_of_2[f'team_player_{user_2_player}']['name']} [ {char_of_2[f'team_player_{user_2_player}']['element']} ]*\n`{char_of_2[f'team_player_{user_2_player}']['name']} HP : `*{char_of_2[f'team_player_{user_2_player}']['hp']}*\n\n[PLAYER 1](tg://user?id={users['user_1_id']}) :  *{char_of_1[f'team_player_{user_1_player}']['name']} [ {char_of_1[f'team_player_{user_1_player}']['element']} ]*\n`{char_of_1[f'team_player_{user_1_player}']['name']} HP : `*{char_of_1[f'team_player_{user_1_player}']['hp']}*"
            moves=charamoves(char_of_2[f"team_player_{user_2_player}"])
            keyboard=[[InlineKeyboardButton(f"{moves['normal_move']['name']}",callback_data=f'pvpmu_normal_{user_2_id}')],[InlineKeyboardButton(f"{moves['dodge_move']['name']}",callback_data=f'pvpmu_dodge_{user_2_id}'),InlineKeyboardButton(f"SWAP",callback_data=f'pvpmuu_swap_{user_2_id}'),InlineKeyboardButton(f"DRAW",callback_data=f'pvpmuu_draw_{user_2_id}_{user_1_id}')],[InlineKeyboardButton(f"WITHDRAW",callback_data=f'pvpmu_withdraw_{user_2_id}_{user_1_id}')]]
            message=query.message.edit_text(text1+text2+f"\n\n[PLAYER 2](tg://user?id={users['user_2_id']}) *choose the move*",reply_markup=InlineKeyboardMarkup(keyboard),parse_mode=ParseMode.MARKDOWN)
            message_id = message.message_id
            cd[message_id] = {}
            cd[message_id]['users']={"user_1_id":user_1_id,"user_2_id":user_2_id}
            cd[message_id]['teams']={"user_1_team":char_of_1,"user_2_team":char_of_2}
            cd[message_id]['passive']=user_passive
            cd[message_id]['move_done']={f"user_{user_1_id}_move":"",f"user_{user_2_id}_move":""}
            cd[message_id]['pvp_player_no']={"user_1s_id":user_1_player,"user_2s_id":user_2_player}
            return
    elif move[f"user_{user_1_id}_move"]=="dodge" and move[f"user_{user_2_id}_move"].split("_")[0]=="swap" :
        new_player_2=int(move[f"user_{user_2_id}_move"].split("_")[1])
        text1=f"\n[PLAYER 2](tg://user?id={users['user_2_id']})* swapped {char_of_2[f'team_player_{new_player_2}']['name']} with {char_of_2[f'team_player_{user_2_player}']['name']}*"
        user_2_player=new_player_2
        text1+="*\nAND*"
        text1+=f"\n[PLAYER 1](tg://user?id={users['user_1_id']})'s {char_of_1[f'team_player_{user_1_player}']['name']}* tried to use Dodge but opponent swapped it's character*"
        moves=charamoves(char_of_2[f"team_player_{user_2_player}"])
        text2=f"\n\n[PLAYER 2](tg://user?id={users['user_2_id']}) :  *{char_of_2[f'team_player_{user_2_player}']['name']} [ {char_of_2[f'team_player_{user_2_player}']['element']} ]*\n`{char_of_2[f'team_player_{user_2_player}']['name']} HP : `*{char_of_2[f'team_player_{user_2_player}']['hp']}*\n\n[PLAYER 1](tg://user?id={users['user_1_id']}) :  *{char_of_1[f'team_player_{user_1_player}']['name']} [ {char_of_1[f'team_player_{user_1_player}']['element']} ]*\n`{char_of_1[f'team_player_{user_1_player}']['name']} HP : `*{char_of_1[f'team_player_{user_1_player}']['hp']}*"
        keyboard=[[InlineKeyboardButton(f"{moves['normal_move']['name']}",callback_data=f'pvpmu_normal_{user_2_id}')],[InlineKeyboardButton(f"{moves['dodge_move']['name']}",callback_data=f'pvpmu_dodge_{user_2_id}'),InlineKeyboardButton(f"SWAP",callback_data=f'pvpmuu_swap_{user_2_id}'),InlineKeyboardButton(f"DRAW",callback_data=f'pvpmuu_draw_{user_2_id}_{user_1_id}')],[InlineKeyboardButton(f"WITHDRAW",callback_data=f'pvpmu_withdraw_{user_2_id}_{user_1_id}')]]
        message=query.message.edit_text(text1+text2+f"\n\n[PLAYER 2](tg://user?id={users['user_2_id']}) *choose the move*",reply_markup=InlineKeyboardMarkup(keyboard),parse_mode=ParseMode.MARKDOWN)
        message_id = message.message_id
        cd[message_id] = {}
        cd[message_id]['users']={"user_1_id":user_1_id,"user_2_id":user_2_id}
        cd[message_id]['teams']={"user_1_team":char_of_1,"user_2_team":char_of_2}
        cd[message_id]['passive']=user_passive
        cd[message_id]['move_done']={f"user_{user_1_id}_move":"",f"user_{user_2_id}_move":""}
        cd[message_id]['pvp_player_no']={"user_1s_id":user_1_player,"user_2s_id":user_2_player}
        return
    elif move[f"user_{user_1_id}_move"].split("_")[0]=="swap" and move[f"user_{user_2_id}_move"]=="dodge" :
        new_player_1=int(move[f"user_{user_1_id}_move"].split("_")[1])
        text1=f"[PLAYER 1](tg://user?id={users['user_1_id']})* swapped {char_of_1[f'team_player_{new_player_1}']['name']} with {char_of_1[f'team_player_{user_1_player}']['name']}*"
        user_1_player=new_player_1
        text1+="*\nAND*"
        text1+=f"\n[PLAYER 2](tg://user?id={users['user_2_id']})'s {char_of_2[f'team_player_{user_2_player}']['name']}* tried to use Dodge but opponent swapped it's character*"
        moves=charamoves(char_of_2[f"team_player_{user_2_player}"])
        text2=f"\n\n[PLAYER 2](tg://user?id={users['user_2_id']}) :  *{char_of_2[f'team_player_{user_2_player}']['name']} [ {char_of_2[f'team_player_{user_2_player}']['element']} ]*\n`{char_of_2[f'team_player_{user_2_player}']['name']} HP : `*{char_of_2[f'team_player_{user_2_player}']['hp']}*\n\n[PLAYER 1](tg://user?id={users['user_1_id']}) :  *{char_of_1[f'team_player_{user_1_player}']['name']} [ {char_of_1[f'team_player_{user_1_player}']['element']} ]*\n`{char_of_1[f'team_player_{user_1_player}']['name']} HP : `*{char_of_1[f'team_player_{user_1_player}']['hp']}*"
        keyboard=[[InlineKeyboardButton(f"{moves['normal_move']['name']}",callback_data=f'pvpmu_normal_{user_2_id}')],[InlineKeyboardButton(f"{moves['dodge_move']['name']}",callback_data=f'pvpmu_dodge_{user_2_id}'),InlineKeyboardButton(f"SWAP",callback_data=f'pvpmuu_swap_{user_2_id}'),InlineKeyboardButton(f"DRAW",callback_data=f'pvpmuu_draw_{user_2_id}_{user_1_id}')],[InlineKeyboardButton(f"WITHDRAW",callback_data=f'pvpmu_withdraw_{user_2_id}_{user_1_id}')]]
        message=query.message.edit_text(text1+text2+f"\n\n[PLAYER 2](tg://user?id={users['user_2_id']}) *choose the move*",reply_markup=InlineKeyboardMarkup(keyboard),parse_mode=ParseMode.MARKDOWN)
        message_id = message.message_id
        cd[message_id] = {}
        cd[message_id]['users']={"user_1_id":user_1_id,"user_2_id":user_2_id}
        cd[message_id]['teams']={"user_1_team":char_of_1,"user_2_team":char_of_2}
        cd[message_id]['passive']=user_passive
        cd[message_id]['move_done']={f"user_{user_1_id}_move":"",f"user_{user_2_id}_move":""}
        cd[message_id]['pvp_player_no']={"user_1s_id":user_1_player,"user_2s_id":user_2_player}
        return
    query.message.edit_text("*4th pass working*",parse_mode=ParseMode.MARKDOWN)
    return

def pvp_swap_mou(update,context):
    global insiders
    if maintenance_mode == "ON":
        if update.effective_user.id not in admins_id:
            try:
                update.callback_query.message.edit_text("*BOT UNDER MAINTENANCE*",parse_mode=ParseMode.MARKDOWN)
            except:
                update.callback_query.message.edit_caption(caption="*BOT UNDER MAINTENANCE*",parse_mode=ParseMode.MARKDOWN)
            return
    user=update.callback_query.from_user
    query=update.callback_query
    cd=context.chat_data
    message_id=query.message.message_id
    user_passive=cd[message_id]['passive']
    user_teams=cd[message_id]['teams']
    users=cd[message_id]['users']
    move=cd[message_id]['move_done']
    player_no=cd[message_id]['pvp_player_no']
    user_1_player=player_no['user_1s_id']
    user_2_player=player_no['user_2s_id']
    user_1_id = users['user_1_id']
    user_2_id = users['user_2_id']
    char_of_1=user_teams['user_1_team']
    char_of_2=user_teams['user_2_team']
    text=""
    if user.id == user_1_id :
        if user.id != int(query.data.split('_')[2]):
            query.answer("PLAYER 1 TURN",show_alert=True)
            return
        keyboard1=[]
        for i in range (4):
            if char_of_1[f'team_player_{i+1}']['name']!='None':
                if char_of_1[f'team_player_{i+1}']['dead']=='False':
                    if char_of_1[f'team_player_{i+1}']['name']!=char_of_1[f'team_player_{user_1_player}']['name']:
                        keyboard1.append([InlineKeyboardButton(f"{char_of_1[f'team_player_{i+1}']['name']}",callback_data=f'pvpmu_sapru_{i+1}_{user_1_id}')])
        if len(keyboard1) < 1 :
            query.answer("You only have 1 character left",show_alert=True)
            return
        keyboard1.append([InlineKeyboardButton(f"BACK",callback_data=f'pvpmu_sapru_back_{user_1_id}')])
        message=query.message.edit_text("*Choose the character*",reply_markup=InlineKeyboardMarkup(keyboard1),parse_mode=ParseMode.MARKDOWN)
        message_id = message.message_id
        cd[message_id] = {}
        cd[message_id]['users']=users
        cd[message_id]['teams']=user_teams
        cd[message_id]['passive']=user_passive
        cd[message_id]['move_done']=move
        cd[message_id]['pvp_player_no']=player_no
        return
    if user.id == user_2_id :
        if user.id != int(query.data.split('_')[2]):
            query.answer("PLAYER 2 TURN",show_alert=True)
            return
        keyboard2=[]
        for i in range (4):
            if char_of_2[f'team_player_{i+1}']['name']!='None':
                if char_of_2[f'team_player_{i+1}']['dead']=='False':
                    if char_of_2[f'team_player_{i+1}']['name']!=char_of_2[f'team_player_{user_2_player}']['name']:
                        keyboard2.append([InlineKeyboardButton(f"{char_of_2[f'team_player_{i+1}']['name']}",callback_data=f'pvpmu_sapru_{i+1}_{user_2_id}')])    
        if len(keyboard2) < 1 :
            query.answer("You only have 1 character left",show_alert=True)
            return
        keyboard2.append([InlineKeyboardButton(f"BACK",callback_data=f'pvpmu_sapru_back_{user_2_id}')])
        message=query.message.edit_text("*Choose the character*",reply_markup=InlineKeyboardMarkup(keyboard2),parse_mode=ParseMode.MARKDOWN)
        message_id = message.message_id
        cd[message_id] = {}
        cd[message_id]['users']=users
        cd[message_id]['teams']=user_teams
        cd[message_id]['passive']=user_passive
        cd[message_id]['move_done']=move
        cd[message_id]['pvp_player_no']=player_no
        return

def recover_user(update,context):
    user=update.effective_user
    if user.id == 1864257459:
        message=int(update.message.text.split(" ")[-1])
        user_data=[db.get_collection("user_datas"),db.get_collection("user_data"),db.get_collection("user_ids"),db.get_collection("beta_users")]
        user_obj_id = user_data[0].find_one()['user_data'][f"user_{message}"]
        print(user_obj_id)
    else:
        update.message.reply_text("*NOT YOUR COMMAND*",parse_mode=ParseMode.MARKDOWN)

def main():
    updater = Updater(API_KEY,use_context=True)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler("start", start,run_async=True))
    dp.add_handler(CommandHandler("explore",explore_cmd,run_async=True))
    dp.add_handler(CommandHandler("open", fgp,run_async=True))
    dp.add_handler(CommandHandler("add_ban",beta_adder,run_async=True))
    dp.add_handler(CommandHandler("characters",charac,run_async=True))
    dp.add_handler(CommandHandler("bag",bag,run_async=True))
    dp.add_handler(CommandHandler("stats",c_stats,run_async=True))
    dp.add_handler(CommandHandler("add",add_res,run_async=True))
    dp.add_handler(CommandHandler("team",team_selection,run_async=True))
    dp.add_handler(CommandHandler("give",giv_cmd))
    dp.add_handler(CommandHandler("update",update_db,run_async=True))
    dp.add_handler(CommandHandler("store",store_cmd,run_async=True))
    dp.add_handler(CommandHandler("enter_dungeon",enter_dungeon,run_async=True))
    dp.add_handler(CommandHandler("elements",element_types,run_async=True))
    dp.add_handler(CommandHandler("travel",travel_logger,run_async=True))
    dp.add_handler(CommandHandler("bot_status",bot_status,run_async=True))
    dp.add_handler(CommandHandler("gift_all",gift_all,run_async=True))
    dp.add_handler(CommandHandler("gacha_gemu",gacha,run_async=True))
    dp.add_handler(CommandHandler("close", fgp_close,run_async=True))
    dp.add_handler(CommandHandler("reset", reset_cmd,run_async=True))
    dp.add_handler(CommandHandler("broadcast",broadcast_all,run_async=True))
    dp.add_handler(CommandHandler("reset_explore",rest_stuk,run_async=True))
    dp.add_handler(CommandHandler("status",status_plate,run_async=True))
    dp.add_handler(CommandHandler("tower",tower_enter,run_async=True))
    dp.add_handler(CommandHandler("history",user_checker,run_async=True))
    dp.add_handler(CommandHandler("kingdom",kingdom,run_async=True))
    dp.add_handler(CommandHandler("events",event_cmd,run_async=True))
    dp.add_handler(CommandHandler("kingdoms",kingdom_adder,run_async=True))
    dp.add_handler(CommandHandler("battle",battle_maker,run_async=True))
    dp.add_handler(CommandHandler("recover",recover_user,run_async=True))
    
    
    CHANGE_WEAPON_HANDLER = ConversationHandler(entry_points=[CallbackQueryHandler(change_weapon, pattern= f'change_weapon',run_async=True),CallbackQueryHandler(char_info, pattern= f'charinfo',run_async=True),CallbackQueryHandler(store_inline, pattern= f'mfstore',run_async=True),CallbackQueryHandler(primo_and_star_store, pattern= f'starstore',run_async=True),CallbackQueryHandler(purchase_maker_1, pattern= f'purchasemaker',run_async=True)],
        states={CHANGE_WEAPON:[CallbackQueryHandler(weapon_changed, pattern= 'weapon-(\d+)',run_async=True)]},
        fallbacks=[],
        allow_reentry=True,
        per_user=True,
        run_async = True)
    GACHA_HANDLER=ConversationHandler(entry_points=[CallbackQueryHandler(gacha_selector,pattern='gacha_standard',run_async=True),CallbackQueryHandler(gacha_selector,pattern='gacha_event',run_async=True),CallbackQueryHandler(gacha_selector,pattern='gacha_weapon',run_async=True),CallbackQueryHandler(gacha_selector,pattern='gacha_close',run_async=True)],
        states={GACHA_LUCK:[CallbackQueryHandler(gacha_got,pattern='gachapull_standard',run_async=True),CallbackQueryHandler(gacha_got,pattern='gachapull_event',run_async=True),CallbackQueryHandler(gacha_got,pattern='gachapull_weapon',run_async=True)]},
        fallbacks=[],
        allow_reentry=True,
        per_user=True,
        run_async=True)
    CHANGE_BAG_HANDLER = ConversationHandler(entry_points=[CallbackQueryHandler(bag_cmd, pattern= f'bag',run_async=True),CallbackQueryHandler(gift_getter, pattern= f'claimdaily',run_async=True),CallbackQueryHandler(smelting, pattern= f'smelter',run_async=True),CallbackQueryHandler(smelting_place, pattern= f'SMELTWEAPON',run_async=True),CallbackQueryHandler(smelt_weapon, pattern= f'smelt_weapon',run_async=True),CallbackQueryHandler(dungon_slt, pattern= f'dungeon_selection',run_async=True),CallbackQueryHandler(travel_slt, pattern= f'travel',run_async=True)],
        states={},
        fallbacks=[],
        allow_reentry=True,
        per_user=True,
        run_async = True)
    CHANGE_TEAM_COMB = ConversationHandler(entry_points=[CallbackQueryHandler(tem_selecter, pattern= f'teamselect',run_async=True),CallbackQueryHandler(c_level_up, pattern= f'level_up',run_async=True),CallbackQueryHandler(main_level_up, pattern= f'level_mychar',run_async=True),CallbackQueryHandler(refferal, pattern= f'reffer_maker',run_async=True)],
        states={TEAM_CHANGER:[CallbackQueryHandler(team_changer,pattern=f"team_change",run_async=True)]},
        fallbacks=[],
        allow_reentry=True,
        per_user=True,
        run_async = True)
    CHANGE_BATTLE = ConversationHandler(entry_points=[CallbackQueryHandler(battle_start, pattern= f'mobbattle',run_async=True),CallbackQueryHandler(char_skill_explorer, pattern= f'mobb_skill',run_async=True),CallbackQueryHandler(middle_of_battle, pattern= f'mobb_',run_async=True)],
        states={BATTLE_FINISH:[CallbackQueryHandler(battle_finsh,pattern=f"Battle_fin",run_async=True)]},
        fallbacks=[],
        allow_reentry=True,
        per_user=True,
        run_async = True)
    CHANGE_PVP = ConversationHandler(entry_points=[CallbackQueryHandler(pvp_battle_handler, pattern= f'pvpstarter_',run_async=True),CallbackQueryHandler(pvp_muu, pattern= f'pvpmu_',run_async=True),CallbackQueryHandler(passer_pvp, pattern= f'passer_pvp',run_async=True),CallbackQueryHandler(pvp_swap_mou, pattern= f'pvpmuu_',run_async=True)],
        states={PVP_FINISH:[]},
        fallbacks=[],
        allow_reentry=True,
        per_user=True,
        run_async = True)
    CHANGE_CHAR_COMB = ConversationHandler(entry_points=[CallbackQueryHandler(charobitan,pattern= f'nex1',run_async=True),CallbackQueryHandler(charobitan,pattern= f'nex2',run_async=True),CallbackQueryHandler(charobitan,pattern= f'nex2',run_async=True),CallbackQueryHandler(charobitan,pattern= f'oba_sha_cha',run_async=True),CallbackQueryHandler(charobitan,pattern= f'oba_mor_cha',run_async=True),CallbackQueryHandler(charobitan,pattern= f'oba_ryz_cha',run_async=True)],
        states={},
        fallbacks=[],
        allow_reentry=True,
        per_user=True,
        run_async = True)
    CHANGE_TOWER = ConversationHandler(entry_points=[CallbackQueryHandler(tower_level, pattern= f'tow_En',run_async=True),CallbackQueryHandler(tower_claimer,pattern=f"tow_claim",run_async=True),CallbackQueryHandler(battle_swapper, pattern=f'mobbb_',run_async=True),CallbackQueryHandler(back_to_event, pattern= f'back_to_event',run_async=True)],
        states={},
        fallbacks=[],
        allow_reentry=True,
        per_user=True,
        run_async = True)
    KINGDOM_HANDLER = ConversationHandler(entry_points=[CallbackQueryHandler(kingdom_joiner, pattern= f'kingjoin',run_async=True),CallbackQueryHandler(kingdom_joined, pattern= f'kingdomjoinextra',run_async=True),CallbackQueryHandler(kingdom_role, pattern= f'Kingdomjoiner-role',run_async=True),CallbackQueryHandler(kingdoom_requester, pattern= f'kingdoom',run_async=True),CallbackQueryHandler(my_kingdom, pattern= f'mykingdom',run_async=True),CallbackQueryHandler(kingdom_power, pattern= f'king',run_async=True)],
        states={},
        fallbacks=[],
        allow_reentry=True,
        per_user=True,
        run_async = True)

    job_queue = updater.job_queue
    if API_KEY != '6343863154:AAE8z14ovv3boMz6jaB-Ien_SI80jF1ngh8':
        job_queue.run_daily(send_gift, datetime.time(hour=0, minute=0, second=0))
    else:
        print("test bot")
    dp.add_handler(CHANGE_CHAR_COMB)
    dp.add_handler(CHANGE_TOWER)
    dp.add_handler(CHANGE_BATTLE)
    dp.add_handler(GACHA_HANDLER)
    dp.add_handler(CHANGE_TEAM_COMB)
    dp.add_handler(CHANGE_BAG_HANDLER)
    dp.add_handler(CHANGE_WEAPON_HANDLER)
    dp.add_handler(KINGDOM_HANDLER)
    dp.add_handler(CHANGE_PVP)
    updater.start_polling()
    updater.idle()

main()
