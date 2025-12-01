# Advent of Code 2025

My solutions for [Advent of Code 2025](https://adventofcode.com/2025) using Python, [marimo](https://marimo.io/), and [uv](https://docs.astral.sh/uv/).

## Tech Stack

- **Python 3.12+**: Modern Python features
- **marimo**: Interactive notebooks for exploratory problem-solving with reactive execution
- **uv**: Lightning-fast Python package installer and resolver for dependency management

## Project Structure

```
.
├── day_01.py          # Day 1 solution (marimo notebook)
├── day_01_input.txt   # Day 1 puzzle input
├── pyproject.toml     # Project configuration
└── uv.lock           # Locked dependencies
```

## Setup

1. Install [uv](https://docs.astral.sh/uv/getting-started/installation/):
   ```bash
   curl -LsSf https://astral.sh/uv/install.sh | sh
   ```

2. Create and activate virtual environment:
   ```bash
   uv venv
   source .venv/bin/activate  # On macOS/Linux
   ```

3. Install dependencies:
   ```bash
   uv pip install -e .
   ```

## Running Solutions

Each day's solution is a marimo notebook that can be run interactively:

```bash
marimo edit day_01.py
```

This opens the notebook in your browser with a reactive interface where cells automatically re-execute when dependencies change.

Alternatively, run as a script:

```bash
marimo run day_01.py
```

Or execute directly with Python:

```bash
python day_01.py
```

## Why marimo?

marimo notebooks offer several advantages for AoC:

- **Reactive execution**: Cells automatically update when you change code
- **Interactive exploration**: Perfect for debugging and testing different approaches
- **Pure Python**: Notebooks are `.py` files, work with version control and standard tools
- **No hidden state**: Execution order is deterministic, preventing notebook bugs

## Why uv?

uv provides:

- **Speed**: 10-100x faster than pip for installing packages
- **Reliability**: Consistent dependency resolution with lock files
- **Simplicity**: Single tool for environment and dependency management

## Progress

- [x] Day 1
- [ ] Day 2
- [ ] Day 3
- ...