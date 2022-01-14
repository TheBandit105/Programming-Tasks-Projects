#!/usr/bin/env python
# coding: utf-8

# # CS3PP19 - Programming in Python for Data Science - Practical 1
# 
# ## Data Types and Operators

# Follow the instructions to complete each of these tasks, and use the testing code cells to check your answers. This set of exercises focuses on writing basic Python code, specificaly python data types and operators.
# 
# The relevant materials for these exercises is Lecture2-DataTypes-ComparisonOperators-FlowControl.
# 
# This is not assessed but will help you gain practical experience for the exam and coursework.
# 
# *Feel free to work on them in any order, and focus on the ones you find most challening or interesting!*

# ### A Classic or Cliche?
# 
# Print Hello World!

# In[1]:


'Hello World!'


# ### Variables
# 
# In python there is no need to declare a type.
# 
# Create the following variables:
#     - Name
#     - Age
# 
# Use your own name and age and then print both.

# In[2]:


name = 'Shavin'
age = '22'

print('Hello, my name is ' + name + ' and I am ' + age + ' years old.')


# ## Array Types in Python
# 
# - Lists
# - Tuple
# - Set
# - Dictionary
# 
# ### Lists
# 
# Lists are declared using [] and they are both ordered and changeable.
# 
# 1.1 Declare a list called modules of the modules you are studing this year and print them.

# In[5]:


modules = ['AI', 'Data Science', 'Distributed Systems & Parallel Computing', 
           'Image Analysis', 'Individual Project', 'Programming in Python', 
           'VR', 'Social, Legal & Ethical points Computing', 'Visual Intelligence']
print(modules)


# #### Accessing lists
# 
# 1.2 Access using the index - print the 3rd module in the list.
#     * note whether python uses 0 or 1 indexing as a comment.
# 
# 

# In[7]:


print(modules[2])

# Python uses 0 indexing.


# 1.3 Negative indexing - this allows you to access from the end of the list, print the 3rd from last module in the list.

# In[8]:


print(modules[-3])


# #### Working with lists
# 
# 1.4 Create a second list called lastyear with the modules you studied last year.

# In[9]:


modulesTwo = ['Algorithms & OS', 'Compilers', 'Computer Architecture & Networking', 
              'Databases & Info Sec', 'HCI', 'Java', 'Systems Design', 'SOSA']
print(modulesTwo)


# 1.5 Join both lists into one. 
# 
# HINT: there are 3 ways you cold do this...

# In[10]:


print(modules + modulesTwo)


# In[3]:


modules = ['AI', 'Data Science', 'Distributed Systems & Parallel Computing', 
           'Image Analysis', 'Individual Project', 'Programming in Python', 
           'VR', 'Social, Legal & Ethical points Computing', 'Visual Intelligence']
modulesTwo = ['Algorithms & OS', 'Compilers', 'Computer Architecture & Networking', 
              'Databases & Info Sec', 'HCI', 'Java', 'Systems Design', 'SOSA']

for x in modulesTwo:
  modules.append(x)

print(modules)


# In[10]:


modules = ['AI', 'Data Science', 'Distributed Systems & Parallel Computing', 
           'Image Analysis', 'Individual Project', 'Programming in Python', 
           'VR', 'Social, Legal & Ethical points Computing', 'Visual Intelligence']
modulesTwo = ['Algorithms & OS', 'Compilers', 'Computer Architecture & Networking', 
              'Databases & Info Sec', 'HCI', 'Java', 'Systems Design', 'SOSA']

modules.extend(modulesTwo)
print(modules)


# ### Dictionaries
# 
# Dictionaries are declared using {} and are unordered, changeable and indexed. They contain key and value pairs.
# 
# 2.1 Declare a dictionary called favmod with the information for your favourite module with the following information:
#     - Name
#     - Year
#     - Lecturer
# 
# Then print the dictionary.

# In[1]:


favmod = {'Name':'Virtual Reality',
          'Year': 'Final Year',
          'Lecturer':'Ritchard Mitchell'}
print(favmod)


# #### Accessing Dictionaries
# 
# 2.2 Get the value for the year of study from the dictionary and print it.

# In[2]:


print(favmod['Year'])


# #### Nesting Dictionaries
# 
# 2.3 Declare a second dictionary called secmod with your second favourite module details.
# 

# In[3]:


secmod = {'Name':'Python for Data Science','Year':'Final Year','Lecturer':'Miguel Sanchez'}
print(secmod)


# 2.4 Create a third dictionary containing the two you previously created called rankedmod and print it.

# In[5]:


rankedmod = {'favmod': favmod,
             'secmod': secmod}

print(rankedmod)


# ### IF...ELSE and Loops in Python
# 
# Python works with indentation rather than brackets to define what is within a IF statement or loop.
# 
# 3.1 Create an if else statement that prints a sentence describing the relationship between the two numbers below (e.g x is greater/smaller than y).

# In[29]:


a = 46
b = 99

if a < b:
    print('a is smaller than b')
else:
    print('a is greater than b')
    
x = 75
y = 13

if x < y:
    print('x is smaller than y')
else:
    print('x is greater than y')


# 3.2 Write a loop (for and while) that prints the values in the modules list you created earlier.

# In[7]:


modules = ['AI', 'Data Science', 'Distributed Systems & Parallel Computing', 
           'Image Analysis', 'Individual Project', 'Programming in Python', 
           'VR', 'Social, Legal & Ethical points Computing', 'Visual Intelligence']
modulesTwo = ['Algorithms & OS', 'Compilers', 'Computer Architecture & Networking', 
              'Databases & Info Sec', 'HCI', 'Java', 'Systems Design', 'SOSA']

modules.extend(modulesTwo)

for a in modules:
    print(a)


# # Operators
# 
# Arithmetic operators in python should be familiar, however logic operators are a little different...
# in Python the words AND, OR and NOT are used as logic operators!
# 
# 4.1 Create and if statement whith multiple conditions using the variables a and b from above and c and d provided below.

# In[6]:


a = 46
b = 99
c = 100
d = 6

if a < b and c > d:
    print('Both true')
else:
    print('False')
    
if a < c or b < d:
    print('One is true')
else:
    print('False')
    
if not a == 46:
     print('True')
else:
     print('False')


# ## Challenge : Odd or Even?
# 
# Write some code that prints out a different message for each number in the list below depending on whether it is odd or even.
# 
# 

# In[8]:


challenge = [2,5,76,89,77,103,24,65,66,12,1,0,19]

for x in challenge:
    if (x % 2) == 0:
         print("{0} is Even number".format(x))  
    else:
         print("{0} is Odd number".format(x))  


# In[ ]:




