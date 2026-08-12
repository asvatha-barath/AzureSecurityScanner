import json #importing json files


with open ("resources.json", "r") as file:
    data = json.load(file) 

print(data)