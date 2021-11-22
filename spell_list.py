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
sl = pd.DataFrame(items.at['Spell', ])
sl.dropna(axis='columns', inplace=True)

sl['Trait'].str.split(',', expand=True)

sl.to_excel("output.xlsx")
