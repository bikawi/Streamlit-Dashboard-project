import plotly.graph_objects as go
from plotly.subplots import make_subplots
from load_all_images import load_images
import plotly.figure_factory as ff


date = ["2021-11-01","2021-11-02","2021-11-03","2021-11-04","2021-11-05","2021-11-06",
        "2021-11-07","2021-11-08","2021-11-09","2021-11-10","2021-11-11","2021-11-12",
        "2021-11-13","2021-11-14","2021-11-15","2021-11-16","2021-11-17","2021-11-18",
        "2021-11-19","2021-11-20","2021-11-21","2021-11-22","2021-11-23","2021-11-24",
        "2021-11-25","2021-11-26","2021-11-27","2021-11-28","2021-11-29","2021-11-30"]

gantt_list = [{"Task": "Brand 1",
    "Start": "datetime.date(2021, 11, 21)",
    "Finish": "datetime.date(2022, 2, 28)",
    "Resource": "Active"},
  {"Task": "Brand 2",
    "Start": "datetime.date(2021, 4, 1)",
    "Finish": "datetime.date(2021, 12, 31)",
    "Resource": "Inactive"},
  {"Task": "Brand 3",
    "Start": "datetime.date(2021, 4, 1)",
    "Finish": "datetime.date(2022, 1, 31)",
    "Resource": "Inactive"},
  {"Task": "Brand 4",
    "Start": "datetime.date(2021, 4, 1)",
    "Finish": "datetime.date(2021, 12, 30)",
    "Resource": "Active"},
  {"Task": "Brand 5",
    "Start": "datetime.date(2021, 4, 1)",
    "Finish": "datetime.date(2021, 12, 30)",
    "Resource": "Inactive"},
  {"Task": "Brand 6",
    "Start": "datetime.date(2021, 4, 1)",
    "Finish": "datetime.date(2022, 3, 31)",
    "Resource": "Inactive"},
  {"Task": "Brand 7",
    "Start": "datetime.date(2021, 4, 1)",
    "Finish": "datetime.date(2021, 12, 30)",
    "Resource": "Inactive"},
  {"Task": "Brand 8",
    "Start": "datetime.date(2021, 4, 1)",
    "Finish": "datetime.date(2021, 12, 30)",
    "Resource": "Inactive"},
  {"Task": "Brand 9",
    "Start": "datetime.date(2021, 4, 1)",
    "Finish": "datetime.date(2021, 12, 30)",
    "Resource": "Inactive"},
  {"Task": "Brand 10",
    "Start": "datetime.date(2021, 9, 15)",
    "Finish": "datetime.date(2021, 12, 31)",
    "Resource": "Inactive"}]




def home_page():
    
    fire_Logo,adjust_Logo,google_Logo,local_Logo,apple_Logo=load_images()

    
    home1 = go.Figure()

    home1.add_trace(go.Indicator(
            title = {'text': "<b>Local Data</b><br><span style='color: #31333F; font-size:0.8em'>NO. User</span>"
                     ,"font": {"size": 20, 'color': "#248f24"}},
            mode = "number+delta",
            value = 2481,
            number={"font": {"size": 30, 'color': "#31333F"}},
            delta = {'reference': 2700, 'relative': True, "valueformat": ".0%"},
            domain = {'row': 0, 'column': 0}))
        
    home1.add_trace(go.Indicator(
            title = {'text': "<b>Adujst</b><br><span style='color: #31333F; font-size:0.8em'>NO. User</span>"
                     ,"font": {"size": 20, 'color': "#1d7595"}},
            mode = "number+delta",
            value = 5590,
            number={"font": {"size": 30, 'color': "#31333F"}},
            delta = {'reference': 6000, 'relative': True, "valueformat": ".0%"},
            domain = {'row': 0, 'column': 1}))
    
    home1.update_layout(
            grid = {'rows': 1, 'columns': 2, 'pattern': "independent"})
        
    home1.update_layout(width=600,height = 189 , margin = {'t':35, 'b':0, 'l':50,'r':50},paper_bgcolor = "#FFFFFF")
    home1.update_traces(delta_decreasing_color="#FF4B4B",
                                     delta_increasing_color="#0a7559",
                                     selector=dict(type='indicator'))
    
    
    ###########################################################################
    
    home2 = go.Figure()
    home2.add_trace(go.Scatter(x=date, y=[32,31,23,31,41,34,112,173,254,178,140,112,57,157,70,128,52,91,82,52,74,46,195,46,54,72,35,40,39,30],
                        mode='lines+markers',
                        name='Local Database',line_color="#248f24"))
    home2.add_trace(go.Scatter(x=date, y=[110,99,83,94,118,96,249,422,428,406,274,257,121,278,113,178,87,212,183,82,259,204,333,182,179,177,82,87,97,98],
                        mode='lines+markers',
                        name='Adjust',line_color="#1d7595"))
    home2.update_layout(autosize=False,paper_bgcolor="#FFFFFF", plot_bgcolor="#FFFFFF",hovermode="x unified"
                      ,width=600, height=350, margin=dict(l=20, r=20, b=20, t=70),
                     title={
                            #'text': "Installation Information",
                            'y':0.98,
                            'x':0.4,
                            'xanchor': 'center',
                            'yanchor': 'top'},
                        xaxis_title="Date",
                        yaxis_title="Number of Users"
                        ,legend=dict(
                                    orientation="h",
                                    yanchor="bottom",
                                    y=1.02,
                                    xanchor="right",
                                    x=1
                                  ) )
    home2.update_xaxes(mirror=True,showgrid=True,showline=True, linewidth=1, linecolor='#afb9cf', gridcolor='#dfe3ec')
    home2.update_yaxes(mirror=True,showgrid=True,showline=True, linewidth=1, linecolor='#afb9cf', gridcolor='#dfe3ec')
    
    home2.layout.xaxis.fixedrange = True
    home2.layout.yaxis.fixedrange = True
    ###########################################################################
    home3 = go.Figure()

    home3.add_trace(go.Indicator(
            title = {'text': "<b>Adjust</b><br><span style='color: #31333F; font-size:0.8em'>NO. User</span>"
                     ,"font": {"size": 20, 'color': "#1d7595"}},
            mode = "number+delta",
            value = 10320,
            number={"font": {"size": 30, 'color': "#31333F"}},
            delta = {'reference': 10500, 'relative': True, "valueformat": ".0%"},
            domain = {'row': 0, 'column': 0}))
        
    home3.add_trace(go.Indicator(
            title = {'text': "<b>Firebase</b><br><span style='color: #31333F; font-size:0.8em'>NO. User</span>"
                     ,"font": {"size": 20, 'color': "#af8104"}},
            mode = "number+delta",
            value = 10450,
            number={"font": {"size": 30, 'color': "#31333F"}},
            delta = {'reference': 10800, 'relative': True, "valueformat": ".0%"},
            domain = {'row': 0, 'column': 1}))
    
    home3.update_layout(
            grid = {'rows': 1, 'columns': 2, 'pattern': "independent"})
        
    home3.update_layout(width=600,height = 189 , margin = {'t':35, 'b':0, 'l':50,'r':50},paper_bgcolor = "#FFFFFF")
    home3.update_traces(delta_decreasing_color="#FF4B4B",
                                     delta_increasing_color="#0a7559",
                                     selector=dict(type='indicator'))
    ###########################################################################
    
    home33 = go.Figure()
    
    home33.add_trace(go.Indicator(
            title = {'text': "<b>Google Console</b><br><span style='color: #31333F; font-size:0.8em'>NO. User</span>"
                     ,"font": {"size": 20, 'color': "#31333F"}},
            mode = "number+delta",
            value = 15000,
            number={"font": {"size": 30, 'color': "#31333F"}},
            delta = {'reference': 14000, 'relative': True, "valueformat": ".0%"},
            domain = {'row': 0, 'column': 0}))
    
    home33.add_trace(go.Indicator(
            title = {'text': "<b>Apple Store</b><br><span style='color: #31333F; font-size:0.8em'>NO. User</span>"
                     ,"font": {"size": 20, 'color': "#7d8182"}},
            mode = "number+delta",
            value = 4000,
            number={"font": {"size": 30, 'color': "#31333F"}},
            delta = {'reference': 3000, 'relative': True, "valueformat": ".0%"},
            domain = {'row': 0, 'column': 1}))
    
    home33.update_layout(
            grid = {'rows': 1, 'columns': 2, 'pattern': "independent"})
        
    home33.update_layout(width=600,height = 189 , margin = {'t':35, 'b':0, 'l':50,'r':50},paper_bgcolor = "#FFFFFF")
    home33.update_traces(delta_decreasing_color="#FF4B4B",
                                     delta_increasing_color="#0a7559",
                                     selector=dict(type='indicator'))
    ###########################################################################
    
    home4 = go.Figure()
    home4.add_trace(go.Scatter(x=date, y=[452,489,419,447,485,433,482,527,527,515,515,472,411,455,426,437,399,438,435,407,367,362,339,358,351,397,367,373,335,357],
                        mode='lines+markers',
                        name='Adjust',line_color="#1d7595"))
    home4.add_trace(go.Scatter(x=date, y=[468,520,439,470,502,458,548,576,585,566,552,503,445,451,424,462,422,469,434,419,373,396,348,348,362,405,380,385,354,365],
                        mode='lines+markers',
                        name='Firebase',line_color="#af8104"))
    home4.add_trace(go.Scatter(x=date, y=[54,50,48,50,51,63,162,212,207,191,138,73,77,57,73,63,78,71,92,59,61,76,74,53,55,74,57,56,67,74],
                        mode='lines+markers',
                        name='Google Console',line_color="#31333F"))
    home4.add_trace(go.Scatter(x=date, y=[3,4,2,1,6,7,13,7,11,22,27,11,6,10,11,6,4,11,10,7,4,7,6,4,7,1,5,6,6,5],
                        mode='lines+markers',
                        name='Apple Store',line_color="#7d8182"))
    home4.update_layout(autosize=False,paper_bgcolor="#FFFFFF", plot_bgcolor="#FFFFFF",hovermode="x unified"
                      ,width=600, height=350, margin=dict(l=20, r=20, b=20, t=70),
                     title={
                            'y':0.98,
                            'x':0.4,
                            'xanchor': 'center',
                            'yanchor': 'top'},
                        xaxis_title="Date",
                        yaxis_title="Number of Users"
                        ,legend=dict(
                                    orientation="h",
                                    yanchor="bottom",
                                    y=1.02,
                                    xanchor="right",
                                    x=1
                                  ) )
    home4.update_xaxes(mirror=True,showgrid=True,showline=True, linewidth=1, linecolor='#afb9cf', gridcolor='#dfe3ec')
    home4.update_yaxes(mirror=True,showgrid=True,showline=True, linewidth=1, linecolor='#afb9cf', gridcolor='#dfe3ec')
    
    home4.layout.xaxis.fixedrange = True
    home4.layout.yaxis.fixedrange = True
    ###########################################################################
    
    home5 = make_subplots(rows=1, cols=1, specs=[[{'type':'domain'}]])
    
    home5.add_trace(go.Indicator(
            mode = "number+delta",
            value = 5400,
            number = {"font": {"size": 35,'color': "#31333F"}},
            delta = {"reference": 3500, 'relative': True, "valueformat": ".0%"},
        ),row = 1 ,col = 1)
    
    home5.add_trace(go.Pie(labels=['Active Users'], values=[1], hole=.85,hoverinfo='skip', textinfo='none'
                             ,showlegend=False,marker=dict(colors=['#fbc226'])), row=1, col=1)
    
    
    home5.update_layout(autosize=False,paper_bgcolor="#FFFFFF", plot_bgcolor="#FFFFFF",
                           width=700, height=400, margin=dict(l=70, r=70, b=70, t=70),
                          xaxis=dict(showgrid=False,showline=False,showticklabels=False,zerolinecolor='#F0F2F6'),
                      yaxis=dict(showgrid=False,showline=False,showticklabels=False,zerolinecolor='#F0F2F6'),
                         ) 
    
    home5.add_layout_image(
                dict(
                    source=fire_Logo,
                    xref="paper",
                    yref="paper",
                    x=0.175,
                    y=1.2,
                    sizex=0.6,
                    sizey=0.6,
                    opacity=0.9,
                    layer="above"
                    )
                )
    
    ###########################################################################
    home6 = make_subplots(rows=1, cols=1, specs=[[{'type':'domain'}]])
    
    home6.add_trace(go.Indicator(
            mode = "number+delta",
            value = 5300,
            number = {"font": {"size": 35,'color': "#31333F"}},
            delta = {"reference": 3500, 'relative': True, "valueformat": ".0%"},
        ),row = 1 ,col = 1)
    
    home6.add_trace(go.Pie(labels=['Active Users'], values=[1], hole=.85,hoverinfo='skip', textinfo='none'
                             ,showlegend=False,marker=dict(colors=['#2596be'])), row=1, col=1)
    
    home6.update_layout(autosize=False,paper_bgcolor="#FFFFFF", plot_bgcolor="#FFFFFF",
                           width=700, height=400, margin=dict(l=70, r=70, b=70, t=70),
                          xaxis=dict(showgrid=False,showline=False,showticklabels=False,zerolinecolor='#F0F2F6'),
                      yaxis=dict(showgrid=False,showline=False,showticklabels=False,zerolinecolor='#F0F2F6'),
                         ) 

    home6.add_layout_image(
                dict(
                    source=adjust_Logo,
                    xref="paper",
                    yref="paper",
                    x=0.27,
                    y=1.2,
                    sizex=0.5,
                    sizey=0.5,
                    opacity=0.9,
                    layer="above"
                    )
                )
    
    ###########################################################################
    

    home7 = make_subplots(rows=1, cols=1, specs=[[{'type':'domain'}]])

    home7.add_trace(go.Indicator(
            mode = "number+delta",
            value = 6500,
            number = {"font": {"size": 35,'color': "#31333F"}},
            delta = {"reference": 6000, 'relative': True, "valueformat": ".0%"},
        ),row = 1 ,col = 1)
    
    home7.add_trace(go.Pie(labels=['Active Users'], values=[1], hole=.85,hoverinfo='skip', textinfo='none'
                             ,showlegend=False,marker=dict(colors=['#7e8384'])), row=1, col=1)
    
    home7.update_layout(autosize=False,paper_bgcolor="#FFFFFF", plot_bgcolor="#FFFFFF",
                           width=700, height=400, margin=dict(l=70, r=70, b=70, t=70),
                          xaxis=dict(showgrid=False,showline=False,showticklabels=False,zerolinecolor='#F0F2F6'),
                      yaxis=dict(showgrid=False,showline=False,showticklabels=False,zerolinecolor='#F0F2F6'),
                         ) 
    
    home7.add_layout_image(
                dict(
                    source=google_Logo,
                    xref="paper",
                    yref="paper",
                    x=0.15,
                    y=1.18,
                    sizex=0.7,
                    sizey=0.7,
                    opacity=0.9,
                    layer="above"
                    )
                )
    ###########################################################################
    home8 = make_subplots(rows=1, cols=1, specs=[[{'type':'domain'}]])
    
    home8.add_trace(go.Indicator(
            mode = "number+delta",
            value = 3200,
            number = {"font": {"size": 35,'color': "#31333F"}},
            delta = {"reference": 3000, 'relative': True, "valueformat": ".0%"},
         
        ),row = 1 ,col = 1)
    
    home8.add_trace(go.Pie(labels=['Active Users'], values=[1], hole=.85,hoverinfo='skip', textinfo='none'
                             ,showlegend=False,marker=dict(colors=['#248f24'])), row=1, col=1)
    
    home8.update_layout(autosize=False,paper_bgcolor="#FFFFFF", plot_bgcolor="#FFFFFF",
                           width=700, height=400, margin=dict(l=70, r=70, b=70, t=70),
                          xaxis=dict(showgrid=False,showline=False,showticklabels=False,zerolinecolor='#F0F2F6'),
                      yaxis=dict(showgrid=False,showline=False,showticklabels=False,zerolinecolor='#F0F2F6'),
                         ) 
    
    home8.add_layout_image(
                dict(
                    source=local_Logo,
                    xref="paper",
                    yref="paper",
                    x=0.45,
                    y=1.17,
                    sizex=0.15,
                    sizey=0.15,
                    opacity=0.9,
                    layer="below"
                    )
                )
    
    ###########################################################################
    home9 = go.Figure()

    home9.add_trace(go.Indicator(
                title = {'text': "<b>Day 1</b><br><span style='color: #31333F; font-size:0.8em'>AVG</span>"
                         ,"font": {"size": 20, 'color': "#31333F"}},
                number={'suffix': "%","font": {"size": 30, 'color': "#cc9c00"}},
                mode = "number",
                value = 21.5,
                    
                domain = {'row': 0, 'column': 0}))    
    home9.add_trace(go.Indicator(
                title = {'text': "<b>Day 7</b><br><span style='color: #31333F; font-size:0.8em'>AVG</span>"
                         ,"font": {"size": 20, 'color': "#31333F"}},
                mode = "number",
                value = 4.5,
                number={'suffix': "%","font": {"size": 30, 'color': "#cc9c00"}},
                domain = {'row': 0, 'column': 1}))
    home9.add_trace(go.Indicator(
                title = {'text': "<b>Day 30</b><br><span style='color: #31333F; font-size:0.8em'>AVG</span>"
                         ,"font": {"size": 20, 'color': "#31333F"}},
                mode = "number",
                value = 2.5,
                number={'suffix': "%","font": {"size": 30, 'color': "#cc9c00"}},
                domain = {'row': 0, 'column': 2}))
            
    home9.update_layout(
                grid = {'rows': 1, 'columns': 3, 'pattern': "independent"})
        
    home9.update_layout(autosize=False,paper_bgcolor="#FFFFFF", plot_bgcolor="#FFFFFF",width=800, height=200, margin=dict(l=20, r=20, b=20, t=65))
        
    home9.add_layout_image(
                dict(
                    source=fire_Logo,
                    xref="paper",
                    yref="paper",
                    x=0.0,
                    y=1.5
                    ,
                    sizex=0.45,
                    sizey=0.45,
                    opacity=0.9,
                    layer="below"
                    )
                )
    
    ###########################################################################
    home10 = go.Figure()
        
    home10.add_trace(go.Indicator(
                title = {'text': "<b>Day 1</b><br><span style='color: #31333F; font-size:0.8em'>AVG</span>"
                         ,"font": {"size": 20, 'color': "#31333F"}},
                mode = "number",
                value = 22.2,
                number={'suffix': "%","font": {"size": 30, 'color': "#2697c0"}},
                domain = {'row': 0, 'column': 0}))
        
    home10.add_trace(go.Indicator(
                title = {'text': "<b>Day 7</b><br><span style='color: #31333F; font-size:0.8em'>AVG</span>"
                         ,"font": {"size": 20, 'color': "#31333F"}},
                mode = "number",
                value = 4.1,
                number={'suffix': "%","font": {"size": 30, 'color': "#2697c0"}},
                domain = {'row': 0, 'column': 1}))
            
    home10.add_trace(go.Indicator(
                title = {'text': "<b>Day 30</b><br><span style='color: #31333F; font-size:0.8em'>AVG</span>"
                         ,"font": {"size": 20, 'color': "#31333F"}},
                mode = "number",
                value = 2.1,
                number={'suffix': "%","font": {"size": 30, 'color': "#2697c0"}},
                domain = {'row': 0, 'column': 2}))
        
        
            
        
    home10.update_layout(
                grid = {'rows': 1, 'columns': 3, 'pattern': "independent"})
    home10.update_layout(autosize=False,paper_bgcolor="#FFFFFF", plot_bgcolor="#FFFFFF",
                        width=800, height=200, margin=dict(l=20, r=20, b=20, t=65))
        
        
    home10.add_layout_image(
                dict(
                    source=adjust_Logo,
                    xref="paper",
                    yref="paper",
                    x=0.0,
                    y=1.5,
                    sizex=0.35,
                    sizey=0.35,
                    opacity=0.9,
                    layer="below"
                    )
                )
        

    ###########################################################################
    home11 = go.Figure()

    home11.add_trace(go.Indicator(
        mode = "gauge", value = 21.5,
        number={'suffix': "%"},
        domain = {'row': 0, 'column': 0},
        title = {'text' :"<b>Day 1</b>"},
        gauge = {
            'shape': "bullet",
            'bar': {'color': "#31333F"},
            'axis': {'range': [0, 40]}, 
            'borderwidth': 3,
                'bordercolor': "#262626",
            'threshold': {
                'line': {'color': "black", 'width': 2},
                'thickness': 0.75,
                'value': 280},
            'steps': [
                {'range': [0, 19], 'color': "#ff4d4d"},
                {'range': [19, 31], 'color': "#ffff66"},
                {'range': [31, 40], 'color': "#99ff66"}]}))   
    home11.add_trace(go.Indicator(
        mode = "gauge", value = 4.5,
        domain = {'row': 1, 'column': 0},
        title = {'text' :"<b>Day 7</b>"},
        gauge = {
            'shape': "bullet",
            'bar': {'color': "#31333F"},
            'axis': {'range': [0, 15]},
            'borderwidth': 3,
                'bordercolor': "#262626",
            'threshold': {
                'line': {'color': "black", 'width': 2},
                'thickness': 0.75,
                'value': 280},
            'steps': [
                {'range': [0, 3], 'color': "#ff4d4d"},
                {'range': [3, 8], 'color': "#ffff66"},
                {'range': [8, 15], 'color': "#99ff66"}]}))
    home11.add_trace(go.Indicator(
        mode = "gauge", value = 2.5,
        domain = {'row': 2, 'column': 0},
        title = {'text' :"<b>Day 30</b>"},
        gauge = {
            'shape': "bullet",
            'bar': {'color': "#31333F"},
            'axis': {'range': [0, 7]},
            'borderwidth': 3,
                'bordercolor': "#262626",
            'threshold': {
                'line': {'color': "black", 'width': 2},
                'thickness': 0.75,
                'value': 280},
            'steps': [
                {'range': [0, 0.5], 'color': "#ff4d4d"},
                {'range': [0.5, 3], 'color': "#ffff66"},
                {'range': [3, 7], 'color': "#99ff66"}]}))
    
    home11.update_layout(
                grid = {'rows': 3, 'columns': 1, 'pattern': "independent"})
    home11.update_layout(autosize=False,paper_bgcolor="#FFFFFF", plot_bgcolor="#FFFFFF",width=700, height=300, margin=dict(l=100, r=20, b=20, t=20))
    ###########################################################################
    home12 = go.Figure()

    home12.add_trace(go.Indicator(
        mode = "gauge", value = 22.2,
        number={'suffix': "%"},
        domain = {'row': 0, 'column': 0},
        title = {'text' :"<b>Day 1</b>"},
        gauge = {
            'shape': "bullet",
            'bar': {'color': "#31333F"},
            'axis': {'range': [0, 40]},
            'borderwidth': 3,
                'bordercolor': "#262626",
            'threshold': {
                'line': {'color': "black", 'width': 2},
                'thickness': 0.75,
                'value': 280},
            'steps': [
                {'range': [0, 19], 'color': "#ff4d4d"},
                {'range': [19, 31], 'color': "#ffff66"},
                {'range': [31, 40], 'color': "#99ff66"}]}))   
    home12.add_trace(go.Indicator(
        mode = "gauge", value = 4.1,
        domain = {'row': 1, 'column': 0},
        title = {'text' :"<b>Day 7</b>"},
        gauge = {
            'shape': "bullet",
            'bar': {'color': "#31333F"},
            'axis': {'range': [0, 15]},
            'borderwidth': 3,
                'bordercolor': "#262626",
            'threshold': {
                'line': {'color': "black", 'width': 2},
                'thickness': 0.75,
                'value': 280},
            'steps': [
                {'range': [0, 3], 'color': "#ff4d4d"},
                {'range': [3, 8], 'color': "#ffff66"},
                {'range': [8, 15], 'color': "#99ff66"}]}))
    home12.add_trace(go.Indicator(
        mode = "gauge", value = 2.1,
        domain = {'row': 2, 'column': 0},
        title = {'text' :"<b>Day 30</b>"},
        gauge = {
            'shape': "bullet",
            'bar': {'color': "#31333F"},
            'axis': {'range': [0, 7]},
            'borderwidth': 3,
                'bordercolor': "#262626",
            'threshold': {
                'line': {'color': "black", 'width': 2},
                'thickness': 0.75,
                'value': 280},
            'steps': [
                {'range': [0, 0.5], 'color': "#ff4d4d"},
                {'range': [0.5, 3], 'color': "#ffff66"},
                {'range': [3, 7], 'color': "#99ff66"}]}))
    
    home12.update_layout(
                grid = {'rows': 3, 'columns': 1, 'pattern': "independent"})
    home12.update_layout(autosize=False,paper_bgcolor="#FFFFFF", plot_bgcolor="#FFFFFF",width=700, height=300, margin=dict(l=100, r=20, b=20, t=20))
    ###########################################################################
    home13 = go.Figure()
    
    home13.add_trace(go.Indicator(
            mode = "number",
            value = 7.2,
            number = {'suffix': "%","font": {"size": 20,'color': "#cc9c00"}},
            title = {"text": "Firebase"
                        ,"font": {"size": 18, 'color': "#1a1a1a"}},
        ))
    
    home13.update_layout(autosize=False,paper_bgcolor="#FFFFFF", plot_bgcolor="#FFFFFF",
                        width=800, height=200, margin=dict(l=20, r=20, b=20, t=65))
    ###########################################################################
    home14 = go.Figure()
    
    home14.add_trace(go.Indicator(
            mode = "number",
            value = 7.6,
            number = {'suffix': "%","font": {"size": 20,'color': "#2697c0"}},
            title = {"text": "Adjust"
                        ,"font": {"size": 18, 'color': "#1a1a1a"}},
        ))
    
    home14.update_layout(autosize=False,paper_bgcolor="#FFFFFF", plot_bgcolor="#FFFFFF",
                        width=800, height=200, margin=dict(l=20, r=20, b=20, t=65))
    ###########################################################################
    home15 = go.Figure()
    
    home15.add_trace(go.Indicator(
            mode = "number",
            value = 7,
            number = {'suffix': "%","font": {"size": 20,'color': "#707475"}},
            title = {"text": "Console"
                        ,"font": {"size": 18, 'color': "#1a1a1a"}},
            ))
    
    home15.update_layout(autosize=False,paper_bgcolor="#FFFFFF", plot_bgcolor="#FFFFFF",
                        width=800, height=200, margin=dict(l=20, r=20, b=20, t=65))
    ###########################################################################
    home16 = go.Figure()
    
    home16.add_trace(go.Indicator(
            mode = "number",
            value = 6.4,
            number = {'suffix': "%","font": {"size": 20,'color': "#33cc33"}},
            title = {"text": "Admin"
                        ,"font": {"size": 18, 'color': "#1a1a1a"}},
            ))
    
    home16.update_layout(autosize=False,paper_bgcolor="#FFFFFF", plot_bgcolor="#FFFFFF",
                        width=800, height=200, margin=dict(l=20, r=20, b=20, t=65))
    ###########################################################################
    
    home17 = go.Figure()
    home17.add_trace(go.Scatter(x =date ,y = [4372,4724,4339,4230,4392,4164,4778,4910,5002,4816,4796,4370,4330,4275,4476,4414,4265,4469,4548,4149,4026,4362,4392,4058,4363,4663,4057,4177,4006,4296],
                                name='Firebase DAU', mode='lines+markers'
                                 ,line_width=1.5,marker_size=4,line_color="#FFC300"))
    home17.add_trace(go.Scatter(x =date ,y = [5361,5799,5398,5311,5478,5256,5731,5914,5901,5701,5690,5300,5307,5271,5466,5428,5219,5610,5643,5117,4928,5242,5352,5110,5255,5566,4901,5194,5018,5285],
                                name='Console DAU', mode='lines+markers'
                                 ,line_width=1.5,marker_size=4,line_color="#bfbfbf"))
    home17.add_trace(go.Scatter(x =date ,y = [3680,3963,3652,3613,3617,3487,4037,4264,4326,4143,4130,3661,3594,3739,3886,3811,3644,3872,3838,3495,3413,3740,3708,3506,3726,3993,3395,3590,3429,3704],
                                name='Adjust DAU', mode='lines+markers'
                                 ,line_width=1.5,marker_size=4,line_color="#55b9dd"))
    home17.add_trace(go.Scatter(x =date ,y = [298,318,308,269,324,288,565,737,859,863,779,596,391,580,440,562,398,626,524,359,463,569,744,492,542,632,307,402,361,385],
                                name='Local DAU', mode='lines+markers'
                                 ,line_width=1.5,marker_size=4,line_color="#33cc33"))
        
    home17.update_layout(autosize=False,paper_bgcolor="#FFFFFF", plot_bgcolor="#FFFFFF",hovermode="x unified"
                          ,width=700, height=450, margin=dict(l=20, r=20, b=20, t=70),
                          xaxis=dict(mirror=True,showgrid=True,showline=True, linewidth=1, linecolor='#afb9cf', gridcolor='#dfe3ec'),
                      yaxis=dict(mirror=True,showgrid=True,showline=True, linewidth=1, linecolor='#afb9cf', gridcolor='#dfe3ec'),
                                    xaxis_title="Date",
                                    yaxis_title="DAU"
                                ,legend=dict(
                                            orientation="h",
                                            yanchor="bottom",
                                            y=1.02,
                                            xanchor="right",
                                            x=0.95
                                          ))      
    home17.layout.xaxis.fixedrange = True
    home17.layout.yaxis.fixedrange = True
    
    ###########################################################################
    
    home18 = go.Figure()

    home18.add_trace(go.Indicator(
            mode = "gauge", value = 7.2,
            number={'suffix': "%"},
            domain = {'row': 0, 'column': 0},
            title = {'text' :"<b>Firebase</b>"},
            gauge = {
                'shape': "bullet",
                'bar': {'color': "#31333F"},
                'axis': {'range': [0, 25]}, 
                'borderwidth': 3,
                    'bordercolor': "#262626",
                'threshold': {
                    'line': {'color': "black", 'width': 2},
                    'thickness': 0.75,
                    'value': 280},
                'steps': [
                    {'range': [0, 6], 'color': "#ff4d4d"},
                    {'range': [6, 13], 'color': "#ffff66"},
                    {'range': [13, 25], 'color': "#99ff66"}]}))   
    home18.add_trace(go.Indicator(
            mode = "gauge", value = 7.6,
            domain = {'row': 1, 'column': 0},
            title = {'text' :"<b>Adjust</b>"},
            gauge = {
                'shape': "bullet",
                'bar': {'color': "#31333F"},
                'axis': {'range': [0, 25]},
                'borderwidth': 3,
                    'bordercolor': "#262626",
                'threshold': {
                    'line': {'color': "black", 'width': 2},
                    'thickness': 0.75,
                    'value': 280},
                'steps': [
                    {'range': [0, 6], 'color': "#ff4d4d"},
                    {'range': [6, 13], 'color': "#ffff66"},
                    {'range': [13, 25], 'color': "#99ff66"}]})) 
    
        
    home18.update_layout(
                    grid = {'rows': 2, 'columns': 1, 'pattern': "independent"})
    home18.update_layout(autosize=False,paper_bgcolor="#FFFFFF", plot_bgcolor="#FFFFFF",width=700,
                         height=200, margin=dict(l=100, r=20, b=20, t=20))
    
    ###########################################################################
    home19 = go.Figure()
    
    home19.add_trace(go.Indicator(
            mode = "gauge", value = 7.0,
            number={'suffix': "%"},
            domain = {'row': 0, 'column': 0},
            title = {'text' :"<b>Console</b>"},
            gauge = {
                'shape': "bullet",
                'bar': {'color': "#31333F"},
                'axis': {'range': [0, 25]},
                'borderwidth': 3,
                    'bordercolor': "#262626",
                'threshold': {
                    'line': {'color': "black", 'width': 2},
                    'thickness': 0.75,
                    'value': 280},
                'steps': [
                    {'range': [0, 6], 'color': "#ff4d4d"},
                    {'range': [6, 13], 'color': "#ffff66"},
                    {'range': [13, 25], 'color': "#99ff66"}]}))    
    home19.add_trace(go.Indicator(
            mode = "gauge", value = 6.4,
            domain = {'row': 1, 'column': 0},
            title = {'text' :"<b>Local</b>"},
            gauge = {
                'shape': "bullet",
                'bar': {'color': "#31333F"},
                'axis': {'range': [0, 25]},
                'borderwidth': 3,
                    'bordercolor': "#262626",
                'threshold': {
                    'line': {'color': "black", 'width': 2},
                    'thickness': 0.75,
                    'value': 280},
                'steps': [
                    {'range': [0, 6], 'color': "#ff4d4d"},
                    {'range': [6, 13], 'color': "#ffff66"},
                    {'range': [13, 25], 'color': "#99ff66"}]})) 
        
    home19.update_layout(
                    grid = {'rows': 2, 'columns': 1, 'pattern': "independent"})
    home19.update_layout(autosize=False,paper_bgcolor="#FFFFFF", plot_bgcolor="#FFFFFF",width=700, 
                         height=200, margin=dict(l=100, r=20, b=20, t=20))


    ###########################################################################
    home20 = go.Figure()
            
    home20.add_trace(go.Indicator(
                title = {'text': "Max Engagement Time"
                         ,"font": {"size": 20, 'color': "#31333F"}},
                mode = "number",
                value =20.2,
                number = {'suffix': " min","font": {"size": 30,'color': "#31333F"}},
                ))
    
    
    home20.update_layout(width=600,height = 120 , margin = {'t':70, 'b':0, 'l':50,'r':50},paper_bgcolor = "#ffffff")
    home20.update_traces(delta_decreasing_color="#FF4B4B",
                                         delta_increasing_color="#0a7559",
                                         selector=dict(type='indicator'))
    home20.add_layout_image(
                dict(
                    source=fire_Logo,
                    xref="paper",
                    yref="paper",
                    x=0.1,
                    y=2.5,
                    sizex=0.8,
                    sizey=0.8,
                    opacity=0.9,
                    layer="above"
                    )
                )
    
    ###########################################################################
    home21 = go.Figure()
            
    home21.add_trace(go.Indicator(
                title = {'text': "AVG Engagement Time"
                         ,"font": {"size": 20, 'color': "#31333F"}},
                mode = "number",
                value =11.45,
                number = {'suffix': " min","font": {"size": 30,'color': "#31333F"}},
                ))
    
    
    home21.update_layout(width=600,height = 120 , margin = {'t':70, 'b':0, 'l':50,'r':50},paper_bgcolor = "#ffffff")
    home21.update_traces(delta_decreasing_color="#FF4B4B",
                                         delta_increasing_color="#0a7559",
                                         #delta_valueformat='.3f',
                                         selector=dict(type='indicator'))
    
    ###########################################################################
        
    home22 = go.Figure()
        
    home22.add_trace(go.Scatter(x=date, y=[152.55,148.76,151.38,142.25,125.04,140.24,208.57,218.79,249.48,292.75,272.23,164.89,156.62,165.56,200.03,191.11,196.01,197.88,205.01,176.34,209.12,220.97,291.94,259.85,251.68,239.52,173.75,206.11,216.32,199.14]
                                ,mode='lines+markers',
                                 name='AVG ENG Time',line_color="#1a8cff",line_width=1.5,marker_size=4,
                                 hovertemplate='%{y}'
                                           ))
        
            
            
    home22.update_layout(showlegend=True)
    home22.update_layout(autosize=False,paper_bgcolor="#FFFFFF",
                              plot_bgcolor="#FFFFFF",width=800, height=400, margin=dict(l=20, r=20, b=20, t=70),
                                xaxis=dict(mirror=True,showline=True, linewidth=1, linecolor='#afb9cf', gridcolor='#dfe3ec'),
                                yaxis=dict(mirror=True,showline=True, linewidth=1, linecolor='#afb9cf', gridcolor='#dfe3ec')
                             ,hovermode="x unified",
                              title={
                                    
                                    'y':0.99,
                                    'x':0.2,
                                    'xanchor': 'center',
                                    'yanchor': 'top'},
                                xaxis_title="Date",
                                yaxis_title="AVG Engagement Time"
                                ,legend=dict(
                                            orientation="h",
                                            yanchor="bottom",
                                            y=1.02,
                                            xanchor="right",
                                            x=1
                                          )) 
    
    home22.layout.xaxis.fixedrange = True
    home22.layout.yaxis.fixedrange = True
    
    home_page = [home1,home2,home3,home33,home4,home5,home6,home7,home8,home9,home10,home11,home12,home13,home14,home15,home16,home17,home18,home19,home20,home21,home22]
    return home_page

