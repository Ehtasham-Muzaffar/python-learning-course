# Interactive Plotly charts

> **Phase 3: Data Visualization and Exploratory Analysis | Lesson 04 of 4** | Beginner+ | 30 minutes

Create an interactive Plotly scatter chart with hover information.

**Keywords:** Plotly Python, interactive charts, dashboards.

[Phase guide](../README.md) | [Runnable Python script](lesson.py) | [Course home](../../README.md)

## What you will learn

Build the concepts before memorizing syntax. Read each step, find the matching idea in `lesson.py`, run it, and change the example.

## Concepts to understand

- **Interactive figure:** Plotly stores data and layout for hover, zoom, and sharing.
- **Scatter plot:** Each point encodes two measurements; color can distinguish a category.
- **Hover data:** Extra values appear on demand without crowding the chart.

## Before you begin

Pandas columns, scatter plots, and core requirements installed.

## Step-by-step walkthrough

1. **Prepare tidy data.** Map target codes to readable species labels.

2. **Select encodings.** Map measurements to axes and species to color.

3. **Inspect and share.** The script saves a self-contained chart to `.outputs/iris_interactive.html`; open it in a browser and inspect hover details.

## Run the Python example

From the repository root, run:

```bash
python 03-visualization/04-interactive-plotly/lesson.py
```

The script prints the path to the generated interactive chart.

## Practice challenge

Add another useful measurement to the chart's hover details.

**Checkpoint:** Explain the input, operation, and what the output can and cannot tell you.

## Common mistake to avoid

Interactivity cannot fix unclear units, scales, or labels; annotate charts for their audience.

## Continue the course

[Next phase: Phase 4: Applied Machine Learning](../../04-machine-learning/README.md)
