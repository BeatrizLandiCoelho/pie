#COMANDS
#python -m venv venv
#.\venv\Scripts\activate

#framework
from flask import Flask, jsonify, make_response, request
#parcial imports
from controller_sender import cheek_if_email_exist

#instance this baby
app = Flask(__name__)

#________________________________________________________________

@app.route("/v1/emailcheek", methods=['POST'])
def email_cheker():

    email_requested = request.json['email']

    cheek_if_email_exist(email_requested)

    return make_response(
      jsonify(

        email = email_requested,
        valid = "a"

      )
    )

#________________________________________________________________

if __name__ == '__main__':

    print("server read to go")
    app.run(port=8080, debug=True) 


