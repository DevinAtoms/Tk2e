import spell_list
import pandas as pd
import re

re_spells = re.compile('sp[A-Z][A-Za-z]+')

exp_file = open('token.json', encoding="utf8")
data = json.load(exp_file)
data_dumped = json.dumps(data)
token = json.loads(data_dumped)
token_items = token['actors']['actor.1']['items']
spell = {}

for i in token_items:
    if bool(re.match(re_spells, i)):
        spName = token_items[i]['name']
        spDesc = token_items[i]['description']

        if 'vaRangeText' in token_items[i].keys():
            spRange = token_items[i]['vaRangeText']
        else:
            spRange = 'Self'

        # spRange = token_items[i]['vaRangeText']
        # spTarget = token_items[i]['vaTarget']
        # spDc = token_items[i]['stDC']

        spell[spName] = [spDesc, spRange]

# spell_list = open('spell_list.json', 'w')
# spell_list.write(json.dumps(spell))

sl = pd.DataFrame(spell)
sl = pd.DataFrame.transpose(sl)
print(spell)
print(sl)
