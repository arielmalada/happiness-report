#!/usr/bin/env python
# coding: utf-8

# In[1]:

import json
import numpy as np 
import pandas as pd
import matplotlib.pyplot as plt 
#import dash as dash
import plotly as py
import plotly.express as px
import plotly.graph_objects as go

from plotly.offline import init_notebook_mode, iplot, plot
from dash import Dash, html, dcc, Input, Output

init_notebook_mode(connected=True)



# In[2]:


external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = Dash(__name__, external_stylesheets=external_stylesheets)


# In[27]:


# Read World Bank Data
happinessDataDf = pd.read_csv("./data/happiness-report-data.csv", encoding = "ISO-8859-1", na_values=['..', '...'])
happinessDataDf.columns = happinessDataDf.columns.str.replace(' ', '_')
# display(happinessDataDf)


# In[4]:


# Merging 2015 Happiness Score
Y2015ScoresDf = pd.read_csv("./data/2015.csv")
Y2015ScoresDf.columns = Y2015ScoresDf.columns.str.replace(' ', '_')
Y2015ScoresDf.columns = Y2015ScoresDf.columns.str.replace('Country', 'Country_Name')
Y2015ScoresDf = Y2015ScoresDf[['Country_Name',"Happiness_Score"]]
Y2015Df = pd.merge(happinessDataDf.query('Time_Code=="YR2015"'), Y2015ScoresDf, on='Country_Name')
# display(Y2015Df)


# In[5]:


# Merging 2016 Happiness Score
Y2016ScoresDf = pd.read_csv("./data/2016.csv")
Y2016ScoresDf.columns = Y2016ScoresDf.columns.str.replace(' ', '_')
Y2016ScoresDf.columns = Y2016ScoresDf.columns.str.replace('Country', 'Country_Name')
Y2016ScoresDf = Y2016ScoresDf[['Country_Name',"Happiness_Score"]]
Y2016Df = pd.merge(happinessDataDf.query('Time_Code=="YR2016"'), Y2016ScoresDf, on='Country_Name')
# display(Y2016Df)


# In[6]:


# Merging 2017 Happiness Score
Y2017ScoresDf = pd.read_csv("./data/2017.csv")
Y2017ScoresDf.columns = Y2017ScoresDf.columns.str.replace('.', '_')
Y2017ScoresDf.columns = Y2017ScoresDf.columns.str.replace('Country', 'Country_Name')
Y2017ScoresDf = Y2017ScoresDf[['Country_Name',"Happiness_Score"]]
Y2017Df = pd.merge(happinessDataDf.query('Time_Code=="YR2017"'), Y2017ScoresDf, on='Country_Name')
# display(Y2017Df)


# In[7]:


# Merging 2018 Happiness Score
Y2018ScoresDf = pd.read_csv("./data/2018.csv")
Y2018ScoresDf.columns = Y2018ScoresDf.columns.str.replace(' ', '_')
Y2018ScoresDf.columns = Y2018ScoresDf.columns.str.replace('Country_or_region', 'Country_Name')
Y2018ScoresDf.columns = Y2018ScoresDf.columns.str.replace('Score', 'Happiness_Score')
Y2018ScoresDf = Y2018ScoresDf[['Country_Name',"Happiness_Score"]]
Y2018Df = pd.merge(happinessDataDf.query('Time_Code=="YR2018"'), Y2018ScoresDf, on='Country_Name')
# display(Y2018Df)


# In[8]:


# Merging 2019 Happiness Score
Y2019ScoresDf = pd.read_csv("./data/2019.csv")
Y2019ScoresDf.columns = Y2019ScoresDf.columns.str.replace(' ', '_')
Y2019ScoresDf.columns = Y2019ScoresDf.columns.str.replace('Country_or_region', 'Country_Name')
Y2019ScoresDf.columns = Y2019ScoresDf.columns.str.replace('Score', 'Happiness_Score')
Y2019ScoresDf = Y2019ScoresDf[['Country_Name',"Happiness_Score"]]

Y2019Df = pd.merge(happinessDataDf.query('Time_Code=="YR2019"'), Y2019ScoresDf, on='Country_Name')
# display(Y2019Df)


# In[9]:


# Merging 2020 Happiness Score
Y2020ScoresDf = pd.read_csv("./data/2020.csv")
Y2020ScoresDf.columns = Y2020ScoresDf.columns.str.replace(' ', '_')
Y2020ScoresDf.columns = Y2020ScoresDf.columns.str.replace('Country_name', 'Country_Name')
Y2020ScoresDf.columns = Y2020ScoresDf.columns.str.replace('Ladder_score', 'Happiness_Score')
Y2020ScoresDf = Y2020ScoresDf[['Country_Name',"Happiness_Score"]]

Y2020Df = pd.merge(happinessDataDf.query('Time_Code=="YR2020"'), Y2020ScoresDf, on='Country_Name')
# display(Y2020Df)


# In[10]:


# Merging 2021 Happiness Score
Y2021ScoresDf = pd.read_csv("./data/2021.csv")
Y2021ScoresDf.columns = Y2021ScoresDf.columns.str.replace(' ', '_')
Y2021ScoresDf.columns = Y2021ScoresDf.columns.str.replace('Country_name', 'Country_Name')
Y2021ScoresDf.columns = Y2021ScoresDf.columns.str.replace('Ladder_score', 'Happiness_Score')
Y2021ScoresDf = Y2021ScoresDf[['Country_Name',"Happiness_Score"]]

