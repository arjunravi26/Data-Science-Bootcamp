# Question 2: Check if Two Strings are Anagrams
# Two strings are considered anagrams if they contain the same characters in the same frequencies but possibly in a different order. Given two strings, determine if they are anagrams of each other.

# Example:

# Input: "listen" and "silent"
# Output: True
dict1 = {}
dict2 = {}
text1 = "listen"
text2 = "silent"


def count(w, dict_count):
    if w in dict_count.keys():
        dict_count[w] += 1
    else:
        dict_count[w] = 1


if len(text1) != len(text2):
    print(False)
else:
    for w1, w2 in zip(text1, text2):
        count(w1, dict1)
        count(w2, dict2)
    print(dict1)
    print(dict2)
    print(dict1 == dict2)
