#pip install validate_emai
#pip install py3dns

from validate_email import validate_email


def email_checker(email):
    
    status = True

    try:
        
        if(validate_email(email)==True):
            email_existence = True

        else:
            email_existence = False
            
    except Exception as e:
        status = False
 
    return status, email_existence


#example
# status,email_existence = email_checker("beatriz.landi.celho@gmail.com")
# print(status) mostra se a funcao funcionou
# print(email_existence) mostra se o email existe
