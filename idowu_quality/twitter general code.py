#!/usr/bin/env python
# coding: utf-8

# In[1]:


# from requests import get
# from requests.exceptions import RequestException
# from contextlib import closing
# import pandas as pd
# import os, sys

# import fire

# import sys
# import os
# import json
# import matplotlib.pyplot as plt
# import re
# import string
# import csv 

# import matplotlib.dates as mdates
# import seaborn as sns

# to view all columns
# pd.set_option("display.max.columns", None)

# import tweepy
# from tweepy.streaming import StreamListener
# from tweepy import OAuthHandler
# from tweepy import Stream
# from tweepy import API
# from tweepy import Cursor
# from datetime import datetime, date, time, timedelta
# from collections import Counter
# import sys


# import preprocessor as p


# In[2]:


# credentials from https://apps.twitter.com/
# consumerKey = 'CONSUMER_KEY'
# consumerSecret = 'CONSUMER_SECRET'
# accessToken = 'ACCESS_TOKEN'
# accessTokenSecret = 'ACCESS_TOKEN_SECRET'

# auth = tweepy.OAuthHandler(consumerKey, consumerSecret)
# auth.set_access_token(accessToken, accessTokenSecret)

# api = tweepy.API(auth, wait_on_rate_limit=True)


# In[ ]:





# In[3]:


'''add more keywords depending with the country .... more so for Ethiopia, Rwanda and Uganda'''

# hashtags=["#foodquality","#foodsafety","#foodtech","#foodpollution","#foodpoisoning","#safefood" ,"#indoorfoodquality",
#           "#food","#foodsafetyjobs","#indoorfood","#KEBS" ,"#FSMA","#healthyeatting" , "#IAFP", 
#           "#ITF","#SQF","#HACCP","#foodies", "#foodsecurity ","#foodtechnology",
#           "#safety","#restaurant","#eateries" ,"#wearethevirus", "#foodbanks",
#          '#cleanfood']


# In[4]:


# from requests import get
# from requests.exceptions import RequestException
# from contextlib import closing
# import pandas as pd
# import os, sys

# import fire

# import sys
# import os
# import json
# import matplotlib.pyplot as plt
# import re
# import string
# import csv 

# import matplotlib.dates as mdates
# import seaborn as sns

# to view all columns
# pd.set_option("display.max.columns", None)
consumerKey = "kImN3N4783RFd5UNKDAkVRhdA"
consumerSecret = "8kWSeV8EAm0HG070DYJAauEnLm8F6DtHVMpvSAipZF6AvSPPXJ"
accessToken = "440809914-jXp0VTJvDm22WnehgGkgaD0IlF9j1N5BCinB2aLz"
accessTokenSecret = "zmSg34B7z77adqhB9Fe9OC39c85KbmPu0tI6iCsC5XBww" 

auth = tweepy.OAuthHandler(consumerKey, consumerSecret)
auth.set_access_token(accessToken, accessTokenSecret)

api = tweepy.API(auth, wait_on_rate_limit=True)
import pandas as pd
import numpy as np
import datetime
import tweepy
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
from tweepy import API
from tweepy import Cursor
from datetime import datetime, date, time, timedelta



# import preprocessor as p

# kenya
'''get the geocodes for the specific countries. Am providing what i have
RWANDA:geocode="1.9403, 29.8739, 91km"
NIGERIA:geocode="6.48937,3.37709,900km"
UGANDA:geocode="0.32400,32.58662, 200km"
'''
SOUTH_AFRICA_geocode="-26.22081,28.03239,400km"

hashtags=["#foodquality","#foodsafety","#foodtech","#foodpollution","#foodpoisoning","#safefood" ,"#indoorfoodquality",
          "#food","#foodsafetyjobs","#indoorfood","#KEBS" ,"#FSMA","#healthyeatting" , "#IAFP", 
          "#ITF","#SQF","#HACCP","#foodies", "#foodsecurity ","#foodtechnology",
          "#safety","#eateries" , "#foodbanks",
         '#cleanfood',"cooking","foodinsecurity","foodsecurity","nutrition"]

names = []
for hashtag in hashtags:
    tweets = tweepy.Cursor(api.search, q = hashtag ,geocode=SOUTH_AFRICA_geocode, wait_on_rate_limit=True).items(1000000)
    users = []
    for status in tweets:
        name = status.user.screen_name
        t=status.text
        users.append(name)
    names.append(users)
    
screen_names = [y for x in names for y in x]
names = screen_names
#print(len(names))

# drop duplicates
screen_names = list(dict.fromkeys(names))

