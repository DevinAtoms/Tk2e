import json
import pandas as pd

exp_file = open('token.json', encoding="utf8")
data = json.load(exp_file)
data_dumped = json.dumps(data)
token = json.loads(data_dumped)
token_items = token['actors']['actor.1']['items']

items = pd.DataFrame(token_items)
items = pd.DataFrame.transpose(items)
items = pd.DataFrame.set_index(items, 'compset')

spell_list = pd.DataFrame(items.at['Spell',])

spell_list.to_excel("output.xlsx")
