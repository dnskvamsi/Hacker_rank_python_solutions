#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import re
m = re.findall(r"([A-Za-z0-9])\1+",input())
if m:
    print(m[0])
else:
    print(-1)

