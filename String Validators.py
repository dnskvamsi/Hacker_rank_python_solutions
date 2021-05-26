#!/usr/bin/env python
# coding: utf-8

# In[ ]:


if __name__ == '__main__':
    s = input()
    p=list(s)
    k=list(map(lambda x:x.isalnum(),p))
    print(bool(sum(k)))
    k=list(map(lambda x:x.isalpha(),p))
    print(bool(sum(k)))
    k=list(map(lambda x:x.isdigit(),p))
    print(bool(sum(k)))
    k=list(map(lambda x:x.islower(),p))
    print(bool(sum(k)))
    k=list(map(lambda x:x.isupper(),p))
    print(bool(sum(k)))

