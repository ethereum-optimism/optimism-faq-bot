import os
import time
from dotenv import load_dotenv

import wit
import discord


from responses import response, greetings, appreciation
from random import choice

load_dotenv()
DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")
WIT_ACCESS_TOKEN = os.getenv("WIT_ACCESS_TOKEN")

discord_client = discord.Client()
wit_client = wit.Wit(WIT_ACCESS_TOKEN)

@discord_client.event
async def on_message(message):
    if message.author == discord_client.user:
        time.sleep(0.3)
        await message.edit(suppress=True)
        return

    intents = wit_client.message(message.content)["intents"]
    if len(intents) == 0:
        return
    
    intent = intents[0]["name"]
    greeting = choice(greetings) if intent not in ["helpNeeded", "priceTalk", "appreciation"] else ""
    print(f'User asking a question. Intent: {intent}')
    await message.channel.send(f"{greeting} {message.author.mention} {response[intent] if intent != 'appreciation' else choice(appreciation)}")

discord_client.run(DISCORD_TOKEN)


