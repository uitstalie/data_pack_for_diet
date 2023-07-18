import json

filelist = [
"proteins.json",
"birds.json",
"eggs.json",
"fishs.json",
"milks.json",
"vegetables.json",
"fruits.json",
"nuts.json",
"grains.json",
"mushrooms.json",
"honeys.json",
"coffee.json",
"wines.json",
"sugars.json",
]


base = {
    "icon": "minecraft:egg",
    "color": "#d41c53",
    "order": 0,
    "default_value": 35,
    "gain_multiplier": 1.0,
    "decay_multiplier": 1.0,
    "beneficial": True
}

for file in filelist:
    with open(file,'w',encoding="utf-8") as f:
        json.dump(base, f,ensure_ascii=False,indent=2)