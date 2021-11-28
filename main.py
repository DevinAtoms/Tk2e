import json
import pandas as pd
from time import sleep


def itemlookup(items):

    armor = {}
    ancestry = {}
    ability_score = {}
    feats_class = {}
    deity = {}

    for i in items.index:
        match i[:2]:
            case 'Pe':
                print(items[i]['name'])
            case 'sp':
                print(items[i]['name'])
            case 'ab':
                print(items[i]['name'])
            case 'as':
                ability_score = {items[i]['name']: items[i]}
                del ability_score[str(items[i]['name'])]['name']
                print(ability_score)
            case 'sk':
                print(items[i]['name'])
            case 'sv':
                print(items[i]['name'])
            case 'ac':
                print(items[i]['name'])
            case 'an':
                ancestry = {items[i]['name']: items[i]}
                del ancestry[str(items[i]['name'])]['name']
            case 'ar':
                armor = {items[i]['name']: items[i]}
                del armor[str(items[i]['name'])]['name']
            case 'cl':
                feats_class = {items[i]['name']: items[i]}
                del feats_class[str(items[i]['name'])]['name']
            case 'de':
                deity = {items[i]['name']: items[i]}
                del deity[str(items[i]['name'])]['name']
            case 'ft':
                print(items[i]['name'])
            case 'fs':
                print(items[i]['name'])
            case 'wp':
                print(items[i]['name'])
            case 'gr':
                print(items[i]['name'])
            case 'sf':
                print(items[i]['name'])
            case 'ln':
                print(items[i]['name'])
            case 'hr':
                print(items[i]['name'])
            case 'rs':
                print(items[i]['name'])
            case _:
                print(i)
                pass
    return ancestry, armor, ability_score, feats_class, deity

# def itemParse(name, item_type):
# print(str(name)+' '+str(item_type))
# pass


exp_file = open('token.json', encoding="utf8")
token = json.load(exp_file)
tokenItems = pd.Series(token['actors']['actor.1']['items'])

