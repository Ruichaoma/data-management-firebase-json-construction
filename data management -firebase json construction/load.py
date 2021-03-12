#!/usr/bin/env python
# coding: utf-8

# In[1]:


import sys
import json
import requests


# In[2]:


chats_info = sys.argv[1]
roster_info = sys.argv[2]


# In[16]:


with open (chats_info) as data_file:
    data = json.load(data_file)
requests.put(url='https://q3b-602e6-default-rtdb.firebaseio.com/.json', json=data)


# In[17]:


with open (roster_info) as data_file_roster:
    data_roster = json.load(data_file_roster)
requests.put(url='https://q3c-f32c4-default-rtdb.firebaseio.com/.json', json=data_roster)


# In[ ]:




