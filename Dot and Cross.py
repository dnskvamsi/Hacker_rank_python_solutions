#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import numpy as np
N=int(input())
A=[]
B=[]
for i in range(N):
    A.extend([list(map(int,input().split(" ")))])
for j in range(N):
    B.extend([list(map(int,input().split(" ")))])
print(np.matmul(A,B))

