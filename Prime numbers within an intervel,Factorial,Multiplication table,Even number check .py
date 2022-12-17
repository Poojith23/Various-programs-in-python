#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Python program to display all the prime numbers within an interval

lower = 900
upper = 1000
print("Prime numbers between", lower, "and", upper, "are:")
for num in range(lower, upper + 1):
   if num > 1:
       for i in range(2, num):
           if (num % i) == 0:
               break
       else:
           print(num)


# In[3]:


#Python program to find the factorial of a Number

num = int(input("Enter the number:"))
factorial = 1
if num < 0:
   print("Sorry, factorial does not exist for negative numbers")
elif num == 0:
   print("The factorial of 0 is 1")
else:
   for i in range(1,num + 1):
       factorial = factorial*i
   print("The factorial of",num,"is",factorial)


# In[7]:


# Multiplication table (from 1 to 10) in Python

num = int(input("Enter the number:"))
for i in range(1, 11):
   print(num, 'x', i, '=', num*i)


# In[8]:


x = 10
if x != 0:
   if x % 2 == 0:
      print('even number')
   else:
      print('odd number')
elif x == 0:
   print('equal to zero')
elif x > 0:
  for i in range(2,x):
     if i % 2 == 0:
        print('not a prime number')
     else:
        print('prime number')
else:
   print('less than zero')


# In[ ]:




