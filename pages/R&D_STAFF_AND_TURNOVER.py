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
    waves = pd.read_excel('wave1.xlsx',sheet_name= 'Sheet1')
    waves.dropna(inplace =True)
    waves['RDSTAFF'].replace({' ':0},inplace =True)
    waves = waves[(waves['RDSTAFF']!=0) &(waves['estab']!=0)]
    waves = waves[['sector','year','turnover050607','RDSTAFF']]
    df = waves.groupby('sector').apply(sum)
    df.drop(['sector','year'],axis =1,inplace=True)
    df.reset_index(inplace=True)
    df.rename({'turnover050607':'TURNOVER (TRILLION NAIRA)', 'RDSTAFF':'R&DSTAFF'},axis =1,inplace=True)
    st.table(df)
    fig = px.scatter(df, y="TURNOVER (TRILLION NAIRA)", x="R&DSTAFF",size="TURNOVER (TRILLION NAIRA)", color="sector",size_max=150)
    fig.update_traces(hovertemplate =None)
    fig.update_layout(width =1000,height=600,hovermode ='x unified',hoverlabel = dict(bgcolor = 'black',font_size =16,font_family = 'Rockwell'))
    fig.update_layout(legend= dict(title_font_family = 'Rockwell',font_size =16))
    st.plotly_chart(fig)
st.set_page_config(page_title="EFFECT3", page_icon="📈")
st.header("EFFECT OF NUMBER OF R&D ON TURNOVER")
fun()
