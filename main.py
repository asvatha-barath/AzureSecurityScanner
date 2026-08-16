import json #importing json files
def access_test_data():
    #opens .json file for data
    with open ("resources.json", "r") as datafile:
     data = json.load(datafile) 
    return data

def get_resource_details(resource):
          #retrieves details from .json through indexing
          name = (resource["common_meta_data"])["name"]
          id = (resource["common_meta_data"])["resource_id"]
          properties =(resource["properties"])
          return name,id,properties

def print_resource_details(name,id,properties,resource_type):
        #prints all resource details. Not used in test but can be used when needed
        print("-"*45)
        print(f"resource type: {resource_type} name: {name} resource_id:, {id}")

        for property,value in properties.items():
            print(" ",property, "-->", value )



def get_encryption(resource_type,properties):
      #retrieves encryption status from .json
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
       #retrives secure boot status from virtual machines
       if resource_type== "virtual_machines":
          BOOT = properties["security"]["secure_boot"]
          return BOOT

     
def check_security(actualValue, expectedValue,issueList,issue_type):
      if actualValue == expectedValue:
        return True
                         
      else:
        issueList.append(issue_type)
        return False

def check_status(issue_list):
      if len(issue_list) == 0:
            status = "SECURE"
      elif len(issue_list) >= 1:
            status = "NEEDS ATTENTION"
      return status



data = access_test_data()
issuedResources =  0 #amount of resources that need attentions
resourcecount = 0 #amount of resources read
totalissues = 0 # total amount of issues


resources = data["resources"] #retreiving resources info from data file

all_issues = {} #dictionary to save issue_list outside the loop


for resource_type, resource_list in resources.items():
        for resource in resource_list:
              resourcecount +=1 #incrementing to find amount of resources read
              issue_list=[]
              name,id,properties = get_resource_details(resource)
              PAK = get_public_access(resource_type,properties)
              ENCRYPT = get_encryption(resource_type,properties)
              check_security(PAK, False,issue_list,"PUBLIC ACCESS")
              check_security(ENCRYPT,True,issue_list,"ENCRYPTION")
              if resource_type == "virtual_machines":
                BOOT = get_secure_boot(resource_type, properties)
                check_security(BOOT,True,issue_list,"SECURE BOOT")
              if issue_list:
               issuedResources += 1
               items = len(issue_list)
               totalissues += items
              all_issues[name]= issue_list

#printing header with counts
print("="*45)
print("Azure Security Scan")
print("="*45)
print(f"Resources Scanned: {resourcecount}")
print(f"Resources with Security Issues: {issuedResources}")
print(f"Total Security Issues: {totalissues}")

#loop to print issue list and alerts for each resources
for resource_type, resource_list in resources.items():
        for resource in resource_list:
              name,id,properties = get_resource_details(resource)
              issue_list = all_issues[name]
              status = check_status(issue_list)
              print("-"*45)
              print(f"{name}")
              print("-"*45)
              print(f"STATUS: {status}")
              if not issue_list:
                    print("ALL SECURITY TESTS PASSED")
              else:
                 for issueTest in issue_list:
                      print(f"FAILED:{issueTest} TEST")


            

