import json

f = open('sample-data.json')
di = json.load(f)
print('''
Interface Status
================================================================================
DN                                                 Description           Speed    MTU  
-------------------------------------------------- --------------------  ------  ------''')
main_info = di["imdata"]
for i in main_info:
    print(f'{i["l1PhysIf"]["attributes"]["dn"]}{' '* (30+42-len(i["l1PhysIf"]["attributes"]["dn"]))}{i["l1PhysIf"]["attributes"]["speed"]}   {i["l1PhysIf"]["attributes"]["mtu"]}')
