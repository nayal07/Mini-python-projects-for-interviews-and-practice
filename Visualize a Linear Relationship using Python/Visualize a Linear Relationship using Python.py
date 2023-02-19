#!/usr/bin/env python
# coding: utf-8

# Visualize a Linear Relationship using Python
# 
# When the value of variable increases or decreases with the increase or decrease in the value of another variable, then it is nothing but a linear relationship. When we visualize a linear relationship, it shows whether the relationship between the two features is linear or not.
# 
# You can use any data visualization library in Python to visualize a linear relationship. I prefer to use plotly as it provides interactive results. But as so many Python programmers use matplotlib for data visualization, I will show you how to visualize a linear relationship with Python using plotly and matplotlib.

# In[5]:


import pandas as pd
import numpy as np
import plotly.express as px
import matplotlib.pyplot as plt
import seaborn as sns
get_ipython().run_line_magic('matplotlib', 'inline')

df = pd.read_csv("Instagram data 2.csv", encoding='latin1')
df = df.dropna()
print(df.head())


# In[8]:


df1= pd.DataFrame(df)
df1


# Here’s how to visualize linear relationships by using the plotly library in Python:

# In[10]:


figure = px.scatter(data_frame=df1,
                   x="Impressions",
                   y="Likes",
                   size= "Likes",
                   trendline="ols",
                   title = "Relationship btw Impressions and likes")
figure.show()


# To visualize linear relationships using matplotlib, you have to use seaborn.regplot method. So here’s how to plot linear relationships by using the matplotlib library in Python:

# In[12]:


plt.figure(figsize=(11,9))
plt.style.use('fivethirtyeight')
plt.title("Relatioship btw Likes and Impression")
sns.regplot(x="Impressions", y="Likes", data = df1)
plt.show()


# In[ ]:




