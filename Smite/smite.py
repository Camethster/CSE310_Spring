# %%
import pandas as pd
import numpy as np
import altair as alt
import requests as rq
import datetime
import hashlib
import json
# %%
# Credentials
creds = pd.read_json("creds.json")
credsDict = creds.to_dict()
devId = str(creds.iloc[0,0])
authKey = creds.iloc[0,1]
# Timestamp
languageCode = "1" #English

# Smite API
baseUrl = "https://api.smitegame.com/smiteapi.svc"
# %%
# Need to create a session first
offset = datetime.timedelta(hours=6)
stamp = datetime.datetime.now() + offset
stamp = stamp.strftime("%Y%m%d%H%M%S")
baseAuth = devId + "createsession" + authKey + stamp
signature =  baseAuth.encode()
signature = hashlib.md5(signature)
extUrl = "/createsessionJson/" + devId + "/" + signature.hexdigest() + "/" + stamp
session = rq.get(baseUrl + extUrl)
session.status_code
sessionId = session.json()["session_id"]
# test Session
# %%
print(session.text)
call = input("Call.")
baseSign = devId + call + authKey + stamp
signature =  baseSign.encode()
signature = hashlib.md5(signature)
response = rq.get(baseUrl + "/" + call + "json/" + devId + "/" + signature.hexdigest() + "/" + sessionId + "/" + stamp + "/" + languageCode)
# %%
response.status_code
response.text
responseJson = response.json()
# %%
session.close()
# %%
with open(call + ".json", "w") as outfile:
    json.dump(responseJson, outfile)

# %%
