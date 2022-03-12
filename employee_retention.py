#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
df = pd.read_csv('Employee_Rentation.csv')
df.head()


# In[2]:


df.info()


# Assume, for each company, that the headcount starts from zero on 2011/01/23. Estimate employee headcount, for each company, on each day, from 2011/01/24 to 2015/12/13.That is, if by 2012/03/02 2000 people have joined company 1 and 1000 of them have already quit, then company headcount on 2012/03/02 for company 1 would be 1000.
# You should create a table with 3 columns: day, employee_headcount, company_id.

# In[3]:


df['join_date'],df['quit_date'] = pd.to_datetime(df['join_date']),pd.to_datetime(df['quit_date'])
time_range = pd.date_range('2011-01-24','2015-12-13') 


# In[4]:


company = df['company_id'].value_counts().reset_index().sort_values('index')['index'].to_list()
headcount = {}

for t in time_range:
    headcount[t] = [0 for i in range(len(company))]


# In[5]:


today = pd.to_datetime('2015-12-13')

for i in range(24702):
    start = df.iloc[i,5]
    end = df.iloc[i,6]
    company_id = df.iloc[i,1]
    for c in company:
        if company_id == c:
            if pd.isnull(end):
                for t in pd.date_range(start,today):
                    headcount[t][c-1] = headcount[t][c-1]+1
            else:
                for t in pd.date_range(start,end):
                    headcount[t][c-1] = headcount[t][c-1]+1


# In[35]:


my_list = []
for day in time_range:
    for c in company:
        my_list.append([day,headcount[day][c-1],c])


# In[36]:


df = pd.DataFrame(data = my_list, columns = ['Day','Headcount','CompanyId'])
df


# In[ ]:




