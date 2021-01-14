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
@client.command(description='Please say hi to me!')
async def hello(ctx):
    msg = f'Hi {ctx.author.mention}'
    await ctx.send(msg)


# Send the users the guide to contribute to this bot
@client.command(name='getstarted',
                description='Learn how to get started on making me smarter')
async def get_started(ctx):
    creator = await client.fetch_user(227469030422741003)

    msg = discord.Embed(
        description=f"""Thank you for your interests in teaching me what I \
don't know. First of all, if you have not yet created a GitHub \
account. Please go to https://www.github.com and create one.

Once you have created an account, go to https://github.com/nathnet/CSE-160-Bot \
On there, you will see a repository named CSE-160-Bot. To the left \
of it, there is a button saying \"fork.\" After you have forked the \
repo, you will be redirected to the forked repo on your account.

You can then \"git clone [repository]\" to your local machine. \
You can now make changes to me! Happy hacking!

Uh oh, one thing. If you would like to test changes, you will have \
to create your own test bot, which can be done on \
https://discord.com/developers/applications. After that, go into your \
application you just created, and select bot on the left tab. Then, \
create a new bot. With that new bot, you copy the token and paste \
that in .env in the root directory. You're good to go!

But hey? Where do I see the changes I made? Oops, I'm sorry. \
You won't see it on the real me yet. On the left navigation bar, \
go to OAuth2. Choose bot for the scope and administrator for \
permissions. Copy the link and paste in on the browser and... \
Bam! You have added a bot to your server. That's where you will \
see all the changes.

Want to push the changes to me? I think I have been talking too much. \
Let's leave it until next time. Or just contact {creator.mention} \
and he will be able to help you if needed."""
    )
    await ctx.send(embed=msg)


# Send the users the output of homework according to the homework number
@client.command()
async def hwoutput(ctx, *args):
    msg = None

    if args[0] == '1':
        msg = discord.Embed(
            description=f"""Problem 1 solution follows:
Root 1: 0.6496430521608568
Root 2: 1.3036902811724767

Problem 2 solution follows:
1/2: 0.5
1/3: 0.3333333333333333
1/4: 0.25
1/5: 0.2
1/6: 0.16666666666666666
1/7: 0.14285714285714285
1/8: 0.125
1/9: 0.1111111111111111
1/10: 0.1

Problem 3 solution follows:
Triangular number 10 via loop: 55
Triangular number 10 via formula: 55.0

Problem 4 solution follows:
10!: 3628800

Problem 5 solution follows:
10!: 3628800
9!: 362880
8!: 40320
7!: 5040
6!: 720
5!: 120
4!: 24
3!: 6
2!: 2
1!: 1

Problem 6 solution follows:
e: 2.7182818011463845"""
        )

    await ctx.send(embed=msg)

# Start the discord bot with the specified token
client.run(DISCORD_TOKEN)
