#COMANDS
#python -m venv venv
#.\venv\Scripts\activate
import model
#framework
from flask import Flask, jsonify, make_response

#instance this baby
app = Flask(__name__)

@app.route("/a", methods=['GET'])
def hi_py():
    return make_response(
      jsonify(
        data = "hy py"
      )
    )

app.run(debug=True, port=8080)
