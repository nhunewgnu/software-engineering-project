from flask import Flask
from Unibot import chat_flow

app = Flask(__name__)

@app.route('/chat_bot')
def respond():
    chat_flow()

if __name__ == "__main__":
    unibot_app.run()
