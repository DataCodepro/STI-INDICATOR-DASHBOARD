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
    df = pd.read_excel('randd.xlsx')
    df2 = df[['iact1','crd','ord']]
    df2.dropna(inplace=True)
    d1 = pd.crosstab(df2['iact1'],df2['ord'])
    d2 = pd.crosstab(df2['iact1'],df2['crd'])
    d3 = {
                    'Continuous R&D':[147,284],
                    'Occassional R&D':[284,147]
                }
    ITCRDORD = pd.DataFrame(d3,index = ['YES','NO'])
    ITCRDORD.rename({0:'NO',1:'YES'},axis = 0,inplace =True)
    ITCRDORD.reset_index(inplace=True)
    ITCRDORD.rename({'index':'Outcome'},axis = 1,inplace =True)
    st.table(ITCRDORD)
    fig = make_subplots(rows=1, cols=2, specs=[[{'type':'domain'}, {'type':'domain'}]])
    fig.add_trace(go.Pie(labels=ITCRDORD['Outcome'], values=ITCRDORD['Continuous R&D'], name="Continuous R&D"),
                1, 1)
    fig.add_trace(go.Pie(labels=ITCRDORD['Outcome'], values=ITCRDORD['Occassional R&D'], name="Occassional R&D"),
                1, 2)

    # Use `hole` to create a donut-like pie chart
    fig.update_traces(hole=.7, hoverinfo="label+percent+name")

    fig.update_layout(
        
        # Add annotations in the center of the donut pies.
        annotations=[dict(text='Continuous R&D', x=0.12, y=0.5, font_size=20, showarrow=False),
                    dict(text='Occassional R&D', x=0.88, y=0.5, font_size=20, showarrow=False)],width=1000,height=500, paper_bgcolor="#202A44")
    st.plotly_chart(fig)
st.set_page_config(page_title="INTERNALR&D", page_icon="📈")
st.header("INTERNAL R&D ON INNOVATION")
fun()