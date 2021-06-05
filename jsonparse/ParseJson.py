import json
# data=''
with open('states.json','r') as f:
    data = f.read()
data = json.loads(data)
with open('abc.json','w') as f:
    json.dump(data,f,indent=2,sort_keys=True)
for item in data['states']:
    print(item['name'],item['abbreviation'])