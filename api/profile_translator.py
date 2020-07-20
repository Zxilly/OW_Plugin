import json

with open('profile.json','r+') as f:
    profile = json.loads(f.read())

with open('translated_gamedata.json','r+') as f:
    gamedata = json.loads(f.read())

data = profile["data"]
