import numpy as np
import nltk
from nltk.corpus import stopwords
import re
import string 
import warnings
import random
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from fuzzywuzzy import fuzz


stopwords_list = stopwords.words('english')
warnings.filterwarnings("ignore")

def queries():
    with open("data.txt", "r", encoding = "UTF-8") as data_file:
        data = data_file.read()
        data = data.lower()
    data_file.close()
    
    return data 

text = queries()
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
    greeting_inputs = ["hello", "hi", "hey", "how is it going?", "how are you doing?", "what's up", "whats up", "hi there"]
    greeting_response = ["Hello", "Hi", "Hey", "How is it going?", "How are you doing?"]
        
    if greeting_sentence in greeting_inputs:
        return random.choices(greeting_response)[0]

def response(user_response):   
    bot_response = ""
    similar_scores = train(user_response)
     
    if not similar_scores:
        bot_response = bot_response + "I am unable to answer that question, sorry."

    else:
        i = 0
        while len(similar_scores) != 0:
            if i == 3:
                break
            idx = similar_scores.index(max(similar_scores))
            bot_response = bot_response + " " + sentence_tokens[idx].strip().capitalize() 
            i += 1
            similar_scores.remove(max(similar_scores))
            
    return bot_response

def train(user_response):
    TfidVec = TfidfVectorizer(tokenizer=LemNormalize, stop_words=stopwords_list)
    tfidf = TfidVec.fit_transform(sentence_tokens)
    vals = cosine_similarity(tfidf[-1], tfidf)
    similarity_scores = []

    for i in range(len(sentence_tokens) - 1):
        ratio = fuzz.token_set_ratio(sentence_tokens[i], user_response)
        weighted_score = vals[0][i] + (ratio / 100)
        similarity_scores.append(weighted_score) 

    return similarity_scores

def chat_flow(user_input):  
    bot_response = ""    
    user_response = user_response.lower()

    if "bye" in user_response:
        bot_response += "Bot: Goodbye!"

    else:
        if user_response.startswith("Thank".lower()):
            bot_reponse += "Bot: You are Welcome. Is that all"
            u_response += input("User: ")

            if u_response == "yes" or u_response == "yep":
                bot_response += "Bot: Goodbye!"

        else:
            if greetings(user_response) != None:
                bot_response += f"Bot: {greetings(user_response)}"
               
            else:
                sentence_tokens.append(user_response)
                bot_response += f"Bot: {response(user_response)}"
                sentence_tokens.remove(user_response)

    return bot_response


