from flask import Flask, render_template, request, jsonify
from Unibot import chat_flow
app = Flask(__name__)

@app.post("/predict")
def predict():
    text = request.get_json().get("message")
    response = chat_flow(text)
    message = {"answer": response}
    return jsonify(message)

if __name__ == "__main__":
    app.run(debug=True)
