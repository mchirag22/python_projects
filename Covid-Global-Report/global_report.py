# Python libraries
from fpdf import FPDF
from datetime import datetime, timedelta
import os
import pandas as pd

# Local libraries
from create_case_maps import plot_global_case_map
from helper import Mode, yesterday
from top_10_countries import plot_bar,country_with_most_cases,country_with_secondmost_cases
from last_x_days import lastx_days_data_country
from paragraphs import date,first_para,second_para

# Dimentions of an A4 sheet
WIDTH = 210
HEIGHT = 297

# This function defines the position and style properties of the dynamic date for the given parameters
def create_date(day, pdf):
  pdf.set_font('Arial', 'B', 10)
  pdf.set_text_color(255,255,255)
  pdf.text(WIDTH-59.6,15, f'Date: {date}')

# This function defines the position and style properties of the dynamic paragraphs for the given parameters
def paragraph(day, pdf,xcord=None,ycord=None,text=None,cellh=5,cellw=WIDTH-20):
  pdf.set_font('Arial', '', 8)
  pdf.set_text_color(0,0,0)
  pdf.set_xy(xcord,ycord)
  pdf.multi_cell(WIDTH-20,5, txt=text,align='L')

# This function defines the position and style properties of the dynamic headings for the given parameters
def heading(day, pdf,xcord=None,ycord=None,text=None,cellh=5,cellw=WIDTH-20):
  pdf.set_font('Arial', 'B', 20)
  pdf.set_text_color(0,0,0)
  pdf.set_xy(xcord,ycord)
  pdf.multi_cell(WIDTH-20,5, txt=text,align='C')


# This function creates the PDF file for the given parameters
def create_analytics_report(day=None, filename="global_report.pdf"):
  
  pdf = FPDF() # A4 (210 by 297 mm)

  ''' First Page '''
  pdf.add_page()

  # Add the header file to the page
  pdf.image("./resources/covid_report_header_c.png", 0, 0, WIDTH)
  
  # Add the dynamic date to the header
  create_date(day, pdf)

  # Create a global case map for the date
  plot_global_case_map("./tmp/global_cases.png", day=day)

  # Create cases and deaths bar charts, for the date
  plot_bar()
  plot_bar(mode=Mode.DEATHS,type='Deaths')

  # Add the above charts to the specified positons
  pdf.image("./tmp/global_cases.png",0, 60, WIDTH)
  pdf.image('tmp/top10_country_cases.png', 5, 180, WIDTH/2)
  pdf.image('tmp/top10_country_deaths.png', WIDTH/2, 180, WIDTH/2)

  # Add the dynamic paragraphs to the specified positions
  paragraph(day, pdf,xcord=10,ycord=170,text=first_para)
  paragraph(day, pdf,xcord=10,ycord=255,text=second_para)

  ''' Second Page '''
  pdf.add_page()
  
  period = 365 # Duration for the last x days
  window = 20  # Days to be averaged out for the moving average trendline

  # Add the dynamic heading to the specified position
  heading(day, pdf,xcord=10,ycord=13,text=f'Last {period} Days Trend')

  # Create cases and deaths scatter charts WRT India and World for the given date
  lastx_days_data_country(last_days=period,country='India',mode=Mode.CASES,type='Cases',trend=window)
  lastx_days_data_country(last_days=period,country='India',mode=Mode.DEATHS,type='Deaths',trend=window)

  # Create cases and deaths scatter charts WRT country with most cases for the given date
  lastx_days_data_country(last_days=period,country=country_with_most_cases,mode=Mode.CASES,type='Cases',trend=window)
  lastx_days_data_country(last_days=period,country=country_with_most_cases,mode=Mode.DEATHS,type='Deaths',trend=window)

  # Create cases and deaths scatter charts WRT country with second most cases for the given date
  lastx_days_data_country(last_days=period,country=country_with_secondmost_cases,mode=Mode.CASES,type='Cases',trend=window)
  lastx_days_data_country(last_days=period,country=country_with_secondmost_cases,mode=Mode.DEATHS,type='Deaths',trend=window)

  # Add the above charts to the specified positons
  pdf.image('tmp/last_365_world_Cases.png', 5, 15, WIDTH/2)
  pdf.image('tmp/last_365_world_Deaths.png', WIDTH/2, 15, WIDTH/2)
  pdf.image('tmp/last_365_india_Cases.png', 5, 80, WIDTH/2)
  pdf.image('tmp/last_365_india_Deaths.png', WIDTH/2, 80, WIDTH/2)  
  pdf.image(f'tmp/last_365_{country_with_most_cases}_Cases.png', 5, 145, WIDTH/2)
  pdf.image(f'tmp/last_365_{country_with_most_cases}_Deaths.png', WIDTH/2, 145, WIDTH/2) 
  pdf.image(f'tmp/last_365_{country_with_secondmost_cases}_Cases.png', 5, 210, WIDTH/2)
  pdf.image(f'tmp/last_365_{country_with_secondmost_cases}_Deaths.png', WIDTH/2, 210, WIDTH/2) 

  ''' Third Page '''
  pdf.add_page()
  
  period = 30 # Duration for the last x days
  window = 7  # Days to be averaged out for the moving average trendline

  # Add the dynamic heading to the specified position
  heading(day, pdf,xcord=10,ycord=13,text=f'Last {period} Days Trend')

  # Create cases and deaths scatter charts WRT India and World for the given date
  lastx_days_data_country(last_days=period,country='India',mode=Mode.CASES,type='Cases',trend=window)
  lastx_days_data_country(last_days=period,country='India',mode=Mode.DEATHS,type='Deaths',trend=window)

  # Create cases and deaths scatter charts WRT country with most cases for the given date
  lastx_days_data_country(last_days=period,country=country_with_most_cases,mode=Mode.CASES,type='Cases',trend=window)
  lastx_days_data_country(last_days=period,country=country_with_most_cases,mode=Mode.DEATHS,type='Deaths',trend=window)

  # Create cases and deaths scatter charts WRT country with second most cases for the given date
  lastx_days_data_country(last_days=period,country=country_with_secondmost_cases,mode=Mode.CASES,type='Cases',trend=window)
  lastx_days_data_country(last_days=period,country=country_with_secondmost_cases,mode=Mode.DEATHS,type='Deaths',trend=window)

  # Add the above charts to the specified positons
  pdf.image('tmp/last_30_world_Cases.png', 5, 15, WIDTH/2)
  pdf.image('tmp/last_30_world_Deaths.png', WIDTH/2, 15, WIDTH/2)
  pdf.image('tmp/last_30_india_Cases.png', 5, 80, WIDTH/2)
  pdf.image('tmp/last_30_india_Deaths.png', WIDTH/2, 80, WIDTH/2)  
  pdf.image(f'tmp/last_30_{country_with_most_cases}_Cases.png', 5, 145, WIDTH/2)
  pdf.image(f'tmp/last_30_{country_with_most_cases}_Deaths.png', WIDTH/2, 145, WIDTH/2) 
  pdf.image(f'tmp/last_30_{country_with_secondmost_cases}_Cases.png', 5, 210, WIDTH/2)
  pdf.image(f'tmp/last_30_{country_with_secondmost_cases}_Deaths.png', WIDTH/2, 210, WIDTH/2) 

  pdf.output(filename)

if __name__ == '__main__':
  
  create_analytics_report(yesterday)
