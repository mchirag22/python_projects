# Python libraries
import pandas as pd
import numpy as np
import plotly.express as plt
import os
from datetime import datetime, timedelta
import statsmodels as sm

import warnings
warnings.filterwarnings('ignore')

# Local files
from helper import Mode, load_relevant_data, yesterday

def plot_line(data=None,x=None,y=None,title=None,xlable=None,ylable=None,filename=None,trend=20):
    fig = plt.scatter(data,x=x,
                y=y, 
                title=title,
                trendline="rolling",
                trendline_options=dict(window=trend),
                color=y,
                opacity=0.5,
                color_continuous_scale='sunsetdark',
                range_color=[0,10000])

    fig.update_traces(showlegend=False, textposition='top center',line=dict(color='#000000', width=2))
    fig.update_layout({'plot_bgcolor': 'rgba(0, 0, 0, 0)','paper_bgcolor': 'rgba(0, 0, 0, 0)'})
    fig.update_xaxes(showgrid=False)
    fig.update_yaxes(showgrid=False)
    fig.update_layout(title={'y':0.83,'x':0.5,'xanchor': 'center','yanchor': 'top'})
    fig.update(layout_coloraxis_showscale=False)
    fig.update_traces(marker_size=10)
    fig.update_layout(title={"font": {"size": 22}},
                        xaxis_title=' ',
                        yaxis_title=ylable)
    
    fig.write_image(filename)

def lastx_days_data_country(last_days=10,country='India',mode=Mode.CASES,type='Cases',trend=20):
    df = load_relevant_data(us_data=False, mode=mode).groupby('Country/Region').sum(numeric_only=True).reset_index()
    column = 'Country/Region'
    m = -last_days
    n = m-1

    world_count = df.iloc[:,n:]
    i=-1
    while i>n:
        world_count.iloc[:,i] = world_count.iloc[:,i] - world_count.iloc[:,i-1]
        i = i-1
    world_count = world_count.iloc[:,m:]
    world_count = world_count.sum()

    fd = df[df[column] == country]
    country_count = fd.iloc[:,n:]
    j=-1
    while j>n:
        country_count.iloc[:,j] = country_count.iloc[:,j] - country_count.iloc[:,j-1]
        j = j-1
        
    country_count = country_count.iloc[:,m:]
    country_count = country_count.sum()

    count = pd.concat([world_count,country_count],axis=1)
    count.columns = ['World',country]
    count.index = pd.to_datetime(count.index, format='%m/%d/%y')

    plot_line(data=count,x=count.index,y='World',title=f'Last {last_days} days World {type}',xlable=None,ylable=type,filename=f'tmp/last_{last_days}_world_{type}.png',trend=trend)
    plot_line(data=count,x=count.index,y=country,title=f'Last {last_days} days {country} {type}',xlable=None,ylable=type,filename=f'tmp/last_{last_days}_{country}_{type}.png',trend=trend)

lastx_days_data_country(last_days=200,country='India',mode=Mode.DEATHS,type='Deaths')