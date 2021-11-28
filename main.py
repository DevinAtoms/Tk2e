import json
import pandas as pd


def initActor():
    exp_file = open('token.json', encoding="utf8")
    token = json.load(exp_file)
    return token['actors']['actor.1']


items = pd.Series(initActor()['items'])
name = initActor()['name']
print(pd.Series(initActor())['gameValues'])
#alignment = initActor()['alignment']


def itemtodict(key):
    itemtype = {items[key]['name']: items[key]}
    del itemtype[str(items[key]['name'])]['name']
    return itemtype


for i in items.index:
    match i[:2]:
        case 'Pe':
            perception = i
        case 'sp':
            spells = itemtodict(i)
        case 'ab':
            abilities = itemtodict(i)
        case 'as':
            ability_score = itemtodict(i)
        case 'sk':
            skills = itemtodict(i)
        case 'sv':
            saves = itemtodict(i)
        case 'ac':
            armor_class = i
        case 'an':
            ancestry = itemtodict(i)
        case 'ar':
            armor = itemtodict(i)
        case 'cl':
            classFeats = itemtodict(i)
        case 'de':
            deity = itemtodict(i)
        case 'ft':
            generalFeats = itemtodict(i)
        case 'fs':
            skillFeats = itemtodict(i)
        case 'wp':
            weapons = itemtodict(i)
        case 'gr':
            gear = itemtodict(i)
        case 'sf':
            staves = itemtodict(i)
        case 'ln':
            languages = itemtodict(i)
        case 'hr':
            heritage = itemtodict(i)
        case 'rv':
            match i[:4]:
                case 'rvFo':
                    focusPoints = i
                case 'rvHe':
                    heroPoints = i
                case _:
                    healthPoints = i
        case 'mv':
            movespeed = i
        case 'nw':
            fists = i
        case _:
            print(i)
            pass
