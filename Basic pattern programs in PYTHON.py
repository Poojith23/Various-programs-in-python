#!/usr/bin/env python
# coding: utf-8

# In[1]:


for i in range(0, 5):
    for j in range(0, i+1):
        print("* ",end="")
    print()


# In[2]:


#Python Program for printing pyramid pattern using stars
a = 8
for i in range(0, 5):
    for j in range(0, a):
        print(end=" ")
    a = a - 2
    for j in range(0, i+1):
        print("* ", end="")
    print()


# In[3]:


# Python Pyramid pattern using a star pattern

k = 16
l = 1
for i in range(0, 5):
    for j in range(0, k):
        print(end=" ")
    k = k - 4
    for j in range(0, l):
        print("* ", end="")
    l = l + 2
    print()


# In[1]:


# Python Numeric Pattern Example 1

k = 1
for i in range(0, 5):
    for j in range(0, i+1):
        print(k, end=" ")
        k = k + 1
    print()


# In[ ]:




