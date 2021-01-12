# Import OS module
import os

# Import discord-related module plus env
import discord
from discord.ext import commands
from dotenv import load_dotenv

# Import sys and asyncio
import sys
import asyncio

# Suppress closing error on Windows
if sys.version_info[0] == 3 and sys.version_info[1] >= 8 and \
        sys.platform.startswith('win'):
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

# Load the .env file to get secret keys
load_dotenv()

# Set Discord token
DISCORD_TOKEN = os.getenv('DISCORD_TOKEN')

# Launch Discord bot and setup command object with prefix '!'
client = discord.Client()
client = commands.Bot(command_prefix='!')


# Notify the server when the bot is up
@client.event
async def on_ready():
    print(f'{client.user} is here to teach Python.')


# Interact with users' messages
@client.event
async def on_message(message):
    if message.author == client.user:
        return

    await client.process_commands(message)


# Reply user with a woke greeting
@client.command()
async def hello(ctx):
    msg = f'Hi {ctx.author.mention}'
    await ctx.send(msg)


# Send the users the guide to contribute to this bot
@client.command(name='getstarted')
async def get_started(ctx):
    print('test')

# Start the discord bot with the specified token
client.run(DISCORD_TOKEN)
