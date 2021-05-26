#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import math
a=float(input())
b=float(input())
c=pow(pow(a,2)+pow(b,2),1/2)
theta = math.acos(b/c)
print(str(round(math.degrees(theta)))+chr(176))

