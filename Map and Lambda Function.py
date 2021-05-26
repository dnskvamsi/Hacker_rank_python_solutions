#!/usr/bin/env python
# coding: utf-8

# In[ ]:


cube = lambda x: x*x*x
def fibonacci(n):
    l=[0,1]
    p=[0]
    if(n==0):
        return []
    if(n==1):
        return p
    if(n==2):
        return l
    for i in range(n-2):
        l.append(l[-1]+l[-2])
    return l

if __name__ == '__main__':
    n = int(input())
    print(list(map(cube, fibonacci(n))))

