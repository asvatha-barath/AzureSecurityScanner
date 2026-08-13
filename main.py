import json #importing json files
with open ("resources.json", "r") as datafile:
    data = json.load(datafile) 


resources = data["resources"]
expected_public_access = False
expected_encryption = True
expected_secure_boot = True

public_access_issues=[]
encryption_issues=[]
secureboot_issues=[]
#PRINTING AND JSON CONNECT

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



#LOGIC for PAK
        if resource_type == "virtual_machines" or resource_type == "databases": 
                PAK = properties["security"]["public_access"]
        elif resource_type=="storage_accounts": 
            PAK = properties["network"]["public_network_access"]
        else:
             raise KeyError

        if resource_type == "storage_accounts" or resource_type == "databases": 
                ENCRYPT = properties["security"]["encryption"]
        elif resource_type=="virtual_machines": 
                ENCRYPT = properties["security"]["disk_encryption"]
                BOOT = properties["security"]["secure_boot"]
        else:
                        raise KeyError

        
        if PAK == expected_public_access:
            print("PUBLIC ACCESS - SECURITY PASS")
            
        else:
             print("PUBLIC ACCESS - SECURITY FAIL")
             public_access_issues.append(name)
             
      
        if ENCRYPT == expected_encryption:
                    print("ENCRYPTION - SECURITY PASS")
                    
        else:
                     print("ENCRYPTION - SECURITY FAIL")
                     encryption_issues.append(name)

        if resource_type == "virtual_machines":
            if BOOT == expected_secure_boot:
               print("VM SECURE BOOT - SECURITY PASS")

            else:
             print("VM SECURE BOOT - SECURITY FAIL")
             secureboot_issues.append(name)

print("\n------CURRENT SECURITY ISSUES------\n")
for i in range(len(public_access_issues)):
      print(public_access_issues[i])
for i in encryption_issues:
      print(encryption_issues[i])
for i in secureboot_issues:
      print(secureboot_issues[i])

                     
        

  
        
        

