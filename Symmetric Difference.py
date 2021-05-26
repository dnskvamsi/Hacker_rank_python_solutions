#!/usr/bin/env python
# coding: utf-8

# In[ ]:


M=int(input())
a=set(list(map(int,input().split(" "))))
N=int(input())
b=set(list(map(int,input().split(" "))))
f=list(a.symmetric_difference(b))
f.sort()
for i in f:
    print(i)

