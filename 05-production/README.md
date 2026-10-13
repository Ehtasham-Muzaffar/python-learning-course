# Phase 5: Deep Learning and Production Basics

**Goal:** Move from an in-memory experiment to a saved model and a small, usable interface.

The PyTorch and ONNX examples use optional dependencies; install them only for the relevant lessons. Model-serving examples are deliberately small teaching demos, not hardened production services.

## Learning path

1. [Understand PyTorch tensors and the training loop](01-pytorch-tensors-and-training/README.md) · [Script](01-pytorch-tensors-and-training/lesson.py)
2. [Save and reload a Scikit-Learn model](02-save-and-load-models/README.md) · [Script](02-save-and-load-models/lesson.py)
3. [Export and run a model with ONNX](03-onnx-model-export/README.md) · [Script](03-onnx-model-export/lesson.py)
4. [Serve predictions with FastAPI](04-fastapi-model-service/README.md) · [Script](04-fastapi-model-service/lesson.py)
5. [Build a prediction demo with Streamlit](05-streamlit-model-demo/README.md) · [Script](05-streamlit-model-demo/lesson.py)

**Finish line:** You can explain the basic training loop, preserve a fitted model, and expose an example prediction through a local API or app.

**Production reminder:** Real services additionally require threat modeling, authentication, monitoring, input constraints, data privacy controls, and deployment-specific testing.
