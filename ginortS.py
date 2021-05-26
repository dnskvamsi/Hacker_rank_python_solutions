#!/usr/bin/env python
# coding: utf-8

# In[ ]:


s=list(input())
up=list(filter(lambda x:x.isupper(),s))
up.sort()
lw=list(filter(lambda x:x.islower(),s))
lw.sort()
ev=list(filter(lambda x:x.isdigit() and int(x)%2==0,s))
ev.sort()
od=list(filter(lambda x:x.isdigit() and int(x)%2!=0,s))
od.sort()
print("".join(lw+up+od+ev))

