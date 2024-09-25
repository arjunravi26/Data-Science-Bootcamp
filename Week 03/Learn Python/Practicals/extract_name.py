# Create a list comprehension that extracts the names of people older than 30 from a list of dictionaries, where each dictionary contains name and age as keys.
lst = [
    {"name":"Arjun","age":21},
    {"name":"John","age":26},
    {"name":"Doe","age":36},
    {"name":"Joe","age":56}
    ]
lst_name = [dct['name'] for dct in lst if dct['age']>30]
print(lst_name)