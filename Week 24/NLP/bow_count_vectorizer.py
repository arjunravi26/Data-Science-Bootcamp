from sklearn.feature_extraction.text import CountVectorizer

documents = [
    "The cat sat on the mat.",
    "The dog barked at the cat."
]


count_vectorizer = CountVectorizer()
X = count_vectorizer.fit_transform(documents)
print(X)

X = X.toarray()
print(count_vectorizer.get_feature_names_out())
print(X)
