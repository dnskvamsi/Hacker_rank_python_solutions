#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import numpy as np
N=int(input())
l=[]
for i in range(N):
    l.append(list(map(float,input().split(" "))))
print(round(np.linalg.det(l),2))

