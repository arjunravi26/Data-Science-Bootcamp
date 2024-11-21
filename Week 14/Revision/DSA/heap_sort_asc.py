def heapify(arr, n, i):
    left_idx = i * 2 + 1
    right_idx = i * 2 + 2
    largest = i
    if left_idx < n and arr[largest] < arr[left_idx]:
        largest = left_idx
    if right_idx < n and arr[largest] < arr[right_idx]:
        largest = right_idx
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)


def heap_sort(arr):
    ran = (len(arr) // 2) - 1
    n = len(arr)
    for i in range(ran, -1, -1):
        heapify(arr, n, i)
    for i in range(n-1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]
        heapify(arr, i, 0)
    print(arr)
    return arr


heap_sort([30, 8, 9, 0, 12, 67, 65])
