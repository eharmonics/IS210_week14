#!/usr/bin/env python
# coding: utf-8

# In[24]:


def fibonacci(maxint):
    a, b = 0, 1
    series=[]
    while a < maxint:
        series.append(a)
        a, b = b, a+b
    return series


# In[25]:


fibonacci(10)


# In[28]:


def lexicographics(to_analyze):
    lines=to_analyze.split('\n')
    words=[]
    for i in lines:
        word=i.split()
        words.append(len(word))
    return max(words),min(words),sum(words)/len(words)


# In[29]:


lexicographics('''Don't stop believing,
Hold on to that feeling!''')


# In[ ]:




