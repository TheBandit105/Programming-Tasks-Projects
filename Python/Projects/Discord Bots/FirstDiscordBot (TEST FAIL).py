import discord
import random

# Token removed as this is private to the owner of the bot. 
TOKEN = ''

intents = discord.Intents.all()
client = discord.Client(command_prefix='!', intents=intents)

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    username = str(message.author).split('#')[0]
    user_message = str(message.content)
    channel = str(message.channel.name)
    print(username + ': ' + user_message + ' ' + channel)

    if message.author == client.user:
        return

    if message.channel.name == 'general':
        if user_message.lower().startswith('hello'):
            await message.channel.send('Hello ' + username + '!')
            return
        elif user_message.lower().startswith('bye'):
            await message.channel.send(f'See you later {username}!')
            return
        elif user_message.lower().startswith('!random'):
            response = f'This is your random number: {random.randrange(1000000)}'
            await message.channel.send(response)
            return

    if user_message.lower().startswith('!anywhere'):
        await message.channel.send('This can be used anywhere!')
        return

client.run(TOKEN)

    
