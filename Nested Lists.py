#!/usr/bin/env python
# coding: utf-8

# In[ ]:


if __name__ == '__main__':
    q=[]
    m=[]
    for _ in range(int(input())):
        name = input()
        score = float(input())
        q.extend([[name,score]])
        m.append(score)
    m.sort()
    q.sort()
    n=[]
    k=list(set(m))
    k.sort()
    for i,j in q:
        if(j==k[1]):
            print(i)

