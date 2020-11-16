#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# In[3]:


data = pd.read_csv("C:/Users/heyda/Desktop/7learn data science/AAPL.csv")
data


# In[4]:


data.tail()


# In[5]:


data.info()


# In[6]:


data.describe()


# In[8]:


data['Date'] = data['Date'].apply(pd.to_datetime)


# In[9]:


data['Date']


# In[10]:


pd.to_datetime('2013-12-10')


# In[11]:


data.info()


# In[12]:


data.set_index('Date', inplace= True)


# In[13]:


data.head()


# In[14]:


data['Open'].plot()


# In[15]:


data['Close'].plot()


# In[16]:


data['Volume'].plot()


# In[17]:


data.head()


# In[19]:


# mean for Open for Months
data.resample(rule = 'M').mean()   #pandas resample


# In[21]:


data.resample(rule = 'M').mean()['Open'].plot()


# In[20]:


# min for Open for Months
data.resample(rule = 'M').min()   #pandas resample


# In[22]:


data.resample(rule = 'M').min()['Open'].plot()


# In[24]:


# Annual
data.resample(rule = 'A').mean()['Volume'].plot()


# In[25]:


data.resample(rule = 'A').mean()['Open'].plot()


# In[26]:


# Quantile
data.resample(rule = 'Q').mean()['Open'].plot()


# In[27]:


data.resample(rule = 'Q').mean()['Volume'].plot()


# In[29]:


data.resample(rule = 'Q').mean()['Open'].plot(kind = 'bar')  # Mean of seasons Open price


# In[30]:


data.resample(rule = 'Q').mean()['Volume'].plot(kind = 'bar')  # Mean of seasons Volume


# In[31]:


data.resample(rule = 'Q').min()['Volume'].plot(kind = 'bar')  # Min of seasons Volume


# In[ ]:




