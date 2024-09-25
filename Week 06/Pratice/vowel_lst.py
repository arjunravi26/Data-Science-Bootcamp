vowels = ['a','e','i','o','u']
st = "aabevecvgguiro"
st_vow = [i for i in st if i in vowels]
print(set(sorted(st_vow)))