import smtplib

email_address=('ivoivan182@gmail.com')
email_password=('Ivan3859')
toaddr=('anteprojic@gmail.com')

with smtplib.SMTP('smtp.gmail.com',587)as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.ehlo()

    smtp.login(email_address,email_password)

    predmet='Python test'
    body='Hi this is a python test from Ivan Kraljevic'

    Message=f'predmet:{predmet}\n\n{body}'

    smtp.sendmail(email_address,toaddr,Message)