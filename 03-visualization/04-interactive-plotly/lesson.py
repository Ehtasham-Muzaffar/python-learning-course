"""Interactive Plotly charts: Create an interactive Plotly scatter chart with hover information.

Lesson walkthrough:
    1. Prepare tidy data: Map target codes to readable species labels.
    2. Select encodings: Map measurements to axes and species to color.
    3. Inspect and share: Open the figure, inspect points, and use `figure.write_html("iris.html")` to export.

See README.md for concept explanations and a practice task.
"""
from pathlib import Path

import plotly.express as px
from sklearn.datasets import load_iris

data = load_iris(as_frame=True)
frame = data.frame
frame["species"] = frame["target"].map(dict(enumerate(data.target_names)))
figure = px.scatter(frame, x="sepal length (cm)", y="petal length (cm)", color="species", hover_data=["sepal width (cm)"])
output_dir = Path(__file__).resolve().parents[2] / ".outputs"
output_dir.mkdir(exist_ok=True)
output_path = output_dir / "iris_interactive.html"
figure.write_html(output_path)
print(f"Open the interactive chart in a browser: {output_path}")
