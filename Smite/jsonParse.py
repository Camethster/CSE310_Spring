#%%
import pandas as pd
import numpy as np
import Automunge as am
import altair as alt
import requests as rq
import datetime
import hashlib
import json
stats = ["Health","AttackSpeed","HP5","MP5","Mana","PhysicalProtection","PhysicalPower","MagicProtection","MagicalPower"]
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
        for x in range(1,21):
            level = str(x)
            y["Level" + level + atb] = prevLevel + healthLevel*x
            prevLevel = y[atb]
#for y in gods:
 #   for x in range(7,20):
  #      level = str(x+1)
   #     print("Speed")
    #    y.pop("Level" + level+ "Speed")

# %%
with open("parseGods.json", "w") as fp:
    json.dump(gods,fp) 
# %%
df = pd.DataFrame()
df["name"] = pd.Series(str)
df["role"] = pd.Series(str)
df["level"] = pd.Series(int)
for x in stats:
    df[x] = pd.Series()

#%%
for y in gods:
    for x in range(1,21):
            print(x)
            level = str(x)
            row = pd.DataFrame.from_dict({"name" : [y["Name"]], "role" : [y["Roles"]], "level" : level, "Health" : [y["Level"+level+"Health"]],"AttackSpeed" : [y["Level"+level+"AttackSpeed"]],"HP5" : [y["Level"+level+"HP5"]],"MP5" : [y["Level"+level+"MP5"]],"Mana" : [y["Level"+level+"Mana"]],"PhysicalProtection" : [y["Level"+level+"PhysicalProtection"]],"PhysicalPower" : [y["Level"+level+"PhysicalPower"]],"MagicProtection" : [y["Level"+level+"MagicProtection"]],"MagicalPower" : [y["Level"+level+"MagicalPower"]]},orient="columns")
            df = pd.concat([df,row],ignore_index=True)


        

# %%
df.drop(index=0).to_csv("baseStats.csv",index=False)
# %%
