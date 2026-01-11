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
```

## Usage

To make program reproducible, simply import the package and add `seed_everything()`.

1. Seed settings only:

    ```python
    from seed_everything import seed_everything

    seed_everything(any_seed_you_like)
    ```

1. Strict deterministic:

    ```python
    from seed_everything import seed_everything

    seed_everything(random_seed=any_seed_you_like, use_deterministic=True)
    ```

    Note that strict mode may lower efficiency, even preformance.

## Disclaimer

This package sets random seeds and optional framework flags.
Full determinism depends on hardware, drivers, libraries, and operators,
and is not guaranteed by this function.
