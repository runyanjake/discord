import re

from commands.echo import echo
from commands.hello_world import hello_world

pws_command_prefix = '/pws '
pws_command_regex = r'/pws (\S+)'
pws_command_with_args_regex = r'/pws \S+(.*)'

async def handle_message(client, message):
    print(message.content)

    #Ignore messages this bot has sent to avoid answering itself.
    if message.author == client.user:
        return

    #Respond only to messages starting with the PWS prefix.
    if message.content.startswith(pws_command_prefix):
        msg = [3]
        msg.append(pws_command_prefix)
        msg.append(re.match(pws_command_regex, message.content)[1])
        msg.append(re.match(pws_command_with_args_regex, message.content)[1])

        command = msg[2]
        args = msg[3]
        print("command: " + command + ", args: " + args)

        match command:
            case 'helloworld':
                if args:
                    print('Command ' + command + ' got unexpected arguments: ' + message.content + '.')
                    await message.author.send('Unexpected arguments for command: `' + message.content + '`. Check list of commands for valid usage.')
                else:
                    await hello_world(message)
            case 'echo': 
                if not args:
                    print('Command ' + command + ' did not specify argument(s): ' + message.content + '.')
                    await message.author.send('Did not specify argument(s) for command: `' + message.content + '`. Check list of commands for valid usage.')
            case _:
                print('Invalid command ' + command + ' received.')
                await message.author.send('Invalid command `' + command + '`. Check list of commands for valid usage.')

