#!/usr/bin/env python
# coding: utf-8

# ## Write a Python program to create a lambda function that adds 25 to a given number passed in as an argument.
# 
# 
# 
# sample input: 10
# 
# sample output: 35

# In[2]:


Add_25 = lambda x : x+25


# In[3]:


Add_25(85)


# ## Write a Python program to triple all numbers of a given list of integers. Use Python map.
# 
# 
# 
# sample list: [1, 2, 3, 4, 5, 6, 7]
# 
# 
# 
# Triple of list numbers:
# 
# [3, 6, 9, 12, 15, 18, 21]

# In[19]:


def triplenum(List):
    return List*3


# In[21]:


print(list(map(triplenum,[1,2,3,4,5])))


# ## Write a Python program to square the elements of a list using map() function.
# 
# 
# 
# Sample List: [4, 5, 2, 9]
# 
# Square the elements of the list:
# 
# [16, 25, 4, 81]

# In[22]:


def findsqr(List):
    return List**2


# In[24]:


print(list(map(findsqr,[8,9,4,6,2,11])))


# In[2]:


print(list(map(lambda i : i**2,[8,9,4,6,2,11])))


# In[ ]:




