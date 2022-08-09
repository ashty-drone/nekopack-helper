# -------------------IMPORTS------------------- #
from os import environ, getenv
from telethon.sessions import StringSession
from telethon import TelegramClient, functions
from telethon.tl.types import InputMessagesFilterDocument as document
# --------------------------------------------- #

#BINDTHEQUOTES

async def getBackupChannels():
  channel_id = None
  async for message in cat.iter_messages("me", search="#CAT_BOTLOG_CHATID"):
    channel_id = int(
      (
        message.text
      ).splitlines()[0]
    )
  return channel_id
  
async def getBackupSQL():
  async def iter_backup_sql(chat, download=False):
    async def iterBackupSql(chat, download=False):
      async for message in cat.iter_messages(chat, filter=document):
        if "#SQL_BACKUP" in message.text:
          date = message.date
          if download:
            download = await cat.download_media(message)
            return
          return date
    try: await iterBackupSql(chat, download=download)
    except:
        x = await cat.send_message(chat, "HI")
        x.delete()
        await iter_backup_sql(chat, download=download)
  channel_id = getenv("PRIVATE_GROUP_BOT_API_ID")
  if channel_id:
    await iter_backup_sql(int((str(channel_id)).strip()), download=True)
  else:
    channel_id = await getBackupChannels()
    if not channel_id: return
    await iter_backup_sql(channel_id, download=True)
        
      
      
cat = TelegramClient(
      StringSession(getenv('STRING_SESSION')), 
      getenv('APP_ID'), 
      getenv('API_HASH')
)
if environ.get("INIT_ENABLED") == "True":
  with cat: cat.loop.run_until_complete(getBackupSQL())
  del environ["INIT_ENABLED"]
  
#BINDTHEQUOTES

  
#"""#BREAKTHEQUOTES
# ---------IMPORTS--------- #
import asyncio
from os import getenv
from pathlib import Path
from userbot import catub
from subprocess import run
# ------------------------- #

async def backupSQL():
  sql_backup_path = "/var/lib/postgresql/catuserbot.sql"
  sql_script = "su - postgres -c 'pg_dump catuserbot > catuserbot.sql'"
  run(sql_script, shell=True)
  sql_backup_path = Path(sql_backup_path)
  sql_backup_path.rename('./catuserbot.sql')
  message = "#SQL_BACKUP\nYour database has been backed up!"
  await client.send_message(getenv("PRIVATE_GROUP_BOT_API_ID"), message, file="catuserbot.sql")

async def timer_backup():
  async for message in cat.iter_messages("me", search="#CAT_BOTLOG_CHATID"):
    await message.delete()
  message = (f"{getenv('PRIVATE_GROUP_BOT_API_ID')}\n"
             "#CAT_BOTLOG_CHATID\n"
             "You are running on local Database. Please don't delete this message")
  await client.send_message("me", message)
  while True:
    await backupSQL()
    asyncio.sleep(900)


with cat as client: client.loop.run_until_complete(timer_backup()
  
@catub.cat_cmd(
  pattern="savedb$",
  command=("savedb", "tools"),
  info={
      "header": "You can use this command to immediately backup your local database.",
      "description": (
          "If you are not using elephantsql and are dependant on Local Database, "
          "please use this command to immediately backup your database otherwise your database will not be saved"
          " and you might lose data such as snips, alive vars, etc. "
          "**But don't sweat too much. Your database is automatically saved every 15 mins.**"
      ),
      "usage": "{tr}savedb"
  }
)
async def savedb(event):
  await backupSQL()
"""#BREAKTHEQUOTES
    
    
    
    
    
    
