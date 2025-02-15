import heapq
import pandas as pd
import nltk
import re
import numpy as np

data = 'Hello My name is Arjun ad^aa. I am studying Data Science. I am 21 year\'s old'
# print(data)

sentences = nltk.tokenize.sent_tokenize(data)
print(sentences)
for i in range(len(sentences)):
    sentences[i] = sentences[i].lower()
    sentences[i] = re.sub('\W', ' ', sentences[i])
    sentences[i] = re.sub('\s+', ' ', sentences[i])
print(sentences)
tokens = []
word2count = {}
for sentence in sentences:
    words = nltk.tokenize.word_tokenize(sentence, preserve_line=True)
    tokens.append(words)
    print(tokens)
    for word in words:
        word2count[word] = word2count.get(word, 0) + 1
print(tokens)
print(word2count)


freq_words = heapq.nlargest(15, word2count, key=word2count.get)
print(freq_words)

X = []
for data in sentences:
    vector = []
    for word in freq_words:
        if word in nltk.word_tokenize(data):
            vector.append(1)
        else:
            vector.append(0)
    X.append(vector)
X = np.asarray(X)
print(X)
