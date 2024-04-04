
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

if chat_id:
    print(f"Chat ID for the link '{chat_link}' is: {chat_id}")
else:
    print("Failed to retrieve chat ID.")
