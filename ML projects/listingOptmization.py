# %%
import pandas as pd
import numpy as np
import sklearn as sk
import Automunge as am


# %%
# Got to read in data and clean it
# First six rows are user information we want to exclude that. It also doesn't include headings
df = pd.read_csv("C:\git\Portfolio\ML projects\eBay-ListingsTrafficReport-Feb-06-2023-13_12_40-0700-1180243584 copy.csv",skiprows=5)

# %%
# We may also want to encode data types into our data to make it more numeric which is what the computer likes.

# imputing nulls. Most of the values are classified as nonull but lets look at the value counts of the columns to get a good read of what is happening
# We may also want to drop columsn that are private and have work 
df["Listing title"].value_counts(dropna=False) # All have Values
df["eBay item ID"].value_counts(dropna=False) # No Nulls
df["Current promoted listings status"].value_counts(dropna=False)
df["Quantity available"].value_counts(dropna=False)
df["Total impressions on eBay site"].value_counts(dropna=False) #"-" is a value which is probably a null
df["Top 20 search slot impressions from promoted listings"].value_counts(dropna=False) # No large amount of nulls
df["Top 20 search slot organic impressions"].value_counts(dropna=False) #
df["% change in top 20 search slot impressions"].value_counts(dropna=False) # 307 nulls
df["Rest of search slot impressions"].value_counts(dropna=False) # More "-"
df["Non-search promoted listings impressions"].value_counts(dropna=False) # Keep having 35 listings "-"
df["% Change in non-search promoted listings impressions"].value_counts(dropna=False) # 145 nulls
df["Non-search organic impressions"].value_counts(dropna=False)  # 35 Nulls
df["% Change in non-search organic impressions"].value_counts(dropna=False) # 57 nulls
df["Total promoted listings impressions (applies to eBay site only)"].value_counts(dropna=False) # 35
df["Total organic impressions on eBay site"].value_counts(dropna=False) # 35 Nulls
df["Total page views"].value_counts(dropna=False) # No Nulls
df["Page views via promoted listings impressions on eBay site"].value_counts(dropna=False) # 35 Nulls
df["Page views via promoted listings Impressions from outside eBay (search engines, affilliates)"].value_counts(dropna=False) # 35 Nulls
df["Page views via organic impressions on eBay site"].value_counts(dropna=False) # No Nulls
df["Page views from organic impressions outside eBay (Includes page views from search engines)"].value_counts(dropna=False) # 35 Nulls
df["Click-through rate = Page views from eBay site/Total impressions"].value_counts(dropna=False) # No Nulls
df["Quantity sold"].value_counts(dropna=False) # No NUlls
df["Sales conversion rate = Quantity sold/Total page views"].value_counts(dropna=False) # 241 Nulls
df["Unnamed: 24"].value_counts(dropna=False) # All Nulls


# %%

# %%
