import smtplib
from email.mime.text import MIMEText

smtp_ssl_host = 'localhost'  # smtp.mail.yahoo.com
smtp_ssl_port = 1025
username = 'bro'
password = 'PASSWORD'
sender = 'me@localhost'
targets = ['he@localhost']

msg = MIMEText('Hi, how are you today?')
msg['Subject'] = 'Hello'
msg['From'] = sender
msg['To'] = ', '.join(targets)

server = smtplib.SMTP(smtp_ssl_host, smtp_ssl_port)
#server.login(username, password)
server.sendmail(sender, targets, msg.as_string())
server.quit()



