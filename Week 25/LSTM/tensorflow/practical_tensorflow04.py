import tensorflow as tf

X = tf.constant(5)
print(X.numpy())

a = tf.constant([[1, 2],[3, 4]])
b = tf.constant([[1, 1],[1, 1]])

print(tf.add(a, b), "\n")
print(tf.multiply(a, b), "\n")
print(tf.matmul(a, b), "\n")


print(a + b, "\n") # element-wise addition
print(a * b, "\n") # element-wise multiplication
print(a @ b, "\n") # matrix multiplication

a = tf.convert_to_tensor([1,2,3])
print(a)