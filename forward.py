'''TGForward, An Telegram Bot Project
Copyright (c) 2021 Anjana Madu and Amarnath CDJ <https://github.com/AnjanaMadu>

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU Affero General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU Affero General Public License for more details.

You should have received a copy of the GNU Affero General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>'''

import asyncio, sys
import os, requests
from telethon import TelegramClient
from telethon.sessions import StringSession
from telethon.tl.types import InputMessagesFilterDocument, InputMessagesFilterMusic, InputMessagesFilterVideo, InputMessagesFilterPhotos
from telethon.errors import FloodError
from os import environ

try:
  tgsession = environ.get("STRING_SESSION")
  api_id = int(environ.get("API_ID"))
  api_hash = environ.get("API_HASH")
  from_chat = int(environ.get("FROM_CHANNEL_ID"))
  to_chat = int(environ.get("TO_CHANNEL_ID"))
  custom_caption = environ.get("CUSTOM_CAPTION")
  thumb_url = environ.get("CUSTOM_THUMBNAIL")
  file_type = environ.get("FILE_TYPE")
except:
  print("OOOPS! PLEASE CHECK CONFIG VARS AND READ THE README AGAIN.")
  print("CONFIG VARS ARE WRONG. SYSTEM EXITING..")
  sys.exit()

bot = TelegramClient(StringSession(tgsession), api_id, api_hash)
bot.start()

if thumb_url:
  if not 'https://' in thumb_url:
    print("PLEASE REFER README AGAIN!")
    sys.exit()
  thumb = requests.get(thumb_url)
  with open('thumb.jpg', 'wb') as f:
    f.write(thumb.content)
    f.close()
  print('Thumbnail Downloaded!')

print('-----------| Bot Started |-----------')

async def forward():
  mode = None
  if file_type == "docs":
    mode = InputMessagesFilterDocument
  elif file_type == "music":
    mode = InputMessagesFilterMusic
  elif file_type == "videos":
    mode = InputMessagesFilterVideo
  elif file_type == "photos":
    mode = InputMessagesFilterPhotos
  elif file_type == "all":
    mode = None

  async for msg in bot.iter_messages(from_chat, reverse=True, max_id=1, filter=mode):
    try:
      if msg:
        if custom_caption and thumb_url:
          await bot.send_file(to_chat, file=msg.media, thumb='thumb.jpg', caption=custom_caption)
        elif custom_caption:
          await bot.send_file(to_chat, file=msg.media, caption=custom_caption)
        elif thumb_url:
          await bot.send_file(to_chat, file=msg.media, thumb='thumb.jpg')
        else:
          await bot.send_file(to_chat, file=msg.media)
    except FloodError as e:
      asyncio.sleep(e.seconds)

bot.loop.run_until_complete(forward())
bot.run_until_disconnected()
