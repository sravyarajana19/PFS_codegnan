'''
Email Automation:
======================================================

SMPT{ simple mail transfer protocol}::

This is used to send emails from server to  another server.......
---------------
note:
1. SMTP SSL Port : 465

2. SMPT TLS Port : 587

-----------------

library :

>> import smtplib

-----------------
email message class :

msg['subject'] = 'SMTP ON Mail'
msg['from'] = 'sender@mail.com'
msg['To'] = 'receivers@mail.com'
--------------------------
>> for sending one mail to another mail


import smtplib
from email.message import EmailMessage
sender = 'rajanasravyasri@gmail.com'
password = 'ybolnqjwjdvhlznt'
msg = EmailMessage()

msg['subject'] = 'Welcome mail'
msg['From'] = sender
msg['To'] = 'nehapriya552@gmail.com'

msg.set_content('hi im sravya how r u what are u doing priya')
server = smtplib.SMTP('smtp.gmail.com',587)
server.starttls()
server.login(sender,password)
server.send_message(msg)
server.quit()
-------------------------------------------
>> for sending one mail to  many other mail

import smtplib
from email.message import EmailMessage

sender = 'rajanasravyasri@gmail.com'
password = 'pnhxuilzipgxidfy'
receiver_ =['nehapriya552@gmail.com','sravya9346@gmail.com','saimosuru0510@gmail.com']
server = smtplib.SMTP('smtp.gmail.com',587)
server.starttls()
server.login(sender,password)
for email in receiver_:
    msg = EmailMessage()

    msg['subject'] = 'Welcome mail'
    msg['From'] = sender
    msg['To'] = email
    msg.set_content('hi im sravya how r u what are u doing')

    server.send_message(msg)
server.quit()    
'''
    































