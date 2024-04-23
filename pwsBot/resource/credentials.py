import json
import sys

TOKEN = 'token'

def get_token():
    try:
        with open(file_path, 'r') as file:
            data = json.load(file)
            if TOKEN in data:
                return data[TOKEN]
            else:
                print("Bot token file missing " + str(TOKEN) + " field. See README.")
    except FileNotFoundError:
        print("No bot token file. See README.")
    except json.JSONDecodeError:
        print("Invalid JSON format for bot token file. See README.")
        
    sys.exit(1)
