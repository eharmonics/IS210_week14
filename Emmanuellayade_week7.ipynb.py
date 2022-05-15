#!/usr/bin/env python
# coding: utf-8

# In[18]:


BP = input('What is your blood pressure? ')

BP = float(BP)

if 0 <= BP <= 89:
    BP_STATUS = 'Low'
elif 90 <= BP <= 119:
    BP_STATUS = 'Ideal'
elif 120 <= BP <= 139:
    BP_STATUS = 'Warning'
elif 140 <= BP <= 159:
    BP_STATUS = 'High'
elif 160 <= BP:
    BP_STATUS = 'Emergency'

print('Your status is currently:{}!'.format(BP_STATUS))


# In[ ]:




