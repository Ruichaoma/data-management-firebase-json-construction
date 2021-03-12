#!/usr/bin/env python
# coding: utf-8

# In[1]:


import json
import sys


# In[113]:


filenames = sys.argv[1]
output_json = sys.argv[2]
fields = ["Time","Person","Message"]
list1 = []


def split_data(s):
    temp = s.split()
    ans = ''
    k = ''
    i = 1
    while(temp[i][-1]!=':'):
        k+=temp[i]
        k+=" "
        i+=1
    k+=temp[i][:-1]
    
    return k
    
def split_data_info(s):
    temp = s.split()
    ans = ''
    k = ''
    l=0
    for i in range(len(temp)):       
        if temp[i][-1]==':':
            l=i
    while l < len(temp)-1:
        k+=temp[l+1]
        k+=' '
        l+=1   
    return k[:-1]


with open(filenames) as fh:
    l = 1
    for line in fh:
        description = list(line.strip().split(None, 4))
        dict1 = {}
        i=0
        while i<len(fields):
            dict1[fields[0]]= description[0]
            dict1[fields[1]]= split_data(line)
            dict1[fields[2]]= split_data_info(line)
            i = i + 1
        list1.append(dict1)
        

#out_file = open(output, "w") 
#json.dump(list1, out_file, indent = 0) 
#out_file.close()
with open(output_json, 'w') as output:
    json.dump(list1, output)
#file.close()

# In[114]:


with open(output_json) as f:
    data = json.load(f)

print(data)


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




