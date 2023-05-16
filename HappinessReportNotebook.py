#!/usr/bin/env python
# coding: utf-8

# In[1]:

import json
import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt 
import dash as dash
import plotly as py
import plotly.express as px
import plotly.graph_objects as go


from plotly.offline import init_notebook_mode, iplot, plot
init_notebook_mode(connected=True)
from dash import Dash, html, dcc
from dash import Dash, html, dcc, Input, Output

# Permanently changes the pandas settings
# pd.set_option('display.max_rows', None)
# pd.set_option('display.max_columns', None)
# pd.set_option('display.width', None)
# pd.set_option('display.max_colwidth', -1)

# Reset pandas settings
# pd.reset_option("all")

# TODO: implement polar chart which will look for the correct dataset name, ie "Y[YearNumber]ScoresdetDf" 
# and column names as specified below:
    # subscores index names model: 
    # 2015-16 pattern:
    # Economy_(GDP_per_Capita)
    # Family
    # Health_(Life_Expectancy)
    # Freedom
    # Trust_(Government_Corruption)
    # Generosity
    # Dystopia_Residual
# Because subscores ranges may change yearly depending on the way its calculated, we need to:
    # Normalize (0-1 rounding up) by
        # looking for local-column min and max
        # divide accordingly
    # Then dynamically feed min/max values to the polar graph axis for every actualization,
    # plus normalized values to render the radius of every go.Barpolar



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
Y2015ScoresdetDf = Y2015ScoresDf
# display(Y2015ScoresdetDf)

Y2015ScoresDf = Y2015ScoresDf[['Country_Name',"Happiness_Score"]]
Y2015Df = pd.merge(happinessDataDf.query('Time_Code=="YR2015"'), Y2015ScoresDf, on='Country_Name')
# display(Y2015Df)


# In[5]:


# Merging 2016 Happiness Score
Y2016ScoresDf = pd.read_csv("./data/2016.csv")
Y2016ScoresDf.columns = Y2016ScoresDf.columns.str.replace(' ', '_')
Y2016ScoresDf.columns = Y2016ScoresDf.columns.str.replace('Country', 'Country_Name')
Y2016ScoresdetDf = Y2016ScoresDf
# display(Y2016ScoresdetDf)

Y2016ScoresDf = Y2016ScoresDf[['Country_Name',"Happiness_Score"]]
Y2016Df = pd.merge(happinessDataDf.query('Time_Code=="YR2016"'), Y2016ScoresDf, on='Country_Name')
# display(Y2016Df)


# In[6]:


# Merging 2017 Happiness Score
Y2017ScoresDf = pd.read_csv("./data/2017.csv")
Y2017ScoresDf = Y2017ScoresDf.replace("..", '.')
Y2017ScoresDf.columns = Y2017ScoresDf.columns.str.replace('.', '_')
Y2017ScoresdetDf = Y2017ScoresDf
# display(Y2017Df)
Y2017ScoresdetDf = Y2017ScoresdetDf.rename(columns={'Economy__GDP_per_Capita_': 'Economy_(GDP_per_Capita)'})
Y2017ScoresdetDf = Y2017ScoresdetDf.rename(columns={"Health__Life_Expectancy_": "Health_(Life_Expectancy)"})
Y2017ScoresdetDf = Y2017ScoresdetDf.rename(columns={"Freedom_to_make_life_choices": "Freedom"})
Y2017ScoresdetDf = Y2017ScoresdetDf.rename(columns={"Trust__Government_Corruption_": "Trust_(Government_Corruption)"})

# display(Y2017ScoresdetDf)

Y2017ScoresDf.columns = Y2017ScoresDf.columns.str.replace('Country', 'Country_Name')
Y2017ScoresDf = Y2017ScoresDf[['Country_Name',"Happiness_Score"]]
Y2017Df = pd.merge(happinessDataDf.query('Time_Code=="YR2017"'), Y2017ScoresDf, on='Country_Name')
# display(Y2017ScoresDf)
# display(Y2017Df)


# In[7]:


