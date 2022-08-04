import streamlit as st
import chart_pr

active_html="""
<div class="title">
    <h5>AVG Daily Active Users</h5>
"""  
stickness_html="""
<div class="title">
    <h5>Stickiness</h5>
"""
returned_html="""
<div class="title">
    <h5>Retention</h5>
"""
newU_html="""
<div class="title">
    <h5>New Users</h5>
"""
install_html="""
<div class="title">
    <h5>Installs</h5>
"""
reg_html="""
<div class="title">
    <h5>Registiration </h5>
"""
eng_time_html_ad="""
<div class="title">
    <h5>AVG Engagement Time</h5>
"""

def app():
    
    home_page = chart_pr.home_page()
    
    with st.container():
        
        
        
        st.title('Home Dashboard')
        
        
        st.markdown(install_html, unsafe_allow_html=True)
        col1,col2 = st.columns(2)
        with col1:
            st.plotly_chart(home_page[2],use_container_width=True)
        with col2:
            st.plotly_chart(home_page[3],use_container_width=True)
        st.plotly_chart(home_page[4],use_container_width=True)
        st.caption('Adjust : Users who open the app for the first time')
        st.caption('Firebase : Users who open the app for the first time')
        st.caption('Google Console : Users who have never installed your app before')
        st.caption('Apple Store : Total Download')
        
        
        st.markdown(reg_html, unsafe_allow_html=True)
        st.plotly_chart(home_page[0],use_container_width=True)
        st.plotly_chart(home_page[1],use_container_width=True)
        st.caption('Local Data : Users who complete all registration steps and verification')
        st.caption('Adjust : Users who registered even completed or not')
            
        
        
            
        
        st.markdown(active_html, unsafe_allow_html=True)
        col1,col2,col3,col4 = st.columns(4)
        with col1:
            st.plotly_chart(home_page[5],use_container_width=True)
            
        with col2:
            st.plotly_chart(home_page[6],use_container_width=True)

        with col3:
            st.plotly_chart(home_page[7],use_container_width=True)
            
        with col4:
            st.plotly_chart(home_page[8],use_container_width=True)    
            
        col1,col2 = st.columns(2)
        with col1:
            st.caption('Firebase : An active user has engaged with an app in the device foreground, and has logged a user_engagement event.')
            st.caption('Adjust : The average number of unique daily active users (DAU) for your selected timeframe')
        with col2:
            st.caption('Google Console : The number of users who opened your app on a given day.')
            st.caption('Local Data : Users who open the app for the first time')
        
        st.markdown(returned_html, unsafe_allow_html=True)
        col1,col2 = st.columns(2)
        with col1:
            st.plotly_chart(home_page[9],use_container_width=True)
            st.plotly_chart(home_page[11],use_container_width=True)
            
        with col2:
            st.plotly_chart(home_page[10],use_container_width=True)
            st.plotly_chart(home_page[12],use_container_width=True)
            
        st.caption('Red : Underperforming')
        st.caption('Yellow : ِAverage Performing')
        st.caption('Green : Top Performing')
        
        
        st.markdown(stickness_html, unsafe_allow_html=True)
        col1,col2,col3,col4 = st.columns(4)
        with col1:
            st.plotly_chart(home_page[13],use_container_width=True)
        with col2:
            st.plotly_chart(home_page[14],use_container_width=True)
        with col3:
            st.plotly_chart(home_page[15],use_container_width=True)
        with col4:
            st.plotly_chart(home_page[16],use_container_width=True)
        st.plotly_chart(home_page[17],use_container_width=True)    
        
        col1,col2 = st.columns(2)
        with col1:
            st.plotly_chart(home_page[18],use_container_width=True)
        with col2:
            st.plotly_chart(home_page[19],use_container_width=True)
            
        st.markdown(eng_time_html_ad, unsafe_allow_html=True)     
        col1,col2 = st.columns(2)
        with col1:
            st.plotly_chart(home_page[20],use_container_width=True)
        with col2:
            st.plotly_chart(home_page[21],use_container_width=True)
        st.plotly_chart(home_page[22],use_container_width=True)
       
        

       
            
            
        
            
            
    