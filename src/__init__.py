"""
Top-level package for the digitalization–measurement–failure codebase.

This package exposes a small, well-structured API around three things:

1. Data loading and preprocessing for the open Chinese A-share firm data.
2. Panel construction and descriptive statistics for the empirical illustration.
3. Regression and synthetic experiments that mirror the paper's methodology.

The public submodules are:

- ``src.paths``: project-root aware path helpers.
- ``src.data_panel``: functions to build the firm-year panel and compute descriptives.
- ``src.regressions``: panel regression routines used for the main tables.
- ``src.synthetic_experiment``: the controlled synthetic experiment.
"""

