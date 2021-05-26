#!/usr/bin/env python
# coding: utf-8

# In[ ]:


s1=int(input())
stu=list(map(int,input().split(" ")))
s2=int(input())
stu2=list(map(int,input().split(" ")))
k=set(stu).union(set(stu2))
print(len(list(k)))

