import os

class Config(object):
  API_ID = int(os.environ.get("API_ID", ""))
  API_HASH = os.environ.get("API_HASH", "")
  BOT_TOKEN = os.environ.get("BOT_TOKEN", "")
  BOT_USERNAME = os.environ.get("BOT_USERNAME", "")
  DB_CHANNEL = int(os.environ.get("DB_CHANNEL", "-1002039630436"))
  SHORTLINK_URL = os.environ.get('SHORTLINK_URL', "Tinyfy.in")
  SHORTLINK_API = os.environ.get('SHORTLINK_API', "dd6eaae867ac95d21f4d7031fef4d82261a3fabd")
  BOT_OWNER = int(os.environ.get("BOT_OWNER", ""))
  DATABASE_URL = os.environ.get("DATABASE_URL", "")
  UPDATES_CHANNEL = os.environ.get("UPDATES_CHANNEL", "")
  LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL", ""))
  BANNED_USERS = set(int(x) for x in os.environ.get("BANNED_USERS", "").split())
  FORWARD_AS_COPY = bool(os.environ.get("FORWARD_AS_COPY", True))
  BROADCAST_AS_COPY = bool(os.environ.get("BROADCAST_AS_COPY", True))
  BANNED_CHAT_IDS = list(set(int(x) for x in os.environ.get("BANNED_CHAT_IDS", "").split()))
  OTHER_USERS_CAN_SAVE_FILE = bool(os.environ.get("OTHER_USERS_CAN_SAVE_FILE", True))
  ABOUT_BOT_TEXT = f"""
🔸I am file store bot that will permanently store your given file and will provide you a permanent link to access that file.🔸

🤖 **ᴍʏ ɴᴀᴍᴇ:** [Gᴀʟᴀxʏ ꜰɪʟᴇꜱ ꜱᴛᴏʀᴇ ʙᴏᴛ](https://t.me/{BOT_USERNAME})
📝 **ʟᴀɴɢᴜᴀɢᴇ:** [Python](https://www.python.org)
📚 **ʟɪʙʀᴀʀʏ:** [Pyrogram](https://docs.pyrogram.org)
📡 **ʜᴏꜱᴛᴇᴅ ᴏɴ:** [koyeb](https://app.koyeb.com)
🧑🏻‍💻 **Dᴇᴠʟᴏᴘᴇʀ:** [Eᴋᴀᴍᴘʀᴇᴇᴛ⑅Sɪɴɢʜ](https://t.me/EK4MPREETSINGH)
"""

  DISCLAIMER_TXT = """❗ᴛʜɪꜱ ʙᴏᴛ ɪꜱ ᴘʀᴇᴍɪᴜᴍ ꜰɪʟᴇ ꜱᴛᴏʀᴇ. ʏᴏᴜ ᴄᴀɴ ᴜꜱᴇ ɪᴛ ᴛᴏ ꜱᴛᴏʀᴇ ᴀꜱ ᴍᴀɴʏ ꜰɪʟᴇꜱ ʏᴏᴜ ᴡᴀɴᴛ ʙᴜᴛ ᴘʟᴇᴀꜱᴇ ᴅᴏ ɴᴏᴛ ꜱᴛᴏʀᴇ ᴀɴᴅ ᴘᴏʀɴ ꜰɪʟᴇꜱ ɪɴ ᴛʜɪꜱ ʙᴏᴛ ᴏᴛʜᴇʀᴡɪꜱᴇ ᴡᴇ ᴀʀᴇ ɢᴏɪɴɢ ᴛᴏ ʙᴀɴ ʏᴏᴜ.
"""
  SOURCE_TXT = """ • ᴛʜɪꜱ ɪꜱ ᴀ ᴜᴘᴅᴀᴛᴇᴅ ᴀɴᴅ ᴘʀᴇᴍɪᴜᴍ ꜰɪʟᴇ ꜱᴛᴏʀᴇ ʙᴏᴛ ʙʏ [ᴇᴋᴀᴍᴘʀᴇᴇᴛ ꜱɪɴɢʜ](https://t.me/EK4MPREETSINGH)
• ʏᴏᴜ ᴄᴀɴ ʙᴜʏ ɪᴛ ꜰʀᴏᴍ ᴍʏ ᴏᴡɴᴇʀ
"""
  
  ABOUT_DEV_TEXT = f"""
🧑🏻‍💻 𝗗𝗲𝘃𝗲𝗹𝗼𝗽𝗲𝗿: [Eᴋᴀᴍᴘʀᴇᴇᴛ⑅Sɪɴɢʜ](https://telegram.me/EK4MPREETSINGH)

ɪꜰ ʏᴏᴜ ꜰᴏᴜɴᴅ ᴀɴʏ ᴇʀʀᴏʀ ᴏʀ ʙᴜɢ ɪɴ ᴛʜɪꜱ ʏᴏᴜ ᴄᴀɴ ᴄᴏɴᴛᴀᴄᴛ ᴛᴏ ᴀᴅᴍɪɴ
"""
  HOME_TEXT = """
ʜᴇʏ, [{}](tg://user?id={})\n\nɪ'ᴍ ᴀ ᴘᴇʀᴍᴀɴᴇɴᴛ ꜰɪʟᴇ ꜱᴛᴏʀᴇ ʙᴏᴛ.\n🔹Jᴜsᴛ sᴇɴᴅ ᴍᴇ ᴀ ғɪʟᴇ ᴀɴᴅ ɪ ᴡɪʟʟ ᴘᴇʀᴍᴀᴍᴇɴᴛʟʏ sᴛᴏʀᴇ ɪᴛ ᴀɴᴅ ᴡɪʟʟ ᴘʀᴏᴠɪᴅᴇ ʏᴏᴜ ᴀ ᴘᴇʀᴍᴀɴᴇɴᴛ ʟɪɴᴋ ᴛᴏ ᴀᴄᴄᴇss ɪᴛ.

🔸 Mᴀɪɴᴛᴀɪɴᴇᴅ ʙʏ: [Eᴋᴀᴍᴘʀᴇᴇᴛ Sɪɴɢʜ](https://t.me/EK4MPREETSINGH)
"""
