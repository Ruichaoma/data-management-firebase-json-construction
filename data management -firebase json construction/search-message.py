#!/usr/bin/env python
# coding: utf-8

# In[23]:


import requests
import json
import sys


# In[ ]:





# In[59]:



required_name = sys.argv[1]
split_required_name = required_name.split(' ') 
name_input = ''
for i in split_required_name:
    name_input += ' '+i.capitalize()
    
name_input = name_input.strip()

message_info = requests.get('https://q3b-602e6-default-rtdb.firebaseio.com/.json?orderBy="Person"&equalTo= "'+name_input+'" ')



# In[60]:





# In[61]:




# In[62]:


message_text=json.loads(message_info.text)



# In[ ]:





# In[ ]:





# In[ ]:





# In[63]:


for i in message_text:
    print(f"{message_text[i]['Time']}\t{message_text[i]['Message']}")


# In[ ]:




