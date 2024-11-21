# Recursive approach
def BinarySearch(arr, val):
    if not arr:
        print("value not found in the array")
        return False
    idx = len(arr) // 2
    if val < arr[idx]:
        BinarySearch(arr[:idx], val)
    elif val > arr[idx]:
        BinarySearch(arr[idx:], val)
    else:
        print(f"value is fount at index postion {idx}")
        return True


BinarySearch([1, 2, 3, 4, 5, 6, 7], 2)

# While loop


def BinarySearch(arr, val):
    if not arr:
        return False
    low, high = 0, len(arr)
    while low < high:
        mid = (low + high) // 2
        if val < arr[mid]:
            high = mid - 1
        elif val > arr[mid]:
            low = mid + 1
        else:
            print(f"{val} is found at index postion {mid}")
            return True
    print(f"{val} not found")
    return False


BinarySearch([1, 2, 3, 4, 5, 6, 7], 12)