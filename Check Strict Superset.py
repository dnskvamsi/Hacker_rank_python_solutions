#!/usr/bin/env python
# coding: utf-8

# In[ ]:


a = set(input().split())
print(all(a > set(input().split()) for i in range(int(input()))))

