import json #importing json files
from abc import ABC, abstractmethod
def access_test_data():
    with open ("resources.json", "r") as datafile:
     data = json.load(datafile) 
    return data

def get_resource_details(resource):
          name = (resource["common_meta_data"])["name"]
          id = (resource["common_meta_data"])["resource_id"]
          properties =(resource["properties"])
          return name,id,properties

def print_resource_details(name,id,properties,resource_type):
        print("-"*45)
        print(f"resource type: {resource_type} name: {name} resource_id:, {id}")

        for property,value in properties.items():
            print(" ",property, "-->", value )

def get_encryption(resource_type,properties):
      if resource_type in ["storage_accounts","databases"]:
            ENCRYPT = properties["security"]["encryption"]
      elif resource_type=="virtual_machines": 
            ENCRYPT = properties["security"]["disk_encryption"]
                
      else:
            raise KeyError 
      return ENCRYPT


       
def get_public_access(resource_type,properties):
     if resource_type in[ "virtual_machines","databases"]: 
                     PAK = properties["security"]["public_access"]
     elif resource_type =="storage_accounts": 
                 PAK = properties["network"]["public_network_access"]
     else:
                  raise KeyError
     return PAK #returning public access key


def get_secure_boot(resource_type,properties):#USE WITH VM ONLY
       if resource_type== "virtual_machines":
          BOOT = properties["security"]["secure_boot"]
          return BOOT

     
def check_security(actualValue, expectedValue,issueList,issue_type):
      if actualValue == expectedValue:
        return True
                         
      else:
        issueList.append(issue_type)
        return False





data = access_test_data()

resources = data["resources"]

for resource_type, resource_list in resources.items():
        for resource in resource_list:
              issue_list=[]
              name,id,properties = get_resource_details(resource)
              print_resource_details(name,id,properties,resource_type)
              PAK = get_public_access(resource_type,properties)
              ENCRYPT = get_encryption(resource_type,properties)
              
              check_security(PAK, False,issue_list,"PUBLIC ACCESS")
              check_security(ENCRYPT,False,issue_list,"ENCRYPTION")
              if resource_type == "virtual_machines":
                BOOT = get_secure_boot(resource_type, properties)
                check_security(BOOT,False,issue_list,"SECURE BOOT")
              for issueTest in issue_list:
                    print(f"FAILED:{issueTest} TEST")

