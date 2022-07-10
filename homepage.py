import streamlit as st
from streamlit.logger import get_logger
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import pyreadstat
import openpyxl



LOGGER = get_logger(__name__)


def run():
    st.set_page_config(
        page_title="NATIONAL CENTRE FOR TECHNOLOGY MANAGEMENT",
        page_icon="👋",
        
    )
    st.header('''NATIONAL CENTRE FOR TECHNOLOGY MANAGEMENT''')
    st.write("# STI INDICATORS DASHBOARD 👋")

    if st.checkbox('PROJECT DESCRIPTION'):
    
        st.markdown(
            """
            The sample was randomly selected based on the list of establishments with at least 10 employees obtained from the National Bureau of Statistics (NBS) and the Nigerian Stock Exchange. 
        The Stock Exchange list includes only formal firms whereas the NBS list includes both formal and informal firms. These two sources were cross-referenced and any firm listed in both sources was automatically selected into the sample. The logic is that if a listed firm is still surviving. Note that firm exit rate is particularly high in Nigeria. 
        Subsequently, all other firms were stratified into six geographical zones (North-East, 
        North-West, North-Central, South-West, South-East, South-South) and sector of activity. 
        The final sample was selected by proportional probability. 
        The survey questionnaire was delivered by hand to all the firms, and in many instances, some of the selected firms did no longer exist. In every possible case, the missing firm was substituted with another one in the same sector and geographical location. 
        The survey was first carried out in 2008 (initial sample of 1000 firms) and then repeated in 2011 (initial sample of 1500 firms). The final pooled sample includes 1359 firms, an overall response rate of 54%.
        The pooled cross-sectional dataset available for download has some specific features:
        The dataset includes data from wave 1 (2005-2007) and wave 2 (2008-2010) of the Nigerian innovation surveys. 
        The year variable identifies the different survey waves. Wave 1 was completed in 2008 and wave 2, in 2011. 
        The service variable sorts the observations broadly into manufacturing and services. 
        The id variable identifies each unique firm. Repeatedness was ignored because repeated cases are only about 2.5%.
        As much as possible, variables have been matched across the two waves.   Due to coding changes and some inconsistencies in the survey instrument, a few variables could not be matched.  
        Any variable that could not be matched is retained in its original form.  
        Some of the variables have notes attached to them. The notes are consistent with what is in the accompanying codebook.xls
        Item numbering on the questionnaire for the two waves are not consistent. Thus, rather than use question numbers for variable names – as is commonly done – intuitive variable names and labels (defined in detail in the accompanying codebook.xls) are used.
        Definitions of main concepts can be found in the accompanying codebook.xls.
        It is strongly recommended that users thoroughly familiarize themselves with the accompanying codebook as well as the questionnaires for each of the waves before applying the dataset. This is crucial especially because of the skip patterns. While everything was done to ensure that the skip patterns were all correctly established, there can be no guarantee of perfection. 
        It is also strongly recommended that users be familiar with the nature of innovation surveys as this will help in understanding how to treat the data for analysis. The Oslo Manual, which is freely available online, is a very useful resource.
        To have a feel of the sectoral distribution of the sample, type in Stata: tab service year
                    Year data collected
            Service		2008	2011	Total
                        
            manufacturing	519	371	890 
            service		209	260	469 
                        
            Total		728	631	1,359 )
        """
        )
    col1, col2= st.columns([20,1])
    col3, col4 = st.columns([70,1])
    col5,col6 = st.columns([20,1])
    with col1:
        df = pd.read_spss('nigeria-innovation.sav')
        df2 =df[['iexptotal','sector','service']]
        df2.dropna(inplace=True)
        df3 = df2.groupby('sector').apply(sum)
        df3.reset_index(inplace=True)
        df3.rename({'sector':'SECTORS','iexptotal':'R&D EXPENDITURE'},axis =1,inplace=True)
        fig = px.scatter(df3, x = 'SECTORS',y = 'R&D EXPENDITURE',size = 'R&D EXPENDITURE',hover_name = 'SECTORS', size_max= 120,color='SECTORS',title = 'HOW MUCH ARE NIGERIAN INDUSTRIES SPENDING ON R&D')
        fig.update_layout(width =800,height = 800,showlegend =False)
        fig.show()
        
        st.plotly_chart(fig)
    with col2:
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
        fig = px.line(df00,x='OUTCOME',y ='RESPONSE',color ='FACTORS AFFECTING',title ='FACTORS AFFECTING INNOVATION ACTIVITIES IN NIGERIAN INDUSTRIES')
        fig.update_layout(width =700,height=600,showlegend =False)
        st.plotly_chart(fig)
    with col3:
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
        fig = px.scatter(df01,x='OUTCOME',y='RESPONSE',size='RESPONSE', color='OUTCOME',hover_name='GOVT SUPPORT POLICY',size_max=100,animation_frame='GOVT SUPPORT POLICY',title = 'EFFECTS OF GOVERNMENT SUPPORT ON INNOVATION')
        fig.update_layout(width =700,height=600,showlegend =False)
        st.plotly_chart(fig)
        
    with col4:
        df = pd.read_spss('nigeria-innovation.sav')
        df2 =df[['iexptotal','sector','service']]
        df2.dropna(inplace=True)
        df3 = df2.groupby('service').apply(sum)
        df3.reset_index(inplace=True)
        df3.rename({'service':'SERVICE','iexptotal':'R&D EXPENDITURE'},axis =1,inplace=True)
            
            
            # Use `hole` to create a donut-like pie chart
        fig = go.Figure(data=[go.Pie(labels=df3['SERVICE'], values=df3['R&D EXPENDITURE'], hole=.6,name="R&D EXPENDITURE")])
        fig.update_traces(hole=.6, hoverinfo="label+percent+name")

        fig.update_layout(
                # Add annotations in the center of the donut pies.
                annotations=[dict(text='R&D EXPENDITURE',  font_size=10, showarrow=False)],height = 500,width =500,paper_bgcolor="#202A44",title = 'SHARE OF R&D EXPENDITURE BY BUSINESS SECTOR')

            
        st.plotly_chart(fig)
    with col5:
        waves = pd.read_excel('wave1.xlsx',sheet_name= 'Sheet1')
        waves.dropna(inplace =True)
        waves['RDSTAFF'].replace({' ':0},inplace =True)
        waves = waves[(waves['RDSTAFF']!=0) &(waves['estab']!=0)]
        waves = waves[['sector','year','turnover050607','RDSTAFF']]
        df = waves.groupby('sector').apply(sum)
        df.drop(['sector','year'],axis =1,inplace=True)
        df.reset_index(inplace=True)
        fig = px.scatter(df, y="turnover050607", x="RDSTAFF",size="turnover050607", color="sector",size_max=150,title='THE EFFECT OF R&D STAFF ON TURNOVER')
        fig.update_layout(width=700,height=600,showlegend =False)
        st.plotly_chart(fig)
    with col6:
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
        fig = px.line(df02,x='OUTCOME',y ='RESPONSE',color ='INFO SOURCE',title = 'IMPORTANCE OF INFORMATION SOURCES TO INNOVATION')
        fig.update_layout(width =700,height=600,showlegend =False)
        st.plotly_chart(fig)



if __name__ == "__main__":
    run()
