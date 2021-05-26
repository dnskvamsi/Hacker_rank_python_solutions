#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import textwrap

def wrap(string, max_width):
    l=textwrap.wrap(string,max_width)
    for i in l[0:-1]:
        print(i)
    return l[-1]

if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)

