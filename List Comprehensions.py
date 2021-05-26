#!/usr/bin/env python
# coding: utf-8

# In[ ]:


if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
    l=[]
    for i in range(0,x+1):
        for j in range(0,y+1):
            for k in range(0,z+1):
                l.extend([[i,j,k]])
    p=[]
    for i in l:
        if(sum(i)!=n):
            p.extend([i])
    print(p)

