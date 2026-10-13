"""ONNX model export: Convert and run a Scikit-Learn model with ONNX Runtime.

Lesson walkthrough:
    1. Fit source model: Train LogisticRegression and note the input feature count.
    2. Convert with signature: Declare a variable batch dimension and fixed width with `FloatTensorType`.
    3. Run inference: Use CPU ONNX Runtime, provide float32 features, and inspect output.

See README.md for concept explanations and a practice task.
"""
import numpy as np
import onnxruntime as ort
from sklearn.datasets import load_iris
from sklearn.linear_model import LogisticRegression
from skl2onnx import convert_sklearn
from skl2onnx.common.data_types import FloatTensorType

data = load_iris()
model = LogisticRegression(max_iter=500).fit(data.data, data.target)
onnx_model = convert_sklearn(
    model,
    initial_types=[("features", FloatTensorType([None, data.data.shape[1]]))],
)
session = ort.InferenceSession(
    onnx_model.SerializeToString(), providers=["CPUExecutionProvider"]
)
input_name = session.get_inputs()[0].name
onnx_predictions = session.run(
    None, {input_name: np.asarray(data.data[:3], dtype=np.float32)}
)[0]
source_predictions = model.predict(data.data[:3])
if not np.array_equal(source_predictions, onnx_predictions):
    raise RuntimeError("ONNX predictions do not match the fitted Scikit-Learn model")
print("Validated ONNX predictions:", onnx_predictions)
