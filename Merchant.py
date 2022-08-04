import chart_pr
import streamlit as st
from datetime import datetime



row1="""
<div class="title">
    <h5>All Campaigns</h5>
"""
row2="""
<div class="title">
    <h5>Gender Per Campaign</h5>
"""
row3="""
<div class="title">
    <h5>AGE Group Per Campaign</h5>
"""
row4="""
<div class="title">
    <h5>Coins Per Campaign</h5>
"""
row5="""
<div class="title">
    <h5>Smileys Per Campaign</h5>
"""
row6="""
<div class="title">
    <h5>Gifts Per Campaign</h5>
"""
row7="""
<div class="title">
    <h5>Campaigns Gantt Chart</h5>
"""


def app():
    with st.container():
        st.title('Merchant')
        st.markdown("<hr/>", unsafe_allow_html=True)
        list_camp = ['All','camp1','camp2','camp3']
        list_count = ('Jordan', 'Saudi Arabia', 'Egypt','United Arab Emirates','Qatar','Morroco')
        st.subheader('Filtring')
        with st.form(key='columns_in_form'):
            col1,col2,col3,col4 = st.columns(4)
            with col1:
                selected = st.selectbox(
                 'Choose Time Period1',
                 ('This Day', 'This Week','Last Week', 'This Month'
                                                 ,'Last Month','This Year','Custom Date'),index =6,key = 1)
            with col2:
                from_date1 =st.date_input('Custom date for marchent',value=(datetime(2021, 12, 1), datetime(2022, 1, 1)),key = 2)    
            with col3:
                campaigns = st.multiselect(
                 'Choose campaigns',
                 list_camp,
                 list_camp[0],key = 3)
            with col4:
                country = st.selectbox(
                 'Choose Country',
                 list_count,
                  key = 4)
            submitted = st.form_submit_button('Submit')
        country1 = country 
        
        
        
        merchant = chart_pr.marchant_chart(selected,country1,from_date1[0], from_date1[1])
        
        ######################## ROW 1 ########################################
        st.markdown(row1, unsafe_allow_html=True)
        
        col1,col2 = st.columns(2)
        with col1:
            st.plotly_chart(merchant[0],use_container_width=True)
            st.plotly_chart(merchant[1],use_container_width=True)
        
        with col2:
            st.plotly_chart(merchant[2],use_container_width=True)
            st.plotly_chart(merchant[3],use_container_width=True)
    
              
        ######################## ROW 2 ########################################    
        st.markdown(row2, unsafe_allow_html=True)
        
        col1,col2,col3 = st.columns([0.664,1,0.6])
        with col1:
            #
            st.plotly_chart(merchant[4],use_container_width=True)
        with col2:
            st.plotly_chart(merchant[5],use_container_width=True) 
        with col3:
            #
            st.plotly_chart(merchant[6],use_container_width=True)
            
        st.plotly_chart(merchant[7],use_container_width=True)    
        
        ######################## ROW 3 ########################################    

        st.markdown(row3, unsafe_allow_html=True)
        
        col1,col2 = st.columns([0.5,1])
        with col1:
            #
            st.plotly_chart(merchant[8],use_container_width=True)
        with col2:
            st.plotly_chart(merchant[9],use_container_width=True) 
        st.plotly_chart(merchant[10],use_container_width=True)
        
        
        col1,col2,col3 = st.columns([1,2,2])
        with col1:
            st.plotly_chart(merchant[11],use_container_width=True)
        with col2:
            st.plotly_chart(merchant[12],use_container_width=True)
        with col3:    
            st.plotly_chart(merchant[13],use_container_width=True)
        
        st.markdown(row7, unsafe_allow_html=True)
        st.plotly_chart(merchant[14],use_container_width=True)
        
        ###############################Row4####################################
        st.markdown(row4, unsafe_allow_html=True)
        
        st.plotly_chart(merchant[15],use_container_width=True)
        st.markdown("<hr/>", unsafe_allow_html=True)
        st.markdown(f'<h5 style="color:#31333F;font-size:30px;">{"Coins Catch per Gender"}</h5>', unsafe_allow_html=True)
        st.plotly_chart(merchant[16],use_container_width=True)
        st.markdown("<hr/>", unsafe_allow_html=True)
        st.markdown(f'<h5 style="color:#31333F;font-size:30px;">{"Coins Catch per Age"}</h5>', unsafe_allow_html=True)
        st.plotly_chart(merchant[17],use_container_width=True)
      
        ###############################Row5####################################
        st.markdown(row5, unsafe_allow_html=True)

        st.plotly_chart(merchant[18],use_container_width=True)
        st.markdown("<hr/>", unsafe_allow_html=True)
        st.markdown(f'<h5 style="color:#31333F;font-size:30px;">{"Smiley Catch per Gender"}</h5>', unsafe_allow_html=True)
        st.plotly_chart(merchant[19],use_container_width=True)
        st.markdown("<hr/>", unsafe_allow_html=True)
        st.markdown(f'<h5 style="color:#31333F;font-size:30px;">{"Smiley Catch per Age"}</h5>', unsafe_allow_html=True)
        st.plotly_chart(merchant[20],use_container_width=True)
        
        ###############################Row6####################################
        st.markdown(row6, unsafe_allow_html=True)
        
        st.plotly_chart(merchant[21],use_container_width=True)
        st.markdown("<hr/>", unsafe_allow_html=True)
        st.markdown(f'<h5 style="color:#31333F;font-size:30px;">{"Gift Catch per Gender"}</h5>', unsafe_allow_html=True)
        st.plotly_chart(merchant[22],use_container_width=True)
        st.markdown("<hr/>", unsafe_allow_html=True)
        st.markdown(f'<h5 style="color:#31333F;font-size:30px;">{"Gift Catch per Age"}</h5>', unsafe_allow_html=True)
        st.plotly_chart(merchant[23],use_container_width=True)
        
