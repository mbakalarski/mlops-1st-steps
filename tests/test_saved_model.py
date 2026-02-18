import tensorflow as tf

SAVED_MODEL_DIR = "../saved_model"


loaded = tf.saved_model.load(SAVED_MODEL_DIR)

x = tf.constant([1.0, 2.0, 3.0])

print(loaded(x))  # Should print [2.0, 4.0, 6.0]

