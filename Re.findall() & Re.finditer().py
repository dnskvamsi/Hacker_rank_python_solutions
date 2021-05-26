#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import re
s = '[qwrtypsdfghjklzxcvbnm]'
a = re.findall('(?<=' + s +')([aeiou]{2,})' + s, input(), re.I)
print('\n'.join(a or ['-1']))

