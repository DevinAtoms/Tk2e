import json
from tkinter import Tk, filedialog, StringVar
from pathlib import Path
import os


def init_actor():
    jpath = filedialog.askopenfilename(initialdir=str(Path.home()))
    token = json.load(os.path.basename(jpath))
    tokenactor = token['actors']['actor.1']
    tokenitems = actor['items']
    return tokenactor, tokenitems


def del_name(itemdict):
    dictname = [key for key in itemdict]
    for key in dictname:
        del itemdict[key]['name']
    return itemdict


actor, items = init_actor()

rv = {k: v for (k, v) in items.items() if k[:2] == 'rv'}
perception = {v['name']: v for (k, v) in items.items() if k[:2] == 'Pe'}
spells = del_name({v['name']: v for (k, v) in items.items() if k[:2] == 'sp'})
abilities = del_name({v['name']: v for (k, v) in items.items() if k[:2] == 'ab'})
abilityScores = del_name({v['name']: v for (k, v) in items.items() if k[:2] == 'as'})
skills = del_name({v['name']: v for (k, v) in items.items() if k[:2] == 'sl'})
saves = del_name({v['name']: v for (k, v) in items.items() if k[:2] == 'sv'})
armorClass = del_name({k: v for (k, v) in items.items() if k[:2] == 'ac'})
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
focusPoints = del_name({v['name']: v for (k, v) in rv.items() if k[:4] == 'rvFo'})
heroPoints = del_name({v['name']: v for (k, v) in rv.items() if k[:4] == 'rvHe'})
hitPoints = del_name({v['name']: v for (k, v) in rv.items() if k[:4] == 'rvHi'})
