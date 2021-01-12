import os

import discord
from dotenv import load_dotenv

import sys
import asyncio

if sys.version_info[0] == 3 and sys.version_info[1] >= 8 and \
        sys.platform.startswith('win'):
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

client = discord.Client()


@client.event
async def on_ready():
    print(f'{client.user} is here to teach Python.')

client.run(TOKEN)
