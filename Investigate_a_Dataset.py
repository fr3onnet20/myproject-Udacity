#!/usr/bin/env python
# coding: utf-8

# 
# ## TMDb movie data
# 
# ## Table of Contents
# <ul>
# <li><a href="#intro">Introduction</a></li>
# <li><a href="#wrangling">Data Wrangling</a></li>
# <li><a href="#eda">Exploratory Data Analysis</a></li>
# <li><a href="#conclusions">Conclusions</a></li>
# </ul>

# # <a id='intro'></a>
# ## Introduction
# 
# 
# ### Dataset Description 
# 
# This data set contains information
# about 10,000 movies collected from
# The Movie Database (TMDb),
# including user ratings and revenue.
# ● Certain columns, like ‘cast’
# and ‘genres’, contain multiple
# values separated by pipe (|)
# characters.
# ● There are some odd characters
# in the ‘cast’ column. Don’t worry
# about cleaning them. You can
# leave them as is.
# ● The final two columns ending
# with “_adj” show the budget and
# revenue of the associated movie
# in terms of 2010 dollars,
# accounting for inflation over
# time.
# 
# 
# ### Question(s) for Analysis
# 
# 1- Which Genre Has The Highest Release Of Movies?
# 
# 2- Which year has the highest release of movies?
# 
# 3- Do most famous films have a long duration?
# 
# 
# 
# 
# 
# 

# In[74]:


# Use this cell to set up import statements for all of the packages that you
#   plan to use.

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
get_ipython().run_line_magic('matplotlib', 'inline')

# Remember to include a 'magic word' so that your visualizations are plotted
#   inline with the notebook. See this page for more:
#   http://ipython.readthedocs.io/en/stable/interactive/magics.html


# <a id='wrangling'></a>
# ## Data Wrangling
# 
# 
# 
# 
# ### General Properties

# In[75]:


# Load your data and print out a few lines. Perform operations to inspect data
#   types and look for instances of missing or possibly errant data.
df=pd.read_csv('tmdb-movies.csv')
df.head()


# In[76]:


df.info()


# In[77]:


df.describe()


# In[78]:


#data has null values so we count total rows in each column which contain null values
df.isnull().sum()


# In[79]:


#fill the null values with zero using 'fillna' function
df1=df.fillna(0)


# ### Data Cleaning
# 
#  Removing Data (Duplicated and Unused information from the dataset)
#  

# # 1-remove duplicate rows from the dataset

# In[12]:



 #counting the duplicates

sum(df1.duplicated())


# In[13]:



#drop these duplicated rows 
df1.drop_duplicates(inplace=True)
df1.shape


# ## 2- remove the unused colums.
# 
# 

# In[16]:


#The columns like imdb_id, homepage,tagline, overview, budget_adj and revenue_adj are not required for my analysis
#I will drop these columns
df1.drop(['imdb_id','homepage','tagline','overview','budget_adj','revenue_adj'],axis =1,inplace = True)


# In[17]:


df1.shape


# <a id='eda'></a>
# ## Exploratory Data Analysis
# 
# ### Research Question 1 (Which Genre Has The Highest Release Of Movies?)

# In[18]:


#make a function will will split the string and return the count of each genre.
def data(x):
    #concatenate all the rows of the genrs.
    data_plot = df[x].str.cat(sep = '|')
    data = pd.Series(data_plot.split('|'))
    #conts each of the genre and return.
    info = data.value_counts(ascending=False)
    return info


# In[19]:


total_genre_movies = data('genres')
print(total_genre_movies)


# In[73]:


# plot a 'bar' plot using plot function for 'genre vs number of movies'.

total_genre_movies.plot(kind= 'bar',figsize = (13,8),fontsize=11)

#setup the title and the labels of the plot.

plt.title("Genre With Highest Release",fontsize=15)
plt.xlabel('Number Of Movies',fontsize=14)
plt.ylabel('Genres',fontsize= 14)
plt.legend(['Number Of Movies']);



#      Here we can see the highest release of movies in all times chart show Drama movies are Most release over years

# ## Research Question 2  (Which year has the highest release of movies?)

# In[21]:


#count the number of movies in each year 

data=df1.groupby('release_year').count()['id']


# In[63]:


data.plot(xticks = np.arange(1960,2016,5))
sns.set(rc={'figure.figsize':(14,5)})
plt.title("Year Vs Number Of Movies",fontsize = 14)
plt.xlabel('Release year',fontsize = 16)
plt.ylabel('Number Of Movies',fontsize = 16)
plt.legend(['Release year']);


#                             Here we can see The highest year in the release movies

# # Research Question 3 (Do most popular movies have a long duration? Let's find out)

# In[68]:


shorter_movies = df.sort_values(by=['runtime'], ascending = False).head(200)
runtime = shorter_movies['runtime']
popularity = shorter_movies['popularity']


# In[71]:


plt.scatter(runtime, popularity)
plt.title("Popular Movies Vs Runtime",fontsize = 14)
plt.xlabel('runtime',fontsize = 16)
plt.ylabel('popularity',fontsize = 16)
plt.legend(['popularity']);


#                     we can see that the more popular movies is the shortest movies.

# <a id='conclusions'></a>
# ## Conclusions
# 
# In the first question, We will find through the analysis that the highest category in the issuance of films is the drama category, and then comes comedies, then horror films, and then comes the rest of the categories.
# 
# In second question,We find that the highest year in the release of films is the year 2015, and it comes in the second place with the highest release in 2010 and the third in 2005.
#  
# In third question, We find that the most popular films are in the short-term films compared to the long-term films 
# 
# ## Limitations:
#  
# 1- we are not sure if the data provided to us is completel corect and up-to-date.the budget and revenue column do not have currency unit
# 2- it might be possible different movies have budget in different currency according to the country they are produce in. So a disparity arises here which can state the complete analysis wrong. 
# 3- i want to Drop the rows with missing values but it will affecte the overall analysis.During the data cleaning process 

# In[1]:


from subprocess import call
call(['python', '-m', 'nbconvert', 'Investigate_a_Dataset.ipynb'])

