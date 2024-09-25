# Write a decorator that logs the execution time of a function and apply it to a function that sorts a large list of integers.
import logging
from datetime import datetime

logging.basicConfig(level=logging.INFO)

lst = range(1,100)
def outer(fun):
    def inner(lst):
        logging.info(f"Time: {datetime.now()}")
        return fun(lst)
    return inner
    
@outer  
def func_sort(lst):
    total = 0
    for i in lst:
        total += i
    return total
print(func_sort(lst))