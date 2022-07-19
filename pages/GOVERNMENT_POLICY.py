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
    df01 = pd.read_excel("output tables.xlsx",sheet_name = 'Sheet9')
    df01.fillna(' ',inplace=True)
    df01.iloc[1:4,0] = 'R&D Funding'
    df01.iloc[5:8,0] = 'Training'
    df01.iloc[9:12,0] = 'Subsidies'
    df01.iloc[13:16,0] = 'Tax Rebates'
    df01.iloc[17:20,0] = 'Technical Support/Advice'
    df01.iloc[21:24,0] = 'Infrastructur Support'
    df01.iloc[25:28,0] = 'Loans And Grants'
    df01.iloc[29:32,0] = 'Others'
    st.table(df01)
    fig = px.scatter(df01,x='OUTCOME',y='RESPONSE',size='RESPONSE', color='OUTCOME',hover_name='GOVT SUPPORT POLICY',size_max=100,animation_frame='GOVT SUPPORT POLICY')
    fig.update_traces(hovertemplate =None)
    fig.update_layout(width =1000,height=600,hovermode ='x unified',hoverlabel = dict(bgcolor = 'black',font_size =16,font_family = 'Rockwell'))
    fig.update_layout(legend= dict(title_font_family = 'Rockwell',font_size =16))
    st.plotly_chart(fig)
    

       
            
            
st.set_page_config(page_title="EFFECT2", page_icon="📈")
st.header("EFFECTS OF GOVERNMENT SUPPORT ON INNOVATION")
fun()
