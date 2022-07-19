import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import pyreadstat
import openpyxl
import streamlit as st
def fun():
    df00 = pd.read_excel("output tables.xlsx",sheet_name = 'Sheet10')
    df00.fillna(' ',inplace=True)
    df00.drop('Unnamed: 3',axis=1,inplace=True)
    df00.iloc[1:4,0] = 'Lack Of In-House Funds'
    df00.iloc[5:8,0] = 'Lack Of External Financing'
    df00.iloc[9:12,0] = 'High Costs Of Innovation'
    df00.iloc[13:16,0] = 'Economic Risk'
    df00.iloc[17:20,0] = 'Expensive Environment-Friendly R&D'
    df00.iloc[21:24,0] = 'Lack Of Qualified Personnel'
    df00.iloc[25:28,0] = 'Lack Of Tech Information'
    df00.iloc[29:32,0] = 'Lack Of Market Information'
    df00.iloc[33:36,0] = 'Difficult To Find Coop Partners'
    df00.iloc[36:40,0] = 'Market Dominated By Large Ent'
    df00.iloc[41:44,0] = 'Uncertain Demand'
    df00.iloc[44:48,0] = 'Market Dominated By Foreign Substitutes'
    df00.iloc[49:52,0] = 'Consumers Unwilling To Pay'
    df00.iloc[53:56,0] = 'Imitation'
    df00.iloc[57:60,0] = 'Poor Basic Infrastructure'
    df00.iloc[61:64,0] = 'Inadequate Facilities'
    df00.iloc[65:68,0] = 'No Need Due To Prior Innovation'
    df00.iloc[69:72,0] = 'No Need Due To No Demand For Innovation'
    df00.iloc[73:76,0] = 'Internal Organisational Rigidities'
    df00.iloc[77:80,0] = 'Inflexible Regulations/Standards'
    df00.iloc[81:84,0] = 'Limitation Of S&T Public Policies'
    st.table(df00)
    fig = px.line(df00,x='OUTCOME',y ='RESPONSE',color ='FACTORS AFFECTING')
    fig.update_traces(hovertemplate =None)
    fig.update_layout(width =1000,height=600,hovermode ='x unified')
    st.plotly_chart(fig)
    fig = px.scatter(df00,x='OUTCOME',y='RESPONSE',size='RESPONSE', color='OUTCOME',hover_name='FACTORS AFFECTING',size_max=100,animation_frame='FACTORS AFFECTING')
    fig.update_traces(hovertemplate =None)
    fig.update_layout(width =1000,height=600,hovermode ='x unified')
    st.plotly_chart(fig)

       
            
            
st.set_page_config(page_title="EFFECT", page_icon="📈")
st.header("FACTORS AFFECTING INNOVATION ACTIVITIES IN NIGERIAN INDUSTRIES")
fun()
