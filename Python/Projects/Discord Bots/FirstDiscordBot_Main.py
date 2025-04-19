from typing import Final
from discord import Intents, Client, Message
import os
from dotenv import load_dotenv
from Responses import get_response

load_dotenv()

intents = Intents.default()
intents.message_content = True 
client = Client(intents=intents)

async def send_message(message: Message, user_message: str) -> None:
    if not user_message:
        print('Message was empty probably due to intents being improperly or incorrectly enabled.')
        return
    
    if is_private := user_message[0] == 'p' or 'P':
        user_message = user_message[1:]

    try:
        response: str = get_response(user_message)
        await message.author.send(response) if is_private else await message.channel.send(response)
    except Exception as error:
        print("An error occurred, please check and try again.")    

@client.event
async def on_ready():
    print('{0.user} is now active'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    username: str = str(message.author)
    user_message: str = message.content
    channel: str = str(message.channel)

    print(f'[{channel}] {username}: "{user_message}"')
    await send_message(message, user_message)


def main():
    client.run(os.getenv("DISCORD_BOT_TOKEN"))

if __name__ == '__main__':
    main()
