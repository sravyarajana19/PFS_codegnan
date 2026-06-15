'''
Date and Time: python provides the built-in datetime module to work with date and time.
--------------
syntax: import datetime

>> to access today date

import datetime
today=datetime.date.today()
print(today)


>> to access today time

import datetime
today=datetime.date.today()
now=datetime.datetime.now()
print(now)
print(today)


>> to access year,month,day,hour

import datetime
now=datetime.datetime.now()
print(f"Year is:{now.year}")
print(f"Month is: {now.month}")
print(f"Day is: {now.day}")
print(f"Hour is: {now.hour}")
print(f"Minute is: {now.minute}")
print(f"Seconds is: {now.second}")
-----------------------------------------
Formatting date and time:
strftime(): is the method used to formate date and time

import datetime
now=datetime.datetime.now()
print(now.strftime("%d-%m-%Y"))
print(now.strftime("%H-%M-%S"))

%d --> day
%m --> month
%Y --> year
%H --> hour
%M --> min
%s -- > sec..

import datetime
date_1 = datetime.date(2025,6,1)
date_2 = datetime.date(2025,6,1)
diff_ = date_2 - date_1
print(diff_)

---------------------------------------------
Timedelta:


import datetime
today = datetime.date.today()
future_ = today +datetime.timedelta(days = 7)
print(future_)


import datetime
day_= datetime.date.today()
print(day_.ctime())



import calendar
import datetime

today = datetime.date.today()
year = today.year
month = today.month
print(calendar.month(year,month))

import calendar
import datetime

today = datetime.date.today()
year = 2004
month = 7
print(calendar.month(year,month))


import calendar

year = 2004
print(calendar.calendar(year))

================================================================================


import smtplib
from email.message import EmailMessage
import datetime
from datetime import datetime

sender = 'rajanasravyasri@gmail.com'
password = 'jjmzcqqncdfydzih'
receiver = 'nehapriya7@gmail.com'
target_time = '1:30'
msg = EmailMessage()

msg['subject'] = 'Welcome mail'
msg['From'] = sender
msg['To'] = 'nehapriya7@gmail.com'

msg.set_content('hi how r uh')
server = smtplib.SMTP('smtp.gmail.com',587)
server.starttls()
server.login(sender,password)
server.send_message(msg)
server.quit()

'''






















