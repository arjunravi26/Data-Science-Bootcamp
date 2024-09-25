lst1 = [1, 2, 3, 4, 5]
lst2 = [6, 7, 8, 9, 10]
dct = {}
# for val1,val2 in zip(lst1,lst2):
#     dct[val1] = val2
dct = {val1:val2 for val1,val2 in zip(lst1,lst2)}
print(dct)