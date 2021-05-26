#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import re
for _ in range(int(input())):
    if(bool(re.match(r'^[789][0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9]$', input()))):
        print("YES")
    else:
        print("NO")

