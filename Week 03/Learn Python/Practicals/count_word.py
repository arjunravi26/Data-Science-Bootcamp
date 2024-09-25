
# Given a sentence, create a dictionary where the keys are the words in the sentence and the values are the number of times each word appears.
sentence = "Hai My Name is Arjun Hai Arjun"
sentence = sentence.lower().split()
dct = {}
for sen in sentence:
    if sen in dct:
        dct[sen] += 1
    else:
        dct[sen] = 1
print(dct)
   