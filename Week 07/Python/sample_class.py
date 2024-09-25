class Sample:
    def add():
        pass
    def __str__(self) -> str:
        return f"Sample"
    def __del__(self):
        print("Deleted")
sample = Sample()
print(sample)
del sample
# # List approach (memory-intensive)
# numbers = [i for i in range(1000000)]

# Generator approach (memory-efficient)
def number_gen():
    for i in range(1000000):
        yield i
print(next(number_gen()))
print(next(number_gen()))
print(next(number_gen()))
def fibonacci():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

fib_gen = fibonacci()
for _ in range(10):
    print(next(fib_gen))

# List comprehension
numbers_list = [x * 2 for x in range(5)]

# Generator expression
numbers_gen = (x * 2 for x in range(5))

print(numbers_list)  # Output: [0, 2, 4, 6, 8]
print(next(numbers_gen))  # Output: 0
print(next(numbers_gen))  # Output: 2
def echo_generator():
    while True:
        received = yield
        print(f"Received: {received}")

gen = echo_generator()
next(gen)  # Initialize the generator
gen.send("Hello")  # Output: Received: Hello
gen.send("World")  # Output: Received: World

