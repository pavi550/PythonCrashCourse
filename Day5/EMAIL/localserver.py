# Sending mail to local server

import smtplib

# diverting the o/p to os
# python -m smtpd -c DebuggingServer -n localhost:1025

mailid = 'kumaprap@gmail.com'
#e_pass = input('Enter the password')
e_pass = 'vkec gyjn ezly otwe'

with smtplib.SMTP('localhost', 1025) as smtp:
    subject = 'Demo 2 for Email'
    body = 'This is the first demo for email using python'

    msg = f'Subject: {subject}\n\n{body}'

    smtp.sendmail(mailid, mailid, msg)
    print('The Mail is sent')