def firebase_page():
    
    labels=['New Users']
    values = [50]
    color2 =['#4D96FF']
    fire1 = go.Figure()
    fire1.add_trace(go.Indicator(
        mode = "number+delta",
        value = 10450,
        number = {"font": {"size": 35,'color': "#31333F"}},
        delta = {"reference": 10800, 'relative': True, "valueformat": ".0%"},
        title = {"text": "New Users","font": {"size": 25, 'color': "#31333F"}}
        ,domain = {'y': [0.3, 0.5], 'x': [0.5, 0.5]}
    ))
    fire1.add_trace(go.Pie(labels=labels, values=values, hole=.9,hoverinfo='skip', textinfo='none'
                         ,showlegend=False,marker=dict(colors=color2)))
    fire1.update_layout(autosize=False,paper_bgcolor="#FFFFFF", plot_bgcolor="#FFFFFF",
                       width=680, height=250, margin=dict(l=20, r=20, b=20, t=30),
                      xaxis=dict(showgrid=False,showline=False,showticklabels=False,zerolinecolor='#F0F2F6'),
                  yaxis=dict(showgrid=False,showline=False,showticklabels=False,zerolinecolor='#F0F2F6'))

    ###########################################################################
    fire2 = go.Figure(data=go.Scatter(x=date, y=[468,520,439,470,502,458,548,576,585,566,552,503,445,451,424,462,422,469,434,419,373,396,348,348,362,405,380,385,354,365],mode='lines+markers',
                               name='New Users',line_color="#4D96FF",line_width=1.5,marker_size=4,
                                hovertemplate='%{y}'
                                   ))
    
    fire2.update_layout(showlegend=True)
    fire2.update_layout(autosize=False,paper_bgcolor="#FFFFFF",
                          plot_bgcolor="#FFFFFF",width=600, height=220, margin=dict(l=20, r=20, b=20, t=30),
                            xaxis=dict(mirror=True,showline=True, linewidth=1, linecolor='#afb9cf', gridcolor='#dfe3ec'),
                            yaxis=dict(mirror=True,showline=True, linewidth=1, linecolor='#afb9cf', gridcolor='#dfe3ec')
                         ,hovermode="x unified"
                            ,legend=dict(
                                        orientation="h",
                                        yanchor="bottom",
                                        y=1.02,
                                        xanchor="right",
                                        x=1
                                      ) 
                             )   
    
    fire2.layout.xaxis.fixedrange = True
    fire2.layout.yaxis.fixedrange = True
    ###########################################################################
    labels=['Active Users']
    values = [50]
    color2 =['#4FBDBA']
    fire3 = go.Figure()
    fire3.add_trace(go.Indicator(
        mode = "number+delta",
        value = 5400,
        number = {"font": {"size": 35,'color': "#31333F"}},
        delta = {"reference": 3500, 'relative': True, "valueformat": ".0%"},
        title = {"text": "Active Users","font": {"size": 25, 'color': "#31333F"}}
        ,domain = {'y': [0.3, 0.5], 'x': [0.5, 0.5]}
    ))
    fire3.add_trace(go.Pie(labels=labels, values=values, hole=.9,hoverinfo='skip', textinfo='none'
                         ,showlegend=False,marker=dict(colors=color2)))
    fire3.update_layout(autosize=False,paper_bgcolor="#FFFFFF", plot_bgcolor="#FFFFFF",
                       width=680, height=250, margin=dict(l=20, r=20, b=20, t=30),
                      xaxis=dict(showgrid=False,showline=False,showticklabels=False,zerolinecolor='#F0F2F6'),
                  yaxis=dict(showgrid=False,showline=False,showticklabels=False,zerolinecolor='#F0F2F6'))
    
    fire4 = go.Figure(data=go.Scatter(x=date, y=[4372,4724,4339,4230,4392,4164,4778,4910,5002,4816,4796,4370,4330,4275,4476,4414,4265,4469,4548,4149,4026,4362,4392,4058,4363,4663,4057,4177,4006,4296]
                                      ,mode='lines+markers',
                               name='Active Users',line_color="#4FBDBA",line_width=1.5,marker_size=4,
                                hovertemplate='%{y}'
                                   ))
    
    fire4.update_layout(showlegend=True)
    fire4.update_layout(autosize=False,paper_bgcolor="#FFFFFF",
                          plot_bgcolor="#FFFFFF",width=680, height=220, margin=dict(l=20, r=20, b=20, t=30),
                            xaxis=dict(mirror=True,showline=True, linewidth=1, linecolor='#afb9cf', gridcolor='#dfe3ec'),
                            yaxis=dict(mirror=True,showline=True, linewidth=1, linecolor='#afb9cf', gridcolor='#dfe3ec')
                         ,hovermode="x unified"
                         ,legend=dict(
                                     orientation="h",
                                     yanchor="bottom",
                                     y=1.02,
                                     xanchor="right",
                                     x=1
                                   )
                             ) 
    
    fire4.layout.xaxis.fixedrange = True
    fire4.layout.yaxis.fixedrange = True
    ###########################################################################
    fire5 = go.Figure()

    fire5.add_trace(go.Indicator(
                title = {'text': "<b>Day 1</b><br><span style='color: #31333F; font-size:0.8em'>AVG</span>"
                         ,"font": {"size": 20, 'color': "#31333F"}},
                mode = "number",
                value = 21.5,
                number={'suffix': "%","font": {"size": 30, 'color': "#3282B8"}},
                ))
    
    fire5.update_layout(width=600,height = 120 , margin = {'t':70, 'b':0, 'l':50,'r':50},paper_bgcolor = "#ffffff")
    fire5.update_traces(delta_decreasing_color="#FF4B4B",
                                         delta_increasing_color="#0a7559",
                                         #delta_valueformat='.3f',
                                         selector=dict(type='indicator'))
    ###########################################################################
    fire6 = go.Figure()
            
    fire6.add_trace(go.Indicator(
                title = {'text': "<b>Day 7</b><br><span style='color: #31333F; font-size:0.8em'>AVG</span>"
                         ,"font": {"size": 20, 'color': "#31333F"}},
                mode = "number",
                value = 4.5,
                number={'suffix': "%","font": {"size": 30, 'color': "#0F4C75"}},
                ))
    
    fire6.update_layout(width=600,height = 120 , margin = {'t':70, 'b':0, 'l':50,'r':50},paper_bgcolor = "#ffffff")
    fire6.update_traces(delta_decreasing_color="#FF4B4B",
                                         delta_increasing_color="#0a7559",
                                         #delta_valueformat='.3f',
                                         selector=dict(type='indicator'))
    ###########################################################################
    fire7 = go.Figure()
            
    fire7.add_trace(go.Indicator(
                title = {'text': "<b>Day 30</b><br><span style='color: #31333F; font-size:0.8em'>AVG</span>"
                         ,"font": {"size": 20, 'color': "#31333F"}},
                mode = "number",
                value =2.5,
                number={'suffix': "%","font": {"size": 30, 'color': "#1B262C"}},
                ))
    
    
    fire7.update_layout(width=600,height = 120 , margin = {'t':70, 'b':0, 'l':50,'r':50},paper_bgcolor = "#ffffff")
    fire7.update_traces(delta_decreasing_color="#FF4B4B",
                                         delta_increasing_color="#0a7559",
                                         #delta_valueformat='.3f',
                                         selector=dict(type='indicator'))
    ###########################################################################    
    
    fire8 = go.Figure()

    fire8.add_trace(go.Indicator(
                    title = {'text': "<b>Max Day 1</b>"
                             ,"font": {"size": 15, 'color': "#31333F"}},
                    mode = "number",
                    value = 26.1,
                    number={'suffix': "%","font": {"size": 20, 'color': "#3282B8"}},
                    domain = {'row': 0, 'column': 0}))
                
    fire8.add_trace(go.Indicator(
                    title = {'text': "<b>Min Day 1</b>"
                             ,"font": {"size": 15, 'color': "#31333F"}},
                    mode = "number",
                    value = 15.1,
                    number={'suffix': "%","font": {"size": 20, 'color': "#3282B8"}},
                    domain = {'row': 0, 'column': 1}))
    fire8.update_layout(
                    grid = {'rows': 1, 'columns': 2, 'pattern': "independent"})
                
                
    fire8.update_layout(width=1400,height = 120 , margin = {'t':70, 'b':0, 'l':50,'r':50},paper_bgcolor = "#ffffff")
    fire8.update_traces(delta_decreasing_color="#FF4B4B",
                                             delta_increasing_color="#0a7559",
                                             selector=dict(type='indicator'))
    ###########################################################################
    fire9 = go.Figure()            
    fire9.add_trace(go.Indicator(
                    title = {'text': "<b>Max Day 7</b>"
                             ,"font": {"size": 15, 'color': "#31333F"}},
                    mode = "number",
                    value =5.6,
                    number={'suffix': "%","font": {"size": 20, 'color': "#0F4C75"}},
                    domain = {'row': 0, 'column': 0}))
    fire9.add_trace(go.Indicator(
                    title = {'text': "<b>Min Day 7</b>"
                             ,"font": {"size": 15, 'color': "#31333F"}},
                    mode = "number",
                    value = 3.2,
                    number={'suffix': "%","font": {"size": 20, 'color': "#0F4C75"}},
                    domain = {'row': 0, 'column': 1}))
    fire9.update_layout(
                    grid = {'rows': 1, 'columns': 2, 'pattern': "independent"})
                
                
    fire9.update_layout(width=1400,height = 120 , margin = {'t':70, 'b':0, 'l':50,'r':50},paper_bgcolor = "#ffffff")
    fire9.update_traces(delta_decreasing_color="#FF4B4B",
                                             delta_increasing_color="#0a7559",
                                             selector=dict(type='indicator'))
    ###########################################################################
    fire10 = go.Figure()
    fire10.add_trace(go.Indicator(
                    title = {'text': "<b>Max Day 30</b>"
                             ,"font": {"size": 15, 'color': "#31333F"}},
                    mode = "number",
                    value = 3.0,
                    number={'suffix': "%","font": {"size": 20, 'color': "#1B262C"}},
                    domain = {'row': 0, 'column': 0}))
                
    fire10.add_trace(go.Indicator(
                    title = {'text': "<b>Min Day 30</b>"
                             ,"font": {"size": 15, 'color': "#31333F"}},
                    mode = "number",
                    value =1.1,
                    number={'suffix': "%","font": {"size": 20, 'color': "#1B262C"}},
                    domain = {'row': 0, 'column': 1}))
            
                
    fire10.update_layout(
                    grid = {'rows': 1, 'columns': 2, 'pattern': "independent"})
                
                
    fire10.update_layout(width=1400,height = 120 , margin = {'t':70, 'b':0, 'l':50,'r':50},paper_bgcolor = "#ffffff")
    fire10.update_traces(delta_decreasing_color="#FF4B4B",
                                             delta_increasing_color="#0a7559",
                                             selector=dict(type='indicator'))
    
    ###########################################################################
    
    
    
    fire11 = go.Figure()

    fire11.add_trace(go.Scatter(x=date, 
                            y=[4.2700000000000005,5.34,2.0500000000000003,3.83,3.5900000000000003,4.590000000000001,18.279999999999998,17.69,17.349999999999998,18.990000000000002,11.03,4.78,4.49,7.08,8.92,5.4,7.090000000000001,7.01,7.870000000000001,6.94,6.7,6.3100000000000005,8.219999999999999,6.92,6.890000000000001,6.47,4.74,5.970000000000001,6.18,7.16],
                            mode='lines+markers',hovertemplate='%{y:.2f}%',
                            name='1 Day',line_color="#1B262C",line_width=1.5,marker_size=4
                                ))
    fire11.add_trace(go.Scatter(x=date, 
                            y=[2.56,3.05,1.59,1.28,2.59,1.31,4.66,3.91,5.609999999999999,3.4799999999999995,3.8,2.79,2.25,3.1,4.93,2.16,2.8400000000000003,4.25,3.6999999999999997,3.11,4.5600000000000005,2.02,3.6799999999999997,2.31,1.9300000000000002,2.74,1.8399999999999999,2.6,1.4000000000000001,3.0300000000000002],
                            mode='lines+markers',hovertemplate='%{y:.2f}%',
                            name='7 Day',line_color="#0F4C75",line_width=1.5,marker_size=4
                                ))
    fire11.add_trace(go.Scatter(x=date, 
                            y=[1.92,1.72,0.91,2.13,1.7999999999999998,1.7500000000000002,4.66,2.21,1.87,1.39,1.27,1,1.5699999999999998,1.55,3.52,2.81,2.13,1.49,1.6199999999999999,2.15,1.34,2.27,2.27,0.86,1.9300000000000002,2.4899999999999998,0.53,2.34,0.84,1.9300000000000002],
                            mode='lines+markers',hovertemplate='%{y:.2f}%',
                            name='30 Day',line_color="#3282B8",line_width=1.5,marker_size=4
                                ))
    fire11.update_layout(autosize=False,paper_bgcolor="#FFFFFF", plot_bgcolor="#FFFFFF",hovermode="x unified"
                          ,width=600, height=400, margin=dict(l=20, r=20, b=20, t=30),
                         xaxis=dict(mirror=True,showgrid=True,showline=True, linewidth=1, linecolor='#afb9cf', gridcolor='#dfe3ec'),
                          yaxis=dict(mirror=True,showgrid=True,showline=True, linewidth=1, linecolor='#afb9cf', gridcolor='#dfe3ec'),
                        legend=dict(
                                    orientation="h",
                                    yanchor="bottom",
                                    y=1.02,
                                    xanchor="right",
                                    x=1
                                  ),
                                xaxis_title="Date",
                                yaxis_title="Percentage",)
                
    fire11.layout.xaxis.fixedrange = True
    fire11.layout.yaxis.fixedrange = True            
    
   
    ###########################################################################
    fire12 = make_subplots(rows=3, cols=3,
                    specs=[[None, {'type': 'indicator'},None],   # first row
                           [{'rowspan': 2,"colspan": 3},  None,     None  ],   # second row
                           [None ,  None,      None  ]])  # third row
    fire12.add_trace(go.Indicator(
            mode = "number",
            value = 7.2,
           title = {'text': "<b>AVG</b><br><span style='color: #31333F; font-size:0.8em'>DAU/MAU</span>"
                    ,"font": {"size": 20, 'color': "#31333F"}},
            number = {'suffix': "%","font": {"size": 30,'color': "#31333F"}},
            domain = {'x': [0.5, 0.5], 'y': [0.5, 1]}
        ), row=1, col=2)
    
    fire12.add_trace(go.Scatter(x=date, 
                                y=[4372,4724,4339,4230,4392,4164,4778,4910,5002,4816,4796,4370,4330,4275,4476,4414,4265,4469,4548,4149,4026,4362,4392,4058,4363,4663,4057,4177,4006,4296]
                                ,mode='lines+markers',
                                name='AVG DAU',line_color="#0F4C75",line_width=1.5,marker_size=4,
                                hovertemplate='%{y}'
                                       ))
    
        
        
    fire12.update_layout(showlegend=True)
    fire12.update_layout(autosize=False,paper_bgcolor="#FFFFFF",
                          plot_bgcolor="#FFFFFF",width=600, height=400, margin=dict(l=20, r=20, b=20, t=70),
                            xaxis=dict(mirror=True,showline=True, linewidth=1, linecolor='#afb9cf', gridcolor='#dfe3ec'),
                            yaxis=dict(mirror=True,showline=True, linewidth=1, linecolor='#afb9cf', gridcolor='#dfe3ec')
                         ,hovermode="x unified",
                          title={
                                
                                'y':0.99,
                                'x':0.2,
                                'xanchor': 'center',
                                'yanchor': 'top'},
                            xaxis_title="Date",
                            yaxis_title="Number of Users"
                            ,legend=dict(
                                        orientation="h",
                                        yanchor="bottom",
                                        y=1.02,
                                        xanchor="right",
                                        x=1
                                      )
                             )

    fire12.layout.xaxis.fixedrange = True
    fire12.layout.yaxis.fixedrange = True
    
    ###########################################################################
    fire13 = go.Figure()
            
    fire13.add_trace(go.Indicator(
                title = {'text': "Max Engagement Time"
                         ,"font": {"size": 20, 'color': "#31333F"}},
                mode = "number",
                value =20.2,
                number = {'suffix': " min","font": {"size": 30,'color': "#31333F"}},
                ))
    
    
    fire13.update_layout(width=600,height = 120 , margin = {'t':70, 'b':0, 'l':50,'r':50},paper_bgcolor = "#ffffff")
    fire13.update_traces(delta_decreasing_color="#FF4B4B",
                                         delta_increasing_color="#0a7559",
                                         selector=dict(type='indicator'))
    ###########################################################################
    fire14 = go.Figure()
            
    fire14.add_trace(go.Indicator(
                title = {'text': "AVG Engagement Time"
                         ,"font": {"size": 20, 'color': "#31333F"}},
                mode = "number",
                value =11.45,
                number = {'suffix': " min","font": {"size": 30,'color': "#31333F"}},
                ))
    
    
    fire14.update_layout(width=600,height = 120 , margin = {'t':70, 'b':0, 'l':50,'r':50},paper_bgcolor = "#ffffff")
    fire14.update_traces(delta_decreasing_color="#FF4B4B",
                                         delta_increasing_color="#0a7559",
                                         selector=dict(type='indicator'))
    
    ###########################################################################
    fire15 = go.Figure()
        
    fire15.add_trace(go.Scatter(x=date, 
                                y=[152.55,148.76,151.38,142.25,125.04,140.24,208.57,218.79,249.48,292.75,272.23,164.89,156.62,165.56,200.03,191.11,196.01,197.88,205.01,176.34,209.12,220.97,291.94,259.85,251.68,239.52,173.75,206.11,216.32,199.14]
                                ,mode='lines+markers',
                                       name='AVG ENG Time',line_color="#1a8cff",line_width=1.5,marker_size=4,
                                        hovertemplate='%{y}'
                                           ))
        
            
            
    fire15.update_layout(showlegend=True)
    fire15.update_layout(autosize=False,paper_bgcolor="#FFFFFF",
                              plot_bgcolor="#FFFFFF",width=800, height=400, margin=dict(l=20, r=20, b=20, t=70),
                                xaxis=dict(mirror=True,showline=True, linewidth=1, linecolor='#afb9cf', gridcolor='#dfe3ec'),
                                yaxis=dict(mirror=True,showline=True, linewidth=1, linecolor='#afb9cf', gridcolor='#dfe3ec')
                             ,hovermode="x unified",
                              title={
                                    
                                    'y':0.99,
                                    'x':0.2,
                                    'xanchor': 'center',
                                    'yanchor': 'top'},
                                xaxis_title="Date",
                                yaxis_title="AVG Engagement Time"
                                ,legend=dict(
                                            orientation="h",
                                            yanchor="bottom",
                                            y=1.02,
                                            xanchor="right",
                                            x=1
                                          )) 
    
    fire15.layout.xaxis.fixedrange = True
    fire15.layout.yaxis.fixedrange = True

    firebase = [fire1,fire2,fire3,fire4,fire5,fire6,fire7,fire8,fire9,fire10,fire11,fire12,fire13,fire14,fire15]
    return firebase

