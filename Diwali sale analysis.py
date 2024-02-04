#!/usr/bin/env python
# coding: utf-8

# In[4]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')
import seaborn as sns


# In[5]:


df=pd.read_csv('Diwali Sales Data.csv',header= 0,
                        encoding= 'unicode_escape')


# In[6]:


df


# In[7]:


df.shape


# In[8]:


df.head()


# In[9]:


df.info()


# In[10]:


df


# In[11]:


df.info()


# In[12]:


pd.isnull(df).sum()


# In[13]:


df


# In[14]:


df.drop(['Status','unnamed1'],axis=1,inplace=True)


# In[15]:


df


# In[16]:


pd.isnull(df).sum()


# In[17]:


df.dropna(inplace=True)


# In[18]:


df


# In[19]:


df['Amount'].dtype


# In[20]:


df['Amount']=df['Amount'].astype('int')


# In[21]:


df['Amount'].dtype


# In[22]:


df.rename(columns={'Marital_Status': 'Shaadi'},inplace=True)


# In[23]:


df


# # EDA

# In[24]:


ax=sns.countplot(x='Gender',data=df)


# In[25]:


ax=sns.countplot(x='Gender',data=df)

for bars in ax.containers:
    ax.bar_label(bars)


# another example of this plot

# In[26]:


virat_kohli_runs=pd.Series({'runs':[0,100,50,0,100,50,100,50,0,0,0,50,50,50,100,100,100]})


# In[27]:


virat_kohli_runs


# In[28]:


ax=sns.countplot(x='runs',data=virat_kohli_runs)

for bars in ax.containers:
    ax.bar_label(bars)


# Countinue to EDA

# In[29]:


ax=sns.countplot(x='Gender',data=df)

for bars in ax.containers:
    ax.bar_label(bars)


# In[30]:


sales_gen=df.groupby(['Gender'],as_index=False)['Amount'].sum().sort_values(by='Amount',ascending=False)


# In[31]:


sns.barplot(x='Gender',y='Amount',data=sales_gen)


# From above both the graph we can see that female are more in number for purchasing than man and also they 
# spend more amount of money than men

# In[32]:


df


# In[33]:


ax=sns.countplot(data=df,x='Age Group',hue='Gender')

for bars in ax.containers:
    ax.bar_label(bars)


# In[34]:


sales_age=df.groupby(['Age Group'],as_index=False)['Amount'].sum().sort_values(by='Amount',ascending=False)


# In[35]:


sns.barplot(x='Age Group',y='Amount',data=sales_age)


# From the graph we can see that most are women between 26-35 who spend most of money as coompare to the others.

# # Let's find the state

# In[36]:


sales_state=df.groupby(['State'],as_index=False)['Orders'].sum().sort_values(by='Orders',ascending=False).head(10)

sns.set(rc={'figure.figsize':(22,11)})
sns.barplot(data=sales_state,x='State',y='Orders')


# Total amount from state

# In[37]:


sales_state=df.groupby(['State'],as_index=False)['Amount'].sum().sort_values(by='Amount',ascending=False).head(10)

sns.set(rc={'figure.figsize':(22,11)})
sns.barplot(data=sales_state,x='State',y='Amount')


# From above graph we can see that most buyers or most active state is uttar pardesh in terms of buying goods

# # Marital status

# In[38]:


ax=sns.countplot(data=df,x='Shaadi')

for bars in ax.containers:
    ax.bar_label(bars)


# From above graph we can see that most buyers are from married women

# # Occupation

# In[39]:


sns.set(rc={'figure.figsize':(20,5)})
ax=sns.countplot(data=df,x='Occupation')
for bars in ax.containers:
    ax.bar_label(bars)


# From above graph we can see that most buyers are from IT sector 

# # Prodouct category 

# In[45]:


sns.set(rc={'figure.figsize':(24,8)})
ax=sns.countplot(data=df,x='Product_Category')

for bars in ax.containers:
    ax.bar_label(bars)


# In[50]:


sales_state=df.groupby(['Product_Category'],as_index=False)['Amount'].sum().sort_values(by='Amount',ascending=False).head(7)

sns.set(rc={'figure.figsize':(30,10)})
ax=sns.barplot(data=sales_state,x='Product_Category',y='Amount')


# From above graph we can see that food is the prodict which is mostly sold.

# # Conclusion:

# Married women age group 26-35 yrs,from UP Maharastra and IT sector are more likely to buy product from food cothing and Electronic category.

# In[ ]:




