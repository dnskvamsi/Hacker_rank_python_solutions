#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def print_rangoli(size):
    # your code goes here
    alpha=[chr(i) for i in range(97,123)]
    L = []
    for i in range(n):
        s = "-".join(alpha[i:n])
        L.append((s[::-1]+s[1:]).center(4*n-3, "-"))
    print('\n'.join(L[:0:-1]+L))
if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)

