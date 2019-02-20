#!/usr/bin/env python
# coding: utf-8

# # Sentiment Analysis

# In[46]:


import tweepy
from tweepy import OAuthHandler


# In[48]:


consumer_key = 'eSthnJY72D6y6DjPkn4UUUUGj'
consumer_secret = 'FzNOEPRnuLeQmIFsrxh14uFDHOa6av2AAUKqYtM2soB2ztOKz9'
access_token = '754476849447796736-j1obvclCx8darYTDOS4ZS7YG6q3gfUK'
access_secret = 'EbF0BqO1wmaxdJLa6DdGobyTeedqX5pwurnnhk0i2XsPP'


# In[49]:


auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)
api = tweepy.API(auth)


# In[50]:


import pandas as pd
import numpy as np
import datetime
import sys


# In[53]:


encoding = sys.stdout.encoding or 'utf-8'
columns = ['Screen_Name', 'Time_Stamp', 'Tweet']
todays_date = datetime.datetime.now().date()
tweetDF = pd.DataFrame(columns=columns)


# In[54]:


for tweet in tweepy.Cursor(api.search, q="manhattan", lang="en").items(10):
    lenDF = len(tweetDF)
    tweetDF.loc[lenDF] = [tweet.user.screen_name, tweet.created_at, tweet.text]


# In[56]:


tweetDF.to_csv("/home/admin9/Downloads/data.csv", sep ='\t', encoding='utf-8')


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




