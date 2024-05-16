import json
import logging
import sys

TOKEN = 'token'

log_format = '%(asctime)s %(levelname)s\t%(filename)s %(message)s'
logging.basicConfig(stream=sys.stdout, level=logging.DEBUG, format=log_format)

def get_token(file_path):
    try:
        with open(file_path, 'r') as file:
            data = json.load(file)
            if TOKEN in data:
                return data[TOKEN]
            else:
                logging.error("Bot token file missing " + str(TOKEN) + " field. See README.")
    except FileNotFoundError:
        logging.error("No bot token file. See README.")
    except json.JSONDecodeError:
        logging.error("Invalid JSON format for bot token file. See README.")
        
    sys.exit(1)
