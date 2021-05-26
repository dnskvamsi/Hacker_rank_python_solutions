#!/usr/bin/env python
# coding: utf-8

# In[ ]:


regex_pattern = r"[,.]"

import re
print("\n".join(re.split(regex_pattern, input())))

