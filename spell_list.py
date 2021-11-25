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

traits = sl.set_index('name')
traits = traits['Trait'].str.split(',', n=0, expand=True)

for t in traits:
    print(t[1])
   # if traits[t].str[:2].contains('ss', regex=False):
      #  print(traits[t])
    #elif traits[t].any(traits[t].str[:3] == 'trd'):
        #sl['Tradition'] = traits[t]
   #else:
        #sl["Trait" + str(t)] = traits[t]

# sl.drop(columns=['Trait'], inplace=True)


#sl.to_excel("output.xlsx")
