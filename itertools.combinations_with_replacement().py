#!/usr/bin/env python
# coding: utf-8

# In[ ]:


v=input().split(" ")
na=v[0]
na=list(na)
na.sort()
na="".join(na)
i=int(v[1])
l=[]
from itertools import combinations_with_replacement as cwr
l.extend(list(cwr(na,i)))
for k in range(len(l)):
    l[k]="".join(l[k])
for p in l:
    print(p)

