def quick(nums):
    if len(nums) <= 1:
        return nums
    p = nums[0]
    left = []
    right = []
    pivot = []
    for i in nums:
        if i < p:
            left.append(i)
        elif i > p:
            right.append(i)
        else:
            pivot.append(i)
    return quick(left) + pivot + quick(right)

numbers = [8, 1, 0, 90, 4, 5]
numbers = quick(numbers)
print(numbers)