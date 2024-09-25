gfg = "arjun"
print("".join(reversed(gfg)))
lst = [i for i in gfg]
print(lst)
gfg = ''.join(lst)
print(gfg)
lst1 = [1,2,3]
lst2 = [4,5,6]
merge_lst = [(a,b) for a in lst1 for b in lst2]
print(merge_lst)
st1 = {2,3,4}
st2 = {3,4,5}
print(st1.union(st2))
print(st1)
print(st1.intersection(st2))
print(st1)
print(st1.difference(st2))
print(st2.symmetric_difference(st1))
print(st1.issubset(st2))