#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def average(array):
    s=list(set(array))
    return round(sum(s)/len(s),3)

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)

