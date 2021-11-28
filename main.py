import json
import pandas as pd
from time import sleep


def itemLookup(items):

    for i in items.index:
        match i.startswith:
            case 'sp':
                print(i.startswith)
            case 'ab':
                print(i)
            case 'sv':
                print(i)
            case 'ac':
                print(i)
            case _:
                print(i.startswith)
                pass


#def itemParse(name, item_type):
    #print(str(name)+' '+str(item_type))
    #pass

exp_file = open('token.json', encoding="utf8")
token = json.load(exp_file)
tokenItems = pd.Series(token['actors']['actor.1']['items'])
itemLookup(tokenItems)