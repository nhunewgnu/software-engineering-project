from flask import Flask, request, render_template, jsonify
from Unibot import chat_flow

unibot_app = Flask(__name__)

unibot_app.config["TEMPLATES_AUTO_RELOAD"] = True

@unibot_app.route('/')
def home():
    return render_template('unibot.html')

@unibot_app.route('/chat_bot', methods=['POST'])
def respond():
    user_input = request.get_json()['message']
    response = chat_flow(user_input)
    return jsonify(response)

if __name__ == "__main__":
    unibot_app.run(host='0.0.0.0', port=5000)
