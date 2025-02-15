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
    token = []
    for word in words:
        if word not in nltk.corpus.stopwords.words('english'):
            word2count[word] = word2count.get(word, 0) + 1
            token.append(word)
    tokens.append(token)
print(tokens)
print(word2count)

freq_words = heapq.nlargest(10, word2count, key=word2count.get)
print(freq_words)
# creating bow document matrix
doc_X = []
for data in sentences:
    vector = []
    for word in freq_words:
        if word in nltk.word_tokenize(data):
            vector.append(1)
        else:
            vector.append(0)
    doc_X.append(vector)
doc_X = np.asarray(doc_X)
print(doc_X)

# create bow word matrix
word_X = []
for word in freq_words:
    vector = []
    for data in sentences:
        if word in nltk.word_tokenize(data):
            vector.append(1)
        else:
            vector.append(0)
    word_X.append(vector)
word_X = np.array(word_X)
print(word_X)
word_df = pd.DataFrame(data=word_X, columns=['doc1', 'doc2', 'doc3'], index=freq_words)
print(word_df)

doc_df = pd.DataFrame(data=doc_X, columns=freq_words,index=['doc1', 'doc2', 'doc3'])
print(doc_df)





