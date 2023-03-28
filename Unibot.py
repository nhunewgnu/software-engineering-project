import numpy as np
import nltk
import re
import string
import random
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from fuzzywuzzy import fuzz


with open("data.txt", "r", encoding = "UTF-8") as data_file:
    text = data_file.read()
    text = text.lower()
    se_tokens = nltk.sent_tokenize(text)
    wo_tokens = nltk.word_tokenize(text)


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
    tfidf = TfidVec.fit_transform(se_tokens)
    vals = cosine_similarity(tfidf[-1], tfidf)
    similarity_scores = []

    for i in range(len(se_tokens) - 1):
        ratio = fuzz.token_sort_ratio(se_tokens[i], user_response)
        weighted_score = vals[0][i] + (ratio / 100)
        similarity_scores.append(weighted_score)

    if not similarity_scores:
        bot_response = bot_response + "I am unable to answer that question, sorry."

    else:
        idx = similarity_scores.index(max(similarity_scores))
        bot_response = se_tokens[idx]

    return bot_response

def chat_flow():

    flag = True
    print("Bot: Hi there! How can I assist you today?")

    while(flag):
        user_response = input("User: ")
        user_response = user_response.lower()

        if("bye" in user_response):
            flag = False
            print("Bot: Goodbye!")

        else:
            if(user_response.startswith("Thank".lower())):
                print("Bot: You are Welcome. Is that all")

                u_response = input("User: ")
                if(u_response == "yes" or u_response == "yep"):
                    print("Bot: Goodbye!")
                    flag = False

            else:
                if(greetings(user_response) != None):
                    print("Bot: " + greetings(user_response))

                else:
                    se_tokens.append(user_response)
                    wo_tokens.extend(nltk.word_tokenize(user_response))
                    final_words = list(set(wo_tokens))
                    print(f"Bot: {response(user_response)}")
                    se_tokens.remove(user_response)

chat_flow()
