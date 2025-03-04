import tensorflow as tf

X = tf.constant([[1,2,3],[4,9,7]],dtype=tf.dtypes.float16)

print(tf.nn.softmax(X,axis=1))

print(tf.transpose(X))
print(tf.concat([X,X],axis=0))
print(tf.math.reduce_sum(X,axis=0)) # Perform operation between row(row-1[0] + row-2[0])
print(tf.math.reduce_sum(X,axis=1)) # Perform operation between col(col-1[0] + col-2[0])


# Check for gpu
tf.print(tf.config.list_physical_devices('GPU'))
tf.print(tf.config.list_physical_devices('CPU'))
if tf.config.list_physical_devices('GPU'):
    print("Tensorflow running on GPU")
else:
    print("Tensorflow does not have GPU")