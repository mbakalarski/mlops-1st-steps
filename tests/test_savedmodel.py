import tensorflow as tf


SAVED_MODEL_DIR = "../saved_model"


def test_saved_model_smoke():
    model = tf.saved_model.load(SAVED_MODEL_DIR)
    x = tf.constant([1.0, 2.0, 3.0])
    tf.debugging.assert_near(model(x), [2.0, 4.0, 6.0])


if __name__ == "__main__":
  test_saved_model_smoke()

