#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import numpy as np
N, M = list(map(int, input().split()))
l1=[]
for i in range(M):
    l1.append(list(map(int,input().split(" "))))
print(np.mean(l1,axis=1))
print(np.var(l1,axis=0))
print(round(np.std(l1,axis=None),11))

