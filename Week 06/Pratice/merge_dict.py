# Write a Python program to merge two dictionaries.
dct1 = {'a':1,'b':2}
dct2 = {'c':3,'d':9}
dct1.update(dct2)
dct3 = {**dct1,**dct2}
print(dct1)
print(dct3)

# Create a dictionary from two lists, one containing keys and the other containing values.
lst1 = [1,2,3,4]
lst2 = ['a','b','c','d']
dct3 = {}
dct3 = dict(zip(lst2,lst1))
print(dct3)

d = {'a': 1}
value = d.setdefault('b', 2)
print(value)  # Output: 2
print(d)  # Output: {'a': 1, 'b': 2}
d = dict({'a':1})
print(d)