def adjust_page():
    
    adjust1 = make_subplots(rows=1, cols=1, specs=[[{'type':'domain'}]])
    
    adjust1.add_trace(go.Indicator(
        mode = "number+delta",
        value = 10320,
        number = {"font": {"size": 25,'color': "#31333F"}},
        delta = {"reference": 10500, 'relative': True, "valueformat": ".0%"},
        title = {"text": "Install", 'font': {'size': 20}}
        ,domain = {'y': [0.3, 0.5], 'x': [0.5, 0.5]}
    ))
    
    adjust1.add_trace(go.Pie(labels=['Active Users'], values=[50], hole=.9,hoverinfo='skip', textinfo='none'
                         ,showlegend=False,marker=dict(colors=['#1CC14B'])), row=1, col=1)
    
    adjust1.update_layout(autosize=False,paper_bgcolor="#FFFFFF", plot_bgcolor="#FFFFFF",
                       width=700, height=250, margin=dict(l=20, r=20, b=20, t=20),
                      xaxis=dict(showgrid=False,showline=False,showticklabels=False,zerolinecolor='#F0F2F6'),
                  yaxis=dict(showgrid=False,showline=False,showticklabels=False,zerolinecolor='#F0F2F6'),
                     title={
                        'xanchor': 'center',    
                        'yanchor': 'top'}, 
                        font=dict(family="Arial",size=18, color='#31333F'))
    ###########################################################################
    adjust2 = make_subplots(rows=1, cols=1, specs=[[{'type':'domain'}]])
    
    adjust2.add_trace(go.Indicator(
        mode = "number+delta",
        value = 5590,
        number = {"font": {"size": 25,'color': "#31333F"}},
        delta = {"reference": 6000, 'relative': True, "valueformat": ".0%"},
        title = {'text': "Registration", 'font': {'size': 20}}
        ,domain = {'y': [0.3, 0.5], 'x': [0.5, 0.5]}
    ))
    
    adjust2.add_trace(go.Pie(labels=['Active Users'], values=[50], hole=.9,hoverinfo='skip', textinfo='none'
                         ,showlegend=False,marker=dict(colors=['#2BC4E0'])), row=1, col=1)
    
    adjust2.update_layout(autosize=False,paper_bgcolor="#FFFFFF", plot_bgcolor="#FFFFFF",
                       width=700, height=250, margin=dict(l=20, r=20, b=20, t=20),
                      xaxis=dict(showgrid=False,showline=False,showticklabels=False,zerolinecolor='#F0F2F6'),
                  yaxis=dict(showgrid=False,showline=False,showticklabels=False,zerolinecolor='#F0F2F6'),
                     title={
                        'xanchor': 'center',    
                        'yanchor': 'top'}, 
                        font=dict(family="Arial",size=18, color='#31333F'))
    ###########################################################################
    adjust3 = make_subplots(rows=1, cols=1, specs=[[{'type':'domain'}]])
    
    adjust3.add_trace(go.Indicator(
        mode = "number+delta",
        value = 5300,
        number = {"font": {"size": 25,'color': "#31333F"}},
        delta = {"reference": 3500, 'relative': True, "valueformat": ".0%"},
        title = {'text': "AVG DAU", 'font': {'size': 20}}
        ,domain = {'y': [0.3, 0.5], 'x': [0.5, 0.5]}
    ))
    
    adjust3.add_trace(go.Pie(labels=['Active Users'], values=[50], hole=.9,hoverinfo='skip', textinfo='none'
                         ,showlegend=False,marker=dict(colors=['#3B3EF7'])), row=1, col=1)
    
    adjust3.update_layout(autosize=False,paper_bgcolor="#FFFFFF", plot_bgcolor="#FFFFFF",
                       width=700, height=250, margin=dict(l=20, r=20, b=20, t=20),
                      xaxis=dict(showgrid=False,showline=False,showticklabels=False,zerolinecolor='#F0F2F6'),
                  yaxis=dict(showgrid=False,showline=False,showticklabels=False,zerolinecolor='#F0F2F6'),
                     title={
                        'xanchor': 'center',    
                        'yanchor': 'top'}, 
                        font=dict(family="Arial",size=18, color='#31333F'))
    ###########################################################################
    
    adjust4 = go.Figure()
    
    adjust4.add_trace(go.Scatter(x=date,
                        y=[452,489,419,447,485,433,482,527,527,515,515,472,411,455,426,437,399,438,435,407,367,362,339,358,351,397,367,373,335,357],
                        mode='lines+markers',
                        name='Installs',line_color="#1CC14B",line_width=1.5,marker_size=4))
    
    adjust4.add_trace(go.Scatter(x=date, 
                        y=[110,99,83,94,118,96,249,422,428,406,274,257,121,278,113,178,87,212,183,82,259,204,333,182,179,177,82,87,97,98],
                        mode='lines+markers',
                        name='Registration',line_color="#2BC4E0",line_width=1.5,marker_size=4))
    
    adjust4.add_trace(go.Scatter(x=date, 
                        y=[3680,3963,3652,3613,3617,3487,4037,4264,4326,4143,4130,3661,3594,3739,3886,3811,3644,3872,3838,3495,3413,3740,3708,3506,3726,3993,3395,3590,3429,3704],
                        mode='lines+markers',
                        name='Daily Active Users',line_color="#3B3EF7",line_width=1.5,marker_size=4))
    
    adjust4.update_layout(autosize=False,paper_bgcolor="#FFFFFF", plot_bgcolor="#FFFFFF",hovermode="x unified"
                      ,width=600, height=400, margin=dict(l=20, r=20, b=20, t=30),
                      xaxis=dict(mirror=True,showline=True, linewidth=1, linecolor='#afb9cf', gridcolor='#dfe3ec'),
                      yaxis=dict(mirror=True,showline=True, linewidth=1, linecolor='#afb9cf', gridcolor='#dfe3ec'),
                     title={
                                'y':0.95,
                                'x':0.5,
                                'xanchor': 'center',
                                'yanchor': 'top'},
                            xaxis_title="Date",
                            yaxis_title="Number of Users"
                            ,legend=dict(
                                        orientation="h",
                                        yanchor="bottom",
                                        y=1.02,
                                        xanchor="right",
                                        x=1
                                      ))
    
    adjust4.layout.xaxis.fixedrange = True
    adjust4.layout.yaxis.fixedrange = True
    ###########################################################################
    adjust5 = go.Figure()

    adjust5.add_trace(go.Indicator(
        title = {'text': "<b>Installs</b><br><span style='color: #31333F; font-size:0.8em'>NO. User</span>"
                 ,"font": {"size": 15, 'color': "#31333F"}},
        mode = "number+delta",
        value = 10320,
        number={"font": {"size": 30, 'color': "#31333F"}},
        delta = {'reference': 10500, 'relative': True, "valueformat": ".0%"},
        domain = {'row': 0, 'column': 0}))
    
    adjust5.add_trace(go.Indicator(
        title = {'text': "<b>Uninstalls</b><br><span style='color: #31333F; font-size:0.8em'>NO. User</span>"
                 ,"font": {"size": 15, 'color': "#31333F"}},
        mode = "number+delta",
        value = 7650,
        number={"font": {"size": 30, 'color': "#31333F"}},
        delta = {'reference': 6200, 'relative': True, "valueformat": ".0%"},
        domain = {'row': 0, 'column': 1}))
    
    
    adjust5.add_trace(go.Indicator(
        title = {'text': "<b>Reinstalls</b><br><span style='color: #31333F; font-size:0.8em'>NO. User</span>"
                 ,"font": {"size": 15, 'color': "#31333F"}},
        mode = "number+delta",
        value = 1600,
        number={"font": {"size": 30, 'color': "#31333F"}},
        delta = {'reference': 1200, 'relative': True, "valueformat": ".0%"},
        domain = {'row': 0, 'column': 2}))
    
    
    adjust5.update_layout(
        grid = {'rows': 1, 'columns': 3, 'pattern': "independent"})
    
    
    adjust5.update_layout(width=600,height = 189 , margin = {'t':35, 'b':0, 'l':50,'r':50},paper_bgcolor = "#FFFFFF")
    adjust5.update_traces(delta_decreasing_color="#FF4B4B",
                                 delta_increasing_color="#0a7559",
                                 selector=dict(type='indicator'))
    
    ###########################################################################
    
    adjust6 = go.Figure()
    adjust6.add_trace(go.Scatter(x=date, 
                        y=[452,489,419,447,485,433,482,527,527,515,515,472,411,455,426,437,399,438,435,407,367,362,339,358,351,397,367,373,335,357],
                        mode='lines+markers',
                        name='Installs',line_color="#FF6B6B"))
    adjust6.add_trace(go.Scatter(x=date, 
                        y=[205,372,294,241,257,267,343,360,422,359,358,329,329,299,309,308,292,338,305,273,199,299,284,237,272,349,227,285,250,261],
                        mode='lines+markers',
                        name='Uninstalls',line_color="#FFD93D"))
    adjust6.add_trace(go.Scatter(x=date, 
                        y=[43,56,45,32,40,48,95,118,112,111,110,66,66,61,80,86,62,74,80,52,58,69,83,51,72,96,46,66,49,68],
                        mode='lines+markers',
                        name='Reinstalls',line_color="#6BCB77"))
    adjust6.update_layout(autosize=False,paper_bgcolor="#FFFFFF", plot_bgcolor="#FFFFFF",hovermode="x unified"
                      ,width=600, height=350, margin=dict(l=20, r=20, b=20, t=70),
                     title={
                            'y':0.98,
                            'x':0.4,
                            'xanchor': 'center',
                            'yanchor': 'top'},
                        xaxis_title="Date",
                        yaxis_title="Number of Users"
                        ,legend=dict(
                                    orientation="h",
                                    yanchor="bottom",
                                    y=1.02,
                                    xanchor="right",
                                    x=1
                                  ) )
    adjust6.update_xaxes(mirror=True,showgrid=True,showline=True, linewidth=1, linecolor='#afb9cf', gridcolor='#dfe3ec')
    adjust6.update_yaxes(mirror=True,showgrid=True,showline=True, linewidth=1, linecolor='#afb9cf', gridcolor='#dfe3ec')
    
    adjust6.layout.xaxis.fixedrange = True
    adjust6.layout.yaxis.fixedrange = True
    
    ###########################################################################
    adjust7 = go.Figure()

    adjust7.add_trace(go.Indicator(
            title = {'text': "<b>Day 1</b><br><span style='color: #31333F; font-size:0.8em'>AVG</span>"
                     ,"font": {"size": 20, 'color': "#31333F"}},
            mode = "number",
            value = 22.2,
            number={'suffix': "%","font": {"size": 30, 'color': "#31333F"}},
            ))
    
    adjust7.update_layout(width=1300,height = 120 , margin = {'t':70, 'b':0, 'l':50,'r':50},paper_bgcolor = "#FFFFFF")
    adjust7.update_traces(delta_decreasing_color="#FF4B4B",
                                     delta_increasing_color="#0a7559",
                                     selector=dict(type='indicator'))
    ###########################################################################
    adjust8 = go.Figure()
    
    
    adjust8.add_trace(go.Indicator(
            title = {'text': "<b>Day 7</b><br><span style='color: #31333F; font-size:0.8em'>AVG</span>"
                     ,"font": {"size": 20, 'color': "#31333F"}},
            mode = "number",
            value = 4.1,
            number={'suffix': "%","font": {"size": 30, 'color': "#31333F"}},
            ))
    
    adjust8.update_layout(width=1300,height = 120 , margin = {'t':70, 'b':0, 'l':50,'r':50},paper_bgcolor = "#FFFFFF")
    adjust8.update_traces(delta_decreasing_color="#FF4B4B",
                                     delta_increasing_color="#0a7559",
                                     selector=dict(type='indicator'))
    ###########################################################################
    adjust9 = go.Figure()
    
    
    adjust9.add_trace(go.Indicator(
            title = {'text': "<b>Day 30</b><br><span style='color: #31333F; font-size:0.8em'>AVG</span>"
                     ,"font": {"size": 20, 'color': "#31333F"}},
            mode = "number",
            value = 2.1,
            number={'suffix': "%","font": {"size": 30, 'color': "#31333F"}},
            ))
    
    adjust9.update_layout(width=1300,height = 120 , margin = {'t':70, 'b':0, 'l':50,'r':50},paper_bgcolor = "#FFFFFF")
    adjust9.update_traces(delta_decreasing_color="#FF4B4B",
                                     delta_increasing_color="#0a7559",
                                     selector=dict(type='indicator'))
    ###########################################################################
    
    
    
    
    adjust10 = go.Figure()

    adjust10.add_trace(go.Indicator(
                    title = {'text': "<b>Max Day 1</b>"
                             ,"font": {"size": 15, 'color': "#31333F"}},
                    mode = "number",
                    value = 25.2,
                    number={'suffix': "%","font": {"size": 20, 'color': "#3282B8"}},
                    domain = {'row': 0, 'column': 0}))
                
    adjust10.add_trace(go.Indicator(
                    title = {'text': "<b>Min Day 1</b>"
                             ,"font": {"size": 15, 'color': "#31333F"}},
                    mode = "number",
                    value = 10.2,
                    number={'suffix': "%","font": {"size": 20, 'color': "#3282B8"}},
                    domain = {'row': 0, 'column': 1}))
    adjust10.update_layout(
                    grid = {'rows': 1, 'columns': 2, 'pattern': "independent"})
                
                
    adjust10.update_layout(width=1400,height = 120 , margin = {'t':70, 'b':0, 'l':50,'r':50},paper_bgcolor = "#FFFFFF")
    adjust10.update_traces(delta_decreasing_color="#FF4B4B",
                                             delta_increasing_color="#0a7559",
                                             selector=dict(type='indicator'))
    ###########################################################################
    adjust11 = go.Figure()            
    adjust11.add_trace(go.Indicator(
                    title = {'text': "<b>Max Day 7</b>"
                             ,"font": {"size": 15, 'color': "#31333F"}},
                    mode = "number",
                    value =5.6,
                    number={'suffix': "%","font": {"size": 20, 'color': "#0F4C75"}},
                    domain = {'row': 0, 'column': 0}))
    adjust11.add_trace(go.Indicator(
                    title = {'text': "<b>Min Day 7</b>"
                             ,"font": {"size": 15, 'color': "#31333F"}},
                    mode = "number",
                    value = 3.0,
                    number={'suffix': "%","font": {"size": 20, 'color': "#0F4C75"}},
                    domain = {'row': 0, 'column': 1}))
    adjust11.update_layout(
                    grid = {'rows': 1, 'columns': 2, 'pattern': "independent"})
                
                
    adjust11.update_layout(width=1400,height = 120 , margin = {'t':70, 'b':0, 'l':50,'r':50},paper_bgcolor = "#FFFFFF")
    adjust11.update_traces(delta_decreasing_color="#FF4B4B",
                                             delta_increasing_color="#0a7559",
                                             selector=dict(type='indicator'))
    ###########################################################################
    adjust12 = go.Figure()
    adjust12.add_trace(go.Indicator(
                    title = {'text': "<b>Max Day 30</b>"
                             ,"font": {"size": 15, 'color': "#31333F"}},
                    mode = "number",
                    value = 2.6,
                    number={'suffix': "%","font": {"size": 20, 'color': "#1B262C"}},
                    domain = {'row': 0, 'column': 0}))
                
    adjust12.add_trace(go.Indicator(
                    title = {'text': "<b>Min Day 30</b>"
                             ,"font": {"size": 15, 'color': "#31333F"}},
                    mode = "number",
                    value =1.6,
                    number={'suffix': "%","font": {"size": 20, 'color': "#1B262C"}},
                    domain = {'row': 0, 'column': 1}))
            
                
    adjust12.update_layout(
                    grid = {'rows': 1, 'columns': 2, 'pattern': "independent"})
                
                
    adjust12.update_layout(width=1400,height = 120 , margin = {'t':70, 'b':0, 'l':50,'r':50},paper_bgcolor = "#FFFFFF")
    adjust12.update_traces(delta_decreasing_color="#FF4B4B",
                                             delta_increasing_color="#0a7559",
                                             selector=dict(type='indicator'))
    ###########################################################################
    
    
    adjust13 = go.Figure()

    adjust13.add_trace(go.Scatter(x=date, 
                        y=[4.2700000000000005,5.34,2.0500000000000003,3.83,3.5900000000000003,4.590000000000001,18.279999999999998,17.69,17.349999999999998,18.990000000000002,11.03,4.78,4.49,7.08,8.92,5.4,7.090000000000001,7.01,7.870000000000001,6.94,6.7,6.3100000000000005,8.219999999999999,6.92,6.890000000000001,6.47,4.74,5.970000000000001,6.18,7.16],
                        mode='lines+markers',hovertemplate='%{y:.2f}%',
                        name='1 Day',line_color="#191A19",line_width=1.5,marker_size=4
                            ))
    adjust13.add_trace(go.Scatter(x=date, 
                        y=[2.56,3.05,1.59,1.28,2.59,1.31,4.66,3.91,5.609999999999999,3.4799999999999995,3.8,2.79,2.25,3.1,4.93,2.16,2.8400000000000003,4.25,3.6999999999999997,3.11,4.5600000000000005,2.02,3.6799999999999997,2.31,1.9300000000000002,2.74,1.8399999999999999,2.6,1.4000000000000001,3.0300000000000002],
                        mode='lines+markers',hovertemplate='%{y:.2f}%',
                        name='7 Day',line_color="#297037",line_width=1.5,marker_size=4
                            ))
    adjust13.add_trace(go.Scatter(x=date, 
                        y=[1.92,1.72,0.91,2.13,1.7999999999999998,1.7500000000000002,4.66,2.21,1.87,1.39,1.27,1,1.5699999999999998,1.55,3.52,2.81,2.13,1.49,1.6199999999999999,2.15,1.34,2.27,2.27,0.86,1.9300000000000002,2.4899999999999998,0.53,2.34,0.84,1.9300000000000002],
                        mode='lines+markers',hovertemplate='%{y:.2f}%',
                        name='30 Day',line_color="#7ac76b",line_width=1.5,marker_size=4
                            ))
    adjust13.update_layout(hovermode="x unified")
    adjust13.update_layout(autosize=False,paper_bgcolor="#FFFFFF", plot_bgcolor="#FFFFFF"
                      ,width=1300, height=400, margin=dict(l=20, r=20, b=20, t=30),
                     xaxis=dict(mirror=True,showgrid=True,showline=True, linewidth=1, linecolor='#afb9cf', gridcolor='#dfe3ec'),
                      yaxis=dict(mirror=True,showgrid=True,showline=True, linewidth=1, linecolor='#afb9cf', gridcolor='#dfe3ec'),
                      legend=dict(
                                  orientation="h",
                                  yanchor="bottom",
                                  y=1.02,
                                  xanchor="right",
                                  x=1
                                ),title={
                                'text': "Retention Rate",
                                'y':0.97,
                                'x':0.5,
                                'xanchor': 'center',
                                'yanchor': 'top'},
                            xaxis_title="Date",
                            yaxis_title="Percentage",)
    adjust13.layout.xaxis.fixedrange = True
    adjust13.layout.yaxis.fixedrange = True       
    ###########################################################################
    adjust14 = make_subplots(rows=3, cols=3,
                    specs=[[None, {'type': 'indicator'},None],   # first row
                           [{'rowspan': 2,"colspan": 3},  None,     None  ],   # second row
                           [None ,  None,      None  ]])  # third row
    adjust14.add_trace(go.Indicator(
            mode = "number",
            value = 6.4,
           title = {'text': "<b>AVG</b><br><span style='color: #31333F; font-size:0.8em'>DAU/MAU</span>"
                    ,"font": {"size": 20, 'color': "#31333F"}},
            number = {'suffix': "%","font": {"size": 30,'color': "#31333F"}},
            domain = {'x': [0.5, 0.5], 'y': [0.5, 1]}
        ), row=1, col=2)
    
    adjust14.add_trace(go.Scatter(x=date, 
                                 y=[4372,4724,4339,4230,4392,4164,4778,4910,5002,4816,4796,4370,4330,4275,4476,4414,4265,4469,4548,4149,4026,4362,4392,4058,4363,4663,4057,4177,4006,4296]
                                 ,mode='lines+markers',
                                 name='AVG DAU',line_color="#0F4C75",line_width=1.5,marker_size=4,
                                 hovertemplate='%{y}'
                                       ))
    
        
        
    adjust14.update_layout(showlegend=True)
    adjust14.update_layout(autosize=False,paper_bgcolor="#FFFFFF",
                          plot_bgcolor="#FFFFFF",width=1300, height=450, margin=dict(l=20, r=20, b=20, t=70),
                            xaxis=dict(mirror=True,showline=True, linewidth=1, linecolor='#afb9cf', gridcolor='#dfe3ec'),
                            yaxis=dict(mirror=True,showline=True, linewidth=1, linecolor='#afb9cf', gridcolor='#dfe3ec')
                         ,hovermode="x unified",
                          title={
                                
                                'y':0.99,
                                'x':0.2,
                                'xanchor': 'center',
                                'yanchor': 'top'},
                            xaxis_title="Date",
                            yaxis_title="Number of Users"
                            ,legend=dict(
                                        orientation="h",
                                        yanchor="bottom",
                                        y=1.02,
                                        xanchor="right",
                                        x=1
                                      )) 
    adjust14.layout.xaxis.fixedrange = True
    adjust14.layout.yaxis.fixedrange = True
    
    adjust = [adjust1,adjust2,adjust3,adjust4,adjust5,adjust6,adjust7,adjust8,adjust9,adjust10,adjust11,adjust12,adjust13,adjust14]
    return adjust

