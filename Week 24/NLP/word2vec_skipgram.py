import nltk
import gensim
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from gensim.models import Word2Vec
from sklearn.decomposition import PCA

# Download necessary resources
nltk.download('punkt')
nltk.download('stopwords')

# Sample text corpus
text = """
Word embeddings are a type of word representation that allows words to be represented as numerical vectors.
These vectors capture semantic relationships between words.
Word2Vec is a popular technique used to learn word embeddings efficiently.
letter are used study.
"""
def get_data(file_path):
    bible_df = pd.read_csv(file_path)
    norm_bible = bible_df['t']
    return norm_bible

file_path = 'dataset\\t_kjv.csv'
text = get_data(file_path)
text = str(text.astype(str).to_list())
print(text)

# **Step 1: Preprocessing**
def preprocess_text(text):
    tokens = word_tokenize(text.lower())  # Convert to lowercase & tokenize
    tokens = [word for word in tokens if word.isalnum()]  # Remove punctuations
    stop_words = set(stopwords.words("english"))
    tokens = [word for word in tokens if word not in stop_words]  # Remove stopwords
    return tokens

# Tokenize and prepare data
tokens = preprocess_text(text)
print("Tokenized Words:", tokens)

# Create a list of sentences (Word2Vec requires a list of lists)
sentences = [tokens]

# **Step 2: Train Word2Vec Model**
model = Word2Vec(sentences, vector_size=10, window=2, min_count=1, sg=1)  # Skip-gram model (sg=1)

# **Step 3: Find Similar Words**
word = "word"
if word in model.wv:
    print(f"\nWords similar to '{word}':")
    print(model.wv.most_similar(word))

# **Step 4: Visualize Word Embeddings**
def plot_embeddings(model):
    print('function')
    words = list(model.wv.index_to_key)
    print('vecotr')
    vectors = np.array([model.wv[word] for word in words])
    print('pca')

    # Reduce dimensions using PCA
    pca = PCA(n_components=2)
    reduced_vectors = pca.fit_transform(vectors)

    plt.figure(figsize=(8, 6))
    print('plotting')
    for i, word in enumerate(words):
        plt.scatter(reduced_vectors[i, 0], reduced_vectors[i, 1])
        plt.text(reduced_vectors[i, 0], reduced_vectors[i, 1], word, fontsize=12)

    plt.title("Word2Vec Embeddings (PCA Projection)")
    plt.show()

plot_embeddings(model)
