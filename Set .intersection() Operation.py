#!/usr/bin/env python
# coding: utf-8

# In[ ]:


s1=int(input())
stu=set(list(map(int,input().split(" "))))
s2=int(input())
stu2=set(list(map(int,input().split(" "))))
k=stu.intersection(stu2)
print(len(list(k)))