def google_page():
    
    google1 = make_subplots(rows=1, cols=1, specs=[[{'type':'domain'}]])
    google1.add_trace(go.Indicator(
        mode = "number+delta",
        value = 6500,
        number = {"font": {"size": 25,'color': "#31333F"}},
        delta = {"reference": 6000, 'relative': True, "valueformat": ".0%"},
        title = {"text": "AVG DAU","font": {"size": 20, 'color': "#31333F"}}
        ,domain = {'y': [0.3, 0.5], 'x': [0.5, 0.5]}
    ))
    
    google1.add_trace(go.Pie(labels=['Active Users'], values=[50], hole=.9,hoverinfo='skip', textinfo='none'
                         ,showlegend=False,marker=dict(colors=['#FF4B4B'])), row=1, col=1)
    
    google1.update_layout(autosize=False,paper_bgcolor="#FFFFFF", plot_bgcolor="#FFFFFF",
                       width=700, height=250, margin=dict(l=20, r=20, b=20, t=20),
                      xaxis=dict(showgrid=False,showline=False,showticklabels=False,zerolinecolor='#F0F2F6'),
                  yaxis=dict(showgrid=False,showline=False,showticklabels=False,zerolinecolor='#F0F2F6'),
                     title={
                        'xanchor': 'center',    
                        'yanchor': 'top'}, 
                        font=dict(family="Arial",size=18, color='#31333F'))
    ###########################################################################
    google2 = make_subplots(rows=1, cols=1, specs=[[{'type':'domain'}]])
    
    google2.add_trace(go.Indicator(
        mode = "number+delta",
        value = 15000,
        number = {"font": {"size": 25,'color': "#31333F"}},
        delta = {"reference": 14000, 'relative': True, "valueformat": ".0%"},
        title = {"text": "New Users","font": {"size": 20, 'color': "#31333F"}}
        ,domain = {'y': [0.3, 0.5], 'x': [0.5, 0.5]}
    ))
    
    google2.add_trace(go.Pie(labels=['Active Users'], values=[50], hole=.9,hoverinfo='skip', textinfo='none'
                         ,showlegend=False,marker=dict(colors=['#966f03'])), row=1, col=1)
    
    google2.update_layout(autosize=False,paper_bgcolor="#FFFFFF", plot_bgcolor="#FFFFFF",
                       width=700, height=250, margin=dict(l=20, r=20, b=20, t=20),
                      xaxis=dict(showgrid=False,showline=False,showticklabels=False,zerolinecolor='#F0F2F6'),
                  yaxis=dict(showgrid=False,showline=False,showticklabels=False,zerolinecolor='#F0F2F6'),
                     title={
                        'xanchor': 'center',    
                        'yanchor': 'top'}, 
                        font=dict(family="Arial",size=18, color='#31333F'))
    ###########################################################################
    google3 = make_subplots(rows=1, cols=1, specs=[[{'type':'domain'}]])
    
    google3.add_trace(go.Indicator(
        mode = "number",
        value = 7,
        number = {'suffix': "%","font": {"size": 25,'color': "#31333F"}},
        title = {"text": "Stickness","font": {"size": 20, 'color': "#31333F"}}
        ,domain = {'y': [0.3, 0.52], 'x': [0.5, 0.5]}
    ))
    
    google3.add_trace(go.Pie(labels=['Active Users'], values=[50], hole=.9,hoverinfo='skip', textinfo='none'
                         ,showlegend=False,marker=dict(colors=['#FE6C35'])), row=1, col=1)
    
    google3.update_layout(autosize=False,paper_bgcolor="#FFFFFF", plot_bgcolor="#FFFFFF",
                       width=700, height=250, margin=dict(l=20, r=20, b=20, t=20),
                      xaxis=dict(showgrid=False,showline=False,showticklabels=False,zerolinecolor='#F0F2F6'),
                  yaxis=dict(showgrid=False,showline=False,showticklabels=False,zerolinecolor='#F0F2F6'),
                     title={
                        'xanchor': 'center',    
                        'yanchor': 'top'}, 
                        font=dict(family="Arial",size=18, color='#31333F'))
    ###########################################################################
    
    
    google4 = go.Figure(data=go.Scatter(x=date, 
                            y=[54,50,48,50,51,63,162,212,207,191,138,73,77,57,73,63,78,71,92,59,61,76,74,53,55,74,57,56,67,74]
                            ,mode='lines+markers',
                               name='New Users',line_color="#966f03",line_width=1.5,marker_size=4,
                                hovertemplate='%{y}'
                                   ))
    google4.add_trace(go.Scatter(x=date, 
                                 y=[5361,5799,5398,5311,5478,5256,5731,5914,5901,5701,5690,5300,5307,5271,5466,5428,5219,5610,5643,5117,4928,5242,5352,5110,5255,5566,4901,5194,5018,5285]
                                 ,mode='lines+markers',
                                  name='AVG DAU',line_color="#FF4B4B",line_width=1.5,marker_size=4,
                                    hovertemplate='%{y}'
                                       ))
        
        
    google4.update_layout(showlegend=True)
    google4.update_layout(autosize=False,paper_bgcolor="#FFFFFF",
                          plot_bgcolor="#FFFFFF",width=600, height=400, margin=dict(l=20, r=20, b=20, t=30),
                            xaxis=dict(mirror=True,showline=True, linewidth=1, linecolor='#afb9cf', gridcolor='#dfe3ec'),
                            yaxis=dict(mirror=True,showline=True, linewidth=1, linecolor='#afb9cf', gridcolor='#dfe3ec')
                         ,hovermode="x unified",
                          title={
                                
                                'y':0.99,
                                'x':0.2,
                                'xanchor': 'center',
                                'yanchor': 'top'},
                            xaxis_title="Date",
                            yaxis_title="Number of Users"
                            ,legend=dict(
                                        orientation="h",
                                        yanchor="bottom",
                                        y=1.02,
                                        xanchor="right",
                                        x=1
                                      )
                             )
    google4.layout.xaxis.fixedrange = True
    google4.layout.yaxis.fixedrange = True
    
    google = [google1,google2,google3,google4]
    
    return google

