#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import numpy as np
n = list(map(float,input().split()));
m = input();
print(np.polyval(n,int(m)));

