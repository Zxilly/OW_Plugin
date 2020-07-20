import json

def merge(dict1, dict2):
    res = {**dict1, **dict2}
    return res

with open('gamedata.json','r+',encoding='utf-8') as f:
    gamedata_dict = json.loads(f.read())

# print(gamedata_dict)

# @pargm id:object

translate_dict = {}

for achievements_type in gamedata_dict['achievements']:
    achievements_type_name = achievements_type['displayName']
    # print(achievements_type)
    for achievements in achievements_type['achievements']:
        # rint(achievements)
        achievements['type'] = achievements_type_name
        translate_dict[achievements['id']] = achievements

translate_dict = merge(translate_dict,gamedata_dict['stats'])
translate_dict = merge(translate_dict,gamedata_dict['heroesMap'])

for one in gamedata_dict['heroComparison']:
    translate_dict[one['id']] = one

with open('translated_gamedata.json','w+') as f:
    f.write(json.dumps(translate_dict))