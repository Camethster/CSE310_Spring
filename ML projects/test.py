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
# Try it on a different set

# lets clean it
df = pd.read_csv("C:\git\Portfolio\ML projects\eBay-ListingsTrafficReport-Feb-21-2023-10_57_28-0700-1291997234.csv",skiprows=5)
df.drop(["Unnamed: 24","Listing title","eBay item ID"],axis=1,inplace=True)
df.drop(["% Change in non-search promoted listings impressions",
         "% change in top 20 search slot impressions",
         "% change in top 20 search slot impressions from promoted listings",
         "% change in top 20 search slot impressions",
         "% Change in non-search organic impressions",
         "Sales conversion rate = Quantity sold/Total page views",
         "Click-through rate = Page views from eBay site/Total impressions"],axis=1,inplace=True)
df.replace("-",np.nan,inplace=True)
df.dropna(thresh=12,inplace=True)
df.replace(",","",inplace=True,regex=True)
oneColumn = pd.get_dummies(df["Current promoted listings status"])
df.drop("Current promoted listings status",axis=1,inplace=True)
df = df.astype(int)
df = df.join(oneColumn)
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
scaler = sk.preprocessing.Normalizer().fit(X)
XNorm = scaler.transform(X)
regression = feature_selection.r_regression(XNorm,y)
oversample = RandomOverSampler()
X, y = oversample.fit_resample(X,y)


XTrain, XTest, yTrain, yTest = sk.model_selection.train_test_split(X,y,test_size=.33,random_state= 16)
# %%
# Terrible Score 0.0
savedRgr = pickle.load(open('model.pkl', 'rb'))
savedRgr.score(X,y)
# %%