Y2021Df = pd.merge(happinessDataDf.query('Time_Code=="YR2021"'), Y2021ScoresDf, on='Country_Name')
# display(Y2021Df)


# In[11]:


# merging all data
dataArray = [Y2015Df, Y2016Df,Y2017Df,Y2018Df,Y2019Df,Y2020Df,Y2021Df]
mergedData = pd.concat(dataArray)


# In[12]:


# create sample chart from data
fig = px.scatter(mergedData, x="Life_expectancy_at_birth,_total_(years)", y="GDP_per_capita,_PPP_(current_international_$)", animation_frame="Time", hover_name="Country_Name" )
fig.show()


# In[13]:


# create sample geospatial visualization from data
fig1 = px.choropleth(mergedData, 
                    locations="Country_Code",
                    hover_name="Country_Name",
                    # hover_data="Country_Code",
                    color="Happiness_Score",
                    color_continuous_scale=px.colors.sequential.Plasma)
fig1.show()


# In[ ]:


geospatialVisual = html.Div([
                        dcc.Graph(
                            id='geospatial',
                        )
                    ], style={'display': 'inline-block', 'padding': '0 20'})


# In[ ]:


happinessScoreVisual = html.Div([
                            dcc.Graph(
                                id='happiness-score-scatter-line'
                            )
                        ], style={ 'display': 'inline-block', 'padding': '0 20'})

# In[ ]:


happinessScoreVisual = html.Div([
                            dcc.Graph(
                                id='happiness-score-detail-polarchart'
                            )
                        ], style={ 'display': 'inline-block', 'padding': '0 20'})


# In[15]:


app.layout = html.Div([
    html.Div([
        geospatialVisual,
        happinessScoreVisual,
    ], style={
        'width': '50%',
        'padding': '10px 5px'
    }),
    # html.Div([
    #     dcc.Graph(id='variable1-scatter-line'),
    #     dcc.Graph(id='variable2-scatter-line'),
    # logging
    # html.Div([
    #         dcc.Markdown("""
    #             **Hover Data**

    #             Mouse over values in the graph.
    #         """),
    #         html.Pre(id='hover-data')
    #     ], className='three columns'),
    html.Div(dcc.Slider(
        min=mergedData['Time'].min(),
        max=mergedData['Time'].max(),
        id='year-slider',
        value=mergedData['Time'].max(),
        marks={str(time): str(time) for time in mergedData['Time'].unique()}
    ), style={'width': '97%', 'padding': '10px 20px 20px 20px'}),
])


# In[ ]:


@app.callback(
    Output('geospatial', 'figure'),
    Input('year-slider', 'value'))
def update_graph(year_value):
    df=mergedData[mergedData['Time'] == year_value]
    fig =  px.choropleth(df, 
                    locations="Country_Code",
                    hover_name="Country_Name",
                    color="Happiness_Score",
                    color_continuous_scale=px.colors.sequential.Plasma)

    return fig


# In[16]:


# happiness score visualization
@app.callback(
    Output('happiness-score-scatter-line', 'figure'),
    Input('geospatial', 'hoverData'))
def update_graph(HoverData):
    countryName = HoverData['points'][0]['hovertext']
    df=mergedData[mergedData['Country_Name'] == countryName]
    fig =  px.scatter(df, 
                      x="Time", 
                      y="Happiness_Score",
                      hover_name="Country_Name" )
    fig.update_traces(mode='lines+markers')
    return fig

# In[17]:
# logging
# @app.callback(
#     Output('hover-data', 'children'),
#     Input('geospatial', 'hoverData'))
# def display_hover_data(hoverData):
#     return json.dumps(hoverData, indent=2)

# In[18]:

# # Data for the polar chart
# categories = ['Category 1', 'Category 2', 'Category 3', 'Category 4', 'Category 5', 'Category 6', 'Category 7']
# values = [4, 7, 2, 5, 1, 6, 3]
# colors = ['red', 'blue', 'green', 'orange', 'purple', 'cyan', 'magenta']

# # Create traces for each category
# traces = []
# for i in range(len(categories)):
#     trace = go.Barpolar(
#         r=[values[i]],
#         theta=[categories[i]],
#         width=1,
#         marker=dict(color=colors[i]),
#         name=categories[i]
#     )
#     traces.append(trace)

# # Layout for the polar chart
# layout = go.Layout(
#     polar=dict(
#         radialaxis=dict(range=[0, max(values)]),
#     ),
# )

# # Create the figure
# fig2 = go.Figure(data=traces, layout=layout)
# fig2.show()


# I don't understand how callbacks works, but I wanted to show the detail of each subscore 
# of the happiness score once user hovers over a point of the happiness score visualization, 
# i.e: once a couple Country/Year is chosen, display the score detail following previously commented code

# happiness score detail visualization
@app.callback(
    Output('happiness-score-detail-polarchart', 'figure'),
    Input('happiness-score-scatter-line', 'hoverData'))
def update_graph(geoHoverData):
    countryName = geoHoverData['points'][0]['hovertext']
    df=mergedData[mergedData['Country_Name'] == countryName]
    fig =  px.scatter(df, 
                      x="Time", 
                      y="Happiness_Score",
                      hover_name="Country_Name" )
    fig.update_traces(mode='lines+markers')
    return fig



# In[ ]:


if __name__ == '__main__':
    app.run_server(port=8088, debug=True)


