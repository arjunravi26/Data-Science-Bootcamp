# Constant

import tensorflow as tf

# Graph Execution
print()
print(f"Example constant using graph execution")

@tf.function
def constant_funct():
    x = tf.constant([[1, 2, 3], [4, 5, 6]])
    print("Array is",x)
    tf.print("Array is ",x) # normal print doesnot works here
    tf.print(f"Name of array is: {x.name}")
    tf.print(f"Shape of array is: {x.shape}")
    tf.print(f"Data type of array is: {x.dtype}")

constant_funct()
print("_"*100)

# Eager Execution
print(f"Example constant using eager execution")
x = tf.constant([[1, 2, 3], [4, 5, 6]])
print(f"Array is {x}")
print(f"Shape of array is: {x.shape}")
print(f"Data type of array is: {x.dtype}")
