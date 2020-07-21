import data

def get_svg_icon(level:int):
    if(level==0):
        return data.svg_icon_0
    elif(level==1):
        return data.svg_icon_1
    elif(level==2):
        return data.svg_icon_2
    elif(level==3):
        return data.svg_icon_3
    elif(level==4):
        return data.svg_icon_4
    else:
        return data.svg_icon_5

def render(profile):
    circle_c = 49.5
    length_1 = profile['player']['endorsement']['shotcaller']/profile['player']['endorsement']['total'] * circle_c
    length_2 = profile['player']['endorsement']['teammate']/profile['player']['endorsement']['total'] * circle_c
    length_3 = profile['player']['endorsement']['sportsmanship']/profile['player']['endorsement']['total'] * circle_c
    icon_name = "svg_icon_"+str(profile['player']['endorsement']['level'])
    player_name = profile['player']['displayName'].split('#')[0]
    hero_portrait_image = 'https://overwatch.nosdn.127.net/images/hero/{}/career-portrait.png'.format(profile['player']['masthead'])
    data_dict = {
        '1length':length_1,
        '2length':length_2,
        '3length':length_3,
        '12length':length_1+length_2,
        'endorsementlevel':profile['player']['endorsement']['level'],
        'endorsementicon':get_svg_icon(profile['player']['endorsement']['level']),
        'playername':player_name,
        'level':profile['player']['level'],
        'trating':profile['ranked']['tank']['level'],
        'crating':profile['ranked']['damage']['level'],
        'nrating':profile['ranked']['support']['level'],
        'heroportraitimage':hero_portrait_image,
        'avatar':'https://overwatch.nosdn.127.net/images/'+profile['player']['portraitAvatar'],
        'winrate':'',
        'winround':int(profile['careerStats']['unranked']['0x02E00000FFFFFFFF']['0x08600000000003F5']+int(profile['careerStats']['ranked']['0x02E00000FFFFFFFF']['0x08600000000003F5'])),
        'kill':'',
        'dead':'',
        'special1':'',
        'special2':'',
    }

