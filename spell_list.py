import json
import pandas as pd
import re

exp_file = open('token.json', encoding="utf8")
data = json.load(exp_file)
data_dumped = json.dumps(data)
token = json.loads(data_dumped)
token_items = token['actors']['actor.1']['items']

items = pd.DataFrame(token_items)
items = items.transpose(copy=True)
items.set_index('compset', inplace=True)
sl = pd.DataFrame(items.at['Spell',])
sl.dropna(axis='columns', inplace=True)
sl.drop(columns=['description'], inplace=True)

traits = sl['Trait'].str.split(',', n=0, expand=True)

for t in traits:
    sl["Trait " + str(t)] = traits[t]

sl.drop(columns=['Trait'], inplace=True)

pat1 = re.compile(r'(\b\w{5,},)', re.MULTILINE)
pat2 = re.compile(r'[^a-z\d\s,]', re.MULTILINE)
pat3 = re.compile(r'(?<!re)action', re.MULTILINE)
pat4 = re.compile(r'(?<=\d)\s\s\w\w\s\s\s(?=\d)', re.MULTILINE)
pat5 = re.compile(r'^\s+|\s(?!\w)', re.MULTILINE)
pat6 = re.compile(r'\b\s(?!Minute)', re.MULTILINE)
sl['spCastingText'] = sl['spCastingText'].str.replace(pat2, ' ')
sl['spCastingText'] = sl['spCastingText'].str.replace('icon', '')
sl['spCastingText'] = sl['spCastingText'].str.replace(pat3, '')
sl['spCastingText'] = sl['spCastingText'].str.replace(pat4, '-')
sl['spCastingText'] = sl['spCastingText'].str.title()
sl['spCastingText'] = sl['spCastingText'].str.replace(pat5, '')
sl['spCastingText'] = sl['spCastingText'].str.replace(pat6, '_')

actions = sl['spCastingText'].str.split('_', n=0, expand=True)
actions = actions.convert_dtypes(infer_objects=True, convert_string=False, convert_boolean=False,
                                 convert_floating=False)
actions[0].convert_dtypes()
actions[0] = actions[0].convert_dtypes(infer_objects=True)

for a in actions[0]:
    if a.isdigit() == True:
        a.convert_dtypes()
    else:
        continue



for a in actions:
    sl["Actions" + str(a)] = actions[a]

sl.drop(columns=['spCastingText'], inplace=True)

sl.rename(columns={'compset': '', 'name': 'Spell Name', 'stAbScModifier': 'Ability Modifier', 'stNet': 'Spell Modifier',
                   'stDC': 'Spell DC', 'proLevelBonNet': 'Proficiency Bonus', 'ProfLevel': 'Proficiency',
                   'spLevelBase': 'Spell Level', 'spLevelNet': 'Heightened Level', 'Trait 0': 'School'}, inplace=True)

sl.set_index('Spell Name', inplace=True)

# sl.to_excel("output.xlsx")
