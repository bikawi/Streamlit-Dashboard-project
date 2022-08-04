import streamlit as st
from load_all_images import load_images
import chart_pr

console_html_ad1="""
<div class="title">
    <h5>Users Information</h5>
"""


def app():
    with st.container():
        fire_Logo,adjust_Logo,google_Logo,local_Logo,apple_Logo=load_images()
        image = google_Logo
        st.image(image,width =300)
        
        #######################################################################
        st.markdown("<hr/>", unsafe_allow_html=True)
        #######################################################################
        
        google = chart_pr.google_page()
        
        #######################################################################
        st.markdown(console_html_ad1, unsafe_allow_html=True)
        col1,col2,col3 = st.columns(3)
        with col1:
            st.plotly_chart(google[0],use_container_width=True)
        with col2:
            st.plotly_chart(google[1],use_container_width=True)
        with col3:
            st.plotly_chart(google[2],use_container_width=True)
        
        st.plotly_chart(google[3],use_container_width=True)
        #######################################################################