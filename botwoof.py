__author__ = "fatwoof"
__version__ = ".001"
__url__ = "https://github.com/fatwoof/botwoof"

import asyncio
import random
import time
from os import getenv
from random import randint
from typing import Union
import datetime
# from typing import Union

import discord
from discord.ext.commands import Bot
from dotenv import load_dotenv


# load dotenv - related to bot token environment variable (sets/imports all variables found in the .env file)
load_dotenv()

# do some things for the on_typing function
DiscordUser = Union[discord.User, discord.Member]
DiscordTextChannel = Union[discord.TextChannel, discord.DMChannel, discord.GroupChannel]
DiscordPrivateTextChannel = Union[discord.DMChannel, discord.GroupChannel]
DiscordGuildChannel = Union[discord.TextChannel, discord.VoiceChannel]
DiscordChannel = Union[discord.TextChannel, discord.DMChannel, discord.GroupChannel, discord.VoiceChannel]

BOT_PREFIX = ";"

# botwoof token - retreived from .env file
BOT_TOKEN = getenv("BOT_TOKEN")

# set game for bot status message
GAME = discord.Game("fetch (" + BOT_PREFIX + ")")
DEAD_GAME = discord.Game("dead")

# create bot object
bot = Bot(command_prefix=BOT_PREFIX)

# remove default help command
bot.remove_command('help')

# tile or hardwood command match
T_OR_H_MATCHES = ["or hardwood", "hardwood or"]

# some things that are more important than hardwood
T_OR_H_EXCLUSIONS = ["world peace", "life", "cancer cure", "curing cancer", "fatwoof", "free speech", "free democracy",
                     "food and water", "team pink", "nuclear disarmament", "botwoof"]

# fetch items - no longer in use
FETCHITEMS = ["\U0001F362", "\U0001F962", "\U0001F361", "\U0001F3CF"]

# fun list for 'whattodo' command
FUNLIST = ["not play GTAV", "play Minecraft split-screen", "go to the top of Maze Bank Tower",
           "play Rocket League split-screen", "go outside", "go for a walk", "drink some water",
           "see what's streaming on RPAN", "take a screen break"]
# greetings list to change things up a bit
GREETLIST = ["But let's stop acting like I care. As a matter of fact, don't call me anymore!!",
             "I'm glad you're here.", "Is that too formal? I'm still learning the language.", "But not really...",
             "", "I truly mean that."]
             

# define a function that is run on the on_ready event
@bot.event
async def on_ready():
    await bot.change_presence(status=discord.Status.online, activity=GAME)
    print("Botwoof is off the leash!")


### enables bad botwoof
##@bot.event
##async def on_typing(channel: DiscordTextChannel, user: discord.User, when: datetime.datetime):
##    print("someone is typing")
##    time.sleep(5)
##    await channel.send("Hey! Hurry up and send the message already!")


### define a function that is run on member join
##@bot.event
##async def on_member_join(self, member):
##    mention = member.mention
##    await self.client.get_channel(channel id).sendchannel = member.server.get_channel("CHANNEL_ID")
##    print("someone has joined")
##    await bot.send_message("Someone has joined")
##    await member.send('Private message')

# define a function that is run on the on_message event
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
            if any(x in message.content.lower() for x in T_OR_H_EXCLUSIONS):
                await message.channel.send("{0.display_name}, ".format(message.author) + "I'm usually #teamhardwood, but sometimes, " +
                                           "one must look past hardwood and consider more imporant things in this life we live... but you already know that.")
            else:
                await message.channel.send("{0.display_name}, ".format(message.author) + "I'm #teamhardwood, but you already know that.")
        # eat food command
        elif message.content.startswith("\U0001F9B4") or message.content.startswith(
        "\U0001F356") or message.content.startswith("\U0001F357") or message.content.startswith(
        "\U0001f969")or message.content.startswith("\U0001F953"):
             await message.channel.send("\U0001F436")
             
        await bot.process_commands(message)

@bot.command(name='help')
async def help_cmd(ctx):
    await ctx.send("```Hi, i'm Botwoof, Here's what I know:\n\
\n\
Helpful:\n\
    nextround - When the next RPAN Pictionary round will be hosted\n\
    version - My version\n\
    libversion - The discord.py library version I use\n\
Fun:\n\
    greetings\n\
    goodbye\n\
    fetch\n\
    bottleflip\n\
    talk\n\
    playdead\n\
    rollover\n\
    whattodo\n\
\n\
Feel free to message my owner, fatwoof, if i'm getting out of hand```")

                   
@bot.command(name='version')
async def version_cmd(ctx):
    await ctx.send(f"My version is: {__version__}")


@bot.command(name='libversion')
async def libversion_cmd(ctx):
    await ctx.send("My discord.py library version is " + discord.__version__)


@bot.command(name='greetings')
async def greetings_cmd(ctx):
    await ctx.send("Greetings and Salutations, " + "{0.display_name}.".format(ctx.author) + " " + random.choice(GREETLIST))


@bot.command(name='goodbye')
async def goodbye_cmd(ctx):
    await ctx.send("Goodbye " + "{0.display_name}. ".format(ctx.author) + "I think i'll stay here but I hope to see you return soon.")


@bot.command(name='fetch')
async def fetch_cmd(ctx, *items: str):
    response = random.choice(FETCHITEMS) if not items else " ".join(items)
    await ctx.send("\U0001F436" + "\U0001F4A8")
    await asyncio.sleep(randint(1, 30))
    await ctx.send("{0.display_name}, ".format(ctx.author) + "\U0001F436" + "\U0001F4A6" + response)


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
        return m.content.lower() == 'hello' and m.channel == channel

    msg = await bot.wait_for('message', check=check)
    await channel.send(f'Hello {msg.author.mention}!')


@bot.command(name='playdead')
async def playdead_cmd(ctx):
    await bot.change_presence(status=discord.Status.invisible, activity=DEAD_GAME)
    await asyncio.sleep(1)
    await ctx.send("https://i.imgur.com/zpGmavE.png")
    await asyncio.sleep(15)
    await bot.change_presence(status=discord.Status.online, activity=GAME)
    await ctx.send("\U0001F436")


@bot.command(name='whattodo')
async def whatshouldwedo_cmd(ctx):
    await ctx.send("{0.display_name}, ".format(ctx.author) + "you should " + random.choice(FUNLIST) + "!")


@bot.command(name='rollover')
async def rollover(ctx):
	await ctx.send("https://cdn.discordapp.com/attachments/714257028637392926/728091591410974780/rollover_small.gif")


def run():
    bot.run(BOT_TOKEN)


if __name__ == '__main__':
    run()
