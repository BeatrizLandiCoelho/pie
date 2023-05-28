#pip install validate_emai
#pip install py3dns

from validate_email import validate_email

def email_cheker(email):


    try:    
        
        if(validate_email(email)==True):
            status = "a"
        else:
            status = "b"
           
        return True

    except Exception as e:

        return False 
    
#exaple    
email_cheker("beatriz.landi.coelho@gmail.com")
