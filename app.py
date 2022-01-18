from distutils.log import debug
from flask import Flask, request, jsonify

from chat import get_response


app = Flask(__name__)

@app.route('/getresponse', methods=['GET'])
def get_answer():
    question = request.get_json().get("message")
    response = get_response(question)
    return jsonify({"answer": response})

if __name__ == "__main__":
    print("running")
    app.run(debug=True)