# Sanware Framework MK III - Branch 'Carter-Discord Boilerplate'

# Boilerplate for linking Discord bot with a Carter API. Written by TheMechanic57.

# Load packages.

import os
import nextcord as discord
from carter import *
from dotenv import load_dotenv

intents = discord.Intents.all()
client = discord.Client(intents=intents)

# Load API keys and UIName from .env

load_dotenv()

APIkey = os.getenv("CARTER_API_KEY")

DiscordAPI = os.getenv("DISCORD_API_KEY")

RawUIName = os.getenv("UIName")


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
        ResponseOutput = SendToCarter(sentence, User, APIkey)

        print(message.content)
        await message.reply(f"{ResponseOutput}")
        print(ResponseOutput)

    else:
        pass

client.run(DiscordAPI)
