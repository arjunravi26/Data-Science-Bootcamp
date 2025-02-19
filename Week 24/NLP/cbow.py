from sklearn.metrics.pairwise import euclidean_distances
from keras._tf_keras.keras.utils import model_to_dot
from IPython.display import SVG
import numpy as np
import pandas as pd
import keras._tf_keras.keras.backend as K
from keras._tf_keras.keras.models import Sequential
from keras._tf_keras.keras.layers import Dense, Embedding, Lambda
from keras._tf_keras.keras.preprocessing import text
from keras._tf_keras.keras.utils import to_categorical
from keras._tf_keras.keras.preprocessing import sequence


def get_data(file_path):
    bible_df = pd.read_csv(file_path)
    norm_bible = bible_df['t']
    return norm_bible


def preprocess_data(norm_bible):
    tokenizer = text.Tokenizer()
    tokenizer.fit_on_texts(norm_bible)
    word2id = tokenizer.word_index
    # build vocabulary of unique words
    word2id['PAD'] = 0
    id2word = {v: k for k, v in word2id.items()}
    wids = [[word2id[w]
             for w in text.text_to_word_sequence(doc)] for doc in norm_bible]
    vocab_size = len(word2id)
    embed_size = 100
    window_size = 2
    print('Vocabulary Size:', vocab_size)
    print('Vocabulary Sample:', list(word2id.items())[:10])
    return wids, id2word, embed_size, word2id, window_size, vocab_size


def generate_context_word_pairs(corpus, window_size, vocab_size):
    context_length = window_size*2
    for words in corpus:
        sentence_length = len(words)
        for index, word in enumerate(words):
            context_words = []
            label_word = []
            start = index - window_size
            end = index + window_size + 1

            context_words.append([words[i]
                                 for i in range(start, end)
                                 if 0 <= i < sentence_length
                                 and i != index])
            label_word.append(word)

            x = sequence.pad_sequences(context_words, maxlen=context_length)
            y = to_categorical(label_word, vocab_size)
            yield (x, y)


# Test this out for some samples
i = 0
file_path = 'dataset\\t_kjv.csv'
norm_bible = get_data(file_path=file_path)
wids, id2word, embed_size, word2id, window_size, vocab_size = preprocess_data(
    norm_bible)

for x, y in generate_context_word_pairs(corpus=wids, window_size=window_size, vocab_size=vocab_size):
    if 0 not in x[0]:
        print('Context (X):', [id2word[w] for w in x[0]],
              '-> Target (Y):', id2word[np.argwhere(y[0])[0][0]])

        if i == 10:
            break
        i += 1

# build CBOW architecture


def build_CBOW(vocab_size, embed_size, window_size):
    cbow = Sequential()
    cbow.add(Embedding(input_dim=vocab_size,
                       output_dim=embed_size, input_length=window_size*2))
    cbow.add(Lambda(lambda x: K.mean(x, axis=1), output_shape=(embed_size,)))
    cbow.add(Dense(vocab_size, activation='softmax'))
    cbow.compile(loss='categorical_crossentropy', optimizer='rmsprop')

    # view model summary
    print(cbow.summary())

    for epoch in range(1, 6):
        loss = 0.
        i = 0
        for x, y in generate_context_word_pairs(corpus=wids, window_size=window_size, vocab_size=vocab_size):
            i += 1
            loss += cbow.train_on_batch(x, y)
            if i % 100000 == 0:
                print('Processed {} (context, word) pairs'.format(i))

        print('Epoch:', epoch, '\tLoss:', loss)
        print()
        weights = cbow.get_weights()[0]

    return cbow, weights


cbow, weights = build_CBOW(vocab_size, embed_size, window_size)


weights = weights[1:]
print(weights.shape)

pd.DataFrame(weights, index=list(id2word.values())[1:]).head()

# compute pairwise distance matrix
distance_matrix = euclidean_distances(weights)
print(distance_matrix.shape)

# view contextually similar words
similar_words = {search_term: [id2word[idx] for idx in distance_matrix[word2id[search_term]-1].argsort()[1:6]+1]
                 for search_term in ['god', 'jesus', 'noah', 'egypt', 'john', 'gospel', 'moses', 'famine']}

print(similar_words)
SVG(model_to_dot(cbow, show_shapes=True, show_layer_names=False,
                 rankdir='TB').create(prog='dot', format='svg'))
