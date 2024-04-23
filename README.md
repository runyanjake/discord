# discord
Some assorted discord bots.

### Env Setup

Env creation: `python3.11 -m venv env`, `source env/bin/activate`

Requirements: `pip install -r requirements.txt`

### Discord Setup

`https://discord.com/developers/applications`

`New Application > Create`, fill out the information. 

Copy bot's token or regenerate it from the main page. Place this in a file called `token.json` in the root directory here or modify `resource/credentials.py` to find it:

`resource/credentials.py`:
```
{
    "token":"AAAAAAAAAAAAAA..."
}
```

If you need to configure permissions for the bot itself, that happens in the `Bot` tab. Can be done later.

For now, go to `OAuth2 > Oauth2 URL Generator` and select Bot with the desired permissions. Can be done later.

Invite bot to server using the url generated above. I've set the redirect URL to `https://github.com/runyanjake/discord` for after users authenticate with OAuth.

