#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import numpy
N,M=list(map(int,input().split(" ")))
l=[]
for i in range(N):
    l.append(list(map(int,input().split(" "))))
print(numpy.transpose(l))
print(numpy.array(l).flatten())

