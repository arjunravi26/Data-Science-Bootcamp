def factorial(num):
    fact = 1
    for i in range(2,num+1):
        fact *= i
    return fact
fact = factorial(5)
print(fact)
