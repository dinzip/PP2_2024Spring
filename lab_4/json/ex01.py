import json
heading = '''
Interface Status
================================================================================
DN                                                 Description           Speed    MTU  
-------------------------------------------------- --------------------  ------  ------'''

with open('sample-data.json') as f:
    main_data = json.load(f)
    print(heading)
    for i in main_data["imdata"]:
        print(f'{i["l1PhysIf"]["attributes"]["dn"]:72}{i["l1PhysIf"]["attributes"]["speed"]:10}{i["l1PhysIf"]["attributes"]["mtu"]}')
