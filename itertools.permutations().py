#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from itertools import permutations
x=input().split()
s=list(x[0])
s.sort()
l=["".join(i) for i in list(permutations(s,int(x[1])))]
print("\n".join(l))

