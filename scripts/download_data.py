#!/usr/bin/env python3
"""
Download open data for the paper: Enterprise digitalization, environmental
performance, and TFP in heavily polluting firms (China A-shares).

Uses AKShare only (open data). Saves to data/raw/.

Usage:
  pip install akshare pandas tqdm
  python scripts/download_data.py                    # full: 2015-2023, all heavy-pollution firms
  python scripts/download_data.py --sample 20        # quick: 20 firms, 2 years
  python scripts/download_data.py --years 2018 2022  # custom year range
"""

import argparse
import os
import sys
import time
from pathlib import Path

import pandas as pd
# Heavily polluting industries (环保核查行业分类): keywords to match 所处行业 from East Money
HEAVY_POLLUTION_KEYWORDS = [
    "火电", "电力", "钢铁", "水泥", "电解铝", "煤炭", "冶金", "化工", "石化",
    "建材", "造纸", "酿造", "酿酒", "制药", "医药制造", "发酵", "纺织", "制革",
    "有色", "石油", "化学", "塑料", "橡胶", "化纤", "印染", "皮革", "农药",
    "焦化", "矿采", "采矿", "热力", "燃气", "非金属", "黑色金属", "有色金属",
]

def project_root():
    return Path(__file__).resolve().parents[1]

def raw_dir():
    d = project_root() / "data" / "raw"
    d.mkdir(parents=True, exist_ok=True)
    return d

def _ensure_akshare():
    try:
        import akshare as ak
        return ak
    except ImportError:
        print("Install akshare: pip install akshare", file=sys.stderr)
        sys.exit(1)

def download_yjbb(ak, years, out_dir):
    """Download 业绩报表 (annual performance) for each year. Has 营业总收入, 所处行业, 股票代码."""
    out_dir = Path(out_dir)
    all_dfs = []
    for year in years:
        date = f"{year}1231"
        try:
            df = ak.stock_yjbb_em(date=date)
            df["report_date"] = date
            df["year"] = year
            all_dfs.append(df)
            f = out_dir / f"yjbb_{year}.csv"
            df.to_csv(f, index=False, encoding="utf-8-sig")
            print(f"  Saved {f.name} ({len(df)} rows)")
        except Exception as e:
            print(f"  Warning: {date} failed: {e}")
        time.sleep(0.5)
    if not all_dfs:
        return None
    return pd.concat(all_dfs, ignore_index=True)

def is_heavy_pollution(industry_str):
    if pd.isna(industry_str) or industry_str is None:
        return False
    s = str(industry_str).strip()
    return any(kw in s for kw in HEAVY_POLLUTION_KEYWORDS)

def get_heavy_pollution_codes(df_yjbb):
    """From yjbb dataframe, filter by 所处行业 and return set of 股票代码."""
    if df_yjbb is None or df_yjbb.empty:
        return set()
    if "所处行业" not in df_yjbb.columns:
        return set()
    mask = df_yjbb["所处行业"].apply(is_heavy_pollution)
    codes = set(df_yjbb.loc[mask, "股票代码"].astype(str).str.zfill(6).unique())
    return codes

def code_to_sina(stock_code):
    """Convert 6-digit code to Sina format: sh6xxxxx or sz0xxxxx/sz3xxxxx."""
    code = str(stock_code).zfill(6)
    if code.startswith("6"):
        return f"sh{code}"
    return f"sz{code}"

def download_financials_sina(ak, stock_code, out_dir, symbol="资产负债表"):
    """Download one balance sheet or income statement. Returns DataFrame or None."""
    sina_code = code_to_sina(stock_code)
    try:
        df = ak.stock_financial_report_sina(stock=sina_code, symbol=symbol)
        return df
    except Exception as e:
        return None

def download_panel_financials(ak, codes, years, out_dir, sample=None):
    """For each stock in codes, download 资产负债表 and 利润表; build panel."""
    out_dir = Path(out_dir)
    codes = list(codes)
    if sample and sample < len(codes):
        codes = codes[:sample]
    balance_list = []
    income_list = []
    for i, code in enumerate(codes):
        sina = code_to_sina(code)
        for name, symbol in [("balance", "资产负债表"), ("income", "利润表")]:
            try:
                df = ak.stock_financial_report_sina(stock=sina, symbol=symbol)
                df["stock_code"] = code
                if name == "balance":
                    balance_list.append(df)
                else:
                    income_list.append(df)
            except Exception as e:
                pass
            time.sleep(0.3)
        if (i + 1) % 10 == 0:
            print(f"  Financials: {i+1}/{len(codes)} stocks")
    if balance_list:
        pd.concat(balance_list, ignore_index=True).to_csv(
            out_dir / "balance_sheet_sina.csv", index=False, encoding="utf-8-sig"
        )
        print(f"  Saved balance_sheet_sina.csv ({len(balance_list)} stocks)")
    if income_list:
        pd.concat(income_list, ignore_index=True).to_csv(
            out_dir / "income_statement_sina.csv", index=False, encoding="utf-8-sig"
        )
        print(f"  Saved income_statement_sina.csv ({len(income_list)} stocks)")

def main():
    parser = argparse.ArgumentParser(description="Download open data for digitalization-TFP paper")
    parser.add_argument("--years", nargs="*", type=int, default=None,
                        help="Year range, e.g. 2018 2022. Default: 2015 2016 2017 2018 2019 2020 2021 2022 2023")
    parser.add_argument("--sample", type=int, default=None,
                        help="If set, only download financials for this many heavy-pollution firms (for testing)")
    args = parser.parse_args()

    years = args.years if args.years else [2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022, 2023]
    out = raw_dir()
    print("Using AKShare (open data). Output dir:", out)

    ak = _ensure_akshare()

    # 1) Annual performance report (has 营业总收入, 所处行业, 股票代码)
    print("\n1) Downloading annual performance (stock_yjbb_em)...")
    df_yjbb = download_yjbb(ak, years, out)
    if df_yjbb is not None:
        df_yjbb.to_csv(out / "yjbb_all.csv", index=False, encoding="utf-8-sig")
        print(f"   Combined: yjbb_all.csv ({len(df_yjbb)} rows)")

    # 2) Heavy-pollution firm codes
    codes = get_heavy_pollution_codes(df_yjbb)
    print(f"\n2) Heavy-pollution firms (industry filter): {len(codes)} unique codes")
    if codes:
        pd.Series(sorted(codes)).to_csv(out / "heavy_pollution_stock_codes.csv", index=False, header=["stock_code"])
        print("   Saved heavy_pollution_stock_codes.csv")

    # 3) Balance sheet & income statement for TFP (per-stock, multi-year in one table)
    if codes:
        print("\n3) Downloading balance sheet & income statement (Sina)...")
        download_panel_financials(ak, codes, years, out, sample=args.sample)

    print("\nDone. Raw data in data/raw/")
    print("Next: build TFP and digitalization in data/processed/ (see data_数据方案.md)")

if __name__ == "__main__":
    main()
