#!/usr/bin/env bash
# Run data analysis, regressions, and compile the paper.
set -e
cd "$(dirname "$0")"
echo "Running analyze_data.py ..."
python3 scripts/analyze_data.py
echo "Running run_regressions.py ..."
python3 scripts/run_regressions.py
echo "Compiling main.tex ..."
pdflatex -interaction=nonstopmode main.tex >/dev/null 2>&1
pdflatex -interaction=nonstopmode main.tex 2>&1 | grep -E "Output written|Error|Warning.*Ref"
echo "Done. See main.pdf"
