Following is the list of files in this repo, along with what they do:

1) send_report_email.py --> Main file that runs everything. This is where the email is drafted and sent.

2) helper.py --> This file gets the live path to related GitHub database files and defines various date variables.

3) create_case_maps.py --> This file defines a function to create the global daily cases chart

4) top_10_countries.py --> This file defines functions to create the bar charts used in the report. 
                            Also, it defines variables for country with most cases and country with second most cases.

5) last_x_days.py --> This file defines funtions to create scatter charts used in the report.

6) paragraphs.py --> This file defines variables that are later used to create dynamic text and paragraphs used in the report.

7) global_report.py --> This file picks up all the above created functions, creates charts for yesterday, compiles it in a PDF file and saves it as global_report.pdf

8) firstpage_extract.py --> This file takes the first page of the global_report.pdf and saves it as a PNG file.