def get_tweets(screen_names):
    a_user = []
    a_times = []
    a_texts = []
    a_favs = []
    a_retweets = []
    a_entities = []
    a_languages = []
    a_description = []
    
    for name in screen_names:
        
        user = []
        times = []
        texts = []
        favs = []
        retweets = []
        entities = []
        description = []
        langs = []
        
        tweets = tweepy.Cursor(api.user_timeline, screen_name = name, since = '2019-10-01', wait_on_rate_limit=True).items(1000)
        for tweet in tweets:
            user_ = tweet.user.screen_name
            time = tweet.created_at
            text_ = tweet.text
            fav = tweet.favorite_count
            retweet = tweet.retweet_count
            description_ = tweet.user.description
            lang = tweet.lang
            
            
            user.append(user_)
            times.append(time)
            texts.append(text_)
            favs.append(fav)
            retweets.append(retweet)
            description.append(description_)
            langs.append(lang)
            
        a_user.append(user)
        a_times.append(times)
        a_texts.append(texts)
        a_favs.append(favs)
        a_retweets.append(retweets)
        a_entities.append(entities)
        a_languages.append(langs)
        a_description.append(description)

    a_user = [y for x in a_user for y in x]
    a_times = [y for x in a_times for y in x]
    a_texts = [y for x in a_texts for y in x]
    a_favs = [y for x in a_favs for y in x]
    a_retweets = [y for x in a_retweets for y in x]
    a_entities = [y for x in a_entities for y in x]
    a_languages = [y for x in a_languages for y in x]
    a_description = [y for x in a_description for y in x ]
        
    df = pd.DataFrame({"user":a_user,'time':a_times, 'text':a_texts, 'favourite_count':a_favs,
                       'retweet_count':a_retweets,'entities':a_entities, 'lang':a_languages,"description":a_description})
    return df
data1 = get_tweets(screen_names[:])
data1.to_csv("{}".format("~/SA"+str(datetime.datetime.now().date())+".csv",index=False)


# In[12]:


# import datetime
# "hello"+str(datetime.datetime.now().date())+".csv"


# In[5]:


# # merge the lists
# names = screen_names
# print(len(names))

# # drop duplicates
# screen_names = list(dict.fromkeys(names))
# print(len(screen_names))


# In[4]:


list1 =[1,2,3]
print(list1[:])


# In[2]:


# df = pd.DataFrame({'names':screen_names})
# df.to_csv('KE_screen_names.csv')
# df.head()


# In[3]:


# def get_tweets(screen_names):
#     a_user = []
#     a_times = []
#     a_texts = []
#     a_favs = []
#     a_retweets = []
#     a_entities = []
#     a_languages = []
#     a_description = []
    
#     for name in screen_names:
        
#         user = []
#         times = []
#         texts = []
#         favs = []
#         retweets = []
#         entities = []
#         description = []
#         langs = []
        
#         tweets = tweepy.Cursor(api.user_timeline, screen_name = name, since = '2020-01-01', wait_on_rate_limit=True).items(500)
#         for tweet in tweets:
#             user_ = user.screen_name
#             time = tweet.created_at
#             text_ = tweet.text
#             fav = tweet.favorite_count
#             retweet = tweet.retweet_count
#             description = tweet.description
#             lang = tweet.lang
            
            
#             user.append(user_)
#             times.append(time)
#             texts.append(text_)
#             favs.append(fav)
#             retweets.append(retweet)
#             description.append(description)
#             langs.append(lang)
            
#         a_user.append(user)
#         a_times.append(times)
#         a_texts.append(texts)
#         a_favs.append(favs)
#         a_retweets.append(retweets)
#         a_entities.append(entities)
#         a_languages.append(langs)
#         a_description.append(description)

#     a_user = [y for x in a_user for y in x]
#     a_times = [y for x in a_times for y in x]
#     a_texts = [y for x in a_texts for y in x]
#     a_favs = [y for x in a_favs for y in x]
#     a_retweets = [y for x in a_retweets for y in x]
#     a_entities = [y for x in a_entities for y in x]
#     a_languages = [y for x in a_languages for y in x]
#     a_description = [y for x in a_description for y in x ]
        
#     df = pd.DataFrame({"user":a_user,'time':a_times, 'text':a_texts, 'favourite_count':a_favs,
#                        'retweet_count':a_retweets,'entities':a_entities, 'lang':a_languages,"description":a_description})
#     return df


# In[17]:


# data1 = get_tweets(screen_names[:50])
# #data1 = get_tweets(screen_name[100:150]) #to mine between 99 to 149 users' tweet #specify the number of users you want to mine  
# data1.sample(10)


# In[19]:


# data1.to_csv('KE_50_tweets.csv') #change csv file name to reflect the range of users


# In[1]:


data1.shape

