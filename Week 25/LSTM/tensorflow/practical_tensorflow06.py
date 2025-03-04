# Gradient and automatic differentiation

import numpy as np
import tensorflow as tf
from tensorflow.keras.layers import Dense
X = tf.Variable(3.0)

with tf.GradientTape() as tape:
    y = X ** 2 + 1

dx_dy = tape.gradient(y, X)
print(dx_dy)


w = tf.Variable(tf.random.normal((3, 2)), name='w')
b = tf.Variable(tf.zeros(2, dtype=tf.float32), name='b')
x = [[1., 2., 3.]]

with tf.GradientTape(persistent=True) as tape:
    y = x @ w + b
    loss = tf.reduce_mean(y**2)

[dl_dw, dl_db] = tape.gradient(loss, [w, b])
print(dl_dw,dl_db)

print(w.shape)
print(dl_dw.shape)


layer = Dense(units=16,activation='relu')
x = tf.constant([[1., 2., 3.]])

with tf.GradientTape() as tape:
    y = layer(x)
    loss = tf.reduce_mean(y**2)

grads = tape.gradient(loss,layer.trainable_variables)

print(grads[1])