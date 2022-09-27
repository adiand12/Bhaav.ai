import nltk
import pickle
import pandas as pd
from nltk.corpus import stopwords
from textblob import Word
from collections import Counter
from keras.models import Sequential
from keras.preprocessing.text import Tokenizer
from keras.preprocessing.sequence import pad_sequences
from tensorflow.keras import models


def predictions(txt):
    #LOADING TOKENIZER
    with open('tokenizer.pickle', 'rb') as handle:
        tokenizer = pickle.load(handle)
    #MODEL PREDICTIONS 
    new_model = models.load_model("Bhaav77")
    emb = tokenizer.texts_to_sequences([txt])
    emb = pad_sequences(emb,maxlen=483)
    predict_x = new_model.predict(emb) 
    positive = predict_x[0][0]
    negative = predict_x[0][1]
    result = ''
    if positive>negative:
        result='Positive'
    else:
        result='Negative'
    
    return [result, positive, negative]
