import data
import base64
import requests

def render_image(url):
    a = requests.get(url)
    base_content = base64.b64encode(a.content)
    return 'data:image/png;base64,'+base_content.decode()

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
    hero_portrait_image = render_image('https://overwatch.nosdn.127.net/images/hero/{}/career-portrait.png'.format(profile['player']['masthead']))
    try:
        level_star = render_image('https://overwatch.nosdn.127.net/images/'+profile['player']['portraitFrameIcon'])
    except:
        level_star = ''
    try:
        win_round = int(profile['careerStats']['unranked']['stats']['0x02E00000FFFFFFFF']['0x08600000000003F5'] + int(
            profile['careerStats']['ranked']['stats']['0x02E00000FFFFFFFF']['0x08600000000003F5']))
        defeat_round = int(
            profile['careerStats']['unranked']['stats']['0x02E00000FFFFFFFF']['0x086000000000042E']) + int(
            profile['careerStats']['ranked']['stats']['0x02E00000FFFFFFFF']['0x086000000000042E'])
        win_rate = str(int(win_round / (win_round + defeat_round) * 100)) + '%'
        # /data/careerStats/unranked/stats/0x02E00000FFFFFFFF/0x086000000000042E
        # /data/careerStats/ranked/stats/0x02E00000FFFFFFFF/0x086000000000042E
        kill = profile['careerStats']['unranked']['stats']['0x02E00000FFFFFFFF']['0x0860000000000025'] + \
               profile['careerStats']['ranked']['stats']['0x02E00000FFFFFFFF']['0x0860000000000025']
        # /data/careerStats/ranked/stats/0x02E00000FFFFFFFF/0x0860000000000025
        dead = profile['careerStats']['unranked']['stats']['0x02E00000FFFFFFFF']['0x0860000000000029'] + \
               profile['careerStats']['ranked']['stats']['0x02E00000FFFFFFFF']['0x0860000000000029']
        # /data/careerStats/ranked/stats/0x02E00000FFFFFFFF/0x0860000000000029
        special1 = profile['careerStats']['unranked']['stats']['0x02E0000000000068']['0x0860000000000229'] + \
                   profile['careerStats']['ranked']['stats']['0x02E0000000000068']['0x0860000000000229']
        # /data/careerStats/unranked/stats/0x02E0000000000068/0x0860000000000229
        special2 = profile['careerStats']['unranked']['stats']['0x02E0000000000068']['0x086000000000022D'] + \
                   profile['careerStats']['ranked']['stats']['0x02E0000000000068']['0x086000000000022D']
        # /data/careerStats/ranked/stats/0x02E0000000000068/0x086000000000022D
        tr = profile['player']['ranked']['tank']['level']
        cr = profile['player']['ranked']['damage']['level']
        nr = profile['player']['ranked']['support']['level']
    except:
        win_round = int(profile['careerStats']['unranked']['stats']['0x02E00000FFFFFFFF']['0x08600000000003F5'])
        defeat_round = int(
            profile['careerStats']['unranked']['stats']['0x02E00000FFFFFFFF']['0x086000000000042E'])
        win_rate = str(int(win_round / (win_round + defeat_round) * 100)) + '%'
        # /data/careerStats/unranked/stats/0x02E00000FFFFFFFF/0x086000000000042E
        # /data/careerStats/ranked/stats/0x02E00000FFFFFFFF/0x086000000000042E
        kill = profile['careerStats']['unranked']['stats']['0x02E00000FFFFFFFF']['0x0860000000000025']
        # /data/careerStats/ranked/stats/0x02E00000FFFFFFFF/0x0860000000000025
        dead = profile['careerStats']['unranked']['stats']['0x02E00000FFFFFFFF']['0x0860000000000029']
        # /data/careerStats/ranked/stats/0x02E00000FFFFFFFF/0x0860000000000029
        special1 = profile['careerStats']['unranked']['stats']['0x02E0000000000068']['0x0860000000000229']
        # /data/careerStats/unranked/stats/0x02E0000000000068/0x0860000000000229
        special2 = profile['careerStats']['unranked']['stats']['0x02E0000000000068']['0x086000000000022D']
        # /data/careerStats/ranked/stats/0x02E0000000000068/0x086000000000022D
        try:
            tr = profile['player']['ranked']['tank']['level']
        except:
            tr = '????'
        try:
            cr = profile['player']['ranked']['damage']['level']
        except:
            cr = '????'
        try:
            nr = profile['player']['ranked']['damage']['level']
        except:
            nr = '????'
    data_dict = {
        'length1':length_1,
        'length2':length_2,
        'length3':length_3,
        'length12':length_1+length_2,
        'endorsementlevel':profile['player']['endorsement']['level'],
        'endorsementicon':get_svg_icon(profile['player']['endorsement']['level']),
        'playername':player_name.upper(),
        'level':profile['player']['level'],
        'trating':tr,
        'crating':cr,
        'nrating':nr,
        'heroportraitimage':hero_portrait_image,
        'avatar':render_image('https://overwatch.nosdn.127.net/images/'+profile['player']['portraitAvatar']),
        'winrate':win_rate,
        'winround':win_round,
        'kill':kill,
        'dead':dead,
        'special1':special1,
        'special2':special2,
        'levelimg':render_image('https://overwatch.nosdn.127.net/images/'+profile['player']['portraitFrame']),
        'levelstarimg':level_star
    }

    output = data.svg_template.format(**data_dict)
    return output

