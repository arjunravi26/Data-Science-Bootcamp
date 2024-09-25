# odd - 2
# even - 3
lst = [1,2,3,4,5]
lst = [i**3 if i%2 == 0 else i**2 for i in lst]
print(lst)