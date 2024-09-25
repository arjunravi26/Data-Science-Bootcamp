# Write a Python program that takes a string as input and counts the frequency of each vowel in the string, storing the result in a dictionary where the vowel is the key and the frequency is the value.
strs = "areijounareaiv"
dct = {}
VOWELS = "aeiou"
for st in strs:
    if st in dct:
        dct[st] +=1
    elif st in VOWELS:
        dct[st] = 1
print(dct)