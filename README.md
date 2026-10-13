# Complete Python for Data Science and Machine Learning: From Zero to Production

[![Python](https://img.shields.io/badge/Python-3.11%2B-3776AB?logo=python&logoColor=white)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![GitHub stars](https://img.shields.io/github/stars/YOUR_GITHUB_USERNAME/python-data-science-machine-learning-course?style=social)](https://github.com/YOUR_GITHUB_USERNAME/python-data-science-machine-learning-course/stargazers)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](CONTRIBUTING.md)
[![Code style: Ruff](https://img.shields.io/badge/code%20style-Ruff-D7FF64?logo=ruff&logoColor=black)](https://docs.astral.sh/ruff/)

Learn modern Python, data analysis, visualization, machine learning, and practical deployment through a free, project-oriented course. Each step-by-step Markdown lesson is paired with its own runnable Python script.

This open-source course is for complete beginners, aspiring data scientists, Python developers moving into machine learning, and anyone who wants a practical path from first program to a small production-ready model demo. It is 100% free: the lessons, example code, and community contributions are available under the MIT license.

**Suggested repository name:** `python-data-science-machine-learning-course`  
**Repository description (137 characters):** Free Python Course for Data Science & Machine Learning with Pandas, NumPy, Scikit-Learn, hands-on lessons, and production-ready projects.

**GitHub topics:** `python`, `python-course`, `data-science`, `machine-learning`, `pandas`, `numpy`, `scikit-learn`, `scipy`, `matplotlib`, `seaborn`, `plotly`, `pytorch`, `django`, `mysql`, `mongodb`, `fastapi`, `streamlit`, `python-dsa`, `beginner-friendly`, `education`

## Table of contents

- [What you'll learn](#what-youll-learn)
- [Course roadmap](#course-roadmap)
  - [Phase 1: Modern Python Core](#phase-1-modern-python-core)
  - [Phase 2: Data Manipulation and Analysis](#phase-2-data-manipulation-and-analysis)
  - [Phase 3: Data Visualization and EDA](#phase-3-data-visualization-and-eda)
  - [Phase 4: Applied Machine Learning](#phase-4-applied-machine-learning)
  - [Phase 5: Deep Learning and Production Basics](#phase-5-deep-learning-and-production-basics)
- [Extended topic library](#extended-topic-library)
- [Quickstart](#quickstart)
- [Repository structure](#repository-structure)
- [How to use the lessons](#how-to-use-the-lessons)
- [How to contribute](#how-to-contribute)
- [Star history](#star-history)
- [License](#license)

## What you'll learn

- Write clear, modern Python and manage isolated project environments.
- Analyze and clean real-world-shaped data with NumPy and Pandas.
- Communicate findings with Matplotlib, Seaborn, and interactive Plotly charts.
- Train, evaluate, and tune reproducible Scikit-Learn models.
- Explore a PyTorch training loop and package models behind lightweight web demos.

## Course roadmap

Each lesson has its own `README.md` explaining the concepts step by step and a matching `lesson.py` you can run and edit. Open a lesson guide first, then follow along in its Python file.

### [Phase 1: Modern Python Core](01-python-core/README.md)

| Lesson | Learning outcome |
|---|---|
| [`01-python-core/01-environment-and-first-program/`](01-python-core/01-environment-and-first-program/README.md) · [Python](01-python-core/01-environment-and-first-program/lesson.py) | Set up a Python 3.11+ virtual environment, install project dependencies, and run a first reproducible Python program. **Keywords:** Python course, virtual environment, Python setup. |
| [`01-python-core/02-types-and-data-structures/`](01-python-core/02-types-and-data-structures/README.md) · [Python](01-python-core/02-types-and-data-structures/lesson.py) | Use Python types, strings, lists, dictionaries, tuples, and sets to represent and inspect data safely. **Keywords:** Python data types, collections, beginner Python. |
| [`01-python-core/03-control-flow-and-iteration/`](01-python-core/03-control-flow-and-iteration/README.md) · [Python](01-python-core/03-control-flow-and-iteration/lesson.py) | Apply conditions, loops, comprehensions, and exceptions to process records and handle invalid input. **Keywords:** Python control flow, loops, comprehensions. |
| [`01-python-core/04-functions-and-modules/`](01-python-core/04-functions-and-modules/README.md) · [Python](01-python-core/04-functions-and-modules/lesson.py) | Build reusable, typed functions and modules with clear inputs, outputs, and docstrings. **Keywords:** Python functions, type hints, modular code. |
| [`01-python-core/05-classes-and-oop/`](01-python-core/05-classes-and-oop/README.md) · [Python](01-python-core/05-classes-and-oop/lesson.py) | Model related data and behavior with simple classes, dataclasses, and composition. **Keywords:** Python OOP, classes, dataclasses. |

### [Phase 2: Data Manipulation and Analysis](02-data-analysis/README.md)

| Lesson | Learning outcome |
|---|---|
| [`02-data-analysis/01-numpy-arrays/`](02-data-analysis/01-numpy-arrays/README.md) · [Python](02-data-analysis/01-numpy-arrays/lesson.py) | Create and reshape NumPy arrays, inspect dimensions, and compute summary statistics efficiently. **Keywords:** NumPy tutorial, numerical Python, arrays. |
| [`02-data-analysis/02-pandas-dataframes/`](02-data-analysis/02-pandas-dataframes/README.md) · [Python](02-data-analysis/02-pandas-dataframes/lesson.py) | Load, inspect, select, filter, and aggregate tabular data with Pandas DataFrames. **Keywords:** Pandas tutorial, DataFrame, data analysis. |
| [`02-data-analysis/03-data-cleaning/`](02-data-analysis/03-data-cleaning/README.md) · [Python](02-data-analysis/03-data-cleaning/lesson.py) | Diagnose missing values, remove duplicates, fix data types, and document defensible cleaning choices. **Keywords:** data cleaning with Pandas, missing data, preprocessing. |
| [`02-data-analysis/04-vectorization-and-feature-prep/`](02-data-analysis/04-vectorization-and-feature-prep/README.md) · [Python](02-data-analysis/04-vectorization-and-feature-prep/lesson.py) | Replace row-wise work with vectorized NumPy/Pandas operations and prepare numeric features for modeling. **Keywords:** vectorization, feature engineering, Pandas performance. |

### [Phase 3: Data Visualization and EDA](03-visualization/README.md)

| Lesson | Learning outcome |
|---|---|
| [`03-visualization/01-matplotlib-fundamentals/`](03-visualization/01-matplotlib-fundamentals/README.md) · [Python](03-visualization/01-matplotlib-fundamentals/lesson.py) | Build and label clear Matplotlib charts, customize axes, and export publication-ready figures. **Keywords:** Matplotlib tutorial, Python charts, data visualization. |
| [`03-visualization/02-seaborn-statistical-plots/`](03-visualization/02-seaborn-statistical-plots/README.md) · [Python](03-visualization/02-seaborn-statistical-plots/lesson.py) | Compare distributions and relationships using Seaborn statistical plots and categorical charts. **Keywords:** Seaborn tutorial, statistical visualization, Python EDA. |
| [`03-visualization/03-exploratory-data-analysis/`](03-visualization/03-exploratory-data-analysis/README.md) · [Python](03-visualization/03-exploratory-data-analysis/lesson.py) | Combine descriptive statistics and visual checks into a repeatable exploratory data analysis workflow. **Keywords:** exploratory data analysis, EDA, data science workflow. |
| [`03-visualization/04-interactive-plotly/`](03-visualization/04-interactive-plotly/README.md) · [Python](03-visualization/04-interactive-plotly/lesson.py) | Create interactive Plotly charts with hover details and save them as shareable HTML. **Keywords:** Plotly Python, interactive charts, dashboards. |

### [Phase 4: Applied Machine Learning](04-machine-learning/README.md)

| Lesson | Learning outcome |
|---|---|
| [`04-machine-learning/01-train-test-split-and-preprocessing/`](04-machine-learning/01-train-test-split-and-preprocessing/README.md) · [Python](04-machine-learning/01-train-test-split-and-preprocessing/lesson.py) | Prevent data leakage by splitting data first and fitting preprocessing inside Scikit-Learn pipelines. **Keywords:** Scikit-Learn preprocessing, train-test split, ML pipeline. |
| [`04-machine-learning/02-regression/`](04-machine-learning/02-regression/README.md) · [Python](04-machine-learning/02-regression/lesson.py) | Train a baseline regression model and interpret predictions and error in original units. **Keywords:** machine learning regression, LinearRegression, Scikit-Learn. |
| [`04-machine-learning/03-classification/`](04-machine-learning/03-classification/README.md) · [Python](04-machine-learning/03-classification/lesson.py) | Train a classifier and inspect class probabilities, precision, recall, and a confusion matrix. **Keywords:** classification, logistic regression, Scikit-Learn. |
| [`04-machine-learning/04-clustering/`](04-machine-learning/04-clustering/README.md) · [Python](04-machine-learning/04-clustering/lesson.py) | Scale features and use K-Means clustering to explore unlabeled groups and their limitations. **Keywords:** unsupervised learning, K-Means, clustering. |
| [`04-machine-learning/05-model-evaluation-and-cross-validation/`](04-machine-learning/05-model-evaluation-and-cross-validation/README.md) · [Python](04-machine-learning/05-model-evaluation-and-cross-validation/lesson.py) | Choose task-appropriate metrics and estimate generalization with stratified cross-validation. **Keywords:** model evaluation, cross-validation, ML metrics. |
| [`04-machine-learning/06-hyperparameter-tuning/`](04-machine-learning/06-hyperparameter-tuning/README.md) · [Python](04-machine-learning/06-hyperparameter-tuning/lesson.py) | Search model parameters with a reproducible Scikit-Learn pipeline and compare results on held-out data. **Keywords:** hyperparameter tuning, GridSearchCV, model selection. |

### [Phase 5: Deep Learning and Production Basics](05-production/README.md)

| Lesson | Learning outcome |
|---|---|
| [`05-production/01-pytorch-tensors-and-training/`](05-production/01-pytorch-tensors-and-training/README.md) · [Python](05-production/01-pytorch-tensors-and-training/lesson.py) | Build a small PyTorch tensor workflow and understand the forward, loss, backward, and optimizer training loop. **Keywords:** PyTorch for beginners, deep learning, tensors. |
| [`05-production/02-save-and-load-models/`](05-production/02-save-and-load-models/README.md) · [Python](05-production/02-save-and-load-models/lesson.py) | Persist a fitted Scikit-Learn pipeline with Joblib and verify predictions after loading it. **Keywords:** save machine learning model, Joblib, model serialization. |
| [`05-production/03-onnx-model-export/`](05-production/03-onnx-model-export/README.md) · [Python](05-production/03-onnx-model-export/lesson.py) | Export and run a portable ONNX model and verify predictions using ONNX Runtime. **Keywords:** ONNX, model deployment, interoperable machine learning. |
| [`05-production/04-fastapi-model-service/`](05-production/04-fastapi-model-service/README.md) · [Python](05-production/04-fastapi-model-service/lesson.py) | Expose validated model predictions through a small FastAPI endpoint with a typed request schema. **Keywords:** FastAPI machine learning API, model serving, REST API. |
| [`05-production/05-streamlit-model-demo/`](05-production/05-streamlit-model-demo/README.md) · [Python](05-production/05-streamlit-model-demo/lesson.py) | Turn model predictions into an approachable Streamlit interface that can run locally. **Keywords:** Streamlit machine learning app, model demo, data app. |

## Extended topic library

Want to go beyond the core data-science roadmap? These supplementary tracks cover the Python topics and technologies you listed. Each topic is an independent mini-project with its own Markdown guide describing its **purpose and use**, plus a runnable Python example. Open a track index to browse its projects.

| Track | Topics covered |
|---|---|
| [Python language fundamentals](06-python-language/README.md) | Syntax, output, comments, variables, types, strings, collections, conditions, loops, functions, modules, dates, math, JSON, regular expressions, exceptions, input, and virtual environments. |
| [Python classes and OOP](07-python-oop/README.md) | Classes, objects, initialization, `self`, properties, class and magic methods, inheritance, polymorphism, encapsulation, and inner classes. |
| [Python file handling](08-file-handling/README.md) | Read, write, create, append, and safely delete files with paths, context managers, and explicit encodings. |
| [Python modules and standard library](09-python-modules/README.md) | Imports, built-in modules, PIP, random, requests, statistics, math, and complex math. |
| [NumPy, Pandas, and SciPy](10-data-libraries/README.md) | Numerical arrays, DataFrames, scientific statistics, and a reproducible analysis flow. |
| [Python Matplotlib tutorial](11-matplotlib/README.md) | Setup, pyplot, plotting, markers, lines, labels, grids, subplots, scatter, bars, histograms, and pie charts. |
| [Python machine learning](12-machine-learning/README.md) | Descriptive statistics, distributions, regression, scaling, train/test, classification, trees, clustering, model evaluation, bagging, cross-validation, ROC/AUC, KNN, and grid search. |
| [Python data structures and algorithms](13-data-structures-algorithms/README.md) | Arrays, stacks, queues, linked lists, hash tables, trees, BST/AVL, graphs, searching, and bubble, selection, insertion, quick, counting, radix, and merge sort. |
| [Python and MySQL](14-python-mysql/README.md) | Database setup, schemas, tables, CRUD, filtering, sorting, limits, parameterized queries, and joins. Requires a database you control and environment-based credentials. |
| [Python and MongoDB](15-python-mongodb/README.md) | Database and collection setup, document CRUD, find/query, sort, limit, and safe cleanup. Requires a local or authorized development database. |
| [Python Django web development](16-django-web/README.md) | Create a Django project/app, route URLs, implement views, and continue to models, forms, and secure settings. |
| [Python reference and practice](17-python-reference-practice/README.md) | Built-in and module references, glossary, examples, exercises, interview practice, study plan, compiler concepts, and safe local-server guidance. |

Optional dependencies for these tracks are separated from the core install: `requirements-data-science.txt`, `requirements-databases.txt`, and `requirements-web.txt`. Read a track guide before installing packages or connecting to an external service.

## Quickstart

1. **Clone the repository**

   ```bash
   git clone https://github.com/YOUR_GITHUB_USERNAME/python-data-science-machine-learning-course.git
   cd python-data-science-machine-learning-course
   ```

2. **Create and activate a virtual environment**

   ```bash
   python -m venv .venv
   ```

   Windows PowerShell: `.venv\Scripts\Activate.ps1`  
   macOS/Linux: `source .venv/bin/activate`

3. **Install dependencies and start learning**

   ```bash
   python -m pip install --upgrade pip
   pip install -r requirements.txt
   ```

   Run your first step-by-step lesson:

   ```bash
   python 01-python-core/01-environment-and-first-program/lesson.py
   ```

## Repository structure

```text
.
├── 01-python-core/
│   ├── README.md
│   ├── 01-environment-and-first-program/
│   │   ├── README.md
│   │   └── lesson.py
│   ├── 02-types-and-data-structures/
│   │   ├── README.md
│   │   └── lesson.py
│   ├── 03-control-flow-and-iteration/
│   │   ├── README.md
│   │   └── lesson.py
│   ├── 04-functions-and-modules/
│   │   ├── README.md
│   │   └── lesson.py
│   └── 05-classes-and-oop/
│       ├── README.md
│       └── lesson.py
├── 02-data-analysis/
│   ├── README.md
│   ├── 01-numpy-arrays/
│   │   ├── README.md
│   │   └── lesson.py
│   ├── 02-pandas-dataframes/
│   │   ├── README.md
│   │   └── lesson.py
│   ├── 03-data-cleaning/
│   │   ├── README.md
│   │   └── lesson.py
│   └── 04-vectorization-and-feature-prep/
│       ├── README.md
│       └── lesson.py
├── 03-visualization/
│   ├── README.md
│   ├── 01-matplotlib-fundamentals/
│   │   ├── README.md
│   │   └── lesson.py
│   ├── 02-seaborn-statistical-plots/
│   │   ├── README.md
│   │   └── lesson.py
│   ├── 03-exploratory-data-analysis/
│   │   ├── README.md
│   │   └── lesson.py
│   └── 04-interactive-plotly/
│       ├── README.md
│       └── lesson.py
├── 04-machine-learning/
│   ├── README.md
│   ├── 01-train-test-split-and-preprocessing/
│   │   ├── README.md
│   │   └── lesson.py
│   ├── 02-regression/
│   │   ├── README.md
│   │   └── lesson.py
│   ├── 03-classification/
│   │   ├── README.md
│   │   └── lesson.py
│   ├── 04-clustering/
│   │   ├── README.md
│   │   └── lesson.py
│   ├── 05-model-evaluation-and-cross-validation/
│   │   ├── README.md
│   │   └── lesson.py
│   └── 06-hyperparameter-tuning/
│       ├── README.md
│       └── lesson.py
├── 05-production/
│   ├── README.md
│   ├── 01-pytorch-tensors-and-training/
│   │   ├── README.md
│   │   └── lesson.py
│   ├── 02-save-and-load-models/
│   │   ├── README.md
│   │   └── lesson.py
│   ├── 03-onnx-model-export/
│   │   ├── README.md
│   │   └── lesson.py
│   ├── 04-fastapi-model-service/
│   │   ├── README.md
│   │   └── lesson.py
│   └── 05-streamlit-model-demo/
│       ├── README.md
│       └── lesson.py
├── 06-python-language/
│   ├── README.md
│   └── topics/<topic-project>/{README.md, main.py}
├── 07-python-oop/
│   ├── README.md
│   └── topics/<topic-project>/{README.md, main.py}
├── 08-file-handling/
│   ├── README.md
│   └── topics/<topic-project>/{README.md, main.py}
├── 09-python-modules/
│   ├── README.md
│   └── topics/<topic-project>/{README.md, main.py}
├── 10-data-libraries/
│   ├── README.md
│   └── topics/<topic-project>/{README.md, main.py}
├── 11-matplotlib/
│   ├── README.md
│   └── topics/<topic-project>/{README.md, main.py}
├── 12-machine-learning/
│   ├── README.md
│   └── topics/<topic-project>/{README.md, main.py}
├── 13-data-structures-algorithms/
│   ├── README.md
│   └── topics/<topic-project>/{README.md, main.py}
├── 14-python-mysql/
│   ├── README.md
│   └── topics/<topic-project>/{README.md, main.py}
├── 15-python-mongodb/
│   ├── README.md
│   └── topics/<topic-project>/{README.md, main.py}
├── 16-django-web/
│   ├── README.md
│   └── topics/<topic-project>/{README.md, main.py}
├── 17-python-reference-practice/
│   ├── README.md
│   └── topics/<topic-project>/{README.md, main.py}
├── requirements.txt
├── requirements-data-science.txt
├── requirements-databases.txt
├── requirements-web.txt
├── requirements-deep-learning.txt
├── CONTRIBUTING.md
└── LICENSE
```

Every core phase has an overview, and every core lesson has a detailed `README.md` and runnable `lesson.py`. Every supplementary topic is its own project with a detailed `README.md` and runnable `main.py`. Optional PyTorch and ONNX dependencies are kept out of the default install; see those lessons before installing them.

## How to use the lessons

Start with Phase 1 if you are new to Python. Each lesson is self-contained, but the phases build on one another. Read the lesson's `README.md`, follow its numbered steps in `lesson.py`, run the script from the repository root, and complete the practice task. Examples use small generated or built-in datasets so you can focus on concepts.

## How to contribute

Issues and pull requests are welcome from beginners and experienced developers alike. You can improve explanations, fix a typo, add tests, contribute an exercise, or suggest a project. Please:

1. Open or find an issue to discuss substantial changes.
2. Fork the repository and make a focused branch with a clear change.
3. Keep examples reproducible, beginner-friendly, and runnable; avoid committing generated datasets or build artifacts.
4. Run `ruff check .` and `pytest` when relevant, then submit a pull request describing what changed and how you checked it.

Helpful issues, thoughtful reviews, and useful pull requests make the lessons better for everyone. If this course helps you, consider starring it and sharing it with another learner.

See [CONTRIBUTING.md](CONTRIBUTING.md) for the full contribution guide.

## Star history

Replace `YOUR_GITHUB_USERNAME` below with the repository owner's GitHub username after publishing:

[![Star History Chart](https://api.star-history.com/svg?repos=YOUR_GITHUB_USERNAME/python-data-science-machine-learning-course&type=Date)](https://star-history.com/#YOUR_GITHUB_USERNAME/python-data-science-machine-learning-course&Date)

## License

This course is free and open source under the [MIT License](LICENSE).
