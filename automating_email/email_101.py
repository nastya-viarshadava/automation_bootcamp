import smtplib

sender_email = 'testerint13@gmail.com'
password = 'password'

connection = smtplib.SMTP('smtp.gmail.com')

connection.starttls()

connection.login(user=sender_email, password=password)

connection.sendmail(from_addr=sender_email, to_addrs=sender_email, msg='Hello world!')

connection.close()