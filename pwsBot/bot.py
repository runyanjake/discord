import discord
import sys

from resource.credentials import get_token

PWS_command_prefix = '/pws '

client = discord.Client()
client_token = get_token()

@client.event
async def on_ready():
    print('Logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith(PWS_command_prefix):
        print('Received Command ' + str(message.content))
        await message.channel.send('Message Received!')

print("Authenticating with token " + str(client_token))
client.run(os.getenv(client_token))
