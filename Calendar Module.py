#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# Enter your code here. Read input from STDIN. Print output to STDOUT
import calendar
m,d,y=list(map(int,input().split()))
a = calendar.weekday(y, m, d)
print(calendar.day_name[a].upper())

