#!/usr/bin/env python
# coding: utf-8

# In[ ]:


if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    p=set(arr)
    k=list(p)
    k.sort()
    print(k[-2])

