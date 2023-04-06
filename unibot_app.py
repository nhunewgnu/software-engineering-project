from flask import Flask, request
from Unibot import chat_flow

unibot_app = Flask(__name__)

@app.route('/chat_bot', methods=['POST'])
def respond():
    response = chat_flow()
    return response

if __name__ == "__main__":
    unibot_app.run(hosts='127.0.0.1', port=5000)
