import smtplib
from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

server = smtplib.SMTP('smtp.gmail.com', 587)

server.ehlo()

with open('message.txt', 'r') as f:
    credentials = f.readlines()
    username = credentials[0].strip().split('=')[1]
    password = credentials[1].strip().split('=')[1]

server.login(username, password)

msg = MIMEMultipart()
msg['From'] = username
msg['To'] = 'to_some_mail@gmail.com'
msg['Subject'] = 'Test email body.'

with open('message.txt', 'r') as f:
    message = f.read()

msg.attach(MIMEText(message, 'plain'))

filename = 'coding.jpg'
attachment = open(filename, 'rb')

payload = MIMEBase('application', 'octet-stream')
payload.set_payload(attachment.read())

encoders.encode_base64(payload)
payload.add_header('Content-Disposition', f'attachment;, filename={filename}')
msg.attach(payload)

text = msg.as_string()
server.sendmail(username, 'to_some_mail@gmail.com', text)

server.quit()
