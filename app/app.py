#COMANDS
#python -m venv venv
#.\venv\Scripts\activate

#framework
from flask import Flask, jsonify, make_response, request
#parcial imports
from controller_sender import cheek_if_email_exist,send_email_gmail_com, generic_send_email_gmail_com

#instance this baby
app = Flask(__name__)

#________________________________________________________________

@app.route("/v1/emailcheek", methods=['POST'])
def email_cheker():

    email_requested = request.json['email']

    if(email_requested ==''):
        return make_response(
            jsonify(
              status=400
            )
            )

    status,email_existence = cheek_if_email_exist(email_requested)

    return make_response(
      jsonify(

        status = 200,
        email = email_requested,
        validity = email_existence

      )
    )

#________________________________________________________________


@app.route("/v1/emailsendgeneric", methods=['POST'])
def email_sender_generic_version():
      
      company_email = request.json['company email']
      company_email_key = request.json['company email key']
      tittle_email = request.json['title']
      user_email = request.json['email']
      body_email = request.json['body']


      generic_send_email_gmail_com(company_email,company_email_key,tittle_email,user_email,body_email)
  
      return make_response(
      jsonify(

        comp_email=company_email,
        tittle=tittle_email,
        body= body_email,
        to=user_email,
        status = 200
  
      )
    )   
    
  
#________________________________________________________________
@app.route("/v2/emailsend", methods=['POST'])
def email_sender():
      

      tittle_email = request.json['title']
      user_email = request.json['email']
      body_email = request.json['body']

      send_email_gmail_com(tittle_email,user_email,body_email)

      return make_response(
      jsonify(

        tittle=tittle_email,
        body= body_email,
        to=user_email,
        status = 200
  
      )
    )
  
#________________________________________________________________

if __name__ == '__main__':

    print("server read to go")
    app.run(port=8080, debug=True) 


