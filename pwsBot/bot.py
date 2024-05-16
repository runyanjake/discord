import discord

from resource.credentials import get_token
from resource.intents import get_intents

from commands.message_handler import handle_message

intents = get_intents()
client = discord.Client(intents=intents)
client_token = get_token('resource/token.json')

@client.event
async def on_ready():
    print('Logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    await handle_message(client, message)

client.run(client_token)