# Merging 2018 Happiness Score
Y2018ScoresDf = pd.read_csv("./data/2018.csv")
Y2018ScoresDf.columns = Y2018ScoresDf.columns.str.replace(' ', '_')
Y2018ScoresDf.columns = Y2018ScoresDf.columns.str.replace('Country_or_region', 'Country_Name')
Y2018ScoresDf.columns = Y2018ScoresDf.columns.str.replace('Score', 'Happiness_Score')
Y2018ScoresdetDf = Y2018ScoresDf
# display(Y2018Df)
Y2018ScoresdetDf.rename(columns={"GDP_per_capita": "Economy_(GDP_per_Capita)"}, inplace=True)
Y2018ScoresdetDf.rename(columns={"Social_support": "Family"}, inplace=True)
Y2018ScoresdetDf.rename(columns={"Healthy_life_expectancy": "Health_(Life_Expectancy)"}, inplace=True)
Y2018ScoresdetDf.rename(columns={"Freedom_to_make_life_choices": "Freedom"}, inplace=True)
Y2018ScoresdetDf.rename(columns={"Generosity": "Generosity"}, inplace=True)
Y2018ScoresdetDf.rename(columns={"Perceptions_of_corruption": "Trust_(Government_Corruption)"}, inplace=True)
# Y2018Df.rename(columns={"Dystopia_+_residual": "Dystopia_Residual"}, inplace=True)
# no dystopia

# display(Y2018ScoresdetDf)

Y2018ScoresDf = Y2018ScoresDf[['Country_Name',"Happiness_Score"]]
Y2018Df = pd.merge(happinessDataDf.query('Time_Code=="YR2018"'), Y2018ScoresDf, on='Country_Name')
# display(Y2018ScoresDf)
# display(Y2018Df)


# In[8]:


# Merging 2019 Happiness Score
Y2019ScoresDf = pd.read_csv("./data/2019.csv")
Y2019ScoresDf.columns = Y2019ScoresDf.columns.str.replace(' ', '_')
Y2019ScoresDf.columns = Y2019ScoresDf.columns.str.replace('Country_or_region', 'Country_Name')
Y2019ScoresDf.columns = Y2019ScoresDf.columns.str.replace('Score', 'Happiness_Score')
Y2019ScoresdetDf = Y2019ScoresDf
# display(Y2019Df)
Y2019ScoresdetDf.rename(columns={"GDP_per_capita": "Economy_(GDP_per_Capita)"}, inplace=True)
Y2019ScoresdetDf.rename(columns={"Social_support": "Family"}, inplace=True)
Y2019ScoresdetDf.rename(columns={"Healthy_life_expectancy": "Health_(Life_Expectancy)"}, inplace=True)
Y2019ScoresdetDf.rename(columns={"Freedom_to_make_life_choices": "Freedom"}, inplace=True)
Y2019ScoresdetDf.rename(columns={"Generosity": "Generosity"}, inplace=True)
Y2019ScoresdetDf.rename(columns={"Perceptions_of_corruption": "Trust_(Government_Corruption)"}, inplace=True)
# Y2019Df.rename(columns={"Dystopia_+_residual": "Dystopia_Residual"}, inplace=True)
# no dystopia

# display(Y2019ScoresdetDf)

Y2019ScoresDf = Y2019ScoresDf[['Country_Name',"Happiness_Score"]]

Y2019Df = pd.merge(happinessDataDf.query('Time_Code=="YR2019"'), Y2019ScoresDf, on='Country_Name')
# display(Y2019ScoresDf)
# display(Y2019Df)


# In[9]:


# Merging 2020 Happiness Score
Y2020ScoresDf = pd.read_csv("./data/2020.csv")
Y2020ScoresDf.columns = Y2020ScoresDf.columns.str.replace(' ', '_')
Y2020ScoresDf.columns = Y2020ScoresDf.columns.str.replace('Country_name', 'Country_Name')
Y2020ScoresDf.columns = Y2020ScoresDf.columns.str.replace('Ladder_score', 'Happiness_Score')
Y2020ScoresdetDf = Y2020ScoresDf
# display(Y2020Df)
Y2020ScoresdetDf.rename(columns={"Logged_GDP_per_capita": "Economy_(GDP_per_Capita)"}, inplace=True)
Y2020ScoresdetDf.rename(columns={"Social_support": "Family"}, inplace=True)
Y2020ScoresdetDf.rename(columns={"Healthy_life_expectancy": "Health_(Life_Expectancy)"}, inplace=True)
Y2020ScoresdetDf.rename(columns={"Freedom_to_make_life_choices": "Freedom"}, inplace=True)
Y2020ScoresdetDf.rename(columns={"Generosity": "Generosity"}, inplace=True)
Y2020ScoresdetDf.rename(columns={"Perceptions_of_corruption": "Trust_(Government_Corruption)"}, inplace=True)
Y2020ScoresdetDf.rename(columns={"Dystopia_+_residual": "Dystopia_Residual"}, inplace=True)

# display(Y2020ScoresdetDf)

Y2020ScoresDf = Y2020ScoresDf[['Country_Name',"Happiness_Score"]]

Y2020Df = pd.merge(happinessDataDf.query('Time_Code=="YR2020"'), Y2020ScoresDf, on='Country_Name')
# display(Y2020ScoresDf)
# display(Y2020Df)


# In[10]:


# Merging 2021 Happiness Score
Y2021ScoresDf = pd.read_csv("./data/2021.csv")
Y2021ScoresDf.columns = Y2021ScoresDf.columns.str.replace(' ', '_')
Y2021ScoresDf.columns = Y2021ScoresDf.columns.str.replace('Country_name', 'Country_Name')
Y2021ScoresDf.columns = Y2021ScoresDf.columns.str.replace('Ladder_score', 'Happiness_Score')
Y2021ScoresdetDf = Y2021ScoresDf
# display(Y2021ScoresdetDf)
Y2021ScoresdetDf.rename(columns={"Logged_GDP_per_capita": "Economy_(GDP_per_Capita)"}, inplace=True)
Y2021ScoresdetDf.rename(columns={"Social_support": "Family"}, inplace=True)
Y2021ScoresdetDf.rename(columns={"Healthy_life_expectancy": "Health_(Life_Expectancy)"}, inplace=True)
Y2021ScoresdetDf.rename(columns={"Freedom_to_make_life_choices": "Freedom"}, inplace=True)
Y2021ScoresdetDf.rename(columns={"Generosity": "Generosity"}, inplace=True)
Y2021ScoresdetDf.rename(columns={"Perceptions_of_corruption": "Trust_(Government_Corruption)"}, inplace=True)
Y2021ScoresdetDf.rename(columns={"Dystopia_+_residual": "Dystopia_Residual"}, inplace=True)

# display(Y2021ScoresdetDf)

Y2021ScoresDf = Y2021ScoresDf[['Country_Name',"Happiness_Score"]]
Y2021Df = pd.merge(happinessDataDf.query('Time_Code=="YR2021"'), Y2021ScoresDf, on='Country_Name')
# display(Y2021ScoresDf)
# display(Y2021Df)


# In[11]:


# merging all data
dataArray = [Y2015Df, Y2016Df,Y2017Df,Y2018Df,Y2019Df,Y2020Df,Y2021Df]
mergedData = pd.concat(dataArray)

#same treatment for scores
dataArrayScoresdetDf = [Y2015ScoresdetDf, 
                        Y2016ScoresdetDf, 
                        Y2017ScoresdetDf, 
                        Y2018ScoresdetDf, 
                        Y2019ScoresdetDf, 
                        Y2020ScoresdetDf, 
                        Y2021ScoresdetDf]
mergedScoresdetDfData = pd.concat(dataArrayScoresdetDf)


# In[12]:


# create sample chart from data
fig = px.scatter(mergedData, 
                 x="Life_expectancy_at_birth,_total_(years)", 
                 y="GDP_per_capita,_PPP_(current_international_$)", 
                 animation_frame="Time", 
                 hover_name="Country_Name" )
fig.show()


# In[13]:


# create sample geospatial visualization from data
fig1 = px.choropleth(mergedData, 
                    locations="Country_Code",
                    hover_name="Country_Name",
                    color="Happiness_Score",
                    color_continuous_scale=px.colors.sequential.Plasma)
fig1.show()


# In[ ]:


geospatialVisual = html.Div([
    dcc.Graph(
    id='geospatial', 
    hoverData={'points': [{'hovertext': 'Finland'}]}
    )
    ], style={'padding': '0 20'})


# In[ ]:


happinessScoreVisual = html.Div([
    dcc.Graph(
    id='happiness-score-scatter-line'
    )
    ], style={'padding': '0 20'})

# In[ ]:


happinessScoreDetailVisual = html.Div([
                            dcc.Graph(
                                id='happiness-score-detail-polarchart'
                            )
                        ], style={'padding': '0 20'})


# In[15]:


app.title = "World Happiness Report Visualization"
app.layout = html.Div([
    html.Div([
        html.H1("World Happiness Visualization"),
        html.Div([
            html.Div([
                dcc.Dropdown(
                    options={
                        'GDP_per_capita_growth_(annual_%)#CO2_emissions_(metric_tons_per_capita)': 'Economic Production',
                        'Life_expectancy_at_birth,_female_(years)#Life_expectancy_at_birth,_male_(years)': 'Health',
                        # 'Adjusted_savings:_carbon_dioxide_damage_(%_of_GNI)#CPIA_social_protection_rating_(1=low_to_6=high)':'Social Support',
                        # 'Intentional_homicides_(per_100,000_people)#Internally_displaced_persons,_total_displaced_by_conflict_and_violence_(number_of_people)':'Human Rights',
                        # 'Proportion_of_people_living_below_50_percent_of_median_income_(%)#Multidimensional_poverty_headcount_ratio_(%_of_total_population)':'Charity',
                        # 'CPIA_transparency,_accountability,_and_corruption_in_the_public_sector_rating_(1=low_to_6=high)#CPIA_policy_and_institutions_for_environmental_sustainability_rating_(1=low_to_6=high)':'Corruption'
                    },
                    value='GDP_per_capita_growth_(annual_%)#CO2_emissions_(metric_tons_per_capita)',
                    id='crossfilter-yaxis-column',
                    placeholder="Select an indicator category"
                ),
            ], style={'width': '100%'})
        ], style={
            'width': '100%',
            'padding': '10px 5px'
        }),
    ], style={
        'display': 'flex',
        'width': '100%',
        'padding': '10px 5px'
    }),
    html.Div([
        html.Div([
            geospatialVisual,
            happinessScoreVisual,
            happinessScoreDetailVisual
        ], style={
            'width': '69%',
            'padding': '10px 5px',

        }),
        html.Div([
            dcc.Graph(id='indicator-series1'),
            dcc.Graph(id='indicator-series2'),
        ], style={'width': '29%'}),
    ], style={
        'display': 'flex',
        'width': '100%',
        'padding': '10px 5px'
    }),


    html.Div(dcc.Slider(
        min=mergedData['Time'].min(),
        max=mergedData['Time'].max(),
        id='year-slider',
        value=mergedData['Time'].max(),
        marks={str(time): str(time) for time in mergedData['Time'].unique()}
    ), style={'width': '97%', 'padding': '10px 20px 20px 20px'}),
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
], style={
    'height': '100vh'
})


# In[ ]:


@app.callback(
    Output('geospatial', 'figure'),
    Input('year-slider', 'value'))
def update_graph(year_value):
    df = mergedData[mergedData['Time'] == year_value]
    fig = px.choropleth(df,
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
    df = mergedData[mergedData['Country_Name'] == countryName]
    fig = px.scatter(df,
                     x="Time",
                     y="Happiness_Score",
                     hover_name="Country_Name")
    fig.update_traces(mode='lines+markers')

    return fig


def create_time_series(df, axis_column, title):
    titleTimeSeries = title.replace('_', ' ')
    fig = px.scatter(df, x='Time', y=axis_column)

    fig.update_traces(mode='lines+markers')

    fig.update_xaxes(showgrid=False)

    fig.add_annotation(x=0, y=0.85, xanchor='left', yanchor='bottom',
                       xref='paper', yref='paper', showarrow=False, align='left',
                       text=titleTimeSeries)

    fig.update_layout(height=250, margin={'l': 20, 'b': 30, 'r': 10, 't': 10})

    return fig


@app.callback(
    Output('indicator-series1', 'figure'),
    Input('geospatial', 'hoverData'),
    Input('crossfilter-yaxis-column', 'value'))
def update_indicator_series1(geoHoverData, value):
    countryName = geoHoverData['points'][0]['hovertext']
    df = mergedData[mergedData['Country_Name'] == countryName]
    y_columns = value.split("#")
    indicator1 = y_columns[0]
    title = '<b>{}</b><br>{}'.format(countryName, indicator1)
    return create_time_series(df, indicator1, title)


@app.callback(
    Output('indicator-series2', 'figure'),
    Input('geospatial', 'hoverData'),
    Input('crossfilter-yaxis-column', 'value'))
def update_indicator_series2(geoHoverData, value):
    countryName = geoHoverData['points'][0]['hovertext']
    df = mergedData[mergedData['Country_Name'] == countryName]
    y_columns = value.split("#")
    indicator2 = y_columns[1]
    title = '<b>{}</b><br>{}'.format(countryName, indicator2)
    return create_time_series(df, indicator2, title)
# logging
# @app.callback(
#     Output('hover-data', 'children'),
#     Input('geospatial', 'hoverData'))
# def display_hover_data(hoverData):
#     return json.dumps(hoverData, indent=2)

# In[17]:
# logging
# @app.callback(
#     Output('hover-data', 'children'),
#     Input('geospatial', 'hoverData'))
# def display_hover_data(hoverData):
#     return json.dumps(hoverData, indent=2)

# In[18]:

## WIP !!

# values = mergedData[(mergedData['Country_Name'] == "Finland")
#                   & (mergedData['Time'] == 2021)]
# countryName = HoverData['points'][0]['hovertext']
# df=mergedData[mergedData['Country_Name'] == 'countryName']

# mergedScoresdetDfData

categories = ["Economy_(GDP_per_Capita)", 
              "Family", 
              "Health_(Life_Expectancy)", 
              "Freedom", 
              "Trust_(Government_Corruption)", 
              "Generosity", 
              "Dystopia_Residual"
              ]
# values = mergedScoresdetDfData[mergedScoresdetDfData['Country_Name'] == "Finland"]

# values = pd.DataFrame
values = Y2021ScoresdetDf[Y2021ScoresdetDf['Country_Name'] == "Finland"]
values = values[categories]

# values = [1,1,1,1,1,1,0]

# display(values)

# happiness score detail visualization
# @app.callback(
#     Output('happiness-score-detail-polarchart', 'figure'),
#     Input('happiness-score-scatter-line', 'hoverData'))
# def update_graph(geoHoverData):
#     countryName = geoHoverData['points'][0]['hovertext']
#     df=mergedData[mergedData['Country_Name'] == countryName]
#     fig =  px.scatter(df, 
#                       x="Time", 
#                       y="Happiness_Score",
#                       hover_name="Country_Name" )
#     fig.update_traces(mode='lines+markers')
#     return fig

# In[19]:

# # Data for the polar chart
# categories = ['Category 1', 'Category 2', 'Category 3', 'Category 4', 'Category 5', 'Category 6', 'Category 7']
# values = [4, 7, 2, 5, 1, 6, 3]
# colors = ['red', 'blue', 'green', 'orange', 'purple', 'cyan', 'magenta']

# Create traces for each category
traces = []
for i in range(len(categories)):
    trace = go.Barpolar(
        r=[values.iloc[:,i]],
        theta=[categories[i]],
        width=1,
        marker=dict(color=px.colors.sequential.Plasma[i]),
        name=categories[i]
    )
    traces.append(trace)

# Layout for the polar chart
layout = go.Layout(
    polar=dict(
        radialaxis=dict(range=[0, max(values)]),
    ),
)

# Create the figure
fig2 = go.Figure(data=traces, layout=layout)
fig2.show()


# I don't understand how callbacks works, but I wanted to show the detail of each subscore 
# of the happiness score once user hovers over a point of the happiness score visualization, 
# i.e: once a couple Country/Year is chosen, display the score detail following previously commented code

# happiness score detail visualization
# @app.callback(
#     Output('happiness-score-detail-polarchart', 'figure'),
#     Input('happiness-score-scatter-line', 'hoverData'))
# def update_graph(geoHoverData):
#     countryName = geoHoverData['points'][0]['hovertext']
#     df=mergedData[mergedData['Country_Name'] == countryName]
#     fig =  px.scatter(df, 
#                       x="Time", 
#                       y="Happiness_Score",
#                       hover_name="Country_Name" )
#     fig.update_traces(mode='lines+markers')
#     return fig

# In[20]:

# 19V2

# Data for the polar chart
# categories = ['Category 1', 'Category 2', 'Category 3', 'Category 4', 'Category 5', 'Category 6', 'Category 7']
# categories = ['Category 1', 'Category 2', 'Category 3', 'Category 4', 'Category 5', 'Category 6', 'Category 7']
# values = [4, 7, 2, 5, 1, 6, 3]
# values = mergedData[(mergedData['Country_Name'] == countryName)
#                   & (mergedData['Time'] == year_value)]

# colors = ['red', 'blue', 'green', 'orange', 'purple', 'cyan', 'magenta']

# countryName = geoHoverData['points'][0]['hovertext']
#     df=

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


# In[ ]:


if __name__ == '__main__':
    app.run_server(port=8088, debug=True)


