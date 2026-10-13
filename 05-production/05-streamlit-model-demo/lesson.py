"""Streamlit model demo: Build an interactive Streamlit interface around a transparent baseline prediction.

Lesson walkthrough:
    1. Create a clear page: Set a title describing the demonstration.
    2. Collect input: The slider constrains the value range and provides a default.
    3. Show a labeled result: Display the baseline and explain that it is not a trained model.

See README.md for concept explanations and a practice task.
"""
import streamlit as st


def main() -> None:
    st.title("Model prediction demo")
    feature = st.slider("Input feature", min_value=0.0, max_value=100.0, value=50.0)
    st.metric("Baseline prediction", f"{feature * 0.5:.1f}")
    st.caption("Replace the baseline formula with your saved model pipeline.")


if __name__ == "__main__":
    main()
