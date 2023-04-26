from flask import Flask, request, render_template, jsonify
from Unibot import chat_flow
import warnings
import logging

app = Flask(__name__, template_folder="templates")

app.config["TEMPLATES_AUTO_RELOAD"] = True

@app.route('/')
def home():
    return render_template('unibot.html')

# Chatbot route endpoint
@app.route('/chat_bot', methods=['POST'])
def respond():
    user_input = request.get_json()['message']
    response = chat_flow(user_input) # use the chat_flow method of the unibot object
    return jsonify(response)

# Add a new route for the login page
@app.route('/login', methods=['GET'])
def login():
    return render_template('login.html')

# Add a new route for the signup page
@app.route('/sign-up', methods=['GET'])
def signup():
    return render_template('sign-up.html')

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
