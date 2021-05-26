#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from itertools import product
x=list(map(int,input().split(" ")))
y=list(map(int,input().split(" ")))
print(" ".join(list(map(str,(list(product(x,y)))))))

