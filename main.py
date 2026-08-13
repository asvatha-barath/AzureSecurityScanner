import json #importing json files
with open ("resources.json", "r") as datafile:
    data = json.load(datafile) 


resources = data["resources"]

for resource_type,resource_list in resources.items():
    print("-"*45)
    print(resource_type)
    for resource in resource_list:
        name = (resource["common_meta_data"])["name"]
        id = (resource["common_meta_data"])["resource_id"]
        properties =(resource["properties"])
        print(" ","-"*45)
        print(" ",name," ", id)
        print(" ","-"*45)
        for property,value in properties.items():
            print(" ",property, "<---->", value )

  
        
        

