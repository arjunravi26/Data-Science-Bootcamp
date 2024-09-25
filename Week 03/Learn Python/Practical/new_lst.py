lst1 = ['apple','orange','grapes']
lst2 = ['banana','carrot','apple']
lst = []
# lst.extend(set(lst1,lst2))
lst1.extend(lst2)
lst = set(lst1)
lst = list(lst)
print(lst)