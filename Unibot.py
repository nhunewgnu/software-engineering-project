import numpy as np
import nltk
import re
import string
import random
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def read_file():
    with open("data.txt", "r", encoding = "UTF-8") as data_file:
        text = data_file.read()
        text = text.lower()
    return text

def tokens(text):
    sentence_tokens = nltk.sent_tokenize(text)
    word_tokens = nltk.word_tokenize(text)

def LemNormalize():
    text = read_file()
    remove_punctuations = dict((ord(punct), None) for punct in string.punctuation)
    lem = nltk.stem.WordNetLemmatizer()
    tokens = nltk.word_tokenize(text.lower().translate(remove_punctuations))
    return [lemmer.lemmatize(token) for token in tokens]

def greetings(greeting_sentence):
    greeting_inputs = ["Hello", "Hi", "Hey", "How is it going?", "How are you doing?", "What's up", "Whats up"]
    greeting_response = ["Hello", "Hi", "Hey", "How is it going?", "How are you doing?"]

    for word in greeting_sentence:
        if word.lower() in greeting_inputs:
            return random.choice(greeting_response)

def response(user_response):
    text = read_file()
    sentence_tokens = nltk.sent_tokenize(text)
    word_tokens = nltk.word_tokenize(text)
    bot_response = ""
    TfidVec = TfidVectorizer(tokenizer = LemNormalize(), stop_words = "english")
    tfidf = TfidVec.fit_transform(sentece_tokens)
    vals = cosine_similarity(tfidf[-1], tfidf)
    idx = vals.argsort()[0][-2]
    flat = vals.flatten()
    flat.sort()
    req_tfidf = flat[-2]

    if(req_tfidf == 0):
        bot_response = bot_response + "I am unable to answer that question, sorry."
    else:
        bot_response = bot_response + sentence_tokens[idx]

    return bot_response

def chat_flow():
    flag = True
    print("Hello! I am Unibot. Please type any questions you might have")

    while(flag):
        user_response = input()
        user_response = user_response.lower()

        if(user_response == "bye"):
            flag = false
            print("Bot: Goodbye!")

        else:
            if(user_response.startswith("Thank"):


read_file()
