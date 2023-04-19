import numpy as np
import nltk
import re
import string
import random
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


f = open("data.txt", "r", errors='ignore')
text = f.read()

text = text.lower()
sentence_tokens = nltk.sent_tokenize(text)


def LemNormalize(doc):
   lem = nltk.stem.WordNetLemmatizer()
   remove_punctuations = dict((ord(punct), None) for punct in string.punctuation)
   tokens = nltk.word_tokenize(doc.lower().translate(remove_punctuations))
   lemmatized = [lem.lemmatize(token) for token in tokens]
   return lemmatized

def greetings(greeting_sentence):
   greeting_inputs = ["hello", "hi", "hey", "how is it going?", "how are you doing?", "what's up", "whats up"]
   greeting_response = ["Hello", "Hi", "Hey", "How is it going?", "How are you doing?"]

   if greeting_sentence in greeting_inputs:
       return random.choice(greeting_response)

def response(user_response):
   robo1_response = ''
   TfidfVec = TfidfVectorizer(tokenizer=LemNormalize, stop_words='english')
   tfidf = TfidfVec.fit_transform(sentence_tokens)
   vals = cosine_similarity(tfidf[-1], tfidf)
   idx = vals.argsort()[0][-2]
   flat = vals.flatten()
   flat.sort()
   req_tfidf = flat[-2]
   if req_tfidf == 0:
       robo1_response = robo1_response + "I am sorry. Unable to understand you!"
       return robo1_response

   else:
       robo1_response = robo1_response + sentence_tokens[idx]
       return robo1_response


def chat_flow(user_response):
    word_tokens = nltk.word_tokenize(text)

    if (user_response == "bye"):
        return "Bot: Goodbye!"
    elif (user_response.startswith("Thank".lower())):
        return "Bot: You are Welcome. Is that all"
    elif (greetings(user_response) != None):
        return "Bot: " + greetings(user_response)
    else:
        sentence_tokens.append(user_response)
        word_tokens = nltk.word_tokenize(text)
        word_tokens += nltk.word_tokenize(user_response)
        final_words = list(set(word_tokens))
        bot_response = response(user_response)
        sentence_tokens.remove(user_response)
        return bot_response
