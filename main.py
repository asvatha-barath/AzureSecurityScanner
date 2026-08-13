import json #importing json files

with open ("resources.json", "r") as datafile:
    data = json.load(datafile) 

print(data)