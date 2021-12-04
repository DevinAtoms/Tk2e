import json


def init_actor():
    jpath = open('token.json', encoding="utf8")
    token = json.load(jpath)
    tokenactor = token['actors']['actor.1']
    tokenitems = tokenactor['items']
    return tokenactor, tokenitems


def del_name(itemdict):
    dictname = [key for key in itemdict]
    for key in dictname:
        if key == 'ArmorClass':
            del itemdict[key]['compset']
        else:
            del itemdict[key]['name']
    return itemdict


actor, items = init_actor()


perception = del_name({v['name']: v for (k, v) in items.items() if k[:2] == 'Pe'})
spells = del_name({v['name']: v for (k, v) in items.items() if k[:2] == 'sp'})
abilities = del_name({v['name']: v for (k, v) in items.items() if k[:2] == 'ab'})
abilityScores = del_name({v['name']: v for (k, v) in items.items() if k[:2] == 'as'})
skills = del_name({v['name']: v for (k, v) in items.items() if k[:2] == 'sl'})
saves = del_name({v['name']: v for (k, v) in items.items() if k[:2] == 'sv'})
armorClass = del_name({v['compset']: v for (k, v) in items.items() if k[:2] == 'ac'})
ancestry = del_name({v['name']: v for (k, v) in items.items() if k[:2] == 'an'})
armor = del_name({v['name']: v for (k, v) in items.items() if k[:2] == 'ar'})
classFeats = del_name({v['name']: v for (k, v) in items.items() if k[:2] == 'cl'})
deity = del_name({v['name']: v for (k, v) in items.items() if k[:2] == 'de'})
generalFeats = del_name({v['name']: v for (k, v) in items.items() if k[:2] == 'ft'})
skillFeats = del_name({v['name']: v for (k, v) in items.items() if k[:2] == 'fs'})
weapons = del_name({v['name']: v for (k, v) in items.items() if k[:2] == 'wp'})
gear = del_name({v['name']: v for (k, v) in items.items() if k[:2] == 'gr'})
staves = del_name({v['name']: v for (k, v) in items.items() if k[:2] == 'sf'})
languages = del_name({v['name']: v for (k, v) in items.items() if k[:2] == 'ln'})
heritage = del_name({v['name']: v for (k, v) in items.items() if k[:2] == 'hr'})
movement = del_name({v['name']: v for (k, v) in items.items() if k[:2] == 'mv'})
fists = del_name({v['name']: v for (k, v) in items.items() if k[:2] == 'nw'})
focusPoints = del_name({v['name']: v for (k, v) in items.items() if k[:5] == 'rvFoc'})
heroPoints = del_name({v['name']: v for (k, v) in items.items() if k[:5] == 'rvHer'})
hitPoints = del_name({v['name']: v for (k, v) in items.items() if k[:5] == 'rvHit'})
