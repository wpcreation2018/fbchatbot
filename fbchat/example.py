import json
import base64
from controller.bot import EchoBot

from cred.config import username, password

_user = username
_secr = base64.b64decode(password)
_pass = _secr.decode('utf-8')

cookies = {}

try:
	with open('sessions/session.json', 'r') as f:
		cookies = json.load(f)
except:
	pass

client = EchoBot(_user, _pass, session_cookies=cookies)

with open('sessions/session.json','w') as f:
	json.dump(client.getSession(), f)

client.listen()