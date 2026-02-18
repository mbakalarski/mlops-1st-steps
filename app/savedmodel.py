"""
This model just computes y = 2x
This tiny model is perfect because:
- No training needed
- Deterministic output
- Fast to load
- Minimal dependencies
- Good for CI/CD testing
- Works with TensorFlow Serving
- Can be converted to ONNX
"""

import tensorflow as tf


class SimpleModel(tf.Module):
  @tf.function(input_signature=[tf.TensorSpec(shape=[None], dtype=tf.float32)])
  def __call__(self, x):
    return x * 2.0


if __name__ == "__main__":
  SAVED_MODEL_DIR = "_savedmodel"

  from pathlib import Path
  target_path = Path(__file__).resolve().parent.parent / SAVED_MODEL_DIR
  target_path.mkdir(parents=True, exist_ok=True)

  model = SimpleModel()
  tf.saved_model.save(model, target_path)

