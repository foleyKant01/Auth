from flask import render_template

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib
from config.constant import *

gmail_user = EMAIL_USER
gmail_password = EMAIL_PASSWORD    

    
def send_mailer_pincode(email: str, temp_password: str):
    fromaddr = gmail_user
    toaddr = email
    subject = 'Changing your Password'
    body = render_template("update_password.html", temp_password=temp_password)
    print('Debut 3')

    msg = MIMEMultipart()
    msg['From'] = fromaddr
    msg['To'] = toaddr  # CORRECTION ICI
    msg['Subject'] = subject
    body = body
    msg.attach(MIMEText(body,'html', 'utf-8'))
    print('Debut 4')

    result = {}
    try:
        s = smtplib.SMTP('smtp.gmail.com', 587)
        result['status'] = '1'
    except Exception as e:
        result['error'] = '0' 
        result['description'] = e
        return result
    
    s.starttls()
    
    s.login(fromaddr, gmail_password)
    print('Debut 6')
    
    text = msg.as_string()
    print('Debut 7')
    
    s.sendmail(fromaddr, toaddr, text)
    print('Debut 8')
    
    s.quit()