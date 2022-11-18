import smtplib
import sendgrid as sg
import os
from sendgrid.helpers.mail import Mail, Email, To, Content

SUBJECT = "Expense Tracker"
s = smtplib.SMTP('smtp.gmail.com', 587)


def sendmail(TEXT, email):
    s = smtplib.SMTP('smtp.gmail.com', 587)
    s.starttls()
    s.login(os.environ.get('SG_EMAIL'), os.environ.get('SG_PASSWORD'))
    message = 'Subject: {}\n\n{}'.format(SUBJECT, TEXT)
    s.sendmail(os.environ.get('SG_EMAIL'), email, message)
    s.quit()


def sendgridmail(user, TEXT):
    from_email = Email(os.environ.get('SG_EMAIL'))
    to_email = To(user)
    content = Content("text/plain", TEXT)
    mail = Mail(from_email, to_email, SUBJECT, content)

    mail_json = mail.get()
    response = sg.client.mail.send.post(request_body=mail_json)
    print(response.status_code)
    print(response.headers)
