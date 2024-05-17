import logging
import sys

VOICE_MANAGED_CHANNELS = ['bot-test-voice']

provisioned_channels = []

log_format = '%(asctime)s %(levelname)s\t%(filename)s %(message)s'
logging.basicConfig(stream=sys.stdout, level=logging.DEBUG, format=log_format)

async def handle_voice_event(member, before, after):
    if after.channel and before.channel != after.channel and after.channel.name in VOICE_MANAGED_CHANNELS:
        # User has joined a managed voice channel that is not yet being tracked.
        if before.channel:
            logging.debug('Member ' + str(member.name) + ' moved from channel ' + str(before.channel.name) + ' to watched channel ' + str(after.channel.name) + '.')
        else:
            logging.debug('Member ' + str(member.name) + ' joined watched channel ' + str(after.channel.name) + '.')
        
        guild = member.guild
        new_channel_name = f"{after.channel.name} ({member.name})"
        new_channel = await guild.create_voice_channel(new_channel_name)
        
        provisioned_channels.append(new_channel_name)
        logging.info('Created and tracked new voice channel: ' + str(new_channel_name))
        logging.debug('Tracked channels: ' + str(provisioned_channels))
        
        await(member.move_to(new_channel))
        logging.info('Moved user ' + str(member.name) + ' from channel ' + str(after.channel.name) + ' to channel ' + str(new_channel.name) + '.')
    elif before.channel and not before.channel.members and before.channel.name in provisioned_channels:
        # User was the last one to leave a tracked channel.
        logging.info('User ' + str(member.name) + ' was the last to leave tracked channel ' + str(before.channel.name) + '.')
        
        logging.info('Removing empty tracked voice channel: ' + str(before.channel.name) + '.')
        await before.channel.delete()
            
        provisioned_channels.remove(before.channel.name)
        logging.debug('Tracked channels: ' + str(provisioned_channels))

