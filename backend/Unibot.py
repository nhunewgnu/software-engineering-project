import numpy as np
import nltk
import re
import string
import random
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from fuzzywuzzy import fuzz

with open("data.txt", "r", encoding="UTF-8") as data_file:
    text = data_file.read()
    text = text.lower()
    sentence_tokens = nltk.sent_tokenize(text)
    word_tokens = nltk.word_tokenize(text)


def LemNormalize(words_list):
    lem = nltk.stem.WordNetLemmatizer()
    remove_punctuations = dict((ord(punct), None) for punct in string.punctuation)
    words_string = ' '.join(words_list)
    tokens = nltk.word_tokenize(words_string.lower().translate(remove_punctuations))
    lemmatized = [lem.lemmatize(token) for token in tokens]
    return lemmatized


def greetings(greeting_sentence):
    greeting_inputs = ["hello", "hi", "hey", "how is it going?", "how are you doing?", "what's up", "whats up"]
    greeting_response = ["Hello", "Hi", "Hey", "How is it going?", "How are you doing?"]

    if greeting_sentence in greeting_inputs:
        return random.choice(greeting_response)


def response(user_response):
    bot_response = ""

    TfidVec = TfidfVectorizer(tokenizer=LemNormalize, stop_words="english")
    tfidf = TfidVec.fit_transform(sentence_tokens)
    vals = cosine_similarity(tfidf[-1], tfidf)
    similarity_scores = []

    for i in range(len(sentence_tokens) - 1):
        ratio = fuzz.token_set_ratio(sentence_tokens[i], user_response)
        weighted_score = vals[0][i] + (ratio / 100)
        similarity_scores.append(weighted_score)

    if not similarity_scores:
        bot_response = bot_response + "I am unable to answer that question, sorry."
    else:
        idx = similarity_scores.index(max(similarity_scores))
        bot_response = sentence_tokens[idx]

    return bot_response


def chat_flow(user_input):
    bot_response = ""
    flag = True
    bot_response += "Bot: Hi there! How can I assist you today?\n"

    while flag:
        user_response = user_input.lower()

        if "bye" in user_response:
            flag = False
            bot_response += "Bot: Goodbye!\n"

        else:
            if user_response.startswith("thank"):
                bot_response += "Bot: You are welcome. Is that all?\n"
                user_response = input("User: ")
                if user_response.lower() == "yes" or user_response.lower() == "yep":
                    bot_response += "Bot: Goodbye!\n"
                    flag = False

            else:
                if greetings(user_response) is not None:
                    bot_response += "Bot: " + greetings(user_response) + "\n"
                else:
                    sentence_tokens.append(user_response)
                    bot_response += f"Bot: {response(user_response)}\n"
                    sentence_tokens.remove(user_response)

    return bot_response
