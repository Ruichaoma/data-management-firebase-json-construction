#!/usr/bin/env python
# coding: utf-8

# In[1]:


import csv
import json
import sys 


# In[30]:


input_file = sys.argv[1]
output_file = sys.argv[2]

json_info = []
with open(input_file) as csv_file:
    read = csv.reader(csv_file, delimiter=',')
    h = next(read)
    if h != None:
        for i in read:
            name = i[0]
            name_list = name.split(", ")
            name = name_list[1] + " " + name_list[0]
            json_info.append({"Name":name,"Participating from": i[1]})
with open(output_file, 'w') as outfile:
    json.dump(json_info, outfile)


# In[31]:


with open(output_file) as f:
    data = json.load(f)
print(data)


# In[ ]:




