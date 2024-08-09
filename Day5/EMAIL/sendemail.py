# Sending mail using Gmail

import smtplib

mailid = 'kumaprap@gmail.com'
#e_pass = input('gmail password ') #gmail generated app password input
e_pass = 'vkec gyjn ezly otwe'
with smtplib.SMTP('smtp.gmail.com',587) as smtp:
    smtp.starttls()   # encrypt the traffic

    smtp.login(mailid,e_pass)

    subject = 'Demo 2 for Email'
    body = 'This is the first demo for email using python'

    msg = f'Subject: {subject}\n\n{body}'

    smtp.sendmail(mailid,mailid,msg)
    print('The Mail is sent')
