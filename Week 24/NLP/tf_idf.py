import pandas as pd
import nltk
import re
import numpy as np
nltk.download('punkt')
data = 'Hello My name is Arjun ad^aa. I am studying Data Science and Science. I am 21 year\'s old'

sentences = nltk.sent_tokenize(data)
print(sentences)

for i in range(len(sentences)):
    sentences[i] = sentences[i].lower()
    sentences[i] = re.sub('\W', ' ', sentences[i])
    sentences[i] = re.sub('\s+', ' ', sentences[i]).strip()
print(sentences)


# create vocabulary
vocab = set(
    [token for sentence in sentences for token in nltk.word_tokenize(sentence)])
print(vocab)


# TF(Term Frequency): c(w) / len(doc)
tf_freq = []
for sentence in sentences:
    words = nltk.word_tokenize(sentence)
    tf_freq.append([words.count(word) / len(words) for word in vocab])
tf_freq = np.array(tf_freq)
print(tf_freq)


# IDF(Inverse Doc Frequency): len(documents) / count(term in doc)
idf = []
no_of_documents = len(sentences)
for word in vocab:
    c = sum(1 for sentence in sentences if word in nltk.word_tokenize(sentence))
    idf_word = np.log((no_of_documents + 1) / (c + 1)) + 1
    idf.append(idf_word)

idf = np.array(idf)
print(idf)

tf_idf = tf_freq * idf
print(tf_idf)

index=[f'doc{i+1}' for i in range(len(sentences))]
df = pd.DataFrame(data=tf_idf, columns=list(
    vocab), index=index)
print(df)
