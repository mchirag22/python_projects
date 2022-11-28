# Python libraries
import pandas as pd
import numpy as np
import plotly.express as plt
import os
from datetime import datetime, timedelta

# Local files
from helper import Mode, load_relevant_data, yesterday, yesterday_1

# This function creates a dataframe of top 10 countries and their yesterday's count for the given parameter
def top10_countries(mode=Mode.CASES):
    df = load_relevant_data(mode).groupby('Country/Region').sum(numeric_only=True).reset_index()
    df = df[['Country/Region',yesterday,yesterday_1]]
    df[yesterday] = df[yesterday] - df[yesterday_1]
    df = df[['Country/Region',yesterday]].sort_values(yesterday,ascending=False)
    df = df.head(10)
    return df

# This function creates a bar chart for the given parameters
def plot_bar(mode=Mode.CASES,type='Cases'):
    data = top10_countries(mode)
    fig = plt.bar(data,x='Country/Region',
                y=yesterday, 
                title=f'Countries with Most {type}',
                labels={'Country/Region':'',
                        yesterday:type},
                color=yesterday,
                color_continuous_scale='sunsetdark',
                range_color=[0,10000],
                text=yesterday)
    fig.update_traces(showlegend=False, textposition='outside')
    fig.update_layout({'plot_bgcolor': 'rgba(0, 0, 0, 0)','paper_bgcolor': 'rgba(0, 0, 0, 0)'})
    fig.update_xaxes(showgrid=False)
    fig.update_yaxes(showgrid=False)
    fig.update_layout(title={'y':0.84,'x':0.5,'xanchor': 'center','yanchor': 'top'})
    fig.update_layout(title={"font": {"size": 22}})
    fig.update(layout_coloraxis_showscale=False)
    
    fig.write_image(f'tmp/top10_country_{type}.png')

# This function creates a list of top 5 countries WRT the yesterday's counts for the given parameter
def top5_countries(mode=Mode.CASES):
    df = top10_countries(mode)
    df = df.head(5)
    list = df['Country/Region'].tolist()
    return list

# These are the variables that contain exactly what their name is WRT yesterday's counts
top_country_cases_list = top5_countries()
country_with_most_cases = top_country_cases_list[0]
country_with_secondmost_cases = top_country_cases_list[1]
