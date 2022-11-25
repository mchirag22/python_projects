# Python libraries
import pandas as pd
import plotly.express as px
from datetime import datetime, timedelta
from helper import yesterday

# Local files
from helper import load_relevant_data

def plot_global_case_map(filename=None, day=None):
	df = load_relevant_data(us_data=False)
	dates = list(df.columns)
	df = df.groupby('Country/Region')[dates].agg('sum',numeric_only=True)
	create_global_figure(df, filename, day)

def create_global_figure(df, filename, day):
	day = day if day else yesterday # default to yesterday's date if not provided

	df['Cases'] = df.diff(axis=1)[day]
	df['Country'] = df.index

	fig = px.choropleth(df,
                    locations="Country",
                    locationmode="country names",
                    scope="world", # Try 'europe', 'africa', 'asia', 'south america', 'north america'
                    color="Cases",
                    hover_name="Country",
                    projection="natural earth",
                    color_continuous_scale='sunsetdark',
                    title='<b>Global Daily Cases<b>',
                    width=1000,
                    #height=500,
                    range_color=[0,10000])

	fig.update_layout(margin=dict(l=0, r=0, t=70, b=20), title={"font": {"size": 30}, "x":0.5},)
	filename = filename if filename else "global_chart.png"
	fig.write_image(filename, engine='kaleido')

if __name__ == '__main__':
	# yesterday = "10/10/20" # Uncomment for testing

	plot_global_case_map(day=yesterday) # saves as global_chart.png by default