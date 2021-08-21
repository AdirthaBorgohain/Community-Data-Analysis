import json
from glob import glob

json_files = glob('data/community_*.json')
complete_data = list()

for file in json_files:
    with open(file, 'r') as fin:
        data = json.load(fin)
        complete_data.extend(data)
        
with open('data/Top10_Communities.json', 'w') as fout:
    json.dump(complete_data, fout)
        

