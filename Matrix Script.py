#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import math
import os
import random
import re
import sys
first_multiple_input = input().rstrip().split()

n = int(first_multiple_input[0])

m = int(first_multiple_input[1])

matrix = []

for _ in range(n):
    matrix_item = input()
    matrix.append(matrix_item)
str1=[]
for j in range(m):
    for i in range(n):
        str1.append(matrix[i][j])
str1="".join(str1)
q1="".join(re.findall("[a-zA-Z0-9].*[a-zA-Z0-9]",str1))
q=q1.replace("!"," ").replace("@"," ").replace("#"," ").replace("$"," ").replace("%"," ").replace("&"," ")
print(str1.replace(q1,q))

