__author__ = "fatwoof"
__version__ = ".001"
__url__ = "https://github.com/fatwoof/botwoof"

import asyncio
import random
import time
from os import getenv
from random import randint
# from typing import Union

import discord
# import emoji
from discord.ext.commands import Bot
from dotenv import load_dotenv


# load dotenv - related to bot token environment variable (sets/imports all variables found in the .env file)
load_dotenv()

# do some things for the on_typing function
# DiscordUser = Union[discord.User, discord.Member]
# DiscordTextChannel = Union[discord.TextChannel, discord.DMChannel, discord.GroupChannel]
# DiscordPrivateTextChannel = Union[discord.DMChannel, discord.GroupChannel]
# DiscordGuildChannel = Union[discord.TextChannel, discord.VoiceChannel]
# DiscordChannel = Union[discord.TextChannel, discord.DMChannel, discord.GroupChannel, discord.VoiceChannel]

BOT_PREFIX = ";"

# botwoof token - retreived from .env file
BOT_TOKEN = getenv("BOT_TOKEN")

# set game for bot status message
GAME = discord.Game("fetch (" + BOT_PREFIX + ")")
DEAD_GAME = discord.Game("dead")

# create bot object
bot = Bot(command_prefix=BOT_PREFIX)

# tile or hardwood command match
T_OR_H_MATCHES = ["or hardwood", "hardwood or"]

# fetch items - no longer in use
FETCH_ITEMS = ["\U0001F362", "\U0001F962", "\U0001F361", "\U0001F3CF"]

# fun list for 'what should we do?' command
FUNLIST = ["not play GTAV", "play Minecraft split-screen", "go to the top of Maze Bank Tower",
           "play Rocket League split-screen"]


# define a function that is run on the on_ready event
@bot.event
async def on_ready():
    await bot.change_presence(status=discord.Status.online, activity=GAME)
    print("The bot is ready!")


# define a function that is run on the on_typing event
# @client.event
# async def on_typing(channel: DiscordTextChannel, user: discord.User, when: datetime.datetime):
#     print("someone is typing")
#     time.sleep(5)
#     await channel.send("Hey! Hurry up and send the message already!")

##SIMPLE COMMANDS
##definie a function that is run on the on_message event
@bot.event
async def on_message(message):
    print(message.author.name + " said, '" + message.content + "'")
    if not message.author == bot.user:
        if message.content.startswith('👍'):
            channel = message.channel
            await channel.send('Send me that 👍 reaction, mate')

            def check(reaction, user):
                return user == message.author and str(reaction.emoji) == '👍'

            try:
                reaction, user = await bot.wait_for('reaction_add', timeout=60.0, check=check)
            except asyncio.TimeoutError:
                await channel.send('👎')
            else:
                await channel.send('👍')
        elif any(x in message.content.lower() for x in T_OR_H_MATCHES):
            await message.channel.send("I'm #teamhardwood, but you already know that.")
        # eat food command
        elif message.content.startswith("\U0001F9B4") or message.content.startswith(
        "\U0001F356") or message.content.startswith("\U0001F357") or message.content.startswith(
             "\U0001F969") or message.content.startswith("\U0001F953"):
             await message.channel.send("\U0001F436")
             # elif prefix + "emoji" in message.content.lower():
             #     channel = message.channel
             #     content = message.content
             #     print("Test content print: " + content)
             #     await channel.send('Hello {.author}!')
             #     await message.channel.send(emoji.emojize('Python is :thumbs_up:'))
             #
             #     def extract_emojis(content):
             #         return ''.join(c for c in content if c in emoji.UNICODE_EMOJI)
        await bot.process_commands(message)


@bot.command(name='version')
async def version_cmd(ctx):
    await ctx.send(f"My version is: {__version__}")


@bot.command(name='libversion')
async def libversion_cmd(ctx):
    await ctx.send("My discord.py library version is " + discord.__version__)


@bot.command(name='greetings')
async def greetings_cmd(ctx):
    await ctx.send("Greetings and Salutations! But let's stop acting like I care. "
                   "As a matter of fact, don't message me anymore!!")


