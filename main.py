import json


def initActor():
    exp_file = open('token.json', encoding="utf8")
    token = json.load(exp_file)
    return token['actors']['actor.1']['items']


def delName(itemdict):
    dictname = [key for key in itemdict]
    for key in dictname:
        del itemdict[key]['name']
    return itemdict


items = initActor()

rv = {k: v for (k, v) in items.items() if k[:2] == 'rv'}
perception = {v['name']: v for (k, v) in items.items() if k[:2] == 'Pe'}
spells = delName({v['name']: v for (k, v) in items.items() if k[:2] == 'sp'})
abilities = delName({v['name']: v for (k, v) in items.items() if k[:2] == 'ab'})
abilityScores = delName({v['name']: v for (k, v) in items.items() if k[:2] == 'as'})
skills = delName({v['name']: v for (k, v) in items.items() if k[:2] == 'sl'})
saves = delName({v['name']: v for (k, v) in items.items() if k[:2] == 'sv'})
armorClass = delName({k: v for (k, v) in items.items() if k[:2] == 'ac'})
ancestry = delName({v['name']: v for (k, v) in items.items() if k[:2] == 'an'})
armor = delName({v['name']: v for (k, v) in items.items() if k[:2] == 'ar'})
classFeats = delName({v['name']: v for (k, v) in items.items() if k[:2] == 'cl'})
deity = delName({v['name']: v for (k, v) in items.items() if k[:2] == 'de'})
generalFeats = delName({v['name']: v for (k, v) in items.items() if k[:2] == 'ft'})
skillFeats = delName({v['name']: v for (k, v) in items.items() if k[:2] == 'fs'})
weapons = delName({v['name']: v for (k, v) in items.items() if k[:2] == 'wp'})
gear = delName({v['name']: v for (k, v) in items.items() if k[:2] == 'gr'})
staves = delName({v['name']: v for (k, v) in items.items() if k[:2] == 'sf'})
languages = delName({v['name']: v for (k, v) in items.items() if k[:2] == 'ln'})
heritage = delName({v['name']: v for (k, v) in items.items() if k[:2] == 'hr'})
movement = delName({v['name']: v for (k, v) in items.items() if k[:2] == 'mv'})
fists = delName({v['name']: v for (k, v) in items.items() if k[:2] == 'nw'})
focusPoints = delName({v['name']: v for (k, v) in rv.items() if k[:4] == 'rvFo'})
heroPoints = delName({v['name']: v for (k, v) in rv.items() if k[:4] == 'rvHe'})
hitPoints = delName({v['name']: v for (k, v) in rv.items() if k[:4] == 'rvHi'})
