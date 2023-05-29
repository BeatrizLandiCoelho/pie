from Email import EmailSender
from model_email_verifier import email_checker

#_______________________________________________________

def cheek_if_email_exist (email):
 
  if(
    email=="" or
    len(email) < 6 or
    len(email) > 256 
    ):
    status = False
    return status

  status,email_existence = email_checker(email) 
  
  return status,email_existence 

#example
#cheek_if_email_exist("beatriz.landi.coelho@gmail.com")

#_______________________________________________________

#exaple
#cheek_if_email_exist("beatriz.landi.coelho@gmail.com")


# def change_passwords():
#     company_email = "emailtesteremailtester123@gmail.com"
#     company_email_key = "wykxeptrluwazmvr"

#     # Instanciar a classe EmailSender
#     email_sender = EmailSender('smtp.gmail.com', 587, 'emailtesteremailtester123@gmail.com', 'wykxeptrluwazmvr')

#     # Enviar um email
#     email_sender.send_email('Assunto do Email', 'beatriz.landi.coelho@gmail.com', 'Corpo do email')

