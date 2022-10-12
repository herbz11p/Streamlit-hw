# -*- coding: utf-8 -*-
"""
Created on Mon Sep 26 14:49:35 2022

@author: user
"""

import streamlit as st
import pandas as pd
from plotly.offline import iplot
import plotly.express as px
import plotly.figure_factory as ff


st.title("GDP on India")
GDP_Of_India=pd.read_csv("large_df (2).csv")


gdp_india=px.scatter(GDP_Of_India, x="Year", y= "GDP of IND")
st.plotly_chart(gdp_india)

gdp_india=px.line(GDP_Of_India, x="Year", y= "GDP of IND")
st.plotly_chart(gdp_india)

slider_year = st.slider("Choose Year Range", max_value = 2020, min_value = 1961, value = [1961, 2020], step=10)
gdp_indias = GDP_Of_India.loc[(GDP_Of_India["Year"] >= slider_year[0]) & (GDP_Of_India["Year"] <= slider_year[1])]
gdp_india=px.line(gdp_indias, x="Year", y= "GDP of IND")


gdp_india=px.histogram(GDP_Of_India, x="Year", y= "GDP of IND")
st.plotly_chart(gdp_india)

gdp_india=px.bar(GDP_Of_India, x="Year", y= "GDP of IND")
st.plotly_chart(gdp_india)

gdp_india=px.box(GDP_Of_India, x="Year", y= "GDP of IND")
st.plotly_chart(gdp_india) 

st.sidebar.title('GDP__Of__India')
st.sidebar.title('scatter')
st.sidebar.title('line')
st.sidebar.title('histogram')
st.sidebar.title('bar')
st.sidebar.title('box')


option = st.selectbox(
    'How would you like to be contacted?',
    ('Email', 'Home phone', 'Mobile phone'))

text_contents = '''GDP'''
st.download_button('Download', text_contents)

@st.cache
def convert_df(df):
    # IMPORTANT: Cache the conversion to prevent computation on every rerun
    return df.to_csv().encode('utf-8')

csv = convert_df(GDP_Of_India)

st.download_button(
    label="Download data as CSV",
    data=csv,
    file_name='large_df.csv',
    mime='text/csv',
)

st.error('This is an error', icon="🚨")

st.balloons()

