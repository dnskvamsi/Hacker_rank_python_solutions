#!/usr/bin/env python
# coding: utf-8

# In[ ]:


s=int(input())
stu=set(list(map(int,input().split(" "))))
s1=int(input())
stu1=set(list(map(int,input().split(" "))))
k=stu.difference(stu1)
print(len(list(k)))

