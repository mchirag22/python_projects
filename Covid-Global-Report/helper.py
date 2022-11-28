# Python libraries
import pandas as pd
from datetime import datetime, timedelta

class Mode:
	CASES = "Cases"
	DEATHS = "Deaths"

# This function defines the correct path to the live GitHub CSV file based on the Mode class
def load_relevant_data(mode=Mode.CASES):
	BASE_PATH = 'https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/'
	if mode == Mode.CASES:
		PATH = BASE_PATH + 'time_series_covid19_confirmed_global.csv'
	elif mode == Mode.DEATHS:
		PATH = BASE_PATH + 'time_series_covid19_deaths_global.csv'
	return pd.read_csv(PATH)

# These are the variable to get the dates for 'yesterday','day before yesterday', and '2 days before yesterday' respectively
yesterday = (datetime.today() - timedelta(days=1)).strftime("%m/%d/%y").replace("/0","/").lstrip("0")
yesterday_1 = (datetime.strptime(yesterday, "%m/%d/%y") - timedelta(days=1)).strftime("%m/%d/%y").replace("/0","/").lstrip("0")
yesterday_2 = (datetime.strptime(yesterday, "%m/%d/%y") - timedelta(days=2)).strftime("%m/%d/%y").replace("/0","/").lstrip("0")

#Uncomment below to get day before data, incase yesterday data is not ready
# yesterday = yesterday_1
# yesterday_1 = yesterday_2