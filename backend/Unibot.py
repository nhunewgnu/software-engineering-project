from spacy import load
import nltk
from nltk.corpus import stopwords
import string
import warnings
import random
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from fuzzywuzzy import fuzz

nlp = load("en_core_web_sm")
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


def LemNormalize(text):
    lem = nltk.stem.WordNetLemmatizer()
    remove_punctuations = dict((ord(punct), None) for punct in string.punctuation)
    tokens = nltk.word_tokenize(text.lower())
    filtered_tokens = [lem.lemmatize(token) for token in tokens if token.lower() not in stopwords_list]
    filtered_text = ' '.join(filtered_tokens)
    filtered_text = filtered_text.translate(remove_punctuations)

    return filtered_text

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
        score = max(similar_scores)
        if score < 0.78:
            bot_response = bot_response + "I am unable to answer that question, sorry.\
                                            \nCould you be more specific?"

        else:
            idx = similar_scores.index(score)
            bot_response = bot_response + sentence_tokens[idx].strip().capitalize()

        #i = 0
        #while len(similar_scores) != 0:
         #   if i == 3:
         #       break
          #  idx = similar_scores.index(max(similar_scores))
           # print(max(similar_scores))
          #  bot_response = bot_response + " " + sentence_tokens[idx].strip().capitalize()
           # i += 1
            #similar_scores.remove(max(similar_scores))

    return bot_response

def train(user_response):
    TfidVec = TfidfVectorizer(tokenizer=LemNormalize, stop_words=stopwords_list)
    tfidf = TfidVec.fit_transform(sentence_tokens)
    vals = cosine_similarity(tfidf[-1], tfidf)
    vals = vals.flatten()
    similarity_scores = []

    for i in range(len(sentence_tokens)):
        ratio = fuzz.token_set_ratio(sentence_tokens[i], user_response)
        weighted_score = vals[i] * (ratio / 100)
        similarity_scores.append(weighted_score)

    return similarity_scores

def chat_flow(user_input):  
    bot_response = ""    
    user_response = user_input.lower()

    if "bye" in user_response:
        bot_response += "Goodbye!"

    else:
        if user_response.startswith("Thank".lower()):
            bot_reponse += "You are Welcome. Is that all"
            u_response += input("User: ")

            if u_response == "yes" or u_response == "yep":
                bot_response += "Goodbye!"

        else:
            if greetings(user_response) != None:
                bot_response += greetings(user_response)
               
            else:
                sentence_tokens.append(user_response)
                bot_response += response(user_response)
                sentence_tokens.remove(user_response)

    return bot_response
