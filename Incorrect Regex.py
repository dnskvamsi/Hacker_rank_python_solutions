#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import re
for _ in range(int(input())):
    ans = True
    try:
        reg = re.compile(input())
    except re.error:
        ans = False
    print(ans)

