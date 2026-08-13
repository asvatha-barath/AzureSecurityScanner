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
        print("-"*45)
        print("  name:",name," resource_id:", id)
        for property,value in properties.items():
            print(" ",property, "-->", value )

        if resource_type == "virtual_machines" or resource_type == "databases": 
                PAK = properties["security"]["public_access"]
        elif resource_type=="storage_accounts": 
            PAK = properties["network"]["public_network_access"]
        else:
             raise KeyError
        if PAK == True:
             print(f"\n{name} --> Public Access Key ENABLED\n")
        else:
             print(f"\n{name} --> Public Access Key NOT ENABLED\n")
             
                
        

  
        
        

