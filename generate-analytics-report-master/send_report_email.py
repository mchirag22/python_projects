import os
import smtplib
from datetime import datetime, timedelta
from email.message import EmailMessage
from global_report import create_analytics_report
from helper import yesterday
from firstpage_extract import save_first_page

from email.utils import make_msgid
import mimetypes

path = "E:\Case Study\Covid\generate-analytics-report-master" # insert your own path here

EMAIL_ADDRESS = os.environ.get('email_chirag')
EMAIL_PASSWORD = os.environ.get('email_chirag_pass')

msg = EmailMessage()
msg['Subject'] = 'Daily Covid 19 Global Report'
msg['From'] = EMAIL_ADDRESS
msg['To'] = 'chiragmalhan97@gmail.com'

create_analytics_report(yesterday, filename="global_report.pdf")
save_first_page()


# set the plain text body
msg.set_content('This is a plain text body.')

# now create a Content-ID for the image
image_cid = make_msgid(domain='xyz.com')
# if `domain` argument isn't provided, it will 
# use your computer's name

# set an alternative html body
msg.add_alternative("""\
<html>
    <body>
        <p>Hi,<br>
            Here is your daily update on the Covid 19 global pandemic. <br>
            You can also find the report PDF attached below, to find further details on the historic trends.
        </p>
        <img src="cid:{image_cid}" style="display:block" width="650">
        <p>Regards,<br>
            Chirag Malhan 
        </p>
    </body>
</html>
""".format(image_cid=image_cid[1:-1]), subtype='html')
# image_cid looks like <long.random.number@xyz.com>
# to use it as the img src, we don't need `<` or `>`
# so we use [1:-1] to strip them off


# now open the image and attach it to the email
with open("./tmp/firstpage_global_report.png", 'rb') as img:

    # know the Content-Type of the image
    maintype, subtype = mimetypes.guess_type(img.name)[0].split('/')

    # attach it
    msg.get_payload()[1].add_related(img.read(), 
                                         maintype=maintype, 
                                         subtype=subtype, 
                                         cid=image_cid)









with open('global_report.pdf', 'rb') as f:
  data = f.read()

msg.add_attachment(data, filename='global_report.pdf', maintype='application/pdf', subtype='pdf')

with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
    smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
    smtp.send_message(msg)