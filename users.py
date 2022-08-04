import streamlit as st 
from streamlit_option_menu import option_menu 
from datetime import datetime
import firebaseDb
import consolDb
import AdjustDb
import Admin
import homeV
import apple


def app():
    
    with st.container():
        selected_page = option_menu('Database', ["Home","Firebase", "Adjust", "Google Console", 'Apple','Admin Panel'], 
        icons=['house-fill','pie-chart-fill', 'badge-ad-fill', "google",'apple' ,'pin-map-fill'], 
        menu_icon="bar-chart-steps", default_index=0, orientation="horizontal",
        styles={
            "container": {"padding": "5!important", "background-color": "#F0F2F6"},
            "icon": { "font-size": "20px"}, 
            "nav-link": {"font-size": "20px", "text-align": "center", "margin":"0px", "--hover-color": "#F0F2F6"},
            "nav-link-selected": {"background-color": "#FF4B4B"},    })
        st.subheader('Filtring')
        
    with st.form(key='columns_in_form'):
        col1,col2,col3 = st.columns(3)
        with col1:
            selected = st.selectbox(
             'Choose Time Period',
             ('This Day', 'This Week','Last Week', 'This Month'
                                             ,'Last Month','This Year','Custom Date'),index =6,key=1)
        with col2:
            
            from_date2 =st.date_input('Custom date for all data',value=(datetime(2021, 12, 1), datetime(2022, 1, 1)),key = 3)
    
        with col3:
            """
            countries = st.multiselect(
             'Choose Country1',
             ['All','jo','kw','ma','qa','sa','tn','ae','eg','dz','iq','oth'],
             ['All'],key=5)
            """

            countries1 = st.multiselect(
                 'Choose Country',
                 ["All"],
                 ['All'],key = 6)
            countries =countries1

                
        submitted = st.form_submit_button('Submit')
           
    
        
    ###################### Database pages #####################################
    if selected_page == 'Home':
        homeV.app()
    if selected_page == 'Firebase':
        firebaseDb.app()  
    if selected_page == 'Adjust':
        AdjustDb.app()
    if selected_page == 'Google Console':
        consolDb.app()
    if selected_page == 'Admin Panel':
        Admin.app()
    if selected_page == 'Apple':
        apple.app()
    ###########################################################################