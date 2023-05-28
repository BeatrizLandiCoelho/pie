import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

class EmailSender:
    #create class
    def __init__(self, smtp_server, smtp_port, username, password):
        self.smtp_server = smtp_server
        self.smtp_port = smtp_port
        self.username = username
        self.password = password


#send email
    def send_email(self, subject, recipient, body):
        message = MIMEMultipart()
        message['From'] = self.username
        message['To'] = recipient
        message['Subject'] = subject

        message.attach(MIMEText(body, 'plain'))

        try:
            with smtplib.SMTP(self.smtp_server, self.smtp_port) as server:
                server.starttls()
                server.login(self.username, self.password)
                server.send_message(message)
                print("Email enviado com sucesso!")
        except Exception as e:
            print("Erro ao enviar email:", str(e))





