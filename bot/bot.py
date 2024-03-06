"""
This script is a Discord bot that uses the Wit.ai API to understand user messages and respond accordingly.
It greets users, provides responses based on the intent of their messages, and handles specific intents like help, price talk, and appreciation.
"""

import os
import time
from dotenv import load_dotenv

import wit
import discord

from responses import response, greetings, appreciation
from random import choice

# Load environment variables
load_dotenv()
DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")
WIT_ACCESS_TOKEN = os.getenv("WIT_ACCESS_TOKEN")

# Initialize Discord and Wit.ai clients
discord_client = discord.Client()
wit_client = wit.Wit(WIT_ACCESS_TOKEN)

@discord_client.event
async def on_message(message):
    """
    Handles incoming messages from Discord, processes them with Wit.ai, and sends appropriate responses.

    Parameters:
    message (discord.Message): The message object received from Discord.
    """
    # Ignore messages from the bot itself
    if message.author == discord_client.user:
        time.sleep(0.3)
        await message.edit(suppress=True)
        return

    # Process the message with Wit.ai
    intents = wit_client.message(message.content)["intents"]
    if len(intents) == 0:
        return
    
    # Extract the first intent and determine the appropriate response
    intent = intents[0]["name"]
    greeting = choice(greetings) if intent not in ["helpNeeded", "priceTalk", "appreciation"] else ""
    print(f'User asking a question. Intent: {intent}')
    # Respond based on the intent, with special handling for appreciation
    await message.channel.send(f"{greeting} {message.author.mention} {response[intent] if intent != 'appreciation' else choice(appreciation)}")

# Run the Discord client
discord_client.run(DISCORD_TOKEN)

# TODO: Implement error handling for Wit.ai API calls
# TODO: Add more intents and responses
