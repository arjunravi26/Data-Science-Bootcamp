# from transformers import pipeline

# ner_pipeline = pipeline(
#     "ner", model="dbmdz/bert-large-cased-finetuned-conll03-english")

# text = "Barack Obama was born in Hawaii. He served as the President of the United States."

# ner_results = ner_pipeline(text)

# print("Named Entity Recognition Results:")
# for entity in ner_results:
#     # Each entity contains the word (or subword), its label, confidence score, and position in the text.
#     print(
#         f"Entity: {entity['word']}, Label: {entity['entity']}, Score: {entity['score']:.4f}, Start: {entity['start']}, End: {entity['end']}")


# import nltk
# from nltk import word_tokenize, pos_tag, ne_chunk

# # Ensure necessary nltk packages are downloaded
# nltk.download('punkt')
# nltk.download('averaged_perceptron_tagger')
# nltk.download('maxent_ne_chunker')
# nltk.download('words')

# # Input text
# text = "Barack Obama was born in Hawaii. He served as the President of the United States."

# # Tokenize the text into words
# tokens = word_tokenize(text)

# # Perform part-of-speech tagging
# pos_tags = pos_tag(tokens)

# # Perform Named Entity Chunking
# ne_tree = ne_chunk(pos_tags)

# print("nltk NER Results:")
# print(ne_tree)


import spacy

# Load a pre-trained English model
nlp = spacy.load("en_core_web_sm")

# Input text
text = "Barack Obama was born in Hawaii. He served as the President of the United States."

# Process the text with spaCy
doc = nlp(text)

# Print out named entities with their labels
print("spaCy NER Results:")
for ent in doc.ents:
    print(f"Entity: {ent.text}, Label: {ent.label_}")
