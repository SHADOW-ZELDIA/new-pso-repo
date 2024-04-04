keyboard=[[InlineKeyboardButton(f"{moves['normal_move']['name']}",callback_data=f'pvpmu_normal_{user_2_id}')],[InlineKeyboardButton(f"{moves['dodge_move']['name']}",callback_data=f'pvpmu_dodge_{user_2_id}'),InlineKeyboardButton(f"SWAP",callback_data=f'pvpmuu_swap_{user_2_id}'),InlineKeyboardButton(f"DRAW",callback_data=f'pvpmuu_draw_{user_1_id}_{user_2_id}')],[InlineKeyboardButton(f"WITHDRAW",callback_data=f'pvpmu_withdraw_{user_1_id}_{user_2_id}')]]


async def get_chat_id_from_link(link):
    try:
        result = await client(ImportChatInviteRequest(link))
        chat_id = result.chats[0].id
        return chat_id
    except Exception as e:
        print(f"Error: {e}")
        return None

# Example chat link (replace with your actual link)
chat_link = 'https://t.me/joinchat/AAAAAEHbEkejzxUjAUCfYg'

chat_id = await get_chat_id_from_link(chat_link)
if chat_id:
    print(f"Chat ID for the link '{chat_link}' is: {chat_id}")
else:
    print("Failed to retrieve chat ID.")
