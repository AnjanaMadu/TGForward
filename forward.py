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
from telethon import TelegramClient
from telethon.sessions import StringSession
from telethon.tl.types import InputMessagesFilterDocument, InputMessagesFilterMusic, InputMessagesFilterVideo, InputMessagesFilterPhotos
from telethon.errors import FloodError
from config import heroku

from_chat = heroku.FROM_CHANNEL_ID
to_chat = heroku.TO_CHANNEL_ID
custom_caption = heroku.CUSTOM_CAPTION
file_type = heroku.FILE_TYPE
api_id = heroku.API_ID
api_hash = heroku.API_HASH

bot = TelegramClient(StringSession(heroku.STRING_SESSION), api_id, api_hash)
bot.start()

print("Please wait starting forwarding")
print("Start auto forwarding....")

async def forward():
  mode = None
  if file_type == "docs":
    print("Now forwarding only documents")
    mode = InputMessagesFilterDocument
  elif file_type == "music":
    print("Now forwarding only music")
    mode=InputMessagesFilterMusic
  elif file_type == "videos":
    print("Now forwarding only videos")
    mode=InputMessagesFilterVideo
  elif file_type == "photos":
    print("Now forwarding only photos")
    mode=InputMessagesFilterPhotos
  elif file_type == "all":
    print("Now forwarding all messages")
    mode=None
  elif not file_type:
    print("No file type given. System exiting...")
    sys.exit()
  async for msg in bot.iter_messages(from_chat, reverse=True, filter=mode):
      try:
        await asyncio.sleep(2)
        bot.parse_mode = 'html'
        k = await bot.send_file(to_chat, file=msg.media, caption=custom_caption)
      except FloodError as e:
        asyncio.sleep(e.seconds)

bot.loop.run_until_complete(forward())
bot.run_until_disconnected()
