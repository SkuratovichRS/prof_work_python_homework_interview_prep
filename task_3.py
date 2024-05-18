import email
import smtplib
import imaplib
from email.message import Message
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


class EmailApp:
    def __init__(self, login, password):
        self.login = login
        self.password = password
        self.GMAIL_SMTP = "smtp.gmail.com"
        self.GMAIL_IMAP = "imap.gmail.com"
        self.subject = 'Subject'
        self.base_recipients = ['vasya@email.com', 'petya@email.com']

    def send_message(self, message: str) -> None:
        msg = MIMEMultipart()
        msg['From'] = self.login
        msg['To'] = ', '.join(self.base_recipients)
        msg['Subject'] = self.subject
        msg.attach(MIMEText(message))

        ms = smtplib.SMTP(self.GMAIL_SMTP, 587)
        ms.ehlo()
        ms.starttls()
        ms.ehlo()
        ms.login(self.login, self.password)
        ms.sendmail(self.login, self.base_recipients, msg.as_string())
        ms.quit()

    def receive_message(self, header) -> str | Message:
        mail = imaplib.IMAP4_SSL(self.GMAIL_IMAP)
        mail.login(self.login, self.password)
        mail.list()
        mail.select("inbox")

        criterion = '(HEADER Subject "%s")' % header if header else 'ALL'
        data = mail.uid('search', criterion)
        if not data[0]:
            return 'There are no letters with current header'

        latest_email_uid = data[0].split()[-1]
        result = mail.uid('fetch', latest_email_uid, '(RFC822)')
        raw_email = result[0][1]
        email_message = email.message_from_string(raw_email)
        mail.logout()

        return email_message


email_app = EmailApp('login@gmail.com', 'qwerty')
email_app.send_message("message")
email_app.receive_message(None)
