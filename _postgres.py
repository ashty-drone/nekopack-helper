from os import environ, getenv
from telethon import TelegramClient, functions
from telethon.tl.types import InputMessagesFilterDocument as document

cat = TelegramClient(
    getenv('STRING_SESSION'), 
    getenv('APP_ID'), 
    getenv('API_HASH')
)

async def getBackupChannels():
  async with client.takeout(finalize=True) as takeout: #credits to https://t.me/UniBorg/142
    result = await takeout(functions.channels.GetLeftChannelsRequest(offset=0))
    channel_id = []
  for chat in result.chats:
    if chat.title == 'CatUserbot Database Backup Group':
       channel_id.append(chat.id)
  return channel_id

async def joinBackupChannels():
  channel_id = await getBackupChannels()
  for chat in channel_id:
    if chat: await client(functions.channels.JoinChannelRequest(channel=chat))
  return channel_id
  
async def getBackupSQL():
  async def iter_backup_sql(chat, download=False):
    async for message in client.iter_messages(chat, filter=document):
      if "#SQL_BACKUP" in message.text:
        date = message.date
        if download:
          download = await client.download_media(message)
          return
        return date
    return None
  channel_id = getenv("CATUSERBOT_DATABASE_GROUP_ID"):
  if channel_id:
    iter_backup_sql(int((str(channel_id)).strip()), download=True)
  else:
    channel_id = joinBackupChannels()
    if channel_id:
      
    
    
    
    
    
    
