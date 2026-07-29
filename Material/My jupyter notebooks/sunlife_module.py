#!/usr/bin/env python
# coding: utf-8

# In[1]:


def check_even(num):
    if num%2==0:
        return "Even"
    else:
        return "Odd"


# In[2]:


def greetings(name):
    return "Welcome "+ name


# In[3]:


def fact(num):
    fact=1
    for i in range(1,num+1):
        fact = fact*i
    return fact


# In[ ]:




