#!/usr/bin/env python
# coding: utf-8

# In[2]:


import requests
import time
import pymongo
from pymongo import MongoClient
client = MongoClient('mongodb+srv://annath:annath@cluster0-gkcsi.mongodb.net/test?retryWrites=true&w=majority')
db = client.Cluster0
while True:
    r = requests.get("https://data.cityofchicago.org/resource/f7f2-ggz5.json?")
    if r.status_code == 200:
        data = r.json()
        print(data)
        db.DevicesUsed.insert_many(data)
        time.sleep(36800)
else:
    exit()


# In[ ]:




