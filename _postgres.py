from os import environ, getenv
from telethon.sessions import StringSession
from telethon import TelegramClient, functions
from telethon.tl.types import InputMessagesFilterDocument as document

print("check 0")

async def getBackupChannels():
  async def get_backup_channel():
    async with client.takeout(finalize=True) as takeout: #credits to https://t.me/UniBorg/142
      result = await takeout(functions.channels.GetLeftChannelsRequest(offset=0))
      channel_id = []
    for chat in result.chats:
      if chat.title == 'CatUserbot Database Backup Group':
        channel_id.append(chat.id)
    print("check 1")
    return channel_id
  try: await get_back_channel()
  except: return None

async def joinBackupChannels():
  channel_id = await getBackupChannels()
  if not channel_id: return channel_id
  for chat in channel_id:
    await client(functions.channels.JoinChannelRequest(channel=chat))
    print("check 2")
  return channel_id
  
async def getBackupSQL():
  async def iter_backup_sql(chat, download=False):
    async def iterBackupSql(chat, download=False):
      async for message in client.iter_messages(chat, filter=document):
        if "#SQL_BACKUP" in message.text:
          date = message.date
          if download:
            download = await client.download_media(message)
            print("check 5")
            return
          return date
    try: await iterBackupSql(chat, download=download)
    except:
        x = await client.send_message(chat, "HI")
        x.delete()
        await iter_backup_sql(chat, download=download)
  channel_id = getenv("CATUSERBOT_DATABASE_GROUP_ID")
  if channel_id:
    await iter_backup_sql(int((str(channel_id)).strip()), download=True)
    print("check 3")
  else:
    channel_id = await joinBackupChannels()
    if channel_id:
      if len(channel_id) == 1:
        await iter_backup_sql(channel_id, download=True)
        print("check 4")
      else:
        date = []
        for chat in channel_id:
          date.append(iter_backup_sql(channel_id))
        sorted_date = sorted(range(len(date)), key=lambda n: date[n], reverse=True)
        await iter_backup_sql(channel_id[sorted_date[0]], download=True)
        

  
cat = TelegramClient(
    StringSession(getenv('STRING_SESSION')), 
    getenv('APP_ID'), 
    getenv('API_HASH')
)
with cat as client: cat.loop.run_until_complete(getBackupSQL())
          
      
    
    
    
    
    
    
