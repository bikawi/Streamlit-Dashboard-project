import streamlit as st
from PIL import Image
from datetime import datetime


path=r"png/"

image_users = Image.open(path+'prs.png')


#############################Main##############################################
def app():
    
    
    
    st.title('Presntation Generator')
    st.markdown("<hr/>", unsafe_allow_html=True)
    st.subheader('Filtring')
    
    with st.form(key='columns_in_form'):
        list_count = ('Jordan', 'Saudi Arabia', 'Egypt','United Arab Emirates','Qatar','Morroco')
        col1,col2,col3,col4 = st.columns(4)
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
        with col4:
            country = st.selectbox(
             'Choose Country',
             list_count,
              key = 4)
    
            
        submitted = st.form_submit_button('Submit')
    
    
    st.header('Fixed Types')
    
    
    camp_name = ['Choose One','Brand 1','Brand 2','Brand 3','Brand 4','Brand 5','Brand 6','Brand 7','Brand 8','Brand 9','Brand 10']
    
    ###########################################################################
    col1, col2 ,col3 = st.columns(3)
    with col1:
        st.image(image_users, caption='Sunrise by the mountains',use_column_width=True)
        genre = st.radio(
         "What Type of Report Do You Want ?",
         ('Employee', 'Board'))
        
        users = st.button('Download Users Presentation')
        
        if genre == 'Employee':
            if users:
             #file_name1 = files_creation.users_files_emp()
             #genPowerPoint.slides_gen_users_emp()
             st.success('Presentation Done')
        else:
            if users:
             #file_name1 = files_creation.users_files_boar()
             #genPowerPoint.slides_gen_board()
             st.success('Presentation Done')
         
         
    with col2:
        
        st.image(image_users, caption='Sunrise by the mountains',use_column_width=True)
        selected_camp = st.selectbox(
         'Choose Camping',
         camp_name,index =0,key=1)
        merchant = st.button('Download Brand Presentation')
        if selected_camp != 'Choose Camping':
            if merchant:
                #file_name3,camp_name = files_creation.merchant_file_clients()
                #genPowerPoint.slides_gen_clients()
                st.success('Presentation Done')
         
         
    with col3:
        st.image(image_users, caption='Sunrise by the mountains',use_column_width=True)
        
        merchant_users = st.button('Download Merchant Presentation')
        
        if merchant_users:
         #file_name1 = files_creation.merchant_file_all()
         #genPowerPoint.slides_gen_merchant()
         st.success('Presentation Done')  
    
