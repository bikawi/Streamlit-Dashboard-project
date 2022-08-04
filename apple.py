import streamlit as st
from load_all_images import load_images
import chart_pr

newUser_html_ad1="""
<div class="title">
    <h5>Installs</h5>
"""
actuser_html_ad="""
<div class="title">
    <h5>AVG Monthly Active Users</h5>
"""


def app():
    fire_Logo,adjust_Logo,google_Logo,local_Logo,apple_Logo=load_images()
    image = apple_Logo
    st.image(image,width =50)
    
    st.markdown("<hr/>", unsafe_allow_html=True)
    
    
    apple = chart_pr.apple_page()
    ##################### Row 1 ###########################################
    col1,col2 = st.columns(2)
    with col1:
        
        st.markdown(newUser_html_ad1, unsafe_allow_html=True)
        st.plotly_chart(apple[0],use_container_width=True)
        st.plotly_chart(apple[1],use_container_width=True)
        
    with col2:
        
        st.markdown(actuser_html_ad, unsafe_allow_html=True)
        st.plotly_chart(apple[2],use_container_width=True)
        st.plotly_chart(apple[3],use_container_width=True) 