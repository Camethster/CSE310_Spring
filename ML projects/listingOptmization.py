# %%
import pandas as pd
import numpy as np
import sklearn as sk
import Automunge as am
import altair as alt
from sklearn import feature_selection
from imblearn.over_sampling import RandomOverSampler
from sklearn import svm
import pickle
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
df["Top 20 search slot organic impressions"].value_counts(dropna=False) # no Nulls
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
#Drop Columns are Unamed Title(We probably shouldn't do NPL) Ebay item ID Private Identifier
df.drop(["Unnamed: 24","Listing title","eBay item ID"],axis=1,inplace=True)
# All percentages need to be dropped. The nulls are too much for the data to handle
# The size of the data is the problem, plus we can't impute these values.
df.drop(["% Change in non-search promoted listings impressions",
         "% change in top 20 search slot impressions",
         "% change in top 20 search slot impressions from promoted listings",
         "% change in top 20 search slot impressions",
         "% Change in non-search organic impressions",
         "Sales conversion rate = Quantity sold/Total page views",
         "Click-through rate = Page views from eBay site/Total impressions"],axis=1,inplace=True)


# %%
# Dealing with the 35 null values "-" need to = np.nan
df.replace("-",np.nan,inplace=True)
# Thresh looking at the values that have > 35
df.dropna(thresh=12,inplace=True)
# Confirmed all 35 nulls are replaced. Probably new listings that haven't had their impressions or promoted impressions tracked.
# %%
# Now imputing nulls for the percent changes will probably need a mean
# This means we are going to have to change the object to decimal
# Then calculate the mean of those decimals and impute it
# Need to remove the comma in the thousands range
df.replace(",","",inplace=True,regex=True)
# Now change the data type
# if we one hot encode the first column all should be numbers
oneColumn = pd.get_dummies(df["Current promoted listings status"])
df.drop("Current promoted listings status",axis=1,inplace=True)
# %%
df = df.astype(int)
# %%
df = df.join(oneColumn)
# %%
# We should index the columns to give a unique identifier but the computer doesn't want it
# df['index'] = range(1, len(df) + 1)
# Seperating our columns
# impressions first we want to drop anything that has a direct connection to impressions
X = df.drop(["Total impressions on eBay site",
             "Top 20 search slot impressions from promoted listings",
             "Top 20 search slot organic impressions",
             "Rest of search slot impressions",
             "Non-search promoted listings impressions",
             "Non-search organic impressions",
             "Total promoted listings impressions (applies to eBay site only)",
             "Total organic impressions on eBay site",
             "Non-promoted"],axis=1) 
y = df["Total impressions on eBay site"]



# We have to scaling lets start with a normalization method
# Changed to an array type
scaler = sk.preprocessing.Normalizer().fit(X)
XNorm = scaler.transform(X)
# %%
# Regression model
regression = feature_selection.r_regression(XNorm,y)
# Interesting. Quantity availible is bad. Promoted > organic, but being promoted lowers your chances
# This is probably due to the low amount of non promoted
# %%
# Going to use a random over sample because it is easy to even out dataset
oversample = RandomOverSampler()
X, y = oversample.fit_resample(X,y)
XNorm = scaler.transform(X)
normRegression = feature_selection.r_regression(XNorm,y)
regression = feature_selection.r_regression(X,y)
# %%
# Time to train
XTrain, XTest, yTrain, yTest = sk.model_selection.train_test_split(X,y,test_size=.33,random_state= 16)
#rgr = svm.SVC(kernel='linear').fit(XTrain,yTrain)
#rgr.score(XTest,yTest)
# %%
# Saved in a pickle
#pickle.dump(rgr,open('impressModel.pkl', 'wb'))

# %%
# Really what we are looking for is sales though

X = df.drop(["Quantity sold",
             "Non-promoted"],axis=1) 
y = df["Quantity sold"]



# We have to scaling lets start with a normalization method
# Changed to an array type
scaler = sk.preprocessing.Normalizer().fit(X)
XNorm = scaler.transform(X)
# %%
# Regression model
regression = feature_selection.r_regression(XNorm,y)
# Interesting. Quantity availible is bad. Promoted > organic, but being promoted lowers your chances
# This is probably due to the low amount of non promoted
# %%
# Going to use a random over sample because it is easy to even out dataset
oversample = RandomOverSampler()
X, y = oversample.fit_resample(X,y)
XNorm = scaler.transform(X)
normRegression = feature_selection.r_regression(XNorm,y)
regression = feature_selection.r_regression(X,y)
# %%
# Time to train
XTrain, XTest, yTrain, yTest = sk.model_selection.train_test_split(X,y,test_size=.33,random_state= 16)
rgr = svm.SVC(kernel='linear').fit(XTrain,yTrain)
rgr.score(XTest,yTest)
 # %%
# Saved in a pickle
pickle.dump(rgr,open('salesModel.pkl', 'wb'))
