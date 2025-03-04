# Eager Exectuion(default) vs Graph Execution(Large Scale computation)

import tensorflow as tf
import time
# Eager execution
# tf.config.run_functions_eagerly(True) not needed for tensorflow 2X
start_time = time.time()
a = tf.constant(3)
b = tf.constant(5)
c = a + b
print(f"Result is {c}")
end_time = time.time()
print(f"Time taken is: {end_time-start_time}")


# Graph execution
start_time = time.time()


@tf.function
def add_func(a, b):
    return a * b + 10


a = tf.constant(3)
b = tf.constant(5)
c = add_func(a, b)
print(f"Result is {c}")
end_time = time.time()
print(f"Time taken is: {end_time-start_time}")
