import pandas as pd
import nltk
import re
import numpy as np

data = 'Hello My name is Arjun ad^aa. I am studying Data Science and Science. I am 21 year\'s old'

sentences = nltk.sent_tokenize(data)
print(sentences)

for i in range(len(sentences)):
    sentences[i] = sentences[i].lower()
    sentences[i] = re.sub('\W', ' ', sentences[i])
    sentences[i] = re.sub('\s+', ' ', sentences[i])
print(sentences)

# TF(Term Frequency): c(w) / len(doc)
words = set()
for sentence in sentences:
    tokens = nltk.word_tokenize(sentence)
    for token in tokens:
        words.add(token)

