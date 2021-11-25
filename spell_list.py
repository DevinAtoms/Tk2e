import json
import pandas as pd

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
sl.rename(columns={'compset': '', 'name': 'Spell Name', 'stAbScModifier': 'Ability Modifier', 'stNet': 'Spell Modifier',
                   'stDC': 'Spell DC', 'proLevelBonNet': 'Proficiency Bonus', 'ProfLevel': 'Proficiency',
          'spLevelBase': 'Spell Level', 'spLevelNet': 'Heightened Level', 'Trait 0': 'School'}, inplace=True)
sl.set_index('Spell Name', inplace=True)

sl.to_excel("output.xlsx")
