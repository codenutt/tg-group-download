"""TG List Chat Id.

Usage:
  chatids.py

"""
from docopt import docopt
from telethon.utils import get_display_name
import os
from telethon import TelegramClient

TG_API_KEY = os.environ['TELEGRAM_API_KEY']
TG_API_HASH = os.environ['TELEGRAM_API_HASH']
TG_SESSION_NAME = os.getenv('TELEGRAM_SESSION_NAME') or 'tg-group-download'

client = TelegramClient(TG_SESSION_NAME, TG_API_KEY, TG_API_HASH)

async def run():

    dialogs = await client.get_dialogs(100)
    for dialog in dialogs:
        print(get_display_name(dialog.entity), dialog.entity.id)


with client:
    arguments = docopt(__doc__, version='1.0')
    client.loop.run_until_complete(run())