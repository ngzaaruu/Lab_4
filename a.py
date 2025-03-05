import json


    with open("C:/Users/naagi/OneDrive/Desktop/code py/lab_4/jssson/sample-data.json", "r") as file:
        y = json.load(file)


s = """Interface Status
================================================================================
DN                                                 Description           Speed    MTU  
-------------------------------------------------- --------------------  ------  ------"""


for el in y["imdata"]:
    
    dn = el["l1PhysIf"]["attributes"].get("dn", "N/A")
    speed = el["l1PhysIf"]["attributes"].get("speed", "N/A")
    mtu = el["l1PhysIf"]["attributes"].get("mtu", "N/A") 
    s += f"\n{dn:<71}  {speed:<8} {mtu:<6}"


print(s)