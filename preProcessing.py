import nltk
from nltk import PorterStemmer
import numpy as np

stemmer = PorterStemmer()

def tokenize(sentence):
    return nltk.word_tokenize(sentence)

def stem(word):
    return stemmer.stem(word.lower())

def bag_of_words(tokenized_sentence,all_words):
    """
    sentence = ["Hello","how","are","you"]
    words = ["hi","hello","I","you","bye","thank","cool"]
    bag =   [  0 ,   1   , 0 ,  1   , 0   ,  0   ,   0  ]
    """
    tokenized_stemmed_sentence = [stem(w) for w in tokenized_sentence]
    bag = np.zeros(len(all_words),dtype=np.float32)
    for idx,w in enumerate(all_words):
        if w in tokenized_stemmed_sentence:
            bag[idx] = 1.0
    
    return bag

# sentence = ["Hello","how","are","you"]
# words = ["hi","hello","I","you","bye","thank","cool"]
# print(bag_of_words(sentence,words))


# words = ["Organize","organizes","organizing"]
# stemmed_words = [stem(w) for w in words]
# print(stemmed_words)