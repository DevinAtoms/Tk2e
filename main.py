import json
from tkinter import Tk, filedialog, StringVar
from pathlib import Path

global items

def initActor(jsonfile):
    token_file = filedialog.askopenfilename(initialdir=str(Path.home()))
    token = json.load(token_file)
    actor = token['actors']['actor.1']
    items = actor['items']
    return actor, items


def delName(itemdict):
    dictname = [key for key in itemdict]
    for key in dictname:
        del itemdict[key]['name']
    return itemdict


actor, items = initActor()

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
