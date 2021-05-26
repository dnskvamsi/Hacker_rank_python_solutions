#!/usr/bin/env python
# coding: utf-8

# In[ ]:


n=int(input())
for i in range(n):
    m,n=input().split(" ")
    try:
        print(int(m)//int(n))
    except Exception as e:
        print("Error Code:",e)

