# discord
Some assorted discord bots.

### Env Setup

Env creation: `python3.11 -m venv env`, `source env/bin/activate`

Requirements: `pip install -r requirements.txt`

### Discord Setup

`https://discord.com/developers/applications`

`New Application > Create`, fill out the information. 

Copy bot's token or regenerate it from the main page. Place this in a file called `token.json` in the root directory here or modify `resource/credentials.py` to find it:

`token.json`:
```
{
    "token":"AAAAAAAAAAAAAA..."
}
```

Go to `Bot` tab to configure permissions. In my experience, the `Requires OAuth2 Code Grant` toggle broke my ability to add the bot to servers, so avoiding that's probably a good idea for local dev.
In general, if there is a mismatch between the scopes and permissions assigned to the bot, it won't be able to be added to the server. 
Additionally you have to grant the bot the right intents. See how this is done in `pwsBot/resources/intents.py`. Also see `https://discordpy.readthedocs.io/en/stable/api.html`.

Go to `OAuth2 > Oauth2 URL Generator` and select Bot with the desired permissions. Can modify these, generate a new invite link, and re-add to the server again later.

I am currently using the following Scopes/Permissions:

Scopes
- bot

Permissions
- administrator

Invite bot to server using the url generated above. I've set the redirect URL to `https://github.com/runyanjake/discord` for after users authenticate with OAuth.

