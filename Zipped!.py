#!/usr/bin/env python
# coding: utf-8

# In[ ]:


N,X=list(map(int,input().split(" ")))
l=[]
for i in range(X):
    l.append(list(map(float,input().split(" "))))
for i in zip(*l):
    print(round(sum(i)/len(i),1))

