import streamlit as st
from datetime import datetime
import chart_pr


coins="""
<div class="title">
    <h5>Coins Availabel and Consumed</h5>
"""
smiley="""
<div class="title">
    <h5>Smiley Availabel and Consumed</h5>
"""
gifts="""
<div class="title">
    <h5>Gifts Availabel and Consumed</h5>
"""
camp_information="""
<div class="title">
    <h5>Campaing Information</h5>
"""
age_player="""
<div class="title">
    <h5>Campaing Age Player</h5>
"""
gender_player="""
<div class="title">
    <h5>Campaing Gender Player</h5>
"""
coins_catches_gender="""
<div class="title">
    <h5>Coins Catches Per Gender</h5>
"""
coins_catches_age="""
<div class="title">
    <h5>Coins Catches Per Age Group</h5>
</div>
"""
smiley_catches_gender="""
<div class="title">
    <h5>Smiley Catches Per Gender</h5>
"""
smiley_catches_age="""
<div class="title">
    <h5>Smiley Catches Per Age Group</h5>
"""
gifts_catches_gender="""
<div class="title">
    <h5>Gifts Catches Per Gender</h5>
"""
gifts_catches_age="""
<div class="title">
    <h5>Gifts Catches Per Age Group</h5>
"""




def app():
    with st.container():
        st.title('Campaings Insights')
        st.markdown("<hr/>", unsafe_allow_html=True)
        st.subheader('Filtring')

        
        with st.form(key='columns_in_form'):
            list_count = ('Jordan', 'Saudi Arabia', 'Egypt','United Arab Emirates','Qatar','Morroco')
            col1,col2,col3 = st.columns(3)
            with col1:
                selected = st.selectbox(
                 'Choose Time Period',
                 ('This Day', 'This Week','Last Week', 'This Month'
                                                 ,'Last Month','This Year','Custom Date'),index =6,key=1)
            with col2:
                from_date2 =st.date_input('Custom date for all data',value=(datetime(2021, 12, 1), datetime(2022, 1, 1)),key = 3)
            with col3:
                country = st.selectbox(
                 'Choose Country',
                 list_count,
                  key = 4)
                
            submitted = st.form_submit_button('Submit')
        st.markdown(f'<h5 style="color:#31333F;font-size:30px;">{"Choose Campaign"}</h5>', unsafe_allow_html=True)    
        
        
        
        camp_name = ['Choose One','Brand 1','Brand 2','Brand 3','Brand 4','Brand 5','Brand 6','Brand 7','Brand 8','Brand 9','Brand 10']
        
            
        selected_camp = st.selectbox(
         'Choose Camping',
         camp_name,index =0,key=1)  
        
        
        #######################################################################
        if selected_camp == 'Choose One':
            st.info('Please Choose Campaing')
        else:
            campaigns = chart_pr.campaigns_charts()
           
            
            st.markdown(camp_information, unsafe_allow_html=True)
            col1,col2,col3 =st.columns(3)
            with col1:
                st.plotly_chart(campaigns[12],use_container_width=True)
            with col2:
                st.plotly_chart(campaigns[11],use_container_width=True)
            with col3:
                st.plotly_chart(campaigns[4],use_container_width=True)
            #######################################################################
            st.markdown("<hr/>", unsafe_allow_html=True)
            col1,col2 = st.columns(2)
            with col1:
                st.markdown(gender_player, unsafe_allow_html=True)
                st.plotly_chart(campaigns[0],use_container_width=True)
                st.plotly_chart(campaigns[1],use_container_width=True)
            with col2:
                st.markdown(age_player, unsafe_allow_html=True)
                st.plotly_chart(campaigns[2],use_container_width=True)
                st.plotly_chart(campaigns[3],use_container_width=True)
                
            ###################################################################    
            st.markdown("<hr/>", unsafe_allow_html=True)    
            st.markdown(f'<h5 style="color:#31333F;font-size:30px;">{"Coins Per Campaign"}</h5>', unsafe_allow_html=True)    
            st.markdown("<hr/>", unsafe_allow_html=True)
            col1,col2 = st.columns(2)
            with col1:
                st.markdown(coins, unsafe_allow_html=True)
                st.plotly_chart(campaigns[5],use_container_width=True)
                st.plotly_chart(campaigns[8],use_container_width=True)
            with col2:
                st.markdown(coins_catches_gender, unsafe_allow_html=True)
                st.plotly_chart(campaigns[13],use_container_width=True)
                st.plotly_chart(campaigns[14],use_container_width=True)
                
            st.markdown(coins_catches_age, unsafe_allow_html=True)    
            col1,col2 = st.columns(2)
            with col1:
                st.plotly_chart(campaigns[15],use_container_width=True)
            with col2:
                st.write('')
                st.write('')
                st.write('')
                st.write('')
                st.write('')
                st.write('')
                st.write('')
                st.plotly_chart(campaigns[16],use_container_width=True)
            
            ###################################################################
            
            ###################################################################    
            st.markdown("<hr/>", unsafe_allow_html=True)    
            st.markdown(f'<h5 style="color:#31333F;font-size:30px;">{"Smiley Per Campaign"}</h5>', unsafe_allow_html=True)    
            st.markdown("<hr/>", unsafe_allow_html=True)
            col1,col2 = st.columns(2)
            with col1:
                st.markdown(smiley, unsafe_allow_html=True)
                st.plotly_chart(campaigns[6],use_container_width=True)
                st.plotly_chart(campaigns[9],use_container_width=True)
            with col2:
                st.markdown(smiley_catches_gender, unsafe_allow_html=True)
                st.plotly_chart(campaigns[17],use_container_width=True)
                st.plotly_chart(campaigns[18],use_container_width=True)
                
            st.markdown(smiley_catches_age, unsafe_allow_html=True)    
            col1,col2 = st.columns(2)
            with col1:
                st.plotly_chart(campaigns[19],use_container_width=True)
            with col2:
                st.write('')
                st.write('')
                st.write('')
                st.write('')
                st.write('')
                st.write('')
                st.write('')
                st.plotly_chart(campaigns[20],use_container_width=True)
            
            ###################################################################
            
            ###################################################################    
            st.markdown("<hr/>", unsafe_allow_html=True)    
            st.markdown(f'<h5 style="color:#31333F;font-size:30px;">{"Gifts Per Campaign"}</h5>', unsafe_allow_html=True)    
            st.markdown("<hr/>", unsafe_allow_html=True)
            col1,col2 = st.columns(2)
            with col1:
                st.markdown(gifts, unsafe_allow_html=True)
                st.plotly_chart(campaigns[7],use_container_width=True)
                st.plotly_chart(campaigns[10],use_container_width=True)
            with col2:
                st.markdown(gifts_catches_gender, unsafe_allow_html=True)
                st.plotly_chart(campaigns[21],use_container_width=True)
                st.plotly_chart(campaigns[22],use_container_width=True)
                
            st.markdown(gifts_catches_age, unsafe_allow_html=True)    
            col1,col2 = st.columns(2)
            with col1:
                st.plotly_chart(campaigns[23],use_container_width=True)
            with col2:
                st.write('')
                st.write('')
                st.write('')
                st.write('')
                st.write('')
                st.write('')
                st.write('')
                st.plotly_chart(campaigns[24],use_container_width=True)
            
            ###################################################################
            
            