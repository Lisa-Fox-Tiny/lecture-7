import email
import smtplib
import imaplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


class Email:

    def __init__(self, login_, password_):
        self.connect = {'login': login_, 'password': password_}

    def sendmail(self, server_, port_, recipients_, subject_, body_):
        try:
            email_message = MIMEMultipart()
            email_message['From'] = self.connect['login']
            email_message['To'] = ', '.join(recipients_)
            email_message['Subject'] = subject_
            email_message.attach(MIMEText(body_))
            send_msg = smtplib.SMTP(server_, port_)
            send_msg.ehlo()
            send_msg.starttls()
            send_msg.ehlo()
            send_msg.login(self.connect['login'], self.connect['password'])
            result = send_msg.sendmail(email_message['From'], email_message['To'], email_message.as_string())
            send_msg.quit()
            return result
        except Exception as e:
            return f'Failed to send email: {e}'

    def receive_mail(self, server_, mailbox_, header_=None):
        receive_mail_instance = imaplib.IMAP4_SSL(server_)
        try:
            receive_mail_instance.login(self.connect['login'], self.connect['password'])
            receive_mail_instance.list()
            receive_mail_instance.select(mailbox_)
            criterion = '(HEADER Subject "%s")' % header_ if header_ else 'ALL'
            result, data = receive_mail_instance.uid('search', None, criterion)
            assert data[0], 'There are no letters with current header'
            latest_email_uid = data[0].split()[-1]
            result, data = receive_mail_instance.uid('fetch', latest_email_uid.decode('utf-8'), '(RFC822)')
            raw_email = data[0][1]
            email_result_receive = email.message_from_string(raw_email.decode('utf-8'))
            receive_mail_instance.logout()
            return email_result_receive
        except Exception as e:
            return f'Failed to receive email:{e}'


if __name__ == '__main__':
    gmail = Email('login@gmail.com', 'qwerty')
    print(gmail.sendmail(
        'smtp.gmail.com',
        587,
        ['vasya@email.com', 'petya@email.com'],
        'Subject',
        'Body of test message'
        ))
    print(gmail.receive_mail('imap.gmail.com', 'inbox'))

