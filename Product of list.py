#!/usr/bin/env python
# coding: utf-8

# In[1]:


list=[1,2,3]
result=1
for i in list:
    result=result*i
print(result)


# In[2]:


import numpy
list=[1,2,3]
multiply=numpy.prod(list)
print(multiply)


# In[3]:


def multiplyList(myList):
    result = 1
    for x in myList:
        result = result * x
    return result
list1 = [1, 2, 3]
list2 = [3, 2, 4]
print(multiplyList(list1))
print(multiplyList(list2))


# In[4]:


import math
list1 = [1, 2, 3]
list2 = [3, 2, 4]
result1 = math.prod(list1)
result2 = math.prod(list2)
print(result1)
print(result2)


# In[ ]:




