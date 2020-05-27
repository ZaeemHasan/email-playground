import smtplib
from email.message import EmailMessage
from string import Template
from pathlib import Path  # similar to os.path library

html = Template(Path('index.html').read_text())

email = EmailMessage()

sender_name = 'SenderName'

email['from'] = sender_name
email['to'] = 'receiver.email@gmail.com'
email['subject'] = 'You won 1,000,000 dollars!'

email.set_content(html.substitute(receiver='ReceiverName', sender=sender_name), 'html')

with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login('sender.email@gmail.com', 'senderPassword')
    smtp.send_message(email)
    print('all good boss!')
