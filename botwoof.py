#import libraries
import discord
from discord.ext.commands import Bot
import random
import datetime
import time
import asyncio
##import emoji

from random import randint
from time import localtime
from time import sleep
from typing import Union
from os import getenv
from dotenv import load_dotenv

#load dotenv - related to bot token environment variable
load_dotenv()

#do some things for the on_typing function
DiscordUser = Union[discord.User, discord.Member]
DiscordTextChannel = Union[discord.TextChannel, discord.DMChannel, discord.GroupChannel]
DiscordPrivateTextChannel = Union[discord.DMChannel, discord.GroupChannel]
DiscordGuildChannel = Union[discord.TextChannel, discord.VoiceChannel]
DiscordChannel = Union[discord.TextChannel, discord.DMChannel, discord.GroupChannel, discord.VoiceChannel]

#bot prefix
prefix = ";"

#bot version
version = ".001"

#botwoof token - retreived from .env file
TOKEN = getenv("BOT_TOKEN")

#create bot object
client = Bot(command_prefix = prefix)

#set game for bot status message
game = discord.Game("fetch (" + prefix + ")")
dead_game = discord.Game("dead")

#tile or hardwood command match
t_or_h_matches = ["or hardwood", "hardwood or"]

#fetch items - no longer in use
fetch_items = ["\U0001F362","\U0001F962","\U0001F361","\U0001F3CF"]

#fun list for 'what should we do?' command
funlist = ["not play GTAV","play Minecraft split-screen","go to the top of Maze Bank Tower","play Rocket League split-screen"]

#define a function that is run on the on_ready event
@client.event
async def on_ready():
    await client.change_presence(status=discord.Status.online, activity=game)
    print("The bot is ready!")

###define a function that is run on the on_typing event
##@client.event
##async def on_typing(channel: DiscordTextChannel, user: discord.User, when: datetime.datetime):
##    print("someone is typing")
##    time.sleep(5)
##    await channel.send("Hey! Hurry up and send the message already!")