def admin_page():
    
    labels = ['UnComplete Registration','Complete Registration']
    values = [1225,2481]
    color = ['#F05454','#30475E']
    
    admin1 = go.Figure(data=[go.Pie(labels=labels, values=values, hole=.7 ,showlegend=True,
        hovertext=[1225,2481],
        hoverinfo="text",marker=dict(colors=color))])
    admin1.add_trace(go.Indicator(
        mode = "number",
        value = 3710,
        number = {"font": {"size": 30,'color': "#31333F"}},
        title = {'text': "<b>Registration</b><br><span style='color: #31333F; font-size:0.8em'>All Reg.</span>"
                     , 'font': {'size': 15}}
        ,domain = {'y': [0.3, 0.4], 'x': [0.5, 0.5]}
    ))
    admin1.update_layout(autosize=False,paper_bgcolor="#FFFFFF", plot_bgcolor="#FFFFFF"
                       ,width=600, height=350, margin=dict(l=20, r=20, b=20, t=30)
                       ,legend=dict(
                                   orientation="h",
                                   yanchor="bottom",
                                   y=1.02,
                                   xanchor="right",
                                   x=1
                                 ))
    
    ###########################################################################
    color_reg = ['#F05454','#eb1414','#30475e','#233343']
    cat5 = 'Reg'
    
    admin2 = go.Figure()

    admin2.add_trace(go.Bar(
                y=["JOR","KSA","UAE","QAT","EGY","MOR"],
                x=["1548","186","181","13","508","9"],
                name='Complete Registration',
                orientation='h',
                text=["1548","186","181","13","508","9"],
                textposition='auto',
                marker=dict(
                    color=color_reg[2],
                    line=dict(color=color_reg[3], width=3)
                )
            ))
    admin2.add_trace(go.Bar(
                y=["JOR","KSA","UAE","QAT","EGY","MOR"],
                x=["416","174","63","13","194","19"],
                name='UnComplete Registration',
                orientation='h',
                text=["416","174","63","13","194","19"],
                textposition='auto',
                marker=dict(
                    color=color_reg[0],
                    line=dict(color=color_reg[1], width=3)
                )
            ))
    
    admin2.update_layout(barmode='stack',autosize=False,
                                 width=600, height=350, margin=dict(l=20, r=20, b=20, t=30), # left , right , bottom , top
                                 paper_bgcolor="#FFFFFF",plot_bgcolor="#FFFFFF", font={'size': 15},
                         xaxis=dict(showgrid=False,showline=False,zerolinecolor='#FFFFFF'),
                      yaxis=dict(showgrid=False,showline=False,zerolinecolor='#FFFFFF')
                      ,legend=dict(
                                  orientation="h",
                                  yanchor="bottom",
                                  y=1.02,
                                  xanchor="right",
                                  x=1
                                )
                     )
    admin2.layout.xaxis.fixedrange = True
    admin2.layout.yaxis.fixedrange = True
    ###########################################################################
    admin3 = go.Figure()
    
    admin3.add_trace(go.Indicator(
        mode = "number",
        value = 2481,
        number = {"font": {"size": 40,'color': "#31333F"}},
        title = {"text": "Complete Registration","font": {"size": 15, 'color': "#31333F"}}
        ,domain = {'y': [0.4, 0.5], 'x': [0.5, 0.5]}
    ))
    
    
    admin3.add_trace(go.Pie(labels=['Complete Registration'], values=[1], hole=.9,hoverinfo='skip', textinfo='none'
                         ,showlegend=False,marker=dict(colors=['#30475E'])))
    
    
    
    admin3.update_layout(autosize=False,paper_bgcolor="#FFFFFF", plot_bgcolor="#FFFFFF",
                       width=700, height=300, margin=dict(l=20, r=20, b=20, t=30),
                      xaxis=dict(showgrid=False,showline=False,showticklabels=False,zerolinecolor='#F0F2F6'),
                  yaxis=dict(showgrid=False,showline=False,showticklabels=False,zerolinecolor='#F0F2F6'),
                     ) 
    ###########################################################################
    
    admin4 = go.Figure()
    
    admin4.add_trace(go.Indicator(
        mode = "number",
        value = 1225,
        number = {"font": {"size": 40,'color': "#31333F"}},
        title = {"text": "UnComplete Registration","font": {"size": 15, 'color': "#31333F"}}
        ,domain = {'y': [0.4, 0.5], 'x': [0.5, 0.5]}
    ))
    
    
    admin4.add_trace(go.Pie(labels=['UnComplete Registration'], values=[1], hole=.9,hoverinfo='skip', textinfo='none'
                         ,showlegend=False,marker=dict(colors=['#F05454'])))
    
    
    
    admin4.update_layout(autosize=False,paper_bgcolor="#FFFFFF", plot_bgcolor="#FFFFFF",
                       width=700, height=300, margin=dict(l=20, r=20, b=20, t=30),
                      xaxis=dict(showgrid=False,showline=False,showticklabels=False,zerolinecolor='#F0F2F6'),
                  yaxis=dict(showgrid=False,showline=False,showticklabels=False,zerolinecolor='#F0F2F6'),
                     ) 
    
    ###########################################################################
    admin5 = go.Figure(data=go.Scatter(x=date, 
                               y=[32,31,23,31,41,34,112,173,254,178,140,112,57,157,70,128,52,91,82,52,74,46,195,46,54,72,35,40,39,30]
                               ,mode='lines+markers',
                               name='Registered Users',line_color="#30475E",line_width=1.5,marker_size=4,
                                hovertemplate='%{y}'
                                   ))
    
    admin5.update_layout(showlegend=True)
    admin5.update_layout(autosize=False,paper_bgcolor="#FFFFFF",
                          plot_bgcolor="#FFFFFF",width=600, height=350, margin=dict(l=20, r=20, b=20, t=30),
                            xaxis=dict(mirror=True,showline=True, linewidth=1, linecolor='#afb9cf', gridcolor='#dfe3ec'),
                            yaxis=dict(mirror=True,showline=True, linewidth=1, linecolor='#afb9cf', gridcolor='#dfe3ec')
                         ,hovermode="x unified"
                         ,legend=dict(
                                     orientation="h",
                                     yanchor="bottom",
                                     y=1.02,
                                     xanchor="right",
                                     x=1
                                   )
                         ,title={
                                                            'text': "Complete Registration",
                                                            'y':0.97,
                                                            'x':0.5,
                                                            'xanchor': 'center',
                                                            'yanchor': 'top'},
                                                        xaxis_title="Date",
                                                        yaxis_title="No. Users",
                             )
                                        
    admin5.layout.xaxis.fixedrange = True
    admin5.layout.yaxis.fixedrange = True
    ################################# Gender###################################
    ###########################################################################

    admin6 = go.Figure(data=[go.Pie(labels=['Male', 'Female'], values=[1225,2481], hole=.85)])
    admin6.update_layout(
        annotations=[dict(text='Gender', x=0.50, y=0.50, font_size=25, showarrow=False)])
    admin6.update_traces(marker=dict(colors=['rgb(153, 187, 255)','rgba(246, 78, 139, 0.6)']),showlegend=False,textinfo='label+percent')
    admin6.update_layout(autosize=False,
                         width=390, height=300, margin=dict(l=20, r=20, b=20, t=30), # left , right , bottom , top
                         paper_bgcolor="#FFFFFF",plot_bgcolor="#FFFFFF", font={'size': 18})
    
    
    cat1,cat2 = 'Male','Female'
    color_gender_bar = ['rgba(246, 78, 139, 0.6)','rgba(246, 78, 139, 1.0)','rgb(153, 187, 255)','rgb(102, 153, 255)']
    

    admin7 = go.Figure()

    admin7.add_trace(go.Bar(
            y=["JOR","KSA","UAE","QAT","EGY","MOR"],
            x=["1548","186","181","13","508","9"],
            name=cat1,
            orientation='h',
            text=["1548","186","181","13","508","9"],
            textposition='auto',
            marker=dict(
                color=color_gender_bar[2],
                line=dict(color=color_gender_bar[3], width=3)
            )
        ))
    admin7.add_trace(go.Bar(
            y=["JOR","KSA","UAE","QAT","EGY","MOR"],
            x=["416","174","63","13","194","19"],
            name=cat2,
            orientation='h',
            text=["416","174","63","13","194","19"],
            textposition='auto',
            marker=dict(
                color=color_gender_bar[0],
                line=dict(color=color_gender_bar[1], width=3)
            )
        ))

    admin7.update_layout(autosize=False,barmode='stack',
                             width=600, height=300, margin=dict(l=20, r=20, b=20, t=30), # left , right , bottom , top
                             paper_bgcolor="#FFFFFF",plot_bgcolor="#FFFFFF", font={'size': 15},
                             xaxis=dict(showgrid=False,showline=False,zerolinecolor='#FFFFFF'),
                                           yaxis=dict(showgrid=False,showline=False,zerolinecolor='#FFFFFF')
                                           ,legend=dict(
                                                       orientation="h",
                                                       yanchor="bottom",
                                                       y=1.02,
                                                       xanchor="right",
                                                       x=1
                                                     ))
    admin7.layout.xaxis.fixedrange = True
    admin7.layout.yaxis.fixedrange = True
    ###########################################################################
    
    admin8 = go.Figure()

    admin8.add_trace(go.Indicator(
                title = {'text': "<b>Male</b><br>"
                         ,"font": {"size": 40, 'color': "#31333F"}},
                mode = "number",
                value = 1225,
                number={"font": {"size": 40, 'color': "#6699ff"}},
                domain = {'row': 0, 'column': 0}))    
    admin8.add_trace(go.Indicator(
                title = {'text': "<b>Female</b><br>"
                         ,"font": {"size": 40, 'color': "#31333F"}},
                mode = "number",
                value = 2481,
                number={"font": {"size": 40, 'color': "#f64e8b"}},
                domain = {'row': 0, 'column': 1}))
    
    admin8.update_layout(
                grid = {'rows': 1, 'columns': 2, 'pattern': "independent"})
    admin8.update_layout(autosize=False,paper_bgcolor="#FFFFFF", plot_bgcolor="#FFFFFF",width=700, height=200, margin=dict(l=20, r=20, b=20, t=65))
    
    
    ###########################################################################

    admin9 = go.Figure(data=[go.Pie(labels=['IOS', 'ANDROID'], values=[1225,2481], hole=.85)])
    admin9.update_layout(
    
        annotations=[dict(text='OS', x=0.50, y=0.50, font_size=25, showarrow=False)])
    admin9.update_traces(marker=dict(colors=['rgb(255, 102, 102)','rgb(112, 219, 112)']),showlegend=False,textinfo='label+percent')
    admin9.update_layout(autosize=False,
                         width=390, height=300, margin=dict(l=20, r=20, b=20, t=30), 
                         paper_bgcolor="#FFFFFF",plot_bgcolor="#FFFFFF", font={'size': 18})
    
    ###########################################################################
    cat3,cat4= 'Android','Ios'
    color_os_bar= ['rgb(255, 102, 102)','rgb(153, 0, 0)','rgb(112, 219, 112)','rgb(0, 153, 0)']
    
    admin10 = go.Figure()

    admin10.add_trace(go.Bar(
            y=["JOR","KSA","UAE","QAT","EGY","MOR"],
            x=["1548","186","181","13","508","9"],
            name=cat3,
            orientation='h',
            text=["1548","186","181","13","508","9"],
            textposition='auto',
            marker=dict(
                color=color_os_bar[2],
                line=dict(color=color_os_bar[3], width=3)
            )
        ))
    admin10.add_trace(go.Bar(
            y=["JOR","KSA","UAE","QAT","EGY","MOR"],
            x=["416","174","63","13","194","19"],
            name=cat4,
            orientation='h',
            text=["416","174","63","13","194","19"],
            textposition='auto',
            marker=dict(
                color=color_os_bar[0],
                line=dict(color=color_os_bar[1], width=3)
            )
        ))
    admin10.update_layout(autosize=False,barmode='stack',
                             width=600, height=300, margin=dict(l=20, r=20, b=20, t=30), # left , right , bottom , top
                             paper_bgcolor="#FFFFFF",plot_bgcolor="#FFFFFF", font={'size': 15},
                             xaxis=dict(showgrid=False,showline=False,zerolinecolor='#FFFFFF'),
                                           yaxis=dict(showgrid=False,showline=False,zerolinecolor='#FFFFFF')
                                           ,legend=dict(
                                                       orientation="h",
                                                       yanchor="bottom",
                                                       y=1.02,
                                                       xanchor="right",
                                                       x=1
                                                     ))
    admin10.layout.xaxis.fixedrange = True
    admin10.layout.yaxis.fixedrange = True
    
    ###########################################################################
    admin11 = go.Figure()

    admin11.add_trace(go.Indicator(
                title = {'text': "<b>Android</b><br>"
                         ,"font": {"size": 40, 'color': "#31333F"}},
                mode = "number",
                value = 2481,
                number={"font": {"size": 40, 'color': "#29a329"}},
                domain = {'row': 0, 'column': 0}))    
    admin11.add_trace(go.Indicator(
                title = {'text': "<b>IOS</b><br>"
                         ,"font": {"size": 40, 'color': "#31333F"}},
                mode = "number",
                value = 1225,
                number={"font": {"size": 40, 'color': "#ff3333"}},
                domain = {'row': 0, 'column': 1}))
    
    admin11.update_layout(
                grid = {'rows': 1, 'columns': 2, 'pattern': "independent"})
    admin11.update_layout(autosize=False,paper_bgcolor="#FFFFFF", plot_bgcolor="#FFFFFF",width=700, height=200, margin=dict(l=20, r=20, b=20, t=65))

    ##################################Age######################################
    color1=['#545BFA','#34D98C','#F0E746','#D96D34','#CF3DFC']
    
    admin12 = go.Figure(data=[go.Pie(labels=['Age 7-16','Age 17-30','Age 31-40','Age 41-50','Age 51-80'], 
                                     values=[857,953,401,139,53], hole=.85)])
    admin12.update_layout(
                annotations=[dict(text='Age Group', x=0.50, y=0.50, font_size=25, showarrow=False)])
    admin12.update_traces(marker=dict(colors=['#545BFA','#34D98C','#F0E746','#D96D34','#CF3DFC']),showlegend=False)
    admin12.update_layout(autosize=False,
                             width=390, height=300, margin=dict(l=20, r=20, b=20, t=30), # left , right , bottom , top
                             paper_bgcolor="#FFFFFF",plot_bgcolor="#FFFFFF", font={'size': 18})
    
    ###########################################################################
    
    admin13 = go.Figure()
    admin13.add_trace(go.Bar(x=['Age 7-16','Age 17-30','Age 31-40','Age 41-50','Age 51-80'],
                            y=[857,953,401,139,53],
                            name='All',
                            text=[857,953,401,139,53],
                            textposition='auto',
                                marker=dict(
                color=color1            )
                            ))
    admin13.update_layout(autosize=False,
                             width=600, height=300, margin=dict(l=20, r=20, b=20, t=30), # left , right , bottom , top
                             paper_bgcolor="#FFFFFF",plot_bgcolor="#FFFFFF", font={'size': 18},
                             xaxis=dict(showgrid=False,showline=False,zerolinecolor='#FFFFFF',showticklabels=True),
                                           yaxis=dict(showgrid=False,showline=True,zerolinecolor='#FFFFFF'))
    
    admin13.layout.xaxis.fixedrange = True
    admin13.layout.yaxis.fixedrange = True
    
    ###########################################################################
    
    cat1,cat2,cat3,cat4,cat5 = 'Age7_16','Age17_30','Age31_40','Age41_50','Age51_80'
    color1=['#545BFA','#34D98C','#F0E746','#D96D34','#CF3DFC']
    
    admin14 = go.Figure()

    admin14.add_trace(go.Bar(
            x=["JOR","KSA","UAE","QAT","EGY","MOR"],
            y=[580,49,25,1,194,2],
                name=cat1,
                text=[580,49,25,1,194,2],
                textposition='auto',
            marker=dict(
                color=color1[0]            )        ))
    admin14.add_trace(go.Bar(
            x=["JOR","KSA","UAE","QAT","EGY","MOR"],
            y=[580,49,25,1,194,2],
            name=cat2,
            text=[580,49,25,1,194,2],
            textposition='auto',
            marker=dict(
                color=color1[1]            )        ))
    admin14.add_trace(go.Bar(
            x=["JOR","KSA","UAE","QAT","EGY","MOR"],
            y=[580,49,25,1,194,2],
            name=cat3,
            text=[580,49,25,1,194,2],
            textposition='auto',
            marker=dict(
                color=color1[2]            )        ))
    admin14.add_trace(go.Bar(
            x=["JOR","KSA","UAE","QAT","EGY","MOR"],
            text=[580,49,25,1,194,2],
            textposition='auto',
            y=[580,49,25,1,194,2],
            name=cat4,
            marker=dict(
                color=color1[3]            )        ))
    admin14.add_trace(go.Bar(
            x=["JOR","KSA","UAE","QAT","EGY","MOR"],
            text=[580,49,25,1,194,2],
            textposition='auto',
            y=[580,49,25,1,194,2],
            name=cat5,
            marker=dict(
                color=color1[4]            )        ))
    
    admin14.update_layout(autosize=False,barmode='group',
                             width=600, height=300, margin=dict(l=20, r=20, b=20, t=30), # left , right , bottom , top
                             paper_bgcolor="#FFFFFF",plot_bgcolor="#FFFFFF", font={'size': 15},
                             xaxis=dict(showgrid=False,showline=False,zerolinecolor='#FFFFFF'),
                                           yaxis=dict(showgrid=False,showline=False,zerolinecolor='#FFFFFF')
                                           ,legend=dict(
                                                       orientation="h",
                                                       yanchor="bottom",
                                                       y=1.02,
                                                       xanchor="right",
                                                       x=1
                                                     ))
    admin14.layout.xaxis.fixedrange = True
    admin14.layout.yaxis.fixedrange = True
    
    ###########################################################################
    
    admin15 = go.Figure()

    admin15.add_trace(go.Indicator(
                title = {'text': "<b>AGE 7-16</b><br>"
                         ,"font": {"size": 25, 'color': "#31333F"}},
                mode = "number",
                value = 857,
                number={"font": {"size": 40, 'color': "#545BFA"}},
                domain = {'row': 0, 'column': 0}))   
    
    admin15.update_layout(
                grid = {'rows': 1, 'columns': 1, 'pattern': "independent"})
    admin15.update_layout(autosize=False,paper_bgcolor="#FFFFFF", plot_bgcolor="#FFFFFF",width=700, height=250, margin=dict(l=20, r=20, b=20, t=65))
    
    ###########################################################################
    
    admin16 = go.Figure()
    admin16.add_trace(go.Indicator(
                title = {'text': "<b>AGE 17-30</b><br>"
                         ,"font": {"size": 25, 'color': "#31333F"}},
                mode = "number",
                value = 953,
                number={"font": {"size": 40, 'color': "#34D98C"}},
                domain = {'row': 0, 'column': 0}))
    admin16.add_trace(go.Indicator(
                title = {'text': "<b>AGE 31-40</b><br>"
                         ,"font": {"size": 25, 'color': "#31333F"}},
                mode = "number",
                value = 401,
                number={"font": {"size": 40, 'color': "#d4cb11"}},
                domain = {'row': 0, 'column': 1}))  
    
    admin16.update_layout(
                grid = {'rows': 1, 'columns': 2, 'pattern': "independent"})
    admin16.update_layout(autosize=False,paper_bgcolor="#FFFFFF", plot_bgcolor="#FFFFFF",width=700, height=250, margin=dict(l=20, r=20, b=20, t=65))
    
    ###########################################################################
    
    admin17 = go.Figure()
    admin17.add_trace(go.Indicator(
                title = {'text': "<b>AGE 41-50</b><br>"
                         ,"font": {"size": 25, 'color': "#31333F"}},
                mode = "number",
                value = 193,
                number={"font": {"size": 40, 'color': "#D96D34"}},
                domain = {'row': 0, 'column': 0}))
    admin17.add_trace(go.Indicator(
                title = {'text': "<b>AGE 51-80</b><br>"
                         ,"font": {"size": 25, 'color': "#31333F"}},
                mode = "number",
                value = 95,
                number={"font": {"size": 40, 'color': "#CF3DFC"}},
                domain = {'row': 0, 'column': 1}))    
    
    admin17.update_layout(
                grid = {'rows': 1, 'columns': 2, 'pattern': "independent"})
    admin17.update_layout(autosize=False,paper_bgcolor="#FFFFFF", plot_bgcolor="#FFFFFF",width=700, height=250, margin=dict(l=20, r=20, b=20, t=65))
    
    admin = [admin1,admin2,admin3,admin4,admin5,admin6,admin7,admin8,admin9,admin10,admin11,admin12,admin13,admin14,admin15,admin16,admin17]
    
    return admin

def apple_page():
    
    apple1 = go.Figure()
    apple1.add_trace(go.Indicator(
        mode = "number+delta",
        value = 4000,
        number = {"font": {"size": 35,'color': "#31333F"}},
        delta = {"reference": 3500, 'relative': True, "valueformat": ".0%"},
        title = {"text": "Installs","font": {"size": 25, 'color': "#31333F"}}
        ,domain = {'y': [0.3, 0.5], 'x': [0.5, 0.5]}
    ))
    apple1.add_trace(go.Pie(labels=['New Users'], values=[50], hole=.9,hoverinfo='skip', textinfo='none'
                         ,showlegend=False,marker=dict(colors=['#4D96FF'])))
    apple1.update_layout(autosize=False,paper_bgcolor="#FFFFFF", plot_bgcolor="#FFFFFF",
                       width=680, height=250, margin=dict(l=20, r=20, b=20, t=30),
                      xaxis=dict(showgrid=False,showline=False,showticklabels=False,zerolinecolor='#F0F2F6'),
                  yaxis=dict(showgrid=False,showline=False,showticklabels=False,zerolinecolor='#F0F2F6'))

    ###########################################################################
    apple2 = go.Figure(data=go.Scatter(x=date, 
                               y=[3,4,2,1,6,7,13,7,11,22,27,11,6,10,11,6,4,11,10,7,4,7,6,4,7,1,5,6,6,5]
                               ,mode='lines+markers',
                               name='Installs',line_color="#4D96FF",line_width=1.5,marker_size=4,
                                hovertemplate='%{y}'
                                   ))
    
    apple2.update_layout(showlegend=True)
    apple2.update_layout(autosize=False,paper_bgcolor="#FFFFFF",
                          plot_bgcolor="#FFFFFF",width=600, height=220, margin=dict(l=20, r=20, b=20, t=30),
                            xaxis=dict(mirror=True,showline=True, linewidth=1, linecolor='#afb9cf', gridcolor='#dfe3ec'),
                            yaxis=dict(mirror=True,showline=True, linewidth=1, linecolor='#afb9cf', gridcolor='#dfe3ec')
                         ,hovermode="x unified"
                         ,legend=dict(
                                     orientation="h",
                                     yanchor="bottom",
                                     y=1.02,
                                     xanchor="right",
                                     x=1
                                   )
                             )   
    
    apple2.layout.xaxis.fixedrange = True
    apple2.layout.yaxis.fixedrange = True
    ###########################################################################
    apple3 = go.Figure()
    apple3.add_trace(go.Indicator(
        mode = "number+delta",
        value = 1200,
        number = {"font": {"size": 35,'color': "#31333F"}},
        delta = {"reference": 1000, 'relative': True, "valueformat": ".0%"},
        title = {"text": "Active Users","font": {"size": 25, 'color': "#31333F"}}
        ,domain = {'y': [0.3, 0.5], 'x': [0.5, 0.5]}
    ))
    apple3.add_trace(go.Pie(labels=['Active Users'], values=[50], hole=.9,hoverinfo='skip', textinfo='none'
                         ,showlegend=False,marker=dict(colors=['#4FBDBA'])))
    apple3.update_layout(autosize=False,paper_bgcolor="#FFFFFF", plot_bgcolor="#FFFFFF",
                       width=680, height=250, margin=dict(l=20, r=20, b=20, t=30),
                      xaxis=dict(showgrid=False,showline=False,showticklabels=False,zerolinecolor='#F0F2F6'),
                  yaxis=dict(showgrid=False,showline=False,showticklabels=False,zerolinecolor='#F0F2F6'))
    
    apple4 = go.Figure(data=go.Scatter(x=date, 
                               y=[589,583,574,578,575,560,581,590,609,629,643,648,645,643,655,647,652,662,669,675,661,661,667,664,673,669,669,675,671,667]
                               ,mode='lines+markers',
                               name='Active Users',line_color="#4FBDBA",line_width=1.5,marker_size=4,
                                hovertemplate='%{y}'
                                   ))
    
    apple4.update_layout(showlegend=True)
    apple4.update_layout(autosize=False,paper_bgcolor="#FFFFFF",
                          plot_bgcolor="#FFFFFF",width=680, height=220, margin=dict(l=20, r=20, b=20, t=30),
                            xaxis=dict(mirror=True,showline=True, linewidth=1, linecolor='#afb9cf', gridcolor='#dfe3ec'),
                            yaxis=dict(mirror=True,showline=True, linewidth=1, linecolor='#afb9cf', gridcolor='#dfe3ec')
                         ,hovermode="x unified"
                         ,legend=dict(
                                     orientation="h",
                                     yanchor="bottom",
                                     y=1.02,
                                     xanchor="right",
                                     x=1
                                   )
                             ) 
    
    apple4.layout.xaxis.fixedrange = True
    apple4.layout.yaxis.fixedrange = True
    
    apple = [apple1,apple2,apple3,apple4]
    
    return apple
    