@bot.command(name='goodbye')
async def goodbye_cmd(ctx):
    await ctx.send("Goodbye friend, I think i'll stay here. Hope to see you return soon.")


@bot.command(name='fetch')
async def fetch_cmd(ctx, *items: str):
    response = random.choice(FETCH_ITEMS) if not items else " ".join(items)
    await ctx.send("\U0001F436" + "\U0001F4A8")
    await asyncio.sleep(randint(1, 30))
    await ctx.send("\U0001F436" + "\U0001F4A6" + response)


@bot.command(name='nextround', aliases=['nr'])
async def nextround_cmd(ctx):
    epoch_time = time.time()
    print(epoch_time)
    local_time = time.localtime(epoch_time)
    if (local_time.tm_wday == 5 and local_time.tm_hour >= 22) or local_time.tm_wday == 6 or (
            local_time.tm_wday == 0 and local_time.tm_hour <= 11):
        await ctx.send(
            "Next round of Pictionary is Monday @ 12:00pm CDT https://s7.gifyu.com/images/ezgif-4-8d916dafcb6b.gif")
    elif (local_time.tm_wday == 0 and local_time.tm_hour >= 12) or (
            local_time.tm_wday == 1 and local_time.tm_hour <= 21):
        await ctx.send(
            "Next round of Pictionary is Tuesday @ 9:30pm CDT https://s7.gifyu.com/images/ezgif-4-8d916dafcb6b.gif")
    elif (local_time.tm_wday == 1 and local_time.tm_hour >= 22) or (
            local_time.tm_wday == 2 and local_time.tm_hour <= 11):
        await ctx.send(
            "Next round of Pictionary is Wednesday @ 12:00pm CDT https://s7.gifyu.com/images/ezgif-4-8d916dafcb6b.gif")
    elif (local_time.tm_wday == 2 and local_time.tm_hour >= 12) or (
            local_time.tm_wday == 3 and local_time.tm_hour <= 21):
        await ctx.send(
            "Next round of Pictionary is Thursday @ 9:30pm CDT https://s7.gifyu.com/images/ezgif-4-8d916dafcb6b.gif")
    elif (local_time.tm_wday == 3 and local_time.tm_hour >= 22) or (
            local_time.tm_wday == 4 and local_time.tm_hour <= 11):
        await ctx.send(
            "Next round of Pictionary is Friday @ 12:00pm CDT https://s7.gifyu.com/images/ezgif-4-8d916dafcb6b.gif")
    elif (local_time.tm_wday == 4 and local_time.tm_hour >= 12) or (
            local_time.tm_wday == 5 and local_time.tm_hour <= 21):
        await ctx.send(
            "Next round of Pictionary is Saturday @ 9:30pm CDT https://s7.gifyu.com/images/ezgif-4-8d916dafcb6b.gif")
    else:
        await ctx.send("The current time is outside of my programmed times. Try again soon.")


@bot.command(name='bottleflip')
async def bottleflip_cmd(ctx):
    await ctx.send("Really, a bottle flip? Here, he'll do one https://s7.gifyu.com/images/ezgif-4-7d0b7b5d9c66.gif")


@bot.command(name='talk')
async def talk_cmd(ctx):
    channel = ctx.channel
    await channel.send('Say "woof", I mean, say "hello"')

    def check(m):
        return m.content == 'hello' and m.channel == channel

    msg = await bot.wait_for('message', check=check)
    await channel.send(f'Hello {msg.author.mention}!')


@bot.command(name='playdead')
async def playdead_cmd(ctx):
    await bot.change_presence(status=discord.Status.invisible, activity=DEAD_GAME)
    await asyncio.sleep(1)
    await ctx.send("https://i.imgur.com/zpGmavE.png")
    await asyncio.sleep(15)
    await bot.change_presence(status=discord.Status.online, activity=GAME)
    print("The bot is ready!")
    await ctx.send("\U0001F436")


@bot.command(name='what should we do?')
async def whatshouldwedo_cmd(ctx):
    await ctx.send("You should " + random.choice(FUNLIST) + "!")


def run():
    bot.run(BOT_TOKEN)


if __name__ == '__main__':
    run()
