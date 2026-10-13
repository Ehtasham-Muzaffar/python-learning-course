# Matplotlib fundamentals

> **Phase 3: Data Visualization and Exploratory Analysis | Lesson 01 of 4** | Beginner+ | 30 minutes

Build a labeled Matplotlib figure and make its visual encodings clear.

**Keywords:** Matplotlib tutorial, Python charts, data visualization.

[Phase guide](../README.md) | [Runnable Python script](lesson.py) | [Course home](../../README.md)

## What you will learn

Build the concepts before memorizing syntax. Read each step, find the matching idea in `lesson.py`, run it, and change the example.

## Concepts to understand

- **Figure and axes:** The Figure is a canvas; an Axes is an individual plotting area.
- **Visual encoding:** A line connects ordered observations; markers and labels clarify what values mean.
- **Layout:** Tight layout reduces clipped labels; saving figures supports reuse.

## Before you begin

Lists or arrays, basic chart reading, and Phase 2 data lessons.

## Step-by-step walkthrough

1. **Define data and question.** Four ordered monthly counts make a line chart suitable for highlighting change.

2. **Create explicit axes.** `plt.subplots` returns the Figure and Axes so settings are targeted.

3. **Label and render.** Add title and units, adjust spacing, then display; `fig.savefig` exports a chart.

## Run the Python example

From the repository root, run:

```bash
python 03-visualization/01-matplotlib-fundamentals/lesson.py
```

A labeled line chart appears. Add `fig.savefig("chart.png")` to export a file.

## Practice challenge

Add a second series, legend, and exported PNG.

**Checkpoint:** Explain the input, operation, and what the output can and cannot tell you.

## Common mistake to avoid

Charts without units or context can mislead; select scales and marks that preserve meaning.

## Continue the course

[Next lesson: Seaborn statistical plots](../02-seaborn-statistical-plots/README.md)
