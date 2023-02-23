# %%
import pandas as pd
import numpy as np
import Automunge as am
import altair as alt
import requests as rq
import datetime
import hashlib
# %%
# Credentials
creds = pd.read_json("creds.json")
credsDict = creds.to_dict()
devId = str(creds.iloc[0,0])
authKey = creds.iloc[0,1]
# Timestamp


# Smite API
baseUrl = "https://api.smitegame.com/smiteapi.svc"
# %%
# Need to create a session first
offset = datetime.timedelta(hours=7)
stamp = datetime.datetime.now() + offset
stamp = stamp.strftime("%Y%m%d%H%M%S")
baseAuth = devId + "createsession" + authKey + stamp
signature =  baseAuth.encode()
signature = hashlib.md5(signature)
extUrl = "/createsessionJson/" + devId + "/" + signature.hexdigest() + "/" + stamp
session = rq.get(baseUrl + extUrl)
session.status_code
# test Session
# %%
print(session.text)
response = rq.get(baseUrl + "/ping", auth=(devId, authKey))
# %%
session.close()
# %%
