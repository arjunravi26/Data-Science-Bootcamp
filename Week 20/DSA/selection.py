def selection(nums):
    n = len(nums)
    for i in range(n):
        small = i
        for j in range(1+i,n):
            if nums[small] > nums[j]:
                small = j
        if small != i:
            nums[i],nums[small] = nums[small],nums[i]

numbers = [8, 1, 0, 90, 4, 5]
selection(numbers)
print(numbers)
