import os
import time
from dotenv import load_dotenv

import wit
import discord

# Import necessary responses and greetings from a module named responses
from responses import response, greetings, appreciation
from random import choice

# Load environment variables from a .env file
load_dotenv()
# Retrieve Discord token and Wit access token from environment variables
DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")
WIT_ACCESS_TOKEN = os.getenv("WIT_ACCESS_TOKEN")

# Initialize the Discord client and Wit client
discord_client = discord.Client()
wit_client = wit.Wit(WIT_ACCESS_TOKEN)

@discord_client.event
async def on_message(message):
    # Ignore messages from the bot itself to prevent infinite loops
    if message.author == discord_client.user:
        time.sleep(0.3) # Pause for a short time to avoid rate limiting
        await message.edit(suppress=True) # Edit the message to suppress it
        return

    # Process the message content with Wit to extract intents
    intents = wit_client.message(message.content)["intents"]
    if len(intents) == 0:
        return # If no intents are detected, ignore the message
    
    # Extract the first intent from the list of intents detected
    intent = intents[0]["name"]
    # Choose a greeting based on the intent, except for certain intents where no greeting is needed
    greeting = choice(greetings) if intent not in ["helpNeeded", "priceTalk", "appreciation"] else ""
    print(f'User asking a question. Intent: {intent}') # Log the intent for debugging
    
    # Construct and send the response based on the intent
    await message.channel.send(f"{greeting} {message.author.mention} {response[intent] if intent != 'appreciation' else choice(appreciation)}")

# Run the Discord client with the token
discord_client.run(DISCORD_TOKEN)



