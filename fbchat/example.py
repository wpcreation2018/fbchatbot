import json
import getpass

from controller.bot import EchoBot
from cred.config import username_{suffix}

cookies = {}

try:
	with open('sessions/session-{suffix}.json', 'r') as f:
		cookies = json.load(f)
except:
	pass

client = EchoBot(username_{suffix}, {password_here}, session_cookies=cookies)

with open('sessions/session-{suffix}.json','w') as f:
	json.dump(client.getSession(), f)

client.listen()
