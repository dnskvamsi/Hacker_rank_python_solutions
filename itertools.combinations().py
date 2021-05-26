#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# Enter your code here. Read input from STDIN. Print output to STDOUT
v=input().split(" ")
na=v[0]
na=list(na)
na.sort()
na="".join(na)
i=int(v[1])
l=[]
from itertools import combinations
for j in range(1,i+1):
    l.extend(list(combinations(na,j)))
for k in range(len(l)):
    l[k]="".join(l[k])
for p in l:
    print(p)

