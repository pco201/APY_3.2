import json

fh = open('weny_dod_tiny.json')
dod = json.load(fh)
fh.close()

def by_mean_temp(dict_key):
    #print(f'arg to sort function:  {dict_key}')
    return int(dod[dict_key]['mean_temp'])

keys = sorted(dod, key=by_mean_temp)

for key in keys:
    print(f'{key}:  {dod[key]}')