#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import numpy as np
l=list(map(float,input().split(" ")))
np.set_printoptions(legacy="1.13")
print(np.floor(l))
print(np.ceil(l))
print(np.rint(l))

