def LinearSeach(arr, value):
    if not arr:
        print("Array is empty")
        return False
    for idx, val in enumerate(arr):
        if val == value:
            print(f"{value} found at index postion {idx}")
            return True
    print(f"{value} is not in the array {arr}")


LinearSeach([1, 2, 3, 5, 6, 9], 0)
LinearSeach([], 0)
LinearSeach([1, 2, 3, 5, 6, 9], 9)
