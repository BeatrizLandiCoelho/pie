from Email import EmailSender


def send_email_passwords():
    company_email = "emailtesteremailtester123@gmail.com"
    company_email_key = "wykxeptrluwazmvr"

    # Instanciar a classe EmailSender
    email_sender = EmailSender('smtp.gmail.com', 587, 'emailtesteremailtester123@gmail.com', 'wykxeptrluwazmvr')

    # Enviar um email
    email_sender.send_email('Assunto do Email', 'beatriz.landi.coelho@gmail.com', 'Corpo do email')


send_email_passwords()
