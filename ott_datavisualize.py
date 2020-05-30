import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import plotly.graph_objects as go
import plotly.offline as py
#--------------------------------DATA EXPLORE---------------------------
df = pd.read_csv("MoviesOnStreamingPlatforms_updated.csv")
print (df.head())

print('Number of rows and columns :',df.shape) # Number of rows and columns
print(df.describe())

print ("----------------------------------------------------")
#----------------------MISSING VALUES-----------------------------------
percentage_missing_values = round(df.isnull().sum() * 100 / len(df), 2).reset_index()
percentage_missing_values.columns = ['column_name', 'percentage_missing_values']
percentage_missing_values = percentage_missing_values.sort_values(
 'percentage_missing_values', ascending= False)
print (percentage_missing_values)
print('-----------------------------------------------------')
#------------------------PLOTTING----------------------------------------

print(sns.distplot(df['Runtime']))
sns.distplot(df['Runtime'])
plt.show()
print(sns.distplot(df['IMDb']))
sns.distplot(df['IMDb'])
plt.show()
print ("-----------------------------------------------------")
#----------------------------------------------------------
movie_count_by_language = df.groupby('Language')['Title'].\
 count().reset_index().sort_values('Title',ascending = False).\
 head(10).rename(columns = {'Title':'Movie Count'})
# fig = px.bar(movie_count_by_language, x='Language',
#              y='Movie Count', color='Movie Count', height=600)
#fig.show()
print('-----------------------------------------------------')
#------------------------------------------------------------------
yearly_movie_count = df.groupby('Year')['Title'].\
    count().reset_index().rename(columns = {'Title':'Movie Count'})
# fig = px.bar(yearly_movie_count, x='Year',
#              y='Movie Count', color='Movie Count', height=600)
# fig.show()

#-----------------------------------------------------------------
digital_platforms = df[['Netflix','Hulu','Prime Video','Disney+']].sum().reset_index()
digital_platforms.columns = ['Platform', 'Movie Count']
digital_platforms = digital_platforms.sort_values('Movie Count',ascending = False)
labels = digital_platforms.Platform
values = digital_platforms['Movie Count']
pie = go.Pie(labels=labels, values=values, marker=dict(line=dict(color='#000000', width=1)))
layout = go.Layout(title='Digital Platforms Movie Share')
fig = go.Figure(data=[pie], layout=layout)
py.plot(fig)