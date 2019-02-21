import json

data = {}
data['people'] = []
data['people'].append({
    'name': 'Scott',
    'website': 'stackabuse.com',
    'from': 'Nebraska'
})
data['people'].append({
    'name': 'Larry',
    'website': 'google.com',
    'from': 'Michigan'
})
data['people'].append({
    'name': 'Tim',
    'website': 'apple.com',
    'from': 'Alabama'
})

with open('data.csv', 'w') as outfile:
    json.dump(data, outfile,sort_keys=True,indent=4)#write json data to the file(json.dump)
'''

with open('C:\PythonProjects\ListExample\JsonFileExample\data.txt')as file1:
    data=json.load(file1)#read data from a json file (json.load)
    for p in data['people']:
        print('Name: ' + p['name'])
        print('Website: ' + p['website'])
        print('From: ' + p['from'])
        print('')
'''
























