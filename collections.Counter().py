#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import collections

nS = int(input())
s = collections.Counter(map(int, input().split()))
nC = int(input())

inc = 0

for i in range(nC):
    size, price = map(int, input().split())
    if s[size]: 
        inc += price
        s[size] -= 1
print(inc)

