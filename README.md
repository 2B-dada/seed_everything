# seed_everything

A lightweight Python utility to **fully control randomness** across Python, NumPy, and PyTorch for reproducible experiments.

This package is especially useful for:
- Machine learning & deep learning experiments
- Scientific computing
- Research code that requires strict reproducibility

---

## ✨ Features

- Set random seeds for:
  - Python built-in `random`
  - NumPy
  - PyTorch (CPU & CUDA, if available)
- Gracefully handles missing PyTorch
- Minimal, dependency-light design
- Tested with `pytest`

---

## 📦 Installation

### Install from GitHub

```bash
pip install git+https://github.com/2B-dada/seed_everything.git
