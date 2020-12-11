#!/usr/bin/env python
# coding: utf-8

# In[1]:


class point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other): 
        if isinstance(other, point):
            return point(self.x + other.x, self.y + other.y)
        elif isinstance(other, tuple):
            return point(self.x + other[0], self.y + other[1])

    def __repr__(self):
        return f'Point ({self.x}, {self.y})'


# In[2]:


p1 = point(4,5)
p2 = point(3,2)
p3 = (1,1)


# In[3]:


p1 + p3


# In[4]:


p1 + p2


# In[5]:


p1 + p2 + p3


# In[ ]:




