#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def count_substring(string, sub_string):
    count=0
    while sub_string in string:
        i = string.find(sub_string)
        string = string[:i] + string[i + 1:]
        count += 1
    return count

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)

