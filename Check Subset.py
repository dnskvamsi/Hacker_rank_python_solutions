#!/usr/bin/env python
# coding: utf-8

# In[ ]:


for _ in range(int(input())):
    na, A, nb, B = input(), set(input().split()), input(), set(input().split())
    print(A.issubset(B))

