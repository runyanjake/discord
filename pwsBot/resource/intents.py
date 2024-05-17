import discord

def get_intents():
    intents= discord.Intents.default()
    
    # Specifying a list of enabled (True) intents.
    intents.messages = True
    intents.message_content = True
    intents.voice_states = True

    return intents

