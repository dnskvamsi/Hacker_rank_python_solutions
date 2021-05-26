#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import numpy as np
np.set_printoptions(legacy='1.13')
N,M=list(map(int,input().split(" ")))
if(N==M):
    print(np.identity(N))
else:
    print(np.eye(N,M))

