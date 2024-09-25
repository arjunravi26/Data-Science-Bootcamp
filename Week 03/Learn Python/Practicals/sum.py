# Given a dictionary where the values are lists of integers, write a Python program to calculate the sum of all integers across all lists and return the result.
dct = {
    "key1":[1,2,4,5,6], 
    "key2":[5,6,8],
    "key3":[10,19],
}
total = 0
for value in dct.values():
    for val in value:
        total += val
print(total)