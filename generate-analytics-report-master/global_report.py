# Python libraries
from fpdf import FPDF
from datetime import datetime, timedelta
import os
import pandas as pd

# Local libraries
from create_case_maps import plot_global_case_map
from helper import Mode, yesterday
from top_10_countries import top10_country_cases,top10_country_deaths,plot_bar,top5_countries,top_country_cases_list,country_with_most_cases,country_with_secondmost_cases
from last_x_days import lastx_days_data_country
from paragraphs import first_para,second_para

path = "E:\Case Study\Covid\generate-analytics-report-master"

WIDTH = 210
HEIGHT = 297

def create_date(day, pdf):
  pdf.set_font('Arial', 'B', 10)
  pdf.set_text_color(255,255,255)
  day = pd.to_datetime(day, format='%m/%d/%y')
  day = day.strftime('%d-%b-%Y')
  pdf.text(WIDTH-59.6,15, f'Date: {day}')

def paragraph(day, pdf,xcord=None,ycord=None,text=None,cellh=5,cellw=WIDTH-20):
  pdf.set_font('Arial', '', 8)
  pdf.set_text_color(0,0,0)
  pdf.set_xy(xcord,ycord)
  pdf.multi_cell(WIDTH-20,5, txt=text,align='L')


def heading(day, pdf,xcord=None,ycord=None,text=None,cellh=5,cellw=WIDTH-20):
  pdf.set_font('Arial', 'B', 20)
  pdf.set_text_color(0,0,0)
  pdf.set_xy(xcord,ycord)
  pdf.multi_cell(WIDTH-20,5, txt=text,align='C')


  
def create_analytics_report(day=None, filename="global_report.pdf"):
  pdf = FPDF() # A4 (210 by 297 mm)

  ''' First Page '''
  pdf.add_page()
  pdf.image("./resources/covid_report_header_c.png", 0, 0, WIDTH)
  create_date(day, pdf)

  plot_global_case_map("./tmp/global_cases.png", day=day)

  plot_bar(data=top10_country_cases(),
            x='Country/Region',
            y=yesterday,
            title='Countries with Most Cases',
            xlable='Countries',
            ylable='Cases',
            filename='tmp/top10_country_cases.png')
  
  plot_bar(data=top10_country_deaths(),
            x='Country/Region',
            y=yesterday,
            title='Countries with Most Deaths',
            xlable='Countries',
            ylable='Deaths',
            filename='tmp/top10_country_deaths.png')

  pdf.image("./tmp/global_cases.png",0, 60, WIDTH)
  pdf.image('tmp/top10_country_cases.png', 5, 180, WIDTH/2)
  pdf.image('tmp/top10_country_deaths.png', WIDTH/2, 180, WIDTH/2)

  paragraph(day, pdf,xcord=10,ycord=170,text=first_para)
  paragraph(day, pdf,xcord=10,ycord=255,text=second_para)

  ''' Second Page '''
  pdf.add_page()
  
  period = 365
  window = 20

  heading(day, pdf,xcord=10,ycord=13,text=f'Last {period} Days Trend')

  lastx_days_data_country(last_days=period,country='India',mode=Mode.CASES,type='Cases',trend=window)
  lastx_days_data_country(last_days=period,country='India',mode=Mode.DEATHS,type='Deaths',trend=window)

  lastx_days_data_country(last_days=period,country=country_with_most_cases,mode=Mode.CASES,type='Cases',trend=window)
  lastx_days_data_country(last_days=period,country=country_with_most_cases,mode=Mode.DEATHS,type='Deaths',trend=window)

  lastx_days_data_country(last_days=period,country=country_with_secondmost_cases,mode=Mode.CASES,type='Cases',trend=window)
  lastx_days_data_country(last_days=period,country=country_with_secondmost_cases,mode=Mode.DEATHS,type='Deaths',trend=window)
# tmp/last_{last_days}_world_{type}.png
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
  
  period = 30
  window = 7

  heading(day, pdf,xcord=10,ycord=13,text=f'Last {period} Days Trend')

  lastx_days_data_country(last_days=period,country='India',mode=Mode.CASES,type='Cases',trend=window)
  lastx_days_data_country(last_days=period,country='India',mode=Mode.DEATHS,type='Deaths',trend=window)

  lastx_days_data_country(last_days=period,country=country_with_most_cases,mode=Mode.CASES,type='Cases',trend=window)
  lastx_days_data_country(last_days=period,country=country_with_most_cases,mode=Mode.DEATHS,type='Deaths',trend=window)

  lastx_days_data_country(last_days=period,country=country_with_secondmost_cases,mode=Mode.CASES,type='Cases',trend=window)
  lastx_days_data_country(last_days=period,country=country_with_secondmost_cases,mode=Mode.DEATHS,type='Deaths',trend=window)

  pdf.image('tmp/last_30_world_Cases.png', 5, 15, WIDTH/2)
  pdf.image('tmp/last_30_world_Deaths.png', WIDTH/2, 15, WIDTH/2)
  pdf.image('tmp/last_30_india_Cases.png', 5, 80, WIDTH/2)
  pdf.image('tmp/last_30_india_Deaths.png', WIDTH/2, 80, WIDTH/2)  
  pdf.image(f'tmp/last_30_{country_with_most_cases}_Cases.png', 5, 145, WIDTH/2)
  pdf.image(f'tmp/last_30_{country_with_most_cases}_Deaths.png', WIDTH/2, 145, WIDTH/2) 
  pdf.image(f'tmp/last_30_{country_with_secondmost_cases}_Cases.png', 5, 210, WIDTH/2)
  pdf.image(f'tmp/last_30_{country_with_secondmost_cases}_Deaths.png', WIDTH/2, 210, WIDTH/2) 

  pdf.output(filename, 'F')

if __name__ == '__main__':
  
  create_analytics_report(yesterday)