def marchant_chart(time_report1,country,x_from, x_to):

    color_gender_bar = ['rgba(246, 78, 139, 0.6)','rgba(246, 78, 139, 1.0)','rgb(153, 187, 255)','rgb(102, 153, 255)']
    
    f1 = go.Figure()

    
    f1.add_trace(go.Indicator(
            mode = "number",
            number = {"font": {"size": 55,'color': "#31333F"}},
            value = 10
            ,domain = {'y': [0.5, 0.5], 'x': [0.5, 0.5]}
            ))
    f1.add_trace(go.Pie(labels=['active'], values=[200], hole=.85,hoverinfo='skip', textinfo='none'
                             ,showlegend=False,marker=dict(colors=['#999999'])))
    
    f1.update_layout(autosize=False,paper_bgcolor="#FFFFFF", plot_bgcolor="#FFFFFF",
                               width=1000, height=250, margin=dict(l=20, r=20, b=20, t=50),
                              xaxis=dict(showgrid=False,showline=False,showticklabels=False,zerolinecolor='#FFFFFF'),
                          yaxis=dict(showgrid=False,showline=False,showticklabels=False,zerolinecolor='#FFFFFF'),title={
                                                  'text': "NO. Campaigns",
                                                  'y':0.9,
                                                  'x':0.5,
                                                  'xanchor': 'center',
                                                  'yanchor': 'top'})
    ###########################################################################
    
    f2 = go.Figure()

    
    f2.add_trace(go.Indicator(
            mode = "number",
            number = {"font": {"size": 55,'color': "#31333F"}},
            value = 611000
            ,domain = {'y': [0.5, 0.5], 'x': [0.5, 0.5]}
            ))
    f2.add_trace(go.Pie(labels=['inactive'], values=[200], hole=.85,hoverinfo='skip', textinfo='none'
                             ,showlegend=False,marker=dict(colors=['#E6815A'])))

    f2.update_layout(autosize=False,paper_bgcolor="#FFFFFF", plot_bgcolor="#FFFFFF",
                               width=1000, height=250, margin=dict(l=20, r=20, b=20, t=50),
                              xaxis=dict(showgrid=False,showline=False,showticklabels=False,zerolinecolor='#FFFFFF'),
                          yaxis=dict(showgrid=False,showline=False,showticklabels=False,zerolinecolor='#FFFFFF'),title={
                                                  'text': "NO. Players",
                                                  'y':0.9,
                                                  'x':0.5,
                                                  'xanchor': 'center',
                                                  'yanchor': 'top'})
    ###########################################################################
    
    
    f4 = go.Figure()

    
    f4.add_trace(go.Indicator(
            mode = "number",
            number = {"font": {"size": 55,'color': "#31333F"}},
            value = 2
            ,domain = {'y': [0.5, 0.5], 'x': [0.5, 0.5]}
            ))
    f4.add_trace(go.Pie(labels=['active'], values=[200], hole=.85,hoverinfo='skip', textinfo='none'
                             ,showlegend=False,marker=dict(colors=['#81DB27'])))
    
    f4.update_layout(autosize=False,paper_bgcolor="#FFFFFF", plot_bgcolor="#FFFFFF",
                               width=1000, height=250, margin=dict(l=20, r=20, b=20, t=50),
                              xaxis=dict(showgrid=False,showline=False,showticklabels=False,zerolinecolor='#FFFFFF'),
                          yaxis=dict(showgrid=False,showline=False,showticklabels=False,zerolinecolor='#FFFFFF'),title={
                                                  'text': "Active Campaigns",
                                                  'y':0.9,
                                                  'x':0.5,
                                                  'xanchor': 'center',
                                                  'yanchor': 'top'})
    ###########################################################################
    
    f5 = go.Figure()

    
    f5.add_trace(go.Indicator(
            mode = "number",
            number = {"font": {"size": 55,'color': "#31333F"}},
            value = 8
            ,domain = {'y': [0.5, 0.5], 'x': [0.5, 0.5]}
            ))
    f5.add_trace(go.Pie(labels=['inactive'], values=[200], hole=.85,hoverinfo='skip', textinfo='none'
                             ,showlegend=False,marker=dict(colors=['#DB3D38'])))

    f5.update_layout(autosize=False,paper_bgcolor="#FFFFFF", plot_bgcolor="#FFFFFF",
                               width=1000, height=250, margin=dict(l=20, r=20, b=20, t=50),
                              xaxis=dict(showgrid=False,showline=False,showticklabels=False,zerolinecolor='#FFFFFF'),
                          yaxis=dict(showgrid=False,showline=False,showticklabels=False,zerolinecolor='#FFFFFF'),title={
                                                  'text': "Inctive Campaigns",
                                                  'y':0.9,
                                                  'x':0.5,
                                                  'xanchor': 'center',
                                                  'yanchor': 'top'})
    
    ###########################################################################
    ###########################################################################

    f6 = go.Figure(data=[go.Pie(labels=['Male', 'Female'], values=[270410,340313], hole=.85)])
    f6.update_layout(
            annotations=[dict(text='Gender', x=0.50, y=0.50, font_size=25, showarrow=False)])
    f6.update_traces(marker=dict(colors=['rgb(153, 187, 255)','rgba(246, 78, 139, 0.6)']),showlegend=False,textinfo='label+percent')
    f6.update_layout(autosize=False,
                             width=390, height=300, margin=dict(l=20, r=20, b=20, t=30), # left , right , bottom , top
                             paper_bgcolor="#FFFFFF",plot_bgcolor="#FFFFFF", font={'size': 18})
    ###################################################################################################################
    
    
    color_gender_bar = ['rgba(246, 78, 139, 0.6)','rgba(246, 78, 139, 1.0)','rgb(153, 187, 255)','rgb(102, 153, 255)']

        

    f7 = go.Figure(data=[
        go.Bar(name='male', 
               x=["Brand 1","Brand 2","Brand 3","Brand 4","Brand 5","Brand 6","Brand 7","Brand 8","Brand 9","Brand 10"],
               y=[2388,48151,38291,32370,27260,27616,35173,34056,23578,1527],
               marker=dict(
                        color=color_gender_bar[2],
                        line=dict(color=color_gender_bar[3], width=3))),
        go.Bar(name='female',
               x=["Brand 1","Brand 2","Brand 3","Brand 4","Brand 5","Brand 6","Brand 7","Brand 8","Brand 9","Brand 10"],
               y=[2804,58255,47951,40832,41770,29831,47441,33184,35423,2822],
               marker=dict(
                        color=color_gender_bar[0],
                        line=dict(color=color_gender_bar[1], width=3)))
    ])
    
    f7.update_layout(barmode='group',autosize=False,
                                     width=600, height=500, margin=dict(l=20, r=20, b=20, t=30), # left , right , bottom , top
                                     paper_bgcolor="#FFFFFF",plot_bgcolor="#FFFFFF", font={'size': 15},
                             xaxis=dict(showgrid=False,showline=False,zerolinecolor='#FFFFFF',tickangle = 50),
                          yaxis=dict(showgrid=False,showline=False,zerolinecolor='#FFFFFF')
                         , bargap=0.5,bargroupgap=0.2
                         ,legend=dict(
                                     orientation="h",
                                     yanchor="bottom",
                                     y=1.02,
                                     xanchor="right",
                                     x=0.95
                                   ))
    f7.layout.xaxis.fixedrange = True
    f7.layout.yaxis.fixedrange = True
    ####################################################################################################################
    f8 = go.Figure()


    f8.add_trace(go.Indicator(
        mode = "number",
        number = {"font": {"size": 40,'color': "rgb(153, 187, 255)"}},
        value = 48200,
        title = {"text": "Max Number of Male","font": {"size": 20, 'color': "#31333F"}},
        domain = {'row': 0, 'column': 0}))

    f8.add_trace(go.Indicator(
        mode = "number",
        number = {"font": {"size": 40,'color': "rgba(246, 78, 139, 0.6)"}},
        value = 58300,
        title = {"text": "Max Number of Female","font": {"size": 20, 'color': "#31333F"}},
        domain = {'row': 1, 'column': 0}))

    f8.update_layout(
        grid = {'rows': 2, 'columns': 1, 'pattern': "independent"},
        template = {'data' : {'indicator': [{
            'title': {'text': "Speed"},
            'mode' : "number"}]}})
    f8.add_annotation(xref="paper",
                    yref="paper",
                    x=0.5,
                    y=0.74  ,
                text='Campaing Name',showarrow=False)
    f8.add_annotation(xref="paper",
                    yref="paper",
                    x=0.5,
                    y=0.1  ,
                text='Campaign Name',showarrow=False)
    f8.add_annotation(xref="paper",
                    yref="paper",
                    x=0.5,
                    y=0.7  ,
                text='Brand 1',showarrow=False)
    f8.add_annotation(xref="paper",
                    yref="paper",
                    x=0.5,
                    y=0.06  ,
                text='Brand 2',showarrow=False)
    f8.update_layout(autosize=False,paper_bgcolor="#FFFFFF", plot_bgcolor="#FFFFFF",
                           width=300, height=500, margin=dict(l=20, r=20, b=20, t=30),
                          xaxis=dict(showgrid=False,showline=False,showticklabels=False,zerolinecolor='#FFFFFF'),
                      yaxis=dict(showgrid=False,showline=False,showticklabels=False,zerolinecolor='#FFFFFF'))
    ###########################################################################
    f9 = go.Figure()

    f9.add_trace(go.Indicator(
                title = {'text': "<b>Male</b><br>"
                         ,"font": {"size": 40, 'color': "#0F4C75"}},
                mode = "number",
                value = 270400,
                number={"font": {"size": 40, 'color': "#6699ff"}},
                domain = {'row': 0, 'column': 0}))    
    f9.add_trace(go.Indicator(
                title = {'text': "<b>Female</b><br>"
                         ,"font": {"size": 40, 'color': "#0F4C75"}},
                mode = "number",
                value = 340000,
                number={"font": {"size": 40, 'color': "#f64e8b"}},
                domain = {'row': 0, 'column': 1}))
    
    f9.update_layout(
                grid = {'rows': 1, 'columns': 2, 'pattern': "independent"})
    f9.update_layout(autosize=False,paper_bgcolor="#FFFFFF", plot_bgcolor="#FFFFFF",width=700, height=200, margin=dict(l=20, r=20, b=20, t=65))
    ###########################################################################

    f10 = go.Figure(data=[go.Pie(labels=["Age7_16","Age17_30","Age31_40","Age41_50","Age51_80"], 
                                 values=[57635,334482,142511,32970,36071],
                                 hole=.85)])
    f10.update_layout(
                    annotations=[dict(text='Age Group', x=0.50, y=0.50, font_size=25, showarrow=False)])
    f10.update_traces(marker=dict(colors=['#545BFA','#34D98C','#F0E746','#D96D34','#CF3DFC']),showlegend=True)
    f10.update_layout(autosize=False,
                                 width=450, height=300, margin=dict(l=20, r=20, b=20, t=30), # left , right , bottom , top
                                 paper_bgcolor="#FFFFFF",plot_bgcolor="#FFFFFF", font={'size': 18},
                             legend=dict( font=dict(
                                              size=10,
                                              color="black"
                                              )))
    
    f11 = go.Figure()

    
    f11.add_trace(go.Indicator(
        mode = "number",
        number = {"font": {"size": 40,'color': "#31333F"}},
        value = 334000,
        title = {"text": 'Age 17-30',"font": {"size": 20, 'color': "#31333F"}}
        ,domain = {'y': [0.5, 0.5], 'x': [0.5, 0.5]}
        ))
    f11.add_trace(go.Pie(labels=['age'], values=[200], hole=.9,hoverinfo='skip', textinfo='none'
                         ,showlegend=False,marker=dict(colors=['#34D98C'])))

    f11.add_annotation(xref="paper",
                    yref="paper",
                    x=0.5,
                    y=0.3  ,
                text='Max Age Group',showarrow=False)
    f11.update_layout(autosize=False,paper_bgcolor="#FFFFFF", plot_bgcolor="#FFFFFF",
                           width=1000, height=250, margin=dict(l=20, r=20, b=20, t=30),
                          xaxis=dict(showgrid=False,showline=False,showticklabels=False,zerolinecolor='#FFFFFF'),
                      yaxis=dict(showgrid=False,showline=False,showticklabels=False,zerolinecolor='#FFFFFF'))
    
    ###########################################################################
   
    color1=['#545BFA','#34D98C','#F0E746','#D96D34','#CF3DFC']
    f12 = go.Figure(data=[
        go.Bar(name='Age 7-16', x=["Brand 1","Brand 2","Brand 3","Brand 4","Brand 5","Brand 6","Brand 7","Brand 8","Brand 9","Brand 10"], 
               y=[453,10610,9007,7423,5877,5618,6782,6685,4912,268],
               marker=dict(color=color1[0]),width=0.1),
        go.Bar(name='Age 17-30', x=["Brand 1","Brand 2","Brand 3","Brand 4","Brand 5","Brand 6","Brand 7","Brand 8","Brand 9","Brand 10"],
               y=[2399,58227,46009,40028,31910,32033,50201,37866,33554,2255],
               marker=dict(color=color1[1]),width=0.1),
        go.Bar(name='Age 31-40', x=["Brand 1","Brand 2","Brand 3","Brand 4","Brand 5","Brand 6","Brand 7","Brand 8","Brand 9","Brand 10"], 
               y=[1031,23018,18699,16863,23404,12659,16800,15214,13691,1132],
               marker=dict(color=color1[2]),width=0.1),
        go.Bar(name='Age 41-50', x=["Brand 1","Brand 2","Brand 3","Brand 4","Brand 5","Brand 6","Brand 7","Brand 8","Brand 9","Brand 10"],
               y=[416,6930,4804,4160,3720,2849,3765,3397,2795,134],
               marker=dict(color=color1[3]),width=0.1),
        go.Bar(name='Age 51-80', x=["Brand 1","Brand 2","Brand 3","Brand 4","Brand 5","Brand 6","Brand 7","Brand 8","Brand 9","Brand 10"],
               y=[958,3968,7387,4010,3936,3926,3939,3713,3687,547],
               marker=dict(color=color1[4]),width=0.1)
    ])
    # Change the bar mode
    f12.update_layout(barmode='group',autosize=False,
                                     width=800, height=500, margin=dict(l=20, r=20, b=20, t=30), # left , right , bottom , top
                                     paper_bgcolor="#FFFFFF",plot_bgcolor="#FFFFFF", font={'size': 15},
                             xaxis=dict(showgrid=False,showline=False,zerolinecolor='#FFFFFF',tickangle = 50),
                          yaxis=dict(showgrid=False,showline=False,zerolinecolor='#FFFFFF')
                         , bargap=0.5,bargroupgap=1
                         ,legend=dict(
                                     orientation="h",
                                     yanchor="bottom",
                                     y=1.02,
                                     xanchor="right",
                                     x=0.95
                                   ))
    f12.layout.xaxis.fixedrange = True
    f12.layout.yaxis.fixedrange = True
    
    color1=['#545BFA','#34D98C','#F0E746','#D96D34','#CF3DFC']

    
    
    ###########################################################################
    f13 = go.Figure()

    f13.add_trace(go.Indicator(
                title = {'text': "<b>AGE 7-16</b><br>"
                         ,"font": {"size": 25, 'color': "#31333F"}},
                mode = "number",
                value = 57600,
                number={"font": {"size": 40, 'color': "#545BFA"}},
                domain = {'row': 0, 'column': 0})) 
    
    f13.update_layout(
               grid = {'rows': 1, 'columns': 1, 'pattern': "independent"})
    f13.update_layout(autosize=False,paper_bgcolor="#FFFFFF", plot_bgcolor="#FFFFFF",width=700, height=250, margin=dict(l=20, r=20, b=20, t=65))
    
    ###########################################################################
    f14 = go.Figure()

        
    f14.add_trace(go.Indicator(
                title = {'text': "<b>AGE 17-30</b><br>"
                         ,"font": {"size": 25, 'color': "#31333F"}},
                mode = "number",
                value = 334000,
                number={"font": {"size": 40, 'color': "#34D98C"}},
                domain = {'row': 0, 'column': 0}))
    f14.add_trace(go.Indicator(
                title = {'text': "<b>AGE 31-40</b><br>"
                         ,"font": {"size": 25, 'color': "#31333F"}},
                mode = "number",
                value = 142500,
                number={"font": {"size": 40, 'color': "#F0E746"}},
                domain = {'row': 0, 'column': 1}))    
  
    
    f14.update_layout(
                grid = {'rows': 1, 'columns': 2, 'pattern': "independent"})
    f14.update_layout(autosize=False,paper_bgcolor="#FFFFFF", plot_bgcolor="#FFFFFF",width=700, height=250, margin=dict(l=20, r=20, b=20, t=65))
    
    ###########################################################################
    f15 = go.Figure()
  
    f15.add_trace(go.Indicator(
                  title = {'text': "<b>AGE 41-50</b><br>"
                           ,"font": {"size": 25, 'color': "#31333F"}},
                  mode = "number",
                  value = 33000,
                  number={"font": {"size": 40, 'color': "#D96D34"}},
                  domain = {'row': 0, 'column': 0}))
    f15.add_trace(go.Indicator(
                  title = {'text': "<b>AGE 51-80</b><br>"
                           ,"font": {"size": 25, 'color': "#31333F"}},
                  mode = "number",
                  value = 36100,
                  number={"font": {"size": 40, 'color': "#CF3DFC"}},
                  domain = {'row': 0, 'column': 1}))   
    f15.update_layout(
                  grid = {'rows': 1, 'columns': 2, 'pattern': "independent"})
    f15.update_layout(autosize=False,paper_bgcolor="#FFFFFF", plot_bgcolor="#FFFFFF",width=700, height=250, margin=dict(l=20, r=20, b=20, t=65))
    ###########################################################################
    colors = {'Inactive': '#b30000',
          'Active': '#00802b'}

    f16 = ff.create_gantt(gantt_list, colors=colors, index_col='Resource', show_colorbar=True,title = 'Campigns',
                          group_tasks=False,show_hover_fill=True,bar_width =0.2,showgrid_x =True)
    f16.update_xaxes(showgrid=True, gridwidth=0.001, gridcolor='Black',showline=True, linewidth=2, linecolor='black', mirror=True)
    f16.update_yaxes(showline=True, linewidth=2, linecolor='black', mirror=True)
    f16.update_layout(autosize=False,
                                 width=1000, height=650,
                                 paper_bgcolor="#FFFFFF",plot_bgcolor="#FFFFFF", font={'size': 15})
                                 
    f16.update_layout(
        xaxis=dict(
            rangeselector=dict(
                buttons=list([
                    dict(count=7,
                         label="1 Week",
                         step="day",
                         stepmode="backward"),
                    dict(count=1,
                         label="1 Month",
                         step="month",
                         stepmode="backward"),
                    dict(count=6,
                         label="6 Month",
                         step="month",
                         stepmode="backward"),
                    dict(count=1,
                         label="Year to Date",
                         step="year",
                         stepmode="todate"),
                    dict(count=1,
                         label="1 Year",
                         step="year",
                         stepmode="backward"),
                    dict(step="all")
                ])
            ),type="date"))
    
    f16.layout.xaxis.fixedrange = True
    f16.layout.yaxis.fixedrange = True
    ###########################################################################
    

    f17 = go.Figure(data=[
    go.Bar(name='Coin Available', 
           x=["Brand 1","Brand 2","Brand 3","Brand 4","Brand 5","Brand 6","Brand 7","Brand 8","Brand 9","Brand 10"],
           y=[4909,3158,38343,41074,42368,113249,41178,42830,42827,8893]
           ,marker=dict(
               color='#CCAD00'),text=[4909,3158,38343,41074,42368,113249,41178,42830,42827,8893],textposition='outside',
            texttemplate = '%{y:.2s}',
                   ),
    go.Bar(name='Coin Consumed', 
           x=["Brand 1","Brand 2","Brand 3","Brand 4","Brand 5","Brand 6","Brand 7","Brand 8","Brand 9","Brand 10"], 
           y=[1657,30462,25289,21553,20238,17091,24438,19855,17661,1107],
                   marker=dict(
                            color='#6E5D00'),text=[1657,30462,25289,21553,20238,17091,24438,19855,17661,1107],textposition='outside',
            texttemplate = '%{y:.2s}',
                   )
    
        ])        
    f17.update_layout(barmode='group',autosize=False,
                                 width=800, height=500, margin=dict(l=20, r=20, b=20, t=100), # left , right , bottom , top
                                paper_bgcolor="#FFFFFF",plot_bgcolor="#FFFFFF", font={'size': 15},
                            xaxis=dict(showgrid=False,showline=False,zerolinecolor='#FFFFFF',tickangle = 30),
                            yaxis=dict(showgrid=False,showline=False,zerolinecolor='#FFFFFF',tickangle = 0)
                             , bargap=0.5,bargroupgap=0.2
                             ,legend=dict(
                                         orientation="h",
                                         yanchor="bottom",
                                         y=1.02,
                                         xanchor="right",
                                         x=0.95
                                       )
                    )
    f17.layout.xaxis.fixedrange = True
    f17.layout.yaxis.fixedrange = True
    ###########################################################################
    color_gender_bar = ['rgba(246, 78, 139, 0.6)','rgba(246, 78, 139, 1.0)','rgb(153, 187, 255)','rgb(102, 153, 255)']

    f18 = go.Figure()
    
    f18.add_trace(go.Bar(
                x=["Brand 1","Brand 2","Brand 3","Brand 4","Brand 5","Brand 6","Brand 7","Brand 8","Brand 9","Brand 10"],
                y=[7030,141262,116124,97453,79637,80559,106122,100971,70725,3999],
                name='Male Coins Catch',
                text=[7030,141262,116124,97453,79637,80559,106122,100971,70725,3999],
                textposition='outside',
                texttemplate = '%{y:.2s}',
                #orientation='h',
                marker=dict(
                    color=color_gender_bar[2],
                    line=dict(color=color_gender_bar[3], width=3)
                )
            ))
    f18.add_trace(go.Bar(
                x=["Brand 1","Brand 2","Brand 3","Brand 4","Brand 5","Brand 6","Brand 7","Brand 8","Brand 9","Brand 10"],
                y=[8385,168959,141037,120970,121092,87792,141016,97149,106896,7034],
                name='Female Coins Catch',
                text=[8385,168959,141037,120970,121092,87792,141016,97149,106896,7034],
                textposition='outside',
                texttemplate = '%{y:.2s}',
                #orientation='h',
                marker=dict(
                    color=color_gender_bar[0],
                    line=dict(color=color_gender_bar[1], width=3)
                )
            ))
    
    f18.update_layout(autosize=False,barmode='group',
                                 width=800, height=500, margin=dict(l=20, r=20, b=20, t=30), # left , right , bottom , top
                                 paper_bgcolor="#FFFFFF",plot_bgcolor="#FFFFFF", font={'size': 15},
                                 bargap=0.5,bargroupgap=0.2,
                                 xaxis=dict(showgrid=False,showline=False,zerolinecolor='#FFFFFF'),
                                 yaxis=dict(showgrid=False,showline=False,zerolinecolor='#FFFFFF'),
                                                     #xaxis_title="Brands",
                                                     yaxis_title="Number of Coin Catch"
                                                     ,legend=dict(
                                                                 orientation="h",
                                                                 yanchor="bottom",
                                                                 y=1.02,
                                                                 xanchor="right",
                                                                 x=0.95
                                                               ))
    f18.layout.xaxis.fixedrange = True
    f18.layout.yaxis.fixedrange = True
    ###########################################################################
    
    color1=['#545BFA','#34D98C','#F0E746','#D96D34','#CF3DFC']
    f19 = go.Figure(data=[
            go.Bar(name='Age 7-16', x=["Brand 1","Brand 2","Brand 3","Brand 4","Brand 5","Brand 6","Brand 7","Brand 8","Brand 9","Brand 10"],
                   y=[1007,31694,27994,21608,16334,16422,21154,20668,14279,477],
                   marker=dict(color=color1[0]),width=0.1),
            go.Bar(name='Age 17-30', x=["Brand 1","Brand 2","Brand 3","Brand 4","Brand 5","Brand 6","Brand 7","Brand 8","Brand 9","Brand 10"],
                   y=[7053,170538,137777,119761,92603,95044,150549,112735,102997,5456],
                   marker=dict(color=color1[1]),width=0.1),
            go.Bar(name='Age 31-40', x=["Brand 1","Brand 2","Brand 3","Brand 4","Brand 5","Brand 6","Brand 7","Brand 8","Brand 9","Brand 10"],
                   y=[3148,67237,54135,50979,68299,37234,48993,43943,40861,3025],
                   marker=dict(color=color1[2]),width=0.1),
            go.Bar(name='Age 41-50', x=["Brand 1","Brand 2","Brand 3","Brand 4","Brand 5","Brand 6","Brand 7","Brand 8","Brand 9","Brand 10"],
                   y=[1196,20068,14039,12272,11624,7585,11020,9706,7943,313],
                   marker=dict(color=color1[3]),width=0.1),
            go.Bar(name='Age 51-80', x=["Brand 1","Brand 2","Brand 3","Brand 4","Brand 5","Brand 6","Brand 7","Brand 8","Brand 9","Brand 10"],
                   y=[3092,10682,22012,12078,10901,11446,11687,10686,10331,1735],
                   marker=dict(color=color1[4]),width=0.1)
        ])
    
    f19.update_layout(barmode='group',autosize=False,
                                         width=1000, height=500, margin=dict(l=20, r=20, b=20, t=30), # left , right , bottom , top
                                         paper_bgcolor="#FFFFFF",plot_bgcolor="#FFFFFF", font={'size': 15},
                                 xaxis=dict(showgrid=False,showline=False,zerolinecolor='#FFFFFF',tickangle = 50),
                              yaxis=dict(showgrid=False,showline=False,zerolinecolor='#FFFFFF')
                             , bargap=0.5,bargroupgap=0,
                                                 #xaxis_title="Brands",
                                                 yaxis_title="Number of Coin Catch"
                                                 ,legend=dict(
                                                             orientation="h",
                                                             yanchor="bottom",
                                                             y=1.02,
                                                             xanchor="right",
                                                             x=0.95
                                                           ))
    f19.layout.xaxis.fixedrange = True
    f19.layout.yaxis.fixedrange = True
    ###########################################################################
    f20= go.Figure(data=[
    
    go.Bar(name='Smile Available', x=["Brand 1","Brand 2","Brand 3","Brand 4","Brand 5","Brand 6","Brand 7","Brand 8","Brand 9","Brand 10"], 
                   y=[4909,3158,38343,41074,42368,113249,41178,42830,42827,8893]
                   ,marker=dict(
                            color='#83d5e2')
                  ),
    go.Bar(name='Smile Consumed', x=["Brand 1","Brand 2","Brand 3","Brand 4","Brand 5","Brand 6","Brand 7","Brand 8","Brand 9","Brand 10"],
                   y=[1657,30462,25289,21553,20238,17091,24438,19855,17661,1107],
                   marker=dict(
                            color='#596B6E')
                  ),
    
        ])
    
    f20.update_layout(barmode='group',autosize=False,
                                 width=800, height=500, margin=dict(l=20, r=20, b=20, t=30), # left , right , bottom , top
                                paper_bgcolor="#FFFFFF",plot_bgcolor="#FFFFFF", font={'size': 15},
                            xaxis=dict(showgrid=False,showline=False,zerolinecolor='#FFFFFF',tickangle = 50),
                            yaxis=dict(showgrid=False,showline=False,zerolinecolor='#FFFFFF')
                             , bargap=0.5,bargroupgap=0.2
                             ,legend=dict(
                                         orientation="h",
                                         yanchor="bottom",
                                         y=1.02,
                                         xanchor="right",
                                         x=0.95
                                       )
                    ) 
    f20.layout.xaxis.fixedrange = True
    f20.layout.yaxis.fixedrange = True
    ###########################################################################
    color_gender_bar = ['rgba(246, 78, 139, 0.6)','rgba(246, 78, 139, 1.0)','rgb(153, 187, 255)','rgb(102, 153, 255)']

    f21 = go.Figure()
    
    f21.add_trace(go.Bar(
                x=["Brand 1","Brand 2","Brand 3","Brand 4","Brand 5","Brand 6","Brand 7","Brand 8","Brand 9","Brand 10"],
                y=[7030,141262,116124,97453,79637,80559,106122,100971,70725,3999],
                name='Male Smiley Catch',
                text=[7030,141262,116124,97453,79637,80559,106122,100971,70725,3999],
                textposition='outside',
                texttemplate = '%{y:.2s}',
                #orientation='h',
                marker=dict(
                    color=color_gender_bar[2],
                    line=dict(color=color_gender_bar[3], width=3)
                )
            ))
    f21.add_trace(go.Bar(
                x=["Brand 1","Brand 2","Brand 3","Brand 4","Brand 5","Brand 6","Brand 7","Brand 8","Brand 9","Brand 10"],
                y=[8385,168959,141037,120970,121092,87792,141016,97149,106896,7034],
                name='Female Smiley Catch',
                text=[8385,168959,141037,120970,121092,87792,141016,97149,106896,7034],
                textposition='outside',
                texttemplate = '%{y:.2s}',
                marker=dict(
                    color=color_gender_bar[0],
                    line=dict(color=color_gender_bar[1], width=3)
                )
            ))
    
    f21.update_layout(autosize=False,barmode='group',
                                 width=800, height=500, margin=dict(l=20, r=20, b=20, t=30), # left , right , bottom , top
                                 paper_bgcolor="#FFFFFF",plot_bgcolor="#FFFFFF", font={'size': 15},
                                 bargap=0.5,bargroupgap=0.2,
                                 xaxis=dict(showgrid=False,showline=False,zerolinecolor='#FFFFFF'),
                                 yaxis=dict(showgrid=False,showline=False,zerolinecolor='#FFFFFF'),
                                                     #xaxis_title="Brands",
                                                     yaxis_title="Number of Coin Catch"
                                                     ,legend=dict(
                                                                 orientation="h",
                                                                 yanchor="bottom",
                                                                 y=1.02,
                                                                 xanchor="right",
                                                                 x=0.95
                                                               ))
    f21.layout.xaxis.fixedrange = True
    f21.layout.yaxis.fixedrange = True
    ###########################################################################
    color1=['#545BFA','#34D98C','#F0E746','#D96D34','#CF3DFC']
    f22 = go.Figure(data=[
           go.Bar(name='Age 7-16', x=["Brand 1","Brand 2","Brand 3","Brand 4","Brand 5","Brand 6","Brand 7","Brand 8","Brand 9","Brand 10"],
                  y=[1007,31694,27994,21608,16334,16422,21154,20668,14279,477],
                  marker=dict(color=color1[0]),width=0.1),
           go.Bar(name='Age 17-30', x=["Brand 1","Brand 2","Brand 3","Brand 4","Brand 5","Brand 6","Brand 7","Brand 8","Brand 9","Brand 10"],
                  y=[7053,170538,137777,119761,92603,95044,150549,112735,102997,5456],
                  marker=dict(color=color1[1]),width=0.1),
           go.Bar(name='Age 31-40', x=["Brand 1","Brand 2","Brand 3","Brand 4","Brand 5","Brand 6","Brand 7","Brand 8","Brand 9","Brand 10"],
                  y=[3148,67237,54135,50979,68299,37234,48993,43943,40861,3025],
                  marker=dict(color=color1[2]),width=0.1),
           go.Bar(name='Age 41-50', x=["Brand 1","Brand 2","Brand 3","Brand 4","Brand 5","Brand 6","Brand 7","Brand 8","Brand 9","Brand 10"],
                  y=[1196,20068,14039,12272,11624,7585,11020,9706,7943,313],
                  marker=dict(color=color1[3]),width=0.1),
           go.Bar(name='Age 51-80', x=["Brand 1","Brand 2","Brand 3","Brand 4","Brand 5","Brand 6","Brand 7","Brand 8","Brand 9","Brand 10"],
                  y=[3092,10682,22012,12078,10901,11446,11687,10686,10331,1735],
                  marker=dict(color=color1[4]),width=0.1)
        ])
    # Change the bar mode
    f22.update_layout(barmode='group',autosize=False,
                                         width=1000, height=500, margin=dict(l=20, r=20, b=20, t=30), # left , right , bottom , top
                                         paper_bgcolor="#FFFFFF",plot_bgcolor="#FFFFFF", font={'size': 15},
                                 xaxis=dict(showgrid=False,showline=False,zerolinecolor='#FFFFFF',tickangle = 50),
                              yaxis=dict(showgrid=False,showline=False,zerolinecolor='#FFFFFF')
                             , bargap=0.5,bargroupgap=0,
                                                 #xaxis_title="Brands",
                                                 yaxis_title="Number of Coin Catch"
                                                 ,legend=dict(
                                                             orientation="h",
                                                             yanchor="bottom",
                                                             y=1.02,
                                                             xanchor="right",
                                                             x=0.95
                                                           ))
    f22.layout.xaxis.fixedrange = True
    f22.layout.yaxis.fixedrange = True
    ###########################################################################
    f23 = go.Figure(data=[
     

     
    go.Bar(name='Gift Available', x=["Brand 1","Brand 2","Brand 3","Brand 4","Brand 5","Brand 6","Brand 7","Brand 8","Brand 9","Brand 10"], 
                   y=[4909,3158,38343,41074,42368,113249,41178,42830,42827,8893]
                   ,marker=dict(
                            color='#F28988')
                  ),
    go.Bar(name='Gift Consumed', x=["Brand 1","Brand 2","Brand 3","Brand 4","Brand 5","Brand 6","Brand 7","Brand 8","Brand 9","Brand 10"], 
                   y=[1657,30462,25289,21553,20238,17091,24438,19855,17661,1107]
                   ,marker=dict(
                            color='#744241')
                   )
        ])
    #    # Change the bar mode
    f23.update_layout(barmode='group',autosize=False,
                                 width=800, height=500, margin=dict(l=20, r=20, b=20, t=30), # left , right , bottom , top
                                paper_bgcolor="#FFFFFF",plot_bgcolor="#FFFFFF", font={'size': 15},
                            xaxis=dict(showgrid=False,showline=False,zerolinecolor='#FFFFFF',tickangle = 50),
                            yaxis=dict(showgrid=False,showline=False,zerolinecolor='#FFFFFF')
                             , bargap=0.5,bargroupgap=0.2
                             ,legend=dict(
                                         orientation="h",
                                         yanchor="bottom",
                                         y=1.02,
                                         xanchor="right",
                                         x=0.95
                                       )
                    ) 
    f23.layout.xaxis.fixedrange = True
    f23.layout.yaxis.fixedrange = True
    ###########################################################################
    color_gender_bar = ['rgba(246, 78, 139, 0.6)','rgba(246, 78, 139, 1.0)','rgb(153, 187, 255)','rgb(102, 153, 255)']

    f24 = go.Figure()
    
    f24.add_trace(go.Bar(
                x=["Brand 1","Brand 2","Brand 3","Brand 4","Brand 5","Brand 6","Brand 7","Brand 8","Brand 9","Brand 10"],
                y=[7030,141262,116124,97453,79637,80559,106122,100971,70725,3999],
                name='Male Gift Catch',
                text=[7030,141262,116124,97453,79637,80559,106122,100971,70725,3999],
                textposition='outside',
                texttemplate = '%{y:.2s}',
                marker=dict(
                    color=color_gender_bar[2],
                    line=dict(color=color_gender_bar[3], width=3)
                )
            ))
    f24.add_trace(go.Bar(
                x=["Brand 1","Brand 2","Brand 3","Brand 4","Brand 5","Brand 6","Brand 7","Brand 8","Brand 9","Brand 10"],
                y=[8385,168959,141037,120970,121092,87792,141016,97149,106896,7034],
                name='Female Gift Catch',
                text=[8385,168959,141037,120970,121092,87792,141016,97149,106896,7034],
                textposition='outside',
                texttemplate = '%{y:.2s}',
                marker=dict(
                    color=color_gender_bar[0],
                    line=dict(color=color_gender_bar[1], width=3)
                )
            ))
    
    f24.update_layout(autosize=False,barmode='group',
                                 width=800, height=500, margin=dict(l=20, r=20, b=20, t=30), # left , right , bottom , top
                                 paper_bgcolor="#FFFFFF",plot_bgcolor="#FFFFFF", font={'size': 15},
                                 bargap=0.5,bargroupgap=0.2,
                                 xaxis=dict(showgrid=False,showline=False,zerolinecolor='#FFFFFF'),
                                 yaxis=dict(showgrid=False,showline=False,zerolinecolor='#FFFFFF'),
                                                     #xaxis_title="Brands",
                                                     yaxis_title="Number of Coin Catch"
                                                     ,legend=dict(
                                                                 orientation="h",
                                                                 yanchor="bottom",
                                                                 y=1.02,
                                                                 xanchor="right",
                                                                 x=0.95
                                                               ))
    f24.layout.xaxis.fixedrange = True
    f24.layout.yaxis.fixedrange = True
    ###########################################################################
    color1=['#545BFA','#34D98C','#F0E746','#D96D34','#CF3DFC']
    f25 = go.Figure(data=[
           go.Bar(name='Age 7-16', x=["Brand 1","Brand 2","Brand 3","Brand 4","Brand 5","Brand 6","Brand 7","Brand 8","Brand 9","Brand 10"],
                  y=[1007,31694,27994,21608,16334,16422,21154,20668,14279,477],
                  marker=dict(color=color1[0]),width=0.1),
           go.Bar(name='Age 17-30', x=["Brand 1","Brand 2","Brand 3","Brand 4","Brand 5","Brand 6","Brand 7","Brand 8","Brand 9","Brand 10"],
                  y=[7053,170538,137777,119761,92603,95044,150549,112735,102997,5456],
                  marker=dict(color=color1[1]),width=0.1),
           go.Bar(name='Age 31-40', x=["Brand 1","Brand 2","Brand 3","Brand 4","Brand 5","Brand 6","Brand 7","Brand 8","Brand 9","Brand 10"],
                  y=[3148,67237,54135,50979,68299,37234,48993,43943,40861,3025],
                  marker=dict(color=color1[2]),width=0.1),
           go.Bar(name='Age 41-50', x=["Brand 1","Brand 2","Brand 3","Brand 4","Brand 5","Brand 6","Brand 7","Brand 8","Brand 9","Brand 10"],
                  y=[1196,20068,14039,12272,11624,7585,11020,9706,7943,313],
                  marker=dict(color=color1[3]),width=0.1),
           go.Bar(name='Age 51-80', x=["Brand 1","Brand 2","Brand 3","Brand 4","Brand 5","Brand 6","Brand 7","Brand 8","Brand 9","Brand 10"],
                  y=[3092,10682,22012,12078,10901,11446,11687,10686,10331,1735],
                  marker=dict(color=color1[4]),width=0.1)
        ])
    # Change the bar mode
    f25.update_layout(barmode='group',autosize=False,
                                         width=1000, height=500, margin=dict(l=20, r=20, b=20, t=30), # left , right , bottom , top
                                         paper_bgcolor="#FFFFFF",plot_bgcolor="#FFFFFF", font={'size': 15},
                                 xaxis=dict(showgrid=False,showline=False,zerolinecolor='#FFFFFF',tickangle = 50),
                              yaxis=dict(showgrid=False,showline=False,zerolinecolor='#FFFFFF')
                             , bargap=0.5,bargroupgap=0,
                                                 #xaxis_title="Brands",
                                                 yaxis_title="Number of Coin Catch"
                                                 ,legend=dict(
                                                             orientation="h",
                                                             yanchor="bottom",
                                                             y=1.02,
                                                             xanchor="right",
                                                             x=0.95
                                                           ))
    f25.layout.xaxis.fixedrange = True
    f25.layout.yaxis.fixedrange = True
    ###########################################################################
    
    merchant = [f1,f2,f4,f5,f6,f7,f8,f9,f10,f11,f12,f13,f14,f15,f16,f17,f18,f19,f20,f21,f22,f23,f24,f25]
    
    return merchant

