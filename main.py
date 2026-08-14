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


       
     
def check_security(actualValue, expectedValue,issueList,name):
      if actualValue == expectedValue:
        return True
                         
      else:
        issueList.append(name)
        return False




#Logic Only
'''
class identify_security_issues(ABC):
    def __init__(self,expected_encryption, expected_public_access, expected_secure_boot):
        self.expected_public_access = expected_public_access
        self.expected_encryption = expected_encryption
        self.expected_secure_boot = expected_secure_boot
        
    @abstractmethod
    def check_public_access(self):
        pass

    @abstractmethod
    def check_encryption(self):
            pass
    
    @abstractmethod
    def check_secureboot(self):
            pass
class VMsecurity (identify_security_issues):
   def __init__(expected_encryption, expected_public_access, expected_secure_boot):
        super().__init__(True,False,True)

        '''
data = access_test_data()

resources = data["resources"]
public_access_issues =[]
encryption_issues = []
for resource_type, resource_list in resources.items():
        for resource in resource_list:
              name,id,properties = get_resource_details(resource)
              print_resource_details(name,id,properties,resource_type)
              PAK = get_public_access(resource_type,properties)
              ENCRYPT = get_encryption(resource_type,properties)
              check_security(PAK, False,public_access_issues,name)
              check_security(ENCRYPT, True,encryption_issues,name)
    


print("\nPublic Access Issues\n")
for issue in public_access_issues:
    print(issue)

print("\nEncryption Issues\n")
for issue in encryption_issues:
    print(issue)


#PRINTING AND JSON CONNECT

        
        

'''
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

print("Public Access Issues")
for i in public_access_issues:
      print(" ", i)

print("Encryption  Issues")
for i in encryption_issues:
      print(" ", i)
print("Virtual Machine Secure Boot Issues")     
for i in secureboot_issues:
      print(" ", i)

                     
    
'''
  
        
        

