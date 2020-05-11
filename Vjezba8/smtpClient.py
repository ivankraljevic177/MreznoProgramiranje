import smtplib


fromaddr = 'ivankraljevic177@gmail.com'
toaddrs  = 'ivankraljevic177@gmail.com'
msg='Hello'
server = smtplib.SMTP('smtp.gmail.com',1025)
server.sendmail(fromaddr, toaddrs, msg)
server.quit()