# %%
import pandas as pd
import numpy as np
df = pd.read_csv(r"CTDC_synthetic_20210825.tsv",sep="\t")
iso = pd.read_csv(r"countries_codes_and_coordinates.csv")
# %%

df["country"] = df

