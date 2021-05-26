#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import numpy as np
N,M=list(map(int,input().split(" ")))
l=[]
for i in range(N):
    l.append(list(map(int,input().split(" "))))
print(max(np.min(l,axis=1)))

