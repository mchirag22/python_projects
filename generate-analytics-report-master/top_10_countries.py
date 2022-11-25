# Python libraries
import pandas as pd
import numpy as np
# import matplotlib.pyplot as plt
import plotly.express as plt
import os
from datetime import datetime, timedelta

# Local files
from helper import Mode, load_relevant_data, yesterday, yesterday_1

def plot_bar(data=None,x=None,y=None,title=None,xlable=None,ylable=None,filename=None):
    fig = plt.bar(data,x=x,
                y=y, 
                title=title,
                labels={x:'',
                        y:ylable},
                color=y,
                color_continuous_scale='sunsetdark',
                range_color=[0,10000],
                text=y)
    fig.update_traces(showlegend=False, textposition='outside')
    fig.update_layout({'plot_bgcolor': 'rgba(0, 0, 0, 0)','paper_bgcolor': 'rgba(0, 0, 0, 0)'})
    fig.update_xaxes(showgrid=False)
    fig.update_yaxes(showgrid=False)
    fig.update_layout(title={'y':0.84,'x':0.5,'xanchor': 'center','yanchor': 'top'})
    fig.update_layout(title={"font": {"size": 22}})
    fig.update(layout_coloraxis_showscale=False)
    
    fig.write_image(filename)

def top10_country_cases():
    df = load_relevant_data(us_data=False).groupby('Country/Region').sum(numeric_only=True).reset_index()
    df = df[['Country/Region',yesterday,yesterday_1]]
    df[yesterday] = df[yesterday] - df[yesterday_1]
    df = df[['Country/Region',yesterday]].sort_values(yesterday,ascending=False)
    df = df.head(10)
    return df

plot_bar(data=top10_country_cases(),
            x='Country/Region',
            y=yesterday,
            title='Countries with Most Cases',
            xlable='Countries',
            ylable='Cases',
            filename='tmp/top10_country_cases.png')


def top10_country_deaths():
    df = load_relevant_data(us_data=False, mode=Mode.DEATHS).groupby('Country/Region').sum(numeric_only=True).reset_index()
    df = df[['Country/Region',yesterday,yesterday_1]]
    df[yesterday] = df[yesterday] - df[yesterday_1]
    df = df[['Country/Region',yesterday]].sort_values(yesterday,ascending=False)
    df = df.head(10)
    return df

plot_bar(data=top10_country_deaths(),
            x='Country/Region',
            y=yesterday,
            title='Countries with Most Deaths',
            xlable='Countries',
            ylable='Deaths',
            filename='tmp/top10_country_deaths.png')


def top5_countries(data=top10_country_cases(),date=yesterday):
    df = top10_country_cases()
    df = df.head(5)
    list = df['Country/Region'].tolist()
    return list

top_country_cases_list = top5_countries(data=top10_country_cases(),date=yesterday)
country_with_most_cases = top_country_cases_list[0]
country_with_secondmost_cases = top_country_cases_list[1]
