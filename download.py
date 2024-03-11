"""TG Group Download.

Usage:
  download.py --group <group> --path FILE

Options:
  --group     Group Id
  --path      Path to file

"""
from docopt import docopt
import os
from telethon import TelegramClient
import time
import csv
from random import randint
import asyncio

TG_API_KEY = os.environ['TELEGRAM_API_KEY']
TG_API_HASH = os.environ['TELEGRAM_API_HASH']
TG_SESSION_NAME = os.getenv('TELEGRAM_SESSION_NAME') or 'tg-group-download'

client = TelegramClient(TG_SESSION_NAME, TG_API_KEY, TG_API_HASH)

async def run(group, path):

    with open(path, 'w', newline='') as csvfile:
        d = csv.writer(csvfile, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        d.writerow(['timestamp','text'])

        async for message in client.iter_messages(group):
            d.writerow([int((time.mktime(message.date.timetuple()))), message.text])


with client:
    arguments = docopt(__doc__, version='1.0')
    client.loop.run_until_complete(run(int(arguments["<group>"]), arguments["FILE"]))