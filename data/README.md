# Data (open data only)

Raw and processed data for the paper *Enterprise digitalization, environmental performance, and TFP*.

## Raw data (`data/raw/`)

Downloaded via `scripts/download_data.py` (AKShare, open data):

| File | Description |
|------|-------------|
| `yjbb_YYYY.csv` | Annual performance report (业绩报表) for year YYYY: 股票代码, 股票简称, 营业总收入, 净利润, 所处行业, etc. |
| `yjbb_all.csv` | Concatenation of all years (for the years you ran). |
| `heavy_pollution_stock_codes.csv` | List of A-share stock codes in heavily polluting industries (industry filter applied). |
| `balance_sheet_sina.csv` | Balance sheet (资产负债表) from Sina Finance: 总资产, 固定资产, etc. by 报告日 and stock. |
| `income_statement_sina.csv` | Income statement (利润表) from Sina Finance: 营业收入, etc. by 报告日 and stock. |

## How to download (full or custom)

```bash
# From project root
pip install -r requirements-data.txt

# Full: 2015–2023, all heavy-pollution firms (takes ~30–60 min)
python scripts/download_data.py

# Custom years and/or limit number of firms for testing
python scripts/download_data.py --years 2018 2019 2020 2021 2022 --sample 50
```

## Processed data (`data/processed/`)

Built by `scripts/analyze_data.py` from raw:

| File | Description |
|------|-------------|
| `panel_heavy_pollution.csv` | Firm-year panel: stock_code, year, name, industry, revenue, net_income, roe, gross_margin, total_assets, fixed_assets, size_log, roa. |
| `descriptives_for_paper.csv` | Summary stats (N, K, year range, mean/SD of revenue, assets, ROE) for the paper. |

Next steps: add TFP (from LP/OP using revenue, fixed_assets, labor if available), digitalization index (from CNINFO annual report text), and environmental/patent variables; then run main regressions and update Tables 1--2. See `data_数据方案.md` and Methods in the paper.
