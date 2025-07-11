#!/usr/bin/env python
# coding: utf-8

# In[11]:


import pandas as pd
import streamlit as st
import plotly.express as px


# In[12]:


megadeth_df = pd.read_csv("Megadeth - Reviews - MusicBrainz.csv", encoding='latin1')


# In[13]:


megadeth_df = megadeth_df.dropna(subset=['Rating'])


# In[14]:


year_range = st.slider(
    "年数を選び",
    min_value=int(megadeth_df["Year"].min()),
    max_value=int(megadeth_df["Year"].max()),
    value=(int(megadeth_df["Year"].min()), int(megadeth_df["Year"].max()))
)


# In[15]:


rating_range = st.slider(
    "点数を選び",
    min_value=0.0,
    max_value=5.0,
    value=(megadeth_df["Rating"].min(), megadeth_df["Rating"].max()),
    step=0.1
)


# In[16]:


filtered_df = megadeth_df[
    (megadeth_df['Year'] >= year_range[0]) & 
    (megadeth_df['Year'] <= year_range[1]) &
    (megadeth_df['Rating'] >= rating_range[0]) & 
    (megadeth_df['Rating'] <= rating_range[1])
]


# In[17]:


fig = px.scatter(
    filtered_df,  
    x="Year",
    y="Rating",
    size='Releases',
    color='Rating',
    hover_data=['Title', 'Releases'],  
    title='発行年数と点数関係'
)
st.plotly_chart(fig)


# In[18]:


selected_album = st.selectbox('アルバムの写真', filtered_df['Title'])
if selected_album:
    url = filtered_df[filtered_df['Title'] == selected_album]['Title_URL'].values[0]
    st.markdown(f"[{selected_album}的MusicBrainz页面]({url})", unsafe_allow_html=True)


# In[19]:


sort_key = st.selectbox(
    "排序依据",
    ("Rating", "Year", "Releases")
)
ascending = False if sort_key in ["Rating", "Releases"] else True
if sort_key == "Year": 
    ascending = False


# In[20]:


st.subheader(f"{sort_key} による专辑排行榜(上位5件)")
ranking_df = filtered_df.sort_values(by=sort_key, ascending=ascending).head(5)
st.dataframe(ranking_df[['Title', 'Year', 'Rating', 'Releases']])


# In[ ]:





# In[ ]:




