#!/usr/bin/env python
# coding: utf-8

# In[ ]:


N, headers, total = int(input()), list(input().split()), 0
for i in range(N):
    total += int(list(input().split())[headers.index('MARKS')])
print(total/N)

