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
    df02 = pd.read_excel("output tables.xlsx",sheet_name = 'Sheet5')
    df02.iloc[1:4,0] = 'Internal'
    df02.iloc[5:8,0] = 'Suppliers'
    df02.iloc[9:12,0] = 'Customers'
    df02.iloc[13:16,0] = 'Competitors'
    df02.iloc[17:20,0] = 'Consultants, commercial labs or private R&D institutes'
    df02.iloc[21:24,0] = 'Universities, other higher ed. institutions'
    df02.iloc[25:28,0] = 'Public research institutes'
    df02.iloc[29:32,0] = 'Conferences, fairs, exhibitions'
    df02.iloc[33:36,0] = 'Journals, trade publications'
    df02.iloc[36:40,0] = 'Professional, industry associations'
    st.table(df02)
    fig = px.scatter(df02,x='OUTCOME',y='RESPONSE',size='RESPONSE', color='OUTCOME',hover_name='INFO SOURCE',size_max=100,animation_frame='INFO SOURCE')
    fig.update_traces(hovertemplate =None)
    fig.update_layout(width =1000,height=600,hovermode ='x unified',hoverlabel = dict(bgcolor = 'black',font_size =16,font_family = 'Rockwell'))
    fig.update_layout(legend= dict(title_font_family = 'Rockwell',font_size =16))
    st.plotly_chart(fig)
st.set_page_config(page_title="IMPORTANCE", page_icon="📈")
st.header("IMPORTANCE OF INFORMATION SOURCES TO INNOVATION")
fun()
