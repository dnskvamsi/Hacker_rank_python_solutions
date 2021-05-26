#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import numpy as np
N,M= list(map(int,input().split(" ")))
l=[]
for i in range(N):
    l.append(list(map(int,input().split(" "))))
#print(np.sum(l,axis=0))
print(np.prod(np.sum(l,axis=0)))

