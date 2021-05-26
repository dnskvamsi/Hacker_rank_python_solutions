#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from collections import defaultdict
d = defaultdict(list)
list1=[]

m, n = list(map(int,input().split(" ")))

for i in range(0,m):
    d[input()].append(i+1) 

for i in range(0,n):
    list1=list1+[input()]  

for i in list1: 
    if i in d:
        print(" ".join( map(str,d[i])))
    else:
        print("-1")

