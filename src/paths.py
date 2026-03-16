"""
Path utilities for the digitalization–measurement–failure project.

All modules should import project- and data-path helpers from here instead of
constructing ad-hoc relative paths. This keeps the codebase robust when moved
or installed as a package.
"""
from __future__ import annotations

from pathlib import Path


def project_root() -> Path:
    """Return the absolute path to the project root."""
    return Path(__file__).resolve().parents[1]


def raw_data_dir() -> Path:
    """Return the directory containing raw data files."""
    d = project_root() / "data" / "raw"
    d.mkdir(parents=True, exist_ok=True)
    return d


def processed_data_dir() -> Path:
    """Return the directory containing processed data files."""
    d = project_root() / "data" / "processed"
    d.mkdir(parents=True, exist_ok=True)
    return d


def regression_results_dir() -> Path:
    """Return the directory where regression outputs should be written."""
    d = processed_data_dir() / "regression_results"
    d.mkdir(parents=True, exist_ok=True)
    return d

