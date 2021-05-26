#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def print_formatted(number):
    w=len(bin(number).replace("0b",""))
    for i in range(1,number+1):
        d=str(i).rjust(w," ")
        o=oct(i)
        o=o.replace("0o","").rjust(w," ")
        h=hex(i)
        h=h.replace("0x","").upper().rjust(w," ")
        b=bin(i)
        b=b.replace("0b","").rjust(w," ")
        print(d,o,h,b)

if __name__ == '__main__':
    n = int(input())
    print_formatted(n)

