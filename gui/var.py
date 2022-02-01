import tkinter as tk
import json
from abc import ABC
from collections.abc import MutableMapping


# TODO Revisit this

class JSONexport:
    def __init__(self, parent, jsonfile):

        self.parent = parent

        if jsonfile:
            jsonvalue = open(jsonfile).read()
            self.jsonvalue = json.loads(jsonvalue)
            self.actor = self.jsonvalue['actors']['actor.1']
            self.items = self.actor['items']
            self.spells = ItemDict({v['name']: v for (k, v) in self.items.items() if k[:2] == 'sp'})
            self.gear = ItemDict({v['name']: v for (k, v) in self.items.items() if k[:2] == 'gr'})
            self.weapons = ItemDict({v['name']: v for (k, v) in self.items.items() if k[:2] == 'wp'})
            self.general_feats = ItemDict({v['name']: v for (k, v) in self.items.items() if k[:2] == 'ft'})
            self.class_ = ItemDict({v['name']: v for (k, v) in self.items.items() if k[:2] == 'cl'})
            self.skill_feats = ItemDict({v['name']: v for (k, v) in self.items.items() if k[:2] == 'fs'})
            self.ability_scores = {v['name']: v for (k, v) in self.items.items() if k[:2] == 'as'}
            self.perception = {v['name']: v for (k, v) in self.items.items() if k[:2] == 'Pe'}
            self.focus_pts = {v['name']: v for (k, v) in self.items.items() if k[:5] == 'rvFoc'}
            self.hero_pts = {v['name']: v for (k, v) in self.items.items() if k[:5] == 'rvHer'}
            # self.hit_pts = ItemDict({v['name']: v for (k, v) in self.items.items() if k[:5] == 'rvHit'})
            self.hit_pts = ItemDict({'Hit Points': {v['name']: v for (k, v) in self.items.items() if k[:5] == 'rvHit'}})
            self.hit_pts.data['Hit Points'] = self.hit_pts.data['Hit Points']['rvMax']
            self.saves = {v['name']: v for (k, v) in self.items.items() if k[:2] == 'sv'}
            self.armor_class = {v['compset']: v for (k, v) in self.items.items() if k[:2] == 'ac'}
            self.move_speed = {v['name']: v for (k, v) in self.items.items() if k[:2] == 'mv'}

        else:
            self.jsonvalue = None

    def __call__(self, *args, **kwargs):
        if 'key' in kwargs:
            if 'dump' in kwargs:
                return json.dumps(self.actor, indent=kwargs['dump'])
            else:
                return self.actor[kwargs['key']]
        else:
            return self.actor

    @staticmethod
    def del_name(itemdict):
        dictname = [k for k in itemdict]
        for key in dictname:
            del itemdict[key]['name']
            del itemdict[key]['compset']
        return itemdict

    def read_json(self, value):
        self.jsonvalue = json.loads(value)

    def get_stringvar(self, **kwargs):
        if 'key' in kwargs:
            string = self.actor[kwargs['key']]
            return tk.StringVar(value=string)
        else:
            string = self.actor
            return tk.StringVar(value=string)

    def get_keys(self):
        return self.actor['items'].keys()

    def spells(self):
        return self.spells.listnames(True)

    def gear(self):
        return self.gear.listnames(True)

    def weapons(self):
        return self.weapons.listnames(True)

    def armor(self):
        self.armor = {v['name']: v for (k, v) in self.items() if k[:2] == 'ar'}
        return self.armor

    def staves(self):
        staves = {v['name']: v for (k, v) in self.items() if k[:2] == 'sf'}
        return staves

    def abilities(self):
        skills = {v['name']: v for (k, v) in self.items() if k[:2] == 'sl'}
        abilities = {v['name']: v for (k, v) in self.items() if k[:2] == 'ab'}
        fists = {v['name']: v for (k, v) in self.items() if k[:2] == 'nw'}

    def background(self):
        ancestry = {v['name']: v for (k, v) in self.items() if k[:2] == 'an'}
        de = {v['name']: v for (k, v) in self.items() if k[:2] == 'de'}
        languages = {v['name']: v for (k, v) in self.items() if k[:2] == 'ln'}
        heritage = {v['name']: v for (k, v) in self.items() if k[:2] == 'hr'}


# TODO Unnecessarily complicated, rework this
class ItemDict(MutableMapping, ABC):
    def __init__(self, items: dict):
        self.data = self.del_name(items)

    @staticmethod
    def del_name(itemdict):
        dictnames = [k for k in itemdict]
        for key in dictnames:
            del itemdict[key]['name']
            del itemdict[key]['compset']
        return itemdict

    def __call__(self, *args, **kwargs):
        return self.data

    def __delitem__(self, key):
        pass

    def __getitem__(self, item):
        pass

    def __iter__(self):
        pass

    def __len__(self):
        pass

    def __setitem__(self, key, value):
        pass

    def listnames(self, valuelist: bool):
        if valuelist:
            keylist = [key for key in self.data]
            return keylist
        else:
            return self.data.keys()

    def key_string(self, key):
        string = self.data[key]
        return tk.StringVar(value=string)

    def value_list(self):
        keylist = [key for key, value in self.data]
        return keylist
