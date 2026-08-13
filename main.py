import json #importing json files
with open ("resources.json", "r") as datafile:
    data = json.load(datafile) 


resources = data["resources"]
print("-"*45)
for resource_type,resource_list in resources.items():
    print(resource_type)
    for resource in resource_list:
        name = (resource["common_meta_data"])["name"]
        id = (resource["common_meta_data"])["resource_id"]
        print(" ",name," ", id)
print("-"*45)
