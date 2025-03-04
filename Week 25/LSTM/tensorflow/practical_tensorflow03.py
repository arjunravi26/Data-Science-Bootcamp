import tensorflow as tf

X = tf.constant([[1,2,3],[4,9,7]],dtype=tf.dtypes.float16)

print(tf.nn.softmax(X,axis=1))
