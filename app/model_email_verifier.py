#pip install validate_emai
#pip install py3dns

from validate_email import validate_email

def email_checker(email):
    try:
        validate_email(email)
        validate_status = True
    except Exception as e:
        validate_status = False
    
    email_checker_status = True  # Defina o status da função email_checker como True
    
    return validate_status, email_checker_status

# Chamada da função e recebimento dos valores retornados
#validate_result, email_checker_result = email_checker("beatriz.landi.coelho@gmail.com")

#print(validate_result)          # Status retornado pela função validate_email
#print(email_checker_result)     # Status retornado pela função email_checker

#exaple
#email_checker("beatriz.landi.coelho@gmail.com")

