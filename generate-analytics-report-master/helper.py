import pandas as pd
from datetime import datetime, timedelta

class Mode:
	CASES = "Cases"
	DEATHS = "Deaths"

def load_relevant_data(us_data=True, mode=Mode.CASES):
	# This can be changed to your local directory (./) for testing purposes
	BASE_PATH = 'https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/'
	# BASE_PATH = './data/'
	if us_data and mode == Mode.CASES:
		PATH = BASE_PATH + 'time_series_covid19_confirmed_US.csv'
	elif us_data and mode == Mode.DEATHS:
		PATH = BASE_PATH + 'time_series_covid19_deaths_US.csv'
	elif not us_data and mode == Mode.CASES:
		PATH = BASE_PATH + 'time_series_covid19_confirmed_global.csv'
	elif not us_data and mode == Mode.DEATHS:
		PATH = BASE_PATH + 'time_series_covid19_deaths_global.csv'

	return pd.read_csv(PATH)

yesterday = (datetime.today() - timedelta(days=1)).strftime("%m/%d/%y").replace("/0","/").lstrip("0")
yesterday_1 = (datetime.strptime(yesterday, "%m/%d/%y") - timedelta(days=1)).strftime("%m/%d/%y").replace("/0","/").lstrip("0")
yesterday_2 = (datetime.strptime(yesterday, "%m/%d/%y") - timedelta(days=2)).strftime("%m/%d/%y").replace("/0","/").lstrip("0")

#Uncomment below to get day before data, incase yesterday data is not ready
# yesterday = yesterday_1
# yesterday_1 = yesterday_2