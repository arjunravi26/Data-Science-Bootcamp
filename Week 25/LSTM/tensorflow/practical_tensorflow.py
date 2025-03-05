# Module
import tensorflow as tf

# Dense layer


class Dense(tf.Module):
    def __init__(self, in_features, out_features, name=None):
        super().__init__(name)
        self.w = tf.Variable(tf.random.normal(
            [in_features, out_features]), name='w')
        self.b = tf.Variable(3.0, name='b')

    def __call__(self, x):
        y = tf.matmul(x, self.w)
        return tf.nn.relu(y)


x = tf.constant([[1, 2, 3]], dtype=tf.float32)
dense = Dense(in_features=3, out_features=2)
y = dense(x)
print(y)

# Sequential


class SequentialModule(tf.Module):
    def __init__(self, name=None):
        super().__init__(name=name)

        self.dense_1 = Dense(in_features=3, out_features=3)
        self.dense_2 = Dense(in_features=3, out_features=2)

    def __call__(self, x):
        x = self.dense_1(x)
        return self.dense_2(x)


# You have made a model!
my_model = SequentialModule(name="the_model")

# Call it, with random results
print("Model results:", my_model(tf.constant([[2.0, 2.0, 2.0]])))
