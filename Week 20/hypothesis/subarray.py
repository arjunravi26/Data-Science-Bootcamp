# smallest subarray with a given sum
lst = [1,2,3,4,5]
k = 9
if k in lst:
    print(1)
n = len(lst)
for i in range(2,n+1):
    for j in range(n-i+1):
        s = sum(lst[j:j+i])
        if s == k:
            print(i)
            break
    if s==k:
        break
