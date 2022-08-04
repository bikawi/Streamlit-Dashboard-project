import streamlit as st
from load_all_images import load_images
import chart_pr

returned_html_ad="""
<div class="title">
    <h5>Retention</h5>
"""
stickness_html_ad="""
<div class="title">
    <h5>Stickiness</h5>
"""
newUser_html_ad1="""
<div class="title">
    <h5>Installs</h5>
"""
actuser_html_ad="""
<div class="title">
    <h5>AVG Daily Active Users</h5>
"""
eng_time_html_ad="""
<div class="title">
    <h5>AVG Engagement Time</h5>
"""


def app():
    
    firebase = chart_pr.firebase_page()
    
    with st.container():
        fire_Logo,adjust_Logo,google_Logo,local_Logo,apple_Logo=load_images()
        image = fire_Logo
        st.image(image,width =300)
        
        st.markdown("<hr/>", unsafe_allow_html=True)
        
        ##################### Row 1 ###########################################
        col1,col2 = st.columns(2)
        with col1:
            
            st.markdown(newUser_html_ad1, unsafe_allow_html=True)
            st.plotly_chart(firebase[0],use_container_width=True)
            st.plotly_chart(firebase[1],use_container_width=True)
            
        with col2:
            
            st.markdown(actuser_html_ad, unsafe_allow_html=True)
            st.plotly_chart(firebase[2],use_container_width=True)
            st.plotly_chart(firebase[3],use_container_width=True)    
            
        
        st.markdown(returned_html_ad, unsafe_allow_html=True)
        col1,col2,col3 = st.columns(3)
        with col1:
            st.plotly_chart(firebase[4],use_container_width=True)
            st.plotly_chart(firebase[7],use_container_width=True)
        with col2:
            st.plotly_chart(firebase[5],use_container_width=True)
            st.plotly_chart(firebase[8],use_container_width=True)
        with col3:
            st.plotly_chart(firebase[6],use_container_width=True)
            st.plotly_chart(firebase[9],use_container_width=True)
        st.plotly_chart(firebase[10],use_container_width=True)
        
        st.markdown(stickness_html_ad, unsafe_allow_html=True)
        st.plotly_chart(firebase[11],use_container_width=True)
        
        st.markdown(eng_time_html_ad, unsafe_allow_html=True)
        col1,col2 = st.columns(2)
        with col1:
            st.plotly_chart(firebase[12],use_container_width=True)
        with col2:
            st.plotly_chart(firebase[13],use_container_width=True)
        st.plotly_chart(firebase[14],use_container_width=True)
        #######################################################################