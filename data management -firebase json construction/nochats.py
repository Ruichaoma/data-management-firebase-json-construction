#!/usr/bin/env python
# coding: utf-8

# In[2]:


import csv
import json
import sys


# In[11]:


input_file_txt = sys.argv[1]
input_file_csv = sys.argv[2]
output_file = sys.argv[3]

all_chat_info = open(input_file_txt, 'r')
people_chat_lst = []
for i in all_chat_info:
    useful_info = i.replace("\n","").split()
    chat_info = (" ").join(useful_info[1:])
    chat_info_split = chat_info.split(":")
    people = chat_info_split[0]
    if people not in people_chat_lst:
        people_chat_lst.append(people)

all_chat_info.close()
csv_lst = []
with open(input_file_csv) as csv_reading:
    read = csv.reader(csv_reading, delimiter=',')
    h = next(read)
    if h != None:
        for j in read:
            name = j[0]
            name_list = name.split(", ")
            name = name_list[1] + " " + name_list[0]
            if name not in people_chat_lst:
                csv_lst.append({"Name":name,"Participating from": j[1]})
                
with open(output_file, 'w') as output:
    json.dump(csv_lst, output)
    
with open(output_file) as f:
    data = json.load(f)
print(data)


# In[12]:





# In[ ]:




