from flask import Flask, request, jsonify
from flask_cors import CORS
from chat import get_response



app = Flask(__name__)
CORS(app)

@app.route('/', methods=['GET'])
def home():
    return "<h1>Working!</h1>"


@app.route('/getresponse', methods=['POST'])
def get_answer():
    question = request.get_json().get("message")
    response = get_response(question)
    return jsonify({"answer": response})

if __name__ == "__main__":
    app.run()