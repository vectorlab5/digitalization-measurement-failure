digitalization-measurement-failure
==================================

This repository contains the **Python source code and data-processing pipeline**
for firm-level digitalization and performance analysis. It is designed as a
clean, reusable codebase for:

- downloading and organizing open financial data,
- building a firm–year panel,
- running panel regressions,
- running a controlled experiment on proxy designs.

No manuscript source, LaTeX, or submission materials are stored here. This
repository is strictly for code and data workflows.

Contents
--------

- `src/`: reusable Python package with:
  - path utilities for project-relative file handling,
  - data loading and panel construction logic,
  - regression routines for firm-level panel analysis,
  - a controlled experiment module illustrating same-source proxy bias.
- `scripts/`: thin command-line wrappers around the `src/` package:
  - `download_data.py`: fetch and prepare the required input datasets,
  - `analyze_data.py`: build the main panel and compute descriptives,
  - `run_regressions.py`: run the core regression specifications.
- `data/`: open raw and processed data (see `data/README.md` for details).
- `requirements-data.txt`: minimal Python dependencies for running the project.

Getting started
---------------

1. **Create and activate a virtual environment**

```bash
python -m venv .venv
source .venv/bin/activate  # on Windows: .venv\\Scripts\\Activate.ps1
```

2. **Install dependencies**

```bash
pip install -r requirements-data.txt
```

3. **Download and prepare data**

```bash
python scripts/download_data.py
```

4. **Build panel and descriptives**

```bash
python scripts/analyze_data.py
```

5. **Run regressions**

```bash
python scripts/run_regressions.py
```

6. **Run the controlled experiment (optional)**

```bash
python scripts/controlled_experiment.py
```

Data and outputs
----------------

All intermediate and final outputs are written under the `data/` directory
next to the code. Typical subdirectories include:

- `data/raw/`: raw input files downloaded by `download_data.py`,
- `data/processed/`: cleaned panels, descriptives, and experiment outputs.

With a fresh clone of the repository, you can fully reproduce the analysis by
re-running the scripts above.

