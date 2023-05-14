#!/usr/bin/env python
# coding: utf-8

# In[1]:

import json
import numpy as np 
import pandas as pd 

import matplotlib.pyplot as plt 
import numpy as np 
import pandas as pd 

from plotly.offline import init_notebook_mode, iplot, plot
from dash import Dash, html, dcc
import plotly as py
init_notebook_mode(connected=True)
import plotly.express as px
from dash import Dash, html, dcc, Input, Output


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
                        ], style={'display': 'inline-block', 'padding': '0 20'})


# In[15]:

app.title = "World Happiness Report Visualization"
app.layout = html.Div([
    html.H1("World Happiness Visualization"),
    html.Div([
        html.Div([
            dcc.Dropdown(
                options={
                  'GDP_per_capita_growth_(annual_%)#CO2_emissions_(metric_tons_per_capita)':'Economic Production',
                  'Life_expectancy_at_birth,_female_(years)#Life_expectancy_at_birth,_male_(years)':'Health',
                  'Adjusted_savings:_carbon_dioxide_damage_(%_of_GNI)#CPIA_social_protection_rating_(1=low_to_6=high)':'Social Support',
                  'Intentional_homicides_(per_100,000_people)#Internally_displaced_persons,_total_displaced_by_conflict_and_violence_(number_of_people)':'Human Rights',
                  'Proportion_of_people_living_below_50_percent_of_median_income_(%)#Multidimensional_poverty_headcount_ratio_(%_of_total_population)':'Charity',
                  'CPIA_transparency,_accountability,_and_corruption_in_the_public_sector_rating_(1=low_to_6=high)#CPIA_policy_and_institutions_for_environmental_sustainability_rating_(1=low_to_6=high)':'Corruption'
                },
                value= 'GDP_per_capita_growth_(annual_%),CO2_emissions_(metric_tons_per_capita)',
                id='crossfilter-yaxis-column',
                placeholder= "Select an indicator category"
            ),
        ], style={'width': '39%', 'float': 'right', 'display': 'inline-block'})
    ], style={
        'padding': '10px 5px'
    }),
    html.Div([
        geospatialVisual,
        happinessScoreVisual,
    ], style={
        'width': '49%',
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
    html.Div([
        dcc.Graph(id='indicator-series1'),
        dcc.Graph(id='indicator-series2'),
    ], style={'display': 'inline-block', 'width': '49%'}),

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
def update_graph(geoHoverData):
    countryName = geoHoverData['points'][0]['hovertext']
    df=mergedData[mergedData['Country_Name'] == countryName]
    fig =  px.scatter(df, 
                      x="Time", 
                      y="Happiness_Score",
                      hover_name="Country_Name" )
    fig.update_traces(mode='lines+markers')

    return fig

def create_time_series(df, axis_column, title):

    fig = px.scatter(df, x='Time', y=axis_column)

    fig.update_traces(mode='lines+markers')

    fig.update_xaxes(showgrid=False)

    fig.add_annotation(x=0, y=0.85, xanchor='left', yanchor='bottom',
                       xref='paper', yref='paper', showarrow=False, align='left',
                       text=title)

    fig.update_layout(height=225, margin={'l': 20, 'b': 30, 'r': 10, 't': 10})

    return fig

@app.callback(
    Output('indicator-series1', 'figure'),
    Input('geospatial', 'hoverData'),
    Input('crossfilter-yaxis-column', 'value'))
def update_indicator_series1(geoHoverData, value):
    countryName = geoHoverData['points'][0]['hovertext']
    df=mergedData[mergedData['Country_Name'] == countryName]
    y_columns= value.split("#")
    indicator1=y_columns[0]
    title = '<b>{}</b><br>{}'.format(countryName, indicator1)
    return create_time_series(df, indicator1, title)


@app.callback(
    Output('indicator-series2', 'figure'),
    Input('geospatial', 'hoverData'),
    Input('crossfilter-yaxis-column', 'value'))
def update_indicator_series2(geoHoverData, value):
    countryName = geoHoverData['points'][0]['hovertext']
    df=mergedData[mergedData['Country_Name'] == countryName]
    y_columns= value.split("#")
    indicator2=y_columns[1]
    title = '<b>{}</b><br>{}'.format(countryName, indicator2)
    return create_time_series(df, indicator2, title)
# logging
# @app.callback(
#     Output('hover-data', 'children'),
#     Input('geospatial', 'hoverData'))
# def display_hover_data(hoverData):
#     return json.dumps(hoverData, indent=2)

# In[18]:


if __name__ == '__main__':
    app.run_server(port=8092, debug=True)


# In[ ]:




