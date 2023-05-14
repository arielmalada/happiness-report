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

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
app = Dash(__name__, external_stylesheets=external_stylesheets)

happinessDataDf = pd.read_csv("./data/happiness-report-data.csv", encoding = "ISO-8859-1", na_values=['..', '...'])
happinessDataDf.columns = happinessDataDf.columns.str.replace(' ', '_')
# display(happinessDataDf)

# Merging 2015 Happiness Score
Y2015ScoresDf = pd.read_csv("./data/2015.csv")
Y2015ScoresDf.columns = Y2015ScoresDf.columns.str.replace(' ', '_')
Y2015ScoresDf.columns = Y2015ScoresDf.columns.str.replace('Country', 'Country_Name')
Y2015ScoresDf = Y2015ScoresDf[['Country_Name',"Happiness_Score"]]
Y2015Df = pd.merge(happinessDataDf.query('Time_Code=="YR2015"'), Y2015ScoresDf, on='Country_Name')
# display(Y2015Df)

# Merging 2016 Happiness Score
Y2016ScoresDf = pd.read_csv("./data/2016.csv")
Y2016ScoresDf.columns = Y2016ScoresDf.columns.str.replace(' ', '_')
Y2016ScoresDf.columns = Y2016ScoresDf.columns.str.replace('Country', 'Country_Name')
Y2016ScoresDf = Y2016ScoresDf[['Country_Name',"Happiness_Score"]]
Y2016Df = pd.merge(happinessDataDf.query('Time_Code=="YR2016"'), Y2016ScoresDf, on='Country_Name')
# display(Y2016Df)

Y2017ScoresDf = pd.read_csv("./data/2017.csv")
Y2017ScoresDf.columns = Y2017ScoresDf.columns.str.replace('.', '_')
Y2017ScoresDf.columns = Y2017ScoresDf.columns.str.replace('Country', 'Country_Name')
Y2017ScoresDf = Y2017ScoresDf[['Country_Name',"Happiness_Score"]]
Y2017Df = pd.merge(happinessDataDf.query('Time_Code=="YR2017"'), Y2017ScoresDf, on='Country_Name')
# display(Y2017Df)

# Merging 2018 Happiness Score
Y2018ScoresDf = pd.read_csv("./data/2018.csv")
Y2018ScoresDf.columns = Y2018ScoresDf.columns.str.replace(' ', '_')
Y2018ScoresDf.columns = Y2018ScoresDf.columns.str.replace('Country_or_region', 'Country_Name')
Y2018ScoresDf.columns = Y2018ScoresDf.columns.str.replace('Score', 'Happiness_Score')
Y2018ScoresDf = Y2018ScoresDf[['Country_Name',"Happiness_Score"]]
Y2018Df = pd.merge(happinessDataDf.query('Time_Code=="YR2018"'), Y2018ScoresDf, on='Country_Name')
# display(Y2018Df)

# Merging 2019 Happiness Score
Y2019ScoresDf = pd.read_csv("./data/2019.csv")
Y2019ScoresDf.columns = Y2019ScoresDf.columns.str.replace(' ', '_')
Y2019ScoresDf.columns = Y2019ScoresDf.columns.str.replace('Country_or_region', 'Country_Name')
Y2019ScoresDf.columns = Y2019ScoresDf.columns.str.replace('Score', 'Happiness_Score')
Y2019ScoresDf = Y2019ScoresDf[['Country_Name',"Happiness_Score"]]

Y2019Df = pd.merge(happinessDataDf.query('Time_Code=="YR2019"'), Y2019ScoresDf, on='Country_Name')
# display(Y2019Df)

# Merging 2020 Happiness Score
Y2020ScoresDf = pd.read_csv("./data/2020.csv")
Y2020ScoresDf.columns = Y2020ScoresDf.columns.str.replace(' ', '_')
Y2020ScoresDf.columns = Y2020ScoresDf.columns.str.replace('Country_name', 'Country_Name')
Y2020ScoresDf.columns = Y2020ScoresDf.columns.str.replace('Ladder_score', 'Happiness_Score')
Y2020ScoresDf = Y2020ScoresDf[['Country_Name',"Happiness_Score"]]

Y2020Df = pd.merge(happinessDataDf.query('Time_Code=="YR2020"'), Y2020ScoresDf, on='Country_Name')
# display(Y2020Df)

# Merging 2021 Happiness Score
Y2021ScoresDf = pd.read_csv("./data/2021.csv")
Y2021ScoresDf.columns = Y2021ScoresDf.columns.str.replace(' ', '_')
Y2021ScoresDf.columns = Y2021ScoresDf.columns.str.replace('Country_name', 'Country_Name')
Y2021ScoresDf.columns = Y2021ScoresDf.columns.str.replace('Ladder_score', 'Happiness_Score')
Y2021ScoresDf = Y2021ScoresDf[['Country_Name',"Happiness_Score"]]

Y2021Df = pd.merge(happinessDataDf.query('Time_Code=="YR2021"'), Y2021ScoresDf, on='Country_Name')
# display(Y2021Df)

# merging all data
dataArray = [Y2015Df, Y2016Df,Y2017Df,Y2018Df,Y2019Df,Y2020Df,Y2021Df]
mergedData = pd.concat(dataArray)

print(mergedData['CPIA_social_protection_rating_(1=low_to_6=high)'].head(100))
print(mergedData['Adjusted_savings:_carbon_dioxide_damage_(%_of_GNI)'].head(4))
print(mergedData.columns)
#print(mergedData['Internally_displaced_persons_total_displaced_by_conflict_and_violence_(number_of_people)'].head(50))

print(sorted(list(mergedData)))



