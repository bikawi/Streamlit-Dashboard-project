import streamlit as st
from load_all_images import load_images
import chart_pr


reg_html_ad1="""
<div class="title">
    <h5>All Registered Users</h5>
"""
reg_html_ad2="""
<div class="title">
    <h5>Complete Registered Users</h5>
"""
pie_gender="""
<div class="title">
    <h5>Gender</h5>
"""
pie_os="""
<div class="title">
    <h5>OS</h5>
"""
pie_age="""
<div class="title">
    <h5>AGE</h5>
"""



def app():
    with st.container():
        fire_Logo,adjust_Logo,google_Logo,local_Logo,apple_Logo=load_images()
        image = local_Logo
        st.image(image,width =70)
        
        st.markdown("<hr/>", unsafe_allow_html=True)
                  
        admin = chart_pr.admin_page()
        ############################# Row 1 ###################################
        st.markdown(reg_html_ad1, unsafe_allow_html=True)
        
        col1,col2 = st.columns(2)
        with col1:
            
            st.plotly_chart(admin[0],use_container_width=True)
        with col2:
            
            st.plotly_chart(admin[1],use_container_width=True)
        
        st.write('')
        
        col1,col2 = st.columns(2)
        with col1:
            st.plotly_chart(admin[3],use_container_width=True)

        with col2:
            st.plotly_chart(admin[2],use_container_width=True) 
            
        st.plotly_chart(admin[4],use_container_width=True)  
        
        st.markdown(pie_gender, unsafe_allow_html=True)
        col1,col2 = st.columns(2)
        with col1:
            st.plotly_chart(admin[5],use_container_width=True)
        with col2:
            st.plotly_chart(admin[6],use_container_width=True)
        st.plotly_chart(admin[7],use_container_width=True)
            
        st.write('')
        
        
        st.markdown(pie_os, unsafe_allow_html=True)    
        col1,col2 = st.columns(2)
        with col1:
            st.plotly_chart(admin[8],use_container_width=True)
        with col2:
            st.plotly_chart(admin[9],use_container_width=True)
        st.plotly_chart(admin[10],use_container_width=True)
           
        
        st.markdown(pie_age, unsafe_allow_html=True)
        col1,col2 = st.columns(2)
        with col1:
            st.plotly_chart(admin[11],use_container_width=True)
        with col2:    
            st.plotly_chart(admin[12],use_container_width=True)
        st.plotly_chart(admin[13],use_container_width=True)
        
        col1,col2,col3 = st.columns([1,2,2])
        with col1:
            st.plotly_chart(admin[14],use_container_width=True)
        with col2:
            st.plotly_chart(admin[15],use_container_width=True)
        with col3:    
            st.plotly_chart(admin[16],use_container_width=True)