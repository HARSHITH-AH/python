#!/usr/bin/env python
# coding: utf-8

# In[1]:


class student:
    
    def __init__(self, name, usn, m1, m2, m3):
        self.name = name
        self.usn = usn
        self.m1 = m1
        self.m2 = m2
        self.m3 = m3
        
    def __str__(self):
        return f"Name: {self.name} \nUSN: {self.usn} \nSubject 1 marks: {self.m1} \nSubject 2 marks: {self.m2} \nSubject 3 marks: {self.m3} \n"
    
    def increment_marks(self, bonus=10):
        self.m1 += bonus/100 * self.m1
        self.m2 += bonus/100 * self.m2
        self.m3 += bonus/100 * self.m3
        if self.m1 > 100:
            self.m1 = 100
        if self.m2 > 100:
            self.m2 = 100
        if self.m3 > 100:
            self.m3 = 100
        
    def percentage(self):
        avg = (self.m1 + self.m2 + self.m3) / 3
        print(f"Percentage: {round(avg, 2)}")


# In[6]:


har=student("harshith", "4VV18CS001",71,77,90)
print(har)


# In[7]:


har.percentage()


# In[8]:


har.increment_marks(5)
print(har)


# In[9]:


har.increment_marks()
print(har)


# In[10]:


har.increment_marks()
print(har)


# In[11]:


har.percentage()


# In[ ]:




