import nltk
from nltk.stem import PorterStemmer  # it will give u stem words/ root words
stemmer= PorterStemmer()

import json
import pickle
import numpy as np

words=[]  # pattern =i am standing in parking
classes=[]
word_tags_list=[]
ignore_words=["?","!",",",".","'s","'m"]

train_data_file=open("intents.json").read()
intents= json.loads(train_data_file)

def get_stem_words(words,ignore_words):
    stem_words=[]
    for word in words:
        if word not in ignore_words:
            w=stemmer.stem(word.lower())
            stem_words.append(w)
    return stem_words

def create_bot_corpus(words,classes,word_tags_list,ignore_words):
    

