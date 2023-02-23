# Overview

This machine learning software will analyze listing data to determine what is important when getting impressions,clicks, and sales on a product.

EBay is a platform where you can sell your products. Second only to the powerhouse Amazon, eBay has been a source of income for small business owners across the world.

The success of a listing is measure in three parts as mentioned earlier.

- Impressions
- Clicks (Click Through Rate)
- Sales (Sales off of Clicks)

# Cleaning
Lets get down into the basics of how this is setup.

Popular sellers on the platform can recieve what is called a traffic report. It is given in csv and when read into pandas reads the following columns

There are several problems here when we clean data for a machine. While some of these are for optimization others are necessary for the machine to learn and provide a reasonable inference.


<dl>
    <dt>Listing title (obj)</dt>
    <dd>Words used to describe the product </dd>
    <dt>eBay item ID (int64)</dt>
    <dd>The platforms identifier for a listing</dd>
    <dt>Current promoted listing status (obj)</dt>
    <dd>Whether or not you pay for extra impressions on your listing</dd>
    <dt>Quantity available (obj)</dt>
    <dd>The amount the sellers has availible for sale at the current time</dd>
    <dt>Total impressions on eBay site (obj)</dt>
    <dd>The total amount of impressions from "Organic" and Promoted </dd>
    <dt>Top 20 search slot impressions from promoted listings (obj)</dt>
    <dd>How many impressions where from the first 20 listings of a search from a promoted rate</dd>
    <dt>% change in top 20 search slot impressions from promoted listings (obj)</dt>
    <dd>I am unsure of what the comparison of the dates are. I believe you can set the period when getting a traffic report.</dd>   
    <dd>This particular report is from January to February</dd>
    <dt>Top 20 search slot organic impressions (obj)</dt>
    <dd>How many impressions where from the first 20 listings of a search with no promoted help</dd> 
    <dt>% change in top 20 search slot impressions (obj)</dt>
    <dd>This particular report is from January to February</dd>
    <dt>Rest of search slot impressions (obj)</dt>
    <dd>These impressions are from searches outside top 20</dd>
    <dt>Non-search promoted listings impressions (obj)</dt>
    <dd>These are impressions from eBay marketing</dd>
    <dt>% Change in non-search promoted listings impressions (obj)</dt>
    <dd>Percent change from non search impressions</dd>
    <dt>Non-search organic impressions (obj)</dt>
    <dd>Impressions these are from seller internal eBay marketing</dd>
    <dt>% Change in non-search organic impressions (obj)</dt>
    <dd>Percent change in impressions from seller internal eBay marketing</dd>
    <dt>% Change in non-search organic impressions (obj)</dt>
    <dd>Impressions these are from seller internal eBay marketing</dd>
    <dt>Total promoted listings impressions (applies to eBay site only) (obj)</dt> 
    <dd>Total impressions on eBay site from promoted listings</dd>
    <dt>Total organic impressions on eBay site (obj)</dt> 
    <dd>Total impressions on eBay site from organic views</dd>
    <dt>Total page views (obj)</dt> 
    <dd>These are our clicks. So very important</dd>
    <dt>Page views via promoted listings impressions on eBay site (obj)</dt>
    <dd>Clicks based on promoted listings</dd>
    <dt>Page views via promoted listings Impressions from outside eBay (search engines, affilliates) (obj) </dt> 
    <dd>Clicks via non-eBay affiliate advertising on promoted listings</dd>
    <dt>Page views via organic impressions on eBay (obj) </dt>
    <dd>Clicks for non-promoted listings</dd>
    <dt>Page views from organic impressions outside eBay (Includes page views from search engines) (obj)</dt>
    <dd>Clicks via non-eBay affiliate advertising on non-promoted listing</dd>
    <dt>Click-through rate = Page views from eBay site/Total impressions (obj) </dt>
    <dd>Self explainitory</dd>
    <dt>Quantity sold (int64)</dt>
    <dd>Amount Sold and our only other int</dd>
    <dt>Sales conversion rate = Quantity sold/Total page views</dt>
    <dd>Self explanitory</dd>
    <dt>Unnamed: 24 (float64)</dt>
    <dd>A random column. Probably some number it has on the side of the sheet</dd>
</dl>

## Shape

Using what we know from the data we are using their are 24 columns and 1560 rows in the data. For training data this is a pretty small dataset. Most AI have closer to 10,000 or 100,000 rows. 

We used random sampling to increase our AI's ability to learn. Instead of the orginal 1560 rows there are going to be over 200,000 rows to work with. This is done by copying samples from the previous data set at random to increase the amount of training data to learn from. 


## Nulls
There are a few ways to handle nulls. The article ["A Comprehensive Guide to Data Preprocessing"](https://neptune.ai/blog/data-preprocessing-guide) by Samadrita Ghosh published January 27th of 2023 goes into great detail about the ways we can clean data for the machine. We are going to do removal because there are only 35 rows that contain dangerous nulls. 

Handling Outliers will also be taken care by removing nulls. Most of the outliers in this dataset are outliers because they have null values. Those with nulls are going to be removed. Imputing values would cause more harm than good in the model.

## Encoding

The only encoding needed for this project is going to be for the column "Current promoted listing status" whose values are logistical instead of numerical. The other columns that had potential are going to be removed in dimesionality reduction.

The one-hot encoding method is going to be used here. This method makes a unique column where a boolean which is a true or false denoted by a 1 for true or a 0 for false. This makes the column numeric instead of a column with text.

## Dimensionality Reduction (Making Our Dataset Smaller)
### This can also be called Feature Selection

# Model Selection

# Performance

# Video

[Software Demo Video](http://youtube.link.goes.here)

# Development Environment

Visual Studio Code
Python 3
Pandas
Numpy
Sklearn
Altair
Imblearn
Pickle

# Useful Websites

* [scikit-learn](https://scikit-learn.org/stable/)
* [Neptune AI](https://neptune.ai/blog/data-preprocessing-guide)