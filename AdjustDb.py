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
install_html_ad1="""
<div class="title">
    <h5>Installs Info</h5>
"""
user_html_ad="""
<div class="title">
    <h5>User Information</h5>
"""


def app():
    with st.container():
        fire_Logo,adjust_Logo,google_Logo,local_Logo,apple_Logo=load_images()
        image = adjust_Logo
        st.image(image,width =250)
        #st.title('ADJUST Dashboard')
        #######################################################################
        st.markdown("<hr/>", unsafe_allow_html=True)
        #######################################################################
        
        adjust = chart_pr.adjust_page()
        
        with st.container():
            ####################### Row 1 #####################################
            st.markdown(user_html_ad, unsafe_allow_html=True)
             
            col1,col2,col3 = st.columns(3)
            with col1:
                st.plotly_chart(adjust[0],use_container_width=True)
            with col2:
                st.plotly_chart(adjust[1],use_container_width=True)
            with col3:
                st.plotly_chart(adjust[2],use_container_width=True)    
            
            st.plotly_chart(adjust[3],use_container_width=True)
            
            st.markdown(install_html_ad1, unsafe_allow_html=True)
            
            st.plotly_chart(adjust[4],use_container_width=True)    
            st.plotly_chart(adjust[5],use_container_width=True)
            
            
            
            ######################Retuntion####################################    
            st.markdown(returned_html_ad, unsafe_allow_html=True)
            col1,col2,col3 = st.columns(3)
            with col1:
                st.plotly_chart(adjust[6],use_container_width=True)
                st.plotly_chart(adjust[9],use_container_width=True)
            with col2:
                st.plotly_chart(adjust[7],use_container_width=True)
                st.plotly_chart(adjust[10],use_container_width=True)
            with col3:
                st.plotly_chart(adjust[8],use_container_width=True)
                st.plotly_chart(adjust[11],use_container_width=True)
            st.plotly_chart(adjust[12],use_container_width=True)
            
    
            
            
            #####################Stickness#####################################
            st.markdown(stickness_html_ad, unsafe_allow_html=True)
            st.plotly_chart(adjust14,use_container_width=True)   
            ###################################################################