#SIMPLE COMMANDS
#definie a function that is run on the on_message event
@client.event
async def on_message(message):
    print(message.author.name+" said, '"+message.content+"'")
    if not message.author == client.user:
        if prefix + "libversion" == message.content.lower():
            await message.channel.send("My discord.py library version is " + discord.__version__)
        elif prefix + "version" == message.content.lower():
            await message.channel.send("My version is " + version)
        elif prefix + "msginfo" == message.content.lower():
            await message.channel.send("Text Channel: " + str(message.pinned))
        if prefix + "talk" == message.content.lower():
            channel = message.channel
            await channel.send('Say "woof", I mean, say "hello"')

            def check(m):
                return m.content == 'hello' and m.channel == channel

            msg = await client.wait_for('message', check=check)
            await channel.send('Hello {.author}!'.format(msg))
        elif prefix + "greetings" == message.content.lower():
            await message.channel.send("Greetings and Salutations! But let's stop acting like I care. As a matter of fact, don't message me anymore!!")
        elif prefix + "goodbye" == message.content.lower():
            message_author = message.author
            await message.channel.send("Goodbye friend, I think i'll stay here. Hope to see you return soon.")

        elif message.content.startswith('👍'):
            channel = message.channel
            await channel.send('Send me that 👍 reaction, mate')   
            def check(reaction, user):
                    return user == message.author and str(reaction.emoji) == '👍'
            try:
                    reaction, user = await client.wait_for('reaction_add', timeout=60.0, check=check)
            except asyncio.TimeoutError:
                    await channel.send('👎')
            else:
                    await channel.send('👍')
        elif prefix + "what should we do?" == message.content.lower():
            await message.channel.send("You should " + random.choice(funlist) + "!")
        elif prefix + "nextround" == message.content.lower ():
            epoch_time = time.time()
            print(epoch_time)
            local_time = time.localtime(epoch_time)
            if (local_time.tm_wday == 5 and local_time.tm_hour >= 22) or local_time.tm_wday == 6 or (local_time.tm_wday == 0 and local_time.tm_hour <= 11):
                await message.channel.send("Next round of Pictionary is Monday @ 12:00pm CDT https://s7.gifyu.com/images/ezgif-4-8d916dafcb6b.gif")
            elif (local_time.tm_wday == 0 and local_time.tm_hour >= 12) or (local_time.tm_wday == 1 and local_time.tm_hour <= 21):
                await message.channel.send("Next round of Pictionary is Tuesday @ 9:30pm CDT https://s7.gifyu.com/images/ezgif-4-8d916dafcb6b.gif")
            elif (local_time.tm_wday == 1 and local_time.tm_hour >= 22) or (local_time.tm_wday == 2 and local_time.tm_hour <= 11):
                await message.channel.send("Next round of Pictionary is Wednesday @ 12:00pm CDT https://s7.gifyu.com/images/ezgif-4-8d916dafcb6b.gif")
            elif (local_time.tm_wday == 2 and local_time.tm_hour >= 12) or (local_time.tm_wday == 3 and local_time.tm_hour <= 21):
                await message.channel.send("Next round of Pictionary is Thursday @ 9:30pm CDT https://s7.gifyu.com/images/ezgif-4-8d916dafcb6b.gif")
            elif (local_time.tm_wday == 3 and local_time.tm_hour >= 22) or (local_time.tm_wday == 4 and local_time.tm_hour <= 11):
                await message.channel.send("Next round of Pictionary is Friday @ 12:00pm CDT https://s7.gifyu.com/images/ezgif-4-8d916dafcb6b.gif")
            elif (local_time.tm_wday == 4 and local_time.tm_hour >= 12) or (local_time.tm_wday == 5 and local_time.tm_hour <= 21):
                await message.channel.send("Next round of Pictionary is Saturday @ 9:30pm CDT https://s7.gifyu.com/images/ezgif-4-8d916dafcb6b.gif")
            else:
                await message.channel.send("The current time is outside of my programmed times. Try again soon.")
        elif prefix + "bottleflip" in message.content.lower():
            await message.channel.send("Really, a bottle flip? Here, he'll do one https://s7.gifyu.com/images/ezgif-4-7d0b7b5d9c66.gif")
        elif any(x in message.content.lower() for x in t_or_h_matches):
            await message.channel.send("I'm #teamhardwood, but you already know that.")
        #eat food command
        elif message.content.startswith("\U0001F9B4") or message.content.startswith("\U0001F356") or message.content.startswith("\U0001F357") or message.content.startswith("\U0001F969") or message.content.startswith("\U0001F953"):
            await message.channel.send("\U0001F436")
        elif prefix + "playdead" == message.content.lower():
            await client.change_presence(status=discord.Status.invisible, activity=dead_game)
            await asyncio.sleep(1)
            await message.channel.send("https://i.imgur.com/zpGmavE.png")
            await asyncio.sleep(15)
            await client.change_presence(status=discord.Status.online, activity=game)
            print("The bot is ready!")
            await message.channel.send("\U0001F436")
        elif prefix + "fetchitem" == message.content.lower():
            time.sleep(randint(1,20))
            await message.channel.send("\U0001F436" + "\U0001F4A6" + random.choice(fetch_items))
        elif prefix + "fetch" in message.content.lower():
            channel = message.channel
            _, item = message.content.split(maxsplit=1)
            await message.channel.send("\U0001F436" + "\U0001F4A8")
            await asyncio.sleep(randint(1,30))
            await message.channel.send("\U0001F436" + "\U0001F4A6" + item)
##        elif prefix + "emoji" in message.content.lower():
##            channel = message.channel
##            content = message.content
##            print("Test content print: " + content)
##            await channel.send('Hello {.author}!')
##            await message.channel.send(emoji.emojize('Python is :thumbs_up:'))
##
##            def extract_emojis(content):
##                return ''.join(c for c in content if c in emoji.UNICODE_EMOJI)
        
            
        
            
                                        
client.run(TOKEN)
