'''TGForward, A Telegram Bot Project
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

import os
import sys
import asyncio
from telethon import TelegramClient
from telethon.sessions import StringSession
from telethon.tl.types import InputMessagesFilterDocument, InputMessagesFilterMusic, InputMessagesFilterVideo, InputMessagesFilterPhotos
from telethon.errors import FloodError

API_ID = int(os.environ.get("API_ID"))
API_HASH = os.environ.get("API_HASH")
STRING_SESSION = os.environ.get("STRING_SESSION")
FROM_CHANNEL_ID = int(os.environ.get("FROM_CHANNEL_ID"))
TO_CHANNEL_ID = int(os.environ.get("TO_CHANNEL_ID"))
CUSTOM_CAPTION = os.environ.get("CUSTOM_CAPTION", None)
FILE_TYPE = os.environ.get("FILE_TYPE", None)

bot = TelegramClient(StringSession(STRING_SESSION), API_ID, API_HASH)
bot.start()
bot.parse_mode = 'html'

print("Please wait starting forwarding")
print("Start auto forwarding....")

async def forward():
  mode = None
  if FILE_TYPE == "docs":
    print("Now forwarding only documents")
    mode = InputMessagesFilterDocument
  elif FILE_TYPE == "music":
    print("Now forwarding only music")
    mode = InputMessagesFilterMusic
  elif FILE_TYPE == "videos":
    print("Now forwarding only videos")
    mode = InputMessagesFilterVideo
  elif FILE_TYPE == "photos":
    print("Now forwarding only photos")
    mode = InputMessagesFilterPhotos
  elif FILE_TYPE == "all":
    print("Now forwarding all messages")
    mode = None
  elif not FILE_TYPE:
    print("No file type given. System exiting...")
    sys.exit()
  async for msg in bot.iter_messages(FROM_CHANNEL_ID, reverse=True, filter=mode):
      try:
        if CUSTOM_CAPTION:
          await bot.send_file(TO_CHANNEL_ID, file=msg.media, caption=CUSTOM_CAPTION)
        else:
          await bot.send_file(TO_CHANNEL_ID, file=msg.media)
        await asyncio.sleep(2)
      except FloodError as e:
        await asyncio.sleep(e.seconds)

bot.loop.run_until_complete(forward())
bot.run_until_disconnected()
