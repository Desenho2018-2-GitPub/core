import smtplib
from email.message import EmailMessage


class EmailSender(object):
    _instance = None

    def __new__(cls, *kwargs):
        if EmailSender._instance is None:
            EmailSender._instance = object.__new__(cls)

        EmailSender._instance.email_connection = smtplib.SMTP(
            host='smtp.office365.com', port=587)
        EmailSender._instance.email_connection.starttls()
        EmailSender._instance.email_connection.login(
            'gitpubapp@hotmail.com', 'MileneMauricio')

        return EmailSender._instance

    def send_email(self, email_to, body):
        msg = EmailMessage()
        msg.set_content(body)
        msg['Subject'] = 'GitPub Notification'
        msg['From'] = 'gitpubapp@hotmail.com'
        msg['To'] = email_to
        self.email_connection.send_message(msg)
