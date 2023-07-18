import json
import os
base = {
    "replace":True,
    "groups":[],
    "effects":[
        {
            "attributes": [
                {
                    "name": "minecraft:generic.max_health",
                    "operation": "add",
                    "amount": 2.0
                }
            ],
            "conditions": [
                {
                    "groups": ["proteins", "fruits", "vegetables", "grains"],
                    "match": "all",
                    "above": 0.8,
                    "below": 1.0
                }
            ]
            },
            {
            "status_effects": [
                {
                    "name": "minecraft:hunger",
                    "power": 3
                }
            ],
            "conditions": [
                {
                    "groups": ["sugars"],
                    "match": "all",
                    "above": 0.8,
                    "below": 1.0
                }
            ]
        }
    ]
}


dirs = os.getcwd()
dirs = dirs.split("\\")
dirs[-1] = "groups"
dirs = "\\".join(dirs)

targetdir = os.listdir(dirs)
print(targetdir)
for i in targetdir:
    i = i.split('.')
    filename = ""
    if i[-1]=='json':
        i.pop()
        if(len(i)>1):
            filename = ".".join(i)
        else: 
            filename = i[0]
        base.get("groups",[]).append(filename)

with open("builtin.json", "w") as f:
    json.dump(base,f,ensure_ascii=False,indent=2)
