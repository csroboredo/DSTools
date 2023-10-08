#!/usr/bin/env python
# coding: utf-8

# # Data Science Tools and Ecosystem

# In this notebook, Data Science Tools and Ecosystem are summarized.

# **Objectives:**
# 
#  - List data science languages
#  - List data science libraries
#  - Create a table of open-source development environment tools
#  - Arithmetic Expression in Python and examples
#  - Ways to convert minutes to hours

# ## Author
# Cátia

# Exercise 4 - Some of the popular languages that Data Scientists use are:
#    1. Python
#    2. R
#    3. SQL
#    4. Scala
#    5. Java
#    6. C++

# Exercise 5 - Some of commonly used libraries used by Data Scientists include:
#    1. Pandas
#    2. NumPy
#    3. MatplotLib
#    4. Scikit-Learn
#    5. Keras
#    6. TensorFlow
#    7. Pytorch
#    
#    Jupyter is not a library but it is a essential tool for Data Scientists.

# Exercise 6 -
# Three development environment open source used in data science
# 
# | Data Science Tools |
# |--------------------|
# | Jupyter Notebook   |
# | RStudio            |
# | Spyder             |

# ### Below are a few examples of evaluating arithmetic expressions in Python
# 
# ### Addition 
#     result = 10 + 5
#     result = 15
#     
# ### Subtraction
#     result = 10 + 5
#     result = 5
#     
# ### Multiplication
#     result = 10 * 5
#     result = 50
#     
# ### Division
#     result = 100 / 5
#     result = 20

# In[17]:


# Exercise 8 - This is a simple arithmetic expression to multiply then add integers

x = (3*4)+5
print (x)


# In[18]:


# Exercise 9 (1) - This will convert 200 minutes to hours by diving by 60

minutes = 200
hours = minutes / 60
print(hours)


# In[19]:


# Exercise 9 (2) - This will convert 200 minutes to hours by diving by 60

minutes = 200
hours = minutes / 60
format_hours = "{:.0f}:{:02.0f}".format(hours, (hours % 1)*60)
print(format_hours)


# In[20]:


# Exercise 9 (3) - This will convert 200 minutes to hours by diving by 60

total_minutes = 200
hours = total_minutes // 60
minutes = total_minutes % 60

print(f"{total_minutes} minutes equals {hours} hours and {minutes} minutes.")


# In[ ]:




