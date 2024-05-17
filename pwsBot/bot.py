import discord
import logging
import sys

from commands.message_handler import handle_message

from resource.credentials import get_token
from resource.intents import get_intents

from voice.voice_event_handler import handle_voice_event

intents = get_intents()
client = discord.Client(intents=intents)
client_token = get_token('resource/token.json')

log_format = '%(asctime)s %(levelname)s\t%(filename)s %(message)s'
logging.basicConfig(stream=sys.stdout, level=logging.DEBUG, format=log_format)

@client.event
async def on_ready():
    logging.info('Logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    await handle_message(client, message)

@client.event
async def on_voice_state_update(member, before, after):
    await handle_voice_event(member, before, after)

client.run(client_token)

