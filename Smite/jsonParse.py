#%%
import pandas as pd
import numpy as np
import Automunge as am
import altair as alt
import requests as rq
import datetime
import hashlib
import json
stats = ["Health","AttackSpeed","HP5","MP5","Mana","PhysicalProtection","PhysicalPower","MagicProtection","MagicalPower","Speed"]
# %%""
file = open(r"C:\Users\Camet\Portfolio\Smite\getgods.json")
gods = json.load(file)
# %%
achilles = gods[0]
for y in gods:
    y["HP5"] = y["HealthPerFive"]
    y["MP5"] = y["ManaPerFive"]
    y.pop("HealthPerFive")
    y.pop("ManaPerFive")
    y["SpeedPerLevel"] = 1.0257
#%%
for atb in stats:
    for y in gods:
        prevLevel = y[atb]
        healthLevel = y[atb+"PerLevel"]
        for x in range(1,20):
            level = str(x+1)
            y["Level"+level+atb] = prevLevel + healthLevel*x
            prevLevel = y["Level"+level+atb]
for y in gods:
    for x in range(7,20):
        level = str(x+1)
        print("Level"+level+"Speed")
        print(y["Level"+level+"Speed"])
        y.pop("Level"+level+"Speed")

# %%
with open("parseGods.json", "w") as fp:
    json.dump(gods,fp) 
# %%
