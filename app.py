import streamlit as st
from streamlit_option_menu import option_menu 
import Merchant
import users
from load_all_images import load_winin_logo
import slides
import campaings
import os

    
    
   
st.set_page_config(page_title = 'Dashboard', 
    layout='wide',
    page_icon="chart_with_upwards_trend",   
    initial_sidebar_state ='auto'
    )



  
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

############# REMOVE FUNCTION ###########

    
with st.sidebar:
    selected_page = option_menu('Menu', ["Users","Merchant",'Campaings','Presentation Generate'], 
    icons=['house-fill','pie-chart-fill','check2-square','file-earmark-ppt-fill'], 
    menu_icon="cast", default_index=0)
    ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
      
    local_css( os.path.join(ROOT_DIR,"style.css"))

if selected_page == 'Users':
    users.app()
if selected_page == 'Merchant':
    Merchant.app()
if selected_page == 'Campaings':
    campaings.app()
if selected_page == 'Presentation Generate':
    slides.app()
    
    
    
