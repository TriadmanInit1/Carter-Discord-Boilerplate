# Sanware Framework MK III - Branch 'Carter-Discord Boilerplate'

# Boilerplate for linking Discord bot with a Carter API. Written by TheMechanic57.

# Load packages.

import os
import nextcord as discord
from carter import *

intents = discord.Intents.all()
client = discord.Client(intents=intents)

APIkey = "REPLACE THIS WITH YOUR CARTER AGENT'S API."
RawUIName = "REPLACE THIS WITH THE NAME OF YOUR CARTER AGENT."
DiscordAPI = "REPLACE THIS WITH YOUR DISCORD BOT'S API. GET IT FROM DISCORD DEVELOPER WEBSITE."

# Program

@client.event
async def on_message(message):
    # Script is below.

    if message.author == client.user:
        return

    User = message.author
    sentence = message.content
    sentence = sentence.lower()
    UIName = RawUIName.lower()

    if UIName in sentence:
        SendToCarter(sentence, User, APIkey)
        with open('CarterResponse.txt') as f:
            ResponseOutput = f.read()

        print(message.content)
        await message.channel.send(f"{ResponseOutput}")
        print(ResponseOutput)
        os.remove("CarterResponse.txt")
    else:
        pass

client.run(DiscordAPI)
