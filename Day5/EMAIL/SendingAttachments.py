# Sending Attachments

import smtplib
from email.message import EmailMessage
import imghdr

mailid = 'kumaprap@gmail.com'
#e_pass = input('Enter the password')
e_pass = 'vkec gyjn ezly otwe'

msg = EmailMessage()
msg['Subject'] ='Demo 4 for Email'
msg['From'] = mailid
msg['To'] = mailid
msg.set_content('Please find the Image attached with mail')

with open('Screenshot 2024-08-08 101808.png','rb')as f:
    file_data=f.read()
    file_type = imghdr.what(f.name)
    file_name = f.name

msg.add_attachment(file_data,maintype = 'image',subtype = file_type,filename =file_name)

with smtplib.SMTP_SSL('smtp.gmail.com',587) as smtp:
    smtp.starttls()  # encrypt the traffic
    smtp.login(mailid,e_pass)
    smtp.send_message(msg)
    print('The mail is sent')