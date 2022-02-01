import json
from tkinter import ttk, filedialog
from tkinter import *


# TODO simplify this to require less function calls

def get_actor():
    return open(filedialog.askopenfilename())


def init_actor():
    token = json.load(get_actor())
    actor = token['actors']['actor.1']
    items = actor['items']
    spells = act_spells(items)
    spell_list = [k for k in spells.keys()]
    spell_name = spell_list[0]
    spell_desc = spells[spell_name]['description']
    return spell_list, spell_name, spell_desc, spells


# Doesn't look like this is used anywhere
# TODO find a usage for this or delete it
def get_list(sp):
    spells_list = [k for k in sp.keys()]
    spells_list.sort()
    return spells_list, sp


def set_desc(sp_list, sp_dict, selection):
    if selection == ():
        pass
    else:
        spell_name = sp_list[selection[0]]
        spell_desc = sp_dict[spell_name]['description']
        return spell_desc


def del_name(itemdict):
    dictname = [key for key in itemdict]
    for key in dictname:
        if key == 'ArmorClass':
            del itemdict[key]['compset']
        else:
            del itemdict[key]['name']
    return itemdict


# I may or may not still need these here
# TODO find a usage or delete these
def act_spells(it):
    sp = del_name({v['name']: v for (k, v) in it.items() if k[:2] == 'sp'})
    return sp


def act_percept(it):
    pe = del_name({v['name']: v for (k, v) in it.items() if k[:2] == 'Pe'})
    return pe


def act_abilities(it):
    ab = del_name({v['name']: v for (k, v) in it.items() if k[:2] == 'ab'})
    return ab


def act_ability_scores(it):
    absc = del_name({v['name']: v for (k, v) in it.items() if k[:2] == 'as'})
    return absc


def act_skills(it):
    sk = del_name({v['name']: v for (k, v) in it.items() if k[:2] == 'sl'})
    return sk


def act_saves(it):
    sv = del_name({v['name']: v for (k, v) in it.items() if k[:2] == 'sv'})
    return sv


def act_armor_class(it):
    ac = del_name({v['compset']: v for (k, v) in it.items() if k[:2] == 'ac'})
    return ac


def act_ancestry(it):
    anc = del_name({v['name']: v for (k, v) in it.items() if k[:2] == 'an'})
    return anc


def gear_armor(it):
    arm = del_name({v['name']: v for (k, v) in it.items() if k[:2] == 'ar'})
    return arm


def act_class_feats(it):
    cf = del_name({v['name']: v for (k, v) in it.items() if k[:2] == 'cl'})
    return cf


def act_deity(it):
    de = del_name({v['name']: v for (k, v) in it.items() if k[:2] == 'de'})
    return de


def act_general_feats(it):
    gf = del_name({v['name']: v for (k, v) in it.items() if k[:2] == 'ft'})
    return gf


def act_skill_feats(it):
    sf = del_name({v['name']: v for (k, v) in it.items() if k[:2] == 'fs'})
    return sf


def gear_weapons(it):
    wp = del_name({v['name']: v for (k, v) in it.items() if k[:2] == 'wp'})
    return wp


def gear_equipment(it):
    eq = del_name({v['name']: v for (k, v) in it.items() if k[:2] == 'gr'})
    return eq


def gear_staves(it):
    stf = del_name({v['name']: v for (k, v) in it.items() if k[:2] == 'sf'})
    return stf


def act_languages(it):
    langs = del_name({v['name']: v for (k, v) in it.items() if k[:2] == 'ln'})
    return langs


def act_heritage(it):
    her = del_name({v['name']: v for (k, v) in it.items() if k[:2] == 'hr'})
    return her


def act_movement(it):
    move = del_name({v['name']: v for (k, v) in it.items() if k[:2] == 'mv'})
    return move


def act_fists(it):
    fists = del_name({v['name']: v for (k, v) in it.items() if k[:2] == 'nw'})
    return fists


def act_focus_pts(it):
    fp = del_name({v['name']: v for (k, v) in it.items() if k[:5] == 'rvFoc'})
    return fp


def act_hero_pts(it):
    hept = del_name({v['name']: v for (k, v) in it.items() if k[:5] == 'rvHer'})
    return hept


def act_hit_pts(it):
    hp = del_name({v['name']: v for (k, v) in it.items() if k[:5] == 'rvHit'})
    return hp

# I don't remember what this is for, but I'm going to leave it here just in case.

# for k, v in spells.items():
#    if re.findall(re.compile(r'\w+\d'), v['spCastingText']) or re.findall(re.compile(r'somatic|verbal|material'),
#                                                                          v['spCastingText']):
#        print(k, re.findall(re.compile(r'reaction|\w+\d'), v['spCastingText']), re.findall(re.compile(
#                r'somatic|verbal|material'), v['spCastingText']))
#    else:
#        print(k, v['spCastingText'])
