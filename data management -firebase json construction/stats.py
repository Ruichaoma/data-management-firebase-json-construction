#!/usr/bin/env python
# coding: utf-8

# In[6]:


import json
import sys
import re


# In[7]:


input_txt = sys.argv[1]
output_json = sys.argv[2]

file = open(input_txt, 'r')

people_chat_dict = {}
for i in file:
    information_total = i.replace("\n","").split()
    chatting_info = (" ").join(information_total[1:])
    people = chatting_info.split(":")[0]
    if people not in people_chat_dict.keys():
        people_chat_dict[people] = 1
    else:
        people_chat_dict[people] = people_chat_dict[people]+1
jsonfile = []
for name in people_chat_dict:
    json_stat = {}
    json_stat["Person"] = name
    json_stat["Message"] = people_chat_dict[name]
    jsonfile.append(json_stat)


with open(output_json, 'w') as output:
    json.dump(jsonfile, output)
file.close()

with open(output_json) as f:
    data = json.load(f)
print(data)

# In[ ]:





# In[ ]:




