#!/usr/bin/env python
# coding: utf-8

# In[ ]:


x=list(map(int,input().split()))
d=(x[0])//2
s=".|."
for i in range(0,d):
    print(s.center(x[1],"-"))
    s=s+2*".|."
print("WELCOME".center(x[1],"-"))
k=6
for i in range(0,d):
    s=s[k:]
    print(s.center(x[1],"-"))

