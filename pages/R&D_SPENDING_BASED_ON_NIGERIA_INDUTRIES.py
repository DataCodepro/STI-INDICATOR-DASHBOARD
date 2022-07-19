import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import pyreadstat
import openpyxl
import streamlit as st
def fun():
    df = pd.read_spss('nigeria-innovation.sav')
    df2 =df[['iexptotal','sector','service']]
    df2.dropna(inplace=True)
    df3 = df2.groupby('sector').apply(sum)
    df3.reset_index(inplace=True)
    df3.rename({'sector':'SECTORS','iexptotal':'R&D EXPENDITURE(BILLION NAIRA)'},axis =1,inplace=True)
    st.table(df3)
    
    fig = px.scatter(df3, x = 'SECTORS',y = 'R&D EXPENDITURE(BILLION NAIRA)',size = 'R&D EXPENDITURE(BILLION NAIRA)',hover_name = 'SECTORS', size_max= 120,color='SECTORS',labels={'x':'SECTORS','y':'R&D EXPENDITURE(BILLION NAIRA)'})
    fig.update_layout(height = 700,width =1000,paper_bgcolor="#202A44",)
    fig.show()
    
    st.plotly_chart(fig)


       
            
            
st.set_page_config(page_title="R&D SPENDING", page_icon="📈")
st.header(
        """HOW MUCH ARE NIGERIAN INDUSTRIES SPENDING ON R&D""")
fun()   
