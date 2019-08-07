import json
import getpass

from controller.bot import EchoBot
from cred.config import username_{suffix}

cookies = {}

try:
	with open('sessions/session-penwisut.json', 'r') as f:
		cookies = json.load(f)
except:
	pass

client = EchoBot(username_{suffix}, getpass.getpass(prompt='Password: '), session_cookies=cookies)

with open('sessions/session-penwisut.json','w') as f:
	json.dump(client.getSession(), f)

client.listen()