def campaigns_charts():
    
    name_fig = go.Figure()

    name_fig.add_trace(go.Pie(labels=['active'], values=[200], hole=.85,hoverinfo='skip', textinfo='none'
                             ,showlegend=False,marker=dict(colors=['#81DB27'])))
    
    name_fig.update_layout(autosize=False,paper_bgcolor="#FFFFFF", plot_bgcolor="#FFFFFF",
                               width=1000, height=250, margin=dict(l=20, r=20, b=20, t=50),
                              xaxis=dict(showgrid=False,showline=False,showticklabels=False,zerolinecolor='#FFFFFF'),
                          yaxis=dict(showgrid=False,showline=False,showticklabels=False,zerolinecolor='#FFFFFF'),title={
                                                  'text': 'Brand 1',
                                                  'y':0.5,
                                                  'x':0.5,
                                                  'xanchor': 'center',
                                                  'yanchor': 'top'})
    
    state_fig = go.Figure()

    state_fig.add_trace(go.Pie(labels=['active'], values=[200], hole=.85,hoverinfo='skip', textinfo='none'
                                 ,showlegend=False,marker=dict(colors=['#81DB27'])))
        
    state_fig.update_layout(autosize=False,paper_bgcolor="#FFFFFF", plot_bgcolor="#FFFFFF",
                                   width=1000, height=250, margin=dict(l=20, r=20, b=20, t=50),
                                  xaxis=dict(showgrid=False,showline=False,showticklabels=False,zerolinecolor='#FFFFFF'),
                              yaxis=dict(showgrid=False,showline=False,showticklabels=False,zerolinecolor='#FFFFFF'),title={
                                                      'text': 'Active',
                                                      'y':0.5,
                                                      'x':0.5,
                                                      'xanchor': 'center',
                                                      'yanchor': 'top'})
        
    

    pie_gender = go.Figure(data=[go.Pie(labels=['Male', 'Female'], values=[272600,41800], hole=.85)])
    pie_gender.update_layout(
            annotations=[dict(text='Gender', x=0.50, y=0.50, font_size=25, showarrow=False)])
    pie_gender.update_traces(marker=dict(colors=['rgb(153, 187, 255)','rgba(246, 78, 139, 0.6)']),showlegend=True,textinfo='label+percent')
    pie_gender.update_layout(autosize=False,
                             margin=dict(l=20, r=20, b=20, t=30), 
                             paper_bgcolor="#FFFFFF",plot_bgcolor="#FFFFFF", font={'size': 18},legend=dict(
                                         orientation="h",
                                         yanchor="bottom",
                                         y=1.02,
                                         xanchor="right",
                                         x=0.95
                                       ))
    
    ###########################################################################
    
    ind_gender = go.Figure()

    ind_gender.add_trace(go.Indicator(
                title = {'text': "<b>Male</b><br>"
                         ,"font": {"size": 40, 'color': "#0F4C75"}},
                mode = "number",
                value = 27260,
                number={"font": {"size": 40, 'color': "#6699ff"}},
                domain = {'row': 0, 'column': 0}))    
    ind_gender.add_trace(go.Indicator(
                title = {'text': "<b>Female</b><br>"
                         ,"font": {"size": 40, 'color': "#0F4C75"}},
                mode = "number",
                value = 41800,
                number={"font": {"size": 40, 'color': "#f64e8b"}},
                domain = {'row': 0, 'column': 1}))
    
    ind_gender.update_layout(
                grid = {'rows': 1, 'columns': 2, 'pattern': "independent"})
    ind_gender.update_layout(height=200,autosize=False,paper_bgcolor="#FFFFFF", plot_bgcolor="#FFFFFF", margin=dict(l=20, r=20, b=20, t=65))
    
    ###########################################################################
    
    pie_age = go.Figure(data=[go.Pie(labels=['AGE 7-16','AGE 17-30','AGE 31-40','AGE 41-50','AGE 51-80'], 
                                     values=[5880,31900,23400,3720,3940], hole=.85)])
    pie_age.update_layout(
                    annotations=[dict(text='Age Group', x=0.50, y=0.50, font_size=25, showarrow=False)])
    pie_age.update_traces(marker=dict(colors=['#545BFA','#34D98C','#F0E746','#D96D34','#CF3DFC']),showlegend=True)
    pie_age.update_layout(autosize=False,
                                 margin=dict(l=20, r=20, b=20, t=30), # left , right , bottom , top
                                 paper_bgcolor="#FFFFFF",plot_bgcolor="#FFFFFF", font={'size': 18},legend=dict(
                                             orientation="h",
                                             yanchor="bottom",
                                             y=1.02,
                                             xanchor="right",
                                             x=0.95
                                           ))
    
    ###########################################################################
    ind_age = go.Figure()

    ind_age.add_trace(go.Indicator(
                title = {'text': "<b>AGE 7-16</b><br>"
                         ,"font": {"size": 15, 'color': "#31333F"}},
                mode = "number",
                value = 5880,
                number={"font": {"size": 30, 'color': "#545BFA"}},
                domain = {'row': 0, 'column': 0})) 
        
    ind_age.add_trace(go.Indicator(
                title = {'text': "<b>AGE 17-30</b><br>"
                         ,"font": {"size": 15, 'color': "#31333F"}},
                mode = "number",
                value = 31900,
                number={"font": {"size": 30, 'color': "#34D98C"}},
                domain = {'row': 0, 'column': 1}))
    ind_age.add_trace(go.Indicator(
                title = {'text': "<b>AGE 31-40</b><br>"
                         ,"font": {"size": 15, 'color': "#31333F"}},
                mode = "number",
                value = 23400,
                number={"font": {"size": 30, 'color': "#F0E746"}},
                domain = {'row': 0, 'column': 2}))    
  
    ind_age.add_trace(go.Indicator(
                  title = {'text': "<b>AGE 41-50</b><br>"
                           ,"font": {"size": 15, 'color': "#31333F"}},
                  mode = "number",
                  value = 3720,
                  number={"font": {"size": 30, 'color': "#D96D34"}},
                  domain = {'row': 0, 'column': 3}))
    ind_age.add_trace(go.Indicator(
                  title = {'text': "<b>AGE 51-80</b><br>"
                           ,"font": {"size": 15, 'color': "#31333F"}},
                  mode = "number",
                  value = 3940,
                  number={"font": {"size": 30, 'color': "#CF3DFC"}},
                  domain = {'row': 0, 'column': 4}))   
    ind_age.update_layout(
                  grid = {'rows': 1, 'columns': 5, 'pattern': "independent"})
    ind_age.update_layout(height=200,autosize=False,paper_bgcolor="#FFFFFF", plot_bgcolor="#FFFFFF", margin=dict(l=20, r=20, b=20, t=65))
    
    ###########################################################################
    ind_players = go.Figure()

    
    ind_players.add_trace(go.Indicator(
            mode = "number",
            number = {"font": {"size": 40,'color': "#31333F"}},
            value = 69000,
            title = {"text": 'No. Players',"font": {"size": 15, 'color': "#31333F"}}
            ,domain = {'y': [0.5, 0.5], 'x': [0.5, 0.5]}
            ))
    ind_players.add_trace(go.Pie(labels=['active'], values=[200], hole=.85,hoverinfo='skip', textinfo='none'
                             ,showlegend=False,marker=dict(colors=['#ffad33'])))
    
    ind_players.update_layout(autosize=False,paper_bgcolor="#FFFFFF", plot_bgcolor="#FFFFFF",
                               width=1000, height=250, margin=dict(l=20, r=20, b=20, t=50),
                              xaxis=dict(showgrid=False,showline=False,showticklabels=False,zerolinecolor='#FFFFFF'),
                          yaxis=dict(showgrid=False,showline=False,showticklabels=False,zerolinecolor='#FFFFFF'))
    
    ###########################################################################     


    pie_coins = go.Figure(data=[go.Pie(labels=['Coin Available', 'Coin Consumed'], values=[42400,20240], hole=.85)])
    pie_coins.update_layout(
            annotations=[dict(text='Coins Catches', x=0.50, y=0.50, font_size=25, showarrow=False)])
    pie_coins.update_traces(marker=dict(colors=['#CCAD00','#6E5D00']),showlegend=True,textinfo='label+percent')
    pie_coins.update_layout(height=350,autosize=False,
                             margin=dict(l=20, r=20, b=20, t=30), # left , right , bottom , top
                             paper_bgcolor="#FFFFFF",plot_bgcolor="#FFFFFF", font={'size': 18},legend=dict(
                                         #orientation="h",
                                         yanchor="bottom",
                                         y=1.02,
                                         xanchor="right",
                                         x=0.95
                                       ))
    
    ind_coins = go.Figure()

    ind_coins.add_trace(go.Indicator(
                title = {'text': "<b>Coin Available</b><br>"
                         ,"font": {"size": 20, 'color': "#CCAD00"}},
                mode = "number",
                value = 42400,
                number={"font": {"size": 40, 'color': "#31333F"}},
                domain = {'row': 0, 'column': 0}))    
    ind_coins.add_trace(go.Indicator(
                title = {'text': "<b>Coin Consumed</b><br>"
                         ,"font": {"size": 20, 'color': "#6E5D00"}},
                mode = "number",
                value = 20240,
                number={"font": {"size": 40, 'color': "#31333F"}},
                domain = {'row': 0, 'column': 1}))
    
    ind_coins.update_layout(
                grid = {'rows': 1, 'columns': 2, 'pattern': "independent"})
    ind_coins.update_layout(height=200,autosize=False,paper_bgcolor="#FFFFFF", plot_bgcolor="#FFFFFF", margin=dict(l=20, r=20, b=20, t=65))
    ###########################################################################
    

    pie_smiley = go.Figure(data=[go.Pie(labels=['Smiley Available', 'Smiley Consumed'], values=[84400,40800], hole=.85)])
    pie_smiley.update_layout(
            annotations=[dict(text='Smiley Catches', x=0.50, y=0.50, font_size=25, showarrow=False)])
    pie_smiley.update_traces(marker=dict(colors=['#83d5e2','#596B6E']),showlegend=True,textinfo='label+percent')
    pie_smiley.update_layout(height=350,autosize=False,
                             margin=dict(l=20, r=20, b=20, t=30), 
                             paper_bgcolor="#FFFFFF",plot_bgcolor="#FFFFFF", font={'size': 18},legend=dict(
                                         yanchor="bottom",
                                         y=1.02,
                                         xanchor="right",
                                         x=0.95
                                       ))
    
    ind_smiley = go.Figure()

    ind_smiley.add_trace(go.Indicator(
                title = {'text': "<b>Smiley Available</b><br>"
                         ,"font": {"size": 20, 'color': "#83d5e2"}},
                mode = "number",
                value = 84400,
                number={"font": {"size": 40, 'color': "#31333F"}},
                domain = {'row': 0, 'column': 0}))    
    ind_smiley.add_trace(go.Indicator(
                title = {'text': "<b>Smiley Consumed</b><br>"
                         ,"font": {"size": 20, 'color': "#596B6E"}},
                mode = "number",
                value = 40800,
                number={"font": {"size": 40, 'color': "#31333F"}},
                domain = {'row': 0, 'column': 1}))
    
    ind_smiley.update_layout(
                grid = {'rows': 1, 'columns': 2, 'pattern': "independent"})
    ind_smiley.update_layout(height=200,autosize=False,paper_bgcolor="#FFFFFF", plot_bgcolor="#FFFFFF", margin=dict(l=20, r=20, b=20, t=65))
    ###########################################################################
    
    pie_gift = go.Figure(data=[go.Pie(labels=['Gifts Available', 'Gifts Consumed'], values=[68,43], hole=.85)])
    pie_gift.update_layout(
            annotations=[dict(text='Gifts Catches', x=0.50, y=0.50, font_size=25, showarrow=False)])
    pie_gift.update_traces(marker=dict(colors=['#F28988','#744241']),showlegend=True,textinfo='label+percent')
    pie_gift.update_layout(height=350,autosize=False,
                             margin=dict(l=20, r=20, b=20, t=30), 
                             paper_bgcolor="#FFFFFF",plot_bgcolor="#FFFFFF", font={'size': 18},legend=dict(
                                         yanchor="bottom",
                                         y=1.02,
                                         xanchor="right",
                                         x=0.95
                                       ))
    
    ###########################################################################
    ind_gift = go.Figure()

    ind_gift.add_trace(go.Indicator(
                title = {'text': "<b>Gifts Available</b><br>"
                         ,"font": {"size": 20, 'color': "#F28988"}},
                mode = "number",
                value = 68,
                number={"font": {"size": 40, 'color': "#31333F"}},
                domain = {'row': 0, 'column': 0}))    
    ind_gift.add_trace(go.Indicator(
                title = {'text': "<b>Gifts Consumed</b><br>"
                         ,"font": {"size": 20, 'color': "#744241"}},
                mode = "number",
                value = 43,
                number={"font": {"size": 40, 'color': "#31333F"}},
                domain = {'row': 0, 'column': 1}))
    
    ind_gift.update_layout(
                grid = {'rows': 1, 'columns': 2, 'pattern': "independent"})
    ind_gift.update_layout(height=200,autosize=False,paper_bgcolor="#FFFFFF", plot_bgcolor="#FFFFFF", margin=dict(l=20, r=20, b=20, t=65))
    ########################Coins Gender#######################################
    
    

    pie_coins_gender = go.Figure(data=[go.Pie(labels=['Male Coins Catch', 'Female Coins Catch'], values=[79600,121100], hole=.85)])
    pie_coins_gender.update_layout(
            annotations=[dict(text='Gender', x=0.50, y=0.50, font_size=25, showarrow=False)])
    pie_coins_gender.update_traces(marker=dict(colors=['rgb(153, 187, 255)','rgba(246, 78, 139, 0.6)']),showlegend=True,textinfo='label+percent')
    pie_coins_gender.update_layout(height=350,autosize=False,
                             margin=dict(l=20, r=20, b=20, t=30), 
                             paper_bgcolor="#FFFFFF",plot_bgcolor="#FFFFFF", font={'size': 18},legend=dict(
                                         yanchor="bottom",
                                         y=1.02,
                                         xanchor="right",
                                         x=0.95
                                       ))
    
    ###########################################################################
    
    ind_coins_gender = go.Figure()

    ind_coins_gender.add_trace(go.Indicator(
                title = {'text': "<b>Male Coins Catch</b><br>"
                         ,"font": {"size": 20, 'color': "#0F4C75"}},
                mode = "number",
                value = 79600,
                number={"font": {"size": 40, 'color': "#6699ff"}},
                domain = {'row': 0, 'column': 0}))    
    ind_coins_gender.add_trace(go.Indicator(
                title = {'text': "<b>Female Coins Catch</b><br>"
                         ,"font": {"size": 20, 'color': "#0F4C75"}},
                mode = "number",
                value = 121100,
                number={"font": {"size": 40, 'color': "#f64e8b"}},
                domain = {'row': 0, 'column': 1}))  
    
    ind_coins_gender.update_layout(
                grid = {'rows': 1, 'columns': 2, 'pattern': "independent"})
    ind_coins_gender.update_layout(height=200,autosize=False,paper_bgcolor="#FFFFFF", plot_bgcolor="#FFFFFF", margin=dict(l=20, r=20, b=20, t=65))
    #########################Coins Age ########################################
    
    pie_coins_age = go.Figure(data=[go.Pie(labels=['AGE 7-16','AGE 17-30','AGE 31-40','AGE 41-50','AGE 51-80'], 
                                           values=[16330,92600,68300,11620,10600], hole=.85)])
    pie_coins_age.update_layout(
                    annotations=[dict(text='Age Group', x=0.50, y=0.50, font_size=25, showarrow=False)])
    pie_coins_age.update_traces(marker=dict(colors=['#545BFA','#34D98C','#F0E746','#D96D34','#CF3DFC']),showlegend=True)
    pie_coins_age.update_layout(autosize=False,
                                 margin=dict(l=20, r=20, b=20, t=30), # left , right , bottom , top
                                 paper_bgcolor="#FFFFFF",plot_bgcolor="#FFFFFF", font={'size': 18},legend=dict(
                                             orientation="h",
                                             yanchor="bottom",
                                             y=1.02,
                                             xanchor="right",
                                             x=0.95
                                           ))
    
    
    ind_coins_age = go.Figure()

    ind_coins_age.add_trace(go.Indicator(
                title = {'text': "<b>AGE 7-16</b><br>"
                         ,"font": {"size": 15, 'color': "#31333F"}},
                mode = "number",
                value = 16330,
                number={"font": {"size": 30, 'color': "#545BFA"}},
                domain = {'row': 0, 'column': 0})) 
        
    ind_coins_age.add_trace(go.Indicator(
                title = {'text': "<b>AGE 17-30</b><br>"
                         ,"font": {"size": 15, 'color': "#31333F"}},
                mode = "number",
                value = 92600,
                number={"font": {"size": 30, 'color': "#34D98C"}},
                domain = {'row': 0, 'column': 1}))
    ind_coins_age.add_trace(go.Indicator(
                title = {'text': "<b>AGE 31-40</b><br>"
                         ,"font": {"size": 15, 'color': "#31333F"}},
                mode = "number",
                value = 68300,
                number={"font": {"size": 30, 'color': "#F0E746"}},
                domain = {'row': 0, 'column': 2}))    
  
    ind_coins_age.add_trace(go.Indicator(
                  title = {'text': "<b>AGE 41-50</b><br>"
                           ,"font": {"size": 15, 'color': "#31333F"}},
                  mode = "number",
                  value = 11620,
                  number={"font": {"size": 30, 'color': "#D96D34"}},
                  domain = {'row': 0, 'column': 3}))
    ind_coins_age.add_trace(go.Indicator(
                  title = {'text': "<b>AGE 51-80</b><br>"
                           ,"font": {"size": 15, 'color': "#31333F"}},
                  mode = "number",
                  value = 10600,
                  number={"font": {"size": 30, 'color': "#CF3DFC"}},
                  domain = {'row': 0, 'column': 4}))   
    ind_coins_age.update_layout(
                  grid = {'rows': 1, 'columns': 5, 'pattern': "independent"})
    ind_coins_age.update_layout(height=200,autosize=False,paper_bgcolor="#FFFFFF", plot_bgcolor="#FFFFFF", margin=dict(l=20, r=20, b=20, t=65))
    
    #########################Smiley Gender#####################################
    

    pie_smiley_gender = go.Figure(data=[go.Pie(labels=['Male Smiley Catch', 'Female Smiley Catch'], values=[174300,261700], hole=.85)])
    pie_smiley_gender.update_layout(
            annotations=[dict(text='Gender', x=0.50, y=0.50, font_size=25, showarrow=False)])
    pie_smiley_gender.update_traces(marker=dict(colors=['rgb(153, 187, 255)','rgba(246, 78, 139, 0.6)']),showlegend=True,textinfo='label+percent')
    pie_smiley_gender.update_layout(height=350,autosize=False,
                             margin=dict(l=20, r=20, b=20, t=30), 
                             paper_bgcolor="#FFFFFF",plot_bgcolor="#FFFFFF", font={'size': 18},legend=dict(
                                         yanchor="bottom",
                                         y=1.02,
                                         xanchor="right",
                                         x=0.95
                                       ))
      
    ind_smiley_gender = go.Figure()

    ind_smiley_gender.add_trace(go.Indicator(
                title = {'text': "<b>Male Coins Catch</b><br>"
                         ,"font": {"size": 20, 'color': "#0F4C75"}},
                mode = "number",
                value = 174300,
                number={"font": {"size": 40, 'color': "#6699ff"}},
                domain = {'row': 0, 'column': 0}))    
    ind_smiley_gender.add_trace(go.Indicator(
                title = {'text': "<b>Female Coins Catch</b><br>"
                         ,"font": {"size": 20, 'color': "#0F4C75"}},
                mode = "number",
                value = 261700,
                number={"font": {"size": 40, 'color': "#f64e8b"}},
                domain = {'row': 0, 'column': 1}))
    
    ind_smiley_gender.update_layout(
                grid = {'rows': 1, 'columns': 2, 'pattern': "independent"})
    ind_smiley_gender.update_layout(height=200,autosize=False,paper_bgcolor="#FFFFFF", plot_bgcolor="#FFFFFF", margin=dict(l=20, r=20, b=20, t=65))
    #######################Smiley Age#######################################
    
    pie_smiley_age = go.Figure(data=[go.Pie(labels=['AGE 7-16','AGE 17-30','AGE 31-40','AGE 41-50','AGE 51-80'], 
                                            values=[37000,203000,147900,22770,24600], hole=.85)])
    pie_smiley_age.update_layout(
                    annotations=[dict(text='Age Group', x=0.50, y=0.50, font_size=25, showarrow=False)])
    pie_smiley_age.update_traces(marker=dict(colors=['#545BFA','#34D98C','#F0E746','#D96D34','#CF3DFC']),showlegend=True)
    pie_smiley_age.update_layout(autosize=False,
                                 margin=dict(l=20, r=20, b=20, t=30), 
                                 paper_bgcolor="#FFFFFF",plot_bgcolor="#FFFFFF", font={'size': 18},legend=dict(
                                             orientation="h",
                                             yanchor="bottom",
                                             y=1.02,
                                             xanchor="right",
                                             x=0.95
                                           ))
    
    
    ind_smiley_age = go.Figure()

    ind_smiley_age.add_trace(go.Indicator(
                title = {'text': "<b>AGE 7-16</b><br>"
                         ,"font": {"size": 15, 'color': "#31333F"}},
                mode = "number",
                value = 37000,
                number={"font": {"size": 30, 'color': "#545BFA"}},
                domain = {'row': 0, 'column': 0})) 
        
    ind_smiley_age.add_trace(go.Indicator(
                title = {'text': "<b>AGE 17-30</b><br>"
                         ,"font": {"size": 15, 'color': "#31333F"}},
                mode = "number",
                value = 203000,
                number={"font": {"size": 30, 'color': "#34D98C"}},
                domain = {'row': 0, 'column': 1}))
    ind_smiley_age.add_trace(go.Indicator(
                title = {'text': "<b>AGE 31-40</b><br>"
                         ,"font": {"size": 15, 'color': "#31333F"}},
                mode = "number",
                value = 147900,
                number={"font": {"size": 30, 'color': "#F0E746"}},
                domain = {'row': 0, 'column': 2}))    
  
    ind_smiley_age.add_trace(go.Indicator(
                  title = {'text': "<b>AGE 41-50</b><br>"
                           ,"font": {"size": 15, 'color': "#31333F"}},
                  mode = "number",
                  value = 22770,
                  number={"font": {"size": 30, 'color': "#D96D34"}},
                  domain = {'row': 0, 'column': 3}))
    ind_smiley_age.add_trace(go.Indicator(
                  title = {'text': "<b>AGE 51-80</b><br>"
                           ,"font": {"size": 15, 'color': "#31333F"}},
                  mode = "number",
                  value = 24600,
                  number={"font": {"size": 30, 'color': "#CF3DFC"}},
                  domain = {'row': 0, 'column': 4}))   
    ind_smiley_age.update_layout(
                  grid = {'rows': 1, 'columns': 5, 'pattern': "independent"})
    ind_smiley_age.update_layout(height=200,autosize=False,paper_bgcolor="#FFFFFF", plot_bgcolor="#FFFFFF", margin=dict(l=20, r=20, b=20, t=65))
    
    #######################Gift Gender#########################################

    pie_gift_gender = go.Figure(data=[go.Pie(labels=['Male Gifts Catch', 'Female Gifts Catch'], values=[32,66], hole=.85)])
    pie_gift_gender.update_layout(
            annotations=[dict(text='Gender', x=0.50, y=0.50, font_size=25, showarrow=False)])
    pie_gift_gender.update_traces(marker=dict(colors=['rgb(153, 187, 255)','rgba(246, 78, 139, 0.6)']),showlegend=True,textinfo='label+percent')
    pie_gift_gender.update_layout(height=350,autosize=False,
                             margin=dict(l=20, r=20, b=20, t=30), 
                             paper_bgcolor="#FFFFFF",plot_bgcolor="#FFFFFF", font={'size': 18},legend=dict(
                                         yanchor="bottom",
                                         y=1.02,
                                         xanchor="right",
                                         x=0.95
                                       ))
      
    ind_gift_gender = go.Figure()

    ind_gift_gender.add_trace(go.Indicator(
                title = {'text': "<b>Male Coins Catch</b><br>"
                         ,"font": {"size": 20, 'color': "#0F4C75"}},
                mode = "number",
                value = 32,
                number={"font": {"size": 40, 'color': "#6699ff"}},
                domain = {'row': 0, 'column': 0}))    
    ind_gift_gender.add_trace(go.Indicator(
                title = {'text': "<b>Female Coins Catch</b><br>"
                         ,"font": {"size": 20, 'color': "#0F4C75"}},
                mode = "number",
                value = 66,
                number={"font": {"size": 40, 'color': "#f64e8b"}},
                domain = {'row': 0, 'column': 1}))
    
    ind_gift_gender.update_layout(
                grid = {'rows': 1, 'columns': 2, 'pattern': "independent"})
    ind_gift_gender.update_layout(height=200,autosize=False,paper_bgcolor="#FFFFFF", plot_bgcolor="#FFFFFF", margin=dict(l=20, r=20, b=20, t=65))
    #########################Gifts Age ########################################
 
    pie_gift_age = go.Figure(data=[go.Pie(labels=['AGE 7-16','AGE 17-30','AGE 31-40','AGE 41-50','AGE 51-80'], 
                                          values=[23,49,16,1,7], hole=.85)])
    pie_gift_age.update_layout(
                    annotations=[dict(text='Age Group', x=0.50, y=0.50, font_size=25, showarrow=False)])
    pie_gift_age.update_traces(marker=dict(colors=['#545BFA','#34D98C','#F0E746','#D96D34','#CF3DFC']),showlegend=True)
    pie_gift_age.update_layout(autosize=False,
                                 margin=dict(l=20, r=20, b=20, t=30), 
                                 paper_bgcolor="#FFFFFF",plot_bgcolor="#FFFFFF", font={'size': 18},legend=dict(
                                             orientation="h",
                                             yanchor="bottom",
                                             y=1.02,
                                             xanchor="right",
                                             x=0.95
                                           ))
    
    ###########################################################################
    ind_gift_age = go.Figure()

    ind_gift_age.add_trace(go.Indicator(
                title = {'text': "<b>AGE 7-16</b><br>"
                         ,"font": {"size": 15, 'color': "#31333F"}},
                mode = "number",
                value = 23,
                number={"font": {"size": 30, 'color': "#545BFA"}},
                domain = {'row': 0, 'column': 0})) 
        
    ind_gift_age.add_trace(go.Indicator(
                title = {'text': "<b>AGE 17-30</b><br>"
                         ,"font": {"size": 15, 'color': "#31333F"}},
                mode = "number",
                value = 49,
                number={"font": {"size": 30, 'color': "#34D98C"}},
                domain = {'row': 0, 'column': 1}))
    ind_gift_age.add_trace(go.Indicator(
                title = {'text': "<b>AGE 31-40</b><br>"
                         ,"font": {"size": 15, 'color': "#31333F"}},
                mode = "number",
                value = 16,
                number={"font": {"size": 30, 'color': "#F0E746"}},
                domain = {'row': 0, 'column': 2}))    
  
    ind_gift_age.add_trace(go.Indicator(
                  title = {'text': "<b>AGE 41-50</b><br>"
                           ,"font": {"size": 15, 'color': "#31333F"}},
                  mode = "number",
                  value = 1,
                  number={"font": {"size": 30, 'color': "#D96D34"}},
                  domain = {'row': 0, 'column': 3}))
    ind_gift_age.add_trace(go.Indicator(
                  title = {'text': "<b>AGE 51-80</b><br>"
                           ,"font": {"size": 15, 'color': "#31333F"}},
                  mode = "number",
                  value = 7,
                  number={"font": {"size": 30, 'color': "#CF3DFC"}},
                  domain = {'row': 0, 'column': 4}))   
    ind_gift_age.update_layout(
                  grid = {'rows': 1, 'columns': 5, 'pattern': "independent"})
    ind_gift_age.update_layout(height=200,autosize=False,paper_bgcolor="#FFFFFF", plot_bgcolor="#FFFFFF", margin=dict(l=20, r=20, b=20, t=65))
    
    ###########################################################################
    
    campaigns = [pie_gender,ind_gender,pie_age,ind_age,ind_players,pie_coins,pie_smiley,pie_gift,ind_coins,ind_smiley,ind_gift,state_fig,name_fig,pie_coins_gender,ind_coins_gender,pie_coins_age,ind_coins_age,pie_smiley_gender,ind_smiley_gender,pie_smiley_age,ind_smiley_age,pie_gift_gender,ind_gift_gender,pie_gift_age,ind_gift_age]
    
    return campaigns




    


