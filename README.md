# Advent of Code 2025

My solutions for [Advent of Code 2025](https://adventofcode.com/2025) using Python, [marimo](https://marimo.io/), and [uv](https://docs.astral.sh/uv/).

## Progress

- [x] Day 1
- [x] Day 2
- [x] Day 3
- [ ] Day 4
- [ ] Day 5
- [ ] Day 6
- [ ] Day 7
- [ ] Day 8
- [ ] Day 9
- [ ] Day 10
- [ ] Day 11
- [ ] Day 12


Note: No input file is upload per the rules of the contest so the code will be looking for *_input.txt files that do not exist in the repote repo.

## Tech Stack

- **Python 3.12+**: Modern Python features
- **marimo**: Interactive notebooks for exploratory problem-solving with reactive execution
- **uv**: Lightning-fast Python package installer and resolver for dependency management

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
   uv add [module]
   ```
   
   or

   ```bash
   uv pip install -e .
   ```

## Running Solutions

Each day's solution is a marimo notebook that can be run interactively:

```bash
marimo edit day_01.py
```
or

```bash
uv run marimo edit day_01.py
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
