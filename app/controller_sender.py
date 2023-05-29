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
#print(cheek_if_email_exist("beatriz.landi.coelho@gmail.com"))


#_______________________________________________________

def send_email_gmail_com(email_title,user_email, body_email):
    company_email = "emailtesteremailtester123@gmail.com"
    company_email_key = "wykxeptrluwazmvr"

    # Instanciar a classe EmailSender
    email_sender = EmailSender('smtp.gmail.com', 587, company_email, company_email_key)

    # Enviar um email
    email_sender.send_email("title", user_email, body_email)

#exammple
#send_email_gmail_com("email tittle","andressa.fideliscoelho@gmail.com","email body")
#______________________________________________________________

def generic_send_email_gmail_com(company_email,company_email_key,email_title, user_email, body_email):
   
    # Instanciar a classe EmailSender
    email_sender = EmailSender('smtp.gmail.com', 587, company_email, company_email_key)

    # Enviar um email
    email_sender.send_email(email_title, user_email, body_email)

#example
#generic_send_email_gmail_com("emailtesteremailtester123@gmail.com","wykxeptrluwazmvr","email tittle","andressa.fideliscoelho@gmail.com","email body")
#______________________________________________________________