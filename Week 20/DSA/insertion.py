def insertion(nums):
    n = len(nums)
    for i in range(1,n):
        j = i
        while j > 0 and nums[j] < nums[j-1]:
            nums[j-1],nums[j] = nums[j],nums[j-1]
            j-=1

        
numbers = [8, 1, 0, 90, 4, 5]
insertion(numbers)
print(numbers)
