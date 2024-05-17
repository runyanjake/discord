#PWSBot

Simple Discord bot that does some useful things.

### Running 
Build and run the docker container with a few commands:

`docker stop pwsBot && docker system prune && docker-compose build && docker-compose up -d && docker logs -f pwsBot`

### Functions

##### Echo

`/pws echo [text]`

The bot will echo the text in the channel.

##### Hello World

`/pws helloworld`

Prints "Hello, World!" to the channel.

##### Voice Channel Auto-Provisioning

If a user joins a watched channel, the bot will auto-provision a new voice channel for them and move them to it. Saves on channel clog!

