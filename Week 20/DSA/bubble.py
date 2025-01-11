def bubble(nums):
    n = len(nums)
    for i in range(n):
        ran = n - i - 1
        swapped = False
        for j in range(ran):
            if nums[j] > nums[j+1]:
                nums[j],nums[j+1] = nums[j+1],nums[j]
                swapped = True
        if not swapped:
            break

numbers = [8, 1, 0, 90, 4, 5]
bubble(numbers)
print(numbers)
