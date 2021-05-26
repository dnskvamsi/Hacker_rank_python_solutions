#!/usr/bin/env python
# coding: utf-8

# In[ ]:


k=int(input())
l=list(map(int,input().split(" ")))
s=set(l)
print(((sum(s)*k)-(sum(l)))//(k-1))

