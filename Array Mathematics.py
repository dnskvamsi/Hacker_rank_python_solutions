#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import numpy as np
N,M=list(map(int,input().split(" ")))
A=[]
B=[]
for i in range(N):
    A.append(list(map(int,input().split(" "))))
for i in range(N):
    B.append(list(map(int,input().split(" "))))
print(np.add(A, B))
print(np.subtract(A, B))
print(np.multiply(A, B))
c=np.divide(A, B)
print(np.array(c,int))
print(np.mod(A, B))
print(np.power(A, B))

