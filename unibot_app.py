from flask import Flask, request
from Unibot import chat_flow

app = Flask(__name__)

@app.route('/chat_bot', methods=['POST'])
def respond():
    message = request.json['message']
    response = chat_flow()
    return response

if __name__ == "__main__":
    unibot_app.run()
