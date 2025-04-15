from typing import Final
from discord import Intents, Client, Message
import os
from dotenv import load_dotenv
# from Responses import get_response

load_dotenv()

intents = Intents.default()
intents.message_content = True 
client = Client(intents=intents)

async def send_message(message: Message, user_message: str) -> None:
    if not user_message:
        print('Message was empty probably due to intents being improperly or incorrectly enabled.')
        return
    
    if is_private := user_message[0] == '?':
        user_message = user_message[1:]
        



@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$hello'):
        await message.channel.send('Hello!')

client.run(os.getenv("DISCORD_BOT_TOKEN"))
