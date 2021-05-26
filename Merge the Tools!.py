#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def merge_the_tools(string, k):
    from textwrap import wrap
    t=wrap(string,k)
    u=[]
    for i in t:
        k=[]
        for j in list(i):
            if j not in k:
                k.append(j)
        print("".join(k))

if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)

