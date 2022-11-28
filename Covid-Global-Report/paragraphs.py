import pandas as pd
from helper import Mode, yesterday
from top_10_countries import country_with_most_cases,country_with_secondmost_cases

day = pd.to_datetime(yesterday, format='%m/%d/%y')
date = day.strftime('%d-%b-%Y')

first_para = f'The above chart shows the number of new covid cases across the globe, as reported by the respective governments, on {date}. This data is collected and maintained by Johns Hopkins University Center for Systems Science and Engineering (JHU CSSE), on their github repository.'
second_para = f'The above charts show the top 10 countries with most cases and deaths respectively, on {date}. We can clearly see that {country_with_most_cases} had the most number of reported cases observed, followed by {country_with_secondmost_cases}, and so on. Here, the colors of the bars are true to the color scale as shown in the global chart.'
