#!/usr/bin/env python
# coding: utf-8

# In[1]:


import requests
import json
import sys


# In[2]:


person_info = requests.get('https://q3c-f32c4-default-rtdb.firebaseio.com/.json',stream=True)


# In[42]:


person = person_info.json()


# In[55]:


def search_names(first_name,last_name):
    
    
    for name_info in person:
        student_name = name_info['Name'].split(" ")
        if first_name ==  student_name[0].lower() or last_name == student_name[1].lower() or last_name ==  student_name[0].lower() or first_name == student_name[1].lower():
            
            print(name_info['Name'])

search_name = str(sys.argv[1])
if len(search_name.split(" "))>1:
    
    first_name = search_name.split(" ")[0].lower()
    last_name = search_name.split(" ")[1].lower()
else:
    
    first_name = search_name.split(" ")[0].lower()
    last_name = "InvalidName"


search_names(first_name,last_name)


# In[ ]:





# In[ ]:





# In[ ]:




