import smtplib
from email.message import EmailMessage

mailid = 'kumaprap@gmail.com'
#e_pass = input('Enter the password')
e_pass = 'vkec gyjn ezly otwe'

msg = EmailMessage()
msg['Subject'] ='Demo 3 for Email'
msg['From'] = mailid
msg['To'] = mailid
msg.set_content('This is the body of the mail')

with smtplib.SMTP('localhost',1025) as smtp:
    #smtp.login(mailid,e_pass)

    smtp.send_message(msg)
    print('The mail is sent')