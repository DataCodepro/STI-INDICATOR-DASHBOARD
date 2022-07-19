import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import plotly.graph_objects as go
import pyreadstat
import openpyxl
import streamlit as st
def fun():
    df = pd.read_spss('nigeria-innovation.sav')
    df2 =df[['iexptotal','sector','service']]
    df2.dropna(inplace=True)
    df3 = df2.groupby('service').apply(sum)
    df3.reset_index(inplace=True)
    df3.rename({'service':'SERVICE','iexptotal':'R&D EXPENDITURE'},axis =1,inplace=True)
    st.table(df3)
    
    
    # Use `hole` to create a donut-like pie chart
    fig = go.Figure(data=[go.Pie(labels=df3['SERVICE'], values=df3['R&D EXPENDITURE'], hole=.6,name="R&D EXPENDITURE")])
    fig.update_traces(hole=.6, hoverinfo="label+percent+name")

    fig.update_layout(
        # Add annotations in the center of the donut pies.
        annotations=[dict(text='R&D EXPENDITURE',  font_size=10, showarrow=False)],height = 600,width =800,paper_bgcolor="#202A44")
    fig.show()
        
    st.plotly_chart(fig)


       
            
            
st.set_page_config(page_title="R&D SPENDING2", page_icon="📈")
st.header("SHARE(PERCENTAGE) OF R&D EXPENDITURE BY BUSINESS SECTOR")
fun()